# -*- coding:utf-8 -*-

from odoo import fields, models, api

class Cliente(models.Model):
    _name = 'client'

    nit = fields.Char(string="NIT")
    name = fields.Char(string="Nombre")
    short_name = fields.Char(string="Nombre Corto")
    city_id = fields.Many2one(comodel_name='city', string="Ciudad")
    sector_id = fields.Many2one(comodel_name='sector', string="Sector")
    coordinator_id = fields.Many2one(comodel_name='user', string="Coordinador")
    image = fields.Char(string="Imagen")
    has_studies = fields.Selection([('0', 'No'), ('1', 'Si')], string="¿Tiene estudios?", default='0')
    has_indicators = fields.Selection([('0', 'No'), ('1', 'Si')], string="¿Tiene indicadores?", default='0')
    has_stats = fields.Selection([('0', 'No'), ('1', 'Si')], string="¿Tiene estadísticas?", default='0')
    has_turns = fields.Selection([('0', 'No'), ('1', 'Si')], string="¿Tiene turnos?", default='0')
    has_turns2 = fields.Selection([('0', 'No'), ('1', 'Si')], string="¿Tiene turnos 2?", default='0')
    has_minute = fields.Selection([('0', 'No'), ('1', 'Si')], string="¿Tiene minuta?", default='0')
    has_riskmap = fields.Selection([('0', 'No'), ('1', 'Si')], string="¿Tiene mapa de riesgos?", default='0')
    has_bykom = fields.Selection([('0', 'No'), ('1', 'Si')], string="¿Tiene ByKom?", default='0')
    link1 = fields.Text(string="Link 1")
    link2 = fields.Text(string="Link 2")
    forms_auto = fields.Selection([('0', 'No'), ('1', 'Si')], string="¿Formularios Automáticos?", default='0')
    active = fields.Boolean(string="Activo", default=True)
