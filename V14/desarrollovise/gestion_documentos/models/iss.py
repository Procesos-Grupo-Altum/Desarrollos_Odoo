# -*- coding:utf-8 -*-
from Tools.scripts.dutree import store

from odoo import models, fields, api



class GestionIss(models.Model):
    _name = 'gestion.iss'
    _description = 'Índice de Series y Subseries Documentales (ISS)'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'codigo_principal, codigo_secundario'

    # ---- Clave y orden ----
    # ---- Campos de Llenado Humano ----
    sequence = fields.Integer(string='Secuencia', default=10)
    name = fields.Char(string='Nombre', compute='_compute_name', store=True)
    codigo_principal = fields.Char(string='Código General', compute='_compute_codigo_general', store=True)
    codigo_secundario = fields.Char(string='Código General', compute='_compute_codigo_secundario', store=True)
    disposicion_ag = fields.Integer(string='AG', store=True, default=0)
    disposicion_ac = fields.Integer(string='AC', store=True, default=0)


    disposicion_final_ids = fields.Many2many(
        comodel_name='gestion.disposicion.final',
        relation='gestion_iss_disposicion_final_rel',
        column1='iss_id',
        column2='disposicion_final_id',
        string='Disposiciones Finales'
    )

    reproduccion_tecnica = fields.Boolean(string='Reproducción Técnica del Papel', default=False)

    nombre_subserie = fields.Many2one(
        comodel_name='gestion.subserie',
        string='Nombre de la Subserie',)

    nombre_serie = fields.Char(
        string='Nombre de la Serie',
        related='nombre_subserie.serie_id.name',
        store=True, )

    codigo_subserie = fields.Char(
        string='Código de la Subserie',
        related='nombre_subserie.codigo',
        store=True,)

    codigo_serie = fields.Char(
        string='Código de la Serie',
        related='nombre_subserie.serie_id.codigo',
        store=True,)

    estado_serie = fields.Boolean(
        string='Estado de la Serie',
        related='nombre_subserie.serie_id.active',
        store=True,)

    cierre_exp = fields.Text(
        string="Cierre Exp.",
        related="nombre_subserie.cierre_expediente",
        store=True,
    )
    procedimiento = fields.Html(
        string="Procedimiento",
        related="nombre_subserie.procedimiento",
        store=True,
    )

    nombre_depen = fields.Many2one('gestion.dependencia',string='Nombre de la Dependencia',store=True,)
    codigo_depen = fields.Char(string='Código de la Dependencia', related='nombre_depen.codigo', store=True,)


    trd_ids = fields.One2many('gestion.trd', 'iss_id', string="Registros",)


    @api.depends('codigo_serie', 'codigo_subserie')
    def _compute_codigo_general(self):
        for rec in self:
            cs = (rec.codigo_serie or '').strip()
            csub = (rec.codigo_subserie or '').strip()
            rec.codigo_principal = f'{cs}.{csub}' if cs and csub else False

    @api.depends('codigo_depen','codigo_serie', 'codigo_subserie')
    def _compute_codigo_secundario(self):
        for rec in self:
            cs = (rec.codigo_serie or '').strip()
            csub = (rec.codigo_subserie or '').strip()
            cd = (rec.codigo_depen or '').strip()
            if cd:
                rec.codigo_secundario = f'{cd}.{cs}.{csub}' if cs and csub else cd
            else:
                rec.codigo_secundario = f'{cs}.{csub}' if cs and csub else False


    @api.depends('codigo_principal','codigo_principal','nombre_subserie')
    def _compute_name(self):
        for rec in self:
            sub_name = rec.nombre_subserie.display_name if rec.nombre_subserie else False
            partes = [p for p in [rec.codigo_secundario, sub_name] if p]
            rec.name = ' / '.join(partes) if partes else False



class DisposicionFinal(models.Model):
    _name = 'gestion.disposicion.final'
    _description = 'Disposiciones Finales'

    name = fields.Char(string='Nombre', required=True)
    code = fields.Char(string='Código', required=True)
    sequence = fields.Integer(string='Secuencia', default=1)
    active = fields.Boolean(string='Activo', default=True)
    description = fields.Text(string='Descripción', store=True,)