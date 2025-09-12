# -*- conding:utf-8 -*-

from odoo import fields, models, api

class HrContractReport(models.Model):
    _name = 'hr.contract.report'
    _description = 'HR Contract Report'

    name = fields.Char(string='Name', store=True, copied=True, tracking=0, )