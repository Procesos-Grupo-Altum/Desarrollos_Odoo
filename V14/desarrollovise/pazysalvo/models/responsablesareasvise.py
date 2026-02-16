# -*- conding:utf-8 -*-
from odoo import fields, models, api


class ResponsablesArea(models.Model):
    _name = 'responsables.areas.vise'
    _descripcion = 'Responsables Areas Vise'

    active = fields.Boolean(string="Activo", store=True, copied=True, default=True)
    name = fields.Many2one('vise.areas', string="Nombre Area", store=True)
    user_id = fields.Many2one('res.users', string="Usuario Responsable", store=True)
