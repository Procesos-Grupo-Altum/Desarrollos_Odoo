# -*- conding:utf-8 -*-

from odoo import fields, models, api


class TiposContratosVise(models.Model):
    _name = 'tipos.contratos.areas.vise'
    _description = 'Tipos de Contratos Areas Vise'

    name = fields.Many2one('vise.areas', string='Area Vise', required=True, index=True)
    contract_type = fields.Many2one('hr.contract.type', string='Tipo de Contrato', required=True, index=True)
    aplica_firma = fields.Boolean(string="Aplica Firma", default=True)
    active = fields.Boolean(string="Activo", default=True)
