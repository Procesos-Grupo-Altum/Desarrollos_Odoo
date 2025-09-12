# -*- coding:utf-8 -*-

from odoo import fields, models, api

class Sector(models.Model):
    _name = 'sector'

    name = fields.Char(string="Nombre")