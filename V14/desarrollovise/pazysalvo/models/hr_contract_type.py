# -*- conding:utf-8 -*-
from odoo import fields, models, api

class HrContractType(models.Model):
    _name = 'hr.contract.type'
    _description = 'Tipo de Contrato'

    active = fields.Boolean(default=True)
    allow_replace_obra_labor = fields.Boolean(string='Permitir remplazo en obra labor', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Tipo de Contrato', store=True, readonly=True, tracking=0, )
    required_date_end = fields.Boolean(string='Obligatorio Fecha Finalización', store=True, copied=True, tracking=0, )
    restrict_schedule = fields.Boolean(string='Restriccion en programación', store=True, copied=True, tracking=0, )

