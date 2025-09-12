# -*- coding:utf-8 -*-

from odoo import fields, models, api

class QuestionAnswerGroup(models.Model):
    _name = 'question_answer_group'

    device_id = fields.Many2one('device', string='Celulares')
    device_date = fields.Datetime(string='Fecha Registro')
    group_num = fields.Integer(string='Grupo N°')
    code = fields.Integer(string='Código')
    user_id = fields.Many2one('res.users', string='Usuario')
    form_id = fields.Many2one('form', string='Formulario')
    client_id = fields.Many2one('client', string='Cliente')
    opened = fields.Selection([('1', 'Abierto'), ('0', 'Cerrado')], string='Abierto/Cerrado', default='0')
    base_answer_group_id = fields.Integer(string='ID Grupo Respuesta Base')
    flight = fields.Char(string='Vuelo')
    base = fields.Char(string='Base')
    regional = fields.Char(string='Regional')
    place_id = fields.Integer(string='ID Lugar')
    ticket_id = fields.Integer(string='ID Ticket')
    close = fields.Selection([('1', 'Cerrado'), ('0', 'Abierto')], string='Cerrado/Abierto', default='0')
    active = fields.Boolean(string='Activo', default=True)
    date = fields.Datetime(string="Fecha Sincronizacion")
