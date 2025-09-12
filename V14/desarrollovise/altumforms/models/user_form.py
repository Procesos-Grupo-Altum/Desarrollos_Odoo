# -*- coding:utf-8 -*-

from odoo import fields, models, api

class UsuarioFormulario(models.Model):
    _name = 'user_form'

    form_id = fields.Many2one(comodel_name="form", string="Formulario")
    user_id = fields.Many2one(comodel_name="user", string="Usuario")
    client_id = fields.Many2one(comodel_name="client", string="Cliente")