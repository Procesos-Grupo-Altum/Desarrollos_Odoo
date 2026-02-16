# -*- coding: utf-8 -*-
from odoo import fields, models, api

class GestionSerie(models.Model):
    _name = "gestion.serie"
    _description = "Series"
    _order = "sequence, name"

    codigo = fields.Char(string="Código", index=True)
    name = fields.Char(string="Nombre de la Serie", index=True)
    active = fields.Boolean(string="Activo", default=True)
    sequence = fields.Integer(string="Secuencia", default=1)


