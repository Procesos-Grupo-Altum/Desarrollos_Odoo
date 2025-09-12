# -*- coding:utf-8 -*-

from odoo import fields, models, api

class QuestionAnswerGroupNews(models.Model):
    _name = 'question_answer_group_news'

    question_answer_group_id = fields.Many2one("question_answer_group", string="Grupo de Respuestas")
    summary = fields.Text(string='Resumen')
    image = fields.Char(string='Imagen')
    user_id = fields.Many2one('user', string='Usuario')
    active = fields.Boolean(string='Activo', default=True)