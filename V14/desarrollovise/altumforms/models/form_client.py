# -*- coding:utf-8 -*-

from odoo import fields, models, api

class FormularioCliente(models.Model):
    _name = 'form_client'

    form_id = fields.Many2one(comodel_name="form", string="Formulario")
    client_id = fields.Many2one(comodel_name="client", string="Cliente")