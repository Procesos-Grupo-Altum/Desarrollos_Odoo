# -*- conding:utf-8 -*-

from odoo import fields, models, api


class AreasVise(models.Model):
    _name = 'vise.areas'

    name = fields.Char(string="Nombre Area")
    active = fields.Boolean(string="Activo", default=True, copy=False)
    sequence = fields.Text(string="Orden en flujo", index=True)

    _sql_constraints = [
        ('vise_areas_code_uniq', 'unique(code)', 'La sigla del área debe ser única.'),
    ]
