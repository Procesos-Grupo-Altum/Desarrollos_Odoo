# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)
from odoo import fields, models, api
from odoo.tools.safe_eval import safe_eval

class TablaRetencion(models.Model):
    _name = "gestion.trd"
    _description = "Tablas de Retención Documental"
    _order = "sequence, dep_grupo, ser_grupo, sub_grupo, name"
    _rec_name = "name"

    codigo_formato = fields.Char(string="Código de Formato", index=True)
    name = fields.Char(string="Nombre de la TRD", index=True)
    active = fields.Boolean(string="Activo", default=True)
    sequence = fields.Integer(string="Secuencia", default=1)
    order = fields.Boolean(string="Ordenar por Fecha", default=False)
    date_field_id = fields.Many2one(
        'ir.model.fields',
        string='Fechas',
        store=True,
    )
    adjunto_field_id = fields.Many2one(
        'ir.model.fields',
        string='Adjuntos',
        store=True,
    )
    res_model = fields.Char(string="Modelo del Recurso", index=True)
    domain = fields.Char(string="Valor del dominio",
                         index=True,
                         )


    soporte_ids = fields.Many2many(
        'gestion.soporte',
        relation='gestion_trd_soporte_rel',
        column1='trd_id',
        column2='soporte_id',
        string='Tipo de Soporte',
        domain=[('active', '=', True)],
        context={'default_active': True},
    )

    file_extension_id = fields.Many2one(
        'file.extension',
        string='Extensión del Archivo',
        ondelete="restrict",
    )

    iss_id = fields.Many2one(
        'gestion.iss',
        string="ISS",
        ondelete="cascade",)

    codigo_dependencia = fields.Char(
        string="CD",
        related= "iss_id.codigo_depen",
        store=True,
    )

    codigo_serie = fields.Char(
        string="SE",
        related="iss_id.codigo_serie",
        store=True,
    )

    nombre_serie = fields.Char(
        string="Nombre de la Serie",
        related= "iss_id.nombre_serie",
        store=True,
    )

    codigo_subserie = fields.Char(
        string="SB",
        related="iss_id.codigo_subserie",
        store=True,
    )

    dep_grupo = fields.Char(
        string="Dependencia (grupo)",
        compute="_compute_dep_grupo",
        store=True,
    )
    ser_grupo = fields.Char(
        string="Serie (grupo)",
        compute="_compute_ser_grupo",
        store=True,
    )
    sub_grupo = fields.Char(
        string="Subserie (grupo)",
        compute="_compute_sub_grupo",
        store=True,
    )

    documentos_ids = fields.One2many(
        'relacion.trd',
        'trd_id',
        string='Documentos Relacionados',
        compute='_compute_documentos_ids',
        store = True
    )



    @api.depends('codigo_dependencia', 'iss_id.nombre_depen')
    def _compute_dep_grupo(self):
        for rec in self:
            dep_name = ''
            if rec.iss_id and hasattr(rec.iss_id, 'nombre_depen'):
                val = rec.iss_id.nombre_depen
                # Si es many2one, usamos display_name; si es char/text, usamos el valor
                if isinstance(val, models.BaseModel):
                    dep_name = val.display_name or ''
                else:
                    dep_name = val or ''
            rec.dep_grupo = "%s - %s" % (rec.codigo_dependencia or '', dep_name)

    @api.depends('codigo_serie', 'nombre_serie')
    def _compute_ser_grupo(self):
        for rec in self:
            rec.ser_grupo = "%s - %s" % (
                rec.codigo_serie or '',
                rec.nombre_serie or '',
            )

    @api.depends('codigo_subserie', 'iss_id.nombre_subserie')
    def _compute_sub_grupo(self):
        for rec in self:
            sub_name = ''
            if rec.iss_id and hasattr(rec.iss_id, 'nombre_subserie'):
                val = rec.iss_id.nombre_subserie
                if isinstance(val, models.BaseModel):
                    sub_name = val.display_name or ''
                else:
                    sub_name = val or ''
            rec.sub_grupo = "%s - %s" % (rec.codigo_subserie or '', sub_name)

    @api.depends('res_model', 'domain', 'date_field_id', 'adjunto_field_id', 'order')
    def _compute_documentos_ids(self):
        """
        Método corregido que ACTUALIZA en lugar de ELIMINAR+CREAR
        Esto evita conflictos con restricciones FK en attachment_id
        """
        IrModel = self.env['ir.model']
        IrFilters = self.env['ir.filters']
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url', '')

        for record in self:
            # -----------------------------
            # 0) Validaciones iniciales
            # -----------------------------
            if not record.res_model:
                # Marcar como inactivos en lugar de eliminar
                if record.documentos_ids:
                    record.documentos_ids.write({'activo': False})
                continue

            if not (record.date_field_id and record.date_field_id.name and
                    record.adjunto_field_id and record.adjunto_field_id.name):
                if record.documentos_ids:
                    record.documentos_ids.write({'activo': False})
                continue

            # -----------------------------
            # 1) Modelo y campos dinámicos
            # -----------------------------
            modelo = IrModel.search([('model', '=', record.res_model)], limit=1)
            if not modelo:
                if record.documentos_ids:
                    record.documentos_ids.write({'activo': False})
                continue

            model_id = modelo.id
            TargetModel = self.env[record.res_model]

            campo_fecha = record.date_field_id.name
            campo_adjunto = record.adjunto_field_id.name

            # -----------------------------
            # 2) Orden dinámico
            # -----------------------------
            if campo_fecha and campo_fecha in TargetModel._fields:
                ordenar = f"{campo_fecha} asc, id asc" if record.order else f"{campo_fecha} desc, id desc"
            else:
                if 'write_date' in TargetModel._fields:
                    ordenar = "write_date asc, id asc" if record.order else "write_date desc, id desc"
                elif 'create_date' in TargetModel._fields:
                    ordenar = "create_date asc, id asc" if record.order else "create_date desc, id desc"
                else:
                    ordenar = "id asc" if record.order else "id desc"

            # -----------------------------
            # 3) Construcción del dominio
            # -----------------------------
            try:
                f = IrFilters.new({
                    'domain': record.domain or '[]',
                    'model_id': model_id,
                    'user_id': self.env.user.id,
                })
                dom = f._get_eval_domain()
                dom = list(dom) if isinstance(dom, (list, tuple)) else []
            except Exception as e:
                _logger.error(f"Error evaluando dominio en TRD {record.id}: {e}")
                if record.documentos_ids:
                    record.documentos_ids.write({'activo': False})
                continue

            # Siempre exigir que el campo de adjunto tenga valor
            dom.append((campo_adjunto, '!=', False))

            # -----------------------------
            # 4) Buscar registros
            # -----------------------------
            records = TargetModel.search(dom, limit=1000, order=ordenar)

            # -----------------------------
            # 5) Sincronización inteligente
            # -----------------------------

            # Paso A: Recopilar adjuntos esperados
            adjuntos_esperados = set()
            adjuntos_data = {}

            for record2 in records:
                x_fecha_val = False

                # Resolver fecha
                if campo_fecha and campo_fecha in record2._fields:
                    field_fecha = record2._fields[campo_fecha]
                    tipo = field_fecha.type

                    if tipo in ('date', 'datetime'):
                        x_fecha_val = record2[campo_fecha]
                    elif tipo == 'many2one':
                        rel = record2[campo_fecha]
                        if rel and 'valid_from' in rel._fields:
                            x_fecha_val = rel['valid_from']

                # Resolver adjuntos
                adj_val = record2[campo_adjunto]
                adjuntos = adj_val if hasattr(adj_val, '__iter__') else self.env['ir.attachment'].browse()

                if adj_val and not adjuntos:
                    adjuntos = adj_val

                for adj in adjuntos:
                    if not adj:
                        continue

                    x_document_url = False
                    if getattr(adj, 'website_url', False) and base_url:
                        x_document_url = base_url + adj.website_url

                    adjuntos_esperados.add(adj.id)
                    adjuntos_data[adj.id] = {
                        'model_id': model_id,
                        'attachment_id': adj.id,
                        'fecha_referencia': x_fecha_val,
                        'document_url': x_document_url,
                        'trd_id': record.id,
                        'activo': True,
                    }

            # Paso B: Obtener adjuntos existentes
            relaciones_existentes = record.documentos_ids
            adjuntos_existentes = {r.attachment_id.id: r for r in relaciones_existentes if r.attachment_id}

            # Paso C: Determinar operaciones
            adjuntos_crear = adjuntos_esperados - set(adjuntos_existentes.keys())
            adjuntos_actualizar = adjuntos_esperados & set(adjuntos_existentes.keys())
            adjuntos_desactivar = set(adjuntos_existentes.keys()) - adjuntos_esperados

            # Paso D: Construir comandos
            comandos = []

            # CREAR nuevos
            for att_id in adjuntos_crear:
                comandos.append((0, 0, adjuntos_data[att_id]))

            # ACTUALIZAR existentes
            for att_id in adjuntos_actualizar:
                relacion = adjuntos_existentes[att_id]
                comandos.append((1, relacion.id, adjuntos_data[att_id]))

            # DESACTIVAR obsoletos (no eliminar)
            for att_id in adjuntos_desactivar:
                relacion = adjuntos_existentes[att_id]
                comandos.append((1, relacion.id, {'activo': False}))

            # Paso E: Aplicar cambios
            if comandos:
                record.documentos_ids = comandos


