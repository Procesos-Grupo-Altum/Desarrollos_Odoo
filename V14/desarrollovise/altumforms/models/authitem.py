# -*- coding:utf-8 -*-

from odoo import fields, models, api

class AuthItem(models.Model):
    _name = 'authitem'
    _description = 'Tipo de Usuario'

    name = fields.Char(string="Nombre")
    type = fields.Integer(string="Tipo")
    description = fields.Char(string="Descripción")
    bizrule = fields.Char()
    data = fields.Char()