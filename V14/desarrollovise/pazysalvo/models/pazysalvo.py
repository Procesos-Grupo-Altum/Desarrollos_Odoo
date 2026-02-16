# -*- conding:utf-8 -*-
from datetime import date
from odoo import fields, models, api


class PazySalvo(models.Model):
    _name = 'pazysalvo'
    _inherit = ['image.mixin']
    _rec_name = 'employee_id'

    employee_id = fields.Many2one('hr.employee', string='Nombre Empleado', index=True, context={
        'employee_show_identification': True,
        'employee_name_search_with_identification': True,
    })
    contract_type_id = fields.Many2one(
        'hr.contract.type',
        string=('Tipo de contrato'),
        compute='_compute_contract_type', store=True, readonly=True, copy=False, index=True
    )

    # image_1920 = fields.Binary(
    #    related='employee_id.image_1920', readonly=True, store=False, string='Foto'
    # )
    state = fields.Selection(
        selection=[
            ('draft', 'Borrador'),
            ('in_progress', 'En Proceso'),
            ('signed', 'Firmas Completas'),
            ('done', 'Finalizado'),
            ('cancel', 'Cancelar')
        ], string='Estado', default='draft', copy=False,

    )

    identification_id = fields.Char(string='Nº identificación', readonly=True, tracking=100,
                                    related='employee_id.identification_id', store=True)
    fecha_nacimiento_id = fields.Date(string='Fecha Nacimiento', readonly=True, tracking=100,
                                      related='employee_id.birthday', store=True
                                      )
    genero = fields.Selection(
        string='Género', related='employee_id.gender', readonly=True, tracking=100, store=True
    )
    fecha_solicitud = fields.Date(
        string='Fecha Solicitud',
        default=lambda self: fields.Date.context_today(self),
        readonly=True,
        copy=False,
        tracking=True
    )

    placa = fields.Char(string='Placa', readonly=True, tracking=0, )
    settlement_date = fields.Date(string='Fecha Retiro', store=True, copy=True, tracking=0, )
    des_settlement_type = fields.Char(string="Descripcion del Retiro")
    settlement_type = fields.Selection(
        selection=[
            ('vol', ('Renuncia voluntaria del trabajador')),
            ('lab', ('Terminación la labor contratada')),
            ('causa', ('Terminación con justa causa (empleador)')),
            ('prueba', ('Terminación durante el período de prueba')),
            ('n_causa', ('Terminación sin justa causa (empleador)')),
            ('exp', ('Vencimiento del término (contrato a término fijo)')),
            ('unil', ('Decisión unilateral del empleador (sin justa causa)')),
            ('fal', ('Fallecimiento del trabajador')),
            ('pen', ('Terminación por reconocimiento de pensión')),
            ('nolab', ('No ingreso / No laboró')),
            ('mutuo', ('Terminación por mutuo acuerdo')),
        ],
        string=('Causal de terminación'),
        help=('Seleccione la causal de terminación del vínculo laboral.'),
    )

    fecha_vinculacion = fields.Date(
        string='Fecha Vinculación',
        related='employee_id.contract_id.date_start',
        readonly=True, store=True
    )
    employee_job_title = fields.Char(
        string='Cargo',
        related='employee_id.job_title',
        store=True, readonly=True
    )

    por_que_1 = fields.Char(string='1 Por Qué?', store=True, copy=True, tracking=0, )
    por_que_2 = fields.Char(string='2 Por Qué?', store=True, copy=True, tracking=0, )
    por_que_3 = fields.Char(string='3 Por Qué?', store=True, copy=True, tracking=0, )
    por_que_4 = fields.Char(string='4 Por Qué?', store=True, copy=True, tracking=0, )
    compromiso_1 = fields.Char(string='Compromiso 1', store=True, copy=True, tracking=0, )
    compromiso_2 = fields.Char(string='Compromiso 2', store=True, copy=True, tracking=0, )
    compromiso_3 = fields.Char(string='Compromiso 3', store=True, copy=True, tracking=0, )
    firma_capacitacion = fields.Binary(string='Capacitación', store=True, copy=True, tracking=0, )
    firma_comunicaciones = fields.Binary(string='Comunicaciones', store=True, copy=True, tracking=0, )
    firma_contabilidad = fields.Binary(string='Contabilidad', store=True, copy=True, tracking=0, )
    firma_creditos = fields.Binary(string='Créditos', store=True, copy=True, tracking=0, )
    firma_del_extrabajador = fields.Binary(string='Firma Del Extrabajador', store=True, copy=True, tracking=0, )
    firma_del_responsable = fields.Binary(string='Firma Del Responsable', store=True, copy=True, tracking=0, )
    firma_disciplina_e_investigaciones = fields.Binary(string='Disciplina E Investigaciones', store=True, copy=True,
                                                       tracking=0, )
    firma_extrabajador = fields.Binary(string='Firma Del Extrabajador', store=True, copy=True, tracking=0, )
    firma_gestion_humana = fields.Binary(string='Gestión Humana', store=True, copy=True, tracking=0, )
    firma_intendencia = fields.Binary(string='Intendencia', store=True, copy=True, tracking=0, )
    firma_jefe_inmediato_administrativos = fields.Binary(string='Jefe Inmediato (Administrativos)', store=True,
                                                         copy=True, tracking=0, )
    firma_nomina = fields.Binary(string='Nomina', store=True, copy=True, tracking=0, )
    firma_operaciones = fields.Binary(string='Operaciones', store=True, copy=True, tracking=0, )
    firma_renovaciones = fields.Binary(string='Renovaciones', store=True, copy=True, tracking=0, )
    firma_responsable = fields.Binary(string='Firma Del Responsable', store=True, copy=True, tracking=1, )
    firma_salud_ocupacional = fields.Binary(string='Salud Ocupacional', store=True, copy=True, tracking=0, )
    firma_servicios_generales = fields.Binary(string='Servicios Generales', store=True, copy=True, tracking=0, )
    firma_sistemas = fields.Binary(string='Sistemas', store=True, copy=True, tracking=0, )

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
        # (opcional) garantiza que siempre venga con fecha si llega vacío
        vals.setdefault('fecha_solicitud', fields.Date.context_today(self))
        return super().create(vals)

    def aceptar(self):
        # Opción A: directo (Odoo lo persiste)
        for rec in self:
            rec.state = 'in_progress'

        # Opción B: explícito
        # self.write({'state': 'accepted'})
        return True

    def borrar(self):
        print('Me vas a borrar')

    @api.onchange('settlement_type', 'employee_id')
    def _onchange_settlement_type(self):
        for rec in self:
            if not rec.settlement_type:
                rec.des_settlement_type = False
                continue

            # Obtener etiqueta (label) del selection sin duplicar strings
            label = dict(rec._fields['settlement_type'].selection).get(rec.settlement_type, "")

            # Tomar nombre del empleado (sirve para hr.employee o res.partner)
            nombre = rec.employee_id.name if rec.employee_id else ""

            if nombre and label:
                rec.des_settlement_type = (
                                              'Al empleado <strong>(%s)</strong> <br>Se le finaliza el contrato por motivo: <strong>"%s". </strong>'
                                          ) % (nombre, label)
            elif label:
                rec.des_settlement_type = (
                                              'Se finaliza el contrato por motivo: "%s"'
                                          ) % (label)
            else:
                rec.des_settlement_type = False

    @api.depends('employee_id', 'employee_id.contract_id', 'employee_id.contract_id.state')
    def _compute_contract_type(self):
        Contract = self.env['hr.contract']
        for rec in self:
            contract = rec.employee_id.contract_id or Contract.search([
                ('employee_id', '=', rec.employee_id.id),
                ('state', 'in', ('open', 'pending')),
            ], order='date_start desc', limit=1) or Contract.search([
                ('employee_id', '=', rec.employee_id.id),
            ], order='date_start desc', limit=1)
            rec.contract_type_id = contract.contract_type_id.id if contract else False
