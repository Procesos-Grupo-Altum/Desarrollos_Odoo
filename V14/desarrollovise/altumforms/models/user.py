# -*- coding:utf-8 -*-

from odoo import fields, models, api

class Usuarios(models.Model):
    _name = 'user'

    name = fields.Char(string="Nombre")
    username = fields.Char(string="Usuario")
    password = fields.Char(string="Contraseña")
    document = fields.Char(string="Documento")
    email = fields.Char(string="Correo Electronico")
    avantel = fields.Char(string="Avantel")
    phone = fields.Char(string="Telefono")
    active = fields.Boolean(string="Activo", default=True)

    modified_user_id = fields.Many2one(
        comodel_name="user",
        string="Modificado por:",
    )
    authitemname = fields.Many2one(
        comodel_name="authitem",
        string = "Tipo de Usuario",
    )
