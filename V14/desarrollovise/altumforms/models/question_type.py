# -*- coding:utf-8 -*-

from odoo import fields, models, api

class QuestionType(models.Model):
    _name = 'question_type'

    name = fields.Char(string="Nombre")
    multiple = fields.Selection([('0', 'No'), ('1', 'Si')], string="Multiple", default='0')
    order = fields.Integer(string="Orden")
    visible = fields.Selection([('0', 'No'), ('1', 'Si')], string="Visible", default='1')
    active = fields.Boolean(string="Activo", default=True)