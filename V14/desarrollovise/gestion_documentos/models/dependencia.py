# -*- coding: utf-8 -*-
from odoo import fields, models, api

class GestionDependencia(models.Model):
    _name = "gestion.dependencia"
    _description = "Dependencias"
    _order = "codigo, name"
    _rec_name = "name"

    codigo = fields.Char(string="Código", index=True)
    name = fields.Char(string="Nombre Dependencia", index=True)
    active = fields.Boolean(string="Activo", default=True)
    sequence = fields.Integer(string="Secuencia", default=1)
    groups_ids = fields.Many2many(
        "res.groups",
        string="Grupos de Usuarios",
        compute="_compute_groups_ids",
        store=True,
    )

    @api.depends('codigo', 'name')
    def _compute_groups_ids(self):
        for rec in self:
            rec.groups_ids = False  # limpia por defecto

            if not rec.codigo:
                continue

            group_xml_id = f'gestion_documentos.group_dependencia_{rec.codigo.lower()}'
            group = self.env.ref(group_xml_id, raise_if_not_found=False)

            if group:
                # Puedes asignar directamente el recordset
                rec.groups_ids = group




