# -*- coding: utf-8 -*-
from odoo import fields, models, api

class GestionSubserie(models.Model):
    _name = "gestion.subserie"
    _description = "Subseries"
    _order = "sequence, name"


    codigo = fields.Char(string="Código Subserie", index=True)
    name = fields.Char(string="Nombre de la Subserie", index=True)
    active = fields.Boolean(string="Activo", default=True)
    sequence = fields.Integer(string="Secuencia", default=0)

    # Relación con Serie
    serie_id = fields.Many2one(
        "gestion.serie",
        string="Nombre de la Serie",
        ondelete="restrict",
        index=True,
    )
    codigo_serie = fields.Char(string="Código Serie", related="serie_id.codigo", store=True)
    procedimiento = fields.Html(string="Procedimiento", help="Descripción del procedimiento asociado a la subserie.")
    cierre_expediente = fields.Text(string="Cierre de Expediente", help="Descripción del cierre de expediente asociado a la subserie.")


