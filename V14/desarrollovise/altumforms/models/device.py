# -*- coding:utf-8 -*-

from odoo import fields, models, api

class Celulares(models.Model):
    _name = 'device'

    UID = fields.Char(string='UID')
    source_id = fields.Many2one(comodel_name="source", string="Fuente")
    company_id = fields.Many2one("company", string="Compañía")
    fcm_tocken = fields.Char(string='FCM Token')
    ip = fields.Char(string='IP')
    gps = fields.Text(string='GPS')
    device = fields.Text(string='Dispositivo')
    user_id = fields.Many2one('user', string='Usuario')