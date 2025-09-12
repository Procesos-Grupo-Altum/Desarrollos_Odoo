# -*- conding:utf-8 -*-

from odoo import fields, models, api

class ResPartnerCategory(models.Model):
    _inherit = 'res.partner.category'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0, )
    color = fields.Integer(string='Índice de Colores', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre de etiqueta', store=True, required=True, copied=True, tracking=0, )
    parent_path = fields.Char(string='Ruta padre', index=True, store=True, copied=True, tracking=0, )
