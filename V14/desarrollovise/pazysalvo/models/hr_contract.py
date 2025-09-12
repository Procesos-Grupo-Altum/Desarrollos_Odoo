# -*- conding:utf-8 -*-

from odoo import fields, models, api

class HrContract(models.Model):
    _inherit = 'hr.contract'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0, )
    activity_date_deadline = fields.Date(string='Siguiente plazo de actividad', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Resumen de la siguiente actividad', tracking=0, )
    activity_type_icon = fields.Char(string='Ícono de tipo de actvidad', readonly=True, tracking=0, )
    apply_procedure_2 = fields.Boolean(string='Aplicar Procedimiento 2', store=True, copied=True, tracking=0, )
    apprentice_to_worker_date = fields.Date(string='Fecha de Cambio a Etapa Productiva', store=True, copied=True,
                                            tracking=0, )
    auxiliar = fields.Boolean(string='Auxiliar', store=True, copied=True, tracking=0, )
    calendar_mismatch = fields.Boolean(string='No coinciden los calendarios', readonly=True, tracking=0, )
    change_date = fields.Date(string='Fecha Efectiva de Vacaciones', store=True, copied=True, tracking=0, )
    compensation_flexible = fields.Boolean(string='Compensacion Flexible', store=True, copied=True, tracking=0, )
    concat_contract = fields.Char(string='Personal', store=True, readonly=True, tracking=0, )
    contract_days = fields.Integer(string='Días de Contrato', store=True, copied=True, tracking=0, )
    date_end = fields.Date(string='Fecha final', store=True, copied=True, tracking=100, )
    date_print = fields.Date(string='Fecha de Impresión de Contrato', store=True, copied=True, tracking=0, )
    date_ref_holiday_book = fields.Date(string='Fecha referencia', store=True, copied=True, tracking=0, )
    date_start = fields.Date(string='Fecha de inicio', store=True, required=True, copied=True, tracking=100, )
    days_config = fields.Boolean(string='Días Configurados', readonly=True, tracking=0, )
    days_expire = fields.Integer(string='Dias a vencer', store=True, readonly=True, tracking=0, )
    days_left = fields.Float(string='Días restantes', store=True, readonly=True, copied=True, tracking=0, )
    days_left_holidays = fields.Float(string='Días Pendientes', store=True, copied=True, tracking=0, )
    deduction_dependents = fields.Boolean(string='Dependientes', store=True, copied=True, tracking=0, )
    due_date = fields.Date(string='Fecha de vencimiento', readonly=True, tracking=0, )
    duration = fields.Integer(string='Duration', store=True, copied=True, tracking=0, )
    fecha_novedad = fields.Date(string='Fecha de Novedad', store=True, copied=True, tracking=1, )
    first_contract_date = fields.Date(string='Primera fecha del contrato', readonly=True, tracking=0, )
    high_risk = fields.Boolean(string='Alto Riesgo', store=True, copied=True, tracking=0, )
    hours_comp_turno = fields.Integer(string='Horas compensadas por turno', store=True, copied=True, tracking=0, )
    jornada_ordinaria_dom = fields.Float(string='Jornada Domingos', store=True, copied=True, tracking=0, )
    jornada_ordinaria_fest = fields.Float(string='Jornada Festivos', store=True, copied=True, tracking=0, )
    limit_deductions = fields.Boolean(string='Limitar Deducciones al 50% de Devengos', store=True, copied=True,
                                      tracking=0, )
    message_attachment_count = fields.Integer(string='Nº de archivos adjuntos', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Error de Envío de Mensaje', readonly=True, tracking=0, )
    message_has_error_counter = fields.Integer(string='Numero de errores', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='Error de entrega del SMS', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Es un seguidor', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Acción requerida', readonly=True, tracking=0, )
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Mensajes sin leer', readonly=True, tracking=0, )
    message_unread_counter = fields.Integer(string='Nº de mensajes sin leer', readonly=True, tracking=0, )
    minimum_wage = fields.Boolean(string='Devenga Salario Mínimo', store=True, copied=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    name = fields.Char(string='Referencia contrato', store=True, required=True, copied=True, tracking=0, )
    new_check = fields.Boolean(string='Nuevo', readonly=True, tracking=0, )
    new_check_save = fields.Boolean(string='Nuevo.', store=True, readonly=True, tracking=0, )
    nota_retiro = fields.Char(string='Observaciones del Retiro', store=True, copied=True, tracking=1, )
    notes = fields.Text(string='Notas', store=True, copied=True, tracking=0, )
    percentage_equivalence = fields.Float(string='Porcentaje Equivalencia', store=True, copied=True, tracking=0, )
    permit_no = fields.Char(string='Número de permiso de trabajo', tracking=100, )
    remote_work_allowance = fields.Boolean(string='Aplica Auxilio de Conectividad', store=True, copied=True,
                                           tracking=0, )
    required_date_end = fields.Boolean(string='Obligatorio Fecha Finalización', readonly=True, tracking=0, )
    restrict_schedule = fields.Boolean(string='Restriccion en programación', readonly=True, tracking=0, )
    risk_percentage = fields.Float(string='Porcentaje de Riesgo', readonly=True, tracking=0, )
    settlement_date = fields.Date(string='Fecha de liquidación', store=True, copied=True, tracking=0, )
    skip_commute_allowance = fields.Boolean(string='Omitir Auxilio de Transporte', store=True, copied=True,
                                            tracking=0, )
    temp_fix = fields.Float(string='Ajuste temporal de sueldo', store=True, copied=True, tracking=0, )
    termino = fields.Char(string='Terminos', store=True, copied=True, tracking=0, )
    trial_date_end = fields.Date(string='Fin del periodo de prueba', store=True, copied=True, tracking=0, )
    trial_date_start = fields.Date(string='Periodo de Prueba', store=True, copied=True, tracking=0, )
    type_job_labor = fields.Char(string='Tipo de Obra o Valor', store=True, copied=True, tracking=0, )
    valor_mensual_horas = fields.Float(string='Valor mensual de horas', store=True, copied=True, tracking=0, )
    visa_expire = fields.Date(string='Fecha expiración visado', tracking=100, )
    visa_no = fields.Char(string='Número de Visado', tracking=100, )
    withholding_percent = fields.Float(string='Porcentaje de Retención', store=True, copied=True, tracking=0, )
    workcenter = fields.Char(string='Centro de Trabajo', store=True, copied=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Siguiente tipo de actividad', tracking=0,
                                       comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Usuario responsable', tracking=0, comodel_name='res.users', )
    afp_pension_id = fields.Many2one(string='Fondo de Pensiones', store=True, copied=True, tracking=0,
                                     comodel_name='res.partner', )
    afp_severance_id = fields.Many2one(string='Fondo de Cesantías', store=True, copied=True, tracking=0,
                                       comodel_name='res.partner', )
    arl_id = fields.Many2one(string='ARL', store=True, copied=True, tracking=0, comodel_name='res.partner', )
    bonus = fields.Monetary(string='Bono', store=True, copied=True, tracking=0, )
    ccf_id = fields.Many2one(string='CCF', store=True, copied=True, tracking=0, comodel_name='res.partner', )
    cliente_obra_labor = fields.Many2one(string='Cliente Obra labor', store=True, copied=True, tracking=0,
                                         comodel_name='res.partner', )
    company_country_id = fields.Many2one(string='País de la empresa', readonly=True, tracking=0,
                                         comodel_name='res.country', )
    company_id = fields.Many2one(string='Compañía', store=True, required=True, copied=True, tracking=0,
                                 comodel_name='res.company', )
    concept_441 = fields.Many2one(string='Concepto 441', store=True, copied=True, tracking=0,
                                  comodel_name='hr.overtime.type', )
    contract_city_id = fields.Many2one(string='Ciudad de Contrato', store=True, copied=True, tracking=0,
                                       comodel_name='res.city', )
    contract_group_id = fields.Many2one(string='Grupo de Contrato', store=True, copied=True, tracking=100,
                                        comodel_name='hr.contract.group', )
    contract_hours_job_id = fields.Many2one(string='Horas Laborables', store=True, copied=True, tracking=0,
                                            comodel_name='contract.hours.job', )
    contract_type_id = fields.Many2one(string='Tipo de Contrato', store=True, copied=True, tracking=100,
                                       comodel_name='hr.contract.type', )
    currency_id = fields.Many2one(string='Moneda', readonly=True, tracking=0, comodel_name='res.currency', )
    daysdiferential_id = fields.Many2one(string='Diferencial de Vacaciones', store=True, copied=True, tracking=0,
                                         comodel_name='hr.vacation.diferential', )
    deduction_by_estate = fields.Monetary(string='Deducción por Interes de Vivienda', store=True, copied=True,
                                          tracking=0, )
    deduction_by_healthcare = fields.Monetary(string='Deducción por Medicina Prepagada', store=True, copied=True,
                                              tracking=0, )
    deduction_by_icetex = fields.Monetary(string='Deducción por Intereses de ICETEX', store=True, copied=True,
                                          tracking=0, )
    department_id = fields.Many2one(string='Área/Departamento/Contrato', store=True, copied=True, tracking=0,
                                    comodel_name='hr.department', )
    employee_id = fields.Many2one(string='Empleado', store=True, copied=True, tracking=100,
                                  comodel_name='hr.employee', )
    eps_id = fields.Many2one(string='EPS', store=True, copied=True, tracking=0, comodel_name='res.partner', )
    fiscal_subtype_id = fields.Many2one(string='Subtipo de Cotizante', store=True, copied=True, tracking=100,
                                        comodel_name='hr.fiscal.subtype', )
    fiscal_type_id = fields.Many2one(string='Tipo de Cotizante', store=True, copied=True, tracking=100,
                                     comodel_name='hr.fiscal.type', )
    hr_contract_job_do_id = fields.Many2one(string='Cargo a Desempeñar', store=True, copied=True, tracking=0,
                                            comodel_name='hr.contract.job.do', )
    hr_responsible_id = fields.Many2one(string='Responsable de RRHH', store=True, copied=True, tracking=100,
                                        comodel_name='res.users', )
    job_id = fields.Many2one(string='Cargo', store=True, copied=True, tracking=0, comodel_name='hr.job', )
    journal_id = fields.Many2one(string='Libro de Salarios', store=True, copied=True, tracking=0,
                                 comodel_name='account.journal', )
    message_channel_ids = fields.Many2many(string='Seguidores (Canales)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_main_attachment_id = fields.Many2one(string='Adjuntos principales', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_partner_ids = fields.Many2many(string='Seguidores (Contactos)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    overtime_type_ids = fields.Many2many(string='Horas Extras ESO/ESU', store=True, copied=True, tracking=0,
                                         comodel_name='hr.overtime.type', )
    resource_calendar_id = fields.Many2one(string='Planificación de trabajo', index=True, store=True, tracking=0,
                                           comodel_name='resource.calendar', )
    risk_id = fields.Many2one(string='Riesgo', store=True, copied=True, tracking=0, comodel_name='hr.contract.risk', )
    settlement_period_id = fields.Many2one(string='Periodo de liquidación', store=True, copied=True, tracking=0,
                                           comodel_name='hr.period', )
    structure_type_id = fields.Many2one(string='Tipo de Estructura Salarial', store=True, copied=True, tracking=0,
                                        comodel_name='hr.payroll.structure.type', )
    subzone_id = fields.Many2one(string='Subzona', store=True, copied=True, tracking=0,
                                 comodel_name='hr.contract.subzone', )
    template_presentation_contract_id = fields.Many2one(string='Carta de Presentación', store=True, copied=True,
                                                        tracking=0, comodel_name='template.report.contract', )
    template_report_contract_id = fields.Many2one(string='Plantilla de Contrato', store=True, copied=True, tracking=0,
                                                  comodel_name='template.report.contract', )
    wage = fields.Monetary(string='Salario', store=True, required=True, copied=True, tracking=100, )
    work_city_id = fields.Many2one(string='Ciudad de Desempeño', store=True, copied=True, tracking=0,
                                   comodel_name='res.city', )
    zone_id = fields.Many2one(string='Zona', store=True, copied=True, tracking=0, comodel_name='hr.contract.zone', )

