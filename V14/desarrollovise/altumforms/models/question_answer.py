# -*- coding:utf-8 -*-

from odoo import fields, models, api

class QuestionAnswer(models.Model):
    _name = 'question_answer'

    question_answer_group_id = fields.Many2one('question_answer_group', string='Question Answer Group', required=True)
    question_id = fields.Many2one('question', string='Question', required=True)
    question_option_id = fields.Many2one('question_option', string='Question Option')
    value = fields.Text(string='Answer Value')

