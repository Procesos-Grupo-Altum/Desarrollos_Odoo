from odoo import models, fields


class BaseTranscriptor(models.Model):
    _name = "base.transcriptor"
    _description = "Modelo base para transcriptores"

    name = fields.Char(string="Nombre", required=True)
    active = fields.Boolean(default=True)