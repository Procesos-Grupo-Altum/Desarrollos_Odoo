# -*- coding: utf-8 -*-
from odoo import fields, models, api

class TablaRetencion(models.Model):
    _name = "gestion.trd"
    _description = "Tablas de Retención Documental"
    _order = "sequence, dep_grupo, ser_grupo, sub_grupo, name"
    _rec_name = "name"

    codigo_formato = fields.Char(string="Código de Formato", index=True)
    name = fields.Char(string="Nombre de la TRD", index=True)
    active = fields.Boolean(string="Activo", default=True)
    sequence = fields.Integer(string="Secuencia", default=1)

    res_model = fields.Char(string="Modelo del Recurso", index=True)
    domain = fields.Char(string="Valor del dominio", index=True)


    soporte_ids = fields.Many2many(
        'gestion.soporte',
        relation='gestion_trd_soporte_rel',
        column1='trd_id',
        column2='soporte_id',
        string='Tipo de Soporte',
        domain=[('active', '=', True)],
        context={'default_active': True},
    )

    soportes_relacionados_ids = fields.Many2many(
        'res.partner.id_number',
        relation='gestion_trd_res_partner_id_number_rel',
        column1='gestion_trd_id',
        column2='res_partner_id_number_id',
        string='Soportes Relacionados',

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