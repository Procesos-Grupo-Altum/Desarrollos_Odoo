# -*- coding:utf-8 -*-

from odoo import fields, models, api

class QuestionOptionGroup(models.Model):
    _name = 'question_option_group'

    code = fields.Char(string="Codigo")
    name = fields.Char(string="Nombre")
    google_path = fields.Char(string="Ruta en Google")
    master = fields.Selection([('0', 'No'), ('1', 'Si')], string="Maestro", default='0')
    company_id = fields.Many2one(comodel_name='company', string="Compañía", required=True)
    is_list = fields.Selection([('0', 'No'), ('1', 'Si')], string="Es lista", default='0')
    active = fields.Boolean(string="Activo", default=True)