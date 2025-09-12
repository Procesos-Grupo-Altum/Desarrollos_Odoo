# -*- conding:utf-8 -*-
from datetime import date


from odoo import fields, models, api



class PazySalvo(models.Model):
    _name = 'pazysalvo'
    _inherit = ['image.mixin']  # Permite agregar imagenes a los registros
    _rec_name = 'employee_id'

    name = fields.Char(string='Nombre Empleado', invisible="1")

    employee_id = fields.Many2one('hr.employee', string='Nombre Empleado', index=True)
    contract_id = fields.Many2one('hr.contract', string='Contrato', index=True, readonly=True, store=True, copied=True)

    image_1920 = fields.Binary(
        related='employee_id.image_1920',  # <-- aquí el cambio
        readonly=True,
        store=False,
        string='Foto'
    )

    state = fields.Selection(
        selection=[
            ('draft', 'Borrador'),
            ('in_progress','En Proceso'),
            ('signed','Firmas Completas'),
            ('done', 'Finalizado'),
            ('cancel','Cancelar')
        ],
        string='Estado',
        default='draft',
        copy=False,

    )

    por_que_1 = fields.Char(string='1 Por Qué?', store=True, copied=True, tracking=0, )
    por_que_2 = fields.Char(string='2 Por Qué?', store=True, copied=True, tracking=0, )
    por_que_3 = fields.Char(string='3 Por Qué?', store=True, copied=True, tracking=0, )
    por_que_4 = fields.Char(string='4 Por Qué?', store=True, copied=True, tracking=0, )
    compromiso_1 = fields.Char(string='Compromiso 1', store=True, copied=True, tracking=0, )
    compromiso_2 = fields.Char(string='Compromiso 2', store=True, copied=True, tracking=0, )
    compromiso_3 = fields.Char(string='Compromiso 3', store=True, copied=True, tracking=0, )
    fecha_vinculacion = fields.Date(string='Fecha Vinculacion', store=True, readonly=True, tracking=1, )
    firma_capacitacion = fields.Binary(string='Capacitación', store=True, copied=True, tracking=0, )
    firma_comunicaciones = fields.Binary(string='Comunicaciones', store=True, copied=True, tracking=0, )
    firma_contabilidad = fields.Binary(string='Contabilidad', store=True, copied=True, tracking=0, )
    firma_creditos = fields.Binary(string='Créditos', store=True, copied=True, tracking=0, )
    firma_del_extrabajador = fields.Binary(string='Firma Del Extrabajador', store=True, copied=True, tracking=0, )
    firma_del_responsable = fields.Binary(string='Firma Del Responsable', store=True, copied=True, tracking=0, )
    firma_disciplina_e_investigaciones = fields.Binary(string='Disciplina E Investigaciones', store=True, copied=True,
                                                       tracking=0, )
    firma_extrabajador = fields.Binary(string='Firma Del Extrabajador', store=True, copied=True, tracking=0, )
    firma_gestion_humana = fields.Binary(string='Gestión Humana', store=True, copied=True, tracking=0, )
    firma_intendencia = fields.Binary(string='Intendencia', store=True, copied=True, tracking=0, )
    firma_jefe_inmediato_administrativos = fields.Binary(string='Jefe Inmediato (Administrativos)', store=True,
                                                         copied=True, tracking=0, )
    firma_nomina = fields.Binary(string='Nomina', store=True, copied=True, tracking=0, )
    firma_operaciones = fields.Binary(string='Operaciones', store=True, copied=True, tracking=0, )
    firma_renovaciones = fields.Binary(string='Renovaciones', store=True, copied=True, tracking=0, )
    firma_responsable = fields.Binary(string='Firma Del Responsable', store=True, copied=True, tracking=1, )
    firma_salud_ocupacional = fields.Binary(string='Salud Ocupacional', store=True, copied=True, tracking=0, )
    firma_servicios_generales = fields.Binary(string='Servicios Generales', store=True, copied=True, tracking=0, )
    firma_sistemas = fields.Binary(string='Sistemas', store=True, copied=True, tracking=0, )
    identification_id = fields.Char(string='Nº identificación', readonly=True, tracking=100, related='employee_id.identification_id')
    fecha_nacimiento_id = fields.Date(string='Fecha Nacimiento', readonly=True, tracking=100, related='employee_id.birthday' )
    fecha_solicitud = fields.Date(string='Fecha Solicitud', readonly=True, tracking=True)
    contract_type = fields.Many2one('hr.contract.type', string="Tipo de Contrato", readonly=True, tracking=100)
    placa = fields.Char(string='Placa', readonly=True, tracking=0, )
    settlement_date = fields.Date(string='Fecha Retiro', store=True, copied=True, tracking=0, )
    user_id_del_extrabajador = fields.Binary(string='Usuario del Extrabajador', store=True, readonly=True, tracking=0, )
    write_date_capacitacion = fields.Datetime(string='Fecha Firma Capacitación', store=True, readonly=True,
                                              tracking=0, )
    write_date_comunicaciones = fields.Datetime(string='Fecha Firma Comunicaciones', store=True, readonly=True,
                                                tracking=0, )
    write_date_contabilidad = fields.Datetime(string='Fecha Firma Contabilidad', store=True, readonly=True,
                                              tracking=0, )
    write_date_creditos = fields.Datetime(string='Fecha Firma Créditos', store=True, readonly=True, tracking=0, )
    write_date_del_extrabajador = fields.Datetime(string='Fecha Firma Del Extrabajador', store=True, readonly=True,
                                                  tracking=0, )
    write_date_disciplina_e_investigaciones = fields.Datetime(string='Fecha Firma Disciplina E Investigaciones',
                                                              store=True, readonly=True, tracking=0, )
    write_date_gestion_humana = fields.Datetime(string='Fecha Firma Gestión Humana', store=True, readonly=True,
                                                tracking=0, )
    write_date_intendencia = fields.Datetime(string='Fecha Firma Intendencia', store=True, readonly=True, tracking=0, )
    write_date_jefe_inmediato_administrativos = fields.Datetime(string='Fecha Firma Jefe Inmediato (Administrativos)',
                                                                store=True, readonly=True, tracking=0, )
    write_date_nomina = fields.Datetime(string='Fecha Firma Nomina', store=True, readonly=True, tracking=0, )
    write_date_operaciones = fields.Datetime(string='Fecha Firma Operaciones', store=True, readonly=True, tracking=0, )
    write_date_renovaciones = fields.Datetime(string='Fecha Firma Renovaciones', store=True, readonly=True,
                                              tracking=0, )
    write_date_responsable = fields.Datetime(string='Fecha Firma Responsable', store=True, readonly=True, tracking=0, )
    write_date_salud_ocupacional = fields.Datetime(string='Fecha Firma Salud Ocupacional', store=True, readonly=True,
                                                   tracking=0, )
    write_date_servicios_generales = fields.Datetime(string='Fecha Firma Servicios Generales', store=True,
                                                     readonly=True, tracking=0, )
    write_date_sistemas = fields.Datetime(string='Fecha Firma Sistemas', store=True, readonly=True, tracking=0, )

    @api.model
    def create(self, vals):
        # Establece la fecha actual al crear el registro
        vals['fecha_solicitud'] = date.today()
        return super(PazySalvo, self).create(vals)  # Cambiado de PazYSalvo a PazySalvo

    def write(self, vals):
        # Establece la fecha actual al actualizar el registro
        vals['fecha_solicitud'] = date.today()
        return super(PazySalvo, self).write(vals)  # Cambiado de PazYSalvo a PazySalvo



    def aceptar(self):
        print('Bienvenido')

    def borrar(self):
        print('Me vas a borrar')