# -*- coding:utf-8 -*-

from odoo import fields, models, api

class Formulario(models.Model):
    _name = 'form'

    company_id = fields.Many2one(comodel_name="company", string="Empresa")
    code = fields.Char(string="Código")
    name = fields.Char(string="Nombre")
    version = fields.Char(string="Versión")
    email = fields.Char(string="Email")
    company = fields.Char(string="Compañía")
    partial_fill = fields.Selection(selection=[('0', 'No'), ('1', 'Si')], string="Llenado Parcial", default='0')
    monitor = fields.Selection(selection=[('0', 'No'), ('1', 'Si')], string="Monitoreo", default='0')
    monitor_color = fields.Char(string="Color Monitoreo")
    index_question_id = fields.Many2one(comodel_name="question", string="Pregunta Índice")
    has_news = fields.Selection(selection=[('0', 'No'), ('1', 'Si')], string="Tiene Novedades", default='0')
    portrait = fields.Selection(selection=[('0', 'No'), ('1', 'Si')], string="Retrato", default='1')
    enabled = fields.Selection(selection=[('0', 'No'), ('1', 'Si')], string="Habilitado", default='1')
    active = fields.Boolean(string="Activo", default=True)
    user_id = fields.Many2one(comodel_name="user",  string="Usuario Creador")