class Soportes(models.Model):
    _name = "gestion.soporte"
    _description = "Soportes de Documentos"
    _order = "sequence, name"
    _rec_name = "abreviatura"

    codigo = fields.Char(string="Código de Soporte", index=True)
    name = fields.Char(string="Nombre del Soporte", index=True)
    active = fields.Boolean(string="Activo", default=True)
    sequence = fields.Integer(string="Secuencia", default=1)
    abreviatura = fields.Char(string="Abreviatura", index=True)


class FileExtension(models.Model):
    _name = 'file.extension'
    _description = 'Extensión de Archivo'

    name = fields.Char(string="Nombre")
    extension = fields.Char(string="Extensión")
    active = fields.Boolean(string="Activo", default=True)
    sequence = fields.Integer(string="Secuencia", default=1)

class RelacionTRDSoporte(models.Model):
    _name = 'relacion.trd'
    _description = 'Relación TRD'


    name = fields.Char(
        string='Descripción',
        store=True,
    )

    activo = fields.Boolean(
        string='Activo',
        store=True,
        copy=True,
        default=True,
    )

    calcula = fields.Char(
        string='Cálculo',
        store=True,
        copy=True,
    )

    document_url = fields.Char(
        string='URL del Documento',
        store=True,
        copy=True,
    )

    fecha_referencia = fields.Date(
        string='Fecha de Referencia',
        store=True,
        copy=True,
    )

    sequence = fields.Integer(
        string='Secuencia',
        store=True,
        copy=True,
        default=1,
    )



    trd_id = fields.Many2one(
        'gestion.trd',
        string='TRD',
        store=True,
    )

    model_id = fields.Many2one(
        'ir.model',
        string='Modelo',
        store=True,
    )

    attachment_id = fields.Many2one(
        'ir.attachment',
        string='Documentos',
        store=True,
        copy=True,
    )


