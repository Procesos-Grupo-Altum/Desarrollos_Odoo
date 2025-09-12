# -*- coding:utf-8 -*-

from odoo import fields, models, api

class AnswerReaded(models.Model):
    _name = 'answer_readed'

    question_answer_group_id = fields.Many2one('question_answer_group', string="Grupo de respuestas")
    user_id = fields.Many2one('user', string="Usuario")