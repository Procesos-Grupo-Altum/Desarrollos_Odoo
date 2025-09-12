# -*- coding:utf-8 -*-

from odoo import fields, models, api

class Ciudad(models.Model):
    _name = 'city'

    name = fields.Char(string="Nombre")
    country =  fields.Char(string="País")
    state =  fields.Char(string="Estado")
    regional =  fields.Char(string="Región")
    country_id = fields.Integer(string="País")