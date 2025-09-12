# -*- coding:utf-8 -*-

from odoo import fields, models, api

class Compania(models.Model):
    _name = 'company'

    name = fields.Char(string="Nombre", required=True)
    nit = fields.Char(string="NIT", required=True)
    short_name = fields.Char(string="Nombre Corto")
    address = fields.Char(string="Dirección")
    phone = fields.Char(string="Teléfono")
    email = fields.Char(string="Email")
    active = fields.Boolean(string="Activo", default=True)
    logo = fields.Binary(string="Logo")
    country_id = fields.Integer(string="Pais")

