# -*- coding:utf-8 -*-

from odoo import fields, models, api

class QuestionOption(models.Model):
    _name = 'question_option'
    

    name = fields.Text(string="Nombre")
    value = fields.Text(string="Valor")
    parent = fields.Text(string="Padre")
    active = fields.Boolean(string="Activo", default=True)
    question_option_group_id = fields.Many2one(comodel_name='question_option_group', string="Grupo de opciones")
