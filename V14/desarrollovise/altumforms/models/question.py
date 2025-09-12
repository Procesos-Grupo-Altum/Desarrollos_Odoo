# -*- coding:utf-8 -*-

from odoo import fields, models, api

class Question(models.Model):
    _name = 'question'

    code = fields.Char(string="Codigo")
    name = fields.Char(string="Nombre")
    size = fields.Integer(string="Tamaño")
    vertical = fields.Selection([('0', 'No'), ('1', 'Si')], string="Vertical", default='0')
    order = fields.Integer(string="Orden")
    js = fields.Text(string="JS")
    options = fields.Text(string="Opciones")
    required = fields.Selection([('0', 'No'), ('1', 'Si')], string="Requerido", default='0')
    is_filter = fields.Selection([('0', 'No'), ('1', 'Si')], string="Es filtro", default='0')
    active = fields.Boolean(string="Activo", default=True)
    question_type_id = fields.Many2one(comodel_name='question_type', string="Tipo de pregunta", required=True)
    img_option_id = fields.Many2one(comodel_name='question_option', string="Opción imagen")
    cb_option_id = fields.Many2one(comodel_name='question_option', string="Opción checkbox")
    p_question_option_id = fields.Many2one(comodel_name='question_option', string="Opción padre")
    p_question_id = fields.Many2one(comodel_name='question', string="Opción padre")
    question_option_group_id = fields.Many2one(comodel_name='question_option_group', string="Grupo de opciones")