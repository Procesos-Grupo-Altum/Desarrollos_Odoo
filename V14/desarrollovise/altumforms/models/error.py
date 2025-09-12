# -*- coding:utf-8 -*-

from odoo import fields, models, api

class Error(models.Model):
    _name = 'error'

    device_id = fields.Many2one("device", string="Dispositivo")
    error_num = fields.Integer(string='Número de Error')
    method = fields.Char(string='Método')
    params = fields.Text(string='Parámetros')
    message = fields.Text(string='Mensaje')