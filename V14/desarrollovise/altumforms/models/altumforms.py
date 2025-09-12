from odoo import fields, models, api

class AltumForms(models.Model):
    _name = 'altumforms'


    name = fields.Char(
        string='Nombre del Formulario')