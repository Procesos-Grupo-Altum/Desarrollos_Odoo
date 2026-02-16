# -*- conding:utf-8 -*-
from datetime import date

from odoo import fields, models, api
from odoo.odoo.exceptions import UserError


class QuoterFivep(models.Model):
    _name = 'quoter.fivep'
    _description = 'Quoter Fivep'
    balance = fields.Float(string='Saldo', readonly=True, tracking=0, )
    delivery_date = fields.Date(string='Fecha Entrega', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Detalle', store=True, copy=True, tracking=0, )
    observation = fields.Char(string='Observación', store=True, copy=True, tracking=0, )
    quantity = fields.Integer(string='Cantidad', store=True, copy=True, tracking=0, )
    sale_quoter_id = fields.Many2one(string='Cotizador', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter', )
    state_fivep_id = fields.Many2one(string='Estado', store=True, copy=True, tracking=0, comodel_name='fivep.state', )
    total_delivery_value = fields.Float(string='Valor Entregado', store=True, copy=True, tracking=0, )
    total_value = fields.Float(string='Valor Total', readonly=True, tracking=0, )
    value = fields.Float(string='Valor', readonly=True, tracking=0, )


class FivepState(models.Model):
    _name = 'fivep.state'
    _description = 'Fivep State'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class Abstractdmsmixin(models.Model):
    _name = 'abstract.dms.mixin'
    _description = 'Abstract Dms Mixin'
    category_id = fields.Many2one(string='Categoría', store=True, copy=True, tracking=0,
                                  comodel_name='dms.category', )
    color = fields.Integer(string='Color', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañía', index=True, store=True, readonly=True, tracking=0,
                                 comodel_name='res.company', )
    is_hidden = fields.Boolean(string='Almacenamiento está oculto', store=True, readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', index=True, store=True, required=True, copy=True, tracking=0, )
    storage_id = fields.Many2one(string='Almacenamiento', store=True, copy=True, tracking=0,
                                 comodel_name='dms.storage', )


class Academia(models.Model):
    _name = 'academia'
    _description = 'Academia'
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    nit = fields.Char(string='Nit', store=True, required=True, copy=True, tracking=0, )


class Acciónautomatizada(models.Model):
    _inherit = 'base.automation'
    _description = 'Acción automatizada'
    action_server_id = fields.Many2one(string='Acciones de servidor', store=True, required=True, copy=True,
                                       tracking=0, comodel_name='ir.actions.server', )
    active = fields.Boolean(string='Activo', store=True, copy=True, tracking=0, )
    activity_date_deadline_range = fields.Integer(string='Fecha límite el', copy=True, tracking=0, )
    activity_note = fields.Html(string='Nota', copy=True, tracking=0, )
    activity_summary = fields.Char(string='Resumen', copy=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Actividad', copy=True, tracking=0, comodel_name='mail.activity.type', )
    activity_user_field_name = fields.Char(string='Nombre del campo de usuario', copy=True, tracking=0, )
    activity_user_id = fields.Many2one(string='Responsable', copy=True, tracking=0, comodel_name='res.users', )
    binding_model_id = fields.Many2one('ir.model', string='Modelo vinculante', ondelete='set null')
    binding_view_types = fields.Char(string='Tipos de vista de enlace', copy=True, tracking=0, )
    channel_ids = fields.Many2many(relation='academia_channel_ids_rel', column1='academia_id', column2='channel_ids_id',
                                   string='Añadir canales', copy=True, tracking=0, comodel_name='mail.channel', )
    child_ids = fields.Many2many(relation='academia_child_ids_rel', column1='academia_id', column2='child_ids_id',
                                 string='Acciones hijas', copy=True, tracking=0, comodel_name='ir.actions.server', )
    code = fields.Text(string='Código Python', copy=True, tracking=0, )
    crud_model_id = fields.Many2one('ir.model', string='Modelo destino', ondelete='set null')
    crud_model_name = fields.Char(string='Nombre del modelo destino', readonly=True, tracking=0, )
    filter_domain = fields.Char(string='Aplicar en', store=True, copy=True, tracking=0, )
    filter_pre_domain = fields.Char(string='Antes de actualizar el dominio', store=True, copy=True, tracking=0, )
    groups_id = fields.Many2many(relation='academia_groups_id_rel', column1='academia_id', column2='groups_id_id',
                                 string='Grupos', copy=True, tracking=0, comodel_name='res.groups', )
    help = fields.Html(string='Descripción de la acción', copy=True, tracking=0, )
    last_run = fields.Datetime(string='Última ejecución', store=True, readonly=True, tracking=0, )
    least_delay_msg = fields.Char(string='Mínimo de retraso del mensaje', readonly=True, tracking=0, )
    link_field_id = fields.Many2one(string='Campo de enlace', copy=True, tracking=0, comodel_name='ir.model.fields', )
    model_id = fields.Many2one(string='Modelo', required=True, index=True, ondelete='cascade',
                               comodel_name='ir.model', )
    model_name = fields.Char(string='Nombre del modelo', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre de acción', required=True, copy=True, tracking=0, )
    on_change_field_ids = fields.Many2many(relation='academia_on_change_field_ids_rel', column1='academia_id',
                                           column2='on_change_field_ids_id', string='Activar al modificar campos',
                                           store=True, copy=True, tracking=0,
                                           comodel_name='ir.model.fields', )
    partner_ids = fields.Many2many(relation='academia_partner_ids_rel', column1='academia_id', column2='partner_ids_id',
                                   string='Añadir seguidores', copy=True, tracking=0, comodel_name='res.partner', )
    sequence = fields.Integer(string='Secuencia', copy=True, tracking=0, )
    sms_mass_keep_log = fields.Boolean(string='Registrar como nota...', copy=True, tracking=0, )
    sms_template_id = fields.Many2one(string='Plantilla de SMS', copy=True, tracking=0, comodel_name='sms.template', )
    template_id = fields.Many2one(string='Plantilla de correo electrónico', copy=True, tracking=0,
                                  comodel_name='mail.template', )
    trg_date_calendar_id = fields.Many2one(string='Usar calendario', store=True, copy=True, tracking=0,
                                           comodel_name='resource.calendar', )
    trg_date_id = fields.Many2one(string='Fecha activación', store=True, copy=True, tracking=0,
                                  comodel_name='ir.model.fields', )
    trg_date_range = fields.Integer(string='Retraso después de la fecha de activación', store=True, copy=True,
                                    tracking=0, )
    trigger_field_ids = fields.Many2many(relation='academia_trigger_field_ids_rel', column1='academia_id',
                                         column2='trigger_field_ids_id', string='Campos de activación', store=True,
                                         copy=True, tracking=0,
                                         comodel_name='ir.model.fields', )
    type = fields.Char(string='Tipo de acción', required=True, copy=True, tracking=0, )
    website_path = fields.Char(string='Ruta del Sitio Web', copy=True, tracking=0, )
    website_published = fields.Boolean(string='Disponible en el Sitio Web', tracking=0, )
    website_url = fields.Char(string='URL del lloc web', readonly=True, tracking=0, )
    xml_id = fields.Char(string='ID externo', readonly=True, tracking=0, )


class Accionesdisciplinarias(models.Model):
    _name = 'hr.employee.disciplinary.action'
    _description = 'Acciones disciplinarias'
    auxiliar_file = fields.Many2many(relation='accionesdisciplinari_auxiliar_file_rel',
                                     column1='accionesdisciplinari_id', column2='auxiliar_file_id',
                                     string='Documento soporte', store=True, copy=True, tracking=0,
                                     comodel_name='ir.attachment', )
    date = fields.Datetime(string='Fecha de ocurrencia', store=True, required=True, copy=True, tracking=0, )
    description = fields.Text(string='Decisión', store=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    type_id = fields.Many2one(string='Acción tomada', store=True, required=True, copy=True, tracking=0,
                              comodel_name='hr.employee.disciplinary.action.line', )


class Accountcontainergroup(models.Model):
    _name = 'account.container.group'
    _description = 'Account Container Group'
    is_container = fields.Boolean(string='Es grupo contenedor?', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Name', store=True, required=True, copy=True, tracking=0, )
    parent_id = fields.Many2one(string='Parent Group', store=True, copy=True, tracking=0,
                                comodel_name='account.container.group', )
    report_group = fields.Boolean(string='Es grupo de reporte?', store=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Sequence', store=True, copy=True, tracking=0, )


class Accountingreporthelper(models.Model):
    _name = 'account.accounting.report'
    _description = 'Accounting Report Helper'
    account_id = fields.Many2one(string='Account', store=True, copy=True, tracking=0,
                                 comodel_name='account.account', )
    analytic_account_id = fields.Many2one(string='Analytic Account', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    analytic_tag_ids = fields.Many2many(relation='accountingreporthelp_analytic_tag_ids_rel',
                                        column1='accountingreporthelp_id', column2='analytic_tag_ids_id',
                                        string='Analytic Tag', store=True, copy=True, tracking=0,
                                        comodel_name='account.analytic.tag', )
    balance = fields.Monetary(string='Saldo', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Company', store=True, copy=True, tracking=0, comodel_name='res.company', )
    credit = fields.Monetary(string='Credit', store=True, copy=True, tracking=0, )
    currency_id = fields.Many2one(string='Moneda', store=True, copy=True, tracking=0, comodel_name='res.currency', )
    date = fields.Date(string='Date', store=True, copy=True, tracking=0, )
    debit = fields.Monetary(string='Debit', store=True, copy=True, tracking=0, )
    display_type = fields.Char(string='Display Type', store=True, copy=True, tracking=0, )
    journal_id = fields.Many2one(string='Journal', store=True, copy=True, tracking=0,
                                 comodel_name='account.journal', )
    move_id = fields.Many2one(string='Move', store=True, copy=True, tracking=0, comodel_name='account.move', )
    name = fields.Char(string='Name', store=True, copy=True, tracking=0, )


class AccountreportHtml(models.Model):
    _name = 'account.financial.html.report'
    _description = 'Account Report (HTML)'
    analytic = fields.Boolean(string='Allow analytic filters', store=True, copy=True, tracking=0, )
    applicable_filters_ids = fields.Many2many(relation='accountreport_html_applicable_filters_i_rel',
                                              column1='accountreport_html_id', column2='applicable_filters_i_id',
                                              string='Applicable Filters', store=True, copy=True, tracking=0,
                                              comodel_name='ir.filters', )
    company_id = fields.Many2one(string='Company', store=True, copy=True, tracking=0, comodel_name='res.company', )
    comparison = fields.Boolean(string='Allow comparison', store=True, copy=True, tracking=0, )
    date_range = fields.Boolean(string='Based on date ranges', store=True, copy=True, tracking=0, )
    generated_menu_id = fields.Many2one(string='Menu Item', store=True, tracking=0, comodel_name='ir.ui.menu', )
    name = fields.Char(string='Name', store=True, copy=True, tracking=0, )
    parent_id = fields.Many2one(string='Parent Menu', tracking=0, comodel_name='ir.ui.menu', )
    show_journal_filter = fields.Boolean(string='Allow filtering by journals', store=True, copy=True, tracking=0, )
    tax_report = fields.Boolean(string='Reporte Impuestos', store=True, copy=True, tracking=0, )
    unfold_all_filter = fields.Boolean(string='Show unfold all filter', store=True, copy=True, tracking=0, )


class AccountreportHtmlLine(models.Model):
    _name = 'account.financial.html.report.line'
    _description = 'Account Report (HTML Line)'
    action_id = fields.Many2one(string='Action', store=True, copy=True, tracking=0,
                                comodel_name='ir.actions.actions', )
    code = fields.Char(string='Code', store=True, copy=True, tracking=0, )
    domain = fields.Char(string='Domain', store=True, copy=True, tracking=0, )
    financial_report_id = fields.Many2one(string='Financial Report', store=True, copy=True, tracking=0,
                                          comodel_name='account.financial.html.report', )
    formulas = fields.Char(string='Formulas', store=True, copy=True, tracking=0, )
    green_on_positive = fields.Boolean(string='Is growth good when positive', store=True, copy=True, tracking=0, )
    groupby = fields.Char(string='Group by', store=True, copy=True, tracking=0, )
    hide_if_empty = fields.Boolean(string='Hide If Empty', store=True, copy=True, tracking=0, )
    hide_if_zero = fields.Boolean(string='Hide If Zero', store=True, copy=True, tracking=0, )
    level = fields.Integer(string='Level', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Section Name', store=True, copy=True, tracking=0, )
    parent_id = fields.Many2one(string='Parent', store=True, copy=True, tracking=0,
                                comodel_name='account.financial.html.report.line', )
    parent_path = fields.Char(string='Parent Path', index=True, store=True, copy=True, tracking=0, )
    print_on_new_page = fields.Boolean(string='Print On New Page', store=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Sequence', store=True, copy=True, tracking=0, )


class Accountreportfootnote(models.Model):
    _name = 'account.report.footnote'
    _description = 'Account Report Footnote'
    line = fields.Char(string='Line', index=True, store=True, copy=True, tracking=0, )
    manager_id = fields.Many2one(string='Manager', store=True, copy=True, tracking=0,
                                 comodel_name='account.report.manager', )
    text = fields.Char(string='Text', store=True, copy=True, tracking=0, )


class Acreditaciontipo(models.Model):
    _name = 'acreditacion.tipo'
    _description = 'Acreditacion tipo'
    cargo_codigo = fields.Char(string='Cargo código', store=True, required=True, copy=True, tracking=0, )
    cargo = fields.Many2one(string='Cargo', store=True, required=True, copy=True, tracking=0, comodel_name='hr.job', )
    codigo = fields.Char(string='Código', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Actializarguiadeentrega(models.Model):
    _name = 'update.delivery.guide'
    _description = 'Actializar Guia de Entrega'
    guides_ids = fields.Many2many(relation='actializarguiadeentr_guides_ids_rel', column1='actializarguiadeentr_id',
                                  column2='guides_ids_id', string='Guias de entrega', store=True, copy=True, tracking=0,
                                  comodel_name='delivery.guide', )


class Activo(models.Model):
    _name = 'account.asset'
    _description = 'Activo'
    account_analytic_id = fields.Many2one(string='Cuenta Analítica', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    accumulated_value = fields.Float(string='Valor depreciación acumulada', store=True, copy=True, tracking=0, )
    active = fields.Boolean(string='Activo', store=True, copy=True, tracking=0, )
    analytic_account_id_niff = fields.Many2one(string='Cuenta analítica Niif', store=True, copy=True, tracking=0,
                                               comodel_name='account.analytic.account', )
    analytic_tag_ids = fields.Many2many(relation='activo_analytic_tag_ids_rel', column1='activo_id',
                                        column2='analytic_tag_ids_id', string='Analytic tags', store=True, copy=True,
                                        tracking=0,
                                        comodel_name='account.analytic.tag', )
    centrocosto_id = fields.Many2one(string='Centro de costo', store=True, copy=True, tracking=0,
                                     comodel_name='account.analytic.account', )
    code = fields.Char(string='Referencia', store=True, copy=True, tracking=0, )
    commercial_distribution_id = fields.Many2one(string='Distribución por comercial', store=True, copy=True,
                                                 tracking=0,
                                                 comodel_name='account.commercial.distribution', )
    company_currency_id = fields.Many2one(string='Moneda la compañía', store=True, readonly=True, tracking=0,
                                          comodel_name='res.currency', )
    company_id = fields.Many2one(string='Compañía', store=True, readonly=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    date_remove_niff = fields.Date(string='Asset Removal Date', store=True, readonly=True, copy=True, tracking=0, )
    date_remove = fields.Date(string='Fecha de eliminación de activo', store=True, readonly=True, copy=True,
                              tracking=0, )
    date_start_niff = fields.Date(string='Fecha de inicio del activo Niif', store=True, copy=True, tracking=0, )
    date_start = fields.Date(string='Fecha de inicio del activo', store=True, required=True, copy=True, tracking=0, )
    days_calc_niff = fields.Boolean(string='Calcular por días Niif', store=True, copy=True, tracking=0, )
    days_calc = fields.Boolean(string='Calcular por días', store=True, copy=True, tracking=0, )
    depreciation_base_niff = fields.Float(string='Base amortización Niif', store=True, readonly=True, tracking=0, )
    depreciation_base = fields.Float(string='Base Amortización', store=True, readonly=True, tracking=0, )
    depresiation_value_niif = fields.Float(string='Valor depreciación acumulada Niif', store=True, copy=True,
                                           tracking=0, )
    group_ids = fields.Many2many(relation='activo_group_ids_rel', column1='activo_id', column2='group_ids_id',
                                 string='Grupos de activo', store=True, copy=True, tracking=0,
                                 comodel_name='account.asset.group', )
    historic_value = fields.Float(string='Valor histórico compra', store=True, copy=True, tracking=0, )
    is_copy = fields.Boolean(string='Is Copy', readonly=True, tracking=0, )
    is_visible = fields.Boolean(string='visible', readonly=True, tracking=0, )
    lot_ids = fields.Many2many(relation='activo_lot_ids_rel', column1='activo_id', column2='lot_ids_id', string='Lotes',
                               store=True, copy=True, tracking=0,
                               comodel_name='stock.production.lot', )
    marca = fields.Char(string='Marca', store=True, copy=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='activo_message_channel_ids_rel', column1='activo_id',
                                           column2='message_channel_ids_id', string='Followers (Channels)',
                                           readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='activo_message_partner_ids_rel', column1='activo_id',
                                           column2='message_partner_ids_id', string='Followers (Partners)',
                                           readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    method_end_niff = fields.Date(string='Fecha de finalización Niif', store=True, copy=True, tracking=0, )
    method_end = fields.Date(string='Fecha de finalización', store=True, copy=True, tracking=0, )
    method_number_niff = fields.Integer(string='Número de periodos', store=True, copy=True, tracking=0, )
    method_number = fields.Integer(string='Número de años', store=True, copy=True, tracking=0, )
    method_progress_factor_niff = fields.Float(string='Factor decreciente Niif', store=True, copy=True, tracking=0, )
    method_progress_factor = fields.Float(string='Factor decreciente', store=True, copy=True, tracking=0, )
    modelo = fields.Char(string='Modelo', store=True, copy=True, tracking=0, )
    move_eliminated_id = fields.Many2one(string='Baja Inventario Fiscal', store=True, readonly=True, tracking=0,
                                         comodel_name='account.move', )
    move_eliminated_niif_id = fields.Many2one(string='Baja Inventario Fiscal Niif', store=True, readonly=True,
                                              tracking=0,
                                              comodel_name='account.move', )
    move_line_check = fields.Boolean(string='Tiene asientos contables', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre de activo', store=True, required=True, copy=True, tracking=0, )
    note = fields.Text(string='Nota', store=True, copy=True, tracking=0, )
    partner_id_niff = fields.Many2one(string='Partner', store=True, copy=True, tracking=0,
                                      comodel_name='res.partner', )
    partner_id = fields.Many2one(string='Empresa', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    placa = fields.Char(string='Placa', store=True, copy=True, tracking=0, )
    prodlot_id = fields.Many2one(string='Serial', store=True, copy=True, tracking=0,
                                 comodel_name='stock.production.lot', )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.product', )
    profile_id_niff = fields.Many2one(string='Categoría de activo Niif', store=True, copy=True, tracking=0,
                                      comodel_name='account.asset.profile', )
    profile_id = fields.Many2one(string='Categoría de activo', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='account.asset.profile', )
    project_distribution_id = fields.Many2one(string='Distribución', store=True, copy=True, tracking=0,
                                              comodel_name='project.distribution', )
    prorata_niff = fields.Boolean(string='Tiempo prorrateado Niif', store=True, copy=True, tracking=0, )
    prorata = fields.Boolean(string='Tiempo prorrateado', store=True, copy=True, tracking=0, )
    puesto_id = fields.Many2one(string='Puesto', store=True, copy=True, tracking=0, comodel_name='hr.roster.puesto', )
    purchase_value_niff = fields.Float(string='Valor de compra Niif', store=True, copy=True, tracking=0, )
    purchase_value = fields.Float(string='Valor de compra', store=True, required=True, copy=True, tracking=0, )
    regional_id = fields.Many2one(string='Sucursal', store=True, copy=True, tracking=0, comodel_name='res.regional', )
    salvage_value_niff = fields.Float(string='Valor de rescate Niif', store=True, copy=True, tracking=0, )
    salvage_value = fields.Float(string='Valor de rescate', store=True, copy=True, tracking=0, )
    use_leap_years_niff = fields.Boolean(string='Usar años bisiestos Niif', store=True, copy=True, tracking=0, )
    use_leap_years = fields.Boolean(string='Use años bisiestos', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Responsable', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    value_depreciated_niff = fields.Float(string='Valor amortizado Niif', store=True, readonly=True, tracking=0, )
    value_depreciated = fields.Float(string='Valor amortizado', store=True, readonly=True, tracking=0, )
    value_residual_niff = fields.Float(string='Valor residual Niif', store=True, readonly=True, tracking=0, )
    value_residual = fields.Float(string='Valor residual', store=True, readonly=True, tracking=0, )
    x_city_id = fields.Many2one(string='Ciudad', store=True, copy=True, tracking=1, comodel_name='res.city', )


class Administrarelresumenylasnotasalpiedepaginadelosinformes(models.Model):
    _name = 'account.report.manager'
    _description = 'Administrar el resumen y las notas al pie de página de los informes'
    company_id = fields.Many2one(string='Company', store=True, copy=True, tracking=0, comodel_name='res.company', )
    financial_report_id = fields.Many2one(string='Financial Report', store=True, copy=True, tracking=0,
                                          comodel_name='account.financial.html.report', )
    partner_id = fields.Many2one(string='Partner', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    report_name = fields.Char(string='Report Name', store=True, required=True, copy=True, tracking=0, )
    summary = fields.Char(string='Summary', store=True, copy=True, tracking=0, )


class Agedpartnerbalances(models.Model):
    _name = 'account.aged.partner'
    _description = 'Aged Partner Balances'
    account_code = fields.Char(string='Account Code', store=True, copy=True, tracking=0, )
    account_id = fields.Many2one(string='Account', store=True, copy=True, tracking=0,
                                 comodel_name='account.account', )
    account_name = fields.Char(string='Account Name', store=True, copy=True, tracking=0, )
    analytic_account_id = fields.Many2one(string='Analytic Account', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    analytic_tag_ids = fields.Many2many(relation='agedpartnerbalances_analytic_tag_ids_rel',
                                        column1='agedpartnerbalances_id', column2='analytic_tag_ids_id',
                                        string='Analytic Tag', store=True, copy=True, tracking=0,
                                        comodel_name='account.analytic.tag', )
    balance = fields.Monetary(string='Saldo', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Company', store=True, copy=True, tracking=0, comodel_name='res.company', )
    credit = fields.Monetary(string='Credit', store=True, copy=True, tracking=0, )
    currency_id = fields.Many2one(string='Moneda', store=True, copy=True, tracking=0, comodel_name='res.currency', )
    date = fields.Date(string='Date', store=True, copy=True, tracking=0, )
    debit = fields.Monetary(string='Debit', store=True, copy=True, tracking=0, )
    display_type = fields.Char(string='Display Type', store=True, copy=True, tracking=0, )
    expected_pay_date = fields.Date(string='Exp. Date', store=True, copy=True, tracking=0, )
    journal_code = fields.Char(string='Journal Code', store=True, copy=True, tracking=0, )
    journal_id = fields.Many2one(string='Journal', store=True, copy=True, tracking=0,
                                 comodel_name='account.journal', )
    move_id = fields.Many2one(string='Move', store=True, copy=True, tracking=0, comodel_name='account.move', )
    move_name = fields.Char(string='Move Name', store=True, copy=True, tracking=0, )
    move_type = fields.Char(string='Move Type', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Name', store=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Asociado', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    partner_name = fields.Char(string='Partner Name', store=True, copy=True, tracking=0, )
    partner_trust = fields.Char(string='Partner Trust', store=True, copy=True, tracking=0, )
    payment_id = fields.Many2one(string='Payment', store=True, copy=True, tracking=0,
                                 comodel_name='account.payment', )
    period0 = fields.Monetary(string='As of:', store=True, copy=True, tracking=0, )
    period1 = fields.Monetary(string='1 - 30', store=True, copy=True, tracking=0, )
    period2 = fields.Monetary(string='31 - 60', store=True, copy=True, tracking=0, )
    period3 = fields.Monetary(string='61 - 90', store=True, copy=True, tracking=0, )
    period4 = fields.Monetary(string='91 - 120', store=True, copy=True, tracking=0, )
    period5 = fields.Monetary(string='Older', store=True, copy=True, tracking=0, )
    report_currency_id = fields.Many2one(string='Report Currency', store=True, copy=True, tracking=0,
                                         comodel_name='res.currency', )
    report_date = fields.Date(string='Report Date', store=True, copy=True, tracking=0, )


class Agruparfacturas(models.Model):
    _name = 'account.move.group'
    _description = 'Agrupar Facturas'
    moves_ids = fields.Many2many(relation='agruparfacturas_moves_ids_rel', column1='agruparfacturas_id',
                                 column2='moves_ids_id', string='Facturas', store=True, copy=True, tracking=0,
                                 comodel_name='account.move', )


class Almacenamiento(models.Model):
    _name = 'dms.storage'
    _description = 'Almacenamiento'
    company_id = fields.Many2one(string='Compañía', store=True, copy=True, tracking=0, comodel_name='res.company', )
    count_storage_directories = fields.Integer(string='Nº de carpetas', readonly=True, tracking=0, )
    count_storage_files = fields.Integer(string='Nº de archivos', readonly=True, tracking=0, )
    include_message_attachments = fields.Boolean(string='Create files from message attachments', store=True,
                                                 copy=True,
                                                 tracking=0, )
    inherit_access_from_parent_record = fields.Boolean(string='Inherit permissions from related record', store=True,
                                                       copy=True, tracking=0, )
    is_hidden = fields.Boolean(string='Almacenamiento está oculto', store=True, copy=True, tracking=0, )
    model_ids = fields.Many2many(relation='almacenamiento_model_ids_rel', column1='almacenamiento_id',
                                 column2='model_ids_id', string='Modelos vinculados', store=True, copy=True, tracking=0,
                                 comodel_name='ir.model', )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Anticipocliente(models.Model):
    _name = 'account.advance.customer'
    _description = 'Anticipo Cliente'
    account_analytic_id = fields.Many2one(string='Centro de Costo', store=True, copy=True, tracking=100,
                                          comodel_name='account.analytic.account', )
    account_id = fields.Many2one(string='Cuenta de Anticipo', store=True, copy=True, tracking=100,
                                 comodel_name='account.account', )
    amount_local = fields.Float(string='Valor Moneda Local', store=True, readonly=True, tracking=0, )
    amount = fields.Float(string='Valor', store=True, copy=True, tracking=100, )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=100, comodel_name='res.company', )
    crossed = fields.Boolean(string='Cruzado', store=True, copy=True, tracking=0, )
    currency_id = fields.Many2one(string='Moneda', store=True, copy=True, tracking=100, comodel_name='res.currency', )
    description = fields.Text(string='Descripción', store=True, copy=True, tracking=100, )
    exchange_rate = fields.Float(string='Tasa de Cambio', store=True, copy=True, tracking=100, )
    full_reconcile_id = fields.Many2one(string='Conciliación', store=True, readonly=True, tracking=0,
                                        comodel_name='account.full.reconcile', )
    journal_id = fields.Many2one(string='Diario', store=True, copy=True, tracking=100,
                                 comodel_name='account.journal', )
    local_currency_id = fields.Many2one(string='Moneda Local', store=True, readonly=True, tracking=0,
                                        comodel_name='res.currency', )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='anticipocliente_message_channel_ids_rel',
                                           column1='anticipocliente_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='anticipocliente_message_partner_ids_rel',
                                           column1='anticipocliente_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    move_id = fields.Many2one(string='Comprobante', store=True, copy=True, tracking=100,
                              comodel_name='account.move', )
    move_line_id = fields.Many2one(string='Linea a reconciliar', store=True, copy=True, tracking=100,
                                   comodel_name='account.move.line', )
    move_nama = fields.Char(string='Nombre del comprobante', store=True, copy=True, tracking=0, )
    multicurrency = fields.Boolean(string='Multimoneda', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=100, )
    partner_id = fields.Many2one(string='Cliente', store=True, copy=True, tracking=100, comodel_name='res.partner', )
    pay_date = fields.Date(string='Fecha de Pago', store=True, copy=True, tracking=100, )
    planned_date = fields.Date(string='Fecha planificada', store=True, copy=True, tracking=100, )
    remaining = fields.Float(string='Balance', readonly=True, tracking=0, )
    request_date = fields.Date(string='Fecha de solicitud', store=True, copy=True, tracking=100, )
    sale_id = fields.Many2one(string='Pedido de venta', store=True, copy=True, tracking=100,
                              comodel_name='sale.order', )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=100, comodel_name='res.users', )


class Anticipoempleado(models.Model):
    _name = 'hr.payroll.advance'
    _description = 'Anticipo Empleado'
    account_payable_id = fields.Many2one(string='Cuenta Por Pagar', store=True, copy=True, tracking=0,
                                         comodel_name='account.account', )
    account_receivable_id = fields.Many2one(string='Cuenta Por Cobrar', store=True, copy=True, tracking=0,
                                            comodel_name='account.account', )
    accounting_date = fields.Date(string='Fecha de Contabilización', store=True, copy=True, tracking=0, )
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Next Activity Type', tracking=0, comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    amount_currency = fields.Float(string='Valor', store=True, copy=True, tracking=0, )
    analytic_account_id = fields.Many2one(string='Centro de costo', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    approve_date = fields.Date(string='Fecha de Aprobación', store=True, copy=True, tracking=0, )
    company_amount_currency = fields.Float(string='Valor Moneda Local', readonly=True, tracking=0, )
    company_currency_id = fields.Many2one(string='Moneda de la Compañia', readonly=True, tracking=0,
                                          comodel_name='res.currency', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    contract_id = fields.Many2one(string='Contrato', store=True, copy=True, tracking=0, comodel_name='hr.contract', )
    currency_id = fields.Many2one(string='Moneda', store=True, copy=True, tracking=0, comodel_name='res.currency', )
    description = fields.Text(string='Descripción', store=True, copy=True, tracking=0, )
    difference = fields.Float(string='Diferencia', store=True, readonly=True, tracking=0, )
    egress_move_id = fields.Many2one(string='Comprobante de Egreso', store=True, copy=True, tracking=0,
                                     comodel_name='account.move', )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    end_date = fields.Date(string='Fecha final', store=True, copy=True, tracking=0, )
    exchange_rate = fields.Float(string='Tasa de Cambio', store=True, copy=True, tracking=0, )
    expire_date = fields.Date(string='Fecha de Vencimiento', store=True, readonly=True, tracking=0, )
    financial_approver_id = fields.Many2one(string='Aprobador Financiero', readonly=True, tracking=100,
                                            comodel_name='hr.employee', )
    full_reconcile_id = fields.Many2one(string='Conciliación', readonly=True, tracking=0,
                                        comodel_name='account.full.reconcile', )
    is_paid = fields.Boolean(string='Esta pagado?', store=True, readonly=True, tracking=0, )
    journal_bank_id = fields.Many2one(string='Diario Anticipo', store=True, copy=True, tracking=0,
                                      comodel_name='account.journal', )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='anticipoempleado_message_channel_ids_rel',
                                           column1='anticipoempleado_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='anticipoempleado_message_partner_ids_rel',
                                           column1='anticipoempleado_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    move_line_id = fields.Many2one(string='Linea de Asiento', store=True, copy=True, tracking=0,
                                   comodel_name='account.move.line', )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    parent_id = fields.Many2one(string='Director', readonly=True, tracking=0, comodel_name='hr.employee', )
    partial_reconciled = fields.Boolean(string='Parcialmente Conciliado', readonly=True, tracking=0, )
    pay_date = fields.Date(string='Fecha de Pago', store=True, copy=True, tracking=0, )
    payment_reference = fields.Char(string='Referencia de Pago', store=True, copy=True, tracking=0, )
    payslip_id = fields.Many2one(string='Nomina', store=True, copy=True, tracking=0, comodel_name='hr.payslip', )
    refund_move_id = fields.Many2one(string='Comprobante Para Reembolson', store=True, copy=True, tracking=0,
                                     comodel_name='account.move', )
    refund_move_line_id = fields.Many2one(string='Linea de Reembolso', store=True, tracking=0,
                                          comodel_name='account.move.line', )
    remaining = fields.Float(string='Balance', store=True, tracking=0, )
    request_date = fields.Date(string='Fecha de Solicitud', store=True, copy=True, tracking=0, )
    start_date = fields.Date(string='Fecha de Inicio', store=True, copy=True, tracking=0, )
    total_expense = fields.Float(string='Total Legalizado', store=True, readonly=True, tracking=0, )
    validate_move_id = fields.Many2one(string='Comprobante de Validación', store=True, copy=True, tracking=0,
                                       comodel_name='account.move', )


class Anticipoproveedor(models.Model):
    _name = 'account.advance.supplier'
    _description = 'Anticipo Proveedor'
    account_analytic_id = fields.Many2one(string='Centro de Costo', store=True, copy=True, tracking=100,
                                          comodel_name='account.analytic.account', )
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Next Activity Type', tracking=0, comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    amount_local = fields.Float(string='Valor Moneda Local', store=True, readonly=True, tracking=0, )
    amount = fields.Float(string='Valor', store=True, copy=True, tracking=100, )
    bank_account_id = fields.Many2one(string='Cuenta Banco Beneficiario', store=True, copy=True, tracking=100,
                                      comodel_name='res.partner.bank', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=100, comodel_name='res.company', )
    crossed = fields.Boolean(string='Cruzado', store=True, copy=True, tracking=0, )
    currency_id = fields.Many2one(string='Moneda', store=True, copy=True, tracking=100, comodel_name='res.currency', )
    description = fields.Text(string='Descripción', store=True, copy=True, tracking=100, )
    exchange_rate = fields.Float(string='Tasa de Cambio', store=True, copy=True, tracking=100, )
    full_reconcile_id = fields.Many2one(string='Conciliación', store=True, readonly=True, tracking=0,
                                        comodel_name='account.full.reconcile', )
    journal_bank_id = fields.Many2one(string='Diario Banco', store=True, copy=True, tracking=100,
                                      comodel_name='account.journal', )
    local_currency_id = fields.Many2one(string='Moneda Local', store=True, readonly=True, tracking=0,
                                        comodel_name='res.currency', )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='anticipoproveedor_message_channel_ids_rel',
                                           column1='anticipoproveedor_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='anticipoproveedor_message_partner_ids_rel',
                                           column1='anticipoproveedor_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    move_id = fields.Many2one(string='Comprobante', store=True, copy=True, tracking=100,
                              comodel_name='account.move', )
    move_line_id = fields.Many2one(string='Linea a reconciliar', store=True, copy=True, tracking=100,
                                   comodel_name='account.move.line', )
    move_nama = fields.Char(string='Nombre del comprobante', store=True, copy=True, tracking=0, )
    multicurrency = fields.Boolean(string='Multimoneda', store=True, copy=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=100, )
    other_partner_id = fields.Many2one(string='Benificiario', store=True, copy=True, tracking=100,
                                       comodel_name='res.partner', )
    partner_id = fields.Many2one(string='Proveedor', store=True, copy=True, tracking=100,
                                 comodel_name='res.partner', )
    pay_date = fields.Date(string='Fecha de Pago', store=True, copy=True, tracking=100, )
    payment_mode_id = fields.Many2one(string='Modo de Pago', store=True, copy=True, tracking=100,
                                      comodel_name='account.payment.mode', )
    planned_date = fields.Date(string='Fecha planificada', store=True, copy=True, tracking=100, )
    purchase_order_id = fields.Many2one(string='Orden de compra', store=True, copy=True, tracking=100,
                                        comodel_name='purchase.order', )
    reference = fields.Char(string='Referencia de Pago', store=True, copy=True, tracking=100, )
    remaining = fields.Float(string='Balance', readonly=True, tracking=0, )
    request_date = fields.Date(string='Fecha de solicitud', store=True, copy=True, tracking=100, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=100, comodel_name='res.users', )


class Añofiscal(models.Model):
    _name = 'account.fiscal.year'
    _description = 'Año Fiscal'
    company_id = fields.Many2one(string='Compañía', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    date_from = fields.Date(string='Fecha de inicio', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    in_invoice_sent = fields.Integer(string='Documentos Soporte Enviados', store=True, copy=True, tracking=0, )
    in_refund_sent = fields.Integer(string='Notas Crédito de Documento Soporte Enviadas', store=True, copy=True,
                                    tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    niae_sent = fields.Integer(string='NIAE Sent', store=True, copy=True, tracking=0, )
    nie_sent = fields.Integer(string='NIE Sent', store=True, copy=True, tracking=0, )
    out_invoice_sent = fields.Integer(string='Facturas Enviadas', store=True, copy=True, tracking=0, )
    out_refund_credit_sent = fields.Integer(string='Notas de Crédito Enviadas', store=True, copy=True, tracking=0, )
    out_refund_debit_sent = fields.Integer(string='Notas de Débito Enviadas', store=True, copy=True, tracking=0, )


class Archivo(models.Model):
    _name = 'dms.file'
    _description = 'Archivo'
    access_token = fields.Char(string='Token de seguridad', store=True, tracking=0, )
    access_url = fields.Char(string='URL de acceso al portal', readonly=True, tracking=0, )
    access_warning = fields.Text(string='Aviso de acceso', readonly=True, tracking=0, )
    active = fields.Boolean(string='Archivado', store=True, copy=True, tracking=0, )
    activity_date_deadline = fields.Date(string='Fecha fin siguiente actividad', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Resumen de siguiente actividad', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Tipo de siguiente actividad', tracking=0,
                                       comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Usuario responsable', tracking=0, comodel_name='res.users', )
    attachment_id = fields.Many2one(string='Archivo adjunto', store=True, copy=True, tracking=0,
                                    comodel_name='ir.attachment', )
    category_id = fields.Many2one(string='Categoría', store=True, copy=True, tracking=0,
                                  comodel_name='dms.category', )
    checksum = fields.Char(string='Checksum/SHA1', index=True, store=True, readonly=True, copy=True, tracking=0, )
    color = fields.Integer(string='Color', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañía', index=True, store=True, readonly=True, tracking=0,
                                 comodel_name='res.company', )
    content_binary = fields.Binary(string='Contenido binario', store=True, copy=True, tracking=0, )
    content_file = fields.Binary(string='Contenido de archivo', store=True, copy=True, tracking=0, )
    content = fields.Binary(string='Contenido', required=True, tracking=0, )
    directory_id = fields.Many2one(string='Carpeta', index=True, store=True, required=True, copy=True, tracking=0,
                                   comodel_name='dms.directory', )
    extension = fields.Char(string='Extensión', store=True, readonly=True, tracking=0, )
    icon_url = fields.Char(string='Icon URL', readonly=True, tracking=0, )
    image_1024 = fields.Binary(string='Image 1024', store=True, readonly=True, tracking=0, )
    image_128 = fields.Binary(string='Image 128', store=True, readonly=True, tracking=0, )
    image_1920 = fields.Binary(string='Image', store=True, copy=True, tracking=0, )
    image_256 = fields.Binary(string='Image 256', store=True, readonly=True, tracking=0, )
    image_512 = fields.Binary(string='Image 512', store=True, readonly=True, tracking=0, )
    is_hidden = fields.Boolean(string='Almacenamiento está oculto', store=True, readonly=True, tracking=0, )
    is_lock_editor = fields.Boolean(string='Editor', readonly=True, tracking=0, )
    is_locked = fields.Boolean(string='Bloqueado', readonly=True, tracking=0, )
    locked_by = fields.Many2one(string='Bloqueado por', store=True, copy=True, tracking=0, comodel_name='res.users', )
    message_attachment_count = fields.Integer(string='Nº de adjuntos', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='archivo_message_channel_ids_rel', column1='archivo_id',
                                           column2='message_channel_ids_id', string='Seguidores (Canales)',
                                           readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Número de error', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Error de entrega de mensaje', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='Error de entrega de SMS', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Es Seguidor', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Adjunto principal', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Acción necesaria', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='archivo_message_partner_ids_rel', column1='archivo_id',
                                           column2='message_partner_ids_id', string='Seguidores (Contactos)',
                                           readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Nº de mensajes no leídos', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Mensajes no leídos', readonly=True, tracking=0, )
    migration = fields.Char(string='Estado de migración', readonly=True, tracking=0, )
    mimetype = fields.Char(string='Tipo', store=True, readonly=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', index=True, store=True, required=True, copy=True, tracking=0, )
    path_json = fields.Text(string='Path Json', readonly=True, tracking=0, )
    path_names = fields.Char(string='Nombres de ruta', readonly=True, tracking=0, )
    permission_create = fields.Boolean(string='Acceso de creación', readonly=True, tracking=0, )
    permission_read = fields.Boolean(string='Acceso de lectura', readonly=True, tracking=0, )
    permission_unlink = fields.Boolean(string='Acceso de eliminación', readonly=True, tracking=0, )
    permission_write = fields.Boolean(string='Acceso de escritura', readonly=True, tracking=0, )
    require_migration = fields.Boolean(string='Requiere migración', store=True, readonly=True, tracking=0, )
    res_id = fields.Integer(string='ID de registro de archivos adjuntos vinculados', index=True, store=True,
                            readonly=True,
                            tracking=0, )
    res_model = fields.Char(string='Modelo de adjuntos vinculado', index=True, store=True, readonly=True, tracking=0, )
    save_type = fields.Char(string='Tipo de guardado actual', readonly=True, tracking=0, )
    size = fields.Integer(string='Tamaño', store=True, readonly=True, copy=True, tracking=0, )
    storage_id = fields.Many2one(string='Almacenamiento', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='dms.storage', )
    tag_ids = fields.Many2many(relation='archivo_tag_ids_rel', column1='archivo_id', column2='tag_ids_id',
                               string='Etiquetas', store=True, copy=True, tracking=0, comodel_name='dms.tag', )


class Asistentecomprobantescontables(models.Model):
    _name = 'account.voucher.wizard'
    _description = 'Asistente Comprobantes contables'
    active_bool = fields.Boolean(string='Muchos', store=True, copy=True, tracking=0, )
    amount = fields.Monetary(string='Valor', store=True, copy=True, tracking=0, )
    company_currency_id = fields.Many2one(string='Moneda de la Compañía', readonly=True, tracking=0,
                                          comodel_name='res.currency', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    currency_id = fields.Many2one(string='Moneda', store=True, copy=True, tracking=0, comodel_name='res.currency', )
    date = fields.Date(string='Fecha', store=True, required=True, copy=True, tracking=0, )
    journal_id = fields.Many2one(string='Diario', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='account.journal', )
    voucher_reference = fields.Char(string='Referencia del Pago', store=True, copy=True, tracking=0, )


class Asistentedeactualizaciónmasiva(models.Model):
    _name = 'sh.helpdesk.ticket.mass.update.wizard'
    _description = 'Asistente de actualización masiva'
    assign_to_multiuser = fields.Many2many(relation='asistentecomprobante_assign_to_multiuser_rel',
                                           column1='asistentecomprobante_id', column2='assign_to_multiuser_id',
                                           string='Asignar múltiples usuarios', store=True, copy=True, tracking=0,
                                           comodel_name='res.users', )
    assign_to = fields.Many2one(string='Asignar a', store=True, copy=True, tracking=0, comodel_name='res.users', )
    check_add_remove = fields.Boolean(string='Agregar eliminar', store=True, copy=True, tracking=0, )
    check_assign_to_multiuser = fields.Boolean(string='Asignar múltiples usuarios', store=True, copy=True,
                                               tracking=0, )
    check_assign_to = fields.Boolean(string='Avisar a', store=True, copy=True, tracking=0, )
    check_helpdesks_state = fields.Boolean(string='Escenario', store=True, copy=True, tracking=0, )
    check_sh_display_multi_user = fields.Boolean(string='Verifique SH Display Multi User', store=True, copy=True,
                                                 tracking=0, )
    followers = fields.Many2many(relation='asistentecomprobante_followers_rel', column1='asistentecomprobante_id',
                                 column2='followers_id', string='Seguidores', store=True, copy=True, tracking=0,
                                 comodel_name='res.partner', )
    helpdesk_stages = fields.Many2one(string='Escenario', store=True, copy=True, tracking=0,
                                      comodel_name='helpdesk.stages', )
    helpdesks_ticket_ids = fields.Many2many(relation='asistentecomprobante_helpdesks_ticket_ids_rel',
                                            column1='asistentecomprobante_id', column2='helpdesks_ticket_ids_id',
                                            string='Ticket de servicio de ayuda', store=True, copy=True, tracking=0,
                                            comodel_name='helpdesk.ticket', )


class Asistentedeconsignación(models.Model):
    _name = 'account.consignment.wizard'
    _description = 'Asistente de Consignación'
    consignments_ids = fields.Many2many(relation='asistentecomprobante_consignments_ids_rel',
                                        column1='asistentecomprobante_id', column2='consignments_ids_id',
                                        string='Consignaciones', store=True, copy=True, tracking=0,
                                        comodel_name='account.consignment', )


class Asistentedeextracto(models.Model):
    _name = 'account.financial.report.abstract.wizard'
    _description = 'Asistente de Extracto'
    company_id = fields.Many2one(string='Compañía', store=True, copy=True, tracking=0, comodel_name='res.company', )


class Asistentedeinformedelibrodiario(models.Model):
    _name = 'journal.ledger.report.wizard'
    _description = 'Asistente de informe de Libro Diario'
    company_id = fields.Many2one(string='Compañía', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha de inicio', store=True, required=True, copy=True, tracking=0, )
    date_range_id = fields.Many2one(string='Periodo', store=True, copy=True, tracking=0, comodel_name='date.range', )
    date_to = fields.Date(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    foreign_currency = fields.Boolean(string='Moneda Extranjera', store=True, copy=True, tracking=0, )
    journal_ids = fields.Many2many(relation='asistentedeinformede_journal_ids_rel', column1='asistentedeinformede_id',
                                   column2='journal_ids_id', string='Diarios', store=True, copy=True, tracking=0,
                                   comodel_name='account.journal', )
    with_account_name = fields.Boolean(string='Cuenta con Nombre', store=True, copy=True, tracking=0, )
    with_auto_sequence = fields.Boolean(string='Show Auto Sequence', store=True, copy=True, tracking=0, )


class Asistentedeinformedelibromayor(models.Model):
    _name = 'general.ledger.report.wizard'
    _description = 'Asistente de informe de Libro Mayor'
    account_code_from = fields.Many2one(string='Código Cuenta Desde', store=True, copy=True, tracking=0,
                                        comodel_name='account.account', )
    account_code_to = fields.Many2one(string='Código Cuenta Hasta', store=True, copy=True, tracking=0,
                                      comodel_name='account.account', )
    account_ids = fields.Many2many(
        'account.account',
        relation='gl_wiz_account_rel',
        column1='wiz_id',
        column2='acc_id',
        string='Cuentas',
        copy=False,
    )
    account_journal_ids = fields.Many2many(relation='asistentedeinformede_account_journal_ids_rel',
                                           column1='asistentedeinformede_id', column2='account_journal_ids_id',
                                           string='Filtrar por diarios', store=True, copy=True, tracking=0,
                                           comodel_name='account.journal', )
    analytic_tag_ids = fields.Many2many(relation='asistentedeinformede_analytic_tag_ids_rel',
                                        column1='asistentedeinformede_id', column2='analytic_tag_ids_id',
                                        string='Filtrar por etiquetas analíticas', store=True, copy=True, tracking=0,
                                        comodel_name='account.analytic.tag', )
    centralize = fields.Boolean(string='Activar centralización', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañía', store=True, copy=True, tracking=0, comodel_name='res.company', )
    cost_center_ids = fields.Many2many(relation='asistentedeinformede_cost_center_ids_rel',
                                       column1='asistentedeinformede_id', column2='cost_center_ids_id',
                                       string='Filtro centro de costos', store=True, copy=True, tracking=0,
                                       comodel_name='account.analytic.account', )
    date_from = fields.Date(string='Fecha de inicio', store=True, required=True, copy=True, tracking=0, )
    date_range_id = fields.Many2one(string='Periodo', store=True, copy=True, tracking=0, comodel_name='date.range', )
    date_to = fields.Date(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    domain = fields.Char(string='Journal Items Domain', store=True, copy=True, tracking=0, )
    foreign_currency = fields.Boolean(string='Mostrar Moneda Extranjera', store=True, copy=True, tracking=0, )
    fy_start_date = fields.Date(string='Fecha Inicio', readonly=True, tracking=0, )
    hide_account_at_0 = fields.Boolean(string='Ocultar saldos finales con valor a 0', store=True, copy=True,
                                       tracking=0, )
    not_only_one_unaffected_earnings_account = fields.Boolean(string='No solo una cuenta de ganancias no afectadas',
                                                              store=True, readonly=True, copy=True, tracking=0, )
    partner_ids = fields.Many2many(relation='asistentedeinformede_partner_ids_rel', column1='asistentedeinformede_id',
                                   column2='partner_ids_id', string='Filtrar empresa', store=True, copy=True,
                                   tracking=0,
                                   comodel_name='res.partner', )
    payable_accounts_only = fields.Boolean(string='Sólo cuentas a pagar', store=True, copy=True, tracking=0, )
    receivable_accounts_only = fields.Boolean(string='Sólo cuentas a cobrar', store=True, copy=True, tracking=0, )
    show_analytic_tags = fields.Boolean(string='Mostrar etiquetas analíticas', store=True, copy=True, tracking=0, )
    show_cost_center = fields.Boolean(string='Mostrar etiquetas analíticas', store=True, copy=True, tracking=0, )
    unaffected_earnings_account = fields.Many2one(string='Cuenta de Ganancias No Afectadas', store=True, readonly=True,
                                                  tracking=0, comodel_name='account.account', )


class Asistentedeinformedepartidasabiertas(models.Model):
    _name = 'open.items.report.wizard'
    _description = 'Asistente de informe de partidas abiertas'
    account_code_from = fields.Many2one(string='Código Cuenta Desde', store=True, copy=True, tracking=0,
                                        comodel_name='account.account', )
    account_code_to = fields.Many2one(string='Código Cuenta Hasta', store=True, copy=True, tracking=0,
                                      comodel_name='account.account', )
    account_ids = fields.Many2many(
        'account.account',
        relation='open_items_wiz_account_rel',
        column1='wiz_id',
        column2='acc_id',
        string='Cuentas',
        copy=False,
    )
    account_journal_ids = fields.Many2many(relation='asistentedeinformede_account_journal_ids_rel',
                                           column1='asistentedeinformede_id', column2='account_journal_ids_id',
                                           string='Diario Contable', store=True, copy=True, tracking=0,
                                           comodel_name='account.journal', )
    company_id = fields.Many2one(string='Compañía', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_at = fields.Date(string='Fecha a', store=True, required=True, copy=True, tracking=0, )
    date_from = fields.Date(string='Fecha de inicio', store=True, copy=True, tracking=0, )
    foreign_currency = fields.Boolean(string='Mostrar Moneda Extranjera', store=True, copy=True, tracking=0, )
    hide_account_at_0 = fields.Boolean(string='Ocultar saldos finales con valor a 0', store=True, copy=True,
                                       tracking=0, )
    partner_ids = fields.Many2many(relation='asistentedeinformede_partner_ids_rel', column1='asistentedeinformede_id',
                                   column2='partner_ids_id', string='Filtrar empresa', store=True, copy=True,
                                   tracking=0,
                                   comodel_name='res.partner', )
    payable_accounts_only = fields.Boolean(string='Sólo cuentas a pagar', store=True, copy=True, tracking=0, )
    receivable_accounts_only = fields.Boolean(string='Sólo cuentas a cobrar', store=True, copy=True, tracking=0, )
    show_partner_details = fields.Boolean(string='Mostrar detalles de empresa', store=True, copy=True, tracking=0, )


class Asistentedeinformetesoreriaycartera(models.Model):
    _name = 'aged.partner.balance.report.wizard'
    _description = 'Asistente de Informe Tesoreria y Cartera'
    account_code_from = fields.Many2one(string='Código Cuenta Desde', store=True, copy=True, tracking=0,
                                        comodel_name='account.account', )
    account_code_to = fields.Many2one(string='Código Cuenta Hasta', store=True, copy=True, tracking=0,
                                      comodel_name='account.account', )
    account_ids = fields.Many2many(relation='asistentedeinformete_account_ids_rel', column1='asistentedeinformete_id',
                                   column2='account_ids_id', string='Filtro Cuentas', store=True, required=True,
                                   copy=True, tracking=0,
                                   comodel_name='account.account', )
    account_journal_ids = fields.Many2many(relation='asistentedeinformete_account_journal_ids_rel',
                                           column1='asistentedeinformete_id', column2='account_journal_ids_id',
                                           string='Diario Contable', store=True, copy=True, tracking=0,
                                           comodel_name='account.journal', )
    company_id = fields.Many2one(string='Compañía', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_at = fields.Date(string='Fecha a', store=True, required=True, copy=True, tracking=0, )
    date_from = fields.Date(string='Fecha de inicio', store=True, copy=True, tracking=0, )
    partner_ids = fields.Many2many(relation='asistentedeinformete_partner_ids_rel', column1='asistentedeinformete_id',
                                   column2='partner_ids_id', string='Filtrar empresa', store=True, copy=True,
                                   tracking=0,
                                   comodel_name='res.partner', )
    payable_accounts_only = fields.Boolean(string='Sólo cuentas a pagar', store=True, copy=True, tracking=0, )
    receivable_accounts_only = fields.Boolean(string='Sólo cuentas a cobrar', store=True, copy=True, tracking=0, )
    show_move_line_details = fields.Boolean(string='Mostrar Detalles Apuntes', store=True, copy=True, tracking=0, )


class Asistentedelinformedebalancedesumasysaldos(models.Model):
    _name = 'trial.balance.report.wizard'
    _description = 'Asistente del informe de balance de sumas y saldos'
    account_code_from = fields.Many2one(string='Código Cuenta Desde', store=True, copy=True, tracking=0,
                                        comodel_name='account.account', )
    account_code_to = fields.Many2one(string='Código Cuenta Hasta', store=True, copy=True, tracking=0,
                                      comodel_name='account.account', )
    account_ids = fields.Many2many(relation='asistentedelinformed_account_ids_rel', column1='asistentedelinformed_id',
                                   column2='account_ids_id', string='Filtro Cuentas', store=True, copy=True, tracking=0,
                                   comodel_name='account.account', )
    company_id = fields.Many2one(string='Compañía', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha de inicio', store=True, required=True, copy=True, tracking=0, )
    date_range_id = fields.Many2one(string='Periodo', store=True, copy=True, tracking=0, comodel_name='date.range', )
    date_to = fields.Date(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    foreign_currency = fields.Boolean(string='Mostrar Moneda Extranjera', store=True, copy=True, tracking=0, )
    fy_start_date = fields.Date(string='Fecha Inicio', readonly=True, tracking=0, )
    hide_account_at_0 = fields.Boolean(string='Ocultar cuentas a 0', store=True, copy=True, tracking=0, )
    hide_parent_hierarchy_level = fields.Boolean(string='No mostrar niveles padre', store=True, copy=True,
                                                 tracking=0, )
    journal_ids = fields.Many2many(relation='asistentedelinformed_journal_ids_rel', column1='asistentedelinformed_id',
                                   column2='journal_ids_id', string='Diario', store=True, copy=True, tracking=0,
                                   comodel_name='account.journal', )
    limit_hierarchy_level = fields.Boolean(string='Limitar niveles de jerarquía', store=True, copy=True, tracking=0, )
    not_only_one_unaffected_earnings_account = fields.Boolean(string='No solo una cuenta de ganancias no afectadas',
                                                              store=True, readonly=True, copy=True, tracking=0, )
    partner_ids = fields.Many2many(relation='asistentedelinformed_partner_ids_rel', column1='asistentedelinformed_id',
                                   column2='partner_ids_id', string='Filtrar empresa', store=True, copy=True,
                                   tracking=0,
                                   comodel_name='res.partner', )
    payable_accounts_only = fields.Boolean(string='Sólo cuentas a pagar', store=True, copy=True, tracking=0, )
    receivable_accounts_only = fields.Boolean(string='Sólo cuentas a cobrar', store=True, copy=True, tracking=0, )
    show_hierarchy_level = fields.Integer(string='Niveles de Jerarquía a mostrar', store=True, copy=True,
                                          tracking=0, )
    show_hierarchy = fields.Boolean(string='Show hierarchy', store=True, copy=True, tracking=0, )
    show_partner_details = fields.Boolean(string='Mostrar detalles de empresa', store=True, copy=True, tracking=0, )
    unaffected_earnings_account = fields.Many2one(string='Cuenta de Ganancias No Afectadas', store=True, readonly=True,
                                                  tracking=0, comodel_name='account.account', )


class Asistentedeseleccióndetransportista(models.Model):
    _name = 'choose.delivery.carrier'
    _description = 'Asistente de selección de transportista'
    available_carrier_ids = fields.Many2many(relation='asistentedelinformed_available_carrier_id_rel',
                                             column1='asistentedelinformed_id', column2='available_carrier_id_id',
                                             string='Operadores disponibles', readonly=True, tracking=0,
                                             comodel_name='delivery.carrier', )
    carrier_id = fields.Many2one(string='Método de envío', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='delivery.carrier', )
    company_id = fields.Many2one(string='Compañía', readonly=True, tracking=0, comodel_name='res.company', )
    currency_id = fields.Many2one(string='Moneda', readonly=True, tracking=0, comodel_name='res.currency', )
    delivery_message = fields.Text(string='Mensaje de entrega', store=True, readonly=True, copy=True, tracking=0, )
    delivery_price = fields.Float(string='Precio de envío', store=True, copy=True, tracking=0, )
    display_price = fields.Float(string='Costo', store=True, readonly=True, copy=True, tracking=0, )
    invoicing_message = fields.Text(string='Mensaje de facturación', readonly=True, tracking=0, )
    order_id = fields.Many2one(string='Pedido', store=True, required=True, copy=True, tracking=0,
                               comodel_name='sale.order', )
    partner_id = fields.Many2one(string='Cliente', readonly=True, required=True, tracking=0,
                                 comodel_name='res.partner', )


class Asistenteinformedeimpuestos(models.Model):
    _name = 'vat.report.wizard'
    _description = 'Asistente Informe de impuestos'
    company_id = fields.Many2one(string='Compañía', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha de comienzo', store=True, required=True, copy=True, tracking=0, )
    date_range_id = fields.Many2one(string='Periodo', store=True, copy=True, tracking=0, comodel_name='date.range', )
    date_to = fields.Date(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    tax_detail = fields.Boolean(string='Detalle de impuestos', store=True, copy=True, tracking=0, )


class Asistenteparacrearlíneasdepago(models.Model):
    _name = 'account.payment.line.create'
    _description = 'Asistente para crear líneas de pago'
    allow_blocked = fields.Boolean(string='Permitir apuntes en litigio', store=True, copy=True, tracking=0, )
    due_date = fields.Date(string='Fecha de vencimiento', store=True, copy=True, tracking=0, )
    invoice = fields.Boolean(string='Vinculado a una factura o factura rectificativa', store=True, copy=True,
                             tracking=0, )
    journal_ids = fields.Many2many(relation='asistenteinformedeim_journal_ids_rel', column1='asistenteinformedeim_id',
                                   column2='journal_ids_id', string='Filtro de diarios', store=True, copy=True,
                                   tracking=0,
                                   comodel_name='account.journal', )
    move_date = fields.Date(string='Fecha del asiento', store=True, copy=True, tracking=0, )
    move_line_ids = fields.Many2many(relation='asistenteinformedeim_move_line_ids_rel',
                                     column1='asistenteinformedeim_id', column2='move_line_ids_id', string='Apuntes',
                                     store=True, copy=True, tracking=0,
                                     comodel_name='account.move.line', )
    order_id = fields.Many2one(string='Orden de pago', store=True, copy=True, tracking=0,
                               comodel_name='account.payment.order', )
    partner_ids = fields.Many2many(relation='asistenteinformedeim_partner_ids_rel', column1='asistenteinformedeim_id',
                                   column2='partner_ids_id', string='Empresa', store=True, copy=True, tracking=0,
                                   comodel_name='res.partner', )


class Asistenteseleccióndeempaquetado(models.Model):
    _name = 'choose.delivery.package'
    _description = 'Asistente selección de empaquetado'
    company_id = fields.Many2one(string='Compañía', readonly=True, tracking=0, comodel_name='res.company', )
    delivery_packaging_id = fields.Many2one(string='Empaquetado', store=True, copy=True, tracking=0,
                                            comodel_name='product.packaging', )
    picking_id = fields.Many2one(string='Recolección', store=True, copy=True, tracking=0,
                                 comodel_name='stock.picking', )
    shipping_weight = fields.Float(string='Peso del envío', store=True, copy=True, tracking=0, )
    weight_uom_name = fields.Char(string='Etiqueta de unidad de medida de peso', readonly=True, tracking=0, )


class Auditaction(models.Model):
    _name = 'audit.action'
    _description = 'Audit Action'
    action_ids = fields.Many2many(relation='auditaction_action_ids_rel', column1='auditaction_id',
                                  column2='action_ids_id', string='No conformidades', store=True, copy=True, tracking=0,
                                  comodel_name='audit.nonconformity', )
    date_end = fields.Datetime(string='Fecha Limite', store=True, required=True, copy=True, tracking=0, )
    description = fields.Text(string='Descripcion', store=True, required=True, copy=True, tracking=0, )
    enviado = fields.Boolean(string='Notificacion Mail Enviada', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    responsable_id = fields.Many2one(string='Responsable', store=True, required=True, copy=True, tracking=0,
                                     comodel_name='hr.employee', )


class Auditaudit(models.Model):
    _name = 'audit.audit'
    _description = 'Audit Audit'
    audit_planning_id = fields.Many2one(string='Planeacion de Auditoria', store=True, copy=True, tracking=0,
                                        comodel_name='audit.planning', )
    audit_user_ids = fields.Many2many('res.users', relation='audit_participants_rel', column1='audit_id',
                                      column2='user_id', string='Usuarios de auditoría')
    conclusiones = fields.Text(string='Conclusion', store=True, copy=True, tracking=0, )
    conformidad = fields.Float(string='Conformidad(%)', store=True, readonly=True, tracking=0, )
    date_end_planning = fields.Datetime(string='Fecha Final Planificada', store=True, required=True, copy=True,
                                        tracking=0, )
    date_end = fields.Datetime(string='Fecha Final Ejecutada', store=True, copy=True, tracking=0, )
    date_start_planning = fields.Datetime(string='Fecha Inicial Planificada', store=True, required=True, copy=True,
                                          tracking=0, )
    date_start = fields.Datetime(string='Fecha Inicial Ejecutada', store=True, copy=True, tracking=0, )
    depart_id = fields.Many2one(string='Departamento', store=True, copy=True, tracking=0,
                                comodel_name='hr.department', )
    duracion = fields.Float(string='Duracion(horas)', store=True, readonly=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='auditaudit_message_channel_ids_rel', column1='auditaudit_id',
                                           column2='message_channel_ids_id', string='Followers (Channels)',
                                           readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='auditaudit_message_partner_ids_rel', column1='auditaudit_id',
                                           column2='message_partner_ids_id', string='Followers (Partners)',
                                           readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    observaciones = fields.Text(string='Observaciones y Recomendaciones', store=True, copy=True, tracking=0, )
    period = fields.Char(string='Periodo de Rastreo', store=True, copy=True, tracking=0, )
    process_id = fields.Many2one(string='Proceso', store=True, copy=True, tracking=0, comodel_name='audit.process', )
    reference = fields.Char(string='Codigo', store=True, readonly=True, copy=True, tracking=0, )
    responsables_ids = fields.Many2many('res.users', relation='audit_responsables_rel', column1='audit_id',
                                        column2='user_id', string='Responsables', )

    system_id = fields.Many2one(string='Sistema de Gestion', store=True, required=True, copy=True, tracking=0,
                                comodel_name='audit.system', )


class Auditcause(models.Model):
    _name = 'audit.cause'
    _description = 'Audit Cause'
    cause_id = fields.Many2one(string='No conformidad', store=True, copy=True, tracking=0,
                               comodel_name='audit.nonconformity', )
    clasification = fields.Many2one(string='Clasificacion', store=True, required=True, copy=True, tracking=0,
                                    comodel_name='audit.cause.clasification', )
    description = fields.Text(string='Descripcion', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Auditcauseclasification(models.Model):
    _name = 'audit.cause.clasification'
    _description = 'Audit Cause Clasification'
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Auditevaluation(models.Model):
    _name = 'audit.evaluation'
    _description = 'Audit Evaluation'
    date_evaluation = fields.Datetime(string='Fecha de Evaluacion', store=True, required=True, copy=True,
                                      tracking=0, )
    description = fields.Text(string='Descripcion', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    nonconformity_ids = fields.Many2many(relation='auditevaluation_nonconformity_ids_rel', column1='auditevaluation_id',
                                         column2='nonconformity_ids_id', string='No conformidades', store=True,
                                         copy=True, tracking=0,
                                         comodel_name='audit.nonconformity', )
    responsable_id = fields.Many2one(string='Responsable', store=True, required=True, copy=True, tracking=0,
                                     comodel_name='hr.employee', )


class Auditindicator(models.Model):
    _name = 'audit.indicator'
    _description = 'Audit Indicator'
    definicion = fields.Text(string='Definicion', store=True, required=True, copy=True, tracking=0, )
    formula = fields.Char(string='Formula de Calculo', store=True, required=True, copy=True, tracking=0, )
    frecuencia_r = fields.Float(string='Frecuencia Recoleccion', store=True, required=True, copy=True, tracking=0, )
    frecuencia_s = fields.Float(string='Frecuencia Revision', store=True, required=True, copy=True, tracking=0, )
    fuente_info = fields.Text(string='Fuente de la Informacion', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    object_specific = fields.Char(string='Objetivo Especifico', store=True, required=True, copy=True, tracking=0, )
    objectivo = fields.Text(string='Objetivo', store=True, required=True, copy=True, tracking=0, )
    observaciones = fields.Text(string='Observaciones', store=True, copy=True, tracking=0, )
    process_id = fields.Many2one(string='Proceso', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='audit.process', )
    responsable_id = fields.Many2one(string='Responsable', store=True, required=True, copy=True, tracking=0,
                                     comodel_name='hr.employee', )
    type_indicator = fields.Many2one(string='Tipo de Indicador', store=True, required=True, copy=True, tracking=0,
                                     comodel_name='audit.indicator.type', )
    uom_id = fields.Many2one(string='Unidad de medida', store=True, required=True, copy=True, tracking=0,
                             comodel_name='uom.uom', )
    users_ids = fields.Many2many(relation='auditindicator_users_ids_rel', column1='auditindicator_id',
                                 column2='users_ids_id', string='Usuarios', store=True, copy=True, tracking=0,
                                 comodel_name='res.users', )


class Auditindicatorrango(models.Model):
    _name = 'audit.indicator.rango'
    _description = 'Audit Indicator Rango'
    indicator_id = fields.Many2one(string='Indicador', store=True, copy=True, tracking=0,
                                   comodel_name='audit.indicator', )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    rang_inf = fields.Float(string='Rango Inferior', store=True, required=True, copy=True, tracking=0, )
    rang_sup = fields.Float(string='Rango Supeior', store=True, required=True, copy=True, tracking=0, )


class Auditindicatorresult(models.Model):
    _name = 'audit.indicator.result'
    _description = 'Audit Indicator Result'
    analysis = fields.Text(string='Analisis', store=True, copy=True, tracking=0, )
    date = fields.Date(string='Fecha Analisis', store=True, required=True, copy=True, tracking=0, )
    indicator_id = fields.Many2one(string='Indicador', store=True, copy=True, tracking=0,
                                   comodel_name='audit.indicator', )
    indicator_name = fields.Char(string='Nombre indicador', readonly=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='auditindicatorresult_message_channel_ids_rel',
                                           column1='auditindicatorresult_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='auditindicatorresult_message_partner_ids_rel',
                                           column1='auditindicatorresult_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    name = fields.Float(string='Resultado', store=True, required=True, copy=True, tracking=0, )
    uom_id = fields.Many2one(string='Unidad', store=True, readonly=True, tracking=0, comodel_name='uom.uom', )


class Auditindicatortype(models.Model):
    _name = 'audit.indicator.type'
    _description = 'Audit Indicator Type'
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Auditlist(models.Model):
    _name = 'audit.list'
    _description = 'Audit List'
    audit_audit_id = fields.Many2one(string='Auditoria', store=True, required=True, copy=True, tracking=0,
                                     comodel_name='audit.audit', )
    criterio_id = fields.Many2one(string='Criterio', store=True, readonly=True, tracking=0,
                                  comodel_name='audit.system', )
    hallazgo = fields.Text(string='Hallazgo', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Numeral', store=True, required=True, copy=True, tracking=0, )
    noconformidad_id = fields.Many2one(string='No conformidad', store=True, copy=True, tracking=0,
                                       comodel_name='audit.nonconformity', )
    pregunta = fields.Char(string='Aspecto a examinar', store=True, required=True, copy=True, tracking=0, )


class AuditlogDetallesderegistroCamposActualizados(models.Model):
    _name = 'auditlog.log.line.view'
    _description = 'Auditlog - Detalles de registro (campos actualizados)'
    field_description = fields.Char(string='Descripción', store=True, readonly=True, copy=True, tracking=0, )
    field_id = fields.Many2one(string='Campo', index=True, store=True, copy=True, tracking=0,
                               comodel_name='ir.model.fields', )
    field_name = fields.Char(string='Nombre técnico', store=True, readonly=True, copy=True, tracking=0, )
    http_request_id = fields.Many2one(string='Petición HTTP', index=True, store=True, copy=True, tracking=0,
                                      comodel_name='auditlog.http.request', )
    http_session_id = fields.Many2one(string='Sesión', index=True, store=True, copy=True, tracking=0,
                                      comodel_name='auditlog.http.session', )
    log_id = fields.Many2one(string='Registro', index=True, store=True, copy=True, tracking=0,
                             comodel_name='auditlog.log', )
    method = fields.Char(string='Método', store=True, copy=True, tracking=0, )
    model_id = fields.Many2one('ir.model', string='Modelo', required=True, index=True, ondelete='cascade', )
    model_model = fields.Char(string='Model Model', store=True, copy=True, tracking=0, )
    model_name = fields.Char(string='Model Name', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    new_value_text = fields.Text(string='Texto del valor nuevo', store=True, copy=True, tracking=0, )
    new_value = fields.Text(string='Valor nuevo', store=True, copy=True, tracking=0, )
    old_value_text = fields.Text(string='Texto del valor anterior', store=True, copy=True, tracking=0, )
    old_value = fields.Text(string='Valor anterior', store=True, copy=True, tracking=0, )
    res_id = fields.Integer(string='Res', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class AuditlogDetallesdeRegistro(models.Model):
    _name = 'auditlog.log.line'
    _description = 'Auditlog - Detalles de registro (campos actualizados)'
    field_description = fields.Char(string='Descripción', store=True, readonly=True, copy=True, tracking=0, )
    field_id = fields.Many2one(string='Campo', index=True, store=True, copy=True, tracking=0,
                               comodel_name='ir.model.fields', )
    field_name = fields.Char(string='Nombre técnico', store=True, readonly=True, copy=True, tracking=0, )
    log_id = fields.Many2one(string='Registro', index=True, store=True, copy=True, tracking=0,
                             comodel_name='auditlog.log', )
    new_value_text = fields.Text(string='Texto del valor nuevo', store=True, copy=True, tracking=0, )
    new_value = fields.Text(string='Valor nuevo', store=True, copy=True, tracking=0, )
    old_value_text = fields.Text(string='Texto del valor anterior', store=True, copy=True, tracking=0, )
    old_value = fields.Text(string='Valor anterior', store=True, copy=True, tracking=0, )


class AuditlogRegistro(models.Model):
    _name = 'auditlog.log'
    _description = 'Auditlog - Registro'
    http_request_id = fields.Many2one(string='Petición HTTP', index=True, store=True, copy=True, tracking=0,
                                      comodel_name='auditlog.http.request', )
    http_session_id = fields.Many2one(string='Sesión', index=True, store=True, copy=True, tracking=0,
                                      comodel_name='auditlog.http.session', )
    method = fields.Char(string='Método', store=True, copy=True, tracking=0, )
    model_id = fields.Many2one('ir.model', string='Modelo', required=True, index=True, ondelete='cascade', )
    model_model = fields.Char(string='Technical Model Name', store=True, readonly=True, copy=True, tracking=0, )
    model_name = fields.Char(string='Model Name', store=True, readonly=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre del recurso', store=True, copy=True, tracking=0, )
    res_id = fields.Integer(string='ID del recurso', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class AuditlogRegistrodeSesióndeUsuarioHTTP(models.Model):
    _name = 'auditlog.http.session'
    _description = 'Auditlog - Registro de sesión de usuario HTTP'
    name = fields.Char(string='ID de sesión', index=True, store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', index=True, store=True, copy=True, tracking=0,
                              comodel_name='res.users', )


class AuditlogRegla(models.Model):
    _name = 'auditlog.rule'
    _description = 'Auditlog - Regla'
    action_id = fields.Many2one(string='Acción', store=True, copy=True, tracking=0,
                                comodel_name='ir.actions.act_window', )
    capture_record = fields.Boolean(string='Capture Record', store=True, copy=True, tracking=0, )
    fields_to_exclude_ids = fields.Many2many(relation='auditlog_regla_fields_to_exclude_id_rel',
                                             column1='auditlog_regla_id', column2='fields_to_exclude_id_id',
                                             string='Fields to Exclude', store=True, copy=True, tracking=0,
                                             comodel_name='ir.model.fields', )
    log_create = fields.Boolean(string='Crear registros', store=True, copy=True, tracking=0, )
    log_read = fields.Boolean(string='Registrar lecturas', store=True, copy=True, tracking=0, )
    log_unlink = fields.Boolean(string='Borrar registros', store=True, copy=True, tracking=0, )
    log_write = fields.Boolean(string='Registrar modificaciones', store=True, copy=True, tracking=0, )
    model_id = fields.Many2one('ir.model', string='Modelo', required=True, index=True, ondelete='cascade', )
    model_model = fields.Char(string='Technical Model Name', store=True, readonly=True, copy=True, tracking=0, )
    model_name = fields.Char(string='Model Name', store=True, readonly=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    user_ids = fields.Many2many('res.users', relation='auditlog_rule_user_rel', column1='rule_id', column2='user_id',
                                string='Users')
    users_to_exclude_ids = fields.Many2many('res.users', relation='auditlog_rule_user_excl_rel', column1='rule_id',
                                            column2='user_id', string='Users to Exclude')


class AuditlogReigstrodepeticioneshttp(models.Model):
    _name = 'auditlog.http.request'
    _description = 'Auditlog - Reigstro de peticiones HTTP'
    http_session_id = fields.Many2one(string='Sesión', index=True, store=True, copy=True, tracking=0,
                                      comodel_name='auditlog.http.session', )
    name = fields.Char(string='Ruta', store=True, copy=True, tracking=0, )
    root_url = fields.Char(string='URL raíz', store=True, copy=True, tracking=0, )
    user_context = fields.Char(string='Contexto', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Auditnonconformity(models.Model):
    _name = 'audit.nonconformity'
    _description = 'Audit Nonconformity'
    action_ids = fields.Many2many(relation='auditnonconformity_action_ids_rel', column1='auditnonconformity_id',
                                  column2='action_ids_id', string='Acciones', store=True, tracking=0,
                                  comodel_name='audit.action', )
    audit_audit_id = fields.Many2one(string='Auditoria', store=True, tracking=0, comodel_name='audit.audit', )
    auditor_id = fields.Many2one(string='Auditor', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='hr.employee', )
    cargo_id = fields.Many2one(string='Cargo', store=True, readonly=True, tracking=0, comodel_name='hr.job', )
    cargo_r_id = fields.Many2one(string='Cargo del responsable', store=True, readonly=True, tracking=0,
                                 comodel_name='hr.job', )
    cause = fields.Text(string='Causa Raiz', store=True, tracking=0, )
    correccion = fields.Text(string='Correccion', store=True, copy=True, tracking=0, )
    crm_claim_id = fields.Many2one(string='Reclamacion', store=True, tracking=0, comodel_name='crm.claim', )
    date_done = fields.Date(string='Fecha de Cierre', store=True, readonly=True, copy=True, tracking=0, )
    date_validate = fields.Date(string='Fecha de Validacion', store=True, copy=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, required=True, tracking=0, )
    depart_id = fields.Many2one(string='Departamento', store=True, copy=True, tracking=0,
                                comodel_name='hr.department', )
    description = fields.Text(string='Descripcion', store=True, required=True, tracking=0, )
    employee_id = fields.Many2one(string='Reportante', store=True, tracking=0, comodel_name='hr.employee', )
    evaluation_ids = fields.Many2many(relation='auditnonconformity_evaluation_ids_rel', column1='auditnonconformity_id',
                                      column2='evaluation_ids_id', string='Verificacion de la Eficacia', store=True,
                                      tracking=0,
                                      comodel_name='audit.evaluation', )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='auditnonconformity_message_channel_ids_rel',
                                           column1='auditnonconformity_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='auditnonconformity_message_partner_ids_rel',
                                           column1='auditnonconformity_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, readonly=True, tracking=0, )
    observaciones = fields.Text(string='Observaciones', store=True, copy=True, tracking=0, )
    origin_ids = fields.Many2many(relation='auditnonconformity_origin_ids_rel', column1='auditnonconformity_id',
                                  column2='origin_ids_id', string='Origen No Conformidades', store=True, required=True,
                                  tracking=0,
                                  comodel_name='audit.nonconformity.origin', )
    partner_id = fields.Many2one(string='Tercero', store=True, tracking=0, comodel_name='res.partner', )
    process_id = fields.Many2one(string='Proceso', store=True, copy=True, tracking=0, comodel_name='audit.process', )
    reference = fields.Char(string='En relacion con', store=True, copy=True, tracking=0, )
    req_incumple = fields.Text(string='Requisito Incumple', store=True, required=True, tracking=0, )
    responsable_id = fields.Many2one(string='Responsable', store=True, required=True, copy=True, tracking=0,
                                     comodel_name='hr.employee', )
    system_id = fields.Many2one(string='Criterio', store=True, required=True, copy=True, tracking=0,
                                comodel_name='audit.system', )


class Auditnonconformityorigin(models.Model):
    _name = 'audit.nonconformity.origin'
    _description = 'Audit Nonconformity Origin'
    description = fields.Text(string='Descripcion', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    noconformidad_ids = fields.Many2many(relation='auditnonconformityor_noconformidad_ids_rel',
                                         column1='auditnonconformityor_id', column2='noconformidad_ids_id',
                                         string='Origen', store=True, copy=True, tracking=0,
                                         comodel_name='audit.nonconformity', )


class Auditobjectives(models.Model):
    _name = 'audit.objectives'
    _description = 'Audit Objectives'
    audit_id = fields.Many2one(string='Planeacion de Auditoria', store=True, copy=True, tracking=0,
                               comodel_name='audit.planning', )
    description = fields.Text(string='Descripcion', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Objetivo', store=True, required=True, copy=True, tracking=0, )


class Auditplanning(models.Model):
    _name = 'audit.planning'
    _description = 'Audit Planning'
    alcance = fields.Text(string='Alcance', store=True, required=True, copy=True, tracking=0, )
    date_end = fields.Datetime(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    date_start = fields.Datetime(string='Fecha Inicial', store=True, required=True, copy=True, tracking=0, )
    duracion = fields.Float(string='Duracion(horas)', store=True, readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    observaciones = fields.Text(string='Observaciones', store=True, copy=True, tracking=0, )
    reference = fields.Char(string='Codigo', store=True, readonly=True, copy=True, tracking=0, )
    responsables_ids = fields.Many2many(relation='auditplanning_responsables_ids_rel', column1='auditplanning_id',
                                        column2='responsables_ids_id', string='Responsables', store=True, required=True,
                                        copy=True, tracking=0,
                                        comodel_name='hr.employee', )
    system_id = fields.Many2one(string='Criterio', store=True, required=True, copy=True, tracking=0,
                                comodel_name='audit.system', )


class Auditprocess(models.Model):
    _name = 'audit.process'
    _description = 'Audit Process'
    audit_process_ids = fields.Many2many(relation='auditprocess_audit_process_ids_rel', column1='auditprocess_id',
                                         column2='audit_process_ids_id', string='Sistema de Gestion', store=True,
                                         copy=True, tracking=0,
                                         comodel_name='audit.system', )
    description = fields.Text(string='Descripcion', store=True, required=True, copy=True, tracking=0, )
    integrantes_ids = fields.Many2many(relation='auditprocess_integrantes_ids_rel', column1='auditprocess_id',
                                       column2='integrantes_ids_id', string='Integrantes', store=True, copy=True,
                                       tracking=0,
                                       comodel_name='hr.employee', )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    reference = fields.Char(string='Referencia', store=True, required=True, copy=True, tracking=0, )
    responsable_id = fields.Many2one(string='Responsable', store=True, required=True, copy=True, tracking=0,
                                     comodel_name='hr.employee', )


class Auditsystem(models.Model):
    _name = 'audit.system'
    _description = 'Audit System'
    description = fields.Text(string='Descripcion', store=True, required=True, copy=True, tracking=0, )
    employee_ids = fields.Many2many('hr.employee', relation='audit_system_employees_rel', column1='system_id',
                                    column2='employee_id', string='Empleados')
    integrantes_ids = fields.Many2many('hr.employee', relation='audit_system_integrantes_rel', column1='system_id',
                                       column2='employee_id', string='Integrantes', )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    process_ids = fields.Many2many(relation='auditsystem_process_ids_rel', column1='auditsystem_id',
                                   column2='process_ids_id', string='Procesos', store=True, required=True, copy=True,
                                   tracking=0,
                                   comodel_name='audit.process', )
    reference = fields.Char(string='Referencia', store=True, required=True, copy=True, tracking=0, )
    responsable_id = fields.Many2one(string='Responsable', store=True, required=True, copy=True, tracking=0,
                                     comodel_name='hr.employee', )


class AutocompletadodeobjetosapartirdeciudadesUbicaciones(models.Model):
    _name = 'res.city.zip'
    _description = 'Autocompletado de objetos a partir de ciudades/ubicaciones'
    city_id = fields.Many2one(string='Ciudad', index=True, store=True, required=True, copy=True, tracking=0,
                              comodel_name='res.city', )
    country_id = fields.Many2one(string='País', readonly=True, tracking=0, comodel_name='res.country', )
    name = fields.Char(string='C.P.', store=True, required=True, copy=True, tracking=0, )
    state_id = fields.Many2one(string='Provincia', readonly=True, tracking=0, comodel_name='res.country.state', )
    type = fields.Char(string='Tipo', store=True, copy=True, tracking=0, )


class Avancysaccountbankstatement(models.Model):
    _name = 'account.bank.statement.avancys'
    _description = 'Avancys Account Bank Statement'
    balance_account_end = fields.Float(string='Saldo Cuenta Libro Mayor a Fecha Final', readonly=True, tracking=0, )
    balance_account = fields.Float(string='Saldo Cuenta', store=True, copy=True, tracking=0, )
    balance_end_real = fields.Float(string='Ending Balance', store=True, copy=True, tracking=0, )
    balance_start = fields.Float(string='Starting Balance', store=True, copy=True, tracking=0, )
    bank_account_id = fields.Many2one(string='Cuenta bancaria', store=True, copy=True, tracking=0,
                                      comodel_name='res.partner.bank', )
    company_id = fields.Many2one(string='Compañía', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Desde', store=True, copy=True, tracking=0, )
    date_multi_get = fields.Date(string='Filtro fecha', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha Hasta', store=True, copy=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, required=True, copy=True, tracking=0, )
    file_name = fields.Char(string='Archivo', store=True, copy=True, tracking=0, )
    file = fields.Binary(string='Archivo', store=True, readonly=True, copy=True, tracking=0, )
    journal_id = fields.Many2one(string='Diario', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='account.journal', )
    match_cheque = fields.Boolean(string='Concilar cheques', store=True, copy=True, tracking=0, )
    match_dom = fields.Char(string='Dominio adicional', store=True, copy=True, tracking=0, )
    multi_move_amount = fields.Float(string='Total movimientos seleccionados', store=True, copy=True, tracking=0, )
    multi_trans_amount = fields.Float(string='Total transacciones seleccionadas', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    nc_not_account = fields.Float(string='N/C no contabilizadas', store=True, copy=True, tracking=0, )
    nd_not_account = fields.Float(string='N/D no contabilizadas', store=True, copy=True, tracking=0, )
    payment_pending = fields.Float(string='Pagos Pendientes', store=True, copy=True, tracking=0, )
    pending_consing_calculated = fields.Float(string='Ingresos Pendientes de Contabilizar (Calculado)', readonly=True,
                                              tracking=0, )
    pending_consing = fields.Float(string='Consignaciones Pendientes', store=True, copy=True, tracking=0, )
    rotated_check = fields.Float(string='Cheques Pendientes', store=True, copy=True, tracking=0, )
    simple_ref = fields.Char(string='Referencia omision cheque', store=True, copy=True, tracking=0, )
    trans_balance = fields.Float(string='Saldo calculado', store=True, copy=True, tracking=0, )
    unfind_move_ids = fields.Many2many(relation='avancysaccountbankst_unfind_move_ids_rel',
                                       column1='avancysaccountbankst_id', column2='unfind_move_ids_id',
                                       string='Movimiento contables no encontrados', store=True, readonly=True,
                                       copy=True,
                                       tracking=0, comodel_name='account.move.line', )
    value_multi_get = fields.Float(string='Filtro valor', store=True, copy=True, tracking=0, )


class Avancysaccountbankstatementline(models.Model):
    _name = 'account.bank.statement.line.avancys'
    _description = 'Avancys Account Bank Statement Line'
    account_id = fields.Many2one(string='Account', store=True, copy=True, tracking=0,
                                 comodel_name='account.account', )
    account_move_line_ids = fields.Many2many(relation='avancysaccountbankst_account_move_line_id_rel',
                                             column1='avancysaccountbankst_id', column2='account_move_line_id_id',
                                             string='Registros Relacionados', store=True, readonly=True, copy=True,
                                             tracking=0, comodel_name='account.move.line', )
    account_number = fields.Char(string='Bank Account Number', store=True, copy=True, tracking=0, )
    amount = fields.Monetary(string='Amount', store=True, copy=True, tracking=0, )
    avancys_statement_id = fields.Many2one(string='Statement', index=True, store=True, copy=True, tracking=0,
                                           comodel_name='account.bank.statement.avancys', )
    balance = fields.Float(string='Balance', store=True, readonly=True, copy=True, tracking=0, )
    bank_account_id = fields.Many2one(string='Bank Account', store=True, copy=True, tracking=0,
                                      comodel_name='res.partner.bank', )
    currency_id = fields.Many2one(string='Journal Currency', store=True, copy=True, tracking=0,
                                  comodel_name='res.currency', )
    date = fields.Date(string='Date', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    new_active_id = fields.Integer(string='New active id', store=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Partner', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    partner_name = fields.Char(string='Partner Name', store=True, copy=True, tracking=0, )
    ref = fields.Char(string='Ref', store=True, copy=True, tracking=0, )
    select = fields.Boolean(string='Select', store=True, readonly=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Sequence', index=True, store=True, copy=True, tracking=0, )
    statement_origin_id = fields.Many2one(string='Origen', index=True, store=True, copy=True, tracking=0,
                                          comodel_name='account.bank.statement.avancys', )


class Balancedepruebas(models.Model):
    _name = 'account.financial.report.trial.wizard'
    _description = 'Balance de Pruebas'
    company_id = fields.Many2one(string='Compañia', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='res.company', )


class BalancedePruebas(models.Model):
    _name = 'account.financial.report.balance'
    _description = 'Balance de Pruebas'
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_end = fields.Date(string='Fecha Fin', store=True, copy=True, tracking=0, )
    date_start = fields.Date(string='Fecha Inicio', store=True, copy=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )


class Balancedepruebaswizard(models.TransientModel):
    _name = 'account.financial.report.balance.wizard'
    _description = 'Balance de Pruebas Wizard'

    account_ids = fields.Many2many('account.account', relation='afr_balwiz_account_rel',
                                   column1='wizard_id', column2='account_id', string='Cuentas', copy=False)
    company_id = fields.Many2one('res.company', string='Compañía', readonly=True, copy=False)
    company_ids = fields.Many2many('res.company', relation='afr_balwiz_company_rel',
                                   column1='wizard_id', column2='company_id', string='Compañías', copy=False)
    date_start = fields.Date(string='Fecha Inicio')
    date_end = fields.Date(string='Fecha Fin')
    journal_ids = fields.Many2many('account.journal', relation='afr_balwiz_journal_rel',
                                   column1='wizard_id', column2='journal_id', string='Diarios', copy=False)
    levels_ids = fields.Many2many('account.financial.levels', relation='afr_balwiz_level_rel',
                                  column1='wizard_id', column2='level_id', string='Niveles', copy=False)
    partner_ids = fields.Many2many('res.partner', relation='afr_balwiz_partner_rel',
                                   column1='wizard_id', column2='partner_id', string='Terceros', copy=False)
    structure_id = fields.Many2one('account.financial.structure', string='Plan Contable', copy=False)


class Balancederesultados(models.Model):
    _name = 'account.financial.report.state.income'
    _description = 'Balance de Resultados'
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_end = fields.Date(string='Fecha Fin', store=True, copy=True, tracking=0, )
    date_start = fields.Date(string='Fecha Inicio', store=True, copy=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )


class Balancegeneral(models.Model):
    _name = 'account.financial.report.balance.general'
    _description = 'Balance General'
    account_ids = fields.Many2many(relation='balancegeneral_account_ids_rel', column1='balancegeneral_id',
                                   column2='account_ids_id', string='Cuentas', store=True, copy=True, tracking=0,
                                   comodel_name='account.account', )
    company_id = fields.Many2one(string='Compañia', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    date_end = fields.Date(string='Fecha de Corte', store=True, copy=True, tracking=0, )
    structure_id = fields.Many2one(string='Estructura', store=True, copy=True, tracking=0,
                                   comodel_name='account.financial.structure', )


class BalanceGeneral(models.Model):
    _name = 'account.financial.report.balance.general'
    _description = 'Balance General'
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_end = fields.Date(string='Fecha Fin', store=True, copy=True, tracking=0, )
    date_start = fields.Date(string='Fecha Inicio', store=True, copy=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )


class Balanceyinventario(models.Model):
    _name = 'account.financial.report.balance.inventory'
    _description = 'Balance y Inventario'
    account_ids = fields.Many2many('account.account', relation='afr_balinv_account_rel', column1='inventory_id',
                                   column2='account_id', string='Cuentas', copy=True, )
    company_id = fields.Many2one('res.company', string='Compañía', readonly=True, copy=True, )
    date_start = fields.Date(string='Fecha Inicio', copy=True)
    date_end = fields.Date(string='Fecha Fin', copy=True)
    levels_ids = fields.Many2many('account.financial.levels', relation='afr_balinv_level_rel', column1='inventory_id',
                                  column2='level_id', string='Niveles', copy=True, )
    partner_ids = fields.Many2many('res.partner', relation='afr_balinv_partner_rel', column1='inventory_id',
                                   column2='partner_id', string='Terceros', copy=True, )
    structure_id = fields.Many2one('account.financial.structure', string='Estructura', copy=True, )


class Calcularamortizaciones(models.Model):
    _name = 'account.asset.compute'
    _description = 'Calcular amortizaciones'
    date_end = fields.Date(string='Fecha', store=True, required=True, copy=True, tracking=0, )
    note = fields.Text(string='Nota', store=True, copy=True, tracking=0, )


class Calendariodehorasextra(models.Model):
    _name = 'hr.payroll.extrahours.type.time'
    _description = 'Calendario de Horas Extra'
    hour_from = fields.Float(string='Desde', store=True, required=True, copy=True, tracking=0, )
    hr_payroll_extrahours_type_id = fields.Many2one(string='Tipo de Hora Extra', store=True, copy=True, tracking=0,
                                                    comodel_name='hr.payroll.extrahours.type', )


class Cambiarfechadebloqueo(models.Model):
    _name = 'account.change.lock.date'
    _description = 'Cambiar Fecha de Bloqueo'
    fiscalyear_lock_date = fields.Date(string='Fecha de bloqueo para todos los usuarios', store=True, copy=True,
                                       tracking=0, )
    period_lock_date = fields.Date(string='Fecha establecida para no asesores', store=True, copy=True, tracking=0, )
    tax_lock_date = fields.Date(string='Fecha de bloqueo de impuestos', store=True, copy=True, tracking=0, )


class Capacitaciones(models.Model):
    _name = 'hr.capacitaciones'
    _description = 'Capacitaciones'
    adj_capacitacion = fields.Binary(string='Soporte Fisico', store=True, copy=True, tracking=0, )
    capacitacion_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0,
                                      comodel_name='hr.employee', )
    date_start = fields.Datetime(string='Fecha de inicio', store=True, required=True, copy=True, tracking=0, )
    date_stop = fields.Datetime(string='Fecha de Finalizacion', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Institucion', store=True, copy=True, tracking=0,
                                 comodel_name='res.partner', )
    size = fields.Integer(string='Duracion', store=True, required=True, copy=True, tracking=0, )


class Cargoadesempeñar(models.Model):
    _name = 'hr.contract.job.do'
    _description = 'Cargo a Desempeñar'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class Carpeta(models.Model):
    _name = 'dms.directory'
    _description = 'Carpeta'
    access_token = fields.Char(string='Token de seguridad', store=True, tracking=0, )
    access_url = fields.Char(string='URL de acceso al portal', readonly=True, tracking=0, )
    access_warning = fields.Text(string='Aviso de acceso', readonly=True, tracking=0, )
    activity_date_deadline = fields.Date(string='Fecha fin siguiente actividad', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Resumen de siguiente actividad', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Tipo de siguiente actividad', tracking=0,
                                       comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Usuario responsable', tracking=0, comodel_name='res.users', )
    alias_bounced_content = fields.Html(string='Custom Bounced Message', copy=True, tracking=0, )
    alias_defaults = fields.Text(string='Valores por defecto', required=True, copy=True, tracking=0, )
    alias_domain = fields.Char(string='Dominio de alias', readonly=True, tracking=0, )
    alias_force_thread_id = fields.Integer(string='ID de hilo de registro', copy=True, tracking=0, )
    alias_id = fields.Many2one(string='Alias', store=True, required=True, copy=True, tracking=0,
                               comodel_name='mail.alias', )
    alias_model_id = fields.Many2one('ir.model', string='Modelo con alias', required=True, index=True,
                                     ondelete='cascade', )
    alias_name = fields.Char(string='Nombre del Alias', tracking=0, )
    alias_parent_model_id = fields.Many2one(string='Grupo padre', index=True, comodel_name='ir.model',
                                            ondelete='set null')
    alias_parent_thread_id = fields.Integer(string='Ruta padre', copy=True, tracking=0, )
    alias_user_id = fields.Many2one(string='Sobrescribir', copy=True, tracking=0, comodel_name='res.users', )
    allowed_model_ids = fields.Many2many('ir.model', relation='carpeta_ir_model_rel', column1='carpeta_id',
                                         column2='model_id', string='Modelos vinculados', )
    category_id = fields.Many2one(string='Categoría', store=True, copy=True, tracking=0,
                                  comodel_name='dms.category', )
    color = fields.Integer(string='Color', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañía', index=True, store=True, readonly=True, tracking=0,
                                 comodel_name='res.company', )
    complete_group_ids = fields.Many2many('res.groups', relation='dms_directory_complete_group_rel',
                                          column1='directory_id',
                                          column2='group_id', string='Complete Groups', )
    complete_name = fields.Char(string='Nombre completo', store=True, readonly=True, tracking=0, )
    count_directories_title = fields.Char(string='Nº de subcarpetas', readonly=True, tracking=0, )
    count_directories = fields.Integer(string='Título de las carpetas de recuento', readonly=True, tracking=0, )
    count_elements = fields.Integer(string='Nº de elementos', readonly=True, tracking=0, )
    count_files_title = fields.Char(string='Nº de archivos', readonly=True, tracking=0, )
    count_files = fields.Integer(string='Título de los archivos de recuento', readonly=True, tracking=0, )
    count_total_directories = fields.Integer(string='Total subcarpetas', readonly=True, tracking=0, )
    count_total_elements = fields.Integer(string='Total elementos', readonly=True, tracking=0, )
    count_total_files = fields.Integer(string='Total archivos', readonly=True, tracking=0, )
    group_ids = fields.Many2many('res.groups', relation='dms_directory_group_rel', column1='directory_id',
                                 column2='group_id', string='Groups', )
    icon_url = fields.Char(string='Icon URL', readonly=True, tracking=0, )
    image_1024 = fields.Binary(string='Image 1024', store=True, readonly=True, tracking=0, )
    image_128 = fields.Binary(string='Image 128', store=True, readonly=True, tracking=0, )
    image_1920 = fields.Binary(string='Image', store=True, copy=True, tracking=0, )
    image_256 = fields.Binary(string='Image 256', store=True, readonly=True, tracking=0, )
    image_512 = fields.Binary(string='Image 512', store=True, readonly=True, tracking=0, )
    inherit_group_ids = fields.Boolean(string='Grupos heredados', store=True, copy=True, tracking=0, )
    is_hidden = fields.Boolean(string='Almacenamiento está oculto', store=True, readonly=True, tracking=0, )
    is_root_directory = fields.Boolean(string='Es carpeta raíz', store=True, copy=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Nº de adjuntos', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='carpeta_message_channel_ids_rel', column1='carpeta_id',
                                           column2='message_channel_ids_id', string='Seguidores (Canales)',
                                           readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Número de error', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Error de entrega de mensaje', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='Error de entrega de SMS', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Es Seguidor', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Adjunto principal', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Acción necesaria', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='carpeta_message_partner_ids_rel', column1='carpeta_id',
                                           column2='message_partner_ids_id', string='Seguidores (Contactos)',
                                           readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Nº de mensajes no leídos', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Mensajes no leídos', readonly=True, tracking=0, )
    model_id = fields.Many2one('ir.model', string='Modelo', required=True, index=True, ondelete='cascade', )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', index=True, store=True, required=True, copy=True, tracking=0, )
    parent_id = fields.Many2one(string='Categoría padre', index=True, store=True, copy=True, tracking=0,
                                comodel_name='dms.directory', )
    parent_path = fields.Char(string='Modelo padre', index=True, store=True, copy=True, tracking=0, )
    permission_create = fields.Boolean(string='Acceso de creación', readonly=True, tracking=0, )
    permission_read = fields.Boolean(string='Acceso de lectura', readonly=True, tracking=0, )
    permission_unlink = fields.Boolean(string='Acceso de eliminación', readonly=True, tracking=0, )
    permission_write = fields.Boolean(string='Acceso de escritura', readonly=True, tracking=0, )
    res_id = fields.Integer(string='ID de registro de archivos adjuntos vinculados', index=True, store=True,
                            copy=True, tracking=0, )
    res_model = fields.Char(string='Modelo de adjuntos vinculado', index=True, store=True, copy=True, tracking=0, )
    size = fields.Integer(string='Tamaño', readonly=True, tracking=0, )
    starred = fields.Boolean(string='Destacado', tracking=0, )
    storage_id_inherit_access_from_parent_record = fields.Boolean(string='Inherit permissions from related record',
                                                                  store=True, readonly=True, tracking=0, )
    storage_id = fields.Many2one(string='Almacenamiento', store=True, copy=True, tracking=0,
                                 comodel_name='dms.storage', )
    tag_ids = fields.Many2many(relation='carpeta_tag_ids_rel', column1='carpeta_id', column2='tag_ids_id',
                               string='Etiquetas', store=True, copy=True, tracking=0, comodel_name='dms.tag', )
    user_star_ids = fields.Many2many(relation='carpeta_user_star_ids_rel', column1='carpeta_id',
                                     column2='user_star_ids_id', string='Estrellas', store=True, copy=True, tracking=0,
                                     comodel_name='res.users', )


class Categoríadeactivo(models.Model):
    _name = 'account.asset.profile'
    _description = 'Categoría de activo'
    account_analytic_id = fields.Many2one(string='Cuenta Analítica', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    account_asset_ganancia_id = fields.Many2one(string='Cuenta de Gasto Baja Activo por Venta', store=True, copy=True,
                                                tracking=0, comodel_name='account.account', )
    account_asset_id = fields.Many2one(string='Cuenta de activo', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    account_cost_depreciation_id = fields.Many2one(string='Cuenta de costos de amortizacion', store=True, copy=True,
                                                   tracking=0, comodel_name='account.account', )
    account_depreciation_id = fields.Many2one(string='Cuenta de amortización', store=True, required=True, copy=True,
                                              tracking=0, comodel_name='account.account', )
    account_expense_depreciation_id = fields.Many2one(string='Cuenta de gastos de amortización', store=True,
                                                      required=True, copy=True, tracking=0,
                                                      comodel_name='account.account', )
    account_gasto_de_venta_depreciation_id = fields.Many2one(string='Cuenta de gasto de venta de amortizacion',
                                                             store=True, copy=True, tracking=0,
                                                             comodel_name='account.account', )
    account_min_value_id = fields.Many2one(string='Cuenta para pérdida de valor', store=True, copy=True, tracking=0,
                                           comodel_name='account.account', )
    account_plus_value_id = fields.Many2one(string='Cuenta para ganancia de valor', store=True, copy=True, tracking=0,
                                            comodel_name='account.account', )
    account_residual_value_id = fields.Many2one(string='Cuenta de valor residual', store=True, copy=True, tracking=0,
                                                comodel_name='account.account', )
    active = fields.Boolean(string='Activo', store=True, copy=True, tracking=0, )
    analytic_tag_ids = fields.Many2many(relation='carpeta_analytic_tag_ids_rel', column1='carpeta_id',
                                        column2='analytic_tag_ids_id', string='Analytic tags', store=True, copy=True,
                                        tracking=0,
                                        comodel_name='account.analytic.tag', )
    asset_product_item = fields.Boolean(string='Crear un activo por artículo de producto', store=True, copy=True,
                                        tracking=0, )
    company_id = fields.Many2one(string='Compañía', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    days_calc = fields.Boolean(string='Calcular por días', store=True, copy=True, tracking=0, )
    group_ids = fields.Many2many(relation='carpeta_group_ids_rel', column1='carpeta_id', column2='group_ids_id',
                                 string='Grupos de activo', store=True, copy=True, tracking=0,
                                 comodel_name='account.asset.group', )
    journal_eliminated_id = fields.Many2one(string='Diario Baja Activo Deterioro Total', store=True, copy=True,
                                            tracking=0, comodel_name='account.journal', )
    journal_eliminated_id1 = fields.Many2one(string='Diario Baja Activo Deterioro Total', store=True, copy=True,
                                             tracking=0, comodel_name='account.journal', )
    journal_eliminated_id2 = fields.Many2one(string='Diario Baja Activo por Perdida', store=True, copy=True,
                                             tracking=0, comodel_name='account.journal', )
    journal_id = fields.Many2one(string='Diario', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='account.journal', )
    method_number = fields.Integer(string='Número de años', store=True, copy=True, tracking=0, )
    method_progress_factor = fields.Float(string='Factor decreciente', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', index=True, store=True, required=True, copy=True, tracking=0, )
    note = fields.Text(string='Nota', store=True, copy=True, tracking=0, )
    open_asset = fields.Boolean(string='Omitir estado borrador', store=True, copy=True, tracking=0, )
    property_account_eliminated_id = fields.Many2one(string='Cuenta de Gasto Baja Activo por Perdida', store=True,
                                                     copy=True, tracking=0, comodel_name='account.account', )
    prorata = fields.Boolean(string='Tiempo prorrateado', store=True, copy=True, tracking=0, )
    use_leap_years = fields.Boolean(string='Use años bisiestos', store=True, copy=True, tracking=0, )


class Categoríadehorasextras(models.Model):
    _name = 'hr.overtime.type'
    _description = 'Categoría de Horas Extras'
    active = fields.Boolean(string='Activo', store=True, copy=True, tracking=0, )
    apr_adm_credit = fields.Many2one(string='Credito Aprendiz Administrativo', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    apr_adm_debit = fields.Many2one(string='Debito Aprendiz Administrativo', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    apr_com_credit = fields.Many2one(string='Credito Aprendiz Comercial', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    apr_com_debit = fields.Many2one(string='Debito Aprendiz Comercial', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    apr_ope_credit = fields.Many2one(string='Credito Aprendiz Operativa', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    apr_ope_debit = fields.Many2one(string='Debito Aprendiz Operativa', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    apr_pro_credit = fields.Many2one(string='Credito Aprendiz Producción', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    apr_pro_debit = fields.Many2one(string='Debito Aprendiz Producción', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    code = fields.Char(string='Código', store=True, required=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    eso_to_compensate = fields.Boolean(string='ESO/ESU A compensar', store=True, copy=True, tracking=0, )
    int_adm_credit = fields.Many2one(string='Credito Integral Administrativo', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    int_adm_debit = fields.Many2one(string='Debito Integral Administrativo', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    int_com_credit = fields.Many2one(string='Credito Integral Comercial', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    int_com_debit = fields.Many2one(string='Debito Integral Comercial', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    int_ope_credit = fields.Many2one(string='Credito Integral Operativa', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    int_ope_debit = fields.Many2one(string='Debito Integral Operativa', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    int_pro_credit = fields.Many2one(string='Credito Integral Producción', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    int_pro_debit = fields.Many2one(string='Debito Integral Producción', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Tercero', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    rate = fields.Float(string='Factor', store=True, copy=True, tracking=0, )
    reg_adm_credit = fields.Many2one(string='Credito Regular Administrativo', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    reg_adm_debit = fields.Many2one(string='Debito Regular Administrativo', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    reg_com_credit = fields.Many2one(string='Credito Regular Comercial', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    reg_com_debit = fields.Many2one(string='Debito Regular Comercial', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    reg_ope_credit = fields.Many2one(string='Credito Regular Operativa', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    reg_ope_debit = fields.Many2one(string='Debito Regular Operativa', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    reg_pro_credit = fields.Many2one(string='Credito Regular Producción', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    reg_pro_debit = fields.Many2one(string='Debito Regular Producción', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )


class Categoriadelanovedad(models.Model):
    _name = 'hr.payroll.novedades.category'
    _description = 'Categoria de la novedad'
    afc = fields.Boolean(string='AFC', store=True, copy=True, tracking=0, )
    apr_adm_credit = fields.Many2one(string='Credito Aprendiz Administrativo', store=True, copy=True, tracking=0,
                                     comodel_name='_unknown', )
    apr_adm_debit = fields.Many2one(string='Debito Aprendiz Administrativo', store=True, copy=True, tracking=0,
                                    comodel_name='_unknown', )
    apr_com_credit = fields.Many2one(string='Credito Aprendiz Comercial', store=True, copy=True, tracking=0,
                                     comodel_name='_unknown', )
    apr_com_debit = fields.Many2one(string='Debito Aprendiz Comercial', store=True, copy=True, tracking=0,
                                    comodel_name='_unknown', )
    apr_ope_credit = fields.Many2one(string='Credito Aprendiz Operativa', store=True, copy=True, tracking=0,
                                     comodel_name='_unknown', )
    apr_ope_debit = fields.Many2one(string='Debito Aprendiz Operativa', store=True, copy=True, tracking=0,
                                    comodel_name='_unknown', )
    code = fields.Char(string='Codigo', store=True, required=True, copy=True, tracking=0, )
    ded_rent = fields.Boolean(string='Aporte voluntario', store=True, copy=True, tracking=0, )
    descripcion = fields.Text(string='Descripcion', store=True, copy=True, tracking=0, )
    ex_rent = fields.Boolean(string='Ingreso exento de retencion', store=True, copy=True, tracking=0, )
    hour_novelty = fields.Boolean(string='Novedad por horas', store=True, copy=True, tracking=0, )
    int_adm_credit = fields.Many2one(string='Credito Integral Administrativo', store=True, copy=True, tracking=0,
                                     comodel_name='_unknown', )
    int_adm_debit = fields.Many2one(string='Debito Integral Administrativo', store=True, copy=True, tracking=0,
                                    comodel_name='_unknown', )
    int_com_credit = fields.Many2one(string='Credito Integral Comercial', store=True, copy=True, tracking=0,
                                     comodel_name='_unknown', )
    int_com_debit = fields.Many2one(string='Debito Integral Comercial', store=True, copy=True, tracking=0,
                                    comodel_name='_unknown', )
    int_ope_credit = fields.Many2one(string='Credito Integral Operativa', store=True, copy=True, tracking=0,
                                     comodel_name='_unknown', )
    int_ope_debit = fields.Many2one(string='Debito Integral Operativa', store=True, copy=True, tracking=0,
                                    comodel_name='_unknown', )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    partner_other = fields.Many2one(string='Otro Tercero', store=True, copy=True, tracking=0,
                                    comodel_name='res.partner', )
    prod_ind_credit = fields.Many2one(string='Credito Costo Indirecto Produccion', store=True, copy=True, tracking=0,
                                      comodel_name='_unknown', )
    prod_ind_debit = fields.Many2one(string='Debito Costo Indirecto Produccion', store=True, copy=True, tracking=0,
                                     comodel_name='_unknown', )
    reg_adm_credit = fields.Many2one(string='Credito Regular Administrativo', store=True, copy=True, tracking=0,
                                     comodel_name='_unknown', )
    reg_adm_debit = fields.Many2one(string='Debito Regular Administrativo', store=True, copy=True, tracking=0,
                                    comodel_name='_unknown', )
    reg_com_credit = fields.Many2one(string='Credito Regular Comercial', store=True, copy=True, tracking=0,
                                     comodel_name='_unknown', )
    reg_com_debit = fields.Many2one(string='Debito Regular Comercial', store=True, copy=True, tracking=0,
                                    comodel_name='_unknown', )
    reg_ope_credit = fields.Many2one(string='Credito Regular Operativa', store=True, copy=True, tracking=0,
                                     comodel_name='_unknown', )
    reg_ope_debit = fields.Many2one(string='Debito Regular Operativa', store=True, copy=True, tracking=0,
                                    comodel_name='_unknown', )


class Categoríadeldocumento(models.Model):
    _name = 'dms.category'
    _description = 'Categoría del documento'
    active = fields.Boolean(string='Activo', store=True, copy=True, tracking=0, )
    complete_name = fields.Char(string='Nombre completo', store=True, readonly=True, tracking=0, )
    count_categories = fields.Integer(string='Nº de subcategorías', readonly=True, tracking=0, )
    count_directories = fields.Integer(string='Nº de carpetas', readonly=True, tracking=0, )
    count_files = fields.Integer(string='Nº de archivos', readonly=True, tracking=0, )
    count_tags = fields.Integer(string='Nº de etiquetas', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    parent_id = fields.Many2one(string='Propietario', index=True, store=True, copy=True, tracking=0,
                                comodel_name='dms.category', )
    parent_path = fields.Char(string='Modelo padre', index=True, store=True, copy=True, tracking=0, )


class Categoríadenómina(models.Model):
    _name = 'hr.payslip.type'
    _description = 'Categoría de Nómina'
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    concepts_ids = fields.Many2many(relation='categoriadelanovedad_concepts_ids_rel', column1='categoriadelanovedad_id',
                                    column2='concepts_ids_id', string='Conceptos de Nómina', store=True, copy=True,
                                    tracking=0,
                                    comodel_name='hr.concept', )
    embargo_category_ids = fields.Many2many(relation='categoriadelanovedad_embargo_category_ids_rel',
                                            column1='categoriadelanovedad_id', column2='embargo_category_ids_id',
                                            string='Categoría de Embargos', store=True, copy=True, tracking=0,
                                            comodel_name='hr.payroll.embargo.category', )
    leave_types_ids = fields.Many2many(relation='categoriadelanovedad_leave_types_ids_rel',
                                       column1='categoriadelanovedad_id', column2='leave_types_ids_id',
                                       string='Categoría de Ausencias', store=True, copy=True, tracking=0,
                                       comodel_name='hr.leave.type', )
    load_contract_states = fields.Boolean(string='Cargar todos los Contratos', store=True, copy=True, tracking=0, )
    load_contract_with_novelty = fields.Boolean(string='Cargas contratos si tiene novedades', store=True, copy=True,
                                                tracking=0, )
    load_icesantias_lastyear = fields.Boolean(string='Cargas cesantias, intereses año anterior', store=True,
                                              copy=True,
                                              tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    novelty_types_ids = fields.Many2many(relation='categoriadelanovedad_novelty_types_ids_rel',
                                         column1='categoriadelanovedad_id', column2='novelty_types_ids_id',
                                         string='Categoría de Novedades', store=True, copy=True, tracking=0,
                                         comodel_name='hr.novelty.type', )
    overtime_types_ids = fields.Many2many(relation='categoriadelanovedad_overtime_types_ids_rel',
                                          column1='categoriadelanovedad_id', column2='overtime_types_ids_id',
                                          string='Categoría de Horas Extras', store=True, copy=True, tracking=0,
                                          comodel_name='hr.overtime.type', )
    portal_exclude = fields.Boolean(string='Excluir del Portal', store=True, copy=True, tracking=0, )


class Categoríadenovedades(models.Model):
    _name = 'hr.novelty.type'
    _description = 'Categoría de Novedades'
    apply_extra_legal = fields.Boolean(string='Aplica Prima Extra Legal', store=True, copy=True, tracking=0, )
    apply_social = fields.Boolean(string='Aplica para prestaciones social', store=True, copy=True, tracking=0, )
    apply_vacation = fields.Boolean(string='Afecta promedio vacaciones difrutadas', store=True, copy=True,
                                    tracking=0, )
    apr_adm_credit = fields.Many2one(string='Credito Aprendiz Administrativo', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    apr_adm_debit = fields.Many2one(string='Debito Aprendiz Administrativo', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    apr_com_credit = fields.Many2one(string='Credito Aprendiz Comercial', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    apr_com_debit = fields.Many2one(string='Debito Aprendiz Comercial', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    apr_ope_credit = fields.Many2one(string='Credito Aprendiz Operativa', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    apr_ope_debit = fields.Many2one(string='Debito Aprendiz Operativa', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    apr_pro_credit = fields.Many2one(string='Credito Aprendiz Producción', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    apr_pro_debit = fields.Many2one(string='Debito Aprendiz Producción', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    bring_contributions_payroll = fields.Boolean(string='Llevar aportes a planilla', store=True, copy=True,
                                                 tracking=0, )
    code = fields.Char(string='Código', store=True, required=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    dep_days_worked_leaves = fields.Boolean(string='Depende de días Trabajados y Vacaciones', store=True, copy=True,
                                            tracking=0, )
    dep_days_worked = fields.Boolean(string='Depende de días trabajados', store=True, copy=True, tracking=0, )
    food_aid = fields.Boolean(string='Subsidio de Alimentación', store=True, copy=True, tracking=0, )
    int_adm_credit = fields.Many2one(string='Credito Integral Administrativo', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    int_adm_debit = fields.Many2one(string='Debito Integral Administrativo', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    int_com_credit = fields.Many2one(string='Credito Integral Comercial', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    int_com_debit = fields.Many2one(string='Debito Integral Comercial', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    int_ope_credit = fields.Many2one(string='Credito Integral Operativa', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    int_ope_debit = fields.Many2one(string='Debito Integral Operativa', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    int_pro_credit = fields.Many2one(string='Credito Integral Producción', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    int_pro_debit = fields.Many2one(string='Debito Integral Producción', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Tercero', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    prepaid_medicine = fields.Boolean(string='Medicina-Dental Prepagada', store=True, copy=True, tracking=0, )
    reg_adm_credit = fields.Many2one(string='Credito Regular Administrativo', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    reg_adm_debit = fields.Many2one(string='Debito Regular Administrativo', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    reg_com_credit = fields.Many2one(string='Credito Regular Comercial', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    reg_com_debit = fields.Many2one(string='Debito Regular Comercial', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    reg_ope_credit = fields.Many2one(string='Credito Regular Operativa', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    reg_ope_debit = fields.Many2one(string='Debito Regular Operativa', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    reg_pro_credit = fields.Many2one(string='Credito Regular Producción', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    reg_pro_debit = fields.Many2one(string='Debito Regular Producción', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    settlement_agreement = fields.Boolean(string='Acuerdo de Transaccional', store=True, copy=True, tracking=0, )


class Categoríadereclamación(models.Model):
    _name = 'crm.claim.category'
    _description = 'Categoría de Reclamación'
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    team_id = fields.Many2one(string='Equipo de Ventas', store=True, copy=True, tracking=0, comodel_name='crm.team', )


class Categoríadeserviciodeayuda(models.Model):
    _name = 'helpdesk.category'
    _description = 'Categoría de servicio de ayuda'
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )


class Categoríaempresa(models.Model):
    _name = 'res.partner.id_category'
    _description = 'Categoría Empresa'
    active = fields.Boolean(string='Activo', store=True, copy=True, tracking=0, )
    code = fields.Char(string='Código', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre ID', store=True, required=True, copy=True, tracking=0, )
    validation_code = fields.Text(string='Código de validación Python', store=True, copy=True, tracking=0, )


class Causadeausencia(models.Model):
    _name = 'hr.leave.cause'
    _description = 'Causa de Ausencia'
    code = fields.Char(string='Código', store=True, copy=True, tracking=0, )
    description = fields.Char(string='Descripción', store=True, copy=True, tracking=0, )
    lower_limit = fields.Integer(string='Límite inferior', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', index=True, store=True, readonly=True, tracking=0, )
    symbol = fields.Char(string='Símbolo', store=True, copy=True, tracking=0, )
    upper_limit = fields.Integer(string='Límite superior', store=True, copy=True, tracking=0, )


class Cierreprogramacion(models.Model):
    _name = 'cierre.programacion.wiz'
    _description = 'Cierre Programacion'
    fecha_cierre = fields.Date(string='Fecha de cierre', store=True, required=True, copy=True, tracking=0, )
    periodo = fields.Many2one(string='Periodo', store=True, required=True, copy=True, tracking=0,
                              comodel_name='payslip.period', )


class Ciuu(models.Model):
    _name = 'res.ciiu'
    _description = 'CIUU'
    description = fields.Char(string='Descripción', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Código', store=True, required=True, copy=True, tracking=0, )
    tax_ids = fields.Many2many(relation='ciuu_tax_ids_rel', column1='ciuu_id', column2='tax_ids_id', string='Impuestos',
                               store=True, copy=True, tracking=0, comodel_name='account.tax', )


class CodesoftheePayrolltypesoftheconcepts(models.Model):
    _name = 'hr.payslip.concept.epayroll.type.code'
    _description = 'Codes of the E-Payroll Types of the Concepts'
    code = fields.Char(string='Code', store=True, copy=True, tracking=0, )
    epayroll_type_id = fields.Many2one(string='E-Payroll Type of the Concept', store=True, copy=True, tracking=0,
                                       comodel_name='hr.payslip.concept.epayroll.type', )
    exclude = fields.Boolean(string='Excluir', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Name', store=True, copy=True, tracking=0, )


class Codigosdeunidaddemedida(models.Model):
    _name = 'uom.code'
    _description = 'Códigos de Unidad de Medida'
    code = fields.Char(string='Código', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class Comprobantescontables(models.Model):
    _name = 'account.voucher'
    _description = 'Comprobantes contables'
    access_token = fields.Char(string='Token de seguridad', store=True, tracking=0, )
    access_url = fields.Char(string='URL de acceso al portal', readonly=True, tracking=0, )
    access_warning = fields.Text(string='Advertencia de acceso', readonly=True, tracking=0, )
    account_id = fields.Many2one(string='Cuenta de destino', store=True, copy=True, tracking=0,
                                 comodel_name='account.account', )
    activity_date_deadline = fields.Date(string='Siguiente plazo de actividad', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Resumen de la siguiente actividad', tracking=0, )
    activity_type_icon = fields.Char(string='Ícono de tipo de actvidad', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Siguiente tipo de actividad', tracking=0,
                                       comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Usuario responsable', tracking=0, comodel_name='res.users', )
    amount_active = fields.Monetary(string='Monto del Activo', store=True, readonly=True, tracking=0, )
    amount_passive = fields.Monetary(string='Monto del Pasivo', store=True, readonly=True, tracking=0, )
    amount_reconcile = fields.Monetary(string='Monto de Conciliación', store=True, readonly=True, tracking=0, )
    amount_voucher = fields.Monetary(string='Monto del Pago', store=True, readonly=True, tracking=0, )
    amount = fields.Monetary(string='Valor', store=True, copy=True, tracking=100, )
    audit = fields.Boolean(string='Por Revisar', store=True, copy=True, tracking=100, )
    authorization = fields.Char(string='Autorización', store=True, tracking=100, )
    company_currency_id = fields.Many2one(string='Moneda de la Compañía', readonly=True, tracking=0,
                                          comodel_name='res.currency', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    compensation_account = fields.Many2one(string='Diario de compensación', store=True, copy=True, tracking=0,
                                           comodel_name='account.journal', )
    compensation_customer = fields.Boolean(string='Pago de compensación', store=True, copy=True, tracking=0, )
    consignment_id = fields.Many2one(string='Consignación', store=True, copy=True, tracking=0,
                                     comodel_name='account.consignment', )
    currency_id = fields.Many2one(string='Moneda', store=True, copy=True, tracking=0, comodel_name='res.currency', )
    date = fields.Date(string='Fecha', store=True, required=True, tracking=0, )
    exchange_rate = fields.Float(string='Tasa de conversión', store=True, copy=True, tracking=0, )
    journal_id = fields.Many2one(string='Diario', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='account.journal', )
    message_attachment_count = fields.Integer(string='Nº de archivos adjuntos', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='comprobantescontable_message_channel_ids_rel',
                                           column1='comprobantescontable_id', column2='message_channel_ids_id',
                                           string='Seguidores (Canales)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Numero de errores', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Error de Envío de Mensaje', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Es un seguidor', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Adjuntos principales', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Acción requerida', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='comprobantescontable_message_partner_ids_rel',
                                           column1='comprobantescontable_id', column2='message_partner_ids_id',
                                           string='Seguidores (Contactos)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Nº de mensajes sin leer', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Mensajes sin Leer', readonly=True, tracking=0, )
    move_id = fields.Many2one(string='Asiento contable', store=True, readonly=True, tracking=0,
                              comodel_name='account.move', )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    number = fields.Char(string='Numero', store=True, copy=True, tracking=100, )
    partner_id = fields.Many2one(string='Cliente', store=True, required=True, copy=True, tracking=100,
                                 comodel_name='res.partner', )
    reference = fields.Char(string='Ref. Pago', store=True, copy=True, tracking=100, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )
    voucher_date = fields.Date(string='Fecha del Pago', store=True, tracking=0, )
    voucher_reference = fields.Char(string='Referencia del Pago', store=True, tracking=0, )
    writeoff_amount = fields.Monetary(string='Cantidad de diferencia', store=True, readonly=True, tracking=0, )
    writeoff_comment = fields.Char(string='Comentario de la contrapartida', store=True, copy=True, tracking=0, )


class Computepayslip(models.Model):
    _name = 'compute.hr.payslip'
    _description = 'Compute Payslip'
    dian_ids = fields.Many2many(relation='computepayslip_dian_ids_rel', column1='computepayslip_id',
                                column2='dian_ids_id', string='Nominas', store=True, copy=True, tracking=0,
                                comodel_name='hr.payslip', )


class Comunicación(models.Model):
    _name = 'quoter.communication'
    _description = 'Comunicación'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    total_price_lines = fields.Float(string='Total', readonly=True, tracking=0, )


class Comunicacióndecontroldecrédito(models.Model):
    _name = 'credit.control.communication'
    _description = 'comunicación de control de crédito'
    activity_date_deadline = fields.Date(string='Fecha de la siguiente acción', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Fecha de la siguiente acción', tracking=0,
                                       comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    company_id = fields.Many2one(string='Compañía', index=True, store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    contact_address_id = fields.Many2one(string='Dirección de contacto', index=True, store=True, readonly=True,
                                         copy=True,
                                         tracking=0, comodel_name='res.partner', )
    currency_id = fields.Many2one(string='Divisa', index=True, store=True, required=True, copy=True, tracking=0,
                                  comodel_name='res.currency', )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='computepayslip_message_channel_ids_rel',
                                           column1='computepayslip_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Siguiente acción', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Seguimiento', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Siguiente acción', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='computepayslip_message_partner_ids_rel',
                                           column1='computepayslip_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    partner_id = fields.Many2one(string='Empresa', index=True, store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.partner', )
    policy_id = fields.Many2one(string='Política asociada', index=True, store=True, readonly=True, tracking=0,
                                comodel_name='credit.control.policy', )
    policy_level_id = fields.Many2one(string='Nivel', index=True, store=True, required=True, copy=True, tracking=0,
                                      comodel_name='credit.control.policy.level', )
    report_date = fields.Date(string='Fecha del informe', store=True, copy=True, tracking=0, )
    total_due = fields.Float(string='Total debido', readonly=True, tracking=0, )
    total_invoiced = fields.Float(string='Total facturado', readonly=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', index=True, store=True, copy=True, tracking=0,
                              comodel_name='res.users', )


class Conceptodenómina(models.Model):
    _name = 'hr.concept'
    _description = 'Concepto de Nómina'
    apr_adm_credit = fields.Many2one(string='Credito Aprendiz Administrativo', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    apr_adm_debit = fields.Many2one(string='Debito Aprendiz Administrativo', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    apr_com_credit = fields.Many2one(string='Credito Aprendiz Comercial', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    apr_com_debit = fields.Many2one(string='Debito Aprendiz Comercial', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    apr_ope_credit = fields.Many2one(string='Credito Aprendiz Operativa', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    apr_ope_debit = fields.Many2one(string='Debito Aprendiz Operativa', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    apr_pro_credit = fields.Many2one(string='Credito Aprendiz Producción', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    apr_pro_debit = fields.Many2one(string='Debito Aprendiz Producción', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    code = fields.Char(string='Código', store=True, required=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    disability_for_embargo = fields.Boolean(string='Incapacidad para embargos', store=True, copy=True, tracking=0, )
    documentation = fields.Char(string='Información', store=True, copy=True, tracking=0, )
    int_adm_credit = fields.Many2one(string='Credito Integral Administrativo', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    int_adm_debit = fields.Many2one(string='Debito Integral Administrativo', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    int_com_credit = fields.Many2one(string='Credito Integral Comercial', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    int_com_debit = fields.Many2one(string='Debito Integral Comercial', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    int_ope_credit = fields.Many2one(string='Credito Integral Operativa', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    int_ope_debit = fields.Many2one(string='Debito Integral Operativa', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    int_pro_credit = fields.Many2one(string='Credito Integral Producción', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    int_pro_debit = fields.Many2one(string='Debito Integral Producción', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    is_retention = fields.Boolean(string='Es Retención', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Tercero', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    reg_adm_credit = fields.Many2one(string='Credito Regular Administrativo', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    reg_adm_debit = fields.Many2one(string='Debito Regular Administrativo', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    reg_com_credit = fields.Many2one(string='Credito Regular Comercial', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    reg_com_debit = fields.Many2one(string='Debito Regular Comercial', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    reg_ope_credit = fields.Many2one(string='Credito Regular Operativa', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    reg_ope_debit = fields.Many2one(string='Debito Regular Operativa', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    reg_pro_credit = fields.Many2one(string='Credito Regular Producción', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    reg_pro_debit = fields.Many2one(string='Debito Regular Producción', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )


class Conceptosdecorrecciónparafacturasrectificativas(models.Model):
    _name = 'account.move.discrepancy.response.code'
    _description = 'Conceptos de Corrección para Facturas Rectificativas'
    code = fields.Char(string='Código', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class Condicióndelvehículo(models.Model):
    _name = 'delivery.vehicle.condition'
    _description = 'Condición del vehículo'
    active = fields.Boolean(string='Activo', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )


class Conductor(models.Model):
    _name = 'res.partner.driver'
    _description = 'Conductor'
    branch_id = fields.Many2one(string='Sucursal', store=True, copy=True, tracking=0, comodel_name='hr.branch', )
    comment = fields.Text(string='Comentario', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    mobile = fields.Char(string='Celular', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Asociado', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    partners_ids = fields.Many2many(relation='conductor_partners_ids_rel', column1='conductor_id',
                                    column2='partners_ids_id', string='Terceros', store=True, copy=True, tracking=0,
                                    comodel_name='res.partner', )
    plate = fields.Char(string='Placa', store=True, copy=True, tracking=0, )
    vat = fields.Char(string='NIT', store=True, copy=True, tracking=0, )
    vehicle_condition_id = fields.Many2one(string='Condición del vehículo', store=True, copy=True, tracking=0,
                                           comodel_name='delivery.vehicle.condition', )
    vehicle_id = fields.Many2one(string='Vehículo', store=True, copy=True, tracking=0,
                                 comodel_name='delivery.vehicle', )


class Configuraciondefactorporcentrodecosto(models.Model):
    _name = 'hr.overtime.categ.config'
    _description = 'Configuracion de factor por centro de costo'
    analytic_account_id = fields.Many2one(string='Centro de costo', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    contract_type_id = fields.Many2one(string='Tipo de contrato', store=True, copy=True, tracking=0,
                                       comodel_name='hr.contract.type', )
    hours_comp_turno = fields.Integer(string='Horas compensadas por turno', store=True, copy=True, tracking=0, )
    overtime_id = fields.Many2one(string='Tipo de hora extra', store=True, copy=True, tracking=0,
                                  comodel_name='hr.overtime.type', )
    partner_id = fields.Many2one(string='Cliente', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    rate = fields.Float(string='Factor', store=True, copy=True, tracking=0, )


class Configuracióndeplantillasdegoogledrive(models.Model):
    _name = 'google.drive.config'
    _description = 'Configuración de plantillas de Google Drive'
    active = fields.Boolean(string='Activo', store=True, copy=True, tracking=0, )
    filter_id = fields.Many2one(string='Filtro', store=True, copy=True, tracking=0, comodel_name='ir.filters', )
    google_drive_client_id = fields.Char(string='Cliente de Google', readonly=True, tracking=0, )
    google_drive_resource_id = fields.Char(string='Id del recurso', readonly=True, tracking=0, )
    google_drive_template_url = fields.Char(string='URL de la plantilla', store=True, required=True, copy=True,
                                            tracking=0, )
    model_id = fields.Many2one('ir.model', string='Modelo', required=True, index=True, ondelete='cascade', )
    model = fields.Char(string='Modelo relacionado', readonly=True, tracking=0, )
    name_template = fields.Char(string='Patrón de nombres de Google Drive', store=True, required=True, copy=True,
                                tracking=0, )
    name = fields.Char(string='Nombre de la plantilla', store=True, required=True, copy=True, tracking=0, )


class Confirmarcaducidad(models.Model):
    _name = 'expiry.picking.confirmation'
    _description = 'Confirmar caducidad'
    description = fields.Char(string='Descripción', readonly=True, tracking=0, )
    lot_ids = fields.Many2many(relation='confirmarcaducidad_lot_ids_rel', column1='confirmarcaducidad_id',
                               column2='lot_ids_id', string='Lote', store=True, readonly=True, required=True, copy=True,
                               tracking=0,
                               comodel_name='stock.production.lot', )
    picking_ids = fields.Many2many(relation='confirmarcaducidad_picking_ids_rel', column1='confirmarcaducidad_id',
                                   column2='picking_ids_id', string='Albarán', store=True, readonly=True, copy=True,
                                   tracking=0,
                                   comodel_name='stock.picking', )
    show_lots = fields.Boolean(string='Mostrar lotes', readonly=True, tracking=0, )


class Consignacion(models.Model):
    _name = 'account.consignment'
    _description = 'Consignación'
    activity_date_deadline = fields.Date(string='Siguiente plazo de actividad', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Resumen de la siguiente actividad', tracking=0, )
    activity_type_icon = fields.Char(string='Ícono de tipo de actvidad', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Siguiente tipo de actividad', tracking=0,
                                       comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Usuario responsable', tracking=0, comodel_name='res.users', )
    amount = fields.Monetary(string='Valor', store=True, copy=True, tracking=100, )
    bank_id = fields.Many2one(string='Banco', store=True, required=True, copy=True, tracking=100,
                              comodel_name='res.bank', )
    bank_source_id = fields.Many2one(string='Banco Origen', store=True, copy=True, tracking=100,
                                     comodel_name='res.bank', )
    company_id = fields.Many2one(string='Compañia', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    consignment_block = fields.Boolean(string='Bloquear', store=True, tracking=0, )
    consignment_date = fields.Date(string='Fecha de Consignación', store=True, copy=True, tracking=0, )
    consignment_reference = fields.Char(string='Referencia de Consignación', store=True, copy=True, tracking=0, )
    currency_id = fields.Many2one(string='Moneda', store=True, copy=True, tracking=0, comodel_name='res.currency', )
    date = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )
    journal_id = fields.Many2one(string='Diario', store=True, readonly=True, tracking=0,
                                 comodel_name='account.journal', )
    message_attachment_count = fields.Integer(string='Nº de archivos adjuntos', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='consignacion_message_channel_ids_rel', column1='consignacion_id',
                                           column2='message_channel_ids_id', string='Seguidores (Canales)',
                                           readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Numero de errores', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Error de Envío de Mensaje', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Es un seguidor', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Adjuntos principales', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Acción requerida', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='consignacion_message_partner_ids_rel', column1='consignacion_id',
                                           column2='message_partner_ids_id', string='Seguidores (Contactos)',
                                           readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Nº de mensajes sin leer', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Mensajes sin Leer', readonly=True, tracking=0, )
    moves_ids = fields.Many2many(relation='consignacion_moves_ids_rel', column1='consignacion_id',
                                 column2='moves_ids_id', string='Facturas', store=True, tracking=0,
                                 comodel_name='account.move', )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, readonly=True, required=True, tracking=0, )
    number = fields.Char(string='Número', store=True, tracking=0, )
    partner_bank_id = fields.Many2one(string='Cuenta del banco', store=True, copy=True, tracking=100,
                                      comodel_name='res.partner.bank', )
    partner_id = fields.Many2one(string='Cliente', store=True, copy=True, tracking=100, comodel_name='res.partner', )
    readonly_partner = fields.Boolean(string='Tercero Solo Lectura', store=True, tracking=0, )
    reference = fields.Char(string='Referencia', store=True, copy=True, tracking=0, )
    show_available = fields.Boolean(string='Mostrar Disponible', readonly=True, tracking=0, )
    show_exchange = fields.Boolean(string='Mostrar Canje', readonly=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )
    voucher_id = fields.Many2one(string='Pago', store=True, tracking=0, comodel_name='account.voucher', )


class Contactodeemergencia(models.Model):
    _name = 'contacto.emergencia'
    _description = 'Contacto de Emergencia'
    ciudad_id = fields.Many2one(string='Ciudad', store=True, copy=True, tracking=0, comodel_name='res.city', )
    departamento_id = fields.Many2one(string='Departamento', store=True, copy=True, tracking=0,
                                      comodel_name='res.country.state', )
    direccion = fields.Char(string='Dirección', store=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    name = fields.Char(string='Nombres', store=True, required=True, copy=True, tracking=0, )
    parentesco = fields.Char(string='Parentesco', store=True, copy=True, tracking=0, )
    telefono = fields.Char(string='Teléfono', store=True, required=True, copy=True, tracking=0, )


class Contractprorroga(models.Model):
    _name = 'wizard.contract.prorroga'
    _description = 'Contract Prorroga'
    specific_date = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )


class Correorebotadomixin(models.Model):
    _name = 'mail.bounced.mixin'
    _description = 'Correo rebotado mixin'
    email_bounced = fields.Boolean(string='Correo rebotado', index=True, store=True, copy=True, tracking=0, )


class Costoendestino(models.Model):
    _name = 'stock.landed.cost'
    _description = 'Costo en Destino'
    account_journal_id = fields.Many2one(string='Libro Contable', store=True, required=True, copy=True, tracking=0,
                                         comodel_name='account.journal', )
    account_move_id = fields.Many2one(string='Asiento del Libro', store=True, readonly=True, tracking=0,
                                      comodel_name='account.move', )
    activity_date_deadline = fields.Date(string='Siguiente plazo de actividad', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Resumen de la siguiente actividad', tracking=0, )
    activity_type_icon = fields.Char(string='Ícono de tipo de actvidad', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Siguiente tipo de actividad', tracking=0,
                                       comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Usuario responsable', tracking=0, comodel_name='res.users', )
    allowed_picking_ids = fields.Many2many('stock.picking', relation='stock_landed_cost_allowed_picking_rel',
                                           column1='cost_id', column2='picking_id', string='Allowed Transfers', )
    amount_total = fields.Monetary(string='Total', store=True, readonly=True, tracking=100, )
    company_id = fields.Many2one(string='Compañía', readonly=True, tracking=0, comodel_name='res.company', )
    currency_id = fields.Many2one(string='Moneda', readonly=True, tracking=0, comodel_name='res.currency', )
    date = fields.Date(string='Fecha', store=True, required=True, tracking=100, )
    description = fields.Text(string='Descripción del Elemento', store=True, copy=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Nº de archivos adjuntos', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='costoendestino_message_channel_ids_rel',
                                           column1='costoendestino_id', column2='message_channel_ids_id',
                                           string='Seguidores (Canales)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Numero de errores', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Error de Envío de Mensaje', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='Error de entrega del SMS', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Es Seguidor', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Adjuntos principales', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Acción requerida', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='costoendestino_message_partner_ids_rel',
                                           column1='costoendestino_id', column2='message_partner_ids_id',
                                           string='Seguidores (Asociados)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Contador de Mensajes no Leídos', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Mensajes sin Leer', readonly=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, readonly=True, tracking=100, )
    picking_ids = fields.Many2many('stock.picking', relation='stock_landed_cost_picking_rel', column1='cost_id',
                                   column2='picking_id', string='Transfers', )
    vendor_bill_id = fields.Many2one(string='Factura de proveedor', store=True, tracking=0,
                                     comodel_name='account.move', )


class Creadordeperiodosdenómina(models.Model):
    _name = 'hr.period.creator'
    _description = 'Creador de periodos de nómina'
    company_id = fields.Many2one(string='Compañia', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    notes = fields.Text(string='Notas', store=True, readonly=True, copy=True, tracking=0, )


class Crearfacturadelproyecto(models.Model):
    _name = 'project.create.invoice'
    _description = 'Crear factura del proyecto'
    _candidate_orders = fields.Many2many(relation='crearfacturadelproye__candidate_orders_rel',
                                         column1='crearfacturadelproye_id', column2='_candidate_orders_id',
                                         string='Pedidos de candidatos', readonly=True, tracking=0,
                                         comodel_name='sale.order', )
    amount_to_invoice = fields.Monetary(string='Importe a facturar', readonly=True, tracking=0, )
    currency_id = fields.Many2one(string='Moneda', readonly=True, tracking=0, comodel_name='res.currency', )
    project_id = fields.Many2one(string='Proyecto', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='project.project', )
    sale_order_id = fields.Many2one(string='Elija el pedido de cliente para facturar', store=True, required=True,
                                    copy=True, tracking=0, comodel_name='sale.order', )


class Crearhojadehorasdesdeunatarea(models.Model):
    _name = 'project.task.create.timesheet'
    _description = 'Crear hoja de horas desde una tarea'
    description = fields.Char(string='Descripción', store=True, copy=True, tracking=0, )
    task_id = fields.Many2one(string='Tarea', store=True, required=True, copy=True, tracking=0,
                              comodel_name='project.task', )
    time_spent = fields.Float(string='Tiempo', store=True, copy=True, tracking=0, )


class Crearlineadepedidodeventasdesdeproyecto(models.Model):
    _name = 'project.create.sale.order.line'
    _description = 'Crear línea de pedido de ventas desde proyecto'
    currency_id = fields.Many2one(string='Moneda', store=True, copy=True, tracking=0, comodel_name='res.currency', )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Servicio', store=True, copy=True, tracking=0,
                                 comodel_name='product.product', )
    sale_line_id = fields.Many2one(string='Elemento del pedido de venta', store=True, copy=True, tracking=0,
                                   comodel_name='sale.order.line', )
    wizard_id = fields.Many2one(string='Asistente', store=True, required=True, copy=True, tracking=0,
                                comodel_name='project.create.sale.order', )


class Crearpedidodeventasdesdeproyecto(models.Model):
    _name = 'project.create.sale.order'
    _description = 'Crear pedido de ventas desde proyecto'
    commercial_partner_id = fields.Many2one(string='Entidad comercial', readonly=True, tracking=0,
                                            comodel_name='res.partner', )
    company_id = fields.Many2one(string='Compañía', readonly=True, tracking=0, comodel_name='res.company', )
    info_invoice = fields.Char(string='Info Factura', readonly=True, tracking=0, )
    partner_id = fields.Many2one(string='Cliente', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.partner', )
    project_id = fields.Many2one(string='Proyecto', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='project.project', )
    sale_order_id = fields.Many2one(string='5 - Orden de Venta', store=True, copy=True, tracking=0,
                                    comodel_name='sale.order', )


class Crearprogramacionesmasivas(models.Model):
    _name = 'massive.shift.scheduling.wizard'
    _description = 'Crear programaciones masivas'
    date_end = fields.Date(string='Fecha Fin', store=True, copy=True, tracking=0, )
    date_start = fields.Date(string='Fecha Inicio', store=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Encargado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    message = fields.Text(string='Mensaje', store=True, readonly=True, copy=True, tracking=0, )
    modality_id = fields.Many2one(string='Modalidad', store=True, copy=True, tracking=0,
                                  comodel_name='hr.roster.modalidad', )
    order_id = fields.Many2one(string='Orden de servicio', store=True, copy=True, tracking=0,
                               comodel_name='project.service.order', )
    order_rel_id = fields.Many2one(string='Orden de servicio', readonly=True, tracking=0,
                                   comodel_name='project.service.order', )
    origin_month = fields.Date(string='Mes, año referencia', store=True, copy=True, tracking=0, )
    project_id = fields.Many2one(string='Proyecto', store=True, copy=True, tracking=0,
                                 comodel_name='project.project', )
    take_lines_date = fields.Boolean(string='Con fechas de referencia', store=True, copy=True, tracking=0, )
    usar_lineas = fields.Boolean(string='Usar lineas a programar', store=True, copy=True, tracking=0, )


class Crearpvapartirdelatarea(models.Model):
    _name = 'project.task.create.sale.order'
    _description = 'Crear PV a partir de la tarea'
    commercial_partner_id = fields.Many2one(string='Entidad comercial', readonly=True, tracking=0,
                                            comodel_name='res.partner', )
    currency_id = fields.Many2one(string='Moneda', tracking=0, comodel_name='res.currency', )
    info_invoice = fields.Char(string='Info Factura', readonly=True, tracking=0, )
    partner_id = fields.Many2one(string='Cliente', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.partner', )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Servicio', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='product.product', )
    sale_line_id = fields.Many2one(string='Elemento del pedido de venta', store=True, copy=True, tracking=0,
                                   comodel_name='sale.order.line', )
    sale_order_id = fields.Many2one(string='3 - Orden de Venta', store=True, copy=True, tracking=0,
                                    comodel_name='sale.order', )
    task_id = fields.Many2one(string='Tarea', store=True, required=True, copy=True, tracking=0,
                              comodel_name='project.task', )


class Creatediandocuments(models.Model):
    _name = 'create.hr.payslip.dian.document'
    _description = 'Create DIAN Documents'
    contract_ids = fields.Many2many(relation='creatediandocuments_contract_ids_rel', column1='creatediandocuments_id',
                                    column2='contract_ids_id', string='Contracts', store=True, copy=True, tracking=0,
                                    comodel_name='hr.contract', )
    date_end = fields.Date(string='Date End', store=True, tracking=0, )
    date_start = fields.Date(string='Date Start', store=True, tracking=0, )


class Criteriosdeseguimiento(models.Model):
    _name = 'avancys_account_followup.followup.line'
    _description = 'Criterios de seguimiento'
    auto_execute = fields.Boolean(string='Auto Execute', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Company', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    delay = fields.Integer(string='Días de vencimiento', store=True, required=True, copy=True, tracking=0, )
    description = fields.Text(string='Printed Message', store=True, copy=True, tracking=0, )
    join_invoices = fields.Boolean(string='Join open Invoices', store=True, copy=True, tracking=0, )
    manual_action_note = fields.Text(string='Action To Do', store=True, copy=True, tracking=0, )
    manual_action_responsible_id = fields.Many2one(string='Asignar una responsable', store=True, copy=True,
                                                   tracking=0,
                                                   comodel_name='res.users', )
    manual_action_type_id = fields.Many2one(string='Manual Action Type', store=True, copy=True, tracking=0,
                                            comodel_name='mail.activity.type', )
    manual_action = fields.Boolean(string='Manual Action', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Criterios de seguimiento', store=True, required=True, copy=True, tracking=0, )
    print_letter = fields.Boolean(string='Imprimir una carta', store=True, copy=True, tracking=0, )
    send_email = fields.Boolean(string='Enviar un correo', store=True, copy=True, tracking=0, )
    send_sms = fields.Boolean(string='Send an SMS Message', store=True, copy=True, tracking=0, )
    sms_description = fields.Char(string='SMS Text Message', store=True, copy=True, tracking=0, )


class Crmreportedereclamacion(models.Model):
    _name = 'crm.claim.report'
    _description = 'CRM Reporte de Reclamación'
    categ_id = fields.Many2one(string='Categoría', store=True, readonly=True, copy=True, tracking=0,
                               comodel_name='crm.claim.category', )
    claim_date = fields.Datetime(string='Fecha de Reclamación', store=True, readonly=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañía', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    date_closed = fields.Datetime(string='Fecha cierre', index=True, store=True, readonly=True, copy=True,
                                  tracking=0, )
    date_deadline = fields.Date(string='Fecha límite', index=True, store=True, readonly=True, copy=True, tracking=0, )
    delay_close = fields.Float(string='Demora cierre', store=True, readonly=True, copy=True, tracking=0, )
    delay_expected = fields.Float(string='Fecha límite excedida', store=True, readonly=True, copy=True, tracking=0, )
    email = fields.Integer(string='# Emails', store=True, readonly=True, copy=True, tracking=0, )
    nbr_claims = fields.Integer(string='# de Reclamaciones', store=True, readonly=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Empresa', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='res.partner', )
    stage_id = fields.Many2one(string='Etapa', store=True, readonly=True, copy=True, tracking=0,
                               comodel_name='crm.claim.stage', )
    subject = fields.Char(string='Objeto de la reclamación', store=True, readonly=True, copy=True, tracking=0, )
    team_id = fields.Many2one(string='Equipo', store=True, readonly=True, copy=True, tracking=0,
                              comodel_name='crm.team', )
    user_id = fields.Many2one(string='Usuario', store=True, readonly=True, copy=True, tracking=0,
                              comodel_name='res.users', )


class Defineunapoliticaderecordatorios(models.Model):
    _name = 'credit.control.policy'
    _description = 'Define una política de recordatorios'
    account_ids = fields.Many2many(relation='defineunapoliticader_account_ids_rel', column1='defineunapoliticader_id',
                                   column2='account_ids_id', string='Cuentas', store=True, required=True, copy=True,
                                   tracking=0,
                                   comodel_name='account.account', )
    active = fields.Boolean(string='Activa', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañía', store=True, copy=True, tracking=0, comodel_name='res.company', )
    do_nothing = fields.Boolean(string='No hace nada', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Detalledelíneadevariableeconómica(models.Model):
    _name = 'economic.variable.line.detail'
    _description = 'Detalle de línea de variable económica'
    add = fields.Float(string='UVTs a Sumar', store=True, copy=True, tracking=0, )
    has_lower_limit = fields.Boolean(string='Tiene límite inferior', store=True, copy=True, tracking=0, )
    has_upper_limit = fields.Boolean(string='Tiene límite superior', store=True, copy=True, tracking=0, )
    lower_limit = fields.Float(string='Límite inferior', store=True, copy=True, tracking=0, )
    rate = fields.Float(string='Porcentaje', store=True, copy=True, tracking=0, )
    subtract = fields.Float(string='UVTs a Restar', store=True, copy=True, tracking=0, )
    upper_limit = fields.Float(string='Límite superior', store=True, copy=True, tracking=0, )
    variable_line_id = fields.Many2one(string='Línea de variable económica', store=True, copy=True, tracking=0,
                                       comodel_name='economic.variable.line', )


class Detalledeplanilladeaportes(models.Model):
    _name = 'hr.contribution.form.line'
    _description = 'Detalle de planilla de aportes'
    afp_code = fields.Char(string='Código AFP', store=True, copy=True, tracking=0, )
    afp_to_code = fields.Char(string='Código AFP traslado', store=True, copy=True, tracking=0, )
    ap_vol_company = fields.Float(string='Aportes voluntarios del aportante', store=True, copy=True, tracking=0, )
    ap_vol_contributor = fields.Float(string='Aportes voluntarios del afiliado', store=True, copy=True, tracking=0, )
    arl_code = fields.Char(string='Código ARL', store=True, copy=True, tracking=0, )
    arl_cot = fields.Float(string='Cotización ARL', store=True, copy=True, tracking=0, )
    arl_days = fields.Integer(string='Días cotizados ARL', store=True, copy=True, tracking=0, )
    arl_ibc = fields.Float(string='IBC ARL', store=True, copy=True, tracking=0, )
    arl_rate = fields.Float(string='Tarifa ARL', store=True, copy=True, tracking=0, )
    arl_risk = fields.Char(string='Clase de riesgo', store=True, copy=True, tracking=0, )
    atep_end = fields.Date(string='Fin AT/EP', store=True, copy=True, tracking=0, )
    atep_start = fields.Date(string='Inicio AT/EP', store=True, copy=True, tracking=0, )
    aus_auth = fields.Char(string='Número de autorización', store=True, copy=True, tracking=0, )
    avp = fields.Boolean(string='Aporte voluntario', store=True, copy=True, tracking=0, )
    ccf_code = fields.Char(string='Código CCF', store=True, copy=True, tracking=0, )
    ccf_cot = fields.Float(string='Cotización CCF', store=True, copy=True, tracking=0, )
    ccf_days = fields.Integer(string='Días cotizados CCF', store=True, copy=True, tracking=0, )
    ccf_ibc = fields.Float(string='IBC CCF', store=True, copy=True, tracking=0, )
    ccf_rate = fields.Float(string='Tarifa CCF', store=True, copy=True, tracking=0, )
    contract_id = fields.Many2one(string='Contrato', store=True, required=True, copy=True, tracking=0,
                                  comodel_name='hr.contract', )
    contribution_id = fields.Many2one(string='Planilla de aportes', store=True, required=True, copy=True, tracking=0,
                                      comodel_name='hr.contribution.form', )
    contribution_name = fields.Char(string='Nombre de la planilla', readonly=True, tracking=0, )
    discount_eps = fields.Float(string='Descuento EPS', readonly=True, tracking=0, )
    discount_pens = fields.Float(string='Descuento pensión', readonly=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, required=True, copy=True, tracking=0,
                                  comodel_name='hr.employee', )
    eps_code = fields.Char(string='Código EPS', store=True, copy=True, tracking=0, )
    eps_cot = fields.Float(string='Cotización EPS', store=True, copy=True, tracking=0, )
    eps_days = fields.Integer(string='Días cotizados EPS', store=True, copy=True, tracking=0, )
    eps_ibc = fields.Float(string='IBC EPS', store=True, copy=True, tracking=0, )
    eps_rate = fields.Float(string='Tarifa EPS', store=True, copy=True, tracking=0, )
    eps_to_code = fields.Char(string='Código EPS traslado', store=True, copy=True, tracking=0, )
    esap_cot = fields.Float(string='Cotización ESAP', store=True, copy=True, tracking=0, )
    esap_rate = fields.Float(string='Tarifa ESAP', store=True, copy=True, tracking=0, )
    exonerated = fields.Boolean(string='Exonerado de aportes', store=True, copy=True, tracking=0, )
    fsol = fields.Float(string='Aportes a fondo de solidaridad', store=True, copy=True, tracking=0, )
    fsub = fields.Float(string='Aportes a fondo de subsistencia', store=True, copy=True, tracking=0, )
    gd_amount = fields.Float(string='Valor de la incapacidad', store=True, copy=True, tracking=0, )
    global_ibc = fields.Float(string='IBC Global', store=True, copy=True, tracking=0, )
    icbf_cot = fields.Float(string='Cotización ICBF', store=True, copy=True, tracking=0, )
    icbf_rate = fields.Float(string='Tarifa ICBF', store=True, copy=True, tracking=0, )
    ige_end = fields.Date(string='Fin incapacidad', store=True, copy=True, tracking=0, )
    ige_start = fields.Date(string='Inicio incapacidad', store=True, copy=True, tracking=0, )
    ige = fields.Boolean(string='Incapacidad general', store=True, copy=True, tracking=0, )
    input_eps = fields.Float(string='Aporte EPS', readonly=True, tracking=0, )
    input_pens = fields.Float(string='Aporte pensión', readonly=True, tracking=0, )
    irl = fields.Integer(string='Días de AT/EP', store=True, copy=True, tracking=0, )
    k_end = fields.Date(string='Fecha de retiro', store=True, copy=True, tracking=0, )
    k_start = fields.Date(string='Fecha de ingreso', store=True, copy=True, tracking=0, )
    leave_id = fields.Many2one(string='Ausencia', store=True, copy=True, tracking=0, comodel_name='hr.leave', )
    lma_end = fields.Date(string='Fin licencia', store=True, copy=True, tracking=0, )
    lma_start = fields.Date(string='Inicio licencia', store=True, copy=True, tracking=0, )
    lma = fields.Boolean(string='Licencia de maternidad/paternidad', store=True, copy=True, tracking=0, )
    main = fields.Boolean(string='Main', store=True, copy=True, tracking=0, )
    mat_amount = fields.Float(string='Valor de la licencia', store=True, copy=True, tracking=0, )
    mat_auth = fields.Char(string='Número de autorización', store=True, copy=True, tracking=0, )
    men_cot = fields.Float(string='Cotización MEN', store=True, copy=True, tracking=0, )
    men_rate = fields.Float(string='Tarifa MEN', store=True, copy=True, tracking=0, )
    other_ibc = fields.Float(string='IBC otros parafiscales', store=True, copy=True, tracking=0, )
    pens_cot = fields.Float(string='Cotización pensión', store=True, copy=True, tracking=0, )
    pens_days = fields.Integer(string='Días cotizados pensión', store=True, copy=True, tracking=0, )
    pens_ibc = fields.Float(string='IBC pensión', store=True, copy=True, tracking=0, )
    pens_rate = fields.Float(string='Tarifa pensión', store=True, copy=True, tracking=0, )
    pens_total = fields.Float(string='Aportes totales de pensión', store=True, copy=True, tracking=0, )
    period_id = fields.Many2one(string='Periodo', readonly=True, tracking=0, comodel_name='hr.period', )
    ret_cont_vol = fields.Float(string='Valor no retenido por aportes voluntarios', store=True, copy=True,
                                tracking=0, )
    sena_cot = fields.Float(string='Cotización SENA', store=True, copy=True, tracking=0, )
    sena_rate = fields.Float(string='Tarifa SENA', store=True, copy=True, tracking=0, )
    sln_end = fields.Date(string='Fin licencia no remunerada', store=True, copy=True, tracking=0, )
    sln_start = fields.Date(string='Inicio licencia no remunerada', store=True, copy=True, tracking=0, )
    sln = fields.Boolean(string='Licencia no remunerada', store=True, copy=True, tracking=0, )
    tae = fields.Boolean(string='Traslado a EPS', store=True, copy=True, tracking=0, )
    tap = fields.Boolean(string='Traslado a fondo de pensiones', store=True, copy=True, tracking=0, )
    tde = fields.Boolean(string='Traslado desde EPS', store=True, copy=True, tracking=0, )
    tdp = fields.Boolean(string='Traslado desde fondo de pensiones', store=True, copy=True, tracking=0, )
    ups = fields.Float(string='Total UPS', store=True, copy=True, tracking=0, )
    vac_end = fields.Date(string='Fin vacaciones', store=True, copy=True, tracking=0, )
    vac_start = fields.Date(string='Inicio vacaciones', store=True, copy=True, tracking=0, )
    vct_end = fields.Date(string='Fin centro de trabajo', store=True, copy=True, tracking=0, )
    vct_start = fields.Date(string='Inicio centro de trabajo', store=True, copy=True, tracking=0, )
    vct = fields.Boolean(string='Variación de centros de trabajo', store=True, copy=True, tracking=0, )
    vsp_start = fields.Date(string='Fecha de inicio de VSP', store=True, copy=True, tracking=0, )
    vsp = fields.Boolean(string='Variación permanente de salario', store=True, copy=True, tracking=0, )
    vst = fields.Boolean(string='Variación transitoria de salario', store=True, copy=True, tracking=0, )
    w_hours = fields.Integer(string='Horas laboradas', store=True, copy=True, tracking=0, )
    wage = fields.Float(string='Salario básico', store=True, copy=True, tracking=0, )
    work_center = fields.Char(string='Centro de trabajo', store=True, copy=True, tracking=0, )


class Detallegasto(models.Model):
    _name = 'hr.expense.line'
    _description = 'Detalle Gasto'
    amount = fields.Float(string='Total', store=True, readonly=True, tracking=0, )
    analytic_account_id = fields.Many2one(string='Centro de costo', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    base_amount = fields.Float(string='Total Base', store=True, readonly=True, tracking=0, )
    city_id = fields.Many2one(string='Ciudad', store=True, copy=True, tracking=0, comodel_name='res.city', )
    company_id = fields.Many2one(string='Compañia', readonly=True, tracking=0, comodel_name='res.company', )
    customer_id = fields.Many2one(string='Cliente', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    date = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    expense_id = fields.Many2one(string='Gasto', store=True, copy=True, tracking=0,
                                 comodel_name='hr.expense.expense', )
    fiscal_position_id = fields.Many2one(string='Posición Fiscal', readonly=True, tracking=0,
                                         comodel_name='account.fiscal.position', )
    impuestos_asumidos = fields.Float(string='Importe Total', store=True, readonly=True, tracking=0, )
    journal_consecutive = fields.Char(string='Consecutivo', store=True, copy=True, tracking=0, )
    journal_id = fields.Many2one(string='Diario', store=True, copy=True, tracking=0, comodel_name='account.journal', )
    manual_taxes = fields.Boolean(string='Impuestos manuales', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nota de Gasto', store=True, copy=True, tracking=0, )
    no_tax = fields.Float(string='Rubro Adicional', store=True, copy=True, tracking=0, )
    note = fields.Text(string='Nota', store=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Tercero', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    payment_mean_id = fields.Many2one(string='Payment Method', readonly=True, tracking=0,
                                      comodel_name='account.payment.mean', )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.product', )
    quantity = fields.Float(string='Cantidad', store=True, copy=True, tracking=0, )
    recoup_move_id = fields.Many2one(string='Factura de recobro', store=True, copy=True, tracking=0,
                                     comodel_name='account.move', )
    recoup = fields.Boolean(string='Recobro', store=True, copy=True, tracking=0, )
    recovery_invoice_id = fields.Many2one(string='Recovery Invoice', store=True, copy=True, tracking=0,
                                          comodel_name='account.move', )
    recovery = fields.Boolean(string='Recobro', store=True, copy=True, tracking=0, )
    ref1 = fields.Char(string='Referencia 1', store=True, copy=True, tracking=0, )
    ref2 = fields.Char(string='Referencia 2', store=True, copy=True, tracking=0, )
    sequence_resolution_id = fields.Many2one(string='Resolución de la Secuencia', readonly=True, tracking=0,
                                             comodel_name='ir.sequence', )
    tax_amount_assumed = fields.Float(string='Total Impuestos Asumidos', store=True, readonly=True, tracking=0, )
    tax_amount = fields.Float(string='Total Impuestos', store=True, readonly=True, tracking=0, )
    tax_ids = fields.Many2many('account.tax', relation='hr_expense_line_tax_rel', column1='expense_line_id',
                               column2='tax_id', string='Taxes',
                               # opcional: domain para compras
                               # domain=[('type_tax_use', 'in', ['purchase', 'none'])],
                               )
    tax_out_ids = fields.Many2many('account.tax', relation='hr_expense_line_tax_out_rel', column1='expense_line_id',
                                   column2='tax_id', string='Output Taxes',
                                   # opcional: domain para ventas
                                   # domain=[('type_tax_use', 'in', ['sale', 'none'])],
                                   )
    uom_id = fields.Many2one(string='Unidad de Medida', store=True, copy=True, tracking=0, comodel_name='uom.uom', )
    vat_amount = fields.Float(string='IVA', readonly=True, tracking=0, )


class Diandocumentlines(models.Model):
    _name = 'hr.payslip.dian.document.line'
    _description = 'DIAN Document Lines'
    dian_document_id = fields.Many2one(string='DIAN Document', store=True, copy=True, tracking=0,
                                       comodel_name='hr.payslip.dian.document', )
    send_async_reason = fields.Char(string='Reason', store=True, copy=True, tracking=0, )
    send_async_response = fields.Text(string='Response', store=True, copy=True, tracking=0, )
    send_async_status_code = fields.Char(string='Status Code', store=True, copy=True, tracking=0, )


class Diandocuments(models.Model):
    _name = 'hr.payslip.dian.document'
    _description = 'DIAN Documents'
    accepted_rejected_datetime = fields.Datetime(string='Datetime of Accepted/Rejected', store=True, tracking=0, )
    access_token = fields.Char(string='Access token', store=True, tracking=0, )
    ad_zipped_file = fields.Binary(string='AttachedDocument Zipped File', store=True, copy=True, tracking=0, )
    ad_zipped_filename = fields.Char(string='AttachedDocument Zipped Filename', store=True, copy=True, tracking=0, )
    ar_xml_file = fields.Binary(string='ApplicationResponse XML File', store=True, copy=True, tracking=0, )
    ar_xml_filename = fields.Char(string='ApplicationResponse XML Filename', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Company', store=True, copy=True, tracking=0, comodel_name='res.company', )
    contract_id = fields.Many2one(string='Contract', store=True, copy=True, tracking=0, comodel_name='hr.contract', )
    cune_uncoded = fields.Char(string='CUNE Uncoded', store=True, copy=True, tracking=0, )
    cune = fields.Char(string='CUNE', store=True, copy=True, tracking=0, )
    date_end = fields.Date(string='End Date', store=True, copy=True, tracking=0, )
    date_start = fields.Date(string='Start Date', store=True, copy=True, tracking=0, )
    dbname = fields.Char(string='DB Name', readonly=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    get_status_zip_response = fields.Text(string='Response', store=True, copy=True, tracking=0, )
    invoice_url = fields.Char(string='Invoice Url', store=True, copy=True, tracking=0, )
    is_accepted_rejected = fields.Boolean(string='Is Accepted/Rejected?', store=True, tracking=0, )
    mail_sent = fields.Boolean(string='Mail Sent?', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Name', store=True, tracking=0, )
    payslip_datetime = fields.Datetime(string='Payslip Datetime', store=True, tracking=0, )
    payslip_ids = fields.Many2many(relation='diandocuments_payslip_ids_rel', column1='diandocuments_id',
                                   column2='payslip_ids_id', string='Payslips', store=True, copy=True, tracking=0,
                                   comodel_name='hr.payslip', )
    qr_image = fields.Binary(string='QR Code', readonly=True, tracking=0, )
    related_dian_document_id = fields.Many2one(string='Related DIAN Document', store=True, copy=True, tracking=0,
                                               comodel_name='hr.payslip.dian.document', )
    software_security_code_uncoded = fields.Char(string='SoftwareSecurityCode Uncoded', store=True, copy=True,
                                                 tracking=0, )
    software_security_code = fields.Char(string='SoftwareSecurityCode', store=True, copy=True, tracking=0, )
    validation_datetime = fields.Datetime(string='Validation Datetime', store=True, copy=True, tracking=0, )
    warn_inactive_certificate = fields.Boolean(string='Warn About Inactive Certificate?', readonly=True, tracking=0, )
    warn_remaining_certificate = fields.Boolean(string='Warn About Remainings?', readonly=True, tracking=0, )
    xml_base_file = fields.Binary(string='XML Base File', store=True, copy=True, tracking=0, )
    xml_base_filename = fields.Char(string='XML Base Filename', store=True, copy=True, tracking=0, )
    xml_file = fields.Binary(string='Invoice XML File', store=True, copy=True, tracking=0, )
    xml_filename = fields.Char(string='Invoice XML Filename', store=True, copy=True, tracking=0, )
    zip_key = fields.Char(string='ZipKey', store=True, copy=True, tracking=0, )
    zipped_file = fields.Binary(string='Zipped File', store=True, copy=True, tracking=0, )
    zipped_filename = fields.Char(string='Zipped Filename', store=True, copy=True, tracking=0, )


class Diario(models.TransientModel):  # si es asistente, mejor TransientModel
    _name = 'account.financial.report.diario.wizard'
    _description = 'Diario'

    account_ids = fields.Many2many('account.account', relation='afr_diwiz_account_rel', column1='diario_id',
                                   column2='account_id', string='Cuentas', copy=False, )

    company_id = fields.Many2one('res.company', string='Compañía', readonly=True, copy=False)
    date_start = fields.Date(string='Fecha Inicio')
    date_end = fields.Date(string='Fecha Fin')
    levels_ids = fields.Many2many('account.financial.levels', relation='afr_diwiz_level_rel', column1='diario_id',
                                  column2='level_id', string='Niveles', copy=False, )
    partner_ids = fields.Many2many('res.partner', relation='afr_diwiz_partner_rel', column1='diario_id',
                                   column2='partner_id', string='Terceros', copy=False, )
    structure_id = fields.Many2one('account.financial.structure', string='Estructura', copy=False)


class Diasdelasemana(models.Model):
    _name = 'res.weekday'
    _description = 'Dias de la semana'
    day_index = fields.Integer(string='Indice de dia', readonly=True, tracking=0, )
    habil = fields.Boolean(string='Dia habil', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Dia de la semana', store=True, copy=True, tracking=0, )


class Díasdenómina(models.Model):
    _name = 'hr.payslip.day'
    _description = 'Días de Nómina'
    day = fields.Integer(string='Día', store=True, copy=True, tracking=0, )
    is_vac = fields.Boolean(string='Vacaciones', store=True, copy=True, tracking=0, )
    leave_id = fields.Many2one(string='Ausencia', store=True, copy=True, tracking=0, comodel_name='hr.leave', )
    leave_line_id = fields.Many2one(string='Linea de Ausencia', store=True, copy=True, tracking=0,
                                    comodel_name='hr.leave.line', )
    name = fields.Char(string='Nombre', readonly=True, tracking=0, )
    payslip_id = fields.Many2one(string='Nómina', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='hr.payslip', )
    period_id = fields.Many2one(string='Periodo', store=True, copy=True, tracking=0, comodel_name='hr.period', )


class Diasfestivos(models.Model):
    _name = 'hr.holiday'
    _description = 'Días Festivos'
    date = fields.Date(string='Fecha', store=True, required=True, copy=True, tracking=0, )
    holiday_year_id = fields.Many2one(string='Año', store=True, required=True, copy=True, tracking=0,
                                      comodel_name='hr.holiday.year', )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class Diferencialesdevacaciones(models.Model):
    _name = 'hr.vacation.diferential'
    _description = 'Diferenciales de vacaciones'
    days = fields.Integer(string='Dias', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', readonly=True, tracking=0, )


class Discapacidades(models.Model):
    _name = 'hr.disability'
    _description = 'Discapacidades'
    name = fields.Char(string='Discapacidades', store=True, copy=True, tracking=0, )


class Disparadoresderecálculodelatabladelactivo(models.Model):
    _name = 'account.asset.recompute.trigger'
    _description = 'Disparadores de recálculo de la tabla del activo'
    company_id = fields.Many2one(string='Compañía', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    date_completed = fields.Datetime(string='Fecha de terminación', store=True, readonly=True, copy=True,
                                     tracking=0, )
    date_trigger = fields.Datetime(string='Fecha de disparo', store=True, readonly=True, copy=True, tracking=0, )
    reason = fields.Char(string='Razón', store=True, required=True, copy=True, tracking=0, )


class Distribuciónanalíticacontrato(models.Model):
    _name = 'hr.contract.analytic.distribution'
    _description = 'Distribución Analítica Contrato'
    analytic_account_id = fields.Many2one(string='Cuenta Analítica', store=True, required=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    contract_id = fields.Many2one(string='Contrato', store=True, copy=True, tracking=0, comodel_name='hr.contract', )
    rate = fields.Float(string='Distribución (%)', store=True, copy=True, tracking=0, )


class Distribucionobligacionfinanciera(models.Model):
    _name = 'account.loan.distribution'
    _description = 'Distribucion Obligacion Financiera'
    account_analytic_id = fields.Many2one(string='Centro de Costo', store=True, required=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    loan_id = fields.Many2one(string='Obligacion Financiera', store=True, required=True, copy=True, tracking=0,
                              comodel_name='account.loan', )
    name = fields.Char(string='Comentario', store=True, copy=True, tracking=0, )
    rate = fields.Float(string='(%)', store=True, required=True, copy=True, tracking=0, )


class Dmssecuritymixin(models.Model):
    _name = 'dms.security.mixin'
    _description = 'DMS Security Mixin'
    permission_create = fields.Boolean(string='Acceso de creación', readonly=True, tracking=0, )
    permission_read = fields.Boolean(string='Acceso de lectura', readonly=True, tracking=0, )
    permission_unlink = fields.Boolean(string='Acceso de eliminación', readonly=True, tracking=0, )
    permission_write = fields.Boolean(string='Acceso de escritura', readonly=True, tracking=0, )
    res_id = fields.Integer(string='ID de registro de archivos adjuntos vinculados', index=True, store=True,
                            copy=True, tracking=0, )
    res_model = fields.Char(string='Modelo de adjuntos vinculado', index=True, store=True, copy=True, tracking=0, )


class Dmsthumbnailandiconmixin(models.Model):
    _name = 'dms.mixins.thumbnail'
    _description = 'DMS thumbnail and icon mixin'
    icon_url = fields.Char(string='Icon URL', readonly=True, tracking=0, )
    image_1024 = fields.Binary(string='Image 1024', store=True, readonly=True, tracking=0, )
    image_128 = fields.Binary(string='Image 128', store=True, readonly=True, tracking=0, )
    image_1920 = fields.Binary(string='Image', store=True, copy=True, tracking=0, )
    image_256 = fields.Binary(string='Image 256', store=True, readonly=True, tracking=0, )
    image_512 = fields.Binary(string='Image 512', store=True, readonly=True, tracking=0, )


class Documentos(models.Model):
    _name = 'wizard.document.page.history.show_diff'
    _description = 'Documentos'
    diff = fields.Text(string='Diff', store=True, readonly=True, copy=True, tracking=0, )


class Documentosdian(models.Model):
    _name = 'account.move.dian.document'
    _description = 'Documentos DIAN'
    ad_zipped_file = fields.Binary(string='Archivo Comprimido del AttachedDocument', store=True, copy=True,
                                   tracking=0, )
    ad_zipped_filename = fields.Char(string='Nombre de Archivo Comprimido del AttachedDocument', store=True,
                                     copy=True, tracking=0, )
    application_response_code = fields.Char(string='Application Response Code', store=True, copy=True, tracking=0, )
    ar_xml_file = fields.Binary(string='Archivo XML del ApplicationResponse', store=True, copy=True, tracking=0, )
    ar_xml_filename = fields.Char(string='Nombre de archivo XML del ApplicationResponse', store=True, copy=True,
                                  tracking=0, )
    company_id = fields.Many2one(string='Compañía', store=True, copy=True, tracking=0, comodel_name='res.company', )
    cufe_cude_uncoded = fields.Char(string='CUFE/CUDE Sin Codificar', store=True, copy=True, tracking=0, )
    cufe_cude = fields.Char(string='CUFE/CUDE', store=True, copy=True, tracking=0, )
    get_status_zip_response = fields.Text(string='Respuesta', store=True, copy=True, tracking=0, )
    hr_expense_line_id = fields.Many2one(string='Expense Line', store=True, readonly=True, copy=True, tracking=0,
                                         comodel_name='hr.expense.line', )
    invoice_id = fields.Many2one(string='Factura', store=True, copy=True, tracking=0, comodel_name='account.move', )
    invoice_url = fields.Char(string='URL de Factura', store=True, copy=True, tracking=0, )
    is_supplier_response = fields.Boolean(string='Is Supplier Response?', store=True, copy=True, tracking=0, )
    mail_sent = fields.Boolean(string='¿Correo Enviado?', store=True, copy=True, tracking=0, )
    qr_image = fields.Binary(string='Código QR', readonly=True, tracking=0, )
    related_expense_id = fields.Many2one(string='Gasto', readonly=True, tracking=0, comodel_name='hr.expense.expense', )
    software_security_code_uncoded = fields.Char(string='SoftwareSecurityCode Sin Codificar', store=True, copy=True,
                                                 tracking=0, )
    software_security_code = fields.Char(string='SoftwareSecurityCode', store=True, copy=True, tracking=0, )
    validation_datetime = fields.Datetime(string='Fecha y Hora de Validación', store=True, copy=True, tracking=0, )
    xml_file = fields.Binary(string='Archivo XML de Factura', store=True, copy=True, tracking=0, )
    xml_filename = fields.Char(string='Nombre de Archivo XML de la Factura', store=True, copy=True, tracking=0, )
    zip_key = fields.Char(string='ZipKey', store=True, copy=True, tracking=0, )
    zipped_file = fields.Binary(string='Archivo Comprimido', store=True, copy=True, tracking=0, )
    zipped_filename = fields.Char(string='Nombre de Archivo Comprimido', store=True, copy=True, tracking=0, )


class Dotacion(models.Model):
    _name = 'hr.dotacion'
    _description = 'Dotacion'
    document = fields.Char(string='Cantidad', store=True, required=True, copy=True, tracking=0, )
    dotacion_id = fields.Many2one(string='Contrato', store=True, copy=True, tracking=0, comodel_name='hr.contract', )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    prodlot_id = fields.Many2one(string='Serial', store=True, copy=True, tracking=0,
                                 comodel_name='stock.production.lot', )
    product_id = fields.Many2one(string='Producto', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='product.product', )


class Dotacion(models.Model):
    _name = 'quoter.dotation'
    _description = 'Dotación'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    total_uniform = fields.Float(string='Total Uniformes', store=True, readonly=True, tracking=0, )


class Dotacionadicional(models.Model):
    _name = 'quoter.additional.dotation'
    _description = 'Dotación adicional'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    total_uniform = fields.Float(string='Total Uniformes', store=True, readonly=True, tracking=0, )


class Dotacionderrhh(models.Model):
    _name = 'hr.equipment'
    _description = 'Dotación de RRHH'
    amount_info = fields.Char(string='Cantidad/Informacion', store=True, required=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Company', index=True, store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    contract_id = fields.Many2one(string='Contrato', store=True, copy=True, tracking=0, comodel_name='hr.contract', )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='product.product', )
    product_lot_id = fields.Many2one(string='Serial', store=True, copy=True, tracking=0,
                                     comodel_name='stock.production.lot', )


class Downloadaccountingreport(models.Model):
    _name = 'ir_actions_account_report_download'
    _description = 'Download accounting report'
    binding_model_id = fields.Many2one(string='Binding Model', store=True, copy=True, tracking=0,
                                       comodel_name='ir.model', )
    binding_view_types = fields.Char(string='Binding View Types', store=True, copy=True, tracking=0, )
    help = fields.Html(string='Action Description', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Name', store=True, required=True, copy=True, tracking=0, )
    type = fields.Char(string='Action Type', store=True, required=True, copy=True, tracking=0, )
    xml_id = fields.Char(string='External ID', readonly=True, tracking=0, )


class Draftpayslip(models.Model):
    _name = 'draft.hr.payslip'
    _description = 'Draft Payslip'
    dian_ids = fields.Many2many(relation='draftpayslip_dian_ids_rel', column1='draftpayslip_id', column2='dian_ids_id',
                                string='Nominas', store=True, copy=True, tracking=0, comodel_name='hr.payslip', )


class Educationalinstitution(models.Model):
    _name = 'hr.ed.institution'
    _description = 'Educational Institution'
    name = fields.Char(string='Institución educativa', store=True, copy=True, tracking=0, )


class Elementosdelclienteasociadosalpuesto(models.Model):
    _name = 'hr.roster.puesto.items.cliente'
    _description = 'Elementos del cliente asociados al puesto'
    name = fields.Char(string='Descripcion', store=True, copy=True, tracking=0, )
    observaciones = fields.Char(string='Observaciones', store=True, copy=True, tracking=0, )
    puesto_id = fields.Many2one(string='Puesto', store=True, copy=True, tracking=0, comodel_name='hr.roster.puesto', )


class Eliminaractivo(models.Model):
    _name = 'account.asset.remove'
    _description = 'Eliminar activo'
    account_min_value_id = fields.Many2one(string='Cuenta para pérdida de valor', store=True, copy=True, tracking=0,
                                           comodel_name='account.account', )
    account_plus_value_id = fields.Many2one(string='Cuenta para ganancia de valor', store=True, copy=True, tracking=0,
                                            comodel_name='account.account', )
    account_residual_value_id = fields.Many2one(string='Cuenta de valor residual', store=True, copy=True, tracking=0,
                                                comodel_name='account.account', )
    account_sale_id = fields.Many2one(string='Cuenta de venta del activo', store=True, copy=True, tracking=0,
                                      comodel_name='account.account', )
    date_remove = fields.Date(string='Fecha de eliminación de activo', store=True, required=True, copy=True,
                              tracking=0, )
    force_date = fields.Date(string='Forzar fecha contable', store=True, copy=True, tracking=0, )
    note = fields.Text(string='Notas', store=True, copy=True, tracking=0, )
    sale_value = fields.Float(string='Valor de venta', store=True, copy=True, tracking=0, )


class Entrenamiento(models.Model):
    _name = 'quoter.training'
    _description = 'entrenamiento'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    total_training = fields.Float(string='Toral Entrenamientos', readonly=True, tracking=0, )


class Envíomasivo(models.Model):
    _name = 'credit.control.emailer'
    _description = 'Envío masivo'
    line_ids = fields.Many2many(relation='entrenamiento_line_ids_rel', column1='entrenamiento_id',
                                column2='line_ids_id', string='Líneas de control de crédito', store=True, copy=True,
                                tracking=0,
                                comodel_name='credit.control.line', )


class EPayrollsubtypesoftheemployee(models.Model):
    _name = 'hr.employee.epayroll.subtype'
    _description = 'E-Payroll Subtypes of the Employee'
    code = fields.Char(string='Code', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Name', store=True, copy=True, tracking=0, )


class EPayrolltypesoftheconcepts(models.Model):
    _name = 'hr.payslip.concept.epayroll.type'
    _description = 'E-Payroll Types of the Concepts'
    code = fields.Char(string='Code', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Name', store=True, copy=True, tracking=0, )


class EPayrolltypesoftheemployee(models.Model):
    _name = 'hr.employee.epayroll.type'
    _description = 'E-Payroll Types of the Employee'
    code = fields.Char(string='Code', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Name', store=True, copy=True, tracking=0, )


class Equipodeserviciodeayuda(models.Model):
    _name = 'helpdesk.team'
    _description = 'Equipo de servicio de ayuda'
    alias_bounced_content = fields.Html(string='Mensaje rebotado personalizado', copy=True, tracking=0, )
    alias_defaults = fields.Text(string='Valores predeterminados', required=True, copy=True, tracking=0, )
    alias_domain = fields.Char(string='Dominio de alias', readonly=True, tracking=0, )
    alias_force_thread_id = fields.Integer(string='Registro de identificación de hilo', copy=True, tracking=0, )
    alias_id = fields.Many2one(string='Alias', store=True, required=True, copy=True, tracking=0,
                               comodel_name='mail.alias', )
    alias_model_id = fields.Many2one('ir.model', string='Modelo Alias', ondelete='set null', index=True, )
    alias_name = fields.Char(string='Sobre nombre', tracking=0, )
    alias_parent_model_id = fields.Many2one(string='Modelo matriz', copy=True, tracking=0, comodel_name='ir.model', )
    alias_parent_thread_id = fields.Integer(string='ID de hilo de registro principal', copy=True, tracking=0, )
    alias_user_id = fields.Many2one(string='Dueño', copy=True, tracking=0, comodel_name='res.users', )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    sh_resource_calendar_id = fields.Many2one(string='Horario de trabajo', store=True, required=True, copy=True,
                                              tracking=0, comodel_name='resource.calendar', )
    sla_count = fields.Integer(string='Conteo de SLA', readonly=True, tracking=0, )
    team_head = fields.Many2one(string='Jefe de equipo', store=True, required=True, copy=True, tracking=0,
                                comodel_name='res.users', )
    team_members = fields.Many2many(relation='equipodeserviciodeay_team_members_rel', column1='equipodeserviciodeay_id',
                                    column2='team_members_id', string='Miembros del equipo', store=True, copy=True,
                                    tracking=0,
                                    comodel_name='res.users', )


class Esquemasdeproductos(models.Model):
    _name = 'product.scheme'
    _description = 'Esquemas de Productos'
    code = fields.Char(string='schemeID', store=True, copy=True, tracking=0, )
    name = fields.Char(string='schemeName', store=True, copy=True, tracking=0, )
    scheme_agency_id = fields.Char(string='schemeAgencyID', store=True, copy=True, tracking=0, )


class Estadodelestudioocapacitación(models.Model):
    _name = 'estado.estudios.capacitaciones'
    _description = 'Estado del Estudio o Capacitación'
    name = fields.Char(string='Estado', store=True, required=True, copy=True, tracking=0, )


class Estadoderesultado(models.Model):
    _name = 'account.financial.report.state'
    _description = 'Estado de resultado'
    account_ids = fields.Many2many('account.account', relation='afr_stincwiz_account_rel', column1='wizard_id',
                                   column2='account_id', string='Cuentas', copy=False, )
    company_id = fields.Many2one(string='Compañia', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicio', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha Fin', store=True, copy=True, tracking=0, )


class Estructurainformescontables(models.Model):
    _name = 'account.financial.structure'
    _description = 'Estructura Informes Contables'
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    is_active = fields.Boolean(string='Activo', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class Estudiosycapacitaciones(models.Model):
    _name = 'estudios.capacitaciones'
    _description = 'Estudios y Capacitaciones'
    ciudad_id = fields.Many2one(string='Ciudad', store=True, copy=True, tracking=0, comodel_name='res.city', )
    comentarios = fields.Text(string='Comentarios', store=True, copy=True, tracking=0, )
    duracion = fields.Float(string='Duración', store=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, required=True, copy=True, tracking=0,
                                  comodel_name='hr.employee', )
    estado_id = fields.Many2one(string='Estado', store=True, copy=True, tracking=0,
                                comodel_name='estado.estudios.capacitaciones', )
    fecha_inicio = fields.Date(string='Fecha de Inicio', store=True, copy=True, tracking=0, )
    fecha_terminacion = fields.Date(string='Fecha de Terminación', store=True, copy=True, tracking=0, )
    fecha_vencimiento = fields.Date(string='Fecha Vencimiento Estudio/Curso', store=True, copy=True, tracking=0, )
    institucion_id = fields.Many2one(string='Institución', store=True, copy=True, tracking=0,
                                     comodel_name='instituciones.estudios.capacitaciones', )
    numero_registro = fields.Char(string='Número de Registro', store=True, copy=True, tracking=0, )
    periodo_curso = fields.Char(string='Periodo en Curso', store=True, copy=True, tracking=0, )
    tipo_duracion_id = fields.Many2one(string='Tipo Duración', store=True, copy=True, tracking=0,
                                       comodel_name='tipo.duracion.estudios.capacitaciones', )
    tipo_id = fields.Many2one(string='Tipo', store=True, copy=True, tracking=0,
                              comodel_name='tipo.estudios.capacitaciones', )
    titulo_id = fields.Many2one(string='Título', store=True, copy=True, tracking=0,
                                comodel_name='titulos.educativos.estudios.capacitaciones', )


class Etapasdelareclamación(models.Model):
    _name = 'crm.claim.stage'
    _description = 'Etapas de la reclamación'
    case_default = fields.Boolean(string='Común a todos los equipos', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre de la etapa', store=True, required=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    team_ids = fields.Many2many(relation='estudiosycapacitacio_team_ids_rel', column1='estudiosycapacitacio_id',
                                column2='team_ids_id', string='Equipos', store=True, copy=True, tracking=0,
                                comodel_name='crm.team', )


class Etapasdeserviciodeayuda(models.Model):
    _name = 'helpdesk.stages'
    _description = 'Etapas de servicio de ayuda'
    is_cancel_button_visible = fields.Boolean(string='¿Es visible el botón Cancelar?', store=True, copy=True,
                                              tracking=0, )
    is_closed_stage = fields.Boolean(string='Is Closed Stage?', store=True, copy=True, tracking=0, )
    is_done_button_visible = fields.Boolean(string='¿Es visible el botón resuelto?', store=True, copy=True,
                                            tracking=0, )
    is_pause_stage = fields.Boolean(string='Is Pause Stage?', store=True, copy=True, tracking=0, )
    is_reopen_stage = fields.Boolean(string='Is Reopen Stage?', store=True, copy=True, tracking=0, )
    is_validated_stage = fields.Boolean(string='Is Validated Stage?', store=True, copy=True, tracking=0, )
    mail_template_ids = fields.Many2many(relation='etapasdeserviciodeay_mail_template_ids_rel',
                                         column1='etapasdeserviciodeay_id', column2='mail_template_ids_id',
                                         string='Plantilla de correo', store=True, copy=True, tracking=0,
                                         comodel_name='mail.template', )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    sh_group_ids = fields.Many2many(relation='etapasdeserviciodeay_sh_group_ids_rel', column1='etapasdeserviciodeay_id',
                                    column2='sh_group_ids_id', string='Grupos', store=True, copy=True, tracking=0,
                                    comodel_name='res.groups', )
    sh_next_stage = fields.Many2one(string='Siguiente etapa', store=True, copy=True, tracking=0,
                                    comodel_name='helpdesk.stages', )


class Etiquetadeldocumento(models.Model):
    _name = 'dms.tag'
    _description = 'Etiqueta del documento'
    active = fields.Boolean(string='Activo', store=True, copy=True, tracking=0, )
    category_id = fields.Many2one(string='Categoría', store=True, copy=True, tracking=0,
                                  comodel_name='dms.category', )
    color = fields.Integer(string='Índice de color', store=True, copy=True, tracking=0, )
    count_directories = fields.Integer(string='Nº de carpetas', readonly=True, tracking=0, )
    count_files = fields.Integer(string='Nº de archivos', readonly=True, tracking=0, )
    directory_ids = fields.Many2many(relation='etiquetadeldocumento_directory_ids_rel',
                                     column1='etiquetadeldocumento_id', column2='directory_ids_id', string='Carpetas',
                                     store=True, readonly=True, copy=True, tracking=0,
                                     comodel_name='dms.directory', )
    file_ids = fields.Many2many(relation='etiquetadeldocumento_file_ids_rel', column1='etiquetadeldocumento_id',
                                column2='file_ids_id', string='Archivos', store=True, readonly=True, copy=True,
                                tracking=0,
                                comodel_name='dms.file', )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Etiquetasdeserviciodeayuda(models.Model):
    _name = 'helpdesk.tags'
    _description = 'Etiquetas de servicio de ayuda'
    color = fields.Integer(string='Indice de color', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class ExportformatforaccountingSreports(models.Model):
    _name = 'account_financial_reports.export.wizard.format'
    _description = 'Export format for accounting S reports'
    export_wizard_id = fields.Many2one(string='Parent Wizard', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account_financial_reports.export.wizard', )
    fun_to_call = fields.Char(string='Function to Call', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Name', store=True, required=True, copy=True, tracking=0, )


class ExportwizardforaccountingSreports(models.Model):
    _name = 'account_financial_reports.export.wizard'
    _description = 'Export wizard for accounting S reports'
    doc_name = fields.Char(string='Documents Name', store=True, copy=True, tracking=0, )
    export_format_ids = fields.Many2many(comodel_name='account.financial.reports.export.wizard.format',
                                         relation='afr_exportwiz_fmt_rel', column1='wizard_id', column2='format_id',
                                         string='Export to',
                                         copy=False, )
    report_id = fields.Integer(string='Parent Report Id', store=True, required=True, copy=True, tracking=0, )
    report_model = fields.Char(string='Report Model', store=True, required=True, copy=True, tracking=0, )


class Facturarentrega(models.Model):
    _name = 'delivery.invoice'
    _description = 'Facturar Entrega'
    activity_date_deadline = fields.Date(string='Siguiente plazo de actividad', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Resumen de la siguiente actividad', tracking=0, )
    activity_type_icon = fields.Char(string='Ícono de tipo de actvidad', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Siguiente tipo de actividad', tracking=0,
                                       comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Usuario responsable', tracking=0, comodel_name='res.users', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    currency_id = fields.Many2one(string='Moneda', readonly=True, tracking=0, comodel_name='res.currency', )
    guides_ids = fields.Many2many(relation='facturarentrega_guides_ids_rel', column1='facturarentrega_id',
                                  column2='guides_ids_id', string='Guias', store=True, copy=True, tracking=0,
                                  comodel_name='delivery.guide', )
    journal_id = fields.Many2one(string='Diario', store=True, copy=True, tracking=0, comodel_name='account.journal', )
    message_attachment_count = fields.Integer(string='Nº de archivos adjuntos', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='facturarentrega_message_channel_ids_rel',
                                           column1='facturarentrega_id', column2='message_channel_ids_id',
                                           string='Seguidores (Canales)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Numero de errores', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Error de Envío de Mensaje', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Es un seguidor', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Adjuntos principales', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Numero de Acciones', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Acción requerida', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='facturarentrega_message_partner_ids_rel',
                                           column1='facturarentrega_id', column2='message_partner_ids_id',
                                           string='Seguidores (Contactos)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Nº de mensajes sin leer', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Mensajes sin Leer', readonly=True, tracking=0, )
    move_id = fields.Many2one(string='Factura', store=True, copy=True, tracking=0, comodel_name='account.move', )
    my_activity_date_deadline = fields.Date(string='Mis Actividades Vencidas', readonly=True, tracking=0, )
    notes = fields.Text(string='Notas', store=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Transportista', store=True, copy=True, tracking=100,
                                 comodel_name='res.partner', )
    price_total = fields.Monetary(string='Precio Total', readonly=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )
    weight_invoiced = fields.Float(string='Peso', readonly=True, tracking=0, )
    weight_returned = fields.Float(string='Peso Retornado', readonly=True, tracking=0, )


class Facturasporagrupar(models.Model):
    _name = 'account.move.recoup'
    _description = 'Facturas por agrupar'
    invoices = fields.Text(string='Facturas por agrupar', store=True, readonly=True, copy=True, tracking=0, )


class Familiares(models.Model):
    _name = 'hr.familiar'
    _description = 'Familiares'
    date = fields.Date(string='Fecha de Nacimineto', store=True, required=True, copy=True, tracking=0, )
    depends = fields.Boolean(string='¿Dependiente?', store=True, copy=True, tracking=0, )
    document_id = fields.Many2one(string='Tipo de Documento', store=True, copy=True, tracking=0,
                                  comodel_name='res.partner.document.type', )
    document = fields.Char(string='Documento', store=True, copy=True, tracking=0, )
    familiar_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    home_contributor = fields.Boolean(string='Aporta ingresos al Hogar', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    parent = fields.Char(string='ParentescoT', store=True, copy=True, tracking=0, )
    phone = fields.Char(string='Teléfono', store=True, copy=True, tracking=0, )
    type_id = fields.Char(string='T. Documento', store=True, copy=True, tracking=0, )


class Festivosenaño(models.Model):
    _name = 'hr.holiday.year'
    _description = 'Festivos en Año'
    date_end = fields.Date(string='Fecha de finalización', store=True, required=True, copy=True, tracking=0, )
    date_start = fields.Date(string='Fecha de Inicio', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Año', store=True, required=True, copy=True, tracking=0, )


class Financialassetsreport(models.Model):
    _name = 'wiz.account.asset.report'
    _description = 'Financial Assets report'
    asset_group_id = fields.Many2one(string='Grupo de activo', store=True, copy=True, tracking=0,
                                     comodel_name='account.asset.group', )
    company_id = fields.Many2one(string='Compañía', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    date_from = fields.Date(string='Start Date', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='End Date', store=True, required=True, copy=True, tracking=0, )
    draft = fields.Boolean(string='Include draft assets', store=True, copy=True, tracking=0, )


class Formasdepago(models.Model):
    _name = 'account.payment.mean'
    _description = 'Formas de Pago'
    code = fields.Char(string='Código', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Fusionarwizarddetickets(models.TransientModel):
    _name = 'sh.helpdesk.ticket.merge.ticket.wizard'
    _description = 'Fusionar Wizard de tickets'
    sh_check_multi_user = fields.Boolean(string='Permitir múltiples usuarios', copy=False)
    sh_existing_ticket = fields.Many2one('helpdesk.ticket', string='Seleccionar ticket', copy=False)
    sh_helpdesk_tags = fields.Many2many('helpdesk.tags', relation='sh_hd_merge_tag_rel', column1='wizard_id',
                                        column2='tag_id', string='Etiquetas', copy=False, )
    sh_helpdesk_ticket_ids = fields.Many2many('helpdesk.ticket', relation='sh_hd_merge_tickets_rel',
                                              column1='wizard_id',
                                              column2='ticket_id', string='Tickets', copy=False, )
    sh_merge_history = fields.Boolean(string='Historia de fusiones', copy=False)
    sh_partner_id = fields.Many2one('res.partner', string='Cliente', required=True, copy=False)
    sh_priority = fields.Many2one('helpdesk.priority', string='Prioridad', copy=False)
    sh_subject_id = fields.Many2one('helpdesk.sub.type', string='Tema', copy=False)
    sh_team_head_id = fields.Many2one('res.users', string='Jefe de equipo', readonly=True, copy=False)
    sh_team_id = fields.Many2one('helpdesk.team', string='Equipo', copy=False)
    sh_ticket_alarm_ids = fields.Many2many('sh.ticket.alarm', relation='sh_hd_merge_alarm_rel', column1='wizard_id',
                                           column2='alarm_id', string='Recordatorio de tickets', copy=False, )
    sh_user_id = fields.Many2one('res.users', string='Usuario asignado', copy=False)
    sh_user_ids = fields.Many2many('res.users', relation='sh_hd_merge_user_rel', column1='wizard_id', column2='user_id',
                                   string='Asignar múltiples usuarios', copy=False, )
    ticket_type = fields.Many2one('helpdesk.ticket.type', string='Tipo Interno', copy=False)


class Gasto(models.Model):
    _name = 'hr.expense.expense'
    _description = 'Gasto'
    account_move_line_refund_id = fields.Many2one(string='Linea a reconciliar reembolso', store=True, copy=True,
                                                  tracking=0, comodel_name='account.move.line', )
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Next Activity Type', tracking=0, comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    advance_id = fields.Many2one(string='Anticipo', store=True, copy=True, tracking=100,
                                 comodel_name='hr.payroll.advance', )
    amount_total2 = fields.Float(string='Total con Impuestos', store=True, readonly=True, tracking=0, )
    amount = fields.Float(string='Total', readonly=True, tracking=0, )
    background_minor_box_related = fields.Float(string='Fondo Caja Menor', readonly=True, tracking=100, )
    background_minor_box = fields.Float(string='Fondo Caja Menor', store=True, copy=True, tracking=100, )
    balance_minor_box = fields.Float(string='Saldo Caja Menor', store=True, readonly=True, tracking=100, )
    company_currency_id = fields.Many2one(string='Moneda de la Compañia', readonly=True, tracking=0,
                                          comodel_name='res.currency', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=100, comodel_name='res.company', )
    currency_id = fields.Many2one(string='Moneda', store=True, copy=True, tracking=100, comodel_name='res.currency', )
    date_move = fields.Date(string='Fecha de Contabilización', store=True, copy=True, tracking=100, )
    date_valid = fields.Date(string='Fecha de Validación', store=True, copy=True, tracking=100, )
    department_id = fields.Many2one(string='Área/Departamento/Contrato', store=True, copy=True, tracking=100,
                                    comodel_name='hr.department', )
    description = fields.Char(string='Descripción', store=True, copy=True, tracking=100, )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=100,
                                  comodel_name='hr.employee', )
    is_paid = fields.Boolean(string='Esta pagado?', readonly=True, tracking=0, )
    journal_id = fields.Many2one(string='Diario Forzado', store=True, copy=True, tracking=100,
                                 comodel_name='account.journal', )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='gasto_message_channel_ids_rel', column1='gasto_id',
                                           column2='message_channel_ids_id', string='Followers (Channels)',
                                           readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='gasto_message_partner_ids_rel', column1='gasto_id',
                                           column2='message_partner_ids_id', string='Followers (Partners)',
                                           readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    move_id = fields.Many2one(string='Asiento Contable', store=True, copy=True, tracking=100,
                              comodel_name='account.move', )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    partial_reconciled = fields.Boolean(string='Partial Reconcile', readonly=True, tracking=0, )
    valid_user_id = fields.Many2one(string='Validado Por', store=True, copy=True, tracking=100,
                                    comodel_name='res.users', )
    x_parent_id = fields.Many2one(string='Director Empleado', tracking=0, comodel_name='res.users', )


class Generadordelíneasdecontroldecrédito(models.Model):
    _name = 'credit.control.run'
    _description = 'Generador de líneas de control de crédito'
    company_id = fields.Many2one(string='Compañía', index=True, store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    credit_control_communication_count = fields.Integer(string='# of Credit Control Communications', readonly=True,
                                                        tracking=0, )
    credit_control_count = fields.Integer(string='Líneas de control de crédito', readonly=True, tracking=0, )
    date = fields.Date(string='Fecha del control', store=True, readonly=True, required=True, copy=True, tracking=0, )
    hide_change_state_button = fields.Boolean(string='Hide Change State Button', store=True, copy=True, tracking=0, )
    manual_ids = fields.Many2many(relation='gasto_manual_ids_rel', column1='gasto_id', column2='manual_ids_id',
                                  string='Líneas a tratar manualmente', store=True, readonly=True, tracking=0,
                                  comodel_name='account.move.line', )
    policy_ids = fields.Many2many(relation='gasto_policy_ids_rel', column1='gasto_id', column2='policy_ids_id',
                                  string='Políticas', store=True, readonly=True, copy=True, tracking=0,
                                  comodel_name='credit.control.policy', )
    report = fields.Html(string='Informe', store=True, readonly=True, tracking=0, )


class Generadorderangosdefecha(models.Model):
    _name = 'date.range.generator'
    _description = 'Generador de rangos de fecha'
    company_id = fields.Many2one(string='Compañía', store=True, copy=True, tracking=0, comodel_name='res.company', )
    count = fields.Integer(string='Número de rangos a generar', store=True, required=True, copy=True, tracking=0, )
    date_start = fields.Date(string='Fecha de Inicio', store=True, required=True, copy=True, tracking=0, )
    duration_count = fields.Integer(string='Duración', store=True, required=True, copy=True, tracking=0, )
    name_prefix = fields.Char(string='Prefijo del nombre del rango', store=True, required=True, copy=True,
                              tracking=0, )
    type_id = fields.Many2one(string='Tipo', store=True, required=True, copy=True, tracking=0,
                              comodel_name='date.range.type', )


class Gestióndeprocesosdisciplinarios(models.Model):
    _name = 'procesos.disciplinarios'
    _description = 'Gestión de Procesos Disciplinarios'
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Next Activity Type', tracking=0, comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    archivos_adjuntos = fields.Many2many(relation='generadorderangosdef_archivos_adjuntos_rel',
                                         column1='generadorderangosdef_id', column2='archivos_adjuntos_id',
                                         string='Archivos Adjuntos', store=True, copy=True, tracking=0,
                                         comodel_name='ir.attachment', )
    cargo = fields.Char(string='Cargo', store=True, readonly=True, tracking=0, )
    centro_costos = fields.Many2one(string='Centro de Costos', store=True, required=True, copy=True, tracking=0,
                                    comodel_name='account.analytic.account', )
    coordinador = fields.Many2one(string='Coordinador del Puesto', store=True, copy=True, tracking=0,
                                  comodel_name='hr.employee', )
    descripcion_falta = fields.Text(string='Descripción de la Falta', store=True, required=True, copy=True,
                                    tracking=0, )
    empleado = fields.Many2one(string='Empleado', store=True, readonly=True, required=True, copy=True, tracking=0,
                               comodel_name='hr.employee', )
    estado_procede = fields.Boolean(string='Estado Procede', store=True, copy=True, tracking=0, )
    estado_suspendido = fields.Boolean(string='Estado Suspendido', store=True, copy=True, tracking=0, )
    fecha_falta = fields.Date(string='Fecha de la Falta Cometida', store=True, required=True, copy=True, tracking=0, )
    fecha_hasta_sancion = fields.Date(string='Fecha Hasta de la Sanción', store=True, copy=True, tracking=0, )
    fecha_informe = fields.Date(string='Fecha de Realización del Informe', store=True, required=True, copy=True,
                                tracking=0, )
    fecha_reinicio_laboral = fields.Date(string='Fecha de Reinicio de Labores', store=True, copy=True, tracking=0, )
    fecha_sancion = fields.Date(string='Fecha de Sanción', store=True, copy=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='generadorderangosdef_message_channel_ids_rel',
                                           column1='generadorderangosdef_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='generadorderangosdef_message_partner_ids_rel',
                                           column1='generadorderangosdef_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    numero_identificacion = fields.Char(string='Número de Identificación', store=True, required=True, copy=True,
                                        tracking=0, )
    observaciones = fields.Text(string='Observaciones', store=True, copy=True, tracking=0, )
    otro_tipo_motivo = fields.Char(string='Otro Tipo de Motivo', store=True, copy=True, tracking=0, )
    otro_tipo_sancion = fields.Char(string='Otro Tipo de Sanción', store=True, copy=True, tracking=0, )
    persona_informe = fields.Many2one(string='Persona que Realiza el Informe', store=True, required=True, copy=True,
                                      tracking=0, comodel_name='hr.employee', )
    reentrenamiento = fields.Boolean(string='Reentrenamiento', store=True, copy=True, tracking=0, )
    subzona = fields.Char(string='Subzona', store=True, readonly=True, tracking=0, )
    tipo_motivo_nombre = fields.Char(string='Nombre Tipo Motivo', store=True, readonly=True, tracking=0, )
    tipo_motivo = fields.Many2one(string='Tipo Motivo', store=True, required=True, copy=True, tracking=0,
                                  comodel_name='tipo.motivo.procesos.disciplinarios', )
    tipo_sancion_nombre = fields.Char(string='Nombre Tipo Sanción', store=True, readonly=True, tracking=0, )
    tipo_sancion = fields.Many2one(string='Tipo sanción', store=True, required=True, copy=True, tracking=0,
                                   comodel_name='tipo.sancion.procesos.disciplinarios', )
    x_branch_id = fields.Many2one(string='Sucursal', store=True, readonly=True, tracking=1, comodel_name='hr.branch', )
    x_city_id = fields.Many2one(string='Ciudad', store=True, copy=True, tracking=1, comodel_name='res.city', )
    x_department_id = fields.Many2one(string='Área / Departamento / Contrato', store=True, copy=True, tracking=1,
                                      comodel_name='hr.department', )
    x_descripcion_citacion = fields.Text(string='Detalles del lugar', store=True, copy=True, tracking=1, )
    x_descripcion_falta = fields.Text(string='Descripción de la Falta', store=True, copy=True, tracking=1, )
    x_duracion_suspension = fields.Integer(string='Duración de la suspensión (días)', store=True, readonly=True,
                                           tracking=1, )
    x_fecha_citacion = fields.Date(string='Fecha de la Citación', store=True, copy=True, tracking=1, )
    x_fecha_reinicio_labor = fields.Date(string='Fecha de Reinicio de Labores', store=True, copy=True, tracking=1, )
    x_fecha_suspension = fields.Date(string='Fecha Suspensión', store=True, copy=True, tracking=1, )
    x_hora_citacion = fields.Float(string='Hora de la Citación', store=True, copy=True, tracking=1, )
    x_hora_falta = fields.Datetime(string='Hora de la Falta', store=True, copy=True, tracking=1, )
    x_hora_falta1 = fields.Float(string='Hora de la Falta', store=True, copy=True, tracking=1, )
    x_informacion_testigo = fields.Text(string='Información de testigo(s)', store=True, copy=True, tracking=1, )
    x_observacion = fields.Text(string='Observaciones', store=True, copy=True, tracking=1, )
    x_partner_id = fields.Many2one(string='Cliente', store=True, tracking=1, comodel_name='res.partner', )
    x_regional_id = fields.Many2one(string='Sucursal', store=True, copy=True, tracking=1,
                                    comodel_name='res.regional', )
    x_san_sign_last_link = fields.Char(string='Último enlace firma sanción', store=True, copy=True, tracking=1, )
    x_san_sign_token_expire = fields.Datetime(string='Vence token sanción', store=True, copy=True, tracking=1, )
    x_san_sign_token = fields.Char(string='Token firma sanción', store=True, copy=True, tracking=1, )
    x_san_signature_date = fields.Datetime(string='Fecha firma (Sanción)', store=True, copy=True, tracking=1, )
    x_san_signature_employee_id = fields.Many2one(string='Empleado firmante (Sanción)', store=True, copy=True,
                                                  tracking=1,
                                                  comodel_name='hr.employee', )
    x_san_signature_image = fields.Binary(string='Firma (Sanción)', store=True, copy=True, tracking=1, )
    x_san_signed_pdf_attachment_id = fields.Many2one(string='PDF sanción firmado', store=True, copy=True, tracking=1,
                                                     comodel_name='ir.attachment', )
    x_sign_last_link = fields.Char(string='Último enlace de firma', store=True, copy=True, tracking=1, )
    x_sign_status = fields.Char(string='Estado de Firma', store=True, copy=True, tracking=1, )
    x_sign_token_expire = fields.Datetime(string='Expira enlace firma', store=True, copy=True, tracking=1, )
    x_sign_token = fields.Char(string='Token firma (público)', store=True, copy=True, tracking=1, )
    x_signature_date = fields.Datetime(string='Fecha de Firma', store=True, copy=True, tracking=1, )
    x_signature_employee_id = fields.Many2one(string='Empleado (Firma)', store=True, copy=True, tracking=1,
                                              comodel_name='hr.employee', )
    x_signature_image = fields.Binary(string='Firma del Empleado', store=True, copy=True, tracking=1, )
    x_signed_pdf_attachment_id = fields.Many2one(string='PDF Firmado', store=True, copy=True, tracking=1,
                                                 comodel_name='ir.attachment', )
    x_url_reunion = fields.Char(string='URL de la reunión', store=True, copy=True, tracking=1, )
    zona = fields.Char(string='Zona', store=True, readonly=True, tracking=0, )


class Googlegmailmixin(models.Model):
    _name = 'google.gmail.mixin'
    _description = 'Google Gmail Mixin'
    google_gmail_access_token_expiration = fields.Integer(string='Access Token Expiration Timestamp', store=True,
                                                          tracking=0, )
    google_gmail_access_token = fields.Char(string='Access Token', store=True, tracking=0, )
    google_gmail_authorization_code = fields.Char(string='Authorization Code', store=True, tracking=0, )
    google_gmail_refresh_token = fields.Char(string='Refresh Token', store=True, tracking=0, )
    google_gmail_uri = fields.Char(string='URI', readonly=True, tracking=0, )
    use_google_gmail_service = fields.Boolean(string='Gmail Authentication', store=True, copy=True, tracking=0, )


class Grupodeactivo(models.Model):
    _name = 'account.asset.group'
    _description = 'Grupo de activo'
    code = fields.Char(string='Código', index=True, store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañía', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    name = fields.Char(string='Nombre', index=True, store=True, required=True, copy=True, tracking=0, )
    parent_id = fields.Many2one(string='Grupo de activo padre', store=True, copy=True, tracking=0,
                                comodel_name='account.asset.group', )
    parent_path = fields.Char(string='Ruta padre', index=True, store=True, copy=True, tracking=0, )


class Grupodecontratos(models.Model):
    _name = 'hr.contract.group'
    _description = 'Grupo de Contratos'
    company_id = fields.Many2one(string='Company', index=True, store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    name = fields.Char(string='Nombre de Grupo', store=True, copy=True, tracking=0, )
    transport_second_fortnight = fields.Boolean(string='Auxilo Transporte Segunda Quincena', store=True, copy=True,
                                                tracking=0, )
    x_user_id = fields.Many2one(string='Analista de Nomina', store=True, copy=True, tracking=1,
                                comodel_name='res.users', )


class Gruposdeaccesoderegistro(models.Model):
    _name = 'dms.access.group'
    _description = 'Grupos de acceso de registro'
    complete_directory_ids = fields.Many2many('dms.directory', relation='dms_access_group_comp_dir_rel',
                                              column1='group_id',
                                              column2='directory_id', string='Directorios (completos)')
    count_directories = fields.Integer(string='Nº de carpetas', readonly=True, tracking=0, )
    count_users = fields.Integer(string='Usuarios', store=True, readonly=True, tracking=0, )
    directory_ids = fields.Many2many('dms.directory', relation='dms_access_group_dir_rel', column1='group_id',
                                     column2='directory_id', string='Directorios')
    explicit_user_ids = fields.Many2many('res.users', relation='dms_access_group_exp_users_rel', column1='group_id',
                                         column2='user_id', string='Usuarios explícitos')
    group_ids = fields.Many2many(relation='gruposdeaccesoderegi_group_ids_rel', column1='gruposdeaccesoderegi_id',
                                 column2='group_ids_id', string='Grupos', store=True, copy=True, tracking=0,
                                 comodel_name='res.groups', )
    name = fields.Char(string='Nombre del grupo', store=True, required=True, copy=True, tracking=0, )
    parent_group_id = fields.Many2one(string='Carpeta padre', index=True, store=True, copy=True, tracking=0,
                                      comodel_name='dms.access.group', )
    parent_path = fields.Char(string='Modelo padre', index=True, store=True, copy=True, tracking=0, )
    perm_create = fields.Boolean(string='Acceso de creación', store=True, copy=True, tracking=0, )
    perm_inclusive_create = fields.Boolean(string='Inherited Create Access', store=True, readonly=True, tracking=0, )
    perm_inclusive_unlink = fields.Boolean(string='Inherited Unlink Access', store=True, readonly=True, tracking=0, )
    perm_inclusive_write = fields.Boolean(string='Inherited Write Access', store=True, readonly=True, tracking=0, )
    perm_unlink = fields.Boolean(string='Acceso de eliminación', store=True, copy=True, tracking=0, )
    perm_write = fields.Boolean(string='Acceso de escritura', store=True, copy=True, tracking=0, )
    users = fields.Many2many('res.users', relation='dms_access_group_res_users_rel', column1='group_id',
                             column2='user_id', string='Usuarios')


class Gruposdenotificación(models.Model):
    _name = 'einvoice.notification.group'
    _description = 'Grupos de Notificación'
    company_id = fields.Many2one(string='Compañía', store=True, copy=True, tracking=0, comodel_name='res.company', )
    email = fields.Char(string='Correo electrónico', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class Guiadeentrega(models.Model):
    _name = 'delivery.guide'
    _description = 'Guía de Entrega'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string='Número', required=True, readonly=True, default='/', copy=False, tracking=True)
    company_id = fields.Many2one('res.company', string='Compañía', required=True, index=True,
                                 default=lambda self: self.env.company, tracking=True)
    currency_id = fields.Many2one('res.currency', string='Moneda', related='company_id.currency_id', store=True,
                                  readonly=True)
    date_scheduled = fields.Date(string='Fecha Programada', required=True, copy=True, tracking=True)
    date_progress = fields.Date(string='Fecha en Progreso', copy=True)
    date_delivered = fields.Date(string='Fecha de Entrega', copy=True)
    date_checked = fields.Date(string='Fecha de Revisión', copy=True)
    date_invoiced = fields.Date(string='Fecha de Factura', copy=True)
    partner_id = fields.Many2one('res.partner', string='Proveedor', required=True, copy=True, tracking=True)
    branch_id = fields.Many2one('hr.branch', string='Sucursal', copy=True)
    analytic_id = fields.Many2one('account.analytic.account', string='Cuenta Analítica', copy=True, index=True)
    analytic_tag_ids = fields.Many2many('account.analytic.tag', relation='delivery_guide_analytic_tag_rel',
                                        column1='guide_id', column2='tag_id', string='Etiquetas analíticas', copy=True)
    pickings_ids = fields.Many2many('stock.picking', relation='delivery_guide_picking_rel', column1='guide_id',
                                    column2='picking_id', string='Transferencias')
    moves_ids = fields.Many2many('stock.move', relation='delivery_guide_move_rel', column1='guide_id',
                                 column2='move_id',
                                 string='Movimientos de stock')
    sales_ids = fields.Many2many('sale.order', relation='delivery_guide_sale_rel', column1='guide_id',
                                 column2='order_id', string='Ventas')
    invoices_ids = fields.Many2many('account.move', relation='delivery_guide_invoice_rel', column1='guide_id',
                                    column2='move_id', string='Facturas')
    invoices_returns_ids = fields.Many2many('account.move', relation='delivery_guide_refund_rel', column1='guide_id',
                                            column2='move_id', string='Facturas rectificativas')
    driver_id = fields.Many2one('res.partner.driver', string='Conductor', copy=False)
    driver_name = fields.Char(string='Nombre', readonly=True)
    driver_mobile = fields.Char(string='Celular', readonly=True)
    driver_plate = fields.Char(string='Placa', readonly=True)
    driver_vat = fields.Char(string='NIT', readonly=True)
    driver_comment = fields.Text(string='Comentario', readonly=True)
    file_name = fields.Char(string='Nombre Público', copy=False)
    file_data = fields.Binary(string='Archivo', copy=False)
    consignment = fields.Char(string='Remesa', copy=True)
    notes = fields.Text(string='Términos y condiciones', copy=True)
    rate_id = fields.Many2one('delivery.rate', string='Tarifas de Entrega', copy=True)
    rate_line_id = fields.Many2one('delivery.rate.line', string='Valores', copy=True)
    price = fields.Monetary(string='Precio Ajustado', currency_field='currency_id', tracking=True)
    price_additional = fields.Monetary(string='Costo Adicional', currency_field='currency_id', copy=True)
    price_standby = fields.Monetary(string='Stand By', currency_field='currency_id', copy=True)
    price_subtotal = fields.Monetary(string='Costo Subtotal', currency_field='currency_id', readonly=True)
    price_total = fields.Monetary(string='Costo Total', currency_field='currency_id', readonly=True)
    rate_tolerance = fields.Float(string='Tolerancia (%)', readonly=True)
    price_tolerance = fields.Float(string='Tolerancia', readonly=True)
    weight_manual = fields.Float(string='Peso Manual', copy=True, tracking=True)
    weight_adjust = fields.Float(string='Peso Ajustado', copy=True)
    weight_invoice = fields.Float(string='Peso Entregado', readonly=True)
    weight_move = fields.Float(string='Peso de Movimientos', readonly=True)
    weight_return = fields.Float(string='Peso Retornado', readonly=True)
    weight_theoretical = fields.Float(string='Peso Teórico', copy=True)
    weight_total = fields.Float(string='Peso Total', readonly=True)
    guide_bool = fields.Boolean(string='Tiene devoluciones', copy=True)
    guide_update = fields.Boolean(string='Actualizar', copy=True)
    show_update_price_kg = fields.Boolean(string='Actualizando precio (Kg)', copy=True)
    show_update_weight_manual = fields.Boolean(string='Ha cambiado el peso (Kg)', copy=True)
    payment_boolean = fields.Boolean(string='Pagado', tracking=True, copy=True)

    # Numeración automática
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals['name'] in ('/', ''):
                vals['name'] = self.env['ir.sequence'].next_by_code('delivery.guide') or '/'
        return super().create(vals_list)


class Helpdeskrelease(models.Model):
    _name = 'helpdesk.release'
    _description = 'Helpdesk Release'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class Helpdesktaskinformation(models.Model):
    _name = 'sh.helpdesk.ticket.stage.info'
    _description = 'Helpdesk Task Information'
    date_in_by = fields.Many2one(string='Date In By', store=True, copy=True, tracking=0, comodel_name='res.users', )
    date_in = fields.Datetime(string='Date In', store=True, copy=True, tracking=0, )
    date_out_by = fields.Many2one(string='Date Out By', store=True, copy=True, tracking=0, comodel_name='res.users', )
    date_out = fields.Datetime(string='Date Out', store=True, copy=True, tracking=0, )
    day_diff = fields.Integer(string='Day Diff', store=True, copy=True, tracking=0, )
    stage_name = fields.Char(string='Stage Name', store=True, copy=True, tracking=0, )
    stage_task_id = fields.Many2one(string='Stage task', store=True, copy=True, tracking=0,
                                    comodel_name='helpdesk.ticket', )
    time_diff = fields.Float(string='Time Diff', store=True, copy=True, tracking=0, )
    total_time_diff = fields.Float(string='Total Time Diff', store=True, copy=True, tracking=0, )


class Helpdeskticketslaestado(models.Model):
    _name = 'sh.helpdesk.sla.status'
    _description = 'HelpDesk Ticket SLA Estado'
    color = fields.Integer(string='Indice de color', readonly=True, tracking=0, )
    sh_deadline = fields.Datetime(string='Fecha límite de SLA', store=True, readonly=True, tracking=0, )
    sh_done_sla_date = fields.Datetime(string='Sla Fecha de hecho', store=True, copy=True, tracking=0, )
    sh_sla_id = fields.Many2one(string='SH SLA', store=True, required=True, copy=True, tracking=0,
                                comodel_name='sh.helpdesk.sla', )
    sh_sla_stage_id = fields.Many2one(string='Alcanzar la etapa', store=True, readonly=True, tracking=0,
                                      comodel_name='helpdesk.stages', )
    sh_ticket_id = fields.Many2one(string='Tickets', index=True, store=True, required=True, copy=True, tracking=0,
                                   comodel_name='helpdesk.ticket', )


class Historialdepáginadeldocumento(models.Model):
    _name = 'document.page.history'
    _description = 'Historial de página del documento'
    company_id = fields.Many2one(string='Company', index=True, store=True, readonly=True, tracking=0,
                                 comodel_name='res.company', )
    content = fields.Text(string='Contenido', store=True, copy=True, tracking=0, )
    diff = fields.Text(string='Diff', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', index=True, store=True, copy=True, tracking=0, )
    page_id = fields.Many2one(string='Página', store=True, copy=True, tracking=0, comodel_name='document.page', )
    summary = fields.Char(string='Resumen', index=True, store=True, copy=True, tracking=0, )


class Historicodecambiosdeeps(models.Model):
    _name = 'eps.update.history'
    _description = 'Historico de Cambios de EPS'
    code_eps_ids = fields.Many2many(relation='historicodecambiosde_code_eps_ids_rel', column1='historicodecambiosde_id',
                                    column2='code_eps_ids_id', string='Otros EPS', readonly=True, tracking=0,
                                    comodel_name='hr.eps.code', )
    code_eps = fields.Many2one(string='Codigo EPS', store=True, copy=True, tracking=0, comodel_name='hr.eps.code', )
    company_id = fields.Many2one(string='Company', index=True, store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    contract_id = fields.Many2one(string='Contrato', store=True, required=True, copy=True, tracking=0,
                                  comodel_name='hr.contract', )
    date = fields.Date(string='Fecha', store=True, required=True, copy=True, tracking=0, )
    eps_id = fields.Many2one(string='EPS', store=True, required=True, copy=True, tracking=0,
                             comodel_name='res.partner', )
    user_id = fields.Many2one(string='Responsable', store=True, readonly=True, required=True, copy=True, tracking=0,
                              comodel_name='res.users', )


class Históricodecambiosdefondodecesantías(models.Model):
    _name = 'severance.update.history'
    _description = 'Histórico de Cambios de Fondo de Cesantías'
    afp_severance_id = fields.Many2one(string='Fondo de Cesantías', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='res.partner', )
    company_id = fields.Many2one(string='Company', index=True, store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    contract_id = fields.Many2one(string='Contrato', store=True, required=True, copy=True, tracking=0,
                                  comodel_name='hr.contract', )
    date = fields.Date(string='Fecha', store=True, required=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Responsable', store=True, readonly=True, required=True, copy=True, tracking=0,
                              comodel_name='res.users', )


class Históricodecambiosdefondodepension(models.Model):
    _name = 'pension.update.history'
    _description = 'Histórico de Cambios de Fondo de Pension'
    afp_pension_id = fields.Many2one(string='Fondo de Pensiones', store=True, required=True, copy=True, tracking=0,
                                     comodel_name='res.partner', )
    company_id = fields.Many2one(string='Company', index=True, store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    contract_id = fields.Many2one(string='Contrato', store=True, required=True, copy=True, tracking=0,
                                  comodel_name='hr.contract', )
    date = fields.Date(string='Fecha', store=True, required=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Responsable', store=True, readonly=True, required=True, copy=True, tracking=0,
                              comodel_name='res.users', )


class Históricodecambiosdegrupodecontrato(models.Model):
    _name = 'group.update.history'
    _description = 'Histórico de Cambios de Grupo de Contrato'
    company_id = fields.Many2one(string='Company', index=True, store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    contract_group_id = fields.Many2one(string='Grupo de Contrato', store=True, copy=True, tracking=0,
                                        comodel_name='hr.contract.group', )
    contract_id = fields.Many2one(string='Contrato', store=True, required=True, copy=True, tracking=0,
                                  comodel_name='hr.contract', )
    date = fields.Date(string='Fecha', store=True, required=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Responsable', store=True, readonly=True, required=True, copy=True, tracking=0,
                              comodel_name='res.users', )


class Históricodecambiosdesalario(models.Model):
    _name = 'wage.update.history'
    _description = 'Histórico de Cambios de Salario'
    company_id = fields.Many2one(string='Company', index=True, store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    contract_id = fields.Many2one(string='Contrato', store=True, required=True, copy=True, tracking=0,
                                  comodel_name='hr.contract', )
    date = fields.Datetime(string='Fecha', store=True, required=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Responsable', store=True, readonly=True, required=True, copy=True, tracking=0,
                              comodel_name='res.users', )
    wage = fields.Float(string='Salario', store=True, required=True, copy=True, tracking=0, )


class Holidaylines(models.Model):
    _name = 'hr.holiday.lines'
    _description = 'Holiday Lines'
    holiday_date = fields.Date(string='Date', store=True, required=True, copy=True, tracking=0, )
    holiday_id = fields.Many2one(string='Holiday List', store=True, copy=True, tracking=0,
                                 comodel_name='hr.holiday.public', )
    name = fields.Char(string='Reason', store=True, copy=True, tracking=0, )


class Horaextra(models.Model):
    _name = 'hr.overtime'
    _description = 'Hora Extra'
    access_token = fields.Char(string='Security Token', store=True, tracking=0, )
    access_url = fields.Char(string='Portal Access URL', readonly=True, tracking=0, )
    access_warning = fields.Text(string='Access warning', readonly=True, tracking=0, )
    account_analytic_id = fields.Many2one(string='Centro de Costo', store=True, copy=True, tracking=100,
                                          comodel_name='account.analytic.account', )
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Next Activity Type', tracking=0, comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    amount = fields.Float(string='Valor', store=True, readonly=True, tracking=100, )
    approve_date = fields.Date(string='Fecha de aprobación', store=True, copy=True, tracking=100, )
    cierre_period_id = fields.Many2one(string='Periodo de cierre', store=True, copy=True, tracking=100,
                                       comodel_name='hr.period', )
    close_from_solo_adicionales = fields.Boolean(string='Cerrado desde solo adicionales', store=True, copy=True,
                                                 tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, readonly=True, copy=True, tracking=100,
                                 comodel_name='res.company', )
    contract_group_id = fields.Many2one(string='Grupo de Contrato', readonly=True, tracking=100,
                                        comodel_name='hr.contract.group', )
    contract_id_2 = fields.Many2one(string='Contrato', store=True, copy=True, tracking=100,
                                    comodel_name='hr.contract', )
    contract_id = fields.Many2one(string='Contrato', store=True, required=True, copy=True, tracking=100,
                                  comodel_name='hr.contract', )
    date_end = fields.Date(string='Fecha Final', store=True, copy=True, tracking=100, )
    date_start_original = fields.Date(string='Inicio original', store=True, copy=True, tracking=0, )
    date_start = fields.Date(string='Fecha Inicio', store=True, required=True, copy=True, tracking=100, )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=100,
                                  comodel_name='hr.employee', )
    from_adicional = fields.Boolean(string='Desde adicional', store=True, copy=True, tracking=100, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='horaextra_message_channel_ids_rel', column1='horaextra_id',
                                           column2='message_channel_ids_id', string='Followers (Channels)',
                                           readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='horaextra_message_partner_ids_rel', column1='horaextra_id',
                                           column2='message_partner_ids_id', string='Followers (Partners)',
                                           readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    modalidad_id = fields.Many2one(string='Modalidad', store=True, copy=True, tracking=100,
                                   comodel_name='hr.roster.modalidad', )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, readonly=True, copy=True, tracking=100, )
    original_period = fields.Many2one(string='Periodo original', store=True, copy=True, tracking=0,
                                      comodel_name='hr.period', )
    overtime_type_id = fields.Many2one(string='Categoría Hora Extra', store=True, required=True, copy=True,
                                       tracking=100,
                                       comodel_name='hr.overtime.type', )
    payslip_id = fields.Many2one(string='Nónima', store=True, readonly=True, copy=True, tracking=100,
                                 comodel_name='hr.payslip', )
    period_id = fields.Many2one(string='Periodo', store=True, readonly=True, copy=True, tracking=100,
                                comodel_name='hr.period', )
    puesto_id = fields.Many2one(string='Puesto', store=True, copy=True, tracking=100,
                                comodel_name='hr.roster.puesto', )
    qty = fields.Float(string='Cantidad', store=True, required=True, copy=True, tracking=100, )
    rate = fields.Float(string='Factor', readonly=True, tracking=100, )
    roster = fields.Boolean(string='Origen cierre de turnos', store=True, copy=True, tracking=100, )
    tipo_pago = fields.Char(string='Tipo de Pago', store=True, copy=True, tracking=100, )
    total = fields.Float(string='Total', store=True, readonly=True, copy=True, tracking=100, )
    turn_ids = fields.Many2many(relation='horaextra_turn_ids_rel', column1='horaextra_id', column2='turn_ids_id',
                                string='Turnos que intervienen', store=True, copy=True, tracking=0,
                                comodel_name='hr.roster.turno', )
    unit = fields.Float(string='Valor Unitario', store=True, readonly=True, copy=True, tracking=100, )


class Horasextra(models.Model):
    _name = 'hr.payroll.extrahours'
    _description = 'Horas Extra'
    account_analytic_id = fields.Many2one(string='Centro de Costo', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Next Activity Type', tracking=0, comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    approve_date = fields.Date(string='Fecha de Aprobacion', store=True, readonly=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Company', store=True, copy=True, tracking=0, comodel_name='res.company', )
    contract_id_2 = fields.Many2one(string='Contrato', store=True, readonly=True, required=True, copy=True,
                                    tracking=0,
                                    comodel_name='hr.contract', )
    contract_id = fields.Many2one(string='Contrato', store=True, readonly=True, required=True, copy=True, tracking=0,
                                  comodel_name='hr.contract', )
    date_end = fields.Datetime(string='Finaliza', store=True, readonly=True, copy=True, tracking=0, )
    date_start = fields.Datetime(string='Comienza', store=True, readonly=True, required=True, copy=True, tracking=0, )
    description = fields.Text(string='Descripcion', store=True, readonly=True, copy=True, tracking=0, )
    duracion = fields.Float(string='Duracion', store=True, readonly=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, readonly=True, required=True, copy=True, tracking=0,
                                  comodel_name='hr.employee', )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='horasextra_message_channel_ids_rel', column1='horasextra_id',
                                           column2='message_channel_ids_id', string='Followers (Channels)',
                                           readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='Error de entrega del SMS', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='horasextra_message_partner_ids_rel', column1='horasextra_id',
                                           column2='message_partner_ids_id', string='Followers (Partners)',
                                           readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    name = fields.Char(string='Codigo', store=True, readonly=True, copy=True, tracking=0, )
    payslip_id = fields.Many2one(string='Pagado en nomina', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='hr.payslip', )
    roster = fields.Boolean(string='Origen cierre de turnos', store=True, copy=True, tracking=0, )
    total = fields.Float(string='Total', store=True, readonly=True, copy=True, tracking=0, )
    type_id = fields.Many2one(string='Tipo', store=True, readonly=True, required=True, copy=True, tracking=0,
                              comodel_name='hr.overtime.type', )
    unit = fields.Float(string='Valor Unitario', store=True, readonly=True, copy=True, tracking=0, )


class Horaslaborables(models.Model):
    _name = 'contract.hours.job'
    _description = 'Horas Laborables'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class Hrmassiveretired(models.Model):
    _name = 'hr.wizard.massive.retired'
    _description = 'HR Massive Retired'
    date_end = fields.Date(string='Fecha de finalización', store=True, required=True, copy=True, tracking=0, )
    settlement_date = fields.Date(string='Fecha de liquidación', store=True, required=True, copy=True, tracking=0, )
    settlement_period_id = fields.Many2one(string='Periodo de liquidación', store=True, required=True, copy=True,
                                           tracking=0, comodel_name='hr.period', )


class Hrpayslipconceptreport(models.Model):
    _name = 'hr.payslip.concept.report'
    _description = 'HR Payslip Concept Report'
    company_cost = fields.Boolean(string='Informe general de nómina', store=True, copy=True, tracking=0, )
    company_expense = fields.Boolean(string='Informe general de gastos de Compañia', store=True, copy=True,
                                     tracking=0, )
    concept_code = fields.Char(string='Codigo de concepto', store=True, copy=True, tracking=0, )
    contract_group_id = fields.Many2one(string='Grupo de Contrato', store=True, copy=True, tracking=0,
                                        comodel_name='hr.contract.group', )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    end_date = fields.Date(string='Fecha hasta', store=True, required=True, copy=True, tracking=0, )
    landscape = fields.Boolean(string='Horizontal', store=True, copy=True, tracking=0, )
    payslip_type_id = fields.Many2one(string='Tipo de nomina', store=True, copy=True, tracking=0,
                                      comodel_name='hr.payslip.type', )
    run_id_1 = fields.Many2one(string='Lote de nomina', store=True, copy=True, tracking=0,
                               comodel_name='hr.payslip.processing', )
    start_date = fields.Date(string='Fecha desde', store=True, required=True, copy=True, tracking=0, )
    workcenter = fields.Char(string='Centro de Trabajo', store=True, copy=True, tracking=0, )


class Hrupdatebookvacation(models.Model):
    _name = 'hr.update.book.vacation'
    _description = 'HR Update Book Vacation'
    date = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )


class Importarxlsxcomocsv(models.Model):
    _name = 'import.excel.wizard'
    _description = 'Importar XLSX como CSV'
    file = fields.Binary(string='Archivo XLSX', store=True, required=True, copy=True, tracking=0, )


class Importbankstatement(models.Model):
    _name = 'account.banking.bank.import'
    _description = 'Import Bank Statement'
    date_from = fields.Date(string='Fecha desde', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha hasta', store=True, required=True, copy=True, tracking=0, )
    file = fields.Binary(string='Archivo', store=True, required=True, copy=True, tracking=0, )
    journal_id = fields.Many2one(string='Diario', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='account.journal', )
    log = fields.Text(string='Log', store=True, readonly=True, copy=True, tracking=0, )
    parser = fields.Many2one(string='Parser', readonly=True, tracking=0, comodel_name='account.banking.parser', )


class Impresiónmasiva(models.Model):
    _name = 'credit.control.printer'
    _description = 'Impresión masiva'
    line_ids = fields.Many2many(relation='importbankstatement_line_ids_rel', column1='importbankstatement_id',
                                column2='line_ids_id', string='Líneas de control de crédito', store=True, copy=True,
                                tracking=0,
                                comodel_name='credit.control.line', )
    mark_as_sent = fields.Boolean(string='Marcar líneas de carta como enviadas', store=True, copy=True, tracking=0, )


class Impuestogastos(models.Model):
    _name = 'hr.expense.tax'
    _description = 'Impuesto Gastos'
    account_id = fields.Many2one(string='Cuenta', store=True, copy=True, tracking=0, comodel_name='account.account', )
    amount_base = fields.Float(string='Código base', store=True, copy=True, tracking=0, )
    amount = fields.Float(string='Total', store=True, copy=True, tracking=0, )
    analytic_account_id = fields.Many2one(string='Cuenta analitica', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    base = fields.Float(string='Base', store=True, copy=True, tracking=0, )
    line_id = fields.Many2one(string='Linea', store=True, copy=True, tracking=0, comodel_name='hr.expense.line', )
    manual = fields.Boolean(string='Manual', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Descripción', store=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    taken = fields.Boolean(string='Asumido', store=True, copy=True, tracking=0, )
    tax_amount = fields.Float(string='Impuesto código base', store=True, copy=True, tracking=0, )
    tax_id = fields.Many2one(string='Impuesto', store=True, copy=True, tracking=0, comodel_name='account.tax', )


class Informecontabilidadpruebas(models.Model):
    _name = 'account.financial.report.trial'
    _description = 'Informe Contabilidad Pruebas'
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_end = fields.Date(string='Fecha Fin', store=True, copy=True, tracking=0, )
    date_start = fields.Date(string='Fecha Inicio', store=True, copy=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )


class Informederentabilidaddelproyecto(models.Model):
    _name = 'project.profitability.report'
    _description = 'Informe de rentabilidad del proyecto'
    amount_untaxed_invoiced = fields.Float(string='Base imponible facturada', store=True, readonly=True, copy=True,
                                           tracking=0, )
    amount_untaxed_to_invoice = fields.Float(string='Importe no gravado a la factura', store=True, readonly=True,
                                             copy=True, tracking=0, )
    analytic_account_id = fields.Many2one(string='Cuenta analítica', store=True, readonly=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    company_id = fields.Many2one(string='Compañía del proyecto', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    currency_id = fields.Many2one(string='Divisa del proyecto', store=True, readonly=True, copy=True, tracking=0,
                                  comodel_name='res.currency', )
    expense_amount_untaxed_invoiced = fields.Float(string='Importe no gravado re-facturado', store=True, readonly=True,
                                                   copy=True, tracking=0, )
    expense_amount_untaxed_to_invoice = fields.Float(string='Importe no gravado para volver a facturar', store=True,
                                                     readonly=True, copy=True, tracking=0, )
    expense_cost = fields.Float(string='Otros costos', store=True, readonly=True, copy=True, tracking=0, )
    line_date = fields.Date(string='Fecha', store=True, readonly=True, copy=True, tracking=0, )
    margin = fields.Float(string='Margen', store=True, readonly=True, copy=True, tracking=0, )
    order_confirmation_date = fields.Datetime(string='Fecha de confirmación del pedido de ventas', store=True,
                                              readonly=True, copy=True, tracking=0, )
    other_revenues = fields.Float(string='Otros ingresos', store=True, readonly=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Cliente', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='res.partner', )
    product_id = fields.Many2one(string='Producto', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='product.product', )
    project_id = fields.Many2one(string='Proyecto', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='project.project', )
    sale_line_id = fields.Many2one(string='Línea pedido de venta', store=True, readonly=True, copy=True, tracking=0,
                                   comodel_name='sale.order.line', )
    sale_order_id = fields.Many2one(string='Pedido de venta', store=True, readonly=True, copy=True, tracking=0,
                                    comodel_name='sale.order', )
    timesheet_cost = fields.Float(string='Costo del Parte de Horas', store=True, readonly=True, copy=True,
                                  tracking=0, )
    timesheet_unit_amount = fields.Float(string='Duración del parte de horas', store=True, readonly=True, copy=True,
                                         tracking=0, )
    user_id = fields.Many2one(string='Responsable de proyecto', store=True, readonly=True, copy=True, tracking=0,
                              comodel_name='res.users', )


class Institucionesdeestudiosycapacitaciones(models.Model):
    _name = 'instituciones.estudios.capacitaciones'
    _description = 'Instituciones de Estudios y Capacitaciones'
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    nit = fields.Char(string='NIT', store=True, copy=True, tracking=0, )


class Journal_Entry_Import_Fast(models.Model):
    _name = 'journal.entry.import.fast'
    _description = 'journal_entry_import_fast'
    company_id = fields.Many2one(string='Company', store=True, copy=True, tracking=0, comodel_name='res.company', )
    file = fields.Binary(string='File', store=True, copy=True, tracking=0, )
    force_validate = fields.Boolean(string='Forzar validacion', store=True, copy=True, tracking=0, )


class Justificación(models.Model):
    _name = 'account.commercial.distribution'
    _description = 'Justificación'
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    rate_type_id = fields.Many2one(string='Tarifa servicio', store=True, copy=True, tracking=0,
                                   comodel_name='quoter.rate.type', )


class Justificacionhoraextra(models.Model):
    _name = 'overtime.justification'
    _description = 'Justificacion hora extra'
    name = fields.Char(string='Description', store=True, copy=True, tracking=0, )


class Juzgadocodigoembargo(models.Model):
    _name = 'hr.court.embargoes.code'
    _description = 'Juzgado Codigo Embargo'
    name = fields.Char(string='Codigo del juzgado', store=True, copy=True, tracking=0, )


class Juzgadodestinoembargo(models.Model):
    _name = 'hr.court.embargoes.destination'
    _description = 'Juzgado Destino Embargo'
    name = fields.Char(string='Codigo del juzgado', store=True, copy=True, tracking=0, )


class Juzgadoembargo(models.Model):
    _name = 'hr.court.embargoes'
    _description = 'Juzgado Embargo'
    bank_id = fields.Many2one(string='Banco', store=True, copy=True, tracking=0, comodel_name='res.bank', )
    court_code = fields.Many2one(string='Código del juzgado', store=True, copy=True, tracking=0,
                                 comodel_name='hr.court.embargoes.code', )
    destination_office = fields.Many2one(string='Oficina de destino', store=True, copy=True, tracking=0,
                                         comodel_name='hr.court.embargoes.destination', )
    name = fields.Char(string='Numero de cuenta', store=True, copy=True, tracking=0, )


class Libroauxiliar(models.Model):
    _name = 'account.financial.report.assistant'
    _description = 'Libro Auxiliar'
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_end = fields.Date(string='Fecha Fin', store=True, copy=True, tracking=0, )
    date_start = fields.Date(string='Fecha Inicio', store=True, copy=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )


class Libroauxiliarimpuestos(models.Model):
    _name = 'account.financial.report.taxes'
    _description = 'Libro Auxiliar Impuestos'
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha final', store=True, copy=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Libroauxiliarimpuestoswizard(models.Model):
    _name = 'account.financial.report.taxes.wizard'
    _description = 'Libro Auxiliar Impuestos Wizard'
    account_ids = fields.Many2many(relation='libroauxiliarimpuest_account_ids_rel', column1='libroauxiliarimpuest_id',
                                   column2='account_ids_id', string='Cuentas', store=True, copy=True, tracking=0,
                                   comodel_name='account.account', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inical', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha final', store=True, copy=True, tracking=0, )
    partner_ids = fields.Many2many(relation='libroauxiliarimpuest_partner_ids_rel', column1='libroauxiliarimpuest_id',
                                   column2='partner_ids_id', string='Terceros', store=True, copy=True, tracking=0,
                                   comodel_name='res.partner', )
    structure_id = fields.Many2one(string='Plan Contable', store=True, copy=True, tracking=0,
                                   comodel_name='account.financial.structure', )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Libroauxiliarwizard(models.TransientModel):
    _name = 'account.financial.report.assistant.wizard'
    _description = 'Libro Auxiliar Wizard'

    company_id = fields.Many2one('res.company', string='Compañía', default=lambda self: self.env.company, readonly=True,
                                 copy=False)
    company_ids = fields.Many2many('res.company', relation='afr_asstwiz_company_rel', column1='wizard_id',
                                   column2='company_id', string='Compañías', copy=False)
    domain_company_ids = fields.Many2many('res.company', relation='afr_asstwiz_domain_company_rel', column1='wizard_id',
                                          column2='company_id', string='Compañías para dominio', copy=False)
    date_from = fields.Date(string='Fecha Inicio', copy=False)
    date_to = fields.Date(string='Fecha Fin', copy=False)
    initial_balance = fields.Boolean(string='Incluir saldo inicial', copy=False)
    account_ids = fields.Many2many('account.account', relation='afr_asstwiz_account_rel', column1='wizard_id',
                                   column2='account_id', string='Cuentas', copy=False)
    journal_ids = fields.Many2many('account.journal', relation='afr_asstwiz_journal_rel', column1='wizard_id',
                                   column2='journal_id', string='Diarios', copy=False)
    levels_ids = fields.Many2many('account.financial.levels', relation='afr_asstwiz_level_rel', column1='wizard_id',
                                  column2='level_id', string='Niveles', copy=False)
    partner_ids = fields.Many2many('res.partner', relation='afr_asstwiz_partner_rel', column1='wizard_id',
                                   column2='partner_id', string='Terceros', copy=False)
    structure_id = fields.Many2one('account.financial.structure', string='Plan Contable', copy=False)


class Librodevacaciones(models.Model):
    _name = 'hr.holiday.book'
    _description = 'Libro de vacaciones'
    auxiliar = fields.Float(string='Auxiliar', store=True, copy=True, tracking=0, )
    bold = fields.Boolean(string='Negrita', store=True, copy=True, tracking=0, )
    caused_days = fields.Float(string='Dias causados', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    contract_id = fields.Many2one(string='Contrato', store=True, copy=True, tracking=0, comodel_name='hr.contract', )
    date_end_holidays = fields.Date(string='Fecha final vacaciones', store=True, copy=True, tracking=0, )
    date_end = fields.Date(string='Fecha final', store=True, copy=True, tracking=0, )
    date_paid = fields.Date(string='Fecha de pago', store=True, copy=True, tracking=0, )
    date_return = fields.Date(string='Fecha de regreso', store=True, copy=True, tracking=0, )
    date_start_holidays = fields.Date(string='Fecha inicio vacaciones', store=True, copy=True, tracking=0, )
    date_start = fields.Date(string='Fecha de inicio', store=True, copy=True, tracking=0, )
    days_enjoyed = fields.Float(string='Dias Disfrutados', store=True, copy=True, tracking=0, )
    days_paid = fields.Float(string='Dias pagados', store=True, copy=True, tracking=0, )
    days_suspension = fields.Float(string='Dias Suspendidos', store=True, copy=True, tracking=0, )
    manual = fields.Boolean(string='Manual', store=True, copy=True, tracking=0, )
    payslip_days = fields.Float(string='Dias en Nomina', store=True, copy=True, tracking=0, )
    pending_days = fields.Float(string='Dias pendientes', store=True, copy=True, tracking=0, )
    period_days = fields.Float(string='Dias en Periodo', store=True, copy=True, tracking=0, )
    period_id = fields.Many2one(string='Periodo', store=True, copy=True, tracking=0, comodel_name='hr.period', )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    validated_days = fields.Float(string='Dias validados', store=True, copy=True, tracking=0, )
    worked_days = fields.Float(string='Dias Trabajados', store=True, copy=True, tracking=0, )


class Líneaadicionaldecomunicación(models.Model):
    _name = 'quoter.communication.line.aditional.aux'
    _description = 'Línea Adicional de Comunicación'
    communication_id = fields.Many2one(string='Comunicación', store=True, copy=True, tracking=0,
                                       comodel_name='quoter.communication', )
    depreciation_value = fields.Integer(string='Valor Depreciación', store=True, copy=True, tracking=0, )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.template', )
    quantity = fields.Integer(string='Cantidad', store=True, copy=True, tracking=0, )
    quoter_line_id = fields.Many2one(string='Linea de Cotizacion', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter.line', )
    total_depreciation = fields.Float(string='Total', readonly=True, tracking=0, )


class Líneacanina(models.Model):
    _name = 'quoter.canine.line.aux'
    _description = 'Línea canina'
    canine_id = fields.Many2one(string='Arma', store=True, copy=True, tracking=0, comodel_name='quoter.canine', )
    depreciation_value = fields.Integer(string='Valor Depreciación', store=True, copy=True, tracking=0, )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.template', )
    quoter_line_id = fields.Many2one(string='Linea de Cotizacion', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter.line', )
    total_depreciation = fields.Float(string='Total', readonly=True, tracking=0, )


class LineaCanica(models.Model):
    _name = 'quoter.canine.line'
    _description = 'Línea canina'
    canine_id = fields.Many2one(string='Arma', store=True, copy=True, tracking=0, comodel_name='quoter.canine', )
    depreciation_value = fields.Integer(string='Valor Depreciación', store=True, copy=True, tracking=0, )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.template', )
    total_depreciation = fields.Float(string='Total', readonly=True, tracking=0, )


class Líneadeamortizacióndelactivo(models.Model):
    _name = 'account.asset.line'
    _description = 'Línea de amortización del activo'
    amount = fields.Float(string='Importe', store=True, required=True, copy=True, tracking=0, )
    asset_id = fields.Many2one(string='Activo', store=True, required=True, copy=True, tracking=0,
                               comodel_name='account.asset', )
    depreciated_value = fields.Float(string='Importe ya amortizado', store=True, readonly=True, tracking=0, )
    depreciation_base = fields.Float(string='Base Amortización', readonly=True, tracking=0, )
    init_entry = fields.Boolean(string='Asiento de saldo inicial', store=True, copy=True, tracking=0, )
    line_date = fields.Date(string='Fecha', store=True, required=True, copy=True, tracking=0, )
    line_days = fields.Integer(string='Dias', store=True, readonly=True, copy=True, tracking=0, )
    move_check = fields.Boolean(string='Asentado', store=True, readonly=True, tracking=0, )
    move_id = fields.Many2one(string='Asiento de amortización', store=True, readonly=True, copy=True, tracking=0,
                              comodel_name='account.move', )
    name = fields.Char(string='Nombre de la amortización', store=True, readonly=True, copy=True, tracking=0, )
    previous_id = fields.Many2one(string='Línea de amortización previa', store=True, readonly=True, copy=True,
                                  tracking=0,
                                  comodel_name='account.asset.line', )
    remaining_value = fields.Float(string='Amortización del siguiente período', store=True, readonly=True, tracking=0, )


class LineadeAmortizaciondelActivo(models.Model):
    _name = 'account.asset.line.niff'
    _description = 'Línea de amortización del activo'
    amount = fields.Float(string='Amount', store=True, required=True, copy=True, tracking=0, )
    asset_id = fields.Many2one(string='Activo', store=True, required=True, copy=True, tracking=0,
                               comodel_name='account.asset', )
    depreciated_value = fields.Float(string='Amount Already Depreciated', store=True, readonly=True, tracking=0, )
    depreciation_base = fields.Float(string='Depreciation Base', store=True, readonly=True, copy=True, tracking=0, )
    hide_button = fields.Boolean(string='Hide Button', readonly=True, tracking=0, )
    init_entry = fields.Boolean(string='Initial Balance Entry', store=True, copy=True, tracking=0, )
    line_date = fields.Date(string='Date', store=True, required=True, copy=True, tracking=0, )
    line_days = fields.Integer(string='Days', store=True, readonly=True, copy=True, tracking=0, )
    move_check = fields.Boolean(string='Posted', store=True, readonly=True, tracking=0, )
    move_id = fields.Many2one(string='Depreciation Entry', store=True, readonly=True, copy=True, tracking=0,
                              comodel_name='account.move', )
    name = fields.Char(string='Depreciation Name', store=True, readonly=True, copy=True, tracking=0, )
    previous_id = fields.Many2one(string='Previous Depreciation Line', store=True, readonly=True, copy=True,
                                  tracking=0,
                                  comodel_name='account.asset.line.niff', )
    remaining_value = fields.Float(string='Next Period Depreciation', store=True, readonly=True, tracking=0, )


class Líneadearma(models.Model):
    _name = 'quoter.weapon.type.line.aux'
    _description = 'Línea de arma'
    depreciation_value = fields.Integer(string='Valor Depreciación', store=True, copy=True, tracking=0, )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.template', )
    quoter_line_id = fields.Many2one(string='quoter_line', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter.line', )
    total_depreciation = fields.Float(string='Total', readonly=True, tracking=0, )
    weapon_type_id = fields.Many2one(string='Arma', store=True, copy=True, tracking=0,
                                     comodel_name='quoter.weapon.type', )


class LineadeArma(models.Model):
    _name = 'quoter.weapon.type.line'
    _description = 'Línea de arma'
    depreciation_value = fields.Integer(string='Valor Depreciación', store=True, copy=True, tracking=0, )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.template', )
    total_depreciation = fields.Float(string='Total', readonly=True, tracking=0, )
    weapon_type_id = fields.Many2one(string='Arma', store=True, copy=True, tracking=0,
                                     comodel_name='quoter.weapon.type', )


class Líneadecomunicación(models.Model):
    _name = 'quoter.communication.line'
    _description = 'Línea de Comunicación'
    communication_id = fields.Many2one(string='Comunicación', store=True, copy=True, tracking=0,
                                       comodel_name='quoter.communication', )
    depreciation_value = fields.Integer(string='Valor Depreciación', store=True, copy=True, tracking=0, )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.template', )
    quantity = fields.Integer(string='Cantidad', store=True, copy=True, tracking=0, )
    total_depreciation = fields.Float(string='Total', readonly=True, tracking=0, )


class LineaComunicacion(models.Model):
    _name = 'quoter.communication.line.aux'
    _description = 'Línea de Comunicación'
    communication_id = fields.Many2one(string='Comunicación', store=True, copy=True, tracking=0,
                                       comodel_name='quoter.communication', )
    depreciation_value = fields.Integer(string='Valor Depreciación', store=True, copy=True, tracking=0, )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.template', )
    quantity = fields.Integer(string='Cantidad', store=True, copy=True, tracking=0, )
    quoter_line_id = fields.Many2one(string='Linea de Cotizacion', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter.line', )
    total_depreciation = fields.Float(string='Total', readonly=True, tracking=0, )


class Líneadecosteendestino(models.Model):
    _name = 'stock.landed.cost.lines'
    _description = 'Línea de coste en destino'
    account_id = fields.Many2one(string='Cuenta', store=True, copy=True, tracking=0, comodel_name='account.account', )
    cost_id = fields.Many2one(string='Costo en Destino', store=True, required=True, copy=True, tracking=0,
                              comodel_name='stock.landed.cost', )
    currency_id = fields.Many2one(string='Moneda', readonly=True, tracking=0, comodel_name='res.currency', )
    name = fields.Char(string='Descripción', store=True, copy=True, tracking=0, )
    price_unit = fields.Monetary(string='Costo', store=True, required=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='product.product', )


class Líneadecuentadetiempodeticket(models.Model):
    _name = 'ticket.time.account.line'
    _description = 'Línea de cuenta de tiempo de ticket'
    company_id = fields.Many2one(string='Compañía', store=True, copy=True, tracking=0, comodel_name='res.company', )
    duration = fields.Float(string='Duración (HH: MM)', store=True, readonly=True, copy=True, tracking=0, )
    end_date = fields.Datetime(string='Fecha final', store=True, readonly=True, copy=True, tracking=0, )
    name = fields.Text(string='Descripción', store=True, required=True, copy=True, tracking=0, )
    project_id = fields.Many2one(string='Proyecto', store=True, copy=True, tracking=0,
                                 comodel_name='project.project', )
    start_date = fields.Datetime(string='Fecha de inicio', store=True, readonly=True, copy=True, tracking=0, )


class Lineadedotacion(models.Model):
    _name = 'quoter.dotation.line.aux'
    _description = 'Línea de Dotación'
    dotation_id = fields.Many2one(string='dotacion', store=True, copy=True, tracking=0,
                                  comodel_name='quoter.dotation', )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.template', )
    qty = fields.Integer(string='Cantidad', store=True, copy=True, tracking=0, )
    quoter_line_id = fields.Many2one(string='quoter_line', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter.line', )
    total_price = fields.Float(string='Total', readonly=True, tracking=0, )


class Lineadedotacion(models.Model):
    _name = 'quoter.dotation.line'
    _description = 'Línea de Dotación'
    dotation_id = fields.Many2one(string='dotacion', store=True, copy=True, tracking=0,
                                  comodel_name='quoter.dotation', )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.template', )
    qty = fields.Integer(string='Cantidad', store=True, copy=True, tracking=0, )
    quoter_line_id = fields.Many2one(string='quoter_line', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter.line', )
    total_price = fields.Float(string='Total', readonly=True, tracking=0, )


class Lineadedotacionadicional(models.Model):
    _name = 'quoter.additional.dotation.line'
    _description = 'Línea de Dotación Adicional'
    dotation_id = fields.Many2one(string='dotación adicional', store=True, copy=True, tracking=0,
                                  comodel_name='quoter.additional.dotation', )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.template', )
    qty = fields.Integer(string='Cantidad', store=True, copy=True, tracking=0, )
    quoter_line_id = fields.Many2one(string='quoter_line', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter.line', )
    total_price = fields.Float(string='Total', readonly=True, tracking=0, )


class Lineadedotacionadicionalaux(models.Model):
    _name = 'quoter.additional.dotation.line.aux'
    _description = 'Linea de Dotación Adicional Aux'
    dotation_id = fields.Many2one(string='dotación adicional', store=True, copy=True, tracking=0,
                                  comodel_name='quoter.additional.dotation', )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.template', )
    qty = fields.Integer(string='Cantidad', store=True, copy=True, tracking=0, )
    quoter_line_id = fields.Many2one(string='quoter_line', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter.line', )
    total_price = fields.Float(string='Total', readonly=True, tracking=0, )


class Lineadeentrenamiento(models.Model):
    _name = 'quoter.training.line'
    _description = 'Línea de entrenamiento'
    course = fields.Float(string='Curso', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    people = fields.Integer(string='Personas', store=True, copy=True, tracking=0, )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    training_id = fields.Many2one(string='entrenamiento', store=True, copy=True, tracking=0,
                                  comodel_name='quoter.training', )


class Lineadeguiadeentrega(models.Model):
    _name = 'delivery.guide.line'
    _description = 'Linea de Guia de Entrega'
    account_amount_total_signed = fields.Monetary(string='Total con signo', readonly=True, tracking=0, )
    account_date = fields.Date(string='Fecha de Factura/Recibo', readonly=True, tracking=0, )
    account_delivery_bool = fields.Boolean(string='Tiene Novedad', store=True, copy=True, tracking=0, )
    account_id = fields.Many2one(string='Factura', store=True, copy=True, tracking=0, comodel_name='account.move', )
    account_name = fields.Char(string='Número', readonly=True, tracking=0, )
    account_partner_id = fields.Many2one(string='Asociado', readonly=True, tracking=0, comodel_name='res.partner', )
    company_id = fields.Many2one(string='Compañia', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    currency_id = fields.Many2one(string='Moneda', readonly=True, tracking=0, comodel_name='res.currency', )
    guide_account_invoice_id = fields.Many2one(string='Guía Factura', store=True, copy=True, tracking=0,
                                               comodel_name='delivery.guide', )
    guide_account_refund_id = fields.Many2one(string='Guia Devuelta', store=True, copy=True, tracking=0,
                                              comodel_name='delivery.guide', )
    guide_stock_invoice_id = fields.Many2one(string='Movimiento Guía Factura', store=True, copy=True, tracking=0,
                                             comodel_name='delivery.guide', )
    guide_stock_refund_id = fields.Many2one(string='Movimientos Guía Devuelta', store=True, copy=True, tracking=0,
                                            comodel_name='delivery.guide', )
    stock_date = fields.Datetime(string='Fecha programada', readonly=True, tracking=0, )
    stock_id = fields.Many2one(string='Movimiento Facturado', store=True, copy=True, tracking=0,
                               comodel_name='stock.move', )
    stock_picking_id = fields.Many2one(string='Transferir', readonly=True, tracking=0, comodel_name='stock.picking', )
    stock_product_id = fields.Many2one(string='Producto', readonly=True, tracking=0, comodel_name='product.product', )
    stock_product_qty = fields.Float(string='Cantidad', store=True, copy=True, tracking=0, )
    stock_product_uom_qty = fields.Float(string='Demanda', store=True, copy=True, tracking=0, )
    stock_uom_id = fields.Many2one(string='Unidad de Medida', readonly=True, tracking=0, comodel_name='uom.uom', )
    stock_weight = fields.Float(string='Peso movimiento', store=True, readonly=True, tracking=0, )


class Lineadenegocio(models.Model):
    _name = 'project.linea.negocio'
    _description = 'Linea de negocio'
    commercial_distribution_ids = fields.Many2many(relation='lineadenegocio_commercial_distribut_rel',
                                                   column1='lineadenegocio_id', column2='commercial_distribut_id',
                                                   string='Unidad de negocio', store=True, copy=True, tracking=0,
                                                   comodel_name='account.commercial.distribution', )
    name = fields.Char(string='Linea de negocio', store=True, copy=True, tracking=0, )


class Lineadenómina(models.Model):
    _name = 'hr.payslip.line'
    _description = 'Linea de Nómina'
    afc = fields.Boolean(string='AFC', store=True, copy=True, tracking=0, )
    concept_id = fields.Many2one(string='Concepto', store=True, copy=True, tracking=0, comodel_name='hr.concept', )
    contract_prod_lec = fields.Float(string='Lectivo', store=True, copy=True, tracking=0, )
    contract_prod_prod = fields.Float(string='Productiva', store=True, copy=True, tracking=0, )
    embargo_id = fields.Many2one(string='Embargo', store=True, copy=True, tracking=0,
                                 comodel_name='hr.payroll.embargo', )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    ex_rent = fields.Boolean(string='Exento de renta', store=True, copy=True, tracking=0, )
    leave_id = fields.Many2one(string='Ausencia', store=True, copy=True, tracking=0, comodel_name='hr.leave', )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    novelty_id = fields.Many2one(string='Novedad', store=True, copy=True, tracking=0, comodel_name='hr.novelty', )
    overtime_id = fields.Many2one(string='Hora Extra', store=True, copy=True, tracking=0,
                                  comodel_name='hr.overtime', )
    partner_id = fields.Many2one(string='Tercero', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    payslip_id = fields.Many2one(string='Nómina', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='hr.payslip', )
    payslip_processing_id = fields.Many2one(string='Procesamiento de Nomina', store=True, copy=True, tracking=0,
                                            comodel_name='hr.payslip.processing', )
    qty = fields.Float(string='Cantidad', store=True, copy=True, tracking=0, )
    rate = fields.Float(string='Porcentaje', store=True, copy=True, tracking=0, )
    total = fields.Float(string='Total', store=True, copy=True, tracking=0, )
    value_overtime = fields.Float(string='Cantidad Hora Extra', store=True, copy=True, tracking=0, )
    value = fields.Float(string='Valor', store=True, copy=True, tracking=0, )


class Lineadeobligacionfinanciera(models.Model):
    _name = 'loan.move.line'
    _description = 'Linea de Obligacion Financiera'
    bank_charges = fields.Float(string='Gastos bancarios', store=True, readonly=True, copy=True, tracking=0, )
    capital_payment = fields.Float(string='Pago a capital', store=True, readonly=True, copy=True, tracking=0, )
    core_adjust = fields.Float(string='Ajuste de cuotas', store=True, readonly=True, copy=True, tracking=0, )
    cote = fields.Float(string='Cuota', readonly=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, readonly=True, required=True, copy=True, tracking=0, )
    final_bal = fields.Float(string='Saldo final', readonly=True, tracking=0, )
    initial_value = fields.Float(string='Saldo inicial', store=True, readonly=True, copy=True, tracking=0, )
    interest = fields.Float(string='Intereses corrientes', store=True, readonly=True, copy=True, tracking=0, )
    loan_id = fields.Many2one(string='Loan', store=True, copy=True, tracking=0, comodel_name='account.loan', )
    move_id = fields.Many2one(string='Comprobante Contable', store=True, readonly=True, copy=True, tracking=0,
                              comodel_name='account.move', )
    move_name = fields.Char(string='Nombre Comprobante', store=True, readonly=True, copy=True, tracking=0, )
    paid = fields.Boolean(string='Pagado', readonly=True, tracking=0, )
    payment = fields.Float(string='Desembolso', store=True, readonly=True, copy=True, tracking=0, )
    penality_interest = fields.Float(string='Interes de mora', store=True, readonly=True, copy=True, tracking=0, )
    period = fields.Integer(string='Periodo', store=True, readonly=True, copy=True, tracking=0, )
    prepaid_id = fields.Many2one(string='Prepago/Desembolso', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='account.loan.prepaid', )
    total_payment = fields.Float(string='Pago Total', readonly=True, tracking=0, )
    val_to_capital = fields.Float(string='Abono extra a capital', store=True, readonly=True, copy=True, tracking=0, )


class Líneadepolíticadecotización(models.Model):
    _name = 'quoter.policy.line'
    _description = 'Línea de Política de Cotización'
    name = fields.Char(string='Garantias', store=True, copy=True, tracking=0, )
    percentege = fields.Float(string='%', store=True, copy=True, tracking=0, )
    premium_insurer = fields.Float(string='Aseguradora Prima', readonly=True, tracking=0, )
    rate_insurer = fields.Float(string='Aseguradora Tasa', store=True, copy=True, tracking=0, )
    sale_quoter_id = fields.Many2one(string='sale_quoter', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter', )
    term_days = fields.Integer(string='Plazo días', readonly=True, tracking=0, )
    validity_since = fields.Date(string='Vigencia desde', store=True, copy=True, tracking=0, )
    validity_until = fields.Date(string='Vigencia hasta', store=True, copy=True, tracking=0, )
    value_guarantees = fields.Float(string='Valor Garantias', readonly=True, tracking=0, )


class Líneadeposiciónadicionaldedotación(models.Model):
    _name = 'quoter.dotation.additional.position.line.aux'
    _description = 'Línea de Posición Adicional de Dotación'
    dotation_additional_position_id = fields.Many2one(string='dotacion', store=True, copy=True, tracking=0,
                                                      comodel_name='quoter.dotation.additional.position', )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.template', )
    qty = fields.Integer(string='Cantidad', store=True, copy=True, tracking=0, )
    quoter_line_id = fields.Many2one(string='Sale quoter line', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter.line', )
    total_price = fields.Float(string='Total', readonly=True, tracking=0, )


class LineadePosicionAdicionaldeDotación(models.Model):
    _name = 'quoter.dotation.additional.position.line'
    _description = 'Línea de Posición Adicional de Dotación'
    dotation_additional_position_id = fields.Many2one(string='dotacion', store=True, copy=True, tracking=0,
                                                      comodel_name='quoter.dotation.additional.position', )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.template', )
    qty = fields.Integer(string='Cantidad', store=True, copy=True, tracking=0, )
    quoter_line_id = fields.Many2one(string='Sale quoter line', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter.line', )
    total_price = fields.Float(string='Total', readonly=True, tracking=0, )


class Líneadeposicióndedotación(models.Model):
    _name = 'quoter.dotation.position.line'
    _description = 'Línea de posición de dotación'
    dotation_position_id = fields.Many2one(string='dotacion', store=True, copy=True, tracking=0,
                                           comodel_name='quoter.dotation.position', )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.template', )
    qty = fields.Integer(string='Cantidad', store=True, copy=True, tracking=0, )
    quoter_line_id = fields.Many2one(string='Sale quoter line', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter.line', )
    total_price = fields.Float(string='Total', readonly=True, tracking=0, )


class Líneadeposicióndedotaciónaux(models.Model):
    _name = 'quoter.dotation.position.line.aux'
    _description = 'Línea de posición de dotación aux'
    dotation_position_id = fields.Many2one(string='dotacion', store=True, copy=True, tracking=0,
                                           comodel_name='quoter.dotation.position', )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.template', )
    qty = fields.Integer(string='Cantidad', store=True, copy=True, tracking=0, )
    quoter_line_id = fields.Many2one(string='Sale quoter line', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter.line', )
    total_price = fields.Float(string='Total', readonly=True, tracking=0, )


class Líneadepresupuesto(models.Model):
    _name = 'crossovered.budget.lines'
    _description = 'Línea de Presupuesto'
    analytic_account_id = fields.Many2one(string='Cuenta Analítica', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    company_id = fields.Many2one(string='Compañía', store=True, readonly=True, tracking=0, comodel_name='res.company', )
    crossovered_budget_id = fields.Many2one(string='Presupuesto', index=True, store=True, required=True, copy=True,
                                            tracking=0, comodel_name='crossovered.budget', )
    date_from = fields.Date(string='Fecha de inicio', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    general_budget_id = fields.Many2one(string='Posición Presupuestaria', store=True, required=True, copy=True,
                                        tracking=0, comodel_name='account.budget.post', )
    paid_date = fields.Date(string='Fecha Pago', store=True, copy=True, tracking=0, )
    percentage = fields.Float(string='Logro', readonly=True, tracking=0, )
    planned_amount = fields.Float(string='Importe Planificado', store=True, required=True, copy=True, tracking=0, )
    practical_amount = fields.Float(string='Importe Real', store=True, readonly=True, tracking=0, )
    project_service_order_id = fields.Many2one(string='Orden de servicio', store=True, copy=True, tracking=0,
                                               comodel_name='project.service.order', )
    theoretical_amount = fields.Float(string='Importe teórico', readonly=True, tracking=0, )


class Lineadeprogramacion(models.Model):
    _name = 'hr.roster.programacion.line'
    _description = 'Linea de Programacion'
    adicional = fields.Boolean(string='Core de programacion', store=True, copy=True, tracking=0, )
    analytic_account_id = fields.Many2one(string='Cuenta analitica', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    code_position = fields.Char(string='Puesto', store=True, readonly=True, tracking=0, )
    company_id = fields.Many2one(string='Compañía', copy=True, tracking=0, comodel_name='res.company', )
    concat_contract = fields.Char(string='Personal', store=True, readonly=True, tracking=0, )
    concat_name = fields.Char(string='Info Puesto', store=True, readonly=True, tracking=0, )
    contract_group = fields.Many2one(string='Grupo de contrato', store=True, copy=True, tracking=0,
                                     comodel_name='hr.contract.group', )
    day_1 = fields.Many2one(string='1', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_10 = fields.Many2one(string='10', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_11 = fields.Many2one(string='11', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_12 = fields.Many2one(string='12', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_13 = fields.Many2one(string='13', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_14 = fields.Many2one(string='14', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_15 = fields.Many2one(string='15', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_16 = fields.Many2one(string='16', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_17 = fields.Many2one(string='17', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_18 = fields.Many2one(string='18', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_19 = fields.Many2one(string='19', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_2 = fields.Many2one(string='2', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_20 = fields.Many2one(string='20', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_21 = fields.Many2one(string='21', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_22 = fields.Many2one(string='22', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_23 = fields.Many2one(string='23', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_24 = fields.Many2one(string='24', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_25 = fields.Many2one(string='25', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_26 = fields.Many2one(string='26', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_27 = fields.Many2one(string='27', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_28 = fields.Many2one(string='28', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_29 = fields.Many2one(string='29', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_3 = fields.Many2one(string='3', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_30 = fields.Many2one(string='30', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_31 = fields.Many2one(string='31', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_4 = fields.Many2one(string='4', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_5 = fields.Many2one(string='5', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_6 = fields.Many2one(string='6', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_7 = fields.Many2one(string='7', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_8 = fields.Many2one(string='8', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    day_9 = fields.Many2one(string='9', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    days = fields.Integer(string='Dias', readonly=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    is_select_wizard = fields.Boolean(string='Check', store=True, copy=True, tracking=0, )
    line_with_comodin = fields.Boolean(string='Linea con comodin', store=True, copy=True, tracking=0, )
    modalidad_id = fields.Many2one(string='Modalidad Patron', store=True, copy=True, tracking=0,
                                   comodel_name='hr.roster.modalidad', )
    modalidad_patron_id = fields.Many2one(string='Modalidad', store=True, copy=True, tracking=0,
                                          comodel_name='hr.roster.modalidad', )
    parent_modality_id = fields.Many2one(string='Modalidad Padre', store=True, copy=True, tracking=0,
                                         comodel_name='hr.roster.modalidad', )
    personal_ausente = fields.Many2one(string='Personal Ausente', store=True, copy=True, tracking=0,
                                       comodel_name='hr.employee', )
    programacion_id = fields.Many2one(string='Programacion', store=True, copy=True, tracking=0,
                                      comodel_name='hr.roster.programacion', )
    programacion_year = fields.Integer(string='Ano', readonly=True, tracking=0, )
    programador_id = fields.Many2one(string='Programador', store=True, readonly=True, tracking=0,
                                     comodel_name='hr.employee', )
    programation_name = fields.Char(string='Nombre de la programación', store=True, readonly=True, tracking=0, )
    programer_aux = fields.Many2one(string='Programador Auxiliar', readonly=True, tracking=0,
                                    comodel_name='hr.employee', )
    project_id = fields.Many2one(string='Proyecto', store=True, readonly=True, tracking=0,
                                 comodel_name='project.project', )
    proyecto_id = fields.Many2one(string='Proyecto', store=True, readonly=True, tracking=0,
                                  comodel_name='project.project', )
    puesto_id = fields.Many2one(string='Centro de Costo', store=True, copy=True, tracking=0,
                                comodel_name='hr.roster.puesto', )
    relevante = fields.Boolean(string='R', store=True, copy=True, tracking=0, )
    responsable_id = fields.Many2one(string='Encargado', store=True, readonly=True, tracking=0,
                                     comodel_name='hr.employee', )
    seq_index = fields.Integer(string='Indice de secuencia', store=True, copy=True, tracking=0, )
    t_1 = fields.Many2one(string='1', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_10 = fields.Many2one(string='10', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_11 = fields.Many2one(string='11', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_12 = fields.Many2one(string='12', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_13 = fields.Many2one(string='13', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_14 = fields.Many2one(string='14', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_15 = fields.Many2one(string='15', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_16 = fields.Many2one(string='16', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_17 = fields.Many2one(string='17', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_18 = fields.Many2one(string='18', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_19 = fields.Many2one(string='19', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_2 = fields.Many2one(string='2', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_20 = fields.Many2one(string='20', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_21 = fields.Many2one(string='21', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_22 = fields.Many2one(string='22', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_23 = fields.Many2one(string='23', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_24 = fields.Many2one(string='24', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_25 = fields.Many2one(string='25', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_26 = fields.Many2one(string='26', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_27 = fields.Many2one(string='27', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_28 = fields.Many2one(string='28', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_29 = fields.Many2one(string='29', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_3 = fields.Many2one(string='3', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_30 = fields.Many2one(string='30', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_31 = fields.Many2one(string='31', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_4 = fields.Many2one(string='4', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_5 = fields.Many2one(string='5', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_6 = fields.Many2one(string='6', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_7 = fields.Many2one(string='7', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_8 = fields.Many2one(string='8', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    t_9 = fields.Many2one(string='9', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    use_parent_modality = fields.Boolean(string='Usa modalidad padre', readonly=True, tracking=0, )
    x_puesto_corto = fields.Char(string='Puesto Corto', store=True, tracking=1, )
    x_regional_id = fields.Many2one(string='Regional', store=True, tracking=1, comodel_name='res.regional', )
    x_sede = fields.Char(string='Sede', store=True, tracking=1, )
    x_vencimiento_contracto = fields.Date(string='Vencimiento Contrato', readonly=True, tracking=0, )
    year = fields.Integer(string='Año', store=True, readonly=True, tracking=0, )


class Líneadeproteccióndedotación(models.Model):
    _name = 'quoter.dotation.protection.line'
    _description = 'Línea de protección de dotación'
    dotation_protection_id = fields.Many2one(string='dotacion', store=True, copy=True, tracking=0,
                                             comodel_name='quoter.dotation.protection', )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.template', )
    qty = fields.Integer(string='Cantidad', store=True, copy=True, tracking=0, )
    quoter_line_id = fields.Many2one(string='Sale quoter line', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter.line', )
    total_price = fields.Float(string='Total', readonly=True, tracking=0, )


class Líneadeproteccióndedotaciónaux(models.Model):
    _name = 'quoter.dotation.protection.line.aux'
    _description = 'Línea de protección de dotación aux'
    dotation_protection_id = fields.Many2one(string='dotacion', store=True, copy=True, tracking=0,
                                             comodel_name='quoter.dotation.protection', )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.template', )
    qty = fields.Integer(string='Cantidad', store=True, copy=True, tracking=0, )
    quoter_line_id = fields.Many2one(string='Sale quoter line', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter.line', )
    total_price = fields.Float(string='Total', readonly=True, tracking=0, )


class Lineadereportenomina(models.Model):
    _name = 'hr.payslip.line.report'
    _description = 'Linea de Reporte Nomina'
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    concept_id = fields.Many2one(string='Concepto', store=True, copy=True, tracking=0, comodel_name='hr.concept', )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    leave_id = fields.Many2one(string='Ausencia', store=True, copy=True, tracking=0, comodel_name='hr.leave', )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    novelty_id = fields.Many2one(string='Novedad', store=True, copy=True, tracking=0, comodel_name='hr.novelty', )
    overtime_id = fields.Many2one(string='Hora Extra', store=True, copy=True, tracking=0,
                                  comodel_name='hr.overtime', )
    partner_id = fields.Many2one(string='Tercero', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    payslip_id = fields.Many2one(string='Nomina', store=True, copy=True, tracking=0, comodel_name='hr.payslip', )
    payslip_processing_id = fields.Many2one(string='Procesamiento de Nómina', store=True, copy=True, tracking=0,
                                            comodel_name='hr.payslip.processing', )
    qty = fields.Float(string='Cantidad', store=True, copy=True, tracking=0, )
    rate = fields.Float(string='Porcentaje', store=True, copy=True, tracking=0, )
    total = fields.Float(string='Total', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )
    value = fields.Float(string='Valor', store=True, copy=True, tracking=0, )


class Lineadereportenominawizard(models.Model):
    _name = 'hr.payslip.line.report.wizard'
    _description = 'Linea de Reporte Nomina Wizard'
    period_id = fields.Many2one(string='Periodo', store=True, copy=True, tracking=0, comodel_name='hr.period', )


class Líneaderequerimientodecompra(models.Model):
    _name = 'purchase.requisition.line'
    _description = 'Línea de Requerimiento de Compra'
    account_analytic_id = fields.Many2one(string='Cuenta Analítica', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    analytic_tag_ids = fields.Many2many(relation='lineadereportenomina_analytic_tag_ids_rel',
                                        column1='lineadereportenomina_id', column2='analytic_tag_ids_id',
                                        string='Etiquetas analíticas', store=True, copy=True, tracking=0,
                                        comodel_name='account.analytic.tag', )
    company_id = fields.Many2one(string='Compañía', store=True, readonly=True, tracking=0, comodel_name='res.company', )
    move_dest_id = fields.Many2one(string='Movimiento de salida', store=True, copy=True, tracking=0,
                                   comodel_name='stock.move', )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_description_variants = fields.Char(string='Descripción personalizada', store=True, copy=True,
                                               tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='product.product', )
    product_qty = fields.Float(string='Cantidad', store=True, copy=True, tracking=0, )
    product_uom_category_id = fields.Many2one(string='Categoría', readonly=True, tracking=0,
                                              comodel_name='uom.category', )
    product_uom_id = fields.Many2one(string='Unidad de Medida del Producto', store=True, copy=True, tracking=0,
                                     comodel_name='uom.uom', )
    qty_ordered = fields.Float(string='Cantidades pedidas', readonly=True, tracking=0, )
    recoup = fields.Boolean(string='Recobro', store=True, copy=True, tracking=0, )
    requisition_id = fields.Many2one(string='Acuerdos de compra', store=True, required=True, copy=True, tracking=0,
                                     comodel_name='purchase.requisition', )
    schedule_date = fields.Date(string='Fecha Programada', store=True, copy=True, tracking=0, )


class Líneadesoporte(models.Model):
    _name = 'quoter.support.line'
    _description = 'Línea de Soporte'
    depreciation_value = fields.Integer(string='Valor Depreciación', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    support_id = fields.Many2one(string='dotacion', store=True, copy=True, tracking=0,
                                 comodel_name='quoter.support', )
    total_depreciation = fields.Float(string='Total', readonly=True, tracking=0, )


class Líneadesoporteaux(models.Model):
    _name = 'quoter.support.line.aux'
    _description = 'Línea de Soporte Aux'
    depreciation_value = fields.Integer(string='Valor Depreciación', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    quoter_line_id = fields.Many2one(string='Linea de Cotizacion', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter.line', )
    support_id = fields.Many2one(string='dotacion', store=True, copy=True, tracking=0,
                                 comodel_name='quoter.support', )
    total_depreciation = fields.Float(string='Total', readonly=True, tracking=0, )


class Líneadevariableeconómica(models.Model):
    _name = 'economic.variable.line'
    _description = 'Línea de variable económica'
    compute_value = fields.Boolean(string='Valor calculado', readonly=True, tracking=0, )
    value = fields.Float(string='Valor', store=True, copy=True, tracking=0, )
    variable_id = fields.Many2one(string='Variable económica', store=True, copy=True, tracking=0,
                                  comodel_name='economic.variable', )


class LíneadeventasdeproyectosMapeodeempleados(models.Model):
    _name = 'project.sale.line.employee.map'
    _description = 'Línea de ventas de proyectos, mapeo de empleados'
    company_id = fields.Many2one(string='Compañía', readonly=True, tracking=0, comodel_name='res.company', )
    currency_id = fields.Many2one(string='Moneda', store=True, copy=True, tracking=0, comodel_name='res.currency', )
    employee_id = fields.Many2one(string='Empleado', store=True, required=True, copy=True, tracking=0,
                                  comodel_name='hr.employee', )
    price_unit = fields.Float(string='Precio Unitario', store=True, readonly=True, tracking=0, )
    project_id = fields.Many2one(string='Proyecto', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='project.project', )
    sale_line_id = fields.Many2one(string='Elemento del pedido de venta', store=True, copy=True, tracking=0,
                                   comodel_name='sale.order.line', )
    timesheet_product_id = fields.Many2one(string='Servicio', store=True, copy=True, tracking=0,
                                           comodel_name='product.product', )


class Lineasaccionesdisciplinarias(models.Model):
    _name = 'hr.employee.disciplinary.action.line'
    _description = 'Lineas Acciones disciplinarias'
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Lineasagrupadasdefactura(models.Model):
    _name = 'account.move.line.print'
    _description = 'Lineas agrupadas de factura'
    invoice_id = fields.Many2one(string='Factura', store=True, copy=True, tracking=0, comodel_name='account.move', )
    name = fields.Char(string='Descripcion', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.product', )
    quantity = fields.Integer(string='Cantidad', store=True, copy=True, tracking=0, )
    total = fields.Float(string='Monto total', store=True, copy=True, tracking=0, )


class Lineasbalancedepruebas(models.Model):
    _name = 'account.financial.report.balance.line'
    _description = 'Lineas Balance de Pruebas'
    account_id = fields.Many2one(string='Cuenta', store=True, copy=True, tracking=0, comodel_name='account.account', )
    amount_final = fields.Float(string='Saldo Final', store=True, copy=True, tracking=0, )
    amount_initial = fields.Float(string='Saldo Inicial', store=True, copy=True, tracking=0, )
    bold = fields.Boolean(string='Negrilla', store=True, copy=True, tracking=0, )
    code = fields.Char(string='Code', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Company', store=True, copy=True, tracking=0, comodel_name='res.company', )
    credit = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    ifrs_group_id = fields.Many2one(string='IFRS Group', store=True, copy=True, tracking=0,
                                    comodel_name='account.group', )
    journal_id = fields.Many2one(string='Diario', store=True, copy=True, tracking=0, comodel_name='account.journal', )
    level = fields.Integer(string='Nivel', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre Cuenta', store=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Tercero', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    period_move = fields.Float(string='Movimiento de Periodo', store=True, copy=True, tracking=0, )
    report_balance_id = fields.Many2one(string='Informe', store=True, copy=True, tracking=0,
                                        comodel_name='account.financial.report.balance', )


class Lineasbalancederesultados(models.Model):
    _name = 'account.financial.report.state.income.line'
    _description = 'Lineas Balance de Resultados'
    account_id = fields.Many2one(string='Cuenta', store=True, copy=True, tracking=0, comodel_name='account.account', )
    amount = fields.Float(string='Saldo Final', store=True, copy=True, tracking=0, )
    bold = fields.Boolean(string='Negrilla', store=True, copy=True, tracking=0, )
    code = fields.Char(string='Code', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Company', store=True, copy=True, tracking=0, comodel_name='res.company', )
    container_group_id = fields.Many2one(string='Container Group', store=True, copy=True, tracking=0,
                                         comodel_name='account.container.group', )
    credit = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    group_id = fields.Many2one(string='Group', store=True, copy=True, tracking=0, comodel_name='account.group', )
    has_value = fields.Boolean(string='Tiene Valor', store=True, copy=True, tracking=0, )
    is_total = fields.Boolean(string='Es Total', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre Cuenta', store=True, copy=True, tracking=0, )
    report_balance_id = fields.Many2one(string='Informe', store=True, copy=True, tracking=0,
                                        comodel_name='account.financial.report.state.income', )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    signo_en_reporte = fields.Char(string='Signo en Reporte', store=True, copy=True, tracking=0, )


class Lineasbalancegeneral(models.Model):
    _name = 'account.financial.report.balance.general.line'
    _description = 'Lineas Balance General'
    account_id = fields.Many2one(string='Cuenta', store=True, copy=True, tracking=0, comodel_name='account.account', )
    amount = fields.Float(string='Saldo Final', store=True, copy=True, tracking=0, )
    bold = fields.Boolean(string='Negrilla', store=True, copy=True, tracking=0, )
    code = fields.Char(string='Code', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Company', store=True, copy=True, tracking=0, comodel_name='res.company', )
    container_group_id = fields.Many2one(string='Container Group', store=True, copy=True, tracking=0,
                                         comodel_name='account.container.group', )
    credit = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    group_id = fields.Many2one(string='Group', store=True, copy=True, tracking=0, comodel_name='account.group', )
    has_value = fields.Boolean(string='Tiene Valor', store=True, copy=True, tracking=0, )
    identation = fields.Integer(string='Identacion', store=True, copy=True, tracking=0, )
    is_total = fields.Boolean(string='Es Total', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre Cuenta', store=True, copy=True, tracking=0, )
    report_balance_id = fields.Many2one(string='Informe', store=True, copy=True, tracking=0,
                                        comodel_name='account.financial.report.balance.general', )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    signo_en_reporte = fields.Char(string='Signo en Reporte', store=True, copy=True, tracking=0, )


class Líneasdeajustedevaloración(models.Model):
    _name = 'stock.valuation.adjustment.lines'
    _description = 'Líneas de ajuste de valoración'
    additional_landed_cost = fields.Monetary(string='Costos Adicionales en Destino', store=True, copy=True,
                                             tracking=0, )
    cost_id = fields.Many2one(string='Costo en Destino', store=True, required=True, copy=True, tracking=0,
                              comodel_name='stock.landed.cost', )
    cost_line_id = fields.Many2one(string='Línea de Costo', store=True, readonly=True, copy=True, tracking=0,
                                   comodel_name='stock.landed.cost.lines', )
    currency_id = fields.Many2one(string='Moneda', readonly=True, tracking=0, comodel_name='res.currency', )
    final_cost = fields.Monetary(string='Nuevo Valor', store=True, readonly=True, tracking=0, )
    former_cost = fields.Monetary(string='Valor original', store=True, copy=True, tracking=0, )
    move_id = fields.Many2one(string='Movimiento de Existencias', store=True, readonly=True, copy=True, tracking=0,
                              comodel_name='stock.move', )
    name = fields.Char(string='Descripción', store=True, readonly=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='product.product', )
    quantity = fields.Float(string='Cantidad', store=True, required=True, copy=True, tracking=0, )
    volume = fields.Float(string='Volumen', store=True, copy=True, tracking=0, )
    weight = fields.Float(string='Peso', store=True, copy=True, tracking=0, )


class Lineasdeamortizacion(models.Model):
    _name = 'project.service.order.tmp'
    _description = 'Lineas de amortizacion'
    balance = fields.Float(string='Saldo anterior', store=True, copy=True, tracking=0, )
    capital = fields.Float(string='Abono capital', store=True, copy=True, tracking=0, )
    checked = fields.Boolean(string='Facturada', store=True, readonly=True, copy=True, tracking=0, )
    cuota_number = fields.Integer(string='Cuota numero', store=True, copy=True, tracking=0, )
    date = fields.Date(string='Fecha cuota', store=True, copy=True, tracking=0, )
    intereses = fields.Float(string='Intereses', store=True, copy=True, tracking=0, )
    new_balance = fields.Float(string='Saldo capital', store=True, copy=True, tracking=0, )
    order_id = fields.Many2one(string='Orden finaciada', store=True, copy=True, tracking=0,
                               comodel_name='project.service.order', )
    value = fields.Float(string='Valor cuota', store=True, copy=True, tracking=0, )


class Lineasdeausencia(models.Model):
    _name = 'hr.leave.line'
    _description = 'Lineas de Ausencia'
    amount = fields.Float(string='Valor', store=True, copy=True, tracking=0, )
    contract_id = fields.Many2one(string='Contrato', readonly=True, tracking=0, comodel_name='hr.contract', )
    date_real_end = fields.Date(string='Fecha Final Real', store=True, copy=True, tracking=0, )
    date_real_start = fields.Date(string='Fecha Inicio Real', store=True, copy=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )
    is_discount_rest_day = fields.Boolean(string='Descontar dia de descanso', store=True, copy=True, tracking=0, )
    leave_id = fields.Many2one(string='Ausencia', store=True, required=True, copy=True, tracking=0,
                               comodel_name='hr.leave', )
    payslip_id = fields.Many2one(string='Nónima', store=True, copy=True, tracking=0, comodel_name='hr.payslip', )
    period_id = fields.Many2one(string='Periodo', store=True, copy=True, tracking=0, comodel_name='hr.period', )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    workday = fields.Boolean(string='Dia de trabajo', store=True, copy=True, tracking=0, )


class Líneasdecomprobante(models.Model):
    _name = 'account.voucher.line'
    _description = 'Líneas de comprobante'
    account_analytic_id = fields.Many2one(string='Cuenta Analítica', readonly=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    account_id = fields.Many2one(string='Cuenta', readonly=True, tracking=0, comodel_name='account.account', )
    amount_original = fields.Float(string='Cantidad original', store=True, readonly=True, tracking=0, )
    amount_unreconciled = fields.Float(string='Saldo abierto', store=True, readonly=True, tracking=0, )
    amount_untax = fields.Float(string='Importe base', store=True, copy=True, tracking=0, )
    amount = fields.Float(string='Valor', store=True, copy=True, tracking=0, )
    analytic_id = fields.Many2one(string='Cuenta Analítica', store=True, copy=True, tracking=0,
                                  comodel_name='account.analytic.account', )
    analytic_tag_ids = fields.Many2many(relation='lineasdeausencia_analytic_tag_ids_rel', column1='lineasdeausencia_id',
                                        column2='analytic_tag_ids_id', string='Etiquetas analíticas', store=True,
                                        copy=True, tracking=0,
                                        comodel_name='account.analytic.tag', )
    comment = fields.Char(string='Comentario de la contrapartida', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', readonly=True, tracking=0, comodel_name='res.company', )
    currency_id = fields.Many2one(string='Moneda', readonly=True, tracking=0, comodel_name='res.currency', )
    date_due = fields.Date(string='Fecha de Vencimiento', readonly=True, tracking=0, )
    date_original = fields.Date(string='Fecha', readonly=True, tracking=0, )
    date = fields.Date(string='Date', readonly=True, tracking=0, )
    invoice_id = fields.Many2one(string='Asiento Contable', store=True, copy=True, tracking=0,
                                 comodel_name='account.move', )
    local_currency_id = fields.Many2one(string='Moneda de la compañia', store=True, copy=True, tracking=0,
                                        comodel_name='res.currency', )
    move_line_id = fields.Many2one(string='Apunte contable', store=True, required=True, copy=True, tracking=0,
                                   comodel_name='account.move.line', )
    name = fields.Char(string='Descripción', store=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Cliente', readonly=True, tracking=0, comodel_name='res.partner', )
    reconcile = fields.Boolean(string='Reconciliación total', store=True, copy=True, tracking=0, )
    voucher_active_id = fields.Many2one(string='Activo', store=True, copy=True, tracking=0,
                                        comodel_name='account.voucher', )
    voucher_id = fields.Many2one(string='Comprobante', store=True, copy=True, tracking=0,
                                 comodel_name='account.voucher', )
    voucher_passive_id = fields.Many2one(string='Pasivo', store=True, copy=True, tracking=0,
                                         comodel_name='account.voucher', )
    voucher_reconcile_id = fields.Many2one(string='Conciliar', store=True, copy=True, tracking=0,
                                           comodel_name='account.voucher', )


class Líneasdecontroldecrédito(models.Model):
    _name = 'credit.control.analysis'
    _description = 'Líneas de control de crédito'
    company_id = fields.Many2one(string='Compañía', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    currency_id = fields.Many2one(string='Divisa', store=True, readonly=True, copy=True, tracking=0,
                                  comodel_name='res.currency', )
    level = fields.Integer(string='Nivel', store=True, readonly=True, copy=True, tracking=0, )
    open_balance = fields.Float(string='Saldo vencido', store=True, readonly=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Empresa', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='res.partner', )
    partner_ref = fields.Char(string='Empresa', store=True, readonly=True, copy=True, tracking=0, )
    policy_id = fields.Many2one(string='Política', store=True, readonly=True, copy=True, tracking=0,
                                comodel_name='credit.control.policy', )
    policy_level_id = fields.Many2one(string='Nivel de retraso', store=True, readonly=True, copy=True, tracking=0,
                                      comodel_name='credit.control.policy.level', )


class Líneasdedistribución(models.Model):
    _name = 'account.commercial.distribution.line'
    _description = 'Líneas de distribución'
    analytic_account_id = fields.Many2one(string='Cuenta Analítica', store=True, required=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    commercial_distribution_id = fields.Many2one(string='Distribución', store=True, required=True, copy=True,
                                                 tracking=0,
                                                 comodel_name='account.commercial.distribution', )
    commercial_id = fields.Many2one(string='Comercial', store=True, required=True, copy=True, tracking=0,
                                    comodel_name='account.commercial', )
    commercial_percentage = fields.Float(string='Porcentaje', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', readonly=True, required=True, tracking=0, )


class Líneasdedocumentosdian(models.Model):
    _name = 'account.move.dian.document.line'
    _description = 'Líneas de Documentos DIAN'
    dian_document_id = fields.Many2one(string='Documento DIAN', store=True, copy=True, tracking=0,
                                       comodel_name='account.move.dian.document', )
    send_async_reason = fields.Char(string='Motivo', store=True, copy=True, tracking=0, )
    send_async_response = fields.Text(string='Respuesta', store=True, copy=True, tracking=0, )
    send_async_status_code = fields.Char(string='Código de Estado', store=True, copy=True, tracking=0, )


class Lineasdeimpuestos(models.Model):
    _name = 'account.move.tax'
    _description = 'Lineas de Impuestos'
    account_id = fields.Many2one(string='Cuenta', store=True, copy=True, tracking=0, comodel_name='account.account', )
    credit = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    hr_expense_line_id = fields.Many2one(string='Expense Line', store=True, readonly=True, copy=True, tracking=0,
                                         comodel_name='hr.expense.line', )
    move_id = fields.Many2one(string='Factura', store=True, copy=True, tracking=0, comodel_name='account.move', )
    move_line_id = fields.Many2one(string='Linea Contable', store=True, copy=True, tracking=0,
                                   comodel_name='account.move.line', )
    name = fields.Char(string='Descripción', store=True, copy=True, tracking=0, )
    tax_base_amount = fields.Float(string='Importe Base', store=True, copy=True, tracking=0, )
    tax_id = fields.Many2one(string='Impuesto', store=True, copy=True, tracking=0, comodel_name='account.tax', )


class Lineasdelegalizacionesporrecobrar(models.Model):
    _name = 'hr.expense.line.recoup'
    _description = 'Lineas de legalizaciones por recobrar'
    description = fields.Text(string='Descripción', store=True, copy=True, tracking=0, )
    journal_id = fields.Many2one(string='Diario', store=True, copy=True, tracking=0, comodel_name='account.journal', )
    recoup_product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                        comodel_name='product.product', )
    tax_add = fields.Boolean(string='Añadir impuestos', store=True, copy=True, tracking=0, )


class Lineasdenovedad(models.Model):
    _name = 'hr.novelty.line'
    _description = 'Lineas de Novedad'
    amount = fields.Float(string='Valor', store=True, copy=True, tracking=0, )
    contract_id = fields.Many2one(string='Contrato', readonly=True, tracking=0, comodel_name='hr.contract', )
    inactive = fields.Boolean(string='Inactivo', store=True, copy=True, tracking=0, )
    novelty_id = fields.Many2one(string='Novedad', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='hr.novelty', )
    payslip_id = fields.Many2one(string='Nónima', store=True, copy=True, tracking=0, comodel_name='hr.payslip', )
    period_id = fields.Many2one(string='Periodo', store=True, copy=True, tracking=0, comodel_name='hr.period', )


class Líneasdepago(models.Model):
    _name = 'account.payment.line'
    _description = 'Líneas de pago'
    amount_company_currency = fields.Monetary(string='Importes moneda compañía', readonly=True, tracking=0, )
    amount_currency = fields.Monetary(string='Importe', store=True, copy=True, tracking=0, )
    amount_to_text = fields.Char(string='Monto en letras', readonly=True, tracking=0, )
    bank_account_required = fields.Boolean(string='Cuenta bancaria requerida', readonly=True, tracking=0, )
    bank_line_id = fields.Many2one(string='Línea de pago bancario', index=True, store=True, readonly=True, copy=True,
                                   tracking=0, comodel_name='bank.payment.line', )
    bank = fields.Many2one(string='Banco', readonly=True, tracking=0, comodel_name='res.bank', )
    communication = fields.Char(string='Comunicación', store=True, required=True, copy=True, tracking=0, )
    company_currency_id = fields.Many2one(string='Moneda', store=True, readonly=True, tracking=0,
                                          comodel_name='res.currency', )
    company_id = fields.Many2one(string='Compañía', store=True, readonly=True, tracking=0, comodel_name='res.company', )
    currency_id = fields.Many2one(string='Moneda de la transacción de pago', store=True, required=True, copy=True,
                                  tracking=0, comodel_name='res.currency', )
    date = fields.Date(string='Fecha de pago', store=True, copy=True, tracking=0, )
    ml_maturity_date = fields.Date(string='Fecha de vencimiento', readonly=True, tracking=0, )
    move_line_id = fields.Many2one(string='Apunte contable', store=True, copy=True, tracking=0,
                                   comodel_name='account.move.line', )
    name = fields.Char(string='Referencia de pago', store=True, readonly=True, tracking=0, )
    numero_cheque = fields.Char(string='Numero de Cheque', store=True, copy=True, tracking=0, )
    order_id = fields.Many2one(string='Orden de pago', index=True, store=True, copy=True, tracking=0,
                               comodel_name='account.payment.order', )
    other_partner_id = fields.Many2one(string='Beneficiario', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='res.partner', )
    partner_bank_id = fields.Many2one(string='Cuenta bancaria', store=True, copy=True, tracking=0,
                                      comodel_name='res.partner.bank', )
    partner_id = fields.Many2one(string='Empresa', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.partner', )


class Líneasdepagobancario(models.Model):
    _name = 'bank.payment.line'
    _description = 'Líneas de pago bancario'
    amount_company_currency = fields.Monetary(string='Importes moneda compañía', store=True, readonly=True,
                                              tracking=0, )
    amount_currency = fields.Monetary(string='Importe', store=True, readonly=True, tracking=0, )
    communication = fields.Char(string='Comunicación', store=True, readonly=True, required=True, copy=True,
                                tracking=0, )
    company_currency_id = fields.Many2one(string='Moneda', store=True, readonly=True, tracking=0,
                                          comodel_name='res.currency', )
    company_id = fields.Many2one(string='Compañía', store=True, readonly=True, tracking=0, comodel_name='res.company', )
    currency_id = fields.Many2one(string='Moneda de la transacción de pago', readonly=True, required=True, tracking=0,
                                  comodel_name='res.currency', )
    date = fields.Date(string='Fecha de pago', readonly=True, tracking=0, )
    name = fields.Char(string='Ref. de la línea de pago bancario', store=True, readonly=True, required=True,
                       copy=True,
                       tracking=0, )
    order_id = fields.Many2one(string='Orden', index=True, store=True, readonly=True, copy=True, tracking=0,
                               comodel_name='account.payment.order', )
    partner_bank_id = fields.Many2one(string='Cuenta bancaria', readonly=True, tracking=0,
                                      comodel_name='res.partner.bank', )
    partner_id = fields.Many2one(string='Empresa', store=True, readonly=True, tracking=0, comodel_name='res.partner', )


class Lineasdepreprogramacion(models.Model):
    _name = 'hr.roster.scheduling.line'
    _description = 'Lineas de pre programacion'
    day_1 = fields.Many2one(string='1', store=True, readonly=True, copy=True, tracking=0,
                            comodel_name='hr.roster.horario', )
    day_10 = fields.Many2one(string='10', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_11 = fields.Many2one(string='11', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_12 = fields.Many2one(string='12', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_13 = fields.Many2one(string='13', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_14 = fields.Many2one(string='14', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_15 = fields.Many2one(string='15', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_16 = fields.Many2one(string='16', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_17 = fields.Many2one(string='17', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_18 = fields.Many2one(string='18', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_19 = fields.Many2one(string='19', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_2 = fields.Many2one(string='2', store=True, readonly=True, copy=True, tracking=0,
                            comodel_name='hr.roster.horario', )
    day_20 = fields.Many2one(string='20', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_21 = fields.Many2one(string='21', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_22 = fields.Many2one(string='22', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_23 = fields.Many2one(string='23', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_24 = fields.Many2one(string='24', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_25 = fields.Many2one(string='25', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_26 = fields.Many2one(string='26', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_27 = fields.Many2one(string='27', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_28 = fields.Many2one(string='28', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_29 = fields.Many2one(string='29', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_3 = fields.Many2one(string='3', store=True, readonly=True, copy=True, tracking=0,
                            comodel_name='hr.roster.horario', )
    day_30 = fields.Many2one(string='30', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_31 = fields.Many2one(string='31', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='hr.roster.horario', )
    day_4 = fields.Many2one(string='4', store=True, readonly=True, copy=True, tracking=0,
                            comodel_name='hr.roster.horario', )
    day_5 = fields.Many2one(string='5', store=True, readonly=True, copy=True, tracking=0,
                            comodel_name='hr.roster.horario', )
    day_6 = fields.Many2one(string='6', store=True, readonly=True, copy=True, tracking=0,
                            comodel_name='hr.roster.horario', )
    day_7 = fields.Many2one(string='7', store=True, readonly=True, copy=True, tracking=0,
                            comodel_name='hr.roster.horario', )
    day_8 = fields.Many2one(string='8', store=True, readonly=True, copy=True, tracking=0,
                            comodel_name='hr.roster.horario', )
    day_9 = fields.Many2one(string='9', store=True, readonly=True, copy=True, tracking=0,
                            comodel_name='hr.roster.horario', )
    desfase = fields.Integer(string='Indice de inicio', store=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    group_index = fields.Integer(string='Index de grupo', store=True, copy=True, tracking=0, )
    index = fields.Integer(string='Indice', store=True, copy=True, tracking=0, )
    massive_scheduling_wizard_id = fields.Many2one(string='Wizard Masivo', store=True, copy=True, tracking=0,
                                                   comodel_name='massive.shift.scheduling.wizard', )
    modality_id = fields.Many2one(string='Modalidad', store=True, readonly=True, copy=True, tracking=0,
                                  comodel_name='hr.roster.modalidad', )
    project_service_order_line_id = fields.Many2one(string='Linea de orden de servicio', store=True, copy=True,
                                                    tracking=0, comodel_name='project.service.order.line', )
    puesto_id = fields.Many2one(string='puesto', store=True, readonly=True, copy=True, tracking=0,
                                comodel_name='hr.roster.puesto', )
    relevante = fields.Boolean(string='Relevante', store=True, copy=True, tracking=0, )
    sequence_ids = fields.Char(string='Sequence', store=True, copy=True, tracking=0, )
    use_relevante = fields.Boolean(string='Relevante', readonly=True, tracking=0, )
    valid_employee_ids = fields.Many2many(relation='lineasdepreprogramac_valid_employee_ids_rel',
                                          column1='lineasdepreprogramac_id', column2='valid_employee_ids_id',
                                          string='Empleados válidos', store=True, copy=True, tracking=0,
                                          comodel_name='hr.employee', )


class Lineasestructurainformescontables(models.Model):
    _name = 'account.financial.structure.line'
    _description = 'Lineas Estructura Informes Contables'
    description = fields.Char(string='Descripción', store=True, copy=True, tracking=0, )
    digits = fields.Integer(string='Digitos', store=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuenca', store=True, copy=True, tracking=0, )
    structure_id = fields.Many2one(string='Estructura', store=True, copy=True, tracking=0,
                                   comodel_name='account.financial.structure', )


class Lineasinformecontabilidadpruebas(models.Model):
    _name = 'account.financial.report.trial.line'
    _description = 'Lineas Informe Contabilidad Pruebas'
    account_id = fields.Many2one(string='Cuenta', store=True, copy=True, tracking=0, comodel_name='account.account', )
    amount_final = fields.Float(string='Saldo Final', store=True, copy=True, tracking=0, )
    amount_initial = fields.Float(string='Saldo Inicial', store=True, copy=True, tracking=0, )
    bold = fields.Boolean(string='Negrilla', store=True, copy=True, tracking=0, )
    code = fields.Char(string='Code', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Company', store=True, copy=True, tracking=0, comodel_name='res.company', )
    credit = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    level = fields.Integer(string='Nivel', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre Cuenta', store=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Tercero', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    report_trial_id = fields.Many2one(string='Informe', store=True, copy=True, tracking=0,
                                      comodel_name='account.financial.report.trial', )


class Lineaslibroauxiliar(models.Model):
    _name = 'account.financial.report.assistant.line'
    _description = 'Lineas Libro Auxiliar'
    account_id = fields.Many2one(string='Cuenta', store=True, copy=True, tracking=0, comodel_name='account.account', )
    amount_final = fields.Float(string='Saldo Final', store=True, copy=True, tracking=0, )
    amount_initial = fields.Float(string='Saldo Inicial', store=True, copy=True, tracking=0, )
    bold = fields.Boolean(string='Negrilla', store=True, copy=True, tracking=0, )
    code = fields.Char(string='Code', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Company', store=True, copy=True, tracking=0, comodel_name='res.company', )
    credit = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    ifrs_group_id = fields.Many2one(string='IFRS Group', store=True, copy=True, tracking=0,
                                    comodel_name='account.group', )
    level = fields.Integer(string='Nivel', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre Cuenta', store=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Tercero', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    report_balance_id = fields.Many2one(string='Informe', store=True, copy=True, tracking=0,
                                        comodel_name='account.financial.report.balance', )


class Lineaslibroauxiliarimpuestoswizard(models.Model):
    _name = 'account.financial.report.taxes.line'
    _description = 'Lineas Libro Auxiliar Impuestos Wizard'
    account_analytic_id = fields.Many2one(string='Cuenta Analitica', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    account_id = fields.Many2one(string='Cuenta', store=True, copy=True, tracking=0, comodel_name='account.account', )
    account_tax_id = fields.Many2one(string='Impuestos', store=True, copy=True, tracking=0,
                                     comodel_name='account.tax', )
    account = fields.Char(string='Código', store=True, copy=True, tracking=0, )
    amount_final = fields.Float(string='Saldo Final', store=True, copy=True, tracking=0, )
    bold = fields.Boolean(string='Bold', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    credit = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    move_id = fields.Many2one(string='Movimiento', store=True, copy=True, tracking=0, comodel_name='account.move', )
    move_line_id = fields.Many2one(string='Linea Contable', store=True, copy=True, tracking=0,
                                   comodel_name='account.move.line', )
    partner_id = fields.Many2one(string='Tercero', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    report_tax_id = fields.Many2one(string='Encabezado', store=True, copy=True, tracking=0,
                                    comodel_name='account.financial.report.taxes', )
    tax_amount = fields.Float(string='Base', store=True, copy=True, tracking=0, )
    tax_base_amount = fields.Float(string='Retención', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Lineasordendeservicio(models.Model):
    _name = 'project.service.order.line'
    _description = 'Lineas orden de servicio'
    adicional_valor = fields.Float(string='Valor adicional', store=True, copy=True, tracking=100, )
    adicional = fields.Char(string='Concepto adicional', store=True, copy=True, tracking=100, )
    cantidad_vigilantes = fields.Float(string='Cantidad de vigilantes', store=True, copy=True, tracking=0, )
    city_id = fields.Many2one(string='Ciudad', store=True, copy=True, tracking=0, comodel_name='res.city', )
    code_puesto = fields.Char(string='Codigo de puesto', store=True, readonly=True, tracking=0, )
    comodin_id = fields.Many2one(string='Comodin', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    company_id = fields.Many2one(string='Compañía', copy=True, tracking=0, comodel_name='res.company', )
    dias_facturables = fields.Integer(string='Dias mes', store=True, readonly=True, tracking=100, )
    duration = fields.Float(string='Total horas', store=True, readonly=True, tracking=100, )
    employee_ids = fields.Many2many(relation='lineasordendeservici_employee_ids_rel', column1='lineasordendeservici_id',
                                    column2='employee_ids_id', string='Vigilantes', store=True, copy=True, tracking=0,
                                    comodel_name='hr.employee', )
    end_date = fields.Datetime(string='Fecha finalizacion', store=True, copy=True, tracking=100, )
    force_value = fields.Boolean(string='Forzar tarifa especial', store=True, copy=True, tracking=100, )
    holidays = fields.Boolean(string='Festivos', store=True, copy=True, tracking=100, )
    horas_facturables = fields.Integer(string='Horas facturables', store=True, copy=True, tracking=100, )
    id_sale_order_line = fields.Integer(string='ID Linea de cotizacion', store=True, copy=True, tracking=0, )
    is_manager = fields.Boolean(string='¿Es gerente?', readonly=True, tracking=0, )
    linea_negocio = fields.Many2one(string='Linea de negocio', store=True, copy=True, tracking=0,
                                    comodel_name='project.linea.negocio', )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='lineasordendeservici_message_channel_ids_rel',
                                           column1='lineasordendeservici_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='lineasordendeservici_message_partner_ids_rel',
                                           column1='lineasordendeservici_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    modality_id = fields.Many2one(string='Modalidad Patron', store=True, copy=True, tracking=0,
                                  comodel_name='hr.roster.modalidad', )
    monitoring_value = fields.Float(string='Valor monitoreo', store=True, copy=True, tracking=0, )
    name_sale_order = fields.Char(string='Numero de cotizacion', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Ubicacion del servicio', store=True, copy=True, tracking=100, )
    no_cost = fields.Boolean(string='Sin Costo', store=True, copy=True, tracking=0, )
    notes = fields.Char(string='Observaciones', store=True, copy=True, tracking=0, )
    observaciones = fields.Text(string='Observaciones', store=True, copy=True, tracking=0, )
    order_id = fields.Many2one(string='Orden de servicio', store=True, copy=True, tracking=0,
                               comodel_name='project.service.order', )
    parent_modality_id = fields.Many2one(string='Modalidad Padre', store=True, copy=True, tracking=0,
                                         comodel_name='hr.roster.modalidad', )
    partner_id = fields.Many2one(string='Cliente', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.product', )
    project_id = fields.Many2one(string='Proyecto', store=True, readonly=True, tracking=100,
                                 comodel_name='project.project', )
    puesto_id = fields.Many2one(string='Puesto asociado', store=True, tracking=100, comodel_name='hr.roster.puesto', )
    regional_id = fields.Many2one(string='Regional', store=True, copy=True, tracking=100,
                                  comodel_name='res.regional', )
    rest_in = fields.Char(string='Salida a descanso', store=True, copy=True, tracking=0, )
    rest_out = fields.Char(string='Entrada de descanso', store=True, copy=True, tracking=0, )
    sale_line_id = fields.Many2one(string='Orden de servicio', store=True, copy=True, tracking=0,
                                   comodel_name='sale.order.line', )
    seguro_psvv = fields.Float(string='Poliza de seguro de vida', store=True, copy=True, tracking=0, )
    service_number = fields.Integer(string='Numero de servicio', store=True, copy=True, tracking=0, )
    service_type = fields.Many2one(string='Tipo de servicio', store=True, copy=True, tracking=100,
                                   comodel_name='project.service.type', )
    start_date = fields.Datetime(string='Fecha de inicio', store=True, copy=True, tracking=100, )
    subtotal = fields.Float(string='Subtotal', store=True, copy=True, tracking=0, )
    time_in = fields.Char(string='Hora de entrada', store=True, copy=True, tracking=100, )
    time_out = fields.Char(string='Hora de salida', store=True, copy=True, tracking=100, )
    use_parent_modality = fields.Boolean(string='Usa modalidad padre', readonly=True, tracking=0, )
    valor = fields.Float(string='Valor antes de IVA', store=True, copy=True, tracking=100, )
    weekdays = fields.Many2many(relation='lineasordendeservici_weekdays_rel', column1='lineasordendeservici_id',
                                column2='weekdays_id', string='Dias de la semana', store=True, copy=True, tracking=100,
                                comodel_name='res.weekday', )
    x_puesto_id_code = fields.Char(string='Puesto Asociado Corto', store=True, tracking=0, )


class Lineasporrecobrar(models.Model):
    _name = 'account.move.recoup.line'
    _description = 'Lineas por recobrar'
    description = fields.Text(string='Descripción', store=True, copy=True, tracking=0, )
    journal_id = fields.Many2one(string='Diario', store=True, copy=True, tracking=0, comodel_name='account.journal', )
    recoup_product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                        comodel_name='product.product', )
    tax_add = fields.Boolean(string='Añadir impuestos', store=True, copy=True, tracking=0, )


class Lineatarifario(models.Model):
    _name = 'hr.roster.tarifario.line'
    _description = 'Linea Tarifario'
    contract_id = fields.Many2one(string='Contrato', store=True, required=True, copy=True, tracking=0,
                                  comodel_name='hr.contract', )
    employee_id = fields.Many2one(string='Empleado', store=True, required=True, copy=True, tracking=0,
                                  comodel_name='hr.employee', )
    novelty_type_id = fields.Many2one(string='Categoria de novedad', store=True, copy=True, tracking=0,
                                      comodel_name='hr.novelty.type', )
    start_date = fields.Date(string='Fecha', store=True, required=True, copy=True, tracking=0, )
    tarifario_id = fields.Many2one(string='Tarfiario', store=True, required=True, copy=True, tracking=0,
                                   comodel_name='hr.roster.tarifario', )
    turn_id = fields.Many2one(string='Turno', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    valor = fields.Float(string='Valor', store=True, copy=True, tracking=0, )


class Lineatarifasdeentrega(models.Model):
    _name = 'delivery.rate.line'
    _description = 'Linea Tarifas de Entrega'
    company_id = fields.Many2one(string='Compañia', store=True, readonly=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    currency_id = fields.Many2one(string='Moneda', store=True, readonly=True, tracking=0, comodel_name='res.currency', )
    name = fields.Monetary(string='Valor', store=True, required=True, copy=True, tracking=0, )
    observation = fields.Char(string='Observación', store=True, copy=True, tracking=0, )
    rate_id = fields.Many2one(string='Tarifa', store=True, copy=True, tracking=0, comodel_name='delivery.rate', )


class LoaddataeInvoice(models.Model):
    _name = 'load.data.einvoice'
    _description = 'Load Data E-Invoice'
    e_invoice_xml = fields.Binary(string='E-Invoice XML', store=True, tracking=0, )
    invoice_id = fields.Many2one(string='Factura', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='account.move', )


class Logcambiodecargo(models.Model):
    _name = 'hr.employee.job.log'
    _description = 'Log Cambio de Cargo'
    hr_employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0,
                                     comodel_name='hr.employee', )
    new_charge = fields.Many2one(string='Nuevo Cargo', store=True, copy=True, tracking=0, comodel_name='hr.job', )
    pre_charge = fields.Many2one(string='Cargo Previo', store=True, copy=True, tracking=0, comodel_name='hr.job', )


class Logdeconceptosnómina(models.Model):
    _name = 'hr.concept.log'
    _description = 'Log de Conceptos Nómina'
    contract_id = fields.Many2one(string='Contrato', store=True, readonly=True, tracking=0,
                                  comodel_name='hr.contract', )
    employee_id = fields.Many2one(string='Empleado', store=True, readonly=True, tracking=0,
                                  comodel_name='hr.employee', )
    hr_concept = fields.Many2one(string='Concepto', store=True, copy=True, tracking=0, comodel_name='hr.concept', )
    hr_payslip_id = fields.Many2one(string='Nomina', store=True, copy=True, tracking=0, comodel_name='hr.payslip', )
    hr_payslip_line_id = fields.Many2one(string='Linea Nomina', store=True, copy=True, tracking=0,
                                         comodel_name='hr.payslip.line', )
    name = fields.Char(string='Descripcion', store=True, copy=True, tracking=0, )
    period_id = fields.Many2one(string='Periodo', store=True, readonly=True, tracking=0, comodel_name='hr.period', )
    value = fields.Float(string='Valor', store=True, copy=True, tracking=0, )


class Logdefacturacionelectronica(models.Model):
    _name = 'ei.transaction.log'
    _description = 'Log de Facturacion Electronica'
    content = fields.Text(string='Contenido', store=True, readonly=True, copy=True, tracking=0, )
    date = fields.Datetime(string='Fecha', store=True, readonly=True, copy=True, tracking=0, )
    invoice_id = fields.Many2one(string='Factura', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='account.move', )


class Logdenovedad(models.Model):
    _name = 'hr.novelty.log'
    _description = 'Log de Novedad'
    name = fields.Char(string='Log', store=True, copy=True, tracking=0, )


class Mailtrackingcorreo(models.Model):
    _name = 'mail.tracking.email'
    _description = 'MailTracking correo'
    bounce_description = fields.Char(string='Descripción del rebote', store=True, readonly=True, copy=True,
                                     tracking=0, )
    bounce_type = fields.Char(string='Tipo de rebote', store=True, readonly=True, copy=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, readonly=True, tracking=0, )
    error_description = fields.Char(string='Descripción del error', store=True, readonly=True, copy=True,
                                    tracking=0, )
    error_smtp_server = fields.Char(string='Error servidor SMTP', store=True, readonly=True, copy=True, tracking=0, )
    error_type = fields.Char(string='Tipo de error', store=True, readonly=True, copy=True, tracking=0, )
    mail_id = fields.Many2one(string='Correo electrónico', store=True, readonly=True, copy=True, tracking=0,
                              comodel_name='mail.mail', )
    mail_message_id = fields.Many2one(string='Mensaje', index=True, store=True, readonly=True, copy=True, tracking=0,
                                      comodel_name='mail.message', )
    name = fields.Char(string='Asunto', index=True, store=True, readonly=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Empresa', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='res.partner', )
    recipient_address = fields.Char(string='Dirección de correo de destinatario', index=True, store=True, readonly=True,
                                    tracking=0, )
    recipient = fields.Char(string='Correo del destinatario', store=True, readonly=True, copy=True, tracking=0, )
    sender = fields.Char(string='Correo del remitente', store=True, readonly=True, copy=True, tracking=0, )
    time = fields.Datetime(string='Tiempo', index=True, store=True, readonly=True, copy=True, tracking=0, )
    timestamp = fields.Float(string='UTC timestamp', store=True, readonly=True, copy=True, tracking=0, )
    token = fields.Char(string='Token de seguridad', store=True, readonly=True, copy=True, tracking=0, )


class Mailtrackingevento(models.Model):
    _name = 'mail.tracking.event'
    _description = 'MailTracking evento'
    date = fields.Date(string='Fecha', store=True, readonly=True, tracking=0, )
    error_description = fields.Char(string='Descripción del error', store=True, readonly=True, copy=True,
                                    tracking=0, )
    error_details = fields.Text(string='Detalles del error', store=True, readonly=True, copy=True, tracking=0, )
    error_type = fields.Char(string='Tipo de error', store=True, readonly=True, copy=True, tracking=0, )
    ip = fields.Char(string='IP del usuario', store=True, readonly=True, copy=True, tracking=0, )
    mobile = fields.Boolean(string='Es móvil?', store=True, readonly=True, copy=True, tracking=0, )
    os_family = fields.Char(string='Familia del sistema operativo', store=True, readonly=True, copy=True,
                            tracking=0, )
    recipient_address = fields.Char(string='Dirección de correo de destinatario', index=True, store=True, readonly=True,
                                    tracking=0, )
    recipient = fields.Char(string='Destinatario', store=True, readonly=True, copy=True, tracking=0, )
    smtp_server = fields.Char(string='Servidor SMTP', store=True, readonly=True, copy=True, tracking=0, )
    time = fields.Datetime(string='Tiempo', store=True, readonly=True, copy=True, tracking=0, )
    timestamp = fields.Float(string='UTC timestamp', store=True, readonly=True, copy=True, tracking=0, )
    tracking_email_id = fields.Many2one(string='Mensaje', index=True, store=True, readonly=True, required=True,
                                        copy=True,
                                        tracking=0, comodel_name='mail.tracking.email', )
    ua_family = fields.Char(string='User agent family', store=True, readonly=True, copy=True, tracking=0, )
    ua_type = fields.Char(string='User agent type', store=True, readonly=True, copy=True, tracking=0, )
    url = fields.Char(string='URL Clicada', store=True, readonly=True, copy=True, tracking=0, )
    user_agent = fields.Char(string='Aplicación del usuario', store=True, readonly=True, copy=True, tracking=0, )
    user_country_id = fields.Many2one(string='País del Usuario', store=True, readonly=True, copy=True, tracking=0,
                                      comodel_name='res.country', )


class Marcadeproducto(models.Model):
    _name = 'product.brand'
    _description = 'Marca de producto'
    description = fields.Text(string='Descripción', store=True, copy=True, tracking=0, )
    logo = fields.Binary(string='Logotipo', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre de la marca', store=True, required=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Empresa', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    products_count = fields.Integer(string='Número de productos', readonly=True, tracking=0, )


class Marcadomasiva(models.Model):
    _name = 'credit.control.marker'
    _description = 'Marcado masiva'
    line_ids = fields.Many2many(relation='marcadomasiva_line_ids_rel', column1='marcadomasiva_id',
                                column2='line_ids_id', string='Líneas de control de crédito', store=True, copy=True,
                                tracking=0,
                                comodel_name='credit.control.line', )


class Margendelproducto(models.Model):
    _name = 'product.margin'
    _description = 'Margen del Producto'
    from_date = fields.Date(string='Desde', store=True, copy=True, tracking=0, )
    to_date = fields.Date(string='A', store=True, copy=True, tracking=0, )


class Mayorybalance(models.TransientModel):
    _name = 'account.financial.report.major.balance.wizard'
    _description = 'Mayor y Balance'
    account_ids = fields.Many2many('account.account', relation='afr_mbwiz_account_rel', column1='wizard_id',
                                   column2='account_id', string='Cuentas', copy=False)
    company_id = fields.Many2one('res.company', string='Compañía', default=lambda self: self.env.company, readonly=True,
                                 copy=False)
    date_start = fields.Date(string='Fecha Inicio', copy=False)
    date_end = fields.Date(string='Fecha Fin', copy=False)
    levels_ids = fields.Many2many('account.financial.levels', relation='afr_mbwiz_level_rel', column1='wizard_id',
                                  column2='level_id', string='Niveles', copy=False)
    partner_ids = fields.Many2many('res.partner', relation='afr_mbwiz_partner_rel', column1='wizard_id',
                                   column2='partner_id', string='Terceros', copy=False)
    structure_id = fields.Many2one('account.financial.structure', string='Estructura', copy=False)


class Mediosdepago(models.Model):
    _name = 'account.payment.mean.code'
    _description = 'Medios de Pago'
    code = fields.Char(string='Código', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Métodosdeenvío(models.Model):
    _name = 'delivery.carrier'
    _description = 'Métodos de envío'
    active = fields.Boolean(string='Activo', store=True, copy=True, tracking=0, )
    amount = fields.Float(string='Importe', store=True, copy=True, tracking=0, )
    can_generate_return = fields.Boolean(string='Puedes generar una devolución', readonly=True, tracking=0, )
    company_id = fields.Many2one(string='Compañía', store=True, tracking=0, comodel_name='res.company', )
    country_ids = fields.Many2many(relation='mediosdepago_country_ids_rel', column1='mediosdepago_id',
                                   column2='country_ids_id', string='Países', store=True, copy=True, tracking=0,
                                   comodel_name='res.country', )
    debug_logging = fields.Boolean(string='Registro de debug', store=True, copy=True, tracking=0, )
    fixed_price = fields.Float(string='Precio fijo', store=True, tracking=0, )
    free_over = fields.Boolean(string='Gratuito si el importe del pedido es superior a', store=True, copy=True,
                               tracking=0, )
    get_return_label_from_portal = fields.Boolean(string='Etiqueta de devolución accesible desde el portal de clientes',
                                                  store=True, copy=True, tracking=0, )
    margin = fields.Float(string='Margen', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Método entrega', store=True, required=True, copy=True, tracking=0, )
    prod_environment = fields.Boolean(string='Entorno', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Envío de producto', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='product.product', )
    return_label_on_delivery = fields.Boolean(string='Generar etiqueta de devolución', store=True, copy=True,
                                              tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    state_ids = fields.Many2many(relation='mediosdepago_state_ids_rel', column1='mediosdepago_id',
                                 column2='state_ids_id', string='Estados', store=True, copy=True, tracking=0,
                                 comodel_name='res.country.state', )
    zip_from = fields.Char(string='CP desde', store=True, copy=True, tracking=0, )
    zip_to = fields.Char(string='CP hasta', store=True, copy=True, tracking=0, )


class Militarydegree(models.Model):
    _name = 'hr.military.degree'
    _description = 'Military Degree'
    name = fields.Char(string='Grado militar', store=True, copy=True, tracking=0, )


class Modalidad(models.Model):
    _name = 'hr.roster.modalidad'
    _description = 'Modalidad'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # chatter + actividades

    # Básicos
    name = fields.Char(string='Nombre', required=True, copy=True, tracking=100)
    horario_id = fields.Many2one('resource.calendar', string='Horario', required=True, copy=True, tracking=100)
    parent_id = fields.Many2one('hr.roster.modalidad', string='Modalidad Padre', copy=True)

    # Números / banderas
    basic_salary = fields.Float(string='Salario Básico', copy=True, tracking=0)
    bearing_value = fields.Float(string='Valor Rodamiento', copy=True, tracking=0)
    supplementary_work_value = fields.Float(string='Valor Trabajo Suplementario', copy=True, tracking=0)
    transport_assistant = fields.Float(string='Auxilio de transporte', copy=True, tracking=0)
    desfase = fields.Integer(string='Desfase', copy=True, tracking=100)
    festivo = fields.Boolean(string='Festivo', copy=True, tracking=100)
    is_parent = fields.Boolean(string='¿Es modalidad padre?', copy=True, tracking=0)
    numero_personal = fields.Integer(string='Número Personal', required=True, copy=True, tracking=100)
    numero_personal2 = fields.Float(string='Número Personal (Capacidad Real)', copy=True, tracking=100)
    not_programmed_turn = fields.Many2one('hr.roster.horario', string='Turno en día no programado', copy=True,
                                          tracking=0)
    regional_ids = fields.Many2many('res.regional', relation='hr_roster_modalidad_regional_rel', column1='modalidad_id',
                                    column2='regional_id', string='Sucursal', copy=True, tracking=0)
    tipo_turno_ids = fields.Many2many('hr.roster.horario', relation='hr_roster_modalidad_turno_rel',
                                      column1='modalidad_id', column2='horario_id', string='Tipo Turnos', copy=True,
                                      tracking=100)


class Modosdepago(models.Model):
    _name = 'account.payment.mode'
    _description = 'Modos de pago'
    active = fields.Boolean(string='Activo', default=True)
    name = fields.Char(string='Nombre', required=True, copy=True)
    company_id = fields.Many2one('res.company', string='Compañía', required=True, default=lambda self: self.env.company,
                                 index=True, ondelete='restrict')
    payment_method_id = fields.Many2one('account.payment.method', string='Método de pago', required=True,
                                        ondelete='restrict')
    payment_method_code = fields.Char(string='Code (Do Not Modify)', related='payment_method_id.code', store=True,
                                      readonly=True)
    bank_id = fields.Many2one('account.payment.file.config', string='Archivo de Banco', ondelete='set null')
    default_invoice = fields.Boolean(string='Vinculado a una factura o factura rectificativa', copy=True)
    payment_order_ok = fields.Boolean(string='Seleccionable en las órdenes', copy=True)
    group_lines = fields.Boolean(string='Agrupar transacciones en las órdenes de pago', copy=True)
    generate_move = fields.Boolean(string='Generar asientos contables al subir el archivo', copy=True)
    post_move = fields.Boolean(string='Publicar movimiento', copy=True)
    no_debit_before_maturity = fields.Boolean(string='No permitir el adeudo antes de la fecha de vencimiento',
                                              copy=True)
    show_bank_account_from_journal = fields.Boolean(string='Cuenta bancaria de los diarios', copy=True)
    show_bank_account_chars = fields.Integer(string='Nº de dígitos de cuenta bancaria del cliente', copy=True)
    note = fields.Text(string='Nota', copy=True)
    fixed_journal_id = fields.Many2one('account.journal', string='Diario de banco fijo', ondelete='set null',
                                       domain="[('type','in',('bank','cash')), ('company_id','=',company_id)]")
    supplier_advance_journal_id = fields.Many2one('account.journal', string='Diario Anticipo Proveedor',
                                                  ondelete='set null', domain="[('company_id','=',company_id)]")
    transfer_journal_id = fields.Many2one('account.journal', string='Diario de transferencia', ondelete='set null',
                                          domain="[('company_id','=',company_id)]")
    transfer_account_id = fields.Many2one('account.account', string='Cuenta de transferencia', ondelete='set null',
                                          domain="[('company_id','=',company_id)]")
    default_journal_ids = fields.Many2many('account.journal', relation='apm_default_journal_rel', column1='mode_id',
                                           column2='journal_id', string='Filtro de diarios',
                                           domain="[('company_id','=',company_id)]",
                                           help='Diarios sugeridos por defecto')
    variable_journal_ids = fields.Many2many('account.journal', relation='apm_variable_journal_rel', column1='mode_id',
                                            column2='journal_id', string='Diarios de banco permitidos',
                                            domain="[('type','in',('bank','cash')), ('company_id','=',company_id)]")


class Montodía(models.Model):
    _name = 'quoter.amount.day'
    _description = 'Monto día'
    amount_day = fields.Integer(string='Cantidad días', store=True, copy=True, tracking=0, )
    holidays = fields.Boolean(string='Festivos', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    weekdays = fields.Many2many(relation='modosdepago_weekdays_rel', column1='modosdepago_id', column2='weekdays_id',
                                string='Dias de la semana', store=True, copy=True, tracking=0,
                                comodel_name='res.weekday', )


class Multicurrencyrevaluationreport(models.Model):
    _name = 'account.multicurrency.revaluation'
    _description = 'Multicurrency Revaluation Report'
    account_code = fields.Char(string='Account Code', store=True, copy=True, tracking=0, )
    account_id = fields.Many2one(string='Account', store=True, copy=True, tracking=0,
                                 comodel_name='account.account', )
    account_name = fields.Char(string='Account Name', store=True, copy=True, tracking=0, )
    analytic_account_id = fields.Many2one(string='Analytic Account', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    analytic_tag_ids = fields.Many2many(relation='multicurrencyrevalua_analytic_tag_ids_rel',
                                        column1='multicurrencyrevalua_id', column2='analytic_tag_ids_id',
                                        string='Analytic Tag', store=True, copy=True, tracking=0,
                                        comodel_name='account.analytic.tag', )
    balance = fields.Monetary(string='Saldo', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Company', store=True, copy=True, tracking=0, comodel_name='res.company', )
    credit = fields.Monetary(string='Credit', store=True, copy=True, tracking=0, )
    currency_code = fields.Char(string='Currency Code', store=True, copy=True, tracking=0, )
    currency_id = fields.Many2one(string='Moneda', store=True, copy=True, tracking=0, comodel_name='res.currency', )
    date = fields.Date(string='Date', store=True, copy=True, tracking=0, )
    debit = fields.Monetary(string='Debit', store=True, copy=True, tracking=0, )
    display_type = fields.Char(string='Display Type', store=True, copy=True, tracking=0, )
    journal_id = fields.Many2one(string='Journal', store=True, copy=True, tracking=0,
                                 comodel_name='account.journal', )
    move_id = fields.Many2one(string='Move', store=True, copy=True, tracking=0, comodel_name='account.move', )
    move_name = fields.Char(string='Move Name', store=True, copy=True, tracking=0, )
    move_ref = fields.Char(string='Move Ref', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Name', store=True, copy=True, tracking=0, )
    report_adjustment = fields.Monetary(string='Adjustment', store=True, copy=True, tracking=0, )
    report_amount_currency_current = fields.Monetary(string='Balance at current rate', store=True, copy=True,
                                                     tracking=0, )
    report_amount_currency = fields.Monetary(string='Balance in foreign currency', store=True, copy=True,
                                             tracking=0, )
    report_balance = fields.Monetary(string='Balance at operation rate', store=True, copy=True, tracking=0, )
    report_currency_id = fields.Many2one(string='Report Currency', store=True, copy=True, tracking=0,
                                         comodel_name='res.currency', )
    report_include = fields.Boolean(string='Report Include', store=True, copy=True, tracking=0, )


class Multicurrencyrevaluationwizard(models.Model):
    _name = 'account.multicurrency.revaluation.wizard'
    _description = 'Multicurrency Revaluation Wizard'
    company_id = fields.Many2one(string='Company', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date = fields.Date(string='Date', store=True, required=True, copy=True, tracking=0, )
    expense_provision_account_id = fields.Many2one(string='Expense account', required=True, tracking=0,
                                                   comodel_name='account.account', )
    income_provision_account_id = fields.Many2one(string='Income Account', required=True, tracking=0,
                                                  comodel_name='account.account', )
    journal_id = fields.Many2one(string='Journal', required=True, tracking=0, comodel_name='account.journal', )
    preview_data = fields.Text(string='Preview Data', readonly=True, tracking=0, )
    reversal_date = fields.Date(string='Reversal Date', store=True, required=True, copy=True, tracking=0, )
    show_warning_move_id = fields.Many2one(string='Show Warning Move', readonly=True, tracking=0,
                                           comodel_name='account.move', )


class Nivelesinformescontables(models.Model):
    _name = 'account.financial.levels'
    _description = 'Niveles Informes Contables'
    code = fields.Char(string='Código', store=True, copy=True, tracking=0, )
    help = fields.Char(string='Ayuda', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class Nómina(models.Model):
    _name = 'hr.payslip'
    _description = 'Nómina'
    accepted_rejected_datetime = fields.Datetime(string='Datetime of Accepted/Rejected', store=True, tracking=0, )
    access_token = fields.Char(string='Access token', store=True, tracking=0, )
    accounting_date = fields.Date(string='Fecha de Contabilización', store=True, copy=True, tracking=0, )
    amount_total_words = fields.Char(string='Neto Total en Palabras', readonly=True, tracking=0, )
    amount_total = fields.Float(string='Neto Total', readonly=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    contract_id = fields.Many2one(string='Contrato', store=True, required=True, copy=True, tracking=0,
                                  comodel_name='hr.contract', )
    dbname = fields.Char(string='DB Name', readonly=True, tracking=0, )
    dian_document_ids = fields.Many2many(relation='nivelesinformesconta_dian_document_ids_rel',
                                         column1='nivelesinformesconta_id', column2='dian_document_ids_id',
                                         string='DIAN Documents', store=True, copy=True, tracking=0,
                                         comodel_name='hr.payslip.dian.document', )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    error_log = fields.Text(string='Errores', store=True, readonly=True, copy=True, tracking=0, )
    hr_puesto = fields.Many2one(string='Puesto', store=True, copy=True, tracking=0, comodel_name='hr.roster.puesto', )
    is_accepted_rejected = fields.Boolean(string='Is Accepted/Rejected?', store=True, tracking=0, )
    journal_id = fields.Many2one(string='Diario', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='account.journal', )
    liquidation_date = fields.Date(string='Fecha de Liquidación', store=True, copy=True, tracking=0, )
    mean_ces = fields.Float(string='Promedio Cesantias', store=True, copy=True, tracking=0, )
    mean_ices = fields.Float(string='Promedio Interes Cesantias', store=True, copy=True, tracking=0, )
    mean_prima = fields.Float(string='Promedio Prima', store=True, copy=True, tracking=0, )
    mean_vac = fields.Float(string='Promedio Vacaciones', store=True, copy=True, tracking=0, )
    move_id = fields.Many2one(string='Asiento contable', store=True, readonly=True, tracking=0,
                              comodel_name='account.move', )
    name = fields.Char(string='Nombre', store=True, readonly=True, copy=True, tracking=0, )
    payslip_processing_id = fields.Many2one(string='Procesamiento de Nómina', store=True, copy=True, tracking=0,
                                            comodel_name='hr.payslip.processing', )
    payslip_type_id = fields.Many2one(string='Tipo de Nómina', store=True, required=True, copy=True, tracking=0,
                                      comodel_name='hr.payslip.type', )
    period_id = fields.Many2one(string='Periodo', store=True, required=True, copy=True, tracking=0,
                                comodel_name='hr.period', )
    portal_exclude = fields.Boolean(string='Excluir del Portal', store=True, copy=True, tracking=0, )
    sequence_resolution_id = fields.Many2one(string='Sequence Resolution', readonly=True, tracking=0,
                                             comodel_name='ir.sequence', )
    slip_processing_id = fields.Many2one(string='Provisiones', store=True, readonly=True, copy=True, tracking=0,
                                         comodel_name='hr.payslip', )
    warn_inactive_certificate = fields.Boolean(string='Warn About Inactive Certificate?', readonly=True, tracking=0, )
    warn_remaining_certificate = fields.Boolean(string='Warn About Remainings?', readonly=True, tracking=0, )


class Novedad(models.Model):
    _name = 'hr.novelty'
    _description = 'Novedad'
    access_token = fields.Char(string='Security Token', store=True, tracking=0, )
    access_url = fields.Char(string='Portal Access URL', readonly=True, tracking=0, )
    access_warning = fields.Text(string='Access warning', readonly=True, tracking=0, )
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Next Activity Type', tracking=0, comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    amount_payment_client = fields.Float(string='Valor cobrar cliente', store=True, copy=True, tracking=0, )
    amount = fields.Float(string='Valor', store=True, copy=True, tracking=100, )
    analytic_account_id = fields.Many2one(string='Analytic Account', store=True, copy=True, tracking=100,
                                          comodel_name='account.analytic.account', )
    approve_date = fields.Date(string='Fecha de aprobación', store=True, copy=True, tracking=100, )
    close_from_solo_adicionales = fields.Boolean(string='Cerrado desde solo adicionales', store=True, copy=True,
                                                 tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, readonly=True, copy=True, tracking=100,
                                 comodel_name='res.company', )
    contract_group_id = fields.Many2one(string='Grupo de Contrato', readonly=True, tracking=100,
                                        comodel_name='hr.contract.group', )
    contract_id = fields.Many2one(string='Contrato', store=True, required=True, copy=True, tracking=100,
                                  comodel_name='hr.contract', )
    date_end = fields.Date(string='Fecha Final', store=True, copy=True, tracking=100, )
    date_start = fields.Date(string='Fecha Inicio', store=True, required=True, copy=True, tracking=100, )
    description = fields.Text(string='Descripcion', store=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=100,
                                  comodel_name='hr.employee', )
    hr_roster_prefactura_ids = fields.Many2many(relation='novedad_hr_roster_prefactura_rel', column1='novedad_id',
                                                column2='hr_roster_prefactura_id', string='Prefacturas', store=True,
                                                copy=True, tracking=0,
                                                comodel_name='hr.roster.prefactura', )
    inactive_definite = fields.Boolean(string='Inactivacion Definitiva', store=True, copy=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='novedad_message_channel_ids_rel', column1='novedad_id',
                                           column2='message_channel_ids_id', string='Followers (Channels)',
                                           readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='novedad_message_partner_ids_rel', column1='novedad_id',
                                           column2='message_partner_ids_id', string='Followers (Partners)',
                                           readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, readonly=True, copy=True, tracking=100, )
    novelty_type_id = fields.Many2one(string='Categoría de Novedad', store=True, required=True, copy=True, tracking=0,
                                      comodel_name='hr.novelty.type', )
    payment_client_date = fields.Date(string='Fecha Cobro cliente', store=True, copy=True, tracking=0, )
    payment_client = fields.Boolean(string='Cobro Cliente', store=True, copy=True, tracking=0, )
    paymentc_analytic_id = fields.Many2one(string='Cuenta A. Cobro', store=True, copy=True, tracking=0,
                                           comodel_name='account.analytic.account', )
    quantity = fields.Float(string='Cantidad', store=True, copy=True, tracking=100, )
    replace_concept = fields.Boolean(string='Remplaza Concepto', store=True, copy=True, tracking=100, )
    roster = fields.Boolean(string='Origen cierre de turnos', store=True, copy=True, tracking=100, )
    tarifario_id = fields.Many2one(string='Tarifario', store=True, copy=True, tracking=0,
                                   comodel_name='hr.roster.tarifario', )
    turn_id = fields.Many2one(string='Turno', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    turn_ids = fields.Many2many(relation='novedad_turn_ids_rel', column1='novedad_id', column2='turn_ids_id',
                                string='Turnos que intervienen', store=True, copy=True, tracking=0,
                                comodel_name='hr.roster.turno', )
    unit_amount = fields.Float(string='Valor Unitario', store=True, copy=True, tracking=100, )


class Novedades(models.Model):
    _name = 'hr.payroll.novedades'
    _description = 'Novedades'
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Next Activity Type', tracking=0, comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    analytic_account_id = fields.Many2one(string='Cuenta analitica', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    apply_payroll_novedad = fields.Boolean(string='Aplica a nomina', store=True, copy=True, tracking=0, )
    approve_date = fields.Date(string='Fecha de Aprobacion', store=True, readonly=True, copy=True, tracking=0, )
    cantidad = fields.Float(string='Cantidad', store=True, readonly=True, copy=True, tracking=0, )
    category_id = fields.Many2one(string='Categoria', store=True, readonly=True, required=True, copy=True, tracking=0,
                                  comodel_name='hr.payroll.novedades.category', )
    contract_id = fields.Many2one(string='Contrato', store=True, copy=True, tracking=0, comodel_name='hr.contract', )
    date = fields.Date(string='Fecha', store=True, readonly=True, required=True, copy=True, tracking=0, )
    description = fields.Text(string='Descripcion', store=True, readonly=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, readonly=True, required=True, copy=True, tracking=0,
                                  comodel_name='hr.employee', )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='novedades_message_channel_ids_rel', column1='novedades_id',
                                           column2='message_channel_ids_id', string='Followers (Channels)',
                                           readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='Error de entrega del SMS', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='novedades_message_partner_ids_rel', column1='novedades_id',
                                           column2='message_partner_ids_id', string='Followers (Partners)',
                                           readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    name = fields.Char(string='Codigo', store=True, readonly=True, copy=True, tracking=0, )
    neto = fields.Boolean(string='Regla del Neto a Pagar', store=True, copy=True, tracking=0, )
    payslip_id = fields.Many2one(string='Pagado en nomina', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='hr.payslip', )
    payslip_neto_id = fields.Many2one(string='Creado en la nomina', store=True, readonly=True, copy=True, tracking=0,
                                      comodel_name='hr.payslip', )
    roster = fields.Boolean(string='Origen cierre de turnos', store=True, copy=True, tracking=0, )
    total = fields.Float(string='Total', store=True, readonly=True, tracking=0, )
    valor = fields.Float(string='Valor', store=True, readonly=True, copy=True, tracking=0, )


class Númeroempresa(models.Model):
    _name = 'res.partner.id_number'
    _description = 'Número empresa'
    active = fields.Boolean(string='Activo', store=True, copy=True, tracking=0, )
    category_id = fields.Many2one(string='Categoría', store=True, required=True, copy=True, tracking=0,
                                  comodel_name='res.partner.id_category', )
    comment = fields.Text(string='Notas', store=True, copy=True, tracking=0, )
    date_issued = fields.Date(string='Emitido en', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Número ID', store=True, required=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Empresa', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.partner', )
    partner_issued_id = fields.Many2one(string='Emitido por', store=True, copy=True, tracking=0,
                                        comodel_name='res.partner', )
    place_issuance = fields.Char(string='Lugar de emisión', store=True, copy=True, tracking=0, )
    valid_from = fields.Date(string='Válido desde', store=True, copy=True, tracking=0, )
    valid_until = fields.Date(string='Válido hasta', store=True, copy=True, tracking=0, )
    x_activo = fields.Boolean(string='Cliente Activo', store=True, readonly=True, tracking=0, )
    x_adjunto_bin = fields.Binary(string='Soporte', store=True, copy=True, tracking=0, )
    x_adjunto_id = fields.Char(string='Id Soporte', readonly=True, tracking=0, )
    x_auxiliar_file_url = fields.Char(string='Url Soporte', store=True, readonly=True, tracking=0, )
    x_auxiliar_file = fields.Many2many(relation='novedades_x_auxiliar_file_rel', column1='novedades_id',
                                       column2='x_auxiliar_file_id', string='Soporte', store=True, copy=True,
                                       tracking=0,
                                       comodel_name='ir.attachment', )
    x_customer = fields.Boolean(string='Es Cliente', readonly=True, tracking=0, )
    x_PD473416478822277 = fields.Binary(string='Adjunto', store=True, copy=True, tracking=0, )
    x_supplier = fields.Boolean(string='Es Proveedor', tracking=0, )


class Obligacionfinanciera(models.Model):
    _name = 'account.loan'
    _description = 'Obligacion Financiera'
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Next Activity Type', tracking=0, comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    balance_debt = fields.Float(string='Saldo por amortizar', readonly=True, tracking=0, )
    balance = fields.Float(string='Valor inicial de obligacion', store=True, required=True, copy=True, tracking=0, )
    bank_journal_id = fields.Many2one(string='Diario de Banco', store=True, required=True, copy=True, tracking=0,
                                      comodel_name='account.journal', )
    capital_id = fields.Many2one(string='Capital', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='account.account', )
    company_id = fields.Many2one(string='Company', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    currency_id = fields.Many2one(string='Moneda', store=True, required=True, copy=True, tracking=0,
                                  comodel_name='res.currency', )
    final_payment = fields.Float(string='Pago final', store=True, copy=True, tracking=100, )
    first_payment = fields.Float(string='Primer desembolso', store=True, copy=True, tracking=0, )
    gastos_bancarios_id = fields.Many2one(string='Gastos Bancarios', store=True, copy=True, tracking=0,
                                          comodel_name='account.account', )
    inter_de_mora_id = fields.Many2one(string='Intereses de Mora', store=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    intereses_id = fields.Many2one(string='Intereses', store=True, required=True, copy=True, tracking=0,
                                   comodel_name='account.account', )
    intrest_per_period = fields.Float(string='Interes', store=True, required=True, copy=True, tracking=100, )
    loan_journal_id = fields.Many2one(string='Diario de Obligacion', store=True, required=True, copy=True, tracking=0,
                                      comodel_name='account.journal', )
    loan_no = fields.Char(string='Numero de Obligacion', store=True, required=True, copy=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='obligacionfinanciera_message_channel_ids_rel',
                                           column1='obligacionfinanciera_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='obligacionfinanciera_message_partner_ids_rel',
                                           column1='obligacionfinanciera_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    partner_bank_id = fields.Many2one(string='Cuenta de banco', store=True, copy=True, tracking=0,
                                      comodel_name='res.partner.bank', )
    partner_id = fields.Many2one(string='Tercero', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.partner', )
    payment_date = fields.Date(string='Fecha de desembolso', store=True, required=True, copy=True, tracking=0, )
    period_no = fields.Integer(string='Meses Entre Periodos', store=True, required=True, copy=True, tracking=0, )
    periods_to_pay = fields.Integer(string='Plazo Inicial', store=True, required=True, copy=True, tracking=0, )
    remain_period = fields.Integer(string='Periodos por pagar', readonly=True, tracking=0, )
    start_period = fields.Integer(string='Periodos de Gracia', store=True, copy=True, tracking=0, )
    tes_oreria_id = fields.Many2one(string='Tesoreria', store=True, required=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    tir_contable = fields.Float(string='TIR Contable', store=True, copy=True, tracking=0, )
    tir = fields.Float(string='TIR Fiscal', store=True, copy=True, tracking=0, )


class Ordendepago(models.Model):
    _name = 'account.payment.order'
    _description = 'Orden de pago'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # Identificación
    name = fields.Char(string='Número', default='/', readonly=True, copy=False, tracking=True)
    description = fields.Char(string='Descripción', copy=True)
    company_id = fields.Many2one('res.company', string='Compañía', required=True, default=lambda self: self.env.company,
                                 index=True, tracking=True)
    company_currency_id = fields.Many2one('res.currency', string='Moneda', related='company_id.currency_id', store=True,
                                          readonly=True)
    payment_mode_id = fields.Many2one('account.payment.mode', string='Modo de pago', required=True, ondelete='restrict',
                                      tracking=True)
    payment_method_id = fields.Many2one('account.payment.method', string='Método de pago',
                                        related='payment_mode_id.payment_method_id', store=True, readonly=True)
    journal_id = fields.Many2one('account.journal', string='Diario de banco',
                                 domain="[('type','in',('bank','cash')), ('company_id','=',company_id)]",
                                 ondelete='restrict', tracking=True)
    allowed_journal_ids = fields.Many2many('account.journal', relation='apo_allowed_journal_rel', column1='order_id',
                                           column2='journal_id', string='Diarios permitidos', readonly=True,
                                           domain="[('company_id','=',company_id)]")
    company_partner_bank_id = fields.Many2one('res.partner.bank', string='Cuenta bancaria de la compañía',
                                              readonly=True)
    move_id = fields.Many2one('account.move', string='Comprobante Contable', readonly=True)
    move_name = fields.Char(string='Nombre Comprobante', readonly=True)
    file_name = fields.Char(string='Archivo Pago Banco', readonly=True, copy=False)
    file_text = fields.Binary(string='Archivo Pago Banco', readonly=True, copy=False)
    payment_order_date = fields.Date(string='Fecha de Pago', required=True, copy=True)
    date_scheduled = fields.Date(string='Fecha de ejecución del pago', copy=True, tracking=True)
    date_generated = fields.Date(string='Fecha del fichero generado', readonly=True, copy=False)
    date_uploaded = fields.Date(string='Fecha de subida del fichero', readonly=True, copy=False)
    date_done = fields.Date(string='Fecha de realización', readonly=True, copy=False)
    time_of_process = fields.Datetime(string='Fecha Transmisión', readonly=True, copy=False)
    cheque = fields.Char(string='Cheque', copy=True, tracking=True)
    narration = fields.Text(string='Notas', copy=True)
    bank_line_count = fields.Integer(string='Número de líneas bancarias', readonly=True)
    total_company_currency = fields.Monetary(string='Total en la moneda de la compañía',
                                             currency_field='company_currency_id', readonly=True)
    generated_user_id = fields.Many2one('res.users', string='Generado por', readonly=True)

    # ----- Secuencia -----
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals['name'] in ('/', ''):
                vals['name'] = self.env['ir.sequence'].next_by_code('account.payment.order') or '/'
        return super().create(vals_list)

    # (Opcional) al generar el archivo, puedes setear:
    # self.write({
    #     'file_name': nombre,
    #     'file_text': binario,
    #     'date_generated': fields.Date.context_today(self),
    #     'generated_user_id': self.env.user.id,
    # })


class Ordendeservicio(models.Model):
    _name = 'project.service.order'
    _description = 'Orden de servicio'
    analytic_account_id = fields.Many2one(string='Centro de costos', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    cliente_address = fields.Char(string='Direccion', store=True, copy=True, tracking=0, )
    cliente_id = fields.Many2one(string='Razon social', store=True, readonly=True, tracking=0,
                                 comodel_name='res.partner', )
    cliente_phone = fields.Char(string='Telefono', store=True, copy=True, tracking=0, )
    contact_id = fields.Many2one(string='Contacto', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    contact_job = fields.Char(string='Cargo de contacto', store=True, readonly=True, tracking=0, )
    corssovered_budget_id = fields.Many2one(string='Presupuesto', store=True, copy=True, tracking=0,
                                            comodel_name='crossovered.budget', )
    count_moves = fields.Integer(string='Movimientos', readonly=True, tracking=0, )
    cuotas = fields.Integer(string='Numero de cuotas', store=True, copy=True, tracking=0, )
    date = fields.Date(string='Fecha de solicitud', store=True, copy=True, tracking=0, )
    description = fields.Char(string='Descripcion', store=True, copy=True, tracking=0, )
    financed = fields.Boolean(string='Financiado', store=True, copy=True, tracking=0, )
    horas_ejecutadas = fields.Float(string='Horas ejecutadas', readonly=True, tracking=0, )
    horas_facturables = fields.Float(string='Horas facturables', readonly=True, tracking=0, )
    initial_cuota = fields.Float(string='Cuota inicial', store=True, copy=True, tracking=0, )
    is_manager = fields.Boolean(string='¿Es gerente?', readonly=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='ordendeservicio_message_channel_ids_rel',
                                           column1='ordendeservicio_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='ordendeservicio_message_partner_ids_rel',
                                           column1='ordendeservicio_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    months_cuota = fields.Integer(string='Meses por cuota', store=True, copy=True, tracking=0, )
    mora_rate = fields.Float(string='Intereses por mora', store=True, copy=True, tracking=0, )
    move_ids = fields.Many2many(relation='ordendeservicio_move_ids_rel', column1='ordendeservicio_id',
                                column2='move_ids_id', string='Facturas', store=True, copy=True, tracking=0,
                                comodel_name='account.move', )
    nit_cliente = fields.Char(string='Nit cliente', store=True, readonly=True, tracking=0, )
    notes = fields.Char(string='Observaciones generales', store=True, copy=True, tracking=0, )
    pref_number = fields.Char(string='Orden de servicio', store=True, readonly=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.product', )
    programmer = fields.Many2one(string='Programador', store=True, copy=True, tracking=0,
                                 comodel_name='hr.employee', )
    project_id = fields.Many2one(string='Proyecto', store=True, copy=True, tracking=100,
                                 comodel_name='project.project', )
    project_value = fields.Float(string='Valor del proyecto', store=True, copy=True, tracking=0, )
    rate = fields.Float(string='Intereses', store=True, copy=True, tracking=0, )
    responsible = fields.Many2one(string='Responsable', store=True, copy=True, tracking=0,
                                  comodel_name='hr.employee', )
    sale_id = fields.Many2one(string='Pedido', store=True, copy=True, tracking=0, comodel_name='sale.order', )
    support = fields.Many2one(string='Soporte', store=True, copy=True, tracking=0,
                              comodel_name='project.service.order.support', )
    to_finance = fields.Float(string='Valor a Financiar', store=True, copy=True, tracking=0, )


class Pagarguiadeentrega(models.Model):
    _name = 'payment.delivery.guide'
    _description = 'Pagar guia de entrega'
    company_id = fields.Many2one(string='Compañia', store=True, readonly=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    payments_ids = fields.Many2many(relation='pagarguiadeentrega_payments_ids_rel', column1='pagarguiadeentrega_id',
                                    column2='payments_ids_id', string='Guias de entrega', store=True, copy=True,
                                    tracking=0,
                                    comodel_name='delivery.guide', )
    user_id = fields.Many2one(string='Usuario', store=True, readonly=True, copy=True, tracking=0,
                              comodel_name='res.users', )


class Páginadeldocumento(models.Model):
    _name = 'document.page'
    _description = 'Página del documento'
    active = fields.Boolean(string='Active', store=True, copy=True, tracking=0, )
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Next Activity Type', tracking=0, comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    backend_url = fields.Char(string='Backend URL', readonly=True, tracking=0, )
    company_id = fields.Many2one(string='Company', index=True, store=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    content_date = fields.Datetime(string='Last Contribution Date', index=True, store=True, readonly=True, tracking=0, )
    content_uid = fields.Many2one(string='Last Contributor', index=True, store=True, readonly=True, tracking=0,
                                  comodel_name='res.users', )
    content = fields.Text(string='Contenido', tracking=0, )
    draft_name = fields.Char(string='Nombre', tracking=0, )
    draft_summary = fields.Char(string='Resumen', tracking=0, )
    history_head = fields.Many2one(string='HEAD', store=True, readonly=True, tracking=0,
                                   comodel_name='document.page.history', )
    menu_id = fields.Many2one(string='Menú', store=True, readonly=True, copy=True, tracking=0,
                              comodel_name='ir.ui.menu', )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='pagarguiadeentrega_message_channel_ids_rel',
                                           column1='pagarguiadeentrega_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='Error de entrega del SMS', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='pagarguiadeentrega_message_partner_ids_rel',
                                           column1='pagarguiadeentrega_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    name = fields.Char(string='Título', store=True, required=True, copy=True, tracking=0, )
    parent_id = fields.Many2one(string='Categoría', store=True, copy=True, tracking=0, comodel_name='document.page', )
    process_id = fields.Many2one(string='Proceso', store=True, copy=True, tracking=0, comodel_name='audit.process', )
    template = fields.Html(string='Plantilla', store=True, copy=True, tracking=0, )


class Parserconfiguracion(models.Model):
    _name = 'account.banking.parser'
    _description = 'Parser Configuracion'
    account_pos = fields.Char(string='Posicion cuenta', store=True, copy=True, tracking=0, )
    amount_pos = fields.Char(string='Posicion valor', store=True, copy=True, tracking=0, )
    date_format = fields.Char(string='Formato de fecha', store=True, copy=True, tracking=0, )
    date_pos = fields.Char(string='Posicion fecha', store=True, copy=True, tracking=0, )
    journal_id = fields.Many2one(string='Journal', store=True, copy=True, tracking=0,
                                 comodel_name='account.journal', )
    line_len = fields.Integer(string='Largo de linea', store=True, copy=True, tracking=0, )
    match_dom = fields.Char(string='Dominio adicional', store=True, copy=True, tracking=0, )
    name_pos = fields.Char(string='Posicion comunicacion', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Formato de banco', store=True, copy=True, tracking=0, )
    ref_pos = fields.Char(string='Posicion referencia', store=True, copy=True, tracking=0, )
    separator = fields.Char(string='Separador', store=True, copy=True, tracking=0, )
    signal_bool = fields.Boolean(string='Signo fuera del valor', store=True, copy=True, tracking=0, )
    signal_declaration = fields.Char(string='Declaracion de signo', store=True, copy=True, tracking=0, )
    signal_position = fields.Char(string='Posicion signo', store=True, copy=True, tracking=0, )


class Partnerpaymentactiontypes(models.Model):
    _name = 'res.partner.payment.action.type'
    _description = 'Partner Payment Action Types'
    active = fields.Boolean(string='Activa', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañía', store=True, copy=True, tracking=0, comodel_name='res.company', )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Sequence', store=True, copy=True, tracking=0, )


class Payslipperiod(models.Model):
    _name = 'payslip.period'
    _description = 'Payslip period'
    closed = fields.Boolean(string='Cerrado', store=True, copy=True, tracking=0, )
    end_date = fields.Date(string='Fin de Corte', store=True, required=True, copy=True, tracking=0, )
    end_period = fields.Date(string='Fin del Periodo', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    start_date = fields.Date(string='Comienzo de Corte', store=True, required=True, copy=True, tracking=0, )
    start_period = fields.Date(string='Comienzo del Periodo', store=True, required=True, copy=True, tracking=0, )


class Periododenómina(models.Model):
    _name = 'hr.period'
    _description = 'Periodo de nómina'
    active = fields.Boolean(string='Activo', store=True, copy=True, tracking=0, )
    closed = fields.Boolean(string='Cerrado', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    end_date = fields.Date(string='Fin de Corte', store=True, required=True, copy=True, tracking=0, )
    end = fields.Date(string='Fin periodo', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, readonly=True, copy=True, tracking=0, )
    start_date = fields.Date(string='Comienzo de Corte', store=True, required=True, copy=True, tracking=0, )
    start = fields.Date(string='Inicio periodo', store=True, required=True, copy=True, tracking=0, )


class Permisoespecialtipo(models.Model):
    _name = 'permiso.especial.tipo'
    _description = 'Permiso especial tipo'
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Planilladeaportes(models.Model):
    _name = 'hr.contribution.form'
    _description = 'Planilla de aportes'
    branch_code = fields.Char(string='Código de sucursal', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    contract_group_id = fields.Many2one(string='Grupo de Contrato', store=True, copy=True, tracking=0,
                                        comodel_name='hr.contract.group', )
    contracts_ids = fields.Many2many(relation='planilladeaportes_contracts_ids_rel', column1='planilladeaportes_id',
                                     column2='contracts_ids_id', string='Contratos', store=True, tracking=0,
                                     comodel_name='hr.contract', )
    error_log = fields.Text(string='Errores', store=True, readonly=True, copy=True, tracking=0, )
    file_name = fields.Char(string='Nombre del Archivo', store=True, readonly=True, copy=True, tracking=0, )
    file_pila = fields.Binary(string='Archivo plano', store=True, readonly=True, copy=True, tracking=0, )
    journal_id = fields.Many2one(string='Diario', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='account.journal', )
    move_id = fields.Many2one(string='Asiento contable', store=True, readonly=True, copy=True, tracking=0,
                              comodel_name='account.move', )
    name = fields.Char(string='Nombre', store=True, readonly=True, copy=True, tracking=0, )
    period_id = fields.Many2one(string='Periodo', store=True, required=True, copy=True, tracking=0,
                                comodel_name='hr.period', )


class Políticadecontroldecrédito(models.Model):
    _name = 'credit.control.policy.changer'
    _description = 'Política de control de crédito'
    do_nothing = fields.Boolean(string='Sin política de seguimiento', store=True, copy=True, tracking=0, )
    move_line_ids = fields.Many2many(relation='planilladeaportes_move_line_ids_rel', column1='planilladeaportes_id',
                                     column2='move_line_ids_id', string='Apunte a cambiar', store=True, copy=True,
                                     tracking=0,
                                     comodel_name='account.move.line', )
    new_policy_id = fields.Many2one(string='Nueva política a aplicar', store=True, required=True, copy=True,
                                    tracking=0,
                                    comodel_name='credit.control.policy', )
    new_policy_level_id = fields.Many2one(string='Nuevo nivel a aplicar', store=True, required=True, copy=True,
                                          tracking=0, comodel_name='credit.control.policy.level', )


class Políticasdesladeserviciodeayuda(models.Model):
    _name = 'sh.helpdesk.sla'
    _description = 'Políticas de SLA de servicio de ayuda'
    company_id = fields.Many2one(string='Compañía', store=True, copy=True, tracking=0, comodel_name='res.company', )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    sh_days = fields.Integer(string='Días', store=True, required=True, copy=True, tracking=0, )
    sh_hours = fields.Integer(string='Horas', store=True, required=True, copy=True, tracking=0, )
    sh_minutes = fields.Integer(string='Minutos', store=True, required=True, copy=True, tracking=0, )
    sh_stage_id = fields.Many2one(string='Alcanzar la etapa', store=True, copy=True, tracking=0,
                                  comodel_name='helpdesk.stages', )
    sh_team_id = fields.Many2one(string='Equipo de servicio de ayuda', store=True, required=True, copy=True,
                                 tracking=0,
                                 comodel_name='helpdesk.team', )
    sh_ticket_type_id = fields.Many2one(string='Tipo de equipo de servicio de ayuda', store=True, copy=True,
                                        tracking=0,
                                        comodel_name='helpdesk.ticket.type', )
    sla_ticket_count = fields.Integer(string='Recuento de tickets de SLA', readonly=True, tracking=0, )


class Posiciónadicionaldedotación(models.Model):
    _name = 'quoter.dotation.additional.position'
    _description = 'Posición Adicional de Dotación'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    total_dotation_additional_position = fields.Float(string='Total Dotation Additional Position', store=True,
                                                      readonly=True, tracking=0, )


class Posicióndedotación(models.Model):
    _name = 'quoter.dotation.position'
    _description = 'Posición de Dotación'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    total_dotation_position = fields.Float(string='Total Dotation Position', store=True, readonly=True, tracking=0, )


class Posiciónpresupuestaria(models.Model):
    _name = 'account.budget.post'
    _description = 'Posición Presupuestaria'
    account_ids = fields.Many2many(relation='planilladeaportes_account_ids_rel', column1='planilladeaportes_id',
                                   column2='account_ids_id', string='Cuentas', store=True, copy=True, tracking=0,
                                   comodel_name='account.account', )
    company_id = fields.Many2one(string='Compañía', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Postgresqueriesfromodoointerface(models.Model):
    _name = 'querydeluxe'
    _description = 'Postgres queries from Odoo interface'
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Next Activity Type', tracking=0, comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    html = fields.Html(string='Html', store=True, copy=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='postgresqueriesfromo_message_channel_ids_rel',
                                           column1='postgresqueriesfromo_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='Error de entrega del SMS', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='postgresqueriesfromo_message_partner_ids_rel',
                                           column1='postgresqueriesfromo_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    name = fields.Text(string='Type a query :', store=True, copy=True, tracking=0, )
    raw_output = fields.Text(string='Raw output', store=True, copy=True, tracking=0, )
    rowcount = fields.Text(string='Rowcount', store=True, copy=True, tracking=0, )
    show_raw_output = fields.Boolean(string='Show the raw output of the query', store=True, copy=True, tracking=0, )
    tips_description = fields.Text(string='Description', readonly=True, tracking=0, )
    tips = fields.Many2one(string='Examples', store=True, copy=True, tracking=0, comodel_name='tipsqueries', )
    valid_query_name = fields.Text(string='Valid Query Name', store=True, copy=True, tracking=0, )
    x_descripcion = fields.Char(string='Descripcion Query', store=True, copy=True, tracking=0, )


class Prefactura(models.Model):
    _name = 'hr.roster.prefactura.line'
    _description = 'Prefactura'
    adicional = fields.Float(string='Costos adicionales', store=True, copy=True, tracking=0, )
    ays = fields.Float(string='A&S', store=True, copy=True, tracking=0, )
    city_id = fields.Many2one(string='Municipio', store=True, copy=True, tracking=0, comodel_name='res.city', )
    customer_id = fields.Many2one(string='Cliente', store=True, readonly=True, copy=True, tracking=0,
                                  comodel_name='res.partner', )
    dias_mes = fields.Float(string='Dias del mes', store=True, copy=True, tracking=0, )
    dias_resumen = fields.Char(string='Dias resumidos', store=True, copy=True, tracking=0, )
    dias = fields.Char(string='Dias', store=True, copy=True, tracking=0, )
    distribution = fields.Float(string='Distribucion', store=True, copy=True, tracking=0, )
    dom_diur = fields.Float(string='Hrs dom diurnas', store=True, copy=True, tracking=0, )
    dom_noct = fields.Float(string='Hrs dom nocturnas', store=True, copy=True, tracking=0, )
    duracion = fields.Integer(string='Duracion', store=True, copy=True, tracking=0, )
    fes_diur = fields.Float(string='Hrs fes diurnas', store=True, copy=True, tracking=0, )
    fes_noct = fields.Float(string='Hrs fes nocturnas', store=True, copy=True, tracking=0, )
    horario = fields.Char(string='Horario', store=True, copy=True, tracking=0, )
    horas_diurno = fields.Float(string='Horas diurnas', store=True, copy=True, tracking=0, )
    horas_nocturno = fields.Float(string='Horas nocturnas', store=True, copy=True, tracking=0, )
    interventor = fields.Many2one(string='Interventor', store=True, copy=True, tracking=0,
                                  comodel_name='res.partner', )
    mod_servicio = fields.Many2one(string='Linea de negocio', store=True, copy=True, tracking=0,
                                   comodel_name='project.linea.negocio', )
    modalidad_id = fields.Many2one(string='Modalidad', store=True, copy=True, tracking=0,
                                   comodel_name='hr.roster.modalidad', )
    move_ids = fields.Many2many(relation='prefactura_move_ids_rel', column1='prefactura_id', column2='move_ids_id',
                                string='Facturas', store=True, copy=True, tracking=0, comodel_name='account.move', )
    name = fields.Char(string='Descripcion', store=True, copy=True, tracking=0, )
    order_line_id = fields.Many2one(string='Linea OS', store=True, copy=True, tracking=0,
                                    comodel_name='project.service.order.line', )
    pref_number = fields.Char(string='Prefactura', store=True, readonly=True, tracking=0, )
    prefactura_id = fields.Many2one(string='Prefactura', store=True, copy=True, tracking=0,
                                    comodel_name='hr.roster.prefactura', )
    product_id = fields.Many2one(string='Servicio', store=True, copy=True, tracking=0,
                                 comodel_name='product.product', )
    programacion_id = fields.Many2one(string='Programacion', store=True, copy=True, tracking=0,
                                      comodel_name='hr.roster.programacion', )
    puesto_id = fields.Many2one(string='Puesto', store=True, copy=True, tracking=0, comodel_name='hr.roster.puesto', )
    puesto_int_code = fields.Char(string='Codigo interno del cliente', store=True, readonly=True, tracking=0, )
    puesto_int_zone = fields.Char(string='Zona interna del cliente', store=True, readonly=True, tracking=0, )
    quantity = fields.Float(string='Cantidad', store=True, copy=True, tracking=0, )
    regional_id = fields.Many2one(string='Regional', store=True, copy=True, tracking=0, comodel_name='res.regional', )
    service_quantity = fields.Float(string='Cantidad', store=True, copy=True, tracking=0, )
    subtotal = fields.Float(string='Subtotal antes de A&S', store=True, copy=True, tracking=0, )
    tipo_servicio = fields.Many2one(string='Tipo de servicio', store=True, copy=True, tracking=0,
                                    comodel_name='project.service.type', )
    total_ays = fields.Float(string='Total A&S', store=True, copy=True, tracking=0, )
    total_validated = fields.Float(string='Total validado', store=True, copy=True, tracking=0, )
    total = fields.Float(string='Total general', store=True, copy=True, tracking=0, )
    valor_total = fields.Float(string='Valor total', store=True, copy=True, tracking=0, )
    valor = fields.Float(string='Valor antes de A&S', store=True, copy=True, tracking=0, )


class Prefactura(models.Model):
    _name = 'hr.roster.prefactura'
    _description = 'Prefactura'
    amount_tax = fields.Float(string='Total impuestos', store=True, copy=True, tracking=0, )
    amount_total = fields.Float(string='Total', store=True, copy=True, tracking=0, )
    amount_untaxed = fields.Float(string='Subtotal', store=True, copy=True, tracking=0, )
    concept = fields.Many2one(string='Concepto', store=True, copy=True, tracking=0,
                              comodel_name='hr.roster.sale.concept', )
    customer_id = fields.Many2one(string='Cliente', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    date_prefactura = fields.Date(string='Fecha prefactura', store=True, copy=True, tracking=0, )
    pref_number = fields.Char(string='Prefactura', store=True, readonly=True, copy=True, tracking=0, )
    ref1 = fields.Char(string='Referencia', store=True, copy=True, tracking=0, )


class Prepagodesembolsoobligacionfinanciera(models.Model):
    _name = 'account.loan.prepaid'
    _description = 'Prepago Desembolso Obligacion Financiera'
    approve_date = fields.Date(string='Fecha de Aprobacion', store=True, readonly=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compania', store=True, readonly=True, tracking=0, comodel_name='res.company', )
    date = fields.Date(string='Fecha de Pago', store=True, readonly=True, required=True, copy=True, tracking=0, )
    description = fields.Text(string='Descripcion', store=True, copy=True, tracking=0, )
    loan_id = fields.Many2one(string='Obligacion Financiera', store=True, readonly=True, copy=True, tracking=0,
                              comodel_name='account.loan', )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='prepagodesembolsoobl_message_channel_ids_rel',
                                           column1='prepagodesembolsoobl_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='prepagodesembolsoobl_message_partner_ids_rel',
                                           column1='prepagodesembolsoobl_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    name = fields.Char(string='Codigo', store=True, readonly=True, copy=True, tracking=0, )
    numero_cuotas = fields.Integer(string='Cuotas a Modificar', store=True, readonly=True, copy=True, tracking=0, )
    value = fields.Float(string='Valor', store=True, readonly=True, required=True, copy=True, tracking=0, )


class Presupuesto(models.Model):
    _name = 'crossovered.budget'
    _description = 'Presupuesto'
    company_id = fields.Many2one(string='Compañía', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    creating_user_id = fields.Many2one(string='Responsable', store=True, copy=True, tracking=0,
                                       comodel_name='res.users', )
    date_from = fields.Date(string='Fecha de inicio', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Cuenta de adjunto', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='presupuesto_message_channel_ids_rel', column1='presupuesto_id',
                                           column2='message_channel_ids_id', string='Seguidores (Canales)',
                                           readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Error en la entrega del mensaje', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Es Seguidor', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Adjunto principal', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Acción necesaria', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='presupuesto_message_partner_ids_rel', column1='presupuesto_id',
                                           column2='message_partner_ids_id', string='Seguidores (Contactos)',
                                           readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Contador de Mensajes no Leídos', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Mensajes no leídos', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre del Presupuesto', store=True, required=True, copy=True, tracking=0, )


class Prioridaddeserviciodeayuda(models.Model):
    _name = 'helpdesk.priority'
    _description = 'Prioridad de servicio de ayuda'
    color = fields.Char(string='Color', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )


class Procesamientodenómina(models.Model):
    _name = 'hr.payslip.processing'
    _description = 'Procesamiento de Nómina'
    accounting_date = fields.Date(string='Fecha de Contabilización', store=True, required=True, copy=True,
                                  tracking=0, )
    approval_managers = fields.Boolean(string='Gestores de Aprobación', readonly=True, tracking=0, )
    bank_id = fields.Many2one(string='Banco', store=True, copy=True, tracking=0, comodel_name='res.bank', )
    company_id = fields.Many2one(string='Compañia', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    contract_group_id = fields.Many2one(string='Grupo de Contrato', store=True, copy=True, tracking=0,
                                        comodel_name='hr.contract.group', )
    contracts_ids = fields.Many2many(relation='prioridaddeserviciod_contracts_ids_rel',
                                     column1='prioridaddeserviciod_id', column2='contracts_ids_id', string='Contratos',
                                     store=True, tracking=0, comodel_name='hr.contract', )
    error_log = fields.Text(string='Errores', store=True, readonly=True, copy=True, tracking=0, )
    journal_id = fields.Many2one(string='Diario', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='account.journal', )
    liquidation_date = fields.Date(string='Fecha de Liquidación', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, tracking=0, )
    payslip_type_id = fields.Many2one(string='Tipo de Nómina', store=True, required=True, copy=True, tracking=0,
                                      comodel_name='hr.payslip.type', )
    period_id = fields.Many2one(string='Periodo', store=True, required=True, copy=True, tracking=0,
                                comodel_name='hr.period', )
    provisions_processing_id = fields.Many2one(string='Provisiones', store=True, readonly=True, copy=True, tracking=0,
                                               comodel_name='hr.payslip.processing', )
    x_correo = fields.Boolean(string='Correo Enviado', store=True, copy=True, tracking=1, )


class Processdiandocument(models.Model):
    _name = 'process.dian.document'
    _description = 'Process DIAN document'
    dian_ids = fields.Many2many(relation='processdiandocument_dian_ids_rel', column1='processdiandocument_id',
                                column2='dian_ids_id', string='Dian Documents', store=True, copy=True, tracking=0,
                                comodel_name='account.move.dian.document', )


class ProcessHrDianDocument(models.Model):
    _name = 'process.hr.dian.document'
    _description = 'Process DIAN document'
    dian_ids = fields.Many2many(relation='process_hr_dian_docu_dian_ids_rel', column1='process_hr_dian_docu_id',
                                column2='dian_ids_id', string='Dian Documents', store=True, copy=True, tracking=0,
                                comodel_name='hr.payslip.dian.document', )


class Processpayslip(models.Model):
    _name = 'process.hr.payslip'
    _description = 'Process Payslip'
    dian_ids = fields.Many2many(relation='processpayslip_dian_ids_rel', column1='processpayslip_id',
                                column2='dian_ids_id', string='Nominas', store=True, copy=True, tracking=0,
                                comodel_name='hr.payslip', )


class Processserviceorder(models.Model):
    _name = 'validate.service.order'
    _description = 'Process Service ORder'
    order_ids = fields.Many2many(relation='processserviceorder_order_ids_rel', column1='processserviceorder_id',
                                 column2='order_ids_id', string='Ordenes', store=True, copy=True, tracking=0,
                                 comodel_name='project.service.order', )


class Processserviceorderline(models.Model):
    _name = 'validate.service.order.line'
    _description = 'Process Service Order Line'
    order_ids = fields.Many2many(relation='processserviceorderl_order_ids_rel', column1='processserviceorderl_id',
                                 column2='order_ids_id', string='Lineas de Ordenes', store=True, copy=True, tracking=0,
                                 comodel_name='project.service.order.line', )


class Programa(models.Model):
    _name = 'programa'
    _description = 'Programa'
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Programacion(models.Model):
    _name = 'hr.roster.programacion'
    _description = 'Programación'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string='Nombre', required=True, copy=True, tracking=True)
    cliente_contract_id = fields.Many2one('project.project', string='Proyecto', required=True, copy=True)
    cliente_id = fields.Many2one('res.partner', string='Cliente', readonly=True, tracking=True)
    employee_id = fields.Many2one('hr.employee', string='Encargado', required=True, copy=True)
    programmer = fields.Many2one('hr.employee', string='Programador', copy=True)
    modalidad_id = fields.Many2one('hr.roster.modalidad', string='Modalidad destino', copy=True)
    modalidad_id_dob = fields.Many2one('hr.roster.modalidad', string='Modalidad destino (doblaje)', copy=True)
    tipo_turno_id = fields.Many2one('hr.roster.horario', string='Tipo de turno', copy=True)
    tipo_turno_id_dob = fields.Many2one('hr.roster.horario', string='Tipo de turno (doblaje)', copy=True)
    order_line_id = fields.Many2one('project.service.order.line', string='Línea de OS', copy=True)
    massive_shift_id = fields.Many2one('massive.shift.scheduling', string='Programación masiva', copy=True)
    contract_date = fields.Date(string='Fecha objetivos', copy=True)
    desc_date = fields.Date(string='Fecha objetivo (descanso)', copy=True)
    disp_date = fields.Date(string='Fecha objetivo (disponibles)', copy=True)
    dobl_date = fields.Date(string='Fecha objetivo (doblaje)', copy=True)
    contratado = fields.Boolean(string='Contrato vigente', copy=True)
    d_disponibles = fields.Boolean(string='Disponibles', copy=True)
    descanso = fields.Boolean(string='Empleados en descanso', copy=True)
    doblaje = fields.Boolean(string='Empleados para doblar', copy=True)
    sin_prog = fields.Boolean(string='Sin programación', copy=True)
    todos = fields.Boolean(string='Todos los empleados', copy=True)
    year = fields.Integer(string='Año', required=True, copy=True)
    qty_employees = fields.Integer(string='Personal asignado', readonly=True)
    billed_diurn_hours = fields.Float(string='Horas diurnas facturadas', readonly=True)
    billed_nocturn_hours = fields.Float(string='Horas nocturnas facturadas', readonly=True)
    billed_hours = fields.Float(string='Total horas facturadas', readonly=True)
    scheduled_diurn_hours = fields.Float(string='Horas diurnas programadas', readonly=True)
    scheduled_nocturn_hours = fields.Float(string='Horas nocturnas programadas', readonly=True)
    scheduled_hours = fields.Float(string='Total horas programadas', readonly=True)
    disponibles = fields.Char(string='Disponibles (texto)', copy=True)
    notification_text = fields.Text(string='Notificación de ausencias no adjuntas', readonly=True)
    leave_turn_ids = fields.Many2many('hr.leave', relation='hr_roster_prog_leave_turn_rel', column1='programacion_id',
                                      column2='leave_id', string='Ausencias', readonly=True)
    not_assigned_leaves = fields.Many2many('hr.leave', relation='hr_roster_prog_leave_unassigned_rel',
                                           column1='programacion_id', column2='leave_id',
                                           string='Ausencias no asignadas', copy=True)


class Programacionesmasivas(models.Model):
    _name = 'massive.shift.scheduling'
    _description = 'Programaciones masivas'
    employee_id = fields.Many2one(string='Encargado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    modality_id = fields.Many2one(string='Modalidad', store=True, copy=True, tracking=0,
                                  comodel_name='hr.roster.modalidad', )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    order_id = fields.Many2one(string='Orden de servicio', store=True, copy=True, tracking=0,
                               comodel_name='project.service.order', )
    project_id = fields.Many2one(string='Proyecto', store=True, copy=True, tracking=0,
                                 comodel_name='project.project', )
    service_line_ids = fields.Many2many(relation='programacionesmasiva_service_line_ids_rel',
                                        column1='programacionesmasiva_id', column2='service_line_ids_id',
                                        string='Linea de servicio', store=True, copy=True, tracking=0,
                                        comodel_name='project.service.order.line', )


class Programacionlinerun(models.Model):
    _name = 'hr.programacion.line.run'
    _description = 'Programacion Line Run'
    line_ids = fields.Many2many(relation='programacionlinerun_line_ids_rel', column1='programacionlinerun_id',
                                column2='line_ids_id', string='Programacion Line', store=True, copy=True, tracking=0,
                                comodel_name='hr.roster.programacion.line', )
    n_times = fields.Integer(string='N Times', store=True, copy=True, tracking=0, )


class Prórrogadecontrato(models.Model):
    _name = 'hr.contract.extension'
    _description = 'Prórroga de Contrato'
    contract_id = fields.Many2one(string='Contrato', store=True, copy=True, tracking=0, comodel_name='hr.contract', )
    date_from = fields.Date(string='Fecha de Inicio Prórroga', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha de Fin Prórroga', store=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Numero de Prórroga', store=True, copy=True, tracking=0, )


class Proteccióndedotación(models.Model):
    _name = 'quoter.dotation.protection'
    _description = 'Protección de dotación'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    total_dotation_protection = fields.Float(string='Total Dotation Protection', store=True, readonly=True,
                                             tracking=0, )


class Proveedorgeo(models.Model):
    _name = 'base.geo_provider'
    _description = 'Proveedor Geo'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    tech_name = fields.Char(string='Nombre Técnico', store=True, copy=True, tracking=0, )


class Publicholidays(models.Model):
    _name = 'hr.holiday.public'
    _description = 'Public holidays'
    name = fields.Char(string='Holiday', store=True, required=True, copy=True, tracking=0, )


class Puesto(models.Model):
    _name = 'hr.roster.puesto'
    _description = 'Puesto'
    analytic_account_id = fields.Many2one(string='Cuenta analitica', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    aplica_adicional_nocturno_dom_fes = fields.Boolean(string='Aplica adicional nocturno dominical festivo',
                                                       readonly=True,
                                                       tracking=0, )
    cliente_contract_id = fields.Many2one(string='Contrato', store=True, required=True, copy=True, tracking=0,
                                          comodel_name='project.project', )
    code = fields.Char(string='Codigo', store=True, copy=True, tracking=0, )
    concat_name = fields.Char(string='Info Puesto', store=True, readonly=True, tracking=0, )
    devengado = fields.Float(string='Devengado', store=True, copy=True, tracking=0, )
    direccion = fields.Char(string='Direccion', store=True, copy=True, tracking=0, )
    fecha_inst = fields.Datetime(string='Fecha de instalacion', store=True, copy=True, tracking=0, )
    heyrec = fields.Float(string='HEYREC', store=True, copy=True, tracking=0, )
    induction_days = fields.Integer(string='Dias Induccion', store=True, copy=True, tracking=0, )
    int_code = fields.Char(string='Codigo interno del cliente', store=True, copy=True, tracking=0, )
    int_zone = fields.Char(string='Codigo zona del cliente', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, readonly=True, tracking=0, )
    risk_id = fields.Many2one(string='Riesgo', store=True, copy=True, tracking=0, comodel_name='hr.contract.risk', )
    valor_mensual_horas = fields.Float(string='Valor mensual de horas', store=True, copy=True, tracking=0, )
    x_city_id = fields.Many2one(string='Municipio', tracking=0, comodel_name='res.city', )
    x_partner_id = fields.Many2one(string='Cliente', store=True, tracking=1, comodel_name='res.partner', )
    x_regional_id = fields.Many2one(string='Regional', tracking=0, comodel_name='res.regional', )
    x_sede = fields.Char(string='Sede', tracking=0, )


class Rangodefechas(models.Model):
    _name = 'date.range'  # si tienes OCA base_date_range, usa: _inherit = 'date.range'
    _description = 'Rango de fechas'
    _order = 'date_start asc, date_end asc'
    active = fields.Boolean(string='Activo', default=True)
    name = fields.Char(string='Nombre', required=True, copy=True, index=True)
    company_id = fields.Many2one('res.company', string='Compañía', index=True, default=lambda self: self.env.company,
                                 ondelete='restrict')
    type_id = fields.Many2one('date.range.type', string='Tipo', required=True, index=True, ondelete='restrict')
    type_name = fields.Char(string='Tipo (nombre)', related='type_id.name', store=True, readonly=True)
    date_start = fields.Date(string='Fecha de inicio', required=True, copy=True)
    date_end = fields.Date(string='Fecha final', required=True, copy=True)
    change_id = fields.Many2one('change.difference', string='Generador de Diferencia en Cambio', ondelete='set null')
    year_id = fields.Many2one('account.fiscal.year', string='Año Fiscal', ondelete='set null')

    @api.constrains('date_start', 'date_end', 'type_id', 'company_id', 'active')
    def _check_overlap(self):
        """Evita solapamientos de rangos activos para el mismo Tipo y Compañía."""
        for rec in self:
            if not (rec.date_start and rec.date_end and rec.type_id):
                continue
            domain = [
                ('id', '!=', rec.id),
                ('type_id', '=', rec.type_id.id),
                ('company_id', '=', rec.company_id.id),
                ('active', '=', True),
                ('date_start', '<=', rec.date_end),
                ('date_end', '>=', rec.date_start),
            ]
            if self.search_count(domain):
                raise ValidationError(_(
                    'El rango se sobrepone con otro rango activo del mismo Tipo y Compañía.'
                ))


class Reclamacion(models.Model):
    _name = 'crm.claim'
    _description = 'Reclamación'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date desc, id desc'
    active = fields.Boolean(string='Activo', default=True)
    name = fields.Char(string='Objeto de la reclamación', required=True, copy=True, tracking=True)
    company_id = fields.Many2one('res.company', string='Compañía', index=True, default=lambda self: self.env.company,
                                 ondelete='restrict')
    date = fields.Datetime(string='Fecha de Reclamación', index=True, default=fields.Datetime.now, copy=True,
                           tracking=True)
    date_deadline = fields.Date(string='Fecha límite', copy=True)
    date_closed = fields.Datetime(string='Cerrada', readonly=True, copy=False)
    stage_id = fields.Many2one('crm.claim.stage', string='Etapa', tracking=3, ondelete='restrict')
    categ_id = fields.Many2one('crm.claim.category', string='Categoría', copy=True, ondelete='set null')
    team_id = fields.Many2one('crm.team', string='Equipo de ventas', index=True, copy=True, ondelete='set null')
    user_id = fields.Many2one('res.users', string='Responsable', copy=True, tracking=True, ondelete='set null')
    partner_id = fields.Many2one('res.partner', string='Empresa', copy=True, ondelete='set null')
    partner_phone = fields.Char(string='Teléfono', copy=True)
    email_from = fields.Char(string='Email', copy=True)
    email_cc = fields.Text(string='Emails en copia', copy=True)
    description = fields.Text(string='Descripción', copy=True)
    cause = fields.Text(string='Causa principal', copy=True)
    resolution = fields.Text(string='Resolución', copy=True)
    user_fault = fields.Char(string='Responsable problema', copy=True)


class Reconciliarlineas(models.TransientModel):
    _name = 'account.move.line.reconcile'
    _description = 'Reconciliar líneas'

    company_id = fields.Many2one('res.company', string='Compañía', default=lambda self: self.env.company, readonly=True)
    lines_ids = fields.Many2many('account.move.line', relation='aml_reconcile_wiz_rel', column1='wizard_id',
                                 column2='line_id', string='Líneas', copy=False,
                                 domain="[('company_id','=',company_id),"
                                        " ('move_id.state','=','posted'),"
                                        " ('reconciled','=',False),"
                                        " ('account_id.reconcile','=',True)]")

    # def action_reconcile(self):
    #     """Conciliar las líneas seleccionadas (misma cuenta/compañía y publicadas)."""
    #     for wiz in self:
    #         lines = wiz.lines_ids
    #         if len(lines) < 2:
    #             raise UserError(_('Seleccione al menos dos líneas.'))
    #         if len(lines.mapped('company_id')) > 1:
    #             raise UserError(_('Todas las líneas deben ser de la misma compañía.'))
    #         if len(lines.mapped('account_id')) > 1:
    #             raise UserError(_('Todas las líneas deben pertenecer a la misma cuenta.'))
    #         if any(not acc.reconcile for acc in lines.mapped('account_id')):
    #             raise UserError(_('La cuenta debe tener activada la opción "Permitir conciliación".'))
    #         if any(m.state != 'posted' for m in lines.mapped('move_id')):
    #             raise UserError(_('Todas las líneas deben pertenecer a asientos publicados.'))
    #
    #         # Ejecuta conciliación (evita diferencias por cambio si no las quieres crear aquí)
    #         lines.with_context(no_exchange_difference=True).reconcile()
    #
    #     return {'type': 'ir.actions.act_window_close'}


class Recordatoriodetickets(models.Model):
    _name = 'sh.ticket.alarm'
    _description = 'Recordatorio de tickets'
    _order = 'sh_remind_before asc, id asc'
    company_id = fields.Many2one('res.company', string='Compañía', default=lambda self: self.env.company, index=True,
                                 ondelete='restrict')
    name = fields.Char(string='Nombre', readonly=True, default='/', copy=False, tracking=True)
    sh_remind_before = fields.Integer(string='Recordatorio antes', copy=True,
                                      help='Tiempo de anticipación para el recordatorio (minutos).')


class Referencias(models.Model):
    _name = 'hr.referencias'
    _description = 'Referencias'
    _order = 'name asc, id asc'

    name = fields.Char(string='Nombre', required=True, copy=True, index=True)
    referencias_id = fields.Many2one('hr.employee', string='Empleado', required=True, copy=True, index=True,
                                     ondelete='cascade')
    rela = fields.Char(string='Relación', required=True, copy=True)
    tele = fields.Char(string='Teléfono', required=True, copy=True,
                       help='Incluye indicativo si aplica (ej. +57 300 123 4567).'
                       )


class Regional(models.Model):
    _name = 'res.regional'
    _description = 'Regional'
    name = fields.Char(string='Regional', store=True, copy=True, tracking=0, )
    x_branch_id = fields.Many2one(string='Sucursal', store=True, copy=True, tracking=1, comodel_name='hr.branch', )
    x_kactus = fields.Char(string='Código Kactus', store=True, copy=True, tracking=1, )


class Reglasdepreciosdeentrega(models.Model):
    _name = 'delivery.price.rule'
    _description = 'Reglas de precios de entrega'
    carrier_id = fields.Many2one(string='Transportista', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='delivery.carrier', )
    list_base_price = fields.Float(string='Precio de venta base', store=True, required=True, copy=True, tracking=0, )
    list_price = fields.Float(string='Precio de venta', store=True, required=True, copy=True, tracking=0, )
    max_value = fields.Float(string='Valor máximo', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', readonly=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, required=True, copy=True, tracking=0, )


class Reportexcelavancys(models.Model):
    _name = 'excel.report.avancys'
    _description = 'Report Excel Avancys'
    excel_file = fields.Binary(string='Reporte Excel', store=True, copy=True, tracking=0, )
    file_name = fields.Char(string='Archivo Excel', store=True, copy=True, tracking=0, )


class Requerimientodecompra(models.Model):
    _name = 'purchase.requisition'  # si existe en core, usa: _inherit = 'purchase.requisition'
    _description = 'Requerimiento de Compra'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc, id desc'

    # Identificación
    name = fields.Char(string='Referencia', default='/', readonly=True, copy=False, tracking=True)

    # Organización / moneda
    company_id = fields.Many2one('res.company', string='Compañía', required=True, index=True,
                                 default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', string='Moneda', related='company_id.currency_id', store=True,
                                  readonly=True)
    type_id = fields.Many2one('purchase.requisition.type', string='Tipo de acuerdo de compra',
                              required=True, ondelete='restrict')
    picking_type_id = fields.Many2one('stock.picking.type', string='Tipo de operación', required=True,
                                      ondelete='restrict',
                                      domain="[('warehouse_id.company_id','=',company_id)]")
    warehouse_id = fields.Many2one('stock.warehouse', string='Almacén', ondelete='set null',
                                   domain="[('company_id','=',company_id)]")
    user_id = fields.Many2one('res.users', string='Usuario', default=lambda self: self.env.user, ondelete='set null')
    vendor_id = fields.Many2one('res.partner', string='Proveedor', domain="[('supplier_rank','>',0)]",
                                ondelete='set null')
    regional_id = fields.Many2one('res.regional', string='Sucursal', ondelete='set null')
    analytic_account_id = fields.Many2one('account.analytic.account', string='Cuenta Analítica', ondelete='set null')
    commercial_distribution_id = fields.Many2one('account.commercial.distribution', string='Justificación',
                                                 ondelete='set null')
    project_distribution_id = fields.Many2one('project.distribution', string='D. Proyecto', ondelete='set null')
    product_id = fields.Many2one('product.product', string='Producto', ondelete='set null')
    ordering_date = fields.Date(string='Fecha del Pedido', default=fields.Date.context_today, copy=True, tracking=True)
    schedule_date = fields.Date(string='Fecha de entrega', index=True, copy=True)
    date_end = fields.Datetime(string='Fecha límite', copy=True)
    origin = fields.Char(string='Documento Origen', copy=True)
    description = fields.Text(string='Descripción', copy=True)
    order_count = fields.Integer(string='Número de órdenes', readonly=True)
    x_employee_parent_id = fields.Many2one('res.users', string='Responsable', readonly=True)
    x_PD6359049686730481 = fields.Many2one('res.city', string='Ciudad', ondelete='set null')


class Resoluciondefacturacionelectronica(models.Model):
    _name = 'electronic.invoice.resolution'
    _description = 'Resolucion de Facturacion Electronica'
    company_id = fields.Many2one(string='Company', index=True, store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    description = fields.Text(string='Texto de Resolución', store=True, copy=True, tracking=0, )
    from_number = fields.Integer(string='Numeración Desde', store=True, tracking=0, )
    id_param = fields.Integer(string='ID Resolución', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    number = fields.Char(string='Número de Resolución', store=True, copy=True, tracking=0, )
    prefix = fields.Char(string='Prefijo', store=True, required=True, copy=True, tracking=0, )
    technical_key = fields.Char(string='Clave Técnica', store=True, tracking=0, )
    to_number = fields.Integer(string='Numeración Hasta', store=True, tracking=0, )
    valid_date_from = fields.Date(string='Fecha Inicio Resolución', store=True, tracking=0, )
    valid_date_to = fields.Date(string='Fecha Fin Resolución', store=True, tracking=0, )


class ResponsabilidadesfiscalesPartytaxscheme(models.Model):
    _name = 'account.fiscal.position.party.tax.scheme'
    _description = 'Responsabilidades Fiscales (PartyTaxScheme)'
    code = fields.Char(string='Código', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class ResponsabilidadesfiscalesTaxlevelcode(models.Model):
    _name = 'account.fiscal.position.tax.level.code'
    _description = 'Responsabilidades Fiscales (TaxLevelCode)'
    code = fields.Char(string='Código', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class Respuestarapida(models.Model):
    _name = 'sh.quick.reply'
    _description = 'Respuesta rápida'
    _order = 'commom_for_all desc, name asc, id asc'

    active = fields.Boolean(string='Activo', default=True)

    # Nota: dejo el nombre del campo tal cual (commom_for_all) para no romper datos existentes
    commom_for_all = fields.Boolean(
        string='Común para todos',
        help='Si está activo, la respuesta estará disponible para todos los usuarios.'
    )

    name = fields.Char(string='Título', required=True, copy=True, index=True)
    sh_description = fields.Html(string='Cuerpo', copy=True)

    # No la marco como required: solo exigimos usuario cuando NO es común
    sh_user_id = fields.Many2one(
        'res.users',
        string='Usuario',
        default=lambda self: self.env.user,
        ondelete='set null',
        help='Usuario propietario cuando la respuesta NO es común.'
    )


class Restablecercuentadecalendariodegoogle(models.Model):
    _name = 'google.calendar.account.reset'
    _description = 'Restablecer cuenta de Calendario de Google'
    user_id = fields.Many2one(string='Usuario', store=True, required=True, copy=True, tracking=0,
                              comodel_name='res.users', )


class Resumendelíneasdefactura(models.Model):
    _name = 'account.move.summary.line'
    _description = 'Resumen de Líneas de Factura'
    company_id = fields.Many2one(string='Compañía', store=True, readonly=True, tracking=0, comodel_name='res.company', )
    cost_price = fields.Float(string='Precio de Coste', store=True, copy=True, tracking=0, )
    currency_id = fields.Many2one(string='Moneda', store=True, required=True, copy=True, tracking=0,
                                  comodel_name='res.currency', )
    discount = fields.Float(string='Descuento (%)', store=True, copy=True, tracking=0, )
    move_id = fields.Many2one(string='Asiento contable', index=True, store=True, readonly=True, required=True,
                              copy=True,
                              tracking=0, comodel_name='account.move', )
    name = fields.Char(string='Etiqueta', store=True, copy=True, tracking=100, )
    price_subtotal = fields.Monetary(string='Subtotal', store=True, readonly=True, copy=True, tracking=0, )
    price_total = fields.Monetary(string='Total', store=True, readonly=True, copy=True, tracking=0, )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.product', )
    product_uom_category_id = fields.Many2one(string='Categoría', readonly=True, tracking=0,
                                              comodel_name='uom.category', )
    product_uom_id = fields.Many2one(string='Unidad de Medida', store=True, copy=True, tracking=0,
                                     comodel_name='uom.uom', )
    quantity = fields.Float(string='Cantidad', store=True, copy=True, tracking=0, )
    reference_price = fields.Float(string='Precio de Referencia', store=True, copy=True, tracking=0, )
    tax_ids = fields.Many2many(relation='restablecercuentadec_tax_ids_rel', column1='restablecercuentadec_id',
                               column2='tax_ids_id', string='Impuestos', store=True, copy=True, tracking=0,
                               comodel_name='account.tax', )


class Retencionescalculadasprocedimiento2(models.Model):
    _name = 'hr.contract.withholding.log'
    _description = 'Retenciones Calculadas Procedimiento 2'
    contract_id = fields.Many2one(string='Contrato', store=True, copy=True, tracking=0, comodel_name='hr.contract', )
    name = fields.Char(string='Descripción', store=True, copy=True, tracking=0, )
    value = fields.Char(string='Detalle', store=True, copy=True, tracking=0, )


class Rh(models.Model):
    _name = 'hr.employee.rh'
    _description = 'RH'
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Riesgolaboral(models.Model):
    _name = 'hr.contract.risk'
    _description = 'Riesgo Laboral'
    ciiu_id = fields.Many2one(string='CIIU', store=True, copy=True, tracking=0, comodel_name='res.ciiu', )
    name = fields.Char(string='Riesgo', store=True, copy=True, tracking=0, )
    risk_percentage = fields.Float(string='Porcentaje de Riesgo', store=True, copy=True, tracking=0, )
    sub_activity = fields.Char(string='Sub actividad economica', store=True, copy=True, tracking=0, )


class Salequoter(models.Model):
    _name = 'sale.quoter'
    _description = 'Sale Quoter'
    accumulated_interest_service = fields.Float(string='Intereses acumulados', store=True, copy=True, tracking=0, )
    accumulated_interest_technology = fields.Float(string='Acumulacion de Interes', store=True, copy=True,
                                                   tracking=0, )
    activity_date_deadline = fields.Date(string='Plazo de la próxima actividad', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Resumen de la siguiente actividad', tracking=0, )
    activity_type_icon = fields.Char(string='Icono de estado de actividad', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Siguiente tipo de actividad', tracking=0,
                                       comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    additional_value_1 = fields.Float(string='Valor Adicional 1', store=True, copy=True, tracking=0, )
    additional_value_2 = fields.Float(string='Valor Adicional 2', store=True, copy=True, tracking=0, )
    additional_value_3 = fields.Float(string='Valor Adicional 3', store=True, copy=True, tracking=0, )
    additionals_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    additionals_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    additionals_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    additionals_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    administration_expenses_month = fields.Float(string='Gastos Administración', readonly=True, tracking=0, )
    administration_expenses_percentage = fields.Float(string='Gastos Administración porcentaje', readonly=True,
                                                      tracking=0, )
    administration_expenses_total = fields.Float(string='Gastos Administración total', readonly=True, tracking=0, )
    bool_generate_quoter = fields.Boolean(string='generate_quoter', readonly=True, tracking=100, )
    canine_month = fields.Float(string='Caninos', readonly=True, tracking=0, )
    canine_percentage = fields.Float(string='Caninos porcentaje', readonly=True, tracking=0, )
    canine_total = fields.Float(string='Caninos total', readonly=True, tracking=0, )
    claims_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    claims_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    claims_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    claims_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    commercial_distribution_id = fields.Many2one(string='Tarifa de Servicio', store=True, copy=True, tracking=100,
                                                 comodel_name='account.commercial.distribution', )
    communication_current = fields.Float(string='Comunicación', readonly=True, tracking=0, )
    communication_month = fields.Float(string='Comunicación', readonly=True, tracking=0, )
    communication_percentage = fields.Float(string='Comunicación porcentaje', readonly=True, tracking=0, )
    communication_total = fields.Float(string='Comunicación total', readonly=True, tracking=0, )
    consulting_commission_month = fields.Float(string='Comisión Consultor', readonly=True, tracking=0, )
    consulting_commission_percentage = fields.Float(string='Comisión Consultor porcentaje', readonly=True, tracking=0, )
    consulting_commission_total = fields.Float(string='Comisión Consultor total', readonly=True, tracking=0, )
    contract_value = fields.Float(string='Valor Contrato', readonly=True, tracking=0, )
    count_sale = fields.Integer(string='cont sale', readonly=True, tracking=0, )
    date_end = fields.Date(string='Fecha Finalización del Contrato', store=True, copy=True, tracking=100, )
    date_start = fields.Date(string='Fecha Inicio del Contrato', store=True, copy=True, tracking=100, )
    date = fields.Date(string='Fecha', store=True, copy=True, tracking=100, )
    dedication_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    dedication_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    dedication_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    dedication_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    direct_tax_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    direct_tax_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    direct_tax_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    direct_tax_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    dotation_current = fields.Float(string='Dotacion total', readonly=True, tracking=0, )
    dotation_month = fields.Float(string='Dotacion', readonly=True, tracking=0, )
    dotation_percentage = fields.Float(string='Dotacion porcentaje', readonly=True, tracking=0, )
    dotation_pos_current = fields.Float(string='Dotacion total', readonly=True, tracking=0, )
    dotation_pos_month = fields.Float(string='Dotacion', readonly=True, tracking=0, )
    dotation_pos_percentage = fields.Float(string='Dotacion porcentaje', readonly=True, tracking=0, )
    dotation_pos_total = fields.Float(string='Dotacion total', readonly=True, tracking=0, )
    dotation_total = fields.Float(string='Dotacion total', readonly=True, tracking=0, )
    duration_months_current = fields.Float(string='Meses al 31/12', readonly=True, tracking=100, )
    duration_months = fields.Float(string='Meses Contrato', readonly=True, tracking=100, )
    duration_years = fields.Float(string='Duracion años', readonly=True, tracking=100, )
    ebtax_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    ebtax_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    ebtax_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    ebtax_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    expedition_expense = fields.Float(string='Gastos de expedició', store=True, copy=True, tracking=0, )
    finantial_cost_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    finantial_cost_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    finantial_cost_payment_term = fields.Float(string='Costos financieros plazo de pago', readonly=True, tracking=100, )
    finantial_cost_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    finantial_cost_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    fp_month = fields.Float(string='5p', readonly=True, tracking=0, )
    fp_percentage = fields.Float(string='5p porcentaje', readonly=True, tracking=0, )
    fp_total = fields.Float(string='5p total', readonly=True, tracking=0, )
    hseq_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    hseq_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    hseq_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    hseq_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    income_current = fields.Float(string='Ingreso', readonly=True, tracking=0, )
    income_month = fields.Float(string='Ingreso', readonly=True, tracking=0, )
    income_percentage = fields.Float(string='Ingreso porcentaje', readonly=True, tracking=0, )
    income_tax_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    income_tax_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    income_tax_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    income_tax_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    income_total = fields.Float(string='Ingreso total', readonly=True, tracking=0, )
    interest_financing_month = fields.Float(string='Intereses Financiación', readonly=True, tracking=0, )
    interest_financing_percentage = fields.Float(string='Intereses Financiación porcentaje', readonly=True,
                                                 tracking=0, )
    interest_financing_tec_month = fields.Float(string='Intereses Financiación Tec', readonly=True, tracking=0, )
    interest_financing_tec_percentage = fields.Float(string='Intereses Financiación Tec porcentaje', readonly=True,
                                                     tracking=0, )
    interest_financing_tec_total = fields.Float(string='Intereses Financiación Tec total', readonly=True, tracking=0, )
    interest_financing_total = fields.Float(string='Intereses Financiación total', readonly=True, tracking=0, )
    life_insurance = fields.Float(string='Prima seguro vida', store=True, readonly=True, tracking=0, )
    loan_service = fields.Float(string='Prestamo', readonly=True, tracking=0, )
    loan_technology = fields.Float(string='Prestamo', readonly=True, tracking=0, )
    manager_commission_month = fields.Float(string='Comisión Gerente DN', readonly=True, tracking=0, )
    manager_commission_percentage = fields.Float(string='Comisión Gerente DN porcentaje', readonly=True, tracking=0, )
    manager_commission_total = fields.Float(string='Comisión Gerente DN total', readonly=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Número de archivos adjuntos', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='salequoter_message_channel_ids_rel', column1='salequoter_id',
                                           column2='message_channel_ids_id', string='Seguidores (Canales)',
                                           readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Número de errores', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Mensaje error de entrega', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Es Seguidor', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Adjunto principal', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Acción necesaria', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='salequoter_message_partner_ids_rel', column1='salequoter_id',
                                           column2='message_partner_ids_id', string='Seguidores (Terceros)',
                                           readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Contador de mensajes sin leer', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Mensajes sin Leer', readonly=True, tracking=0, )
    month_value = fields.Float(string='Valor mes', readonly=True, tracking=100, )
    my_activity_date_deadline = fields.Date(string='Fecha límite de mi actividad', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=100, )
    net_income_month = fields.Float(string='Ingresos netos', readonly=True, tracking=0, )
    net_income_percentage = fields.Float(string='Ingresos netos porcentaje', readonly=True, tracking=0, )
    net_income_total = fields.Float(string='Ingresos netos total', readonly=True, tracking=0, )
    net_premium = fields.Float(string='Prima neta', readonly=True, tracking=0, )
    net_profit_after_commission_month = fields.Float(string='Utilidad neta despues de comision', readonly=True,
                                                     tracking=0, )
    net_profit_after_commission_percentage = fields.Float(string='Utilidad neta despues de comision porcentaje',
                                                          readonly=True, tracking=0, )
    net_profit_after_commission_total = fields.Float(string='Utilidad neta despues de comision total', readonly=True,
                                                     tracking=0, )
    net_profit_before_taxes_month = fields.Float(string='Utilidad neta antes de impuestos', readonly=True, tracking=0, )
    net_profit_before_taxes_percentage = fields.Float(string='Utilidad neta antes de impuestos porcentaje',
                                                      readonly=True,
                                                      tracking=0, )
    net_profit_before_taxes_total = fields.Float(string='Utilidad neta antes de impuestos total', readonly=True,
                                                 tracking=0, )
    net_result_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    net_result_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    net_result_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    net_result_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    overhead_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    overhead_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    overhead_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    overhead_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    partner_id = fields.Many2one(string='Cliente', store=True, copy=True, tracking=100, comodel_name='res.partner', )
    partner_invoice_id = fields.Many2one(string='Dirección de Factura', store=True, copy=True, tracking=100,
                                         comodel_name='res.partner', )
    partner_shipping_id = fields.Many2one(string='Dirección de Entrega', store=True, copy=True, tracking=100,
                                          comodel_name='res.partner', )
    payment_term_id = fields.Many2one(string='Plazos de pago', store=True, copy=True, tracking=100,
                                      comodel_name='account.payment.term', )
    percentage_fp = fields.Float(string='Porcentaje 5p', store=True, copy=True, tracking=0, )
    percentage_value = fields.Float(string='%', readonly=True, tracking=0, )
    policies_month = fields.Float(string='Polizas', readonly=True, tracking=0, )
    policies_percentage = fields.Float(string='Polizas porcentaje', readonly=True, tracking=0, )
    policies_total = fields.Float(string='Polizas total', readonly=True, tracking=0, )
    pricelist_id = fields.Many2one(string='Lista de Precios', store=True, copy=True, tracking=100,
                                   comodel_name='product.pricelist', )
    profitableness = fields.Float(string='Rentabilidad', readonly=True, tracking=0, )
    rate_service = fields.Float(string='Tasa', store=True, copy=True, tracking=0, )
    rate_technology = fields.Float(string='Tasa', store=True, copy=True, tracking=0, )
    rent_provision_month = fields.Float(string='Provision de renta', readonly=True, tracking=0, )
    rent_provision_percentage = fields.Float(string='Provision de renta porcentaje', readonly=True, tracking=0, )
    rent_provision_total = fields.Float(string='Provision de renta total', readonly=True, tracking=0, )
    risk_id = fields.Many2one(string='Riesgo', readonly=True, tracking=100, comodel_name='hr.contract.risk', )
    rotation_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    rotation_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    rotation_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    rotation_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    salary_current = fields.Float(string='Salarios', readonly=True, tracking=0, )
    salary_month = fields.Float(string='Salarios', readonly=True, tracking=0, )
    salary_percentage = fields.Float(string='Salarios porcentaje', store=True, copy=True, tracking=0, )
    salary_total = fields.Float(string='Salarios total', readonly=True, tracking=0, )
    selection_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    selection_month = fields.Float(string='Selección', readonly=True, tracking=0, )
    selection_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    selection_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    special_transport_month = fields.Float(string='Transporte especial', store=True, copy=True, tracking=0, )
    special_transport_percentage = fields.Float(string='Transporte especial porcentaje', store=True, copy=True,
                                                tracking=0, )
    special_transport_total = fields.Float(string='Transporte especial total', store=True, copy=True, tracking=0, )
    stage_id = fields.Many2one(string='Estado', store=True, copy=True, tracking=100,
                               comodel_name='sale.quoter.stage', )
    supervision_month = fields.Float(string='Supervisión', readonly=True, tracking=0, )
    supervision_percentage = fields.Float(string='Supervisión porcentaje', readonly=True, tracking=0, )
    supervision_total = fields.Float(string='Supervisión total', readonly=True, tracking=0, )
    support_cost_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    support_cost_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    support_cost_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    support_cost_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    support_month = fields.Float(string='Apoyo', readonly=True, tracking=0, )
    support_percentage = fields.Float(string='Apoyo porcentaje', readonly=True, tracking=0, )
    support_staff_month = fields.Float(string='Personal de apoyo', readonly=True, tracking=0, )
    support_staff_percentage = fields.Float(string='Apoyo', readonly=True, tracking=0, )
    support_staff_total = fields.Float(string='Apoyo', readonly=True, tracking=0, )
    support_total = fields.Float(string='Apoyo total', readonly=True, tracking=0, )
    tax_ica_month = fields.Float(string='Impuesto 4X1000 E ICA', readonly=True, tracking=0, )
    tax_ica_percentage = fields.Float(string='Impuesto ICA porcentaje', readonly=True, tracking=0, )
    tax_ica_total = fields.Float(string='Impuesto ICA total', readonly=True, tracking=0, )
    technology_cost_month = fields.Float(string='Costo tecnologia', readonly=True, tracking=0, )
    technology_cost_percentage = fields.Float(string='Costo tecnologia', readonly=True, tracking=0, )
    technology_cost_total = fields.Float(string='Costo tecnologia', readonly=True, tracking=0, )
    technology_month = fields.Float(string='Tecnologia', readonly=True, tracking=0, )
    technology_percentage = fields.Float(string='Tecnologia porcentaje', readonly=True, tracking=0, )
    technology_total = fields.Float(string='Tecnologia Total', readonly=True, tracking=0, )
    term_months_service = fields.Integer(string='Plazo (Meses)', store=True, copy=True, tracking=0, )
    term_months_technology = fields.Float(string='Plazo (Meses)', store=True, copy=True, tracking=0, )
    total_commision_1invoice_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    total_commision_1invoice_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    total_commision_1invoice_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    total_commision_1invoice_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    total_commision_manager_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    total_commision_manager_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    total_commision_manager_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    total_commision_manager_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    total_commision_sostent_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    total_commision_sostent_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    total_commision_sostent_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    total_commision_sostent_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    total_commisions_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    total_commisions_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    total_commisions_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    total_commisions_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    total_contract = fields.Float(string='Total Contrato', readonly=True, tracking=0, )
    total_coordinador_total_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    total_coordinador_total_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    total_coordinador_total_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    total_coordinador_total_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    total_coordinator_cost_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    total_coordinator_cost_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    total_coordinator_cost_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    total_coordinator_cost_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    total_coordinator_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    total_coordinator_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    total_coordinator_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    total_coordinator_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    total_cost_general_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    total_cost_general_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    total_cost_general_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    total_cost_general_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    total_cost_technology = fields.Float(string='Total costo', readonly=True, tracking=0, )
    total_direct_cost_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    total_direct_cost_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    total_direct_cost_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    total_direct_cost_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    total_expense_month = fields.Float(string='Total Gastos', readonly=True, tracking=0, )
    total_expense_percentage = fields.Float(string='Total Gastos porcentaje', readonly=True, tracking=0, )
    total_expense_total = fields.Float(string='Total Gastos', readonly=True, tracking=0, )
    total_income_technology = fields.Float(string='Total ingreso', readonly=True, tracking=0, )
    total_interest_service = fields.Float(string='Total Interes', store=True, copy=True, tracking=0, )
    total_interest_technology = fields.Float(string='Total Interes', store=True, copy=True, tracking=0, )
    total_labor_commision_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    total_labor_commision_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    total_labor_commision_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    total_labor_commision_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    total_other_cost_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    total_other_cost_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    total_other_cost_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    total_other_cost_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    total_premium = fields.Float(string='Total prima', readonly=True, tracking=0, )
    total_value_fivep = fields.Float(string='Valor Total 5p', readonly=True, tracking=0, )
    total_value = fields.Float(string='Valor total', readonly=True, tracking=100, )
    training_month = fields.Float(string='Capacitación', readonly=True, tracking=0, )
    training_percentage = fields.Float(string='Capacitación porcentaje', readonly=True, tracking=0, )
    training_total = fields.Float(string='Capacitación total', readonly=True, tracking=0, )
    uac_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    uac_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    uac_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    uac_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    unexpected_month = fields.Float(string='Imprevisto', readonly=True, tracking=0, )
    unexpected_percentage = fields.Float(string='Imprevisto porcentaje', readonly=True, tracking=0, )
    unexpected_total = fields.Float(string='Imprevisto total', readonly=True, tracking=0, )
    unforeseen_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    unforeseen_month = fields.Float(string='Rotacion', readonly=True, tracking=0, )
    unforeseen_percentage = fields.Float(string='Selección porcentaje', readonly=True, tracking=0, )
    unforeseen_total = fields.Float(string='Selección total', readonly=True, tracking=0, )
    validity_date = fields.Date(string='Expiración Oferta', store=True, copy=True, tracking=100, )
    vat = fields.Float(string='IVA 19%', readonly=True, tracking=0, )
    weapon_month = fields.Float(string='Armamento', readonly=True, tracking=0, )
    weapon_percentage = fields.Float(string='Armamento porcentaje', readonly=True, tracking=0, )
    weapon_total = fields.Float(string='Armamento total', readonly=True, tracking=0, )


class Salequoterstage(models.Model):
    _name = 'sale.quoter.stage'
    _description = 'Sale Quoter Stage'
    bool_generate_quoter = fields.Boolean(string='Generar cotizacion', store=True, copy=True, tracking=0, )
    mail_template_ids = fields.Many2many(relation='salequoterstage_mail_template_ids_rel', column1='salequoterstage_id',
                                         column2='mail_template_ids_id', string='Plantilla de correo', store=True,
                                         copy=True, tracking=0,
                                         comodel_name='mail.template', )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    sq_next_stage = fields.Many2one(string='Siguiente Etapa', store=True, copy=True, tracking=0,
                                    comodel_name='sale.quoter.stage', )
    sq_res_users_ids = fields.Many2many(relation='salequoterstage_sq_res_users_ids_rel', column1='salequoterstage_id',
                                        column2='sq_res_users_ids_id', string='Usuarios', store=True, copy=True,
                                        tracking=0,
                                        comodel_name='res.users', )


class Secuenciaparaexportacióndearchivos(models.Model):
    _name = 'ap.file.sequence'
    _description = 'Secuencia para exportación de archivos'
    date = fields.Date(string='Fecha', store=True, required=True, copy=True, tracking=0, )
    sequence_number = fields.Integer(string='Número de Secuencia', store=True, required=True, copy=True, tracking=0, )


class Seguimientodeexámenesmédicos(models.Model):
    _name = 'examenes.medicos.seguimiento'
    _description = 'Seguimiento de Exámenes Médicos'
    archivos_adjuntos = fields.Many2many(relation='salequoterstage_archivos_adjuntos_rel', column1='salequoterstage_id',
                                         column2='archivos_adjuntos_id', string='Archivos Adjuntos', store=True,
                                         copy=True, tracking=0,
                                         comodel_name='ir.attachment', )
    examen_id = fields.Many2one(string='Examen Relacionado', store=True, required=True, copy=True, tracking=0,
                                comodel_name='examenes.medicos', )
    fecha_seguimiento = fields.Date(string='Fecha de Seguimiento', store=True, required=True, copy=True, tracking=0, )
    observacion = fields.Text(string='Observación', store=True, copy=True, tracking=0, )
    programas = fields.Many2many(relation='salequoterstage_programas_rel', column1='salequoterstage_id',
                                 column2='programas_id', string='Programas', store=True, copy=True, tracking=0,
                                 comodel_name='programa', )


class Selection(models.Model):
    _name = 'quoter.selection'
    _description = 'Selection'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    service_mod_id = fields.Many2one(string='Modalidad', store=True, copy=True, tracking=0,
                                     comodel_name='quoter.service.mod', )
    total_selection = fields.Float(string='Total Selección', readonly=True, tracking=0, )


class Selectionline(models.Model):
    _name = 'quoter.selection.line.aux'
    _description = 'selection Line'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    quoter_line_id = fields.Many2one(string='Sale quoter line', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter.line', )
    selection_id = fields.Many2one(string='Selection', store=True, copy=True, tracking=0,
                                   comodel_name='quoter.selection', )


class Selectionline(models.Model):
    _name = 'quoter.selection.line'
    _description = 'selection Line'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    price_unit = fields.Float(string='Precio Unitario', store=True, copy=True, tracking=0, )
    quoter_line_id = fields.Many2one(string='Sale quoter line', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter.line', )
    selection_id = fields.Many2one(string='Selection', store=True, copy=True, tracking=0,
                                   comodel_name='quoter.selection', )


class Selecttheorientationofthepdf(models.Model):
    _name = 'pdforientation'
    _description = 'Select the orientation of the pdf'
    query_name = fields.Text(string='Query', store=True, copy=True, tracking=0, )


class Servicemod(models.Model):
    _name = 'quoter.service.mod'
    _description = 'Service Mod'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    value_percentage = fields.Float(string='Valor porcentaje', store=True, copy=True, tracking=0, )


class Serviciospúblicos(models.Model):
    _name = 'hr.public.service'
    _description = 'Servicios públicos'
    name = fields.Char(string='Servicio publico', store=True, copy=True, tracking=0, )


class Sincronizaunregistroconcalendariodegoogle(models.Model):
    _name = 'google.calendar.sync'
    _description = 'Sincroniza un registro con Calendario de Google'
    active = fields.Boolean(string='Activo', store=True, copy=True, tracking=0, )
    google_id = fields.Char(string='ID de Calendario de Google', store=True, tracking=0, )
    need_sync = fields.Boolean(string='Necesita sincronización', store=True, tracking=0, )


class Soporte(models.Model):
    _name = 'quoter.support'
    _description = 'Soporte'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    total_support = fields.Float(string='Total Soportes', readonly=True, tracking=0, )


class Soportesdeordenesdeservicio(models.Model):
    _name = 'project.service.order.support'
    _description = 'Soportes de ordenes de servicio'
    name = fields.Char(string='Soporte de orden de servicio', store=True, copy=True, tracking=0, )


class Subcategoríadeserviciodeayuda(models.Model):
    _name = 'helpdesk.subcategory'
    _description = 'Subcategoría de servicio de ayuda'
    name = fields.Char(string='Nombre de la subcategoría', store=True, required=True, copy=True, tracking=0, )
    parent_category_id = fields.Many2one(string='Categoría de padres', store=True, required=True, copy=True,
                                         tracking=0,
                                         comodel_name='helpdesk.category', )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    support_user_ids = fields.Many2many(comodel_name='res.users', relation='helpdesk_subcat_support_user_rel',
                                        column1='subcategory_id', column2='user_id', string='Usuarios de soporte',
                                        copy=False, )
    technical_user_ids = fields.Many2many(comodel_name='res.users', relation='helpdesk_subcat_tech_user_rel',
                                          column1='subcategory_id', column2='user_id', string='Usuarios técnicos',
                                          copy=False, )


class Subtipodecotizante(models.Model):
    _name = 'hr.fiscal.subtype'
    _description = 'Subtipo de Cotizante'
    code = fields.Char(string='Código', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    note = fields.Text(string='Notas', store=True, copy=True, tracking=0, )


class Subzonacontrato(models.Model):
    _name = 'hr.contract.subzone'
    _description = 'Subzona Contrato'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class Tablerodetickets(models.Model):
    _name = 'ticket.dashboard'
    _description = 'Tablero de tickets'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class Tarifario(models.Model):
    _name = 'hr.roster.tarifario'
    _description = 'Tarifario'
    contract_id = fields.Many2one(string='Contrato', store=True, required=True, copy=True, tracking=0,
                                  comodel_name='hr.contract', )
    employee_id = fields.Many2one(string='Empleado', store=True, required=True, copy=True, tracking=0,
                                  comodel_name='hr.employee', )
    fecha_aprobacion = fields.Date(string='Fecha de aprobacion', store=True, copy=True, tracking=0, )
    from_close = fields.Boolean(string='Creado desde Cierre', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', readonly=True, tracking=0, )
    novelty_id = fields.Many2one(string='Novedad', store=True, copy=True, tracking=0, comodel_name='hr.novelty', )
    novelty_type_id = fields.Many2one(string='Categoria de novedad', store=True, copy=True, tracking=0,
                                      comodel_name='hr.novelty.type', )
    period_id = fields.Many2one(string='Periodo', store=True, required=True, copy=True, tracking=0,
                                comodel_name='hr.period', )
    valor_total = fields.Float(string='Valor Total', readonly=True, tracking=0, )


class Tarifario(models.Model):
    _name = 'hr.tarifario'
    _description = 'Tarifario'
    horario_id = fields.Many2one(string='Horario', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='hr.roster.horario', )
    name = fields.Char(string='Nombre', readonly=True, tracking=0, )
    puesto_id = fields.Many2one(string='Puesto', store=True, required=True, copy=True, tracking=0,
                                comodel_name='hr.roster.puesto', )
    valor = fields.Float(string='Valor', store=True, required=True, copy=True, tracking=0, )


class Tarifasdeentrega(models.Model):
    _name = 'delivery.rate'
    _description = 'Tarifas de Entrega'
    city_dest_id = fields.Many2one(string='Ubicación de destino', store=True, required=True, copy=True, tracking=0,
                                   comodel_name='res.city', )
    city_id = fields.Many2one(string='Origen', store=True, required=True, copy=True, tracking=0,
                              comodel_name='res.city', )
    company_id = fields.Many2one(string='Compañia', store=True, readonly=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    currency_id = fields.Many2one(string='Moneda', store=True, readonly=True, tracking=0, comodel_name='res.currency', )
    name = fields.Char(string='Título', store=True, copy=True, tracking=0, )
    notes = fields.Text(string='Terminos y condiciones', store=True, copy=True, tracking=0, )
    price_kg = fields.Monetary(string='Precio (Kg)', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='product.product', )
    tolerance = fields.Float(string='Tolerancia (%)', store=True, copy=True, tracking=0, )


class Technology(models.Model):
    _name = 'quoter.technology'
    _description = 'Technology'
    name = fields.Char(string='Concepto', store=True, copy=True, tracking=0, )
    sale_quoter_id = fields.Many2one(string='Cotizador', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter', )
    total_cost = fields.Float(string='Costo Total', store=True, copy=True, tracking=0, )
    total_income = fields.Float(string='Ingrso Total', store=True, copy=True, tracking=0, )


class Templatereportecontrato(models.Model):
    _name = 'template.report.contract'
    _description = 'Template Reporte Contrato'
    codes_print = fields.Text(string='Campos usables', readonly=True, tracking=0, )
    description = fields.Html(string='Descripción', store=True, copy=True, tracking=0, )
    footer_section = fields.Html(string='Pie de Página', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class Thsucursal(models.Model):
    _name = 'hr.branch'
    _description = 'TH Sucursal'
    active = fields.Boolean(string='Activo', store=True, copy=True, tracking=0, )
    biller_id = fields.Many2one(string='Facturador', store=True, copy=True, tracking=0, comodel_name='res.users', )
    cashier_id = fields.Many2one(string='Cajero', store=True, copy=True, tracking=0, comodel_name='res.users', )
    code = fields.Char(string='Código', store=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    parent_id = fields.Many2one(string='Padre', store=True, copy=True, tracking=0, comodel_name='hr.branch', )
    partner_id = fields.Many2one(string='Tercero', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    restock_locations_ids = fields.Many2many(relation='thsucursal_restock_locations_id_rel', column1='thsucursal_id',
                                             column2='restock_locations_id_id', string='Location Transit', store=True,
                                             copy=True, tracking=0,
                                             comodel_name='stock.location', )
    restock_type_id = fields.Many2one(string='Restock Type', store=True, copy=True, tracking=0,
                                      comodel_name='stock.picking.type', )
    restock_warehouses_ids = fields.Many2many(relation='thsucursal_restock_warehouses_i_rel', column1='thsucursal_id',
                                              column2='restock_warehouses_i_id', string='Supply Warehouses', store=True,
                                              copy=True, tracking=0,
                                              comodel_name='stock.warehouse', )
    user_id = fields.Many2one(string='Director', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Ticketdeserviciodeayuda(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Ticket de servicio de ayuda'
    access_token = fields.Char(string='Token de seguridad', store=True, tracking=0, )
    access_url = fields.Char(string='URL de acceso al portal', readonly=True, tracking=0, )
    access_warning = fields.Text(string='Advertencia de acceso', readonly=True, tracking=0, )
    account_analytic_id = fields.Many2one(string='Centro de Costo', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    active = fields.Boolean(string='Activo', store=True, copy=True, tracking=0, )
    activity_date_deadline = fields.Date(string='Fecha límite de la próxima actividad', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Siguiente resumen de actividad', tracking=0, )
    activity_type_icon = fields.Char(string='Icono de tipo de actividad', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Siguiente tipo de actividad', tracking=0,
                                       comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Usuario responsable', tracking=0, comodel_name='res.users', )
    attachment_ids = fields.Many2many(relation='ticketdeserviciodeay_attachment_ids_rel',
                                      column1='ticketdeserviciodeay_id', column2='attachment_ids_id',
                                      string='Archivos adjuntos', store=True, copy=True, tracking=0,
                                      comodel_name='ir.attachment', )
    bussines_name = fields.Char(string='Bussines Name', store=True, copy=True, tracking=100, )
    cancel_button_boolean = fields.Boolean(string='Botón de cancelación', readonly=True, tracking=0, )
    cancel_by = fields.Many2one(string='Cancelado por', store=True, copy=True, tracking=100,
                                comodel_name='res.users', )
    cancel_date = fields.Datetime(string='Fecha cancelada', store=True, copy=True, tracking=100, )
    cancel_reason = fields.Char(string='Cancelar razón', store=True, copy=True, tracking=100, )
    cancel_stage_boolean = fields.Boolean(string='Cancelar etapa', store=True, readonly=True, tracking=0, )
    category_bool = fields.Boolean(string='Configuración de categoría', store=True, readonly=True, tracking=0, )
    category_id = fields.Many2one(string='Categoría', store=True, copy=True, tracking=100,
                                  comodel_name='helpdesk.category', )
    client_validate = fields.Boolean(string='Validado por el cliente', store=True, copy=True, tracking=0, )
    close_by = fields.Many2one(string='Cerrado', store=True, copy=True, tracking=100, comodel_name='res.users', )
    close_date = fields.Datetime(string='Fecha de cierre', store=True, copy=True, tracking=100, )
    closed_stage_boolean = fields.Boolean(string='Etapa cerrada', store=True, readonly=True, tracking=0, )
    color = fields.Integer(string='Indice de color', store=True, copy=True, tracking=0, )
    comment = fields.Text(string='Comentario', store=True, copy=True, tracking=100, )
    company_id = fields.Many2one(string='Compañía', store=True, copy=True, tracking=0, comodel_name='res.company', )
    cumple_lo_requerido = fields.Boolean(string='Cumple lo requerido', store=True, copy=True, tracking=0, )
    customer_comment = fields.Text(string='Comentario del cliente', store=True, copy=True, tracking=100, )
    description = fields.Html(string='Descripción', store=True, copy=True, tracking=100, )
    done_button_boolean = fields.Boolean(string='Botón hecho', readonly=True, tracking=0, )
    done_stage_boolean = fields.Boolean(string='Etapa de hecho', store=True, readonly=True, tracking=0, )
    duration_dev = fields.Float(string='Tiempo previsto', store=True, copy=True, tracking=0, )
    duration = fields.Float(string='Duración real', readonly=True, tracking=0, )
    email_subject = fields.Char(string='Tema', store=True, copy=True, tracking=0, )
    email = fields.Char(string='Correo electrónico', store=True, copy=True, tracking=100, )
    end_time = fields.Datetime(string='Hora de finalización', store=True, tracking=0, )
    form_url = fields.Char(string='Forma URL', readonly=True, tracking=0, )
    invoice_count = fields.Integer(string='Factura', readonly=True, tracking=0, )
    invoice_hours = fields.Float(string='Tiempo facturable', store=True, copy=True, tracking=0, )
    is_stage_new = fields.Boolean(string='New Stage', readonly=True, tracking=0, )
    last_update = fields.Datetime(string='Last Update', store=True, readonly=True, tracking=0, )
    lead_count = fields.Integer(string='Guiar', readonly=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Recuento de adjuntos', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='ticketdeserviciodeay_message_channel_ids_rel',
                                           column1='ticketdeserviciodeay_id', column2='message_channel_ids_id',
                                           string='Seguidores (Canales)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Número de errores', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Error de entrega de mensajes', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='Error de entrega de SMS', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Es Seguidor', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Apego principal', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Accion necesaria', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='ticketdeserviciodeay_message_partner_ids_rel',
                                           column1='ticketdeserviciodeay_id', column2='message_partner_ids_id',
                                           string='Seguidores (socios)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Contador de Mensajes no Leídos', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Mensajes no leídos', readonly=True, tracking=0, )
    mobile_no = fields.Char(string='Teléfono', store=True, copy=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='Mi fecha límite de actividad', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=100, )
    open_boolean = fields.Boolean(string='Ticket abierto', store=True, readonly=True, tracking=0, )
    opportunity_count = fields.Integer(string='Oportunidad', readonly=True, tracking=0, )
    partner_id = fields.Many2one(string='Cliente', store=True, required=True, copy=True, tracking=100,
                                 comodel_name='res.partner', )
    person_name = fields.Char(string='Nombre de la persona', store=True, copy=True, tracking=100, )
    portal_ticket_url_wp = fields.Char(string='URL de ticket portal WP', readonly=True, tracking=0, )
    priority = fields.Many2one(string='Prioridad', store=True, copy=True, tracking=100,
                               comodel_name='helpdesk.priority', )
    product_ids = fields.Many2many(relation='ticketdeserviciodeay_product_ids_rel', column1='ticketdeserviciodeay_id',
                                   column2='product_ids_id', string='Productos', store=True, copy=True, tracking=0,
                                   comodel_name='product.product', )
    project_id = fields.Many2one(string='Proyecto', store=True, copy=True, tracking=100,
                                 comodel_name='project.project', )
    purchase_order_count = fields.Integer(string='Pedido de compra', readonly=True, tracking=0, )
    rating_bool = fields.Boolean(string='Configuración de calificación', store=True, readonly=True, tracking=0, )
    real_time = fields.Float(string='Tiempo Real', store=True, copy=True, tracking=0, )
    release_id = fields.Many2one(string='Release', store=True, copy=True, tracking=100,
                                 comodel_name='helpdesk.release', )
    reopen_stage_boolean = fields.Boolean(string='Etapa reabrida', store=True, readonly=True, tracking=0, )
    replied_date = fields.Datetime(string='Fecha de respuesta', store=True, copy=True, tracking=100, )
    report_token = fields.Char(string='Token de acceso', store=True, copy=True, tracking=0, )
    resolution_detail = fields.Html(string='Realización Interna', store=True, copy=True, tracking=100, )
    responsable_id = fields.Many2one(string='Responsable del Ticket', store=True, copy=True, tracking=0,
                                     comodel_name='res.partner', )
    sale_id = fields.Many2one(string='Pedido', store=True, copy=True, tracking=0, comodel_name='sale.order', )
    sale_order_count = fields.Integer(string='Ordenar', readonly=True, tracking=0, )
    sh_days_to_late = fields.Float(string='SLA Duración tardía', store=True, readonly=True, tracking=0, )
    sh_days_to_reach = fields.Float(string='SLA alcanzó la duración', store=True, readonly=True, tracking=0, )
    sh_display_multi_user = fields.Boolean(string='SH Display Multi User', readonly=True, tracking=0, )
    sh_display_product = fields.Boolean(string='Producto de pantalla SH', readonly=True, tracking=0, )
    sh_due_date = fields.Datetime(string='Fecha Entrega', store=True, copy=True, tracking=0, )
    sh_invoice_ids = fields.Many2many(relation='ticketdeserviciodeay_sh_invoice_ids_rel',
                                      column1='ticketdeserviciodeay_id', column2='sh_invoice_ids_id', string='Factura',
                                      store=True, copy=True, tracking=0,
                                      comodel_name='account.move', )
    sh_lead_ids = fields.Many2many(relation='ticketdeserviciodeay_sh_lead_ids_rel', column1='ticketdeserviciodeay_id',
                                   column2='sh_lead_ids_id', string='Leads/Oportunidades', store=True, copy=True,
                                   tracking=0,
                                   comodel_name='crm.lead', )
    sh_merge_ticket_count = fields.Integer(string='SH MERGE RECTURA', readonly=True, tracking=0, )
    sh_merge_ticket_ids = fields.Many2many(comodel_name='helpdesk.ticket', relation='helpdesk_ticket_merge_rel',
                                           column1='src_ticket_id', column2='dst_ticket_id',
                                           string='Tickets a fusionar', copy=False, )
    sh_planned_date = fields.Datetime(string='Fecha Inicio Solicitud', store=True, copy=True, tracking=0, )
    sh_purchase_order_ids = fields.Many2many(relation='ticketdeserviciodeay_sh_purchase_order_id_rel',
                                             column1='ticketdeserviciodeay_id', column2='sh_purchase_order_id_id',
                                             string='Pedidos', store=True, copy=True, tracking=0,
                                             comodel_name='purchase.order', )
    sh_sale_order_ids = fields.Many2many(relation='ticketdeserviciodeay_sh_sale_order_ids_rel',
                                         column1='ticketdeserviciodeay_id', column2='sh_sale_order_ids_id',
                                         string='Ordenar', store=True, copy=True, tracking=0,
                                         comodel_name='sale.order', )
    sh_sla_deadline = fields.Datetime(string='Fecha límite de SLA', store=True, readonly=True, tracking=0, )
    sh_sla_policy_ids = fields.Many2many(relation='ticketdeserviciodeay_sh_sla_policy_ids_rel',
                                         column1='ticketdeserviciodeay_id', column2='sh_sla_policy_ids_id',
                                         string='Políticas de SLA de servicio de ayuda', store=True, tracking=0,
                                         comodel_name='sh.helpdesk.sla', )
    sh_status_boolean = fields.Boolean(string='Sh status boolean', readonly=True, tracking=0, )
    sh_ticket_alarm_ids = fields.Many2many(relation='ticketdeserviciodeay_sh_ticket_alarm_ids_rel',
                                           column1='ticketdeserviciodeay_id', column2='sh_ticket_alarm_ids_id',
                                           string='Recordatorios de tickets', store=True, copy=True, tracking=0,
                                           comodel_name='sh.ticket.alarm', )
    sh_ticket_report_url = fields.Char(string='URL de informe de tickets de SH', readonly=True, tracking=0, )
    sh_user_ids = fields.Many2many(relation='ticketdeserviciodeay_sh_user_ids_rel', column1='ticketdeserviciodeay_id',
                                   column2='sh_user_ids_id', string='Asignar múltiples usuarios', store=True, copy=True,
                                   tracking=0,
                                   comodel_name='res.users', )
    solucion_inmediata = fields.Boolean(string='Solución inmediada', store=True, copy=True, tracking=0, )
    solution_done = fields.Html(string='Solución propuesta cliente', store=True, copy=True, tracking=100, )
    stage_id = fields.Many2one(string='Escenario', index=True, store=True, copy=True, tracking=100,
                               comodel_name='helpdesk.stages', )
    start_time = fields.Datetime(string='Hora de inicio', store=True, tracking=0, )
    start_uid = fields.Many2one(string='Usuario en progreso', store=True, copy=True, tracking=0,
                                comodel_name='res.users', )
    sub_category_bool = fields.Boolean(string='Configuración de subcasegas', store=True, readonly=True, tracking=0, )
    sub_category_id = fields.Many2one(string='Subcategoría', store=True, copy=True, tracking=0,
                                      comodel_name='helpdesk.subcategory', )
    subject_id = fields.Many2one(string='ipo Intern', store=True, copy=True, tracking=100,
                                 comodel_name='helpdesk.sub.type', )
    tag_ids = fields.Many2many(relation='ticketdeserviciodeay_tag_ids_rel', column1='ticketdeserviciodeay_id',
                               column2='tag_ids_id', string='Etiquetas', store=True, copy=True, tracking=0,
                               comodel_name='helpdesk.tags', )
    task_count = fields.Integer(string='Tareas', readonly=True, tracking=0, )
    task_ids = fields.Many2many(relation='ticketdeserviciodeay_task_ids_rel', column1='ticketdeserviciodeay_id',
                                column2='task_ids_id', string='Tarea', store=True, copy=True, tracking=0,
                                comodel_name='project.task', )
    team_head = fields.Many2one(string='Jefe de equipo', store=True, copy=True, tracking=100,
                                comodel_name='res.users', )
    team_id = fields.Many2one(string='Equipo', store=True, copy=True, tracking=100, comodel_name='helpdesk.team', )
    ticket_allocated = fields.Boolean(string='Asignado', store=True, copy=True, tracking=0, )
    ticket_from_portal = fields.Boolean(string='Ticket desde portal', store=True, copy=True, tracking=0, )
    ticket_from_website = fields.Boolean(string='Ticket del sitio web', store=True, copy=True, tracking=0, )
    ticket_running = fields.Boolean(string='Ticket', store=True, copy=True, tracking=0, )
    ticket_type = fields.Many2one(string='Tipo Interno', store=True, copy=True, tracking=100,
                                  comodel_name='helpdesk.ticket.type', )
    total_time = fields.Char(string='Tiempo Total', store=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario asignado', store=True, copy=True, tracking=100,
                              comodel_name='res.users', )
    video_link = fields.Char(string='Video Link', store=True, copy=True, tracking=100, )
    x_city = fields.Many2one(string='Ciudad', store=True, copy=True, tracking=1, comodel_name='res.city', )


class Tipodeacuerdo(models.Model):
    _name = 'purchase.requisition.type'
    _description = 'Tipo de Acuerdo'
    name = fields.Char(string='Tipo de acuerdo de compra', store=True, required=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )


class Tipodecontrato(models.Model):
    _name = 'hr.contract.type'
    _description = 'Tipo de Contrato'
    allow_replace_obra_labor = fields.Boolean(string='Permitir remplazo en obra labor', store=True, copy=True,
                                              tracking=0, )
    company_id = fields.Many2one(string='Company', index=True, store=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    name = fields.Char(string='Tipo de Contrato', store=True, readonly=True, tracking=0, )
    required_date_end = fields.Boolean(string='Obligatorio Fecha Finalización', store=True, copy=True, tracking=0, )
    restrict_schedule = fields.Boolean(string='Restriccion en programación', store=True, copy=True, tracking=0, )


class Tipodecotizante(models.Model):
    _name = 'hr.fiscal.type'
    _description = 'Tipo de Cotizante'
    code = fields.Char(string='Código', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    note = fields.Text(string='Notas', store=True, copy=True, tracking=0, )


class Tipodeduración(models.Model):
    _name = 'tipo.duracion.estudios.capacitaciones'
    _description = 'Tipo de Duración'
    name = fields.Char(string='Tipo de Duración', store=True, required=True, copy=True, tracking=0, )


class Tipodeestudiosocapacitaciones(models.Model):
    _name = 'tipo.estudios.capacitaciones'
    _description = 'Tipo de Estudios o Capacitaciones'
    name = fields.Char(string='Tipo', store=True, required=True, copy=True, tracking=0, )


class Tipodeidentificación(models.Model):
    _name = 'res.partner.document.type'
    _description = 'Tipo de identificación'
    code_dian = fields.Char(string='Código DIAN', store=True, copy=True, tracking=0, )
    code = fields.Char(string='Código', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    no_validar_nit = fields.Boolean(string='No validar NIT', store=True, copy=True, tracking=0, )


class Tipodelicitaciones(models.Model):
    _name = 'tipo.licitaciones'
    _description = 'Tipo de Licitaciones'
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Tipoderangodefechas(models.Model):
    _name = 'date.range.type'
    _description = 'Tipo de rango de fechas'
    active = fields.Boolean(string='Activo', store=True, copy=True, tracking=0, )
    allow_overlap = fields.Boolean(string='Permitir solapamiento', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañía', index=True, store=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Tipodeservicio(models.Model):
    _name = 'project.service.type'
    _description = 'Tipo de servicio'
    ays = fields.Float(string='A&S', store=True, copy=True, tracking=0, )
    linea_negocio_id = fields.Many2one(string='Linea de negocio', store=True, copy=True, tracking=0,
                                       comodel_name='project.linea.negocio', )
    name = fields.Char(string='Tipo de servicio', store=True, copy=True, tracking=0, )
    product_ids = fields.Many2many(relation='tipodeservicio_product_ids_rel', column1='tipodeservicio_id',
                                   column2='product_ids_id', string='Producto', store=True, copy=True, tracking=0,
                                   comodel_name='product.product', )


class Tipodesujetodeserviciodeayuda(models.Model):
    _name = 'helpdesk.sub.type'
    _description = 'Tipo de sujeto de servicio de ayuda'
    is_technical = fields.Boolean(string='Equipo Técnico', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    partner_ids = fields.Many2many(relation='tipodesujetodeservic_partner_ids_rel', column1='tipodesujetodeservic_id',
                                   column2='partner_ids_id', string='Tercero', store=True, copy=True, tracking=0,
                                   comodel_name='res.partner', )


class Tipodetarifa(models.Model):
    _name = 'quoter.rate.type'
    _description = 'Tipo de tarifa'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    rate_value = fields.Float(string='Valor de Tarifa', store=True, copy=True, tracking=0, )


class Tipointernodeserviciodeayuda(models.Model):
    _name = 'helpdesk.ticket.type'
    _description = 'Tipo Interno de servicio de ayuda'
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    sla_count = fields.Integer(string='Conteo de SLA', readonly=True, tracking=0, )


class Tiposdecursosdeseguridad(models.Model):
    _name = 'security.course.type'
    _description = 'Tipos de Cursos de Seguridad'
    code = fields.Char(string='Código', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, readonly=True, tracking=0, )
    type = fields.Char(string='Curso', store=True, required=True, copy=True, tracking=0, )


class Tiposdegruposdeimpuestos(models.Model):
    _name = 'account.tax.group.type'
    _description = 'Tipos de Grupos de Impuestos'
    code = fields.Char(string='Código', store=True, required=True, copy=True, tracking=0, )
    description = fields.Char(string='Descripción', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Tiposdemotivos(models.Model):
    _name = 'tipo.motivo.procesos.disciplinarios'
    _description = 'Tipos de Motivos'
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Tiposdesanciones(models.Model):
    _name = 'tipo.sancion.procesos.disciplinarios'
    _description = 'Tipos de Sanciones'
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Tipoturno(models.Model):
    _name = 'hr.roster.tipo.turno'
    _description = 'Tipo Turno'
    codigo = fields.Char(string='Codigo', store=True, required=True, copy=True, tracking=0, )
    duration = fields.Integer(string='Duracion horas', readonly=True, tracking=0, )
    modalidad_id = fields.Many2one(string='Modalidad', store=True, required=True, copy=True, tracking=0,
                                   comodel_name='hr.roster.modalidad', )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    time_break = fields.Char(string='Descanso', store=True, copy=True, tracking=0, )
    time_in = fields.Char(string='Entrada', store=True, required=True, copy=True, tracking=0, )
    time_out = fields.Char(string='Salida', store=True, required=True, copy=True, tracking=0, )


class Tipsforqueries(models.Model):
    _name = 'tipsqueries'
    _description = 'Tips for queries'
    description = fields.Text(string='Description', store=True, copy=True, tracking=0, )
    name = fields.Text(string='Query', store=True, required=True, copy=True, tracking=0, )


class Títuloseducativos(models.Model):
    _name = 'titulos.educativos.estudios.capacitaciones'
    _description = 'Títulos Educativos'
    name = fields.Char(string='Nombre del Título', store=True, required=True, copy=True, tracking=0, )


class Topedehoras(models.Model):
    _name = 'hr.contract.hour.limit'
    _description = 'Tope de horas'
    concept_diurn_id = fields.Many2one(string='Concepto extra diurno', store=True, copy=True, tracking=0,
                                       comodel_name='hr.overtime.type', )
    concept_female_diurn_id = fields.Many2one(string='Concepto Femenino >= 47 extra diurno', store=True, copy=True,
                                              tracking=0, comodel_name='hr.overtime.type', )
    concept_female_nocturn_id = fields.Many2one(string='Concepto Femenino >= 47 extra nocturno', store=True,
                                                copy=True,
                                                tracking=0, comodel_name='hr.overtime.type', )
    concept_male_diurn_id = fields.Many2one(string='Concepto Masculino >= 50 extra diurno', store=True, copy=True,
                                            tracking=0, comodel_name='hr.overtime.type', )
    concept_male_nocturn_id = fields.Many2one(string='Concepto Masculino >= 50 extra nocturno', store=True, copy=True,
                                              tracking=0, comodel_name='hr.overtime.type', )
    concept_nocturn_id = fields.Many2one(string='Concepto extra nocturno', store=True, copy=True, tracking=0,
                                         comodel_name='hr.overtime.type', )
    contract_id = fields.Many2one(string='Contrato', store=True, copy=True, tracking=0, comodel_name='hr.contract', )
    contract_type_id = fields.Many2one(string='Tipo de contrato', store=True, copy=True, tracking=0,
                                       comodel_name='hr.contract.type', )
    extra_hours_max = fields.Float(string='Máximo de horas extra', store=True, copy=True, tracking=0, )
    limit = fields.Float(string='Tope de horas', store=True, copy=True, tracking=0, )


class Turno(models.Model):
    _name = 'hr.roster.turno'
    _description = 'Turno'
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Next Activity Type', tracking=0, comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    additional_per_hour = fields.Boolean(string='Turno adicional (Por horas)', store=True, copy=True, tracking=0, )
    adicional_nom = fields.Boolean(string='Turno adicional (NOM)', store=True, copy=True, tracking=0, )
    adicional = fields.Boolean(string='Servicio adicional (FAC)', store=True, copy=True, tracking=0, )
    categoria_turno = fields.Char(string='Estado', store=True, tracking=0, )
    category_id = fields.Many2one(string='Concepto de novedad', store=True, copy=True, tracking=0,
                                  comodel_name='hr.novelty.type', )
    cliente_contract_id = fields.Many2one(string='Contrato', store=True, readonly=True, tracking=0,
                                          comodel_name='project.project', )
    close_from_solo_adicionales = fields.Boolean(string='Cerrado desde solo adicionales', store=True, copy=True,
                                                 tracking=0, )
    company_id = fields.Many2one(string='Compañía', copy=True, tracking=0, comodel_name='res.company', )
    contract_id = fields.Many2one(string='Contrato', store=True, readonly=True, tracking=0,
                                  comodel_name='hr.contract', )
    date_from = fields.Datetime(string='Desde', store=True, copy=True, tracking=0, )
    date_to = fields.Datetime(string='Hasta', store=True, copy=True, tracking=0, )
    descanso = fields.Boolean(string='Descanso', store=True, copy=True, tracking=0, )
    dummy = fields.Boolean(string='Dummy', store=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, readonly=True, tracking=0,
                                  comodel_name='hr.employee', )
    estado_cierre = fields.Boolean(string='Estado cierre', store=True, readonly=True, copy=True, tracking=0, )
    estado_tarifario = fields.Boolean(string='Estado tarifario', store=True, readonly=True, copy=True, tracking=0, )
    extended = fields.Boolean(string='Extendido', store=True, copy=True, tracking=0, )
    extra_hour = fields.Boolean(string='Hora Extra', store=True, copy=True, tracking=0, )
    fecha_cierre = fields.Date(string='Fecha de cierre', store=True, readonly=True, copy=True, tracking=0, )
    holiday_id = fields.Many2one(string='Ausencia', store=True, copy=True, tracking=0, comodel_name='hr.leave', )
    induction = fields.Boolean(string='Induccion', store=True, copy=True, tracking=0, )
    linea_programacion_id = fields.Many2one(string='Linea Programacion', store=True, copy=True, tracking=0,
                                            comodel_name='hr.roster.programacion.line', )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='turno_message_channel_ids_rel', column1='turno_id',
                                           column2='message_channel_ids_id', string='Followers (Channels)',
                                           readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='turno_message_partner_ids_rel', column1='turno_id',
                                           column2='message_partner_ids_id', string='Followers (Partners)',
                                           readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    modalidad_id = fields.Many2one(string='Modalidad', store=True, tracking=0, comodel_name='hr.roster.modalidad', )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    name = fields.Char(string='Codigo', store=True, readonly=True, tracking=0, )
    order_line_id = fields.Many2one(string='Orden de servicio adicional', store=True, copy=True, tracking=0,
                                    comodel_name='project.service.order.line', )
    parent_modality_id = fields.Many2one(string='Modalidad Padre', store=True, copy=True, tracking=0,
                                         comodel_name='hr.roster.modalidad', )
    partial_replace = fields.Boolean(string='Reemplazo parcial', store=True, copy=True, tracking=0, )
    prog_adicional = fields.Many2one(string='Adicional de programacion', store=True, copy=True, tracking=0,
                                     comodel_name='hr.roster.programacion', )
    programacion_id = fields.Many2one(string='Programacion', store=True, readonly=True, tracking=0,
                                      comodel_name='hr.roster.programacion', )
    puesto_id = fields.Many2one(string='Puesto', store=True, readonly=True, tracking=0,
                                comodel_name='hr.roster.puesto', )
    st_control = fields.Boolean(string='Control de estados', store=True, copy=True, tracking=0, )
    tarifario_id = fields.Many2one(string='Tarifario', store=True, copy=True, tracking=0,
                                   comodel_name='hr.roster.tarifario', )
    tipo_turno_id = fields.Many2one(string='Tipo Turno', store=True, copy=True, tracking=0,
                                    comodel_name='hr.roster.horario', )
    turno_remplazo_2_id = fields.Many2one(string='Turno que Remplaza', store=True, readonly=True, copy=True,
                                          tracking=0,
                                          comodel_name='hr.roster.turno', )
    turno_remplazo_id = fields.Many2one(string='Remplazado por', store=True, readonly=True, copy=True, tracking=0,
                                        comodel_name='hr.roster.turno', )
    use_parent_modality = fields.Boolean(string='Usa modalidad padre', readonly=True, tracking=0, )


class Unalíneadecontroldecrédito(models.Model):
    _name = 'credit.control.line'
    _description = 'Una línea de control de crédito'
    account_id = fields.Many2one(string='Cuenta', store=True, readonly=True, tracking=100,
                                 comodel_name='account.account', )
    activity_date_deadline = fields.Date(string='Fecha de la siguiente acción', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Fecha de la siguiente acción', tracking=0,
                                       comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    amount_due = fields.Float(string='Importe vencido con imp.', store=True, readonly=True, required=True, copy=True,
                              tracking=0, )
    balance_due = fields.Float(string='Saldo vencido', store=True, readonly=True, required=True, copy=True,
                               tracking=0, )
    commercial_partner_id = fields.Many2one(string='Commercial Entity', index=True, store=True, readonly=True,
                                            tracking=0,
                                            comodel_name='res.partner', )
    communication_id = fields.Many2one(string='Communication process', store=True, copy=True, tracking=0,
                                       comodel_name='credit.control.communication', )
    company_id = fields.Many2one(string='Compañía', store=True, readonly=True, tracking=0, comodel_name='res.company', )
    currency_id = fields.Many2one(string='Divisa', store=True, readonly=True, tracking=0, comodel_name='res.currency', )
    date_due = fields.Date(string='Fecha de vencimiento', store=True, readonly=True, required=True, copy=True,
                           tracking=0, )
    date_entry = fields.Date(string='Fecha del asiento', store=True, readonly=True, tracking=0, )
    date_sent = fields.Date(string='Fecha de ejecución', store=True, readonly=True, copy=True, tracking=0, )
    date = fields.Date(string='Fecha del control', index=True, store=True, readonly=True, required=True, copy=True,
                       tracking=0, )
    invoice_id = fields.Many2one(string='Factura', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='account.move', )
    level = fields.Integer(string='Nivel', store=True, readonly=True, tracking=0, )
    manual_followup = fields.Boolean(string='Seguimiento manual', store=True, copy=True, tracking=0, )
    manually_overridden = fields.Boolean(string='Sobreescrito manualmente', store=True, copy=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='turno_message_channel_ids_rel', column1='turno_id',
                                           column2='message_channel_ids_id', string='Followers (Channels)',
                                           readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Siguiente acción', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Seguimiento', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Siguiente acción', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='turno_message_partner_ids_rel', column1='turno_id',
                                           column2='message_partner_ids_id', string='Followers (Partners)',
                                           readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    move_line_id = fields.Many2one(string='Apunte', index=True, store=True, readonly=True, required=True, copy=True,
                                   tracking=0, comodel_name='account.move.line', )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    partner_id = fields.Many2one(string='Empresa', store=True, readonly=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.partner', )
    partner_user_id = fields.Many2one(string='Salesperson', store=True, readonly=True, tracking=0,
                                      comodel_name='res.users', )
    policy_id = fields.Many2one(string='Política asociada', store=True, readonly=True, tracking=0,
                                comodel_name='credit.control.policy', )
    policy_level_id = fields.Many2one(string='Nivel de retraso', store=True, readonly=True, required=True, copy=True,
                                      tracking=0, comodel_name='credit.control.policy.level', )
    run_id = fields.Many2one(string='Origen', store=True, copy=True, tracking=0, comodel_name='credit.control.run', )


class Uninvoicedserviceorderlines(models.Model):
    _name = 'report.uninvoiced.order.line'
    _description = 'Uninvoiced Service Order Lines'
    adicional_valor = fields.Float(string='Valor adicional', store=True, readonly=True, tracking=0, )
    client_id = fields.Many2one(string='Razon social', store=True, readonly=True, tracking=0,
                                comodel_name='res.partner', )
    date_end = fields.Datetime(string='Fecha finalizacion', store=True, readonly=True, tracking=0, )
    date_from = fields.Datetime(string='Facturar desde', store=True, copy=True, tracking=0, )
    date_start = fields.Datetime(string='Fecha de inicio', store=True, readonly=True, tracking=0, )
    date_to = fields.Datetime(string='Facturar hasta', store=True, copy=True, tracking=0, )
    force_value = fields.Boolean(string='Forzar tarifa especial', store=True, readonly=True, tracking=0, )
    no_cost = fields.Boolean(string='Sin Costo', readonly=True, tracking=0, )
    order_id = fields.Many2one(string='Orden de servicio', store=True, readonly=True, tracking=0,
                               comodel_name='project.service.order', )
    order_line_id = fields.Many2one(string='Linea de servicio', store=True, copy=True, tracking=0,
                                    comodel_name='project.service.order.line', )
    product_id = fields.Many2one(string='Producto', readonly=True, tracking=0, comodel_name='product.product', )
    project_id = fields.Many2one(string='Proyecto', store=True, readonly=True, tracking=0,
                                 comodel_name='project.project', )
    puesto_id = fields.Many2one(string='Puesto asociado', store=True, readonly=True, tracking=0,
                                comodel_name='hr.roster.puesto', )
    valor = fields.Float(string='Valor antes de IVA', store=True, readonly=True, tracking=0, )


class Unniveldepolíticadecontroldecrédito(models.Model):
    _name = 'credit.control.policy.level'
    _description = 'Un nivel de política de control de crédito'
    custom_mail_text = fields.Html(string='Mensaje de correo electrónico personalizado', store=True, required=True,
                                   copy=True, tracking=0, )
    custom_text_after_details = fields.Text(string='Mensaje personalizado después de los detalles', store=True,
                                            copy=True,
                                            tracking=0, )
    custom_text = fields.Text(string='Mensaje personalizado', store=True, required=True, copy=True, tracking=0, )
    delay_days = fields.Integer(string='Retardo (en días)', store=True, required=True, copy=True, tracking=0, )
    email_template_id = fields.Many2one(string='Plantilla de correo', store=True, required=True, copy=True,
                                        tracking=0,
                                        comodel_name='mail.template', )
    level = fields.Integer(string='Nivel', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    policy_id = fields.Many2one(string='Política asociada', store=True, required=True, copy=True, tracking=0,
                                comodel_name='credit.control.policy', )


class Variableeconómica(models.Model):
    _name = 'economic.variable'
    _description = 'Variable económica'
    active = fields.Boolean(string='Activo', store=True, copy=True, tracking=0, )
    code = fields.Char(string='Código', store=True, readonly=True, required=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    compute_value = fields.Boolean(string='Valor calculado', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, readonly=True, required=True, copy=True, tracking=0, )


class Varlidartarifario(models.Model):
    _name = 'validate.tarifario'
    _description = 'Varlidar Tarifario'
    tarifario_ids = fields.Many2many(relation='varlidartarifario_tarifario_ids_rel', column1='varlidartarifario_id',
                                     column2='tarifario_ids_id', string='Tarifario', store=True, copy=True, tracking=0,
                                     comodel_name='hr.roster.tarifario', )


class Vehiculo(models.Model):
    _name = 'delivery.vehicle'
    _description = 'Vehículo'
    active = fields.Boolean(string='Activo', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )


class Vencidaporcobrar(models.Model):
    _name = 'account.aged.receivable'
    _description = 'Vencida por Cobrar'
    account_code = fields.Char(string='Account Code', store=True, copy=True, tracking=0, )
    account_id = fields.Many2one(string='Account', store=True, copy=True, tracking=0,
                                 comodel_name='account.account', )
    account_name = fields.Char(string='Account Name', store=True, copy=True, tracking=0, )
    analytic_account_id = fields.Many2one(string='Analytic Account', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    analytic_tag_ids = fields.Many2many(relation='vencidaporcobrar_analytic_tag_ids_rel', column1='vencidaporcobrar_id',
                                        column2='analytic_tag_ids_id', string='Analytic Tag', store=True, copy=True,
                                        tracking=0,
                                        comodel_name='account.analytic.tag', )
    balance = fields.Monetary(string='Saldo', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Company', store=True, copy=True, tracking=0, comodel_name='res.company', )
    credit = fields.Monetary(string='Credit', store=True, copy=True, tracking=0, )
    currency_id = fields.Many2one(string='Moneda', store=True, copy=True, tracking=0, comodel_name='res.currency', )
    date = fields.Date(string='Date', store=True, copy=True, tracking=0, )
    debit = fields.Monetary(string='Debit', store=True, copy=True, tracking=0, )
    display_type = fields.Char(string='Display Type', store=True, copy=True, tracking=0, )
    expected_pay_date = fields.Date(string='Exp. Date', store=True, copy=True, tracking=0, )
    journal_code = fields.Char(string='Journal Code', store=True, copy=True, tracking=0, )
    journal_id = fields.Many2one(string='Journal', store=True, copy=True, tracking=0,
                                 comodel_name='account.journal', )
    move_id = fields.Many2one(string='Move', store=True, copy=True, tracking=0, comodel_name='account.move', )
    move_name = fields.Char(string='Move Name', store=True, copy=True, tracking=0, )
    move_type = fields.Char(string='Move Type', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Name', store=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Asociado', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    partner_name = fields.Char(string='Partner Name', store=True, copy=True, tracking=0, )
    partner_trust = fields.Char(string='Partner Trust', store=True, copy=True, tracking=0, )
    payment_id = fields.Many2one(string='Payment', store=True, copy=True, tracking=0,
                                 comodel_name='account.payment', )
    period0 = fields.Monetary(string='As of:', store=True, copy=True, tracking=0, )
    period1 = fields.Monetary(string='1 - 30', store=True, copy=True, tracking=0, )
    period2 = fields.Monetary(string='31 - 60', store=True, copy=True, tracking=0, )
    period3 = fields.Monetary(string='61 - 90', store=True, copy=True, tracking=0, )
    period4 = fields.Monetary(string='91 - 120', store=True, copy=True, tracking=0, )
    period5 = fields.Monetary(string='Older', store=True, copy=True, tracking=0, )
    report_currency_id = fields.Many2one(string='Report Currency', store=True, copy=True, tracking=0,
                                         comodel_name='res.currency', )
    report_date = fields.Date(string='Report Date', store=True, copy=True, tracking=0, )


class Vencidaporpagar(models.Model):
    _name = 'account.aged.payable'
    _description = 'Vencida por Pagar'
    account_code = fields.Char(string='Account Code', store=True, copy=True, tracking=0, )
    account_id = fields.Many2one(string='Account', store=True, copy=True, tracking=0,
                                 comodel_name='account.account', )
    account_name = fields.Char(string='Account Name', store=True, copy=True, tracking=0, )
    analytic_account_id = fields.Many2one(string='Analytic Account', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    analytic_tag_ids = fields.Many2many(relation='vencidaporpagar_analytic_tag_ids_rel', column1='vencidaporpagar_id',
                                        column2='analytic_tag_ids_id', string='Analytic Tag', store=True, copy=True,
                                        tracking=0,
                                        comodel_name='account.analytic.tag', )
    balance = fields.Monetary(string='Saldo', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Company', store=True, copy=True, tracking=0, comodel_name='res.company', )
    credit = fields.Monetary(string='Credit', store=True, copy=True, tracking=0, )
    currency_id = fields.Many2one(string='Moneda', store=True, copy=True, tracking=0, comodel_name='res.currency', )
    date = fields.Date(string='Date', store=True, copy=True, tracking=0, )
    debit = fields.Monetary(string='Debit', store=True, copy=True, tracking=0, )
    display_type = fields.Char(string='Display Type', store=True, copy=True, tracking=0, )
    expected_pay_date = fields.Date(string='Exp. Date', store=True, copy=True, tracking=0, )
    journal_code = fields.Char(string='Journal Code', store=True, copy=True, tracking=0, )
    journal_id = fields.Many2one(string='Journal', store=True, copy=True, tracking=0,
                                 comodel_name='account.journal', )
    move_id = fields.Many2one(string='Move', store=True, copy=True, tracking=0, comodel_name='account.move', )
    move_name = fields.Char(string='Move Name', store=True, copy=True, tracking=0, )
    move_type = fields.Char(string='Move Type', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Name', store=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Asociado', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    partner_name = fields.Char(string='Partner Name', store=True, copy=True, tracking=0, )
    partner_trust = fields.Char(string='Partner Trust', store=True, copy=True, tracking=0, )
    payment_id = fields.Many2one(string='Payment', store=True, copy=True, tracking=0,
                                 comodel_name='account.payment', )
    period0 = fields.Monetary(string='As of:', store=True, copy=True, tracking=0, )
    period1 = fields.Monetary(string='1 - 30', store=True, copy=True, tracking=0, )
    period2 = fields.Monetary(string='31 - 60', store=True, copy=True, tracking=0, )
    period3 = fields.Monetary(string='61 - 90', store=True, copy=True, tracking=0, )
    period4 = fields.Monetary(string='91 - 120', store=True, copy=True, tracking=0, )
    period5 = fields.Monetary(string='Older', store=True, copy=True, tracking=0, )
    report_currency_id = fields.Many2one(string='Report Currency', store=True, copy=True, tracking=0,
                                         comodel_name='res.currency', )
    report_date = fields.Date(string='Report Date', store=True, copy=True, tracking=0, )


class Wizardcreatemenu(models.Model):
    _name = 'document.page.create.menu'
    _description = 'Wizard Create Menu'
    menu_name = fields.Char(string='Nombre del menú', store=True, required=True, copy=True, tracking=0, )
    menu_parent_id = fields.Many2one(string='Menú superior', store=True, required=True, copy=True, tracking=0,
                                     comodel_name='ir.ui.menu', )


class Wizardetransferenciaaguía(models.Model):
    _name = 'picking.guide.wizard'
    _description = 'Wizar de Transferencia a Guía'
    driver_id = fields.Many2one(string='Conductor', store=True, copy=True, tracking=0,
                                comodel_name='res.partner.driver', )
    guide_id = fields.Many2one(string='Guía', store=True, copy=True, tracking=0, comodel_name='delivery.guide', )
    partner_id = fields.Many2one(string='Proveedor', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    pickings_ids = fields.Many2many(relation='wizardcreatemenu_pickings_ids_rel', column1='wizardcreatemenu_id',
                                    column2='pickings_ids_id', string='Transferencias', store=True, copy=True,
                                    tracking=0,
                                    comodel_name='stock.picking', )


class Wizardnoveltyadvance(models.Model):
    _name = 'wizard.novelty.advance'
    _description = 'Wizard Novelty Advance'
    date = fields.Date(string='Fecha Referencia', store=True, copy=True, tracking=0, )


class Wizardparaenviarmultiplesfacturaselectrónica(models.Model):
    _name = 'ei.multi.process'
    _description = 'Wizard para enviar multiples facturas electrónica'
    invoices = fields.Text(string='Facturas por Procesar', store=True, readonly=True, copy=True, tracking=0, )


class Wizardparafiltrarlíneasdeordendeservicioporfecha(models.Model):
    _name = 'wizard.service.order.line'
    _description = 'Wizard para filtrar líneas de orden de servicio por fecha'
    date_start = fields.Date(string='Fecha de Calculo', store=True, copy=True, tracking=0, )
    line_ids = fields.Many2many(relation='wizardnoveltyadvance_line_ids_rel', column1='wizardnoveltyadvance_id',
                                column2='line_ids_id', string='Líneas seleccionadas', store=True, readonly=True,
                                copy=True, tracking=0,
                                comodel_name='project.service.order.line', )


class Wizardparaingresarturnosmanuales(models.Model):
    _name = 'manual.entry'
    _description = 'Wizard para ingresar turnos manuales'
    adicional_nom = fields.Boolean(string='Adicional Nomina', store=True, copy=True, tracking=0, )
    category_id = fields.Many2one(string='Concepto de novedad', store=True, copy=True, tracking=0,
                                  comodel_name='hr.novelty.type', )
    date_from = fields.Datetime(string='Desde', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Datetime(string='Hasta', store=True, required=True, copy=True, tracking=0, )
    descanso = fields.Boolean(string='Descanso', store=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, required=True, copy=True, tracking=0,
                                  comodel_name='hr.employee', )
    extra_hour = fields.Boolean(string='Hora Extra', store=True, copy=True, tracking=0, )
    modalidad_id = fields.Many2one(string='Modalidad', store=True, copy=True, tracking=0,
                                   comodel_name='hr.roster.modalidad', )
    programacion_id = fields.Many2one(string='Programacion', store=True, copy=True, tracking=0,
                                      comodel_name='hr.roster.programacion', )
    puesto_id = fields.Many2one(string='Puesto', store=True, copy=True, tracking=0, comodel_name='hr.roster.puesto', )
    tipo_turno_id = fields.Many2one(string='Tipo Turno', store=True, required=True, copy=True, tracking=0,
                                    comodel_name='hr.roster.horario', )


class Wizardtofinduninvoicedserviceorderlines(models.Model):
    _name = 'report.uninvoiced.order.line.wizard'
    _description = 'Wizard to Find Uninvoiced Service Order Lines'
    date_from = fields.Date(string='Date From', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Date To', store=True, required=True, copy=True, tracking=0, )
    journal_id = fields.Many2one(string='Diario', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='account.journal', )


class Workoccupation(models.Model):
    _name = 'hr.work.occupation'
    _description = 'Work Occupation'
    name = fields.Char(string='Ocupación', store=True, copy=True, tracking=0, )


class Zonacontrato(models.Model):
    _name = 'hr.contract.zone'
    _description = 'Zona Contrato'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class Puestos(models.Model):
    _name = 'quoter.position'
    _description = '¨Puestos'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class Cursosdevigilanciavsacreditacion(models.Model):
    _name = 'cursosvigilancia.vs.acreditacion'
    _description = 'Cursos de vigilancia vs. acreditacion'
    academia = fields.Many2one(string='Academia', store=True, required=True, copy=True, tracking=0,
                               comodel_name='academia', )
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Next Activity Type', tracking=0, comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    archivos_adjuntos = fields.Many2many(relation='cursosdevigilanciavs_archivos_adjuntos_rel',
                                         column1='cursosdevigilanciavs_id', column2='archivos_adjuntos_id',
                                         string='Archivos Adjuntos', store=True, copy=True, tracking=0,
                                         comodel_name='ir.attachment', )
    cargo = fields.Char(string='Cargo', store=True, readonly=True, tracking=0, )
    comentario = fields.Text(string='Comentario', store=True, copy=True, tracking=0, )
    empleado = fields.Many2one(string='Empleado', store=True, readonly=True, required=True, copy=True, tracking=0,
                               comodel_name='hr.employee', )
    fecha_realizacion_curso = fields.Date(string='Fecha de realización curso', store=True, required=True, copy=True,
                                          tracking=0, )
    fecha_registro_sistema = fields.Date(string='Fecha de registro en el sistema', store=True, readonly=True,
                                         copy=True,
                                         tracking=0, )
    fecha_vencimiento_acreditacion = fields.Date(string='Fecha de vencimiento acreditación', store=True, copy=True,
                                                 tracking=0, )
    fecha_vencimiento_curso = fields.Date(string='Fecha de vencimiento curso', store=True, copy=True, tracking=0, )
    has_attachments = fields.Boolean(string='Tiene Archivos', readonly=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='cursosdevigilanciavs_message_channel_ids_rel',
                                           column1='cursosdevigilanciavs_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='cursosdevigilanciavs_message_partner_ids_rel',
                                           column1='cursosdevigilanciavs_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    numero_identificacion = fields.Char(string='Número de Identificación', store=True, copy=True, tracking=0, )
    numero_registro = fields.Text(string='Número registro', store=True, required=True, copy=True, tracking=0, )
    tipo = fields.Many2one(string='Tipo', store=True, required=True, copy=True, tracking=0,
                           comodel_name='acreditacion.tipo', )


class Fpaauxiliarline(models.Model):
    _name = 'fpa.auxiliar.line'
    _description = 'fpa.auxiliar.line'
    account_analytic_id = fields.Many2one(string='Cuenta analitica', index=True, store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    account_id = fields.Many2one(string='Cuenta', index=True, store=True, copy=True, tracking=0,
                                 comodel_name='account.account', )
    account_niif_id = fields.Many2one(string='Cuenta NIIF', index=True, store=True, copy=True, tracking=0,
                                      comodel_name='account.account', )
    amount_final = fields.Float(string='Saldo Final', store=True, copy=True, tracking=0, )
    amount_inicial = fields.Float(string='Saldo Inicial', store=True, copy=True, tracking=0, )
    asiento = fields.Char(string='Asiento', store=True, copy=True, tracking=0, )
    bold = fields.Boolean(string='Bold', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', index=True, store=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    concepts_id = fields.Many2one(string='Conceptos', index=True, store=True, copy=True, tracking=0,
                                  comodel_name='fpa.financial.reports.concepts', )
    credit = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    cuenta = fields.Char(string='Cuenta', store=True, copy=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    encabezado_id = fields.Many2one(string='Encabezado', index=True, store=True, copy=True, tracking=0,
                                    comodel_name='fpa.auxiliar', )
    fecha = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )
    financial_id = fields.Many2one(string='Reporte', index=True, store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    journal_id = fields.Many2one(string='Diario', index=True, store=True, copy=True, tracking=0,
                                 comodel_name='account.journal', )
    linea = fields.Char(string='Linea', store=True, copy=True, tracking=0, )
    move_line_id = fields.Many2one(string='Move line', index=True, store=True, copy=True, tracking=0,
                                   comodel_name='account.move.line', )
    nivel = fields.Integer(string='Nivel', store=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Tercero', index=True, store=True, copy=True, tracking=0,
                                 comodel_name='res.partner', )
    resume = fields.Boolean(string='Resumen', store=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    sucursal_name = fields.Char(string='Sucursal', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', index=True, store=True, copy=True, tracking=0,
                              comodel_name='res.users', )


class Fpaauxiliaranaliticoline(models.Model):
    _name = 'fpa.auxiliar.analitico.line'
    _description = 'fpa.auxiliar.analitico.line'
    account_analytic_id = fields.Many2one(string='Cuenta analitica', index=True, store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    account_id = fields.Many2one(string='Cuenta', index=True, store=True, copy=True, tracking=0,
                                 comodel_name='account.account', )
    account_niif_id = fields.Many2one(string='Cuenta NIIF', index=True, store=True, copy=True, tracking=0,
                                      comodel_name='account.account', )
    amount_currency = fields.Float(string='Monto moneda', store=True, copy=True, tracking=0, )
    amount_final = fields.Float(string='Saldo Final', store=True, copy=True, tracking=0, )
    amount_inicial = fields.Float(string='Saldo Inicial', store=True, copy=True, tracking=0, )
    asiento = fields.Char(string='Asiento', store=True, copy=True, tracking=0, )
    bold = fields.Boolean(string='Bold', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', index=True, store=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    concepts_id = fields.Many2one(string='Conceptos', index=True, store=True, copy=True, tracking=0,
                                  comodel_name='fpa.financial.reports.concepts', )
    credit = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    cuenta = fields.Char(string='Cuenta', store=True, copy=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    encabezado_id = fields.Many2one(string='Encabezado', index=True, store=True, copy=True, tracking=0,
                                    comodel_name='fpa.auxiliar.analitico', )
    fecha = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )
    financial_id = fields.Many2one(string='Reporte', index=True, store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    nivel = fields.Integer(string='Nivel', store=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Tercero', index=True, store=True, copy=True, tracking=0,
                                 comodel_name='res.partner', )
    resume = fields.Boolean(string='Resumen', store=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', index=True, store=True, copy=True, tracking=0,
                              comodel_name='res.users', )


class Fpaauxiliarfcline(models.Model):
    _name = 'fpa.auxiliar.fc.line'
    _description = 'fpa.auxiliar.fc.line'
    account_analytic_id = fields.Many2one(string='Cuenta analitica', index=True, store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    account_id = fields.Many2one(string='Cuenta', index=True, store=True, copy=True, tracking=0,
                                 comodel_name='account.account', )
    account_niif_id = fields.Many2one(string='Cuenta NIIF', index=True, store=True, copy=True, tracking=0,
                                      comodel_name='account.account', )
    af_fc = fields.Float(string='SF - ME', store=True, copy=True, tracking=0, )
    ai_fc = fields.Float(string='SI - ME', store=True, copy=True, tracking=0, )
    amount_final = fields.Float(string='Saldo Final', store=True, copy=True, tracking=0, )
    amount_inicial = fields.Float(string='Saldo Inicial', store=True, copy=True, tracking=0, )
    asiento = fields.Char(string='Asiento', store=True, copy=True, tracking=0, )
    bold = fields.Boolean(string='Bold', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', index=True, store=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    concepts_id = fields.Many2one(string='Conceptos', index=True, store=True, copy=True, tracking=0,
                                  comodel_name='fpa.financial.reports.concepts', )
    credit = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    cuenta = fields.Char(string='Cuenta', store=True, copy=True, tracking=0, )
    currency_id = fields.Many2one(string='Moneda', index=True, store=True, copy=True, tracking=0,
                                  comodel_name='res.currency', )
    debit = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    encabezado_id = fields.Many2one(string='Encabezado', index=True, store=True, copy=True, tracking=0,
                                    comodel_name='fpa.auxiliar', )
    fecha = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )
    financial_id = fields.Many2one(string='Reporte', index=True, store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    linea = fields.Char(string='Linea', store=True, copy=True, tracking=0, )
    move_line_id = fields.Many2one(string='Move line', index=True, store=True, copy=True, tracking=0,
                                   comodel_name='account.move.line', )
    mv_fc = fields.Float(string='DC - ME', store=True, copy=True, tracking=0, )
    nivel = fields.Integer(string='Nivel', store=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Tercero', index=True, store=True, copy=True, tracking=0,
                                 comodel_name='res.partner', )
    resume = fields.Boolean(string='Resumen', store=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', index=True, store=True, copy=True, tracking=0,
                              comodel_name='res.users', )


class Fpaauxiliarequivalenteline(models.Model):
    _name = 'fpa.auxiliar.equivalente.line'
    _description = 'fpa.auxiliar.equivalente.line'
    account_analytic_id = fields.Many2one(string='Cuenta analitica', index=True, store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    account_equivalente_id = fields.Many2one(string='Cuenta Equiv. Colgaap', index=True, store=True, copy=True,
                                             tracking=0, comodel_name='account.account', )
    account_id = fields.Many2one(string='Cuenta NIIF', index=True, store=True, copy=True, tracking=0,
                                 comodel_name='account.account', )
    amount_final = fields.Float(string='Saldo Final', store=True, copy=True, tracking=0, )
    amount_inicial = fields.Float(string='Saldo Inicial', store=True, copy=True, tracking=0, )
    asiento = fields.Char(string='Asiento', store=True, copy=True, tracking=0, )
    bold = fields.Boolean(string='Bold', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', index=True, store=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    concepts_id = fields.Many2one(string='Conceptos', index=True, store=True, copy=True, tracking=0,
                                  comodel_name='fpa.financial.reports.concepts', )
    credit_c = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    credit = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    cuenta = fields.Char(string='Cuenta', store=True, copy=True, tracking=0, )
    debit_c = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    encabezado_id = fields.Many2one(string='Encabezado', index=True, store=True, copy=True, tracking=0,
                                    comodel_name='fpa.auxiliar.equivalente', )
    fecha = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )
    financial_id = fields.Many2one(string='Reporte', index=True, store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    move_line_id = fields.Many2one(string='Move line', index=True, store=True, copy=True, tracking=0,
                                   comodel_name='account.move.line', )
    nivel = fields.Integer(string='Nivel', store=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Tercero', index=True, store=True, copy=True, tracking=0,
                                 comodel_name='res.partner', )
    resume = fields.Boolean(string='Resumen', store=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', index=True, store=True, copy=True, tracking=0,
                              comodel_name='res.users', )


class Banktransactionwiz(models.Model):
    _name = 'bank.transaction.wiz'
    _description = 'bank.transaction.wiz'
    account_bank_statement_avancys_id = fields.Many2one(string='Extracto bancario', store=True, copy=True, tracking=0,
                                                        comodel_name='account.bank.statement.avancys', )
    analytic_account_id = fields.Many2one(string='Cuenta analitica', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    date = fields.Date(string='Fecha movimiento', store=True, copy=True, tracking=0, )
    debit_account_id = fields.Many2one(string='Account', store=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    journal_id = fields.Many2one(string='Diario', store=True, copy=True, tracking=0, comodel_name='account.journal', )
    partner_id = fields.Many2one(string='Partner', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    transaction_ids = fields.Many2many(relation='banktransactionwiz_transaction_ids_rel',
                                       column1='banktransactionwiz_id', column2='transaction_ids_id',
                                       string='Selected Transaction', store=True, copy=True, tracking=0,
                                       comodel_name='account.bank.statement.line.avancys', )


class Hrpayrollembargocategory(models.Model):
    _name = 'hr.payroll.embargo.category'
    _description = 'hr.payroll.embargo.category'
    account_credit = fields.Many2one(string='Cuenta credito', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    account_debit = fields.Many2one(string='Cuenta debito', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    analytic_account_id = fields.Many2one(string='Centro de costos', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    apr_adm_credit = fields.Many2one(string='Credito Aprendiz Administrativo', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    apr_adm_debit = fields.Many2one(string='Debito Aprendiz Administrativo', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    apr_com_credit = fields.Many2one(string='Credito Aprendiz Comercial', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    apr_com_debit = fields.Many2one(string='Debito Aprendiz Comercial', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    apr_ope_credit = fields.Many2one(string='Credito Aprendiz Operativa', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    apr_ope_debit = fields.Many2one(string='Debito Aprendiz Operativa', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    code_emb = fields.Char(string='Codigo Archivo', store=True, copy=True, tracking=0, )
    code = fields.Char(string='Codigo', store=True, copy=True, tracking=0, )
    concept_id = fields.Many2one(string='Concepto', store=True, copy=True, tracking=0, comodel_name='hr.concept', )
    description = fields.Text(string='Descripcion', store=True, copy=True, tracking=0, )
    int_adm_credit = fields.Many2one(string='Credito Integral Administrativo', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    int_adm_debit = fields.Many2one(string='Debito Integral Administrativo', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    int_com_credit = fields.Many2one(string='Credito Integral Comercial', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    int_com_debit = fields.Many2one(string='Debito Integral Comercial', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    int_ope_credit = fields.Many2one(string='Credito Integral Operativa', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    int_ope_debit = fields.Many2one(string='Debito Integral Operativa', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Otro tercero', store=True, copy=True, tracking=0,
                                 comodel_name='res.partner', )
    prod_ind_credit = fields.Many2one(string='Credito Costo Indirecto Produccion', store=True, copy=True, tracking=0,
                                      comodel_name='account.account', )
    prod_ind_debit = fields.Many2one(string='Debito Costo Indirecto Produccion', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    reg_adm_credit = fields.Many2one(string='Credito Regular Administrativo', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    reg_adm_debit = fields.Many2one(string='Debito Regular Administrativo', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    reg_com_credit = fields.Many2one(string='Credito Regular Comercial', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    reg_com_debit = fields.Many2one(string='Debito Regular Comercial', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    reg_ope_credit = fields.Many2one(string='Credito Regular Operativa', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    reg_ope_debit = fields.Many2one(string='Debito Regular Operativa', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )


class Fpaauxiliarwizard(models.Model):
    _name = 'fpa.auxiliar.wizard'
    _description = 'fpa.auxiliar.wizard'
    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copy=True, tracking=0, )
    account_ids = fields.Many2many(relation='fpaauxiliarwizard_account_ids_rel', column1='fpaauxiliarwizard_id',
                                   column2='account_ids_id', string='Cuentas', store=True, copy=True, tracking=0,
                                   comodel_name='account.account', )
    analytic_ids = fields.Many2many(relation='fpaauxiliarwizard_analytic_ids_rel', column1='fpaauxiliarwizard_id',
                                    column2='analytic_ids_id', string='Cuentas analiticas', store=True, copy=True,
                                    tracking=0,
                                    comodel_name='account.analytic.account', )
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    detailed = fields.Boolean(string='Detallado', store=True, copy=True, tracking=0, )
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copy=True, tracking=0, )
    journal_ids = fields.Many2many(relation='fpaauxiliarwizard_journal_ids_rel', column1='fpaauxiliarwizard_id',
                                   column2='journal_ids_id', string='Diarios', store=True, copy=True, tracking=0,
                                   comodel_name='account.journal', )
    niveles = fields.Many2many(relation='fpa_aux_wiz_nivel_rel', column1='wiz_id', column2='nivel_id', string='Niveles',
                               copy=False, )
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copy=True, tracking=0, )
    partner_ids = fields.Many2many(relation='fpaauxiliarwizard_partner_ids_rel', column1='fpaauxiliarwizard_id',
                                   column2='partner_ids_id', string='Terceros', store=True, copy=True, tracking=0,
                                   comodel_name='res.partner', )
    period_balance_ids = fields.Many2many(relation='fpa_aux_wiz_period_rel', column1='wiz_id', column2='period_id',
                                          string='Periodos', copy=False, )
    sp_periods = fields.Boolean(string='Apertura/Cierre', store=True, copy=True, tracking=0, )
    sucursal_ids = fields.Many2many(relation='fpaauxiliarwizard_sucursal_ids_rel', column1='fpaauxiliarwizard_id',
                                    column2='sucursal_ids_id', string='Sucursales', store=True, copy=True, tracking=0,
                                    comodel_name='res.regional', )
    totalizado_por_tercero = fields.Boolean(string='Totalizador por tercero', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Fpapygwizard(models.Model):
    _name = 'fpa.pyg.wizard'
    _description = 'fpa.pyg.wizard'
    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copy=True, tracking=0, )
    account_ids = fields.Many2many(relation='fpapygwizard_account_ids_rel', column1='fpapygwizard_id',
                                   column2='account_ids_id', string='Cuentas', store=True, copy=True, tracking=0,
                                   comodel_name='account.account', )
    analytic_filter = fields.Boolean(string='Filtro adicional de cuenta analitica', store=True, copy=True,
                                     tracking=0, )
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    cierre = fields.Boolean(string='Cierre', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Company', readonly=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copy=True, tracking=0, )
    journal_ids = fields.Many2many(relation='fpapygwizard_journal_ids_rel', column1='fpapygwizard_id',
                                   column2='journal_ids_id', string='Diarios', store=True, copy=True, tracking=0,
                                   comodel_name='account.journal', )
    niveles = fields.Many2many(relation='fpa_pyg_wiz_nivel_rel', column1='wiz_id', column2='nivel_id', string='Niveles',
                               copy=False, )
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copy=True, tracking=0, )
    partner_ids = fields.Many2many(relation='fpapygwizard_partner_ids_rel', column1='fpapygwizard_id',
                                   column2='partner_ids_id', string='Terceros', store=True, copy=True, tracking=0,
                                   comodel_name='res.partner', )
    period_balance_ids = fields.Many2many(relation='fpa_pyg_wiz_period_rel', column1='wiz_id', column2='period_id',
                                          string='Periodos', copy=False, )


class Fpapygccwizard(models.Model):
    _name = 'fpa.pyg.cc.wizard'
    _description = 'fpa.pyg.cc.wizard'
    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copy=True, tracking=0, )
    account_ids = fields.Many2many(relation='fpapygccwizard_account_ids_rel', column1='fpapygccwizard_id',
                                   column2='account_ids_id', string='Cuentas', store=True, copy=True, tracking=0,
                                   comodel_name='account.account', )
    analytic_filter = fields.Boolean(string='Filtro adicional de cuenta analitica', store=True, copy=True,
                                     tracking=0, )
    analytic_ids = fields.Many2many(relation='fpapygccwizard_analytic_ids_rel', column1='fpapygccwizard_id',
                                    column2='analytic_ids_id', string='Cuentas analiticas', store=True, copy=True,
                                    tracking=0,
                                    comodel_name='account.analytic.account', )
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    cierre = fields.Boolean(string='Apertura/Cierre', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Company', readonly=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copy=True, tracking=0, )
    journal_ids = fields.Many2many(relation='fpapygccwizard_journal_ids_rel', column1='fpapygccwizard_id',
                                   column2='journal_ids_id', string='Diarios', store=True, copy=True, tracking=0,
                                   comodel_name='account.journal', )
    niveles = fields.Many2many(relation='fpa_pygcc_wiz_nivel_rel', column1='wiz_id', column2='nivel_id',
                               string='Niveles',
                               copy=False, )
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copy=True, tracking=0, )
    partner_ids = fields.Many2many(relation='fpapygccwizard_partner_ids_rel', column1='fpapygccwizard_id',
                                   column2='partner_ids_id', string='Terceros', store=True, copy=True, tracking=0,
                                   comodel_name='res.partner', )
    period_balance_ids = fields.Many2many(relation='fpa_pygcc_wiz_period_rel', column1='wiz_id', column2='period_id',
                                          string='Periodos', copy=False, )


class Fpaauxiliarequivalentewizard(models.Model):
    _name = 'fpa.auxiliar.equivalente.wizard'
    _description = 'fpa.auxiliar.equivalente.wizard'
    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copy=True, tracking=0, )
    account_ids = fields.Many2many(relation='fpaauxiliarequivalen_account_ids_rel', column1='fpaauxiliarequivalen_id',
                                   column2='account_ids_id', string='Cuentas', store=True, copy=True, tracking=0,
                                   comodel_name='account.account', )
    analytic_ids = fields.Many2many(relation='fpaauxiliarequivalen_analytic_ids_rel', column1='fpaauxiliarequivalen_id',
                                    column2='analytic_ids_id', string='Cuentas analiticas', store=True, copy=True,
                                    tracking=0,
                                    comodel_name='account.analytic.account', )
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copy=True, tracking=0, )
    journal_ids = fields.Many2many(relation='fpaauxiliarequivalen_journal_ids_rel', column1='fpaauxiliarequivalen_id',
                                   column2='journal_ids_id', string='Diarios', store=True, copy=True, tracking=0,
                                   comodel_name='account.journal', )
    niveles = fields.Many2many(
        relation='fpa_aux_eq_wiz_nivel_rel',
        column1='wiz_id',
        column2='nivel_id',
        string='Niveles',
        copy=False,
    )
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copy=True, tracking=0, )
    partner_ids = fields.Many2many(relation='fpaauxiliarequivalen_partner_ids_rel', column1='fpaauxiliarequivalen_id',
                                   column2='partner_ids_id', string='Terceros', store=True, copy=True, tracking=0,
                                   comodel_name='res.partner', )
    period_balance_ids = fields.Many2many(
        relation='fpa_aux_eq_wiz_period_rel',
        column1='wiz_id',
        column2='period_id',
        string='Periodos',
        copy=False,
    )
    sp_periods = fields.Boolean(string='Apertura/Cierre', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Fpapygccanalyticwizard(models.Model):
    _name = 'fpa.pyg.cc.analytic.wizard'
    _description = 'fpa.pyg.cc.analytic.wizard'
    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copy=True, tracking=0, )
    account_ids = fields.Many2many(relation='fpapygccanalyticwiza_account_ids_rel', column1='fpapygccanalyticwiza_id',
                                   column2='account_ids_id', string='Cuentas', store=True, copy=True, tracking=0,
                                   comodel_name='account.account', )
    analytic_filter = fields.Boolean(string='Filtro adicional de cuenta analitica', store=True, copy=True,
                                     tracking=0, )
    analytic_ids = fields.Many2many(relation='fpapygccanalyticwiza_analytic_ids_rel', column1='fpapygccanalyticwiza_id',
                                    column2='analytic_ids_id', string='Cuentas analiticas', store=True, copy=True,
                                    tracking=0,
                                    comodel_name='account.analytic.account', )
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    cierre = fields.Boolean(string='Cierre', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Company', readonly=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copy=True, tracking=0, )
    journal_ids = fields.Many2many(relation='fpapygccanalyticwiza_journal_ids_rel', column1='fpapygccanalyticwiza_id',
                                   column2='journal_ids_id', string='Diarios', store=True, copy=True, tracking=0,
                                   comodel_name='account.journal', )
    niveles = fields.Many2many(
        relation='fpa_pygcc_an_wiz_nivel_rel',
        column1='wiz_id',
        column2='nivel_id',
        string='Niveles',
        copy=False,
    )
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copy=True, tracking=0, )
    partner_ids = fields.Many2many(relation='fpapygccanalyticwiza_partner_ids_rel', column1='fpapygccanalyticwiza_id',
                                   column2='partner_ids_id', string='Terceros', store=True, copy=True, tracking=0,
                                   comodel_name='res.partner', )
    period_balance_ids = fields.Many2many(
        relation='fpa_pygcc_an_wiz_period_rel',
        column1='wiz_id',
        column2='period_id',
        string='Periodos',
        copy=False,
    )


class Fpadiariowizard(models.Model):
    _name = 'fpa.diario.wizard'
    _description = 'fpa.diario.wizard'
    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copy=True, tracking=0, )
    account_ids = fields.Many2many(relation='fpadiariowizard_account_ids_rel', column1='fpadiariowizard_id',
                                   column2='account_ids_id', string='Cuentas', store=True, copy=True, tracking=0,
                                   comodel_name='account.account', )
    analytic_ids = fields.Many2many(relation='fpadiariowizard_analytic_ids_rel', column1='fpadiariowizard_id',
                                    column2='analytic_ids_id', string='Cuentas analiticas', store=True, copy=True,
                                    tracking=0,
                                    comodel_name='account.analytic.account', )
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    company_id = fields.Many2one(string='Company', readonly=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copy=True, tracking=0, )
    journal_ids = fields.Many2many(relation='fpadiariowizard_journal_ids_rel', column1='fpadiariowizard_id',
                                   column2='journal_ids_id', string='Diarios', store=True, copy=True, tracking=0,
                                   comodel_name='account.journal', )
    niveles = fields.Many2many(
        relation='fpa_diario_wiz_nivel_rel',
        column1='wiz_id',
        column2='nivel_id',
        string='Niveles',
        copy=False,
    )
    period_balance_ids = fields.Many2many(
        relation='fpa_diario_wiz_period_rel',
        column1='wiz_id',
        column2='period_id',
        string='Periodos',
        copy=False,
    )
    sp_periods = fields.Boolean(string='Apertura/Cierre', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Fpaflujocajawizard(models.Model):
    _name = 'fpa.flujocaja.wizard'
    _description = 'fpa.flujocaja.wizard'
    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copy=True, tracking=0, )
    account_ids = fields.Many2many(relation='fpaflujocajawizard_account_ids_rel', column1='fpaflujocajawizard_id',
                                   column2='account_ids_id', string='Cuentas', store=True, copy=True, tracking=0,
                                   comodel_name='account.account', )
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    company_id = fields.Many2one(string='Company', readonly=True, tracking=0, comodel_name='res.company', )
    fiscalyear_id = fields.Many2one(string='Año fiscal', store=True, required=True, copy=True, tracking=0,
                                    comodel_name='_unknown', )
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copy=True, tracking=0, )
    journal_ids = fields.Many2many(relation='fpaflujocajawizard_journal_ids_rel', column1='fpaflujocajawizard_id',
                                   column2='journal_ids_id', string='Diarios', store=True, copy=True, tracking=0,
                                   comodel_name='account.journal', )
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copy=True, tracking=0, )
    period_balance_ids = fields.Many2many(relation='fpaflujocajawizard_period_balance_ids_rel',
                                          column1='fpaflujocajawizard_id', column2='period_balance_ids_id',
                                          string='Periodos', store=True, copy=True, tracking=0,
                                          comodel_name='_unknown', )


class Fpapygcwizard(models.Model):
    _name = 'fpa.pyg.c.wizard'
    _description = 'fpa.pyg.c.wizard'
    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copy=True, tracking=0, )
    account_ids = fields.Many2many(relation='fpapygcwizard_account_ids_rel', column1='fpapygcwizard_id',
                                   column2='account_ids_id', string='Cuentas', store=True, copy=True, tracking=0,
                                   comodel_name='account.account', )
    analytic_filter = fields.Boolean(string='Filtro adicional de cuenta analitica', store=True, copy=True,
                                     tracking=0, )
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    cierre = fields.Boolean(string='Cierre', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Company', readonly=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copy=True, tracking=0, )
    journal_ids = fields.Many2many(relation='fpapygcwizard_journal_ids_rel', column1='fpapygcwizard_id',
                                   column2='journal_ids_id', string='Diarios', store=True, copy=True, tracking=0,
                                   comodel_name='account.journal', )
    niveles = fields.Many2many(
        relation='fpa_pygc_wiz_nivel_rel',
        column1='wiz_id',
        column2='nivel_id',
        string='Niveles',
        copy=False,
    )
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copy=True, tracking=0, )
    partner_ids = fields.Many2many(relation='fpapygcwizard_partner_ids_rel', column1='fpapygcwizard_id',
                                   column2='partner_ids_id', string='Terceros', store=True, copy=True, tracking=0,
                                   comodel_name='res.partner', )
    period_balance_ids = fields.Many2many(
        relation='fpa_pygc_wiz_period_rel',
        column1='wiz_id',
        column2='period_id',
        string='Periodos',
        copy=False,
    )
    period_range = fields.Many2one(string='Rango de periodos', store=True, required=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports.period_range', )


class Fpafinancialreports(models.Model):
    _name = 'fpa.financial.reports'
    _description = 'fpa.financial.reports'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    account_filter = fields.Boolean(string='Filtro adicional de cuentas', copy=True)
    account_ids = fields.Many2many(comodel_name='account.account', relation='fpa_acc_rel', column1='fpa_id',
                                   column2='acc_id', string='Cuentas', copy=False, )
    accumulated = fields.Boolean(string='Acumulado', copy=True)
    action = fields.Char(string='Accion', copy=True)
    analytic_filter = fields.Boolean(string='Filtro adicional de cuentas analiticas', copy=True)
    analyze = fields.Boolean(string='Analizar', copy=True)
    cierre = fields.Boolean(string='Cierre', copy=True)
    clase = fields.Boolean(string='Clase', copy=True)
    codigo = fields.Boolean(string='Código', copy=True)
    consulta_xlsx = fields.Text(string='Consulta XLSX', copy=True)
    consulta = fields.Text(string='Consulta PDF', copy=True)
    detailed = fields.Boolean(string='Detallado', copy=True)
    detalle = fields.Boolean(string='Detalle', copy=True)
    domain = fields.Char(string='Dominio vista tree', copy=True)
    equivalente = fields.Boolean(string='Equivalente NIIF', copy=True)
    exlusion_journal_ids = fields.Many2many(comodel_name='account.journal', relation='fpa_journal_excl_rel',
                                            column1='fpa_id', column2='journal_id', string='Diarios a excluir',
                                            copy=False, )
    export_contract = fields.Boolean(string='Contatos', copy=True)
    export = fields.Boolean(string='Exportacion', copy=True)
    field_hidden = fields.Char(string='Campos a ocultar', copy=True)
    fields_name = fields.Char(string='Campos', copy=True)
    form = fields.Char(string='Form', copy=True)
    format_date = fields.Char(string='Formato Fecha', copy=True)
    format_money = fields.Char(string='Formato Dinero', copy=True)
    formato = fields.Char(string='Formato', copy=True)
    from_merge = fields.Many2one('fpa.financial.reports.concepts', string='Concepto a mezclar', copy=True,
                                 ondelete='set null', )
    indentacion = fields.Integer(string='Indentacion', copy=True)
    is_payslip = fields.Boolean(string='Es Nomina', copy=True)
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', copy=True)
    mode = fields.Char(string='Modo de vista', required=True, copy=True)
    model_wzr = fields.Char(string='Modelo Wizard', copy=True)
    model = fields.Char(string='Modelo', copy=True)
    name = fields.Char(string='Nombre del reporte', copy=True)
    numeric = fields.Char(string='Columnas moneda', copy=True)
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', copy=True)
    porc = fields.Char(string='Columnas %', copy=True)
    query = fields.Text(string='Consulta SQL', copy=True)
    search_default = fields.Char(string='Search por defecto (tree)', copy=True)
    sign = fields.Boolean(string='Invertir signo', copy=True)
    sum_column = fields.Boolean(string='Totalizar', copy=True)
    template = fields.Char(string='Plantilla QWEB', copy=True)
    title_color = fields.Char(string='Color titulos', copy=True)
    title = fields.Char(string='Titulo', copy=True)
    to_merge = fields.Many2one('fpa.financial.reports.concepts', string='Concepto destino para mezclar',
                               copy=True, ondelete='set null', )
    tope_min = fields.Float(string='Tope minimo', copy=True)
    totalizado_por_tercero = fields.Boolean(string='Totalizado por tercero', copy=True)
    tree = fields.Char(string='Tree', copy=True)
    unidades = fields.Char(string='Unidades', copy=True)
    view_color = fields.Char(string='Color resumen', copy=True)
    view = fields.Char(string='Vista', copy=True)
    with_exlusion = fields.Boolean(string='Con Exclusion', copy=True)
    with_min_cuantias = fields.Boolean(string='Con CUANTÍAS MENORES', copy=True)


class Fpabalancepruebaswizard(models.Model):
    _name = 'fpa.balance.pruebas.wizard'
    _description = 'fpa.balance.pruebas.wizard'
    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copy=True, tracking=0, )
    account_ids = fields.Many2many(relation='fpabalancepruebaswiz_account_ids_rel', column1='fpabalancepruebaswiz_id',
                                   column2='account_ids_id', string='Cuentas', store=True, copy=True, tracking=0,
                                   comodel_name='account.account', )
    analytic_ids = fields.Many2many(relation='fpabalancepruebaswiz_analytic_ids_rel', column1='fpabalancepruebaswiz_id',
                                    column2='analytic_ids_id', string='Cuentas analiticas', store=True, copy=True,
                                    tracking=0,
                                    comodel_name='account.analytic.account', )
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    cierre = fields.Boolean(string='Cierre', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Company', readonly=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copy=True, tracking=0, )
    journal_ids = fields.Many2many(relation='fpabalancepruebaswiz_journal_ids_rel', column1='fpabalancepruebaswiz_id',
                                   column2='journal_ids_id', string='Diarios', store=True, copy=True, tracking=0,
                                   comodel_name='account.journal', )
    niveles = fields.Many2many(
        relation='fpa_balpr_wiz_nivel_rel',
        column1='wiz_id',
        column2='nivel_id',
        string='Niveles',
        copy=False,
    )
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copy=True, tracking=0, )
    partner_ids = fields.Many2many(relation='fpabalancepruebaswiz_partner_ids_rel', column1='fpabalancepruebaswiz_id',
                                   column2='partner_ids_id', string='Terceros', store=True, copy=True, tracking=0,
                                   comodel_name='res.partner', )
    period_balance_ids = fields.Many2many(
        relation='fpa_balpr_wiz_period_rel',
        column1='wiz_id',
        column2='period_id',
        string='Periodos',
        copy=False,
    )
    regional_ids = fields.Many2many(relation='fpabalancepruebaswiz_regional_ids_rel', column1='fpabalancepruebaswiz_id',
                                    column2='regional_ids_id', string='Sucursales', store=True, copy=True, tracking=0,
                                    comodel_name='res.regional', )
    resume = fields.Boolean(string='Resumen', store=True, copy=True, tracking=0, )
    sp_periods = fields.Boolean(string='Apertura/Cierre', store=True, copy=True, tracking=0, )


class Fpainventariobalancewizard(models.Model):
    _name = 'fpa.inventario.balance.wizard'
    _description = 'fpa.inventario.balance.wizard'
    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copy=True, tracking=0, )
    account_ids = fields.Many2many(relation='fpainventariobalance_account_ids_rel', column1='fpainventariobalance_id',
                                   column2='account_ids_id', string='Cuentas', store=True, copy=True, tracking=0,
                                   comodel_name='account.account', )
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    company_id = fields.Many2one(string='Company', readonly=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copy=True, tracking=0, )
    journal_ids = fields.Many2many(relation='fpainventariobalance_journal_ids_rel', column1='fpainventariobalance_id',
                                   column2='journal_ids_id', string='Diarios', store=True, copy=True, tracking=0,
                                   comodel_name='account.journal', )
    niveles = fields.Many2many(
        relation='fpa_invbal_wiz_nivel_rel',
        column1='wiz_id',
        column2='nivel_id',
        string='Niveles',
        copy=False,
    )
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copy=True, tracking=0, )
    period_balance_ids = fields.Many2many(
        relation='fpa_invbal_wiz_period_rel',
        column1='wiz_id',
        column2='period_id',
        string='Periodos',
        copy=False,
    )
    sp_periods = fields.Boolean(string='Apertura/Cierre', store=True, copy=True, tracking=0, )


class Fpamayorbalancewizard(models.Model):
    _name = 'fpa.mayor.balance.wizard'
    _description = 'fpa.mayor.balance.wizard'
    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copy=True, tracking=0, )
    account_ids = fields.Many2many(relation='fpamayorbalancewizar_account_ids_rel', column1='fpamayorbalancewizar_id',
                                   column2='account_ids_id', string='Cuentas', store=True, copy=True, tracking=0,
                                   comodel_name='account.account', )
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    cierre = fields.Boolean(string='Cierre', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Company', readonly=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copy=True, tracking=0, )
    journal_ids = fields.Many2many(relation='fpamayorbalancewizar_journal_ids_rel', column1='fpamayorbalancewizar_id',
                                   column2='journal_ids_id', string='Diarios', store=True, copy=True, tracking=0,
                                   comodel_name='account.journal', )
    niveles = fields.Many2many(
        relation='fpa_maybal_wiz_nivel_rel',
        column1='wiz_id',
        column2='nivel_id',
        string='Niveles',
        copy=False,
    )
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copy=True, tracking=0, )
    partner_ids = fields.Many2many(relation='fpamayorbalancewizar_partner_ids_rel', column1='fpamayorbalancewizar_id',
                                   column2='partner_ids_id', string='Terceros', store=True, copy=True, tracking=0,
                                   comodel_name='res.partner', )
    period_balance_ids = fields.Many2many(
        relation='fpa_maybal_wiz_period_rel',
        column1='wiz_id',
        column2='period_id',
        string='Periodos',
        copy=False,
    )

    sp_periods = fields.Boolean(string='Apertura/Cierre', store=True, copy=True, tracking=0, )


class Fpaauxiliarfcwizard(models.Model):
    _name = 'fpa.auxiliar.fc.wizard'
    _description = 'fpa.auxiliar.fc.wizard'
    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copy=True, tracking=0, )
    account_ids = fields.Many2many(relation='fpaauxiliarfcwizard_account_ids_rel', column1='fpaauxiliarfcwizard_id',
                                   column2='account_ids_id', string='Cuentas', store=True, copy=True, tracking=0,
                                   comodel_name='account.account', )
    analytic_ids = fields.Many2many(relation='fpaauxiliarfcwizard_analytic_ids_rel', column1='fpaauxiliarfcwizard_id',
                                    column2='analytic_ids_id', string='Cuentas analiticas', store=True, copy=True,
                                    tracking=0,
                                    comodel_name='account.analytic.account', )
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    currency_ids = fields.Many2many(relation='fpaauxiliarfcwizard_currency_ids_rel', column1='fpaauxiliarfcwizard_id',
                                    column2='currency_ids_id', string='Monedas', store=True, copy=True, tracking=0,
                                    comodel_name='res.currency', )
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copy=True, tracking=0, )
    journal_ids = fields.Many2many(relation='fpaauxiliarfcwizard_journal_ids_rel', column1='fpaauxiliarfcwizard_id',
                                   column2='journal_ids_id', string='Diarios', store=True, copy=True, tracking=0,
                                   comodel_name='account.journal', )
    niveles = fields.Many2many(
        relation='fpa_auxfc_wiz_nivel_rel',
        column1='wiz_id',
        column2='nivel_id',
        string='Niveles',
        copy=False,
    )
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copy=True, tracking=0, )
    partner_ids = fields.Many2many(relation='fpaauxiliarfcwizard_partner_ids_rel', column1='fpaauxiliarfcwizard_id',
                                   column2='partner_ids_id', string='Terceros', store=True, copy=True, tracking=0,
                                   comodel_name='res.partner', )
    period_balance_ids = fields.Many2many(
        relation='fpa_auxfc_wiz_period_rel',
        column1='wiz_id',
        column2='period_id',
        string='Periodos',
        copy=False,
    )
    sp_periods = fields.Boolean(string='Apertura/Cierre', store=True, copy=True, tracking=0, )
    structure_id = fields.Many2one(string='Estructura', store=True, required=True, copy=True, tracking=0,
                                   comodel_name='account.financial.structure', )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Fpaauxiliaranaliticowizard(models.Model):
    _name = 'fpa.auxiliar.analitico.wizard'
    _description = 'fpa.auxiliar.analitico.wizard'
    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copy=True, tracking=0, )
    account_ids = fields.Many2many(relation='fpaauxiliaranalitico_account_ids_rel', column1='fpaauxiliaranalitico_id',
                                   column2='account_ids_id', string='Cuentas', store=True, copy=True, tracking=0,
                                   comodel_name='account.account', )
    analytic_filter = fields.Boolean(string='Filtro adicional de cuenta analitica', store=True, copy=True,
                                     tracking=0, )
    analytic_ids = fields.Many2many(relation='fpaauxiliaranalitico_analytic_ids_rel', column1='fpaauxiliaranalitico_id',
                                    column2='analytic_ids_id', string='Cuentas analiticas', store=True, copy=True,
                                    tracking=0,
                                    comodel_name='account.analytic.account', )
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copy=True, tracking=0, )
    journal_ids = fields.Many2many(relation='fpaauxiliaranalitico_journal_ids_rel', column1='fpaauxiliaranalitico_id',
                                   column2='journal_ids_id', string='Diarios analiticos', store=True, copy=True,
                                   tracking=0,
                                   comodel_name='account.journal', )
    niveles = fields.Many2many(
        relation='fpa_auxan_wiz_nivel_rel',
        column1='wiz_id',
        column2='nivel_id',
        string='Niveles',
        copy=False,
    )
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copy=True, tracking=0, )
    partner_ids = fields.Many2many(relation='fpaauxiliaranalitico_partner_ids_rel', column1='fpaauxiliaranalitico_id',
                                   column2='partner_ids_id', string='Terceros', store=True, copy=True, tracking=0,
                                   comodel_name='res.partner', )
    period_balance_ids = fields.Many2many(
        relation='fpa_auxan_wiz_period_rel',
        column1='wiz_id',
        column2='period_id',
        string='Periodos',
        copy=False,
    )
    show_currency = fields.Boolean(string='Mostrar valor en otra moneda', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Fpaequitychangeswizard(models.Model):
    _name = 'fpa.equity.changes.wizard'
    _description = 'fpa.equity.changes.wizard'
    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copy=True, tracking=0, )
    account_ids = fields.Many2many(relation='fpaequitychangeswiza_account_ids_rel', column1='fpaequitychangeswiza_id',
                                   column2='account_ids_id', string='Cuentas', store=True, copy=True, tracking=0,
                                   comodel_name='account.account', )
    analytic_filter = fields.Boolean(string='Filtro adicional de cuenta analitica', store=True, copy=True,
                                     tracking=0, )
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    cierre = fields.Boolean(string='Cierre', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Company', readonly=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copy=True, tracking=0, )
    journal_ids = fields.Many2many(relation='fpaequitychangeswiza_journal_ids_rel', column1='fpaequitychangeswiza_id',
                                   column2='journal_ids_id', string='Diarios', store=True, copy=True, tracking=0,
                                   comodel_name='account.journal', )
    niveles = fields.Many2many(
        relation='fpa_eqchg_wiz_nivel_rel',
        column1='wiz_id',
        column2='nivel_id',
        string='Niveles',
        copy=False,
    )
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copy=True, tracking=0, )
    partner_ids = fields.Many2many(relation='fpaequitychangeswiza_partner_ids_rel', column1='fpaequitychangeswiza_id',
                                   column2='partner_ids_id', string='Terceros', store=True, copy=True, tracking=0,
                                   comodel_name='res.partner', )
    period_balance_ids = fields.Many2many(
        relation='fpa_eqchg_wiz_period_rel',
        column1='wiz_id',
        column2='period_id',
        string='Periodos',
        copy=False,
    )
    period_range = fields.Many2one(string='Rango de periodos', store=True, required=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports.period_range', )


class Fpaflujocajaline(models.Model):
    _name = 'fpa.flujocaja.line'
    _description = 'fpa.flujocaja.line'
    account_id = fields.Many2one(string='Cuenta', store=True, copy=True, tracking=0, comodel_name='account.account', )
    amount_01 = fields.Float(string='Enero', store=True, copy=True, tracking=0, )
    amount_02 = fields.Float(string='Febrero', store=True, copy=True, tracking=0, )
    amount_03 = fields.Float(string='Marzo', store=True, copy=True, tracking=0, )
    amount_04 = fields.Float(string='Abril', store=True, copy=True, tracking=0, )
    amount_05 = fields.Float(string='Mayo', store=True, copy=True, tracking=0, )
    amount_06 = fields.Float(string='Junio', store=True, copy=True, tracking=0, )
    amount_07 = fields.Float(string='Julio', store=True, copy=True, tracking=0, )
    amount_08 = fields.Float(string='Agosto', store=True, copy=True, tracking=0, )
    amount_09 = fields.Float(string='Septiembre', store=True, copy=True, tracking=0, )
    amount_10 = fields.Float(string='Octubre', store=True, copy=True, tracking=0, )
    amount_11 = fields.Float(string='Noviembre', store=True, copy=True, tracking=0, )
    amount_12 = fields.Float(string='Diciembre', store=True, copy=True, tracking=0, )
    amount_total = fields.Float(string='Monto total', store=True, copy=True, tracking=0, )
    bold = fields.Boolean(string='Bold', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    concepts_id = fields.Many2one(string='Conceptos', store=True, copy=True, tracking=0,
                                  comodel_name='fpa.financial.reports.concepts', )
    cuenta = fields.Char(string='Cuenta', store=True, copy=True, tracking=0, )
    description = fields.Text(string='Descripción', store=True, copy=True, tracking=0, )
    encabezado_id = fields.Many2one(string='Encabezado', store=True, copy=True, tracking=0,
                                    comodel_name='fpa.flujocaja', )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    nivel = fields.Integer(string='Nivel', store=True, copy=True, tracking=0, )
    resume = fields.Boolean(string='Resumen', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Carteraavancysline(models.Model):
    _name = 'cartera.avancys.line'
    _description = 'cartera.avancys.line'
    account_id = fields.Many2one(string='Cuenta', store=True, copy=True, tracking=0, comodel_name='account.account', )
    currency_facturado_rate = fields.Float(string='Valor Facturado Currency Rate', store=True, copy=True,
                                           tracking=0, )
    currency_facturado = fields.Float(string='Valor Facturado Currency', store=True, copy=True, tracking=0, )
    currency_id = fields.Many2one(string='Moneda', store=True, copy=True, tracking=0, comodel_name='res.currency', )
    currency_residual_rate = fields.Float(string='Valor Adeudado Currency Rate', store=True, copy=True, tracking=0, )
    currency_residual = fields.Float(string='Valor Adeudado Currency', store=True, copy=True, tracking=0, )
    date_emision = fields.Datetime(string='Fecha Emision Informe', store=True, copy=True, tracking=0, )
    date = fields.Date(string='Fecha de Corte', store=True, copy=True, tracking=0, )
    en_mora = fields.Boolean(string='En Mora', store=True, copy=True, tracking=0, )
    fecha_elaboracion = fields.Date(string='Fecha de elaboracion', store=True, copy=True, tracking=0, )
    fecha_vencimiento = fields.Date(string='Fecha de vencimiento', store=True, copy=True, tracking=0, )
    foreign_currency_id = fields.Many2one(string='Moneda Extranjera', store=True, copy=True, tracking=0,
                                          comodel_name='res.currency', )
    move_id = fields.Many2one(string='Factura', store=True, copy=True, tracking=0, comodel_name='account.move', )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    numero_dias_expedicion = fields.Integer(string='Numero de dias de Expedicion', store=True, copy=True,
                                            tracking=0, )
    numero_dias_vencidos = fields.Integer(string='Numero de dias Vencidos', store=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Tercero', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    plazo_pago_id = fields.Many2one(string='Plazo de Pago', store=True, copy=True, tracking=0,
                                    comodel_name='account.payment.term', )
    rango = fields.Char(string='Rango', store=True, copy=True, tracking=0, )
    valor_facturado = fields.Float(string='Valor Facturado', store=True, copy=True, tracking=0, )
    valor_residual = fields.Float(string='Valor Adeudado', store=True, copy=True, tracking=0, )


class Fpapygccanalyticline(models.Model):
    _name = 'fpa.pyg.cc.analytic.line'
    _description = 'fpa.pyg.cc.analytic.line'
    account_id = fields.Many2one(string='Cuenta', store=True, copy=True, tracking=0, comodel_name='account.account', )
    amount_1 = fields.Float(string='Saldo Año 1', store=True, copy=True, tracking=0, )
    amount_2 = fields.Float(string='Saldo Año 2', store=True, copy=True, tracking=0, )
    amount_3 = fields.Float(string='Saldo Año 3', store=True, copy=True, tracking=0, )
    amount_4 = fields.Float(string='Saldo Año 4', store=True, copy=True, tracking=0, )
    amount_5 = fields.Float(string='Saldo Año 5', store=True, copy=True, tracking=0, )
    amount_final = fields.Float(string='Saldo Final', store=True, copy=True, tracking=0, )
    amount_inicial = fields.Float(string='Saldo Inicial', store=True, copy=True, tracking=0, )
    analytic_account_id = fields.Many2one(string='Cuenta analitica', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    bold = fields.Boolean(string='Bold', store=True, copy=True, tracking=0, )
    cc1 = fields.Char(string='cc1', store=True, copy=True, tracking=0, )
    cc2 = fields.Char(string='cc2', store=True, copy=True, tracking=0, )
    cc3 = fields.Char(string='cc3', store=True, copy=True, tracking=0, )
    cc4 = fields.Char(string='cc4', store=True, copy=True, tracking=0, )
    cc5 = fields.Char(string='cc5', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    concepts_id = fields.Many2one(string='Conceptos', store=True, copy=True, tracking=0,
                                  comodel_name='fpa.financial.reports.concepts', )
    credit = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    cuenta = fields.Char(string='Cuenta', store=True, copy=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    encabezado_id = fields.Many2one(string='Encabezado', store=True, copy=True, tracking=0,
                                    comodel_name='fpa.pyg.cc.analytic', )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    nivel = fields.Integer(string='Nivel', store=True, copy=True, tracking=0, )
    resume = fields.Boolean(string='Resumen', store=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Printcertificadoretencionline(models.Model):
    _name = 'print.certificado.retencion.line'
    _description = 'print.certificado.retencion.line'
    account_id = fields.Many2one(string='Cuenta/Impuesto', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='account.account', )
    base_amount = fields.Float(string='Base', store=True, readonly=True, copy=True, tracking=0, )
    certificado_print_id = fields.Many2one(string='Certificado', store=True, copy=True, tracking=0,
                                           comodel_name='print.certificado.retencion', )
    company_id = fields.Many2one(string='Compañia', store=True, readonly=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    count = fields.Integer(string='Movimientos', store=True, readonly=True, copy=True, tracking=0, )
    invoice_ids = fields.Char(string='Facturas', store=True, readonly=True, copy=True, tracking=0, )
    name = fields.Char(string='Name', store=True, readonly=True, copy=True, tracking=0, )
    note = fields.Char(string='Descripcion', store=True, readonly=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Tercero', store=True, readonly=True, copy=True, tracking=0,
                                 comodel_name='res.partner', )
    porcentaje = fields.Float(string='Porcentaje', store=True, readonly=True, copy=True, tracking=0, )
    tax_amount_parent = fields.Float(string='Base Padre', store=True, readonly=True, copy=True, tracking=0, )
    tax_amount = fields.Float(string='Retenido', store=True, readonly=True, copy=True, tracking=0, )
    tax_id = fields.Many2one(string='Id_Impuesto', store=True, readonly=True, copy=True, tracking=0,
                             comodel_name='account.tax', )


class Accountaccountestructure(models.Model):
    _name = 'account.account.estructure'
    _description = 'account.account.estructure'
    account_id = fields.Many2one(string='Cuenta', store=True, copy=True, tracking=0, comodel_name='account.account', )
    description = fields.Char(string='Descripcion', store=True, required=True, copy=True, tracking=0, )
    digits = fields.Integer(string='Digitos', store=True, required=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, required=True, copy=True, tracking=0, )


class Quoterconfaccount(models.Model):
    _name = 'quoter.conf.account'
    _description = 'quoter.conf.account'
    account_id = fields.Many2one(string='Cuenta', store=True, copy=True, tracking=0, comodel_name='account.account', )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class Fpabalancepruebasline(models.Model):
    _name = 'fpa.balance.pruebas.line'
    _description = 'fpa.balance.pruebas.line'
    account_id = fields.Many2one(string='Cuenta', store=True, copy=True, tracking=0, comodel_name='account.account', )
    amount_final = fields.Float(string='Saldo Final', store=True, copy=True, tracking=0, )
    amount_inicial = fields.Float(string='Saldo Inicial', store=True, copy=True, tracking=0, )
    bold = fields.Boolean(string='Bold', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    concepts_id = fields.Many2one(string='Conceptos', store=True, copy=True, tracking=0,
                                  comodel_name='fpa.financial.reports.concepts', )
    credit = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    cuenta = fields.Char(string='Cuenta', store=True, copy=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    encabezado_id = fields.Many2one(string='Encabezado', store=True, copy=True, tracking=0,
                                    comodel_name='fpa.balance.pruebas', )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    nivel = fields.Integer(string='Nivel', store=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Tercero', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    resume = fields.Boolean(string='Resumen', store=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    sucursal_name = fields.Char(string='Sucursal', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Fpainventariobalanceline(models.Model):
    _name = 'fpa.inventario.balance.line'
    _description = 'fpa.inventario.balance.line'
    account_id = fields.Many2one(string='Cuenta', store=True, copy=True, tracking=0, comodel_name='account.account', )
    amount_final = fields.Float(string='Saldo Final', store=True, copy=True, tracking=0, )
    amount_inicial = fields.Float(string='Saldo', store=True, copy=True, tracking=0, )
    bold = fields.Boolean(string='Bold', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    concepts_id = fields.Many2one(string='Conceptos', store=True, copy=True, tracking=0,
                                  comodel_name='fpa.financial.reports.concepts', )
    credit = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    cuenta = fields.Char(string='Cuenta', store=True, copy=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    encabezado_id = fields.Many2one(string='Encabezado', store=True, copy=True, tracking=0,
                                    comodel_name='fpa.inventario.balance', )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    nivel = fields.Integer(string='Nivel', store=True, copy=True, tracking=0, )
    resume = fields.Boolean(string='Resumen', store=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Fpapygline(models.Model):
    _name = 'fpa.pyg.line'
    _description = 'fpa.pyg.line'
    account_id = fields.Many2one(string='Cuenta', store=True, copy=True, tracking=0, comodel_name='account.account', )
    amount_1 = fields.Float(string='Saldo Comparativo', store=True, copy=True, tracking=0, )
    amount_final = fields.Float(string='Saldo Final', store=True, copy=True, tracking=0, )
    amount_inicial = fields.Float(string='Saldo Inicial', store=True, copy=True, tracking=0, )
    bold = fields.Boolean(string='Bold', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    concepts_id = fields.Many2one(string='Conceptos', store=True, copy=True, tracking=0,
                                  comodel_name='fpa.financial.reports.concepts', )
    credit = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    cuenta = fields.Char(string='Cuenta', store=True, copy=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    encabezado_id = fields.Many2one(string='Encabezado', store=True, copy=True, tracking=0, comodel_name='fpa.pyg', )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    nivel = fields.Integer(string='Nivel', store=True, copy=True, tracking=0, )
    resume = fields.Boolean(string='Resumen', store=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Movepettycash(models.Model):
    _name = 'move.petty.cash'
    _description = 'move.petty.cash'
    account_id = fields.Many2one(string='Cuenta', readonly=True, tracking=0, comodel_name='account.account', )
    credit = fields.Monetary(string='Credito', readonly=True, tracking=0, )
    currency_id = fields.Many2one(string='Currency', readonly=True, tracking=0, comodel_name='res.currency', )
    date = fields.Date(string='Fecha', readonly=True, tracking=0, )
    debit = fields.Monetary(string='Debito', readonly=True, tracking=0, )
    detail = fields.Text(string='Detalle', readonly=True, tracking=0, )
    journal_id = fields.Many2one(string='Comprobante', store=True, copy=True, tracking=0,
                                 comodel_name='account.journal', )
    move_id = fields.Many2one(string='Movimiento', store=True, copy=True, tracking=0,
                              comodel_name='account.move.line', )
    partner_id = fields.Many2one(string='Partner', readonly=True, tracking=0, comodel_name='res.partner', )


class Fpapygcline(models.Model):
    _name = 'fpa.pyg.c.line'
    _description = 'fpa.pyg.c.line'
    account_id = fields.Many2one(string='Cuenta', store=True, copy=True, tracking=0, comodel_name='account.account', )
    amount_comparative = fields.Float(string='Saldo Comparativo', store=True, copy=True, tracking=0, )
    amount_final = fields.Float(string='Saldo Final', store=True, copy=True, tracking=0, )
    amount_inicial = fields.Float(string='Saldo Inicial', store=True, copy=True, tracking=0, )
    bold = fields.Boolean(string='Bold', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    concepts_id = fields.Many2one(string='Conceptos', store=True, copy=True, tracking=0,
                                  comodel_name='fpa.financial.reports.concepts', )
    credit = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    cuenta = fields.Char(string='Cuenta', store=True, copy=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    encabezado_id = fields.Many2one(string='Encabezado', store=True, copy=True, tracking=0,
                                    comodel_name='fpa.pyg.c', )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    nivel = fields.Integer(string='Nivel', store=True, copy=True, tracking=0, )
    porc_variation = fields.Float(string='% Variación', store=True, copy=True, tracking=0, )
    resume = fields.Boolean(string='Resumen', store=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )
    variation = fields.Float(string='Variación', store=True, copy=True, tracking=0, )


class Fpadiarioline(models.Model):
    _name = 'fpa.diario.line'
    _description = 'fpa.diario.line'
    account_id = fields.Many2one(string='Cuenta', index=True, store=True, copy=True, tracking=0,
                                 comodel_name='account.account', )
    asiento = fields.Char(string='Asiento', store=True, copy=True, tracking=0, )
    bold = fields.Boolean(string='Bold', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', index=True, store=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    credit = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    cuenta = fields.Char(string='Cuenta', store=True, copy=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    encabezado_id = fields.Many2one(string='Encabezado', index=True, store=True, copy=True, tracking=0,
                                    comodel_name='fpa.diario', )
    fecha = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )
    financial_id = fields.Many2one(string='Reporte', index=True, store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    journal_id = fields.Many2one(string='Diario', index=True, store=True, copy=True, tracking=0,
                                 comodel_name='account.journal', )
    nivel = fields.Integer(string='Nivel', store=True, copy=True, tracking=0, )
    resume = fields.Boolean(string='Resumen', store=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', index=True, store=True, copy=True, tracking=0,
                              comodel_name='res.users', )


class Accountfiscalyearcloseaccount(models.Model):
    _name = 'account.fiscalyear.close.account'
    _description = 'account.fiscalyear.close.account'
    account_id = fields.Many2one(string='Cuenta destino', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='account.account', )
    account_ids = fields.Many2many(relation='accountfiscalyearclo_account_ids_rel', column1='accountfiscalyearclo_id',
                                   column2='account_ids_id', string='Account', store=True, required=True, copy=True,
                                   tracking=0,
                                   comodel_name='account.account', )
    analytic_account_id = fields.Many2one(string='Cuenta analitica', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    close_move = fields.Many2one(string='Asiento de cierre', store=True, copy=True, tracking=0,
                                 comodel_name='account.move', )
    company_id = fields.Many2one(string='Compania', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    date_from = fields.Date(string='Desde', store=True, required=True, copy=True, tracking=0, )
    date_maturity = fields.Date(string='Fecha de vencimiento', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Hasta', store=True, required=True, copy=True, tracking=0, )
    detail = fields.Boolean(string='Detalle', store=True, copy=True, tracking=0, )
    journal_id = fields.Many2one(string='Diario', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='account.journal', )
    name = fields.Char(string='Descripción', store=True, required=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Tercero', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.partner', )
    partner = fields.Boolean(string='Por tercero', store=True, copy=True, tracking=0, )
    period_id = fields.Integer(string='Periodo', store=True, readonly=True, copy=True, tracking=0, )


class Fpamayorbalanceline(models.Model):
    _name = 'fpa.mayor.balance.line'
    _description = 'fpa.mayor.balance.line'
    account_id = fields.Many2one(string='Cuenta', store=True, copy=True, tracking=0, comodel_name='account.account', )
    amount_final_credit = fields.Float(string='Saldo Final Crédito', store=True, copy=True, tracking=0, )
    amount_final_debit = fields.Float(string='Saldo Final Débito', store=True, copy=True, tracking=0, )
    amount_inicial_credit = fields.Float(string='Saldo Inicial Crédito', store=True, copy=True, tracking=0, )
    amount_inicial_debit = fields.Float(string='Saldo Inicial Débito', store=True, copy=True, tracking=0, )
    bold = fields.Boolean(string='Bold', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    concepts_id = fields.Many2one(string='Conceptos', store=True, copy=True, tracking=0,
                                  comodel_name='fpa.financial.reports.concepts', )
    credit = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    cuenta = fields.Char(string='Cuenta', store=True, copy=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    encabezado_id = fields.Many2one(string='Encabezado', store=True, copy=True, tracking=0,
                                    comodel_name='fpa.mayor.balance', )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    nivel = fields.Integer(string='Nivel', store=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Tercero', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    resume = fields.Boolean(string='Resumen', store=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Reportaccountbibudgetline(models.Model):
    _name = 'report.account.bi.budget.line'
    _description = 'report.account.bi.budget.line'
    account_id = fields.Many2one(string='Cuenta General', store=True, copy=True, tracking=0,
                                 comodel_name='account.account', )
    amount = fields.Float(string='Monto Presupuesto', store=True, copy=True, tracking=0, )
    analytic_id = fields.Many2one(string='Centro de costo', store=True, copy=True, tracking=0,
                                  comodel_name='account.analytic.account', )
    budget_post_id = fields.Many2one(string='Presupuesto', store=True, copy=True, tracking=0,
                                     comodel_name='account.budget.post', )
    city_id = fields.Many2one(string='Ciudad', store=True, copy=True, tracking=0, comodel_name='res.city', )
    date = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )
    difference = fields.Float(string='Diferencia', store=True, copy=True, tracking=0, )
    linea_servicio_id = fields.Many2one(string='Linea de Servicio', store=True, copy=True, tracking=0,
                                        comodel_name='_unknown', )
    partner_id = fields.Many2one(string='Tercero', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    place = fields.Char(string='Puesto', store=True, copy=True, tracking=0, )
    practical_amount = fields.Float(string='Monto Real', store=True, copy=True, tracking=0, )
    regional_id = fields.Many2one(string='Regional', store=True, copy=True, tracking=0, comodel_name='_unknown', )
    sede = fields.Char(string='Sede', store=True, copy=True, tracking=0, )
    variation = fields.Float(string='Variación (%)', store=True, copy=True, tracking=0, )


class Fpapygccline(models.Model):
    _name = 'fpa.pyg.cc.line'
    _description = 'fpa.pyg.cc.line'
    account_id = fields.Many2one(string='Cuenta', store=True, copy=True, tracking=0, comodel_name='account.account', )
    amount_1 = fields.Float(string='Saldo Año 1', store=True, copy=True, tracking=0, )
    amount_2 = fields.Float(string='Saldo Año 2', store=True, copy=True, tracking=0, )
    amount_3 = fields.Float(string='Saldo Año 3', store=True, copy=True, tracking=0, )
    amount_4 = fields.Float(string='Saldo Año 4', store=True, copy=True, tracking=0, )
    amount_5 = fields.Float(string='Saldo Año 5', store=True, copy=True, tracking=0, )
    amount_final = fields.Float(string='Saldo Final', store=True, copy=True, tracking=0, )
    amount_inicial = fields.Float(string='Saldo Inicial', store=True, copy=True, tracking=0, )
    analytic_account_id = fields.Many2one(string='Cuenta analitica', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    bold = fields.Boolean(string='Bold', store=True, copy=True, tracking=0, )
    cc1 = fields.Char(string='cc1', store=True, copy=True, tracking=0, )
    cc2 = fields.Char(string='cc2', store=True, copy=True, tracking=0, )
    cc3 = fields.Char(string='cc3', store=True, copy=True, tracking=0, )
    cc4 = fields.Char(string='cc4', store=True, copy=True, tracking=0, )
    cc5 = fields.Char(string='cc5', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    concepts_id = fields.Many2one(string='Conceptos', store=True, copy=True, tracking=0,
                                  comodel_name='fpa.financial.reports.concepts', )
    credit = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    cuenta = fields.Char(string='Cuenta', store=True, copy=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    encabezado_id = fields.Many2one(string='Encabezado', store=True, copy=True, tracking=0,
                                    comodel_name='fpa.pyg.cc', )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    nivel = fields.Integer(string='Nivel', store=True, copy=True, tracking=0, )
    resume = fields.Boolean(string='Resumen', store=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Fpaequitychangesline(models.Model):
    _name = 'fpa.equity.changes.line'
    _description = 'fpa.equity.changes.line'
    account_id = fields.Many2one(string='Cuenta', store=True, copy=True, tracking=0, comodel_name='account.account', )
    amount_comparative = fields.Float(string='Saldo Comparativo', store=True, copy=True, tracking=0, )
    amount_final = fields.Float(string='Saldo Final', store=True, copy=True, tracking=0, )
    aumentos = fields.Float(string='Aumento', store=True, copy=True, tracking=0, )
    bold = fields.Boolean(string='Bold', store=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    concepts_id = fields.Many2one(string='Conceptos', store=True, copy=True, tracking=0,
                                  comodel_name='fpa.financial.reports.concepts', )
    credit = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    cuenta = fields.Char(string='Cuenta', store=True, copy=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    disminuciones = fields.Float(string='Disminuciones', store=True, copy=True, tracking=0, )
    encabezado_id = fields.Many2one(string='Encabezado', store=True, copy=True, tracking=0,
                                    comodel_name='fpa.equity.changes', )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    nivel = fields.Integer(string='Nivel', store=True, copy=True, tracking=0, )
    resume = fields.Boolean(string='Resumen', store=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Certificadoreportretencionline(models.Model):
    _name = 'certificado.report.retencion.line'
    _description = 'certificado.report.retencion.line'
    account_id = fields.Many2one(string='Cuentas de Impuestos', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='account.account', )
    ciudad_tercero = fields.Char(string='Ciudad', store=True, copy=True, tracking=0, )
    line_id = fields.Many2one(string='Parent', store=True, copy=True, tracking=0,
                              comodel_name='certificado.report.retencion', )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    porcentaje = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    tax_id = fields.Many2one(string='Impuesto', store=True, required=True, copy=True, tracking=0,
                             comodel_name='account.tax', )


class Fpafinancialreportsconcepts(models.Model):
    _name = 'fpa.financial.reports.concepts'
    _description = 'fpa.financial.reports.concepts'
    account_ids = fields.Many2many(relation='fpafinancialreportsc_account_ids_rel', column1='fpafinancialreportsc_id',
                                   column2='account_ids_id', string='Cuentas', store=True, copy=True, tracking=0,
                                   comodel_name='account.account', )
    accumulated = fields.Boolean(string='¿Acumulado?', store=True, copy=True, tracking=0, )
    before = fields.Boolean(string='¿Antes del detalle?', store=True, copy=True, tracking=0, )
    cierre = fields.Boolean(string='Cierre', store=True, copy=True, tracking=0, )
    code = fields.Char(string='Codigo concepto', store=True, copy=True, tracking=0, )
    detail = fields.Boolean(string='¿Con detalle?', store=True, copy=True, tracking=0, )
    financial_reports = fields.Many2one(string='Informe financiero', store=True, required=True, copy=True, tracking=0,
                                        comodel_name='fpa.financial.reports', )
    name = fields.Char(string='Concepto', store=True, required=True, copy=True, tracking=0, )
    resume = fields.Boolean(string='¿Solo en Resumen?', store=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, required=True, copy=True, tracking=0, )
    tipo = fields.Boolean(string='¿Filtrar por tipo de cuenta?', store=True, copy=True, tracking=0, )


class Changedifference(models.Model):
    _name = 'change.difference'
    _description = 'change.difference'
    account_ids = fields.Many2many(relation='changedifference_account_ids_rel', column1='changedifference_id',
                                   column2='account_ids_id', string='Cuentas', store=True, copy=True, tracking=0,
                                   comodel_name='account.account', )
    currency_id = fields.Many2one(string='Moneda', store=True, readonly=True, required=True, copy=True, tracking=0,
                                  comodel_name='res.currency', )
    date = fields.Date(string='Fecha', store=True, readonly=True, required=True, copy=True, tracking=0, )
    journal_id = fields.Many2one(string='Diario', store=True, readonly=True, required=True, copy=True, tracking=0,
                                 comodel_name='account.journal', )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='changedifference_message_channel_ids_rel',
                                           column1='changedifference_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='changedifference_message_partner_ids_rel',
                                           column1='changedifference_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    move_ids = fields.Many2many(relation='changedifference_move_ids_rel', column1='changedifference_id',
                                column2='move_ids_id', string='Movimiento', store=True, copy=True, tracking=0,
                                comodel_name='account.move.line', )
    name = fields.Char(string='Name', store=True, readonly=True, copy=True, tracking=0, )
    range_id = fields.Many2one(string='Periodo', store=True, readonly=True, tracking=0, comodel_name='date.range', )
    rate = fields.Float(string='Tasa', store=True, readonly=True, required=True, copy=True, tracking=0, )


class Fpafinancialreportsconceptscolumnslines(models.Model):
    _name = 'fpa.financial.reports.concepts.columns.lines'
    _description = 'fpa.financial.reports.concepts.columns.lines'
    account_ids = fields.Many2many('account.account', 'fpa_acc_ccl_rel', 'ccl_id', 'acc_id', string='Cuentas',
                                   copy=False, )
    name = fields.Char(string='Descripcion', store=True, copy=True, tracking=0, )
    parent_id = fields.Many2one(string='Conceptos(Medios)', store=True, required=True, copy=True, tracking=0,
                                comodel_name='fpa.financial.reports.concepts.columns', )


class Carteraavancysextended(models.Model):
    _name = 'cartera.avancys.extended'
    _description = 'cartera.avancys.extended'
    account_ids_payable = fields.Many2many(
        'account.account',
        relation='cartera_acc_pay_rel',
        column1='cartera_id',
        column2='acc_id',
        string='Cuentas por pagar',
        copy=False,
    )
    account_ids_receivable = fields.Many2many(
        'account.account',
        relation='cartera_acc_recv_rel',
        column1='cartera_id',
        column2='acc_id',
        string='Cuentas por cobrar',
        copy=False,
    )
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.financial.structure', )
    company = fields.Many2one(string='Company', readonly=True, tracking=0, comodel_name='res.company', )
    currency_id = fields.Many2one(string='Moneda', store=True, copy=True, tracking=0, comodel_name='res.currency', )
    date = fields.Date(string='Fecha de Corte', store=True, copy=True, tracking=0, )
    journal_ids = fields.Many2many(relation='carteraavancysextend_journal_ids_rel', column1='carteraavancysextend_id',
                                   column2='journal_ids_id', string='Diarios', store=True, copy=True, tracking=0,
                                   comodel_name='account.journal', )
    partner_ids = fields.Many2many(relation='carteraavancysextend_partner_ids_rel', column1='carteraavancysextend_id',
                                   column2='partner_ids_id', string='Terceros', store=True, copy=True, tracking=0,
                                   comodel_name='res.partner', )
    rate = fields.Float(string='Tasa', store=True, copy=True, tracking=0, )


class Wizardcertificadoingresos(models.Model):
    _name = 'wizard.certificado.ingresos'
    _description = 'wizard.certificado.ingresos'
    account_year_id = fields.Many2one(string='Ejercicio', store=True, required=True, copy=True, tracking=0,
                                      comodel_name='account.fiscal.year', )
    cert_id = fields.Many2one(string='Formulario', store=True, required=True, copy=True, tracking=0,
                              comodel_name='certificado.report.ingresos', )
    employee_ids = fields.Many2many(relation='wizardcertificadoing_employee_ids_rel', column1='wizardcertificadoing_id',
                                    column2='employee_ids_id', string='Empleados', store=True, copy=True, tracking=0,
                                    comodel_name='hr.employee', )


class Certificadoingresosline(models.Model):
    _name = 'certificado.ingresos.line'
    _description = 'certificado.ingresos.line'
    account_year_id = fields.Many2one(string='Ejercicio', store=True, readonly=True, copy=True, tracking=0,
                                      comodel_name='account.fiscal.year', )
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Next Activity Type', tracking=0, comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    cert_id = fields.Many2one(string='Formulario', store=True, readonly=True, required=True, copy=True, tracking=0,
                              comodel_name='certificado.report.ingresos', )
    certificado_id = fields.Many2one(string='Certificado', store=True, readonly=True, required=True, copy=True,
                                     tracking=0, comodel_name='certificado.ingresos', )
    company_id = fields.Many2one(string='Compañia', store=True, readonly=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    date_from = fields.Date(string='Desde', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Hasta', store=True, copy=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='certificadoingresosl_message_channel_ids_rel',
                                           column1='certificadoingresosl_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='certificadoingresosl_message_partner_ids_rel',
                                           column1='certificadoingresosl_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    name = fields.Many2one(string='Empleado', store=True, readonly=True, copy=True, tracking=0,
                           comodel_name='hr.employee', )


class Certificadoingresos(models.Model):
    _name = 'certificado.ingresos'
    _description = 'certificado.ingresos'
    account_year_id = fields.Many2one(string='Ejercicio', store=True, readonly=True, copy=True, tracking=0,
                                      comodel_name='account.fiscal.year', )
    cert_id = fields.Many2one(string='Formulario', store=True, readonly=True, required=True, copy=True, tracking=0,
                              comodel_name='certificado.report.ingresos', )
    company_id = fields.Many2one(string='Compañia', store=True, readonly=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    name = fields.Char(string='Name', store=True, readonly=True, copy=True, tracking=0, )


class Iractionscenter(models.Model):
    _name = 'ir.actions.center'
    _description = 'ir.actions.center'
    action_id = fields.Many2one(string='Action', store=True, copy=True, tracking=0,
                                comodel_name='ir.actions.act_window', )
    name = fields.Char(string='Name', store=True, copy=True, tracking=0, )
    views_order = fields.Char(string='Views Order', store=True, copy=True, tracking=0, )


class Studioviewcenter(models.Model):
    _name = 'studio.view.center'
    _description = 'studio.view.center'
    action_id = fields.Many2one(string='Action', store=True, copy=True, tracking=0,
                                comodel_name='ir.actions.act_window', )
    arch = fields.Text(string='Arch', store=True, copy=True, tracking=0, )
    field_name = fields.Char(string='Field Name', store=True, copy=True, tracking=0, )
    new_fields = fields.Many2many(relation='studioviewcenter_new_fields_rel', column1='studioviewcenter_id',
                                  column2='new_fields_id', string='New Fields', store=True, tracking=0,
                                  comodel_name='ir.model.fields', )
    parent_id = fields.Many2one(string='Parent Id', store=True, copy=True, tracking=0,
                                comodel_name='studio.view.center', )
    parent_view_id = fields.Many2one(string='Parent View Id', store=True, copy=True, tracking=0,
                                     comodel_name='ir.ui.view', )
    view_id = fields.Many2one(string='View id', store=True, copy=True, tracking=0, comodel_name='ir.ui.view', )
    view_key = fields.Char(string='View Key', store=True, copy=True, tracking=0, )
    views_order = fields.Char(string='Views Order', store=True, copy=True, tracking=0, )


class Hrrosterhorario(models.Model):
    _name = 'hr.roster.horario'
    _description = 'hr.roster.horario'
    active = fields.Boolean(string='Active', store=True, copy=True, tracking=100, )
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Next Activity Type', tracking=0, comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    description = fields.Text(string='Descripcion', store=True, copy=True, tracking=100, )
    diurn_comp = fields.Float(string='Componente Diurno', store=True, copy=True, tracking=100, )
    duration = fields.Float(string='Duracion', readonly=True, tracking=0, )
    end_break = fields.Char(string='Fin Descanso', store=True, copy=True, tracking=100, )
    is_rest = fields.Boolean(string='Turno con Descanso?', store=True, copy=True, tracking=100, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='hrrosterhorario_message_channel_ids_rel',
                                           column1='hrrosterhorario_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='hrrosterhorario_message_partner_ids_rel',
                                           column1='hrrosterhorario_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    name = fields.Char(string='Codigo', store=True, copy=True, tracking=100, )
    nocturn_comp = fields.Float(string='Componente Nocturno', store=True, copy=True, tracking=100, )
    start_break = fields.Char(string='Inicio Descanso', store=True, copy=True, tracking=100, )
    time_in = fields.Char(string='Entrada', store=True, required=True, copy=True, tracking=100, )
    time_out = fields.Char(string='Salida', store=True, required=True, copy=True, tracking=100, )
    x_editar = fields.Boolean(string='Editar', store=True, copy=True, tracking=1, )


class Examenesmedicos(models.Model):
    _name = 'examenes.medicos'
    _description = 'examenes.medicos'
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Next Activity Type', tracking=0, comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    archivos_adjuntos = fields.Many2many(relation='examenesmedicos_archivos_adjuntos_rel', column1='examenesmedicos_id',
                                         column2='archivos_adjuntos_id', string='Archivos Adjuntos', store=True,
                                         copy=True, tracking=0,
                                         comodel_name='ir.attachment', )
    cargo = fields.Char(string='Cargo', store=True, readonly=True, tracking=0, )
    celular = fields.Char(string='Celular', store=True, readonly=True, tracking=0, )
    dias_incapacidad = fields.Integer(string='Días de incapacidad', store=True, copy=True, tracking=0, )
    edad = fields.Integer(string='Edad', store=True, readonly=True, tracking=0, )
    empleado = fields.Many2one(string='Empleado', store=True, readonly=True, required=True, copy=True, tracking=0,
                               comodel_name='hr.employee', )
    eps = fields.Char(string='Eps', store=True, readonly=True, tracking=0, )
    especificas_temporalidad = fields.Integer(string='Temporalidad en meses', store=True, copy=True, tracking=0, )
    fecha_ingreso = fields.Char(string='Fecha de Ingreso a la Empresa', store=True, readonly=True, tracking=0, )
    fecha_nacimiento = fields.Char(string='Fecha de Nacimiento', store=True, readonly=True, tracking=0, )
    fecha_probable_seguimiento = fields.Date(string='Fecha probable de seguimiento', store=True, readonly=True,
                                             tracking=0, )
    fecha_realizacion = fields.Date(string='Fecha de Realización', store=True, required=True, copy=True, tracking=0, )
    fecha_vencimiento = fields.Date(string='Fecha de vencimiento', store=True, copy=True, tracking=0, )
    fondo_pension = fields.Char(string='Fondo de pensión', store=True, readonly=True, tracking=0, )
    imc = fields.Float(string='Ingrese el IMC', store=True, copy=True, tracking=0, )
    ips = fields.Text(string='Ips', store=True, copy=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='examenesmedicos_message_channel_ids_rel',
                                           column1='examenesmedicos_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='examenesmedicos_message_partner_ids_rel',
                                           column1='examenesmedicos_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    numero_identificacion = fields.Char(string='Número de Identificación', store=True, required=True, copy=True,
                                        tracking=0, )
    observaciones = fields.Text(string='Observaciones', store=True, copy=True, tracking=0, )
    otro_programa = fields.Text(string='Otro programa', store=True, copy=True, tracking=0, )
    programas_seleccionados = fields.Char(string='Programas Seleccionados', store=True, readonly=True, tracking=0, )
    programas = fields.Many2many(relation='examenesmedicos_programas_rel', column1='examenesmedicos_id',
                                 column2='programas_id', string='Programas', store=True, copy=True, tracking=0,
                                 comodel_name='programa', )
    recomendacion_permanente = fields.Boolean(string='Recomendación permanente', store=True, copy=True, tracking=0, )
    recomendaciones_especificas_texto = fields.Text(string='Recomendaciones específicas texto', store=True, copy=True,
                                                    tracking=0, )
    recomendaciones_generales_texto = fields.Text(string='Recomendaciones generales texto', store=True, copy=True,
                                                  tracking=0, )
    remisiones_medicas = fields.Text(string='Remisiones médicas', store=True, copy=True, tracking=0, )
    restriccion_permanente = fields.Boolean(string='Restricción permanente', store=True, copy=True, tracking=0, )
    restricciones_temporalidad = fields.Integer(string='Temporalidad en meses', store=True, copy=True, tracking=0, )
    restricciones_texto = fields.Text(string='Restricciones', store=True, copy=True, tracking=0, )
    subzona = fields.Char(string='Subzona', store=True, readonly=True, tracking=0, )
    telefono = fields.Char(string='Teléfono', store=True, readonly=True, tracking=0, )
    tipo_contrato = fields.Char(string='Tipo de contrato', store=True, readonly=True, tracking=0, )
    valor_imc = fields.Char(string='El IMC es', store=True, readonly=True, tracking=0, )
    zona = fields.Char(string='Zona', store=True, readonly=True, tracking=0, )


class Printcertificadoretencion(models.Model):
    _name = 'print.certificado.retencion'
    _description = 'print.certificado.retencion'
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Next Activity Type', tracking=0, comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    amount_total_text = fields.Char(string='amount_text', readonly=True, tracking=0, )
    amount_total = fields.Float(string='amount', readonly=True, tracking=0, )
    cert_id = fields.Many2one(string='Certificado', store=True, readonly=True, required=True, copy=True, tracking=0,
                              comodel_name='certificado.report.retencion', )
    city_id = fields.Many2one(string='Ciudad', store=True, readonly=True, copy=True, tracking=0,
                              comodel_name='res.city', )
    company_id = fields.Many2one(string='Compañia', store=True, readonly=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    date_expedition = fields.Date(string='Fecha de Expedicion', store=True, copy=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='printcertificadorete_message_channel_ids_rel',
                                           column1='printcertificadorete_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='printcertificadorete_message_partner_ids_rel',
                                           column1='printcertificadorete_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    partner_id = fields.Many2one(string='Tercero', store=True, readonly=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.partner', )
    periodo_id = fields.Many2one(string='Periodo', store=True, readonly=True, required=True, copy=True, tracking=0,
                                 comodel_name='certificado.report.retencion.periodicidad', )


class Hrpayrollembargo(models.Model):
    _name = 'hr.payroll.embargo'
    _description = 'hr.payroll.embargo'
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    activity_type_id = fields.Many2one(string='Next Activity Type', tracking=0, comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    amount_salary_value = fields.Float(string='Valor del monto', store=True, copy=True, tracking=0, )
    amount_salary = fields.Boolean(string='Monto o tope', store=True, copy=True, tracking=0, )
    category_id = fields.Many2one(string='Categoria', store=True, copy=True, tracking=0,
                                  comodel_name='hr.payroll.embargo.category', )
    contract_id = fields.Many2one(string='Contrato', store=True, copy=True, tracking=0, comodel_name='hr.contract', )
    court_account_number_id = fields.Many2one(string='Número de cuenta del juzgado', store=True, copy=True,
                                              tracking=0,
                                              comodel_name='hr.court.embargoes', )
    court_account_number = fields.Char(string='Número de cuenta del juzgado', store=True, copy=True, tracking=0, )
    court_code_id = fields.Many2one(string='Código del juzgado', store=True, copy=True, tracking=0,
                                    comodel_name='hr.court.embargoes.code', )
    court_code = fields.Char(string='Código del juzgado old', store=True, copy=True, tracking=0, )
    date_start = fields.Date(string='Fecha de inicio', store=True, copy=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )
    demand_city_id = fields.Many2one(string='Ciudad de la demanda', store=True, copy=True, tracking=0,
                                     comodel_name='res.city', )
    description = fields.Text(string='Descripción', store=True, copy=True, tracking=0, )
    destination_office_id = fields.Many2one(string='Oficina de destino', store=True, copy=True, tracking=0,
                                            comodel_name='hr.court.embargoes.destination', )
    destination_office = fields.Char(string='Oficina de destino', store=True, copy=True, tracking=0, )
    due = fields.Float(string='Deuda', store=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    exceed_salary = fields.Boolean(string='1/5 De lo que exceda el salario mínimo legal mensual vigente', store=True,
                                   copy=True, tracking=0, )
    exceed_without_discount_salary = fields.Boolean(
        string='1/5 De lo que exceda el salario mínimo Sin Descuento de Ley',
        store=True, copy=True, tracking=0, )
    file_number = fields.Char(string='Número de expediente', store=True, copy=True, tracking=0, )
    fixed_fee_value = fields.Float(string='Valor de la cuota fija', store=True, copy=True, tracking=0, )
    fixed_fee = fields.Boolean(string='Cuota Fija', store=True, copy=True, tracking=0, )
    located = fields.Char(string='Radicado', store=True, copy=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='hrpayrollembargo_message_channel_ids_rel',
                                           column1='hrpayrollembargo_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='hrpayrollembargo_message_partner_ids_rel',
                                           column1='hrpayrollembargo_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    more_smmlv_percentage = fields.Boolean(string='Porcentaje que exceda el salario minimo', store=True, copy=True,
                                           tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    number_process_court = fields.Char(string='Número del proceso en la corte', store=True, copy=True, tracking=0, )
    office = fields.Char(string='Oficio', store=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Demandante', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    payout_percentage_value = fields.Float(string='Valor del porcentaje', store=True, copy=True, tracking=0, )
    payout_percentage = fields.Boolean(string='Porcentaje de pago', store=True, copy=True, tracking=0, )
    pending_debt = fields.Float(string='Deuda pendiente', store=True, copy=True, tracking=0, )
    priority_id = fields.Many2one(string='Prioridades', store=True, copy=True, tracking=0,
                                  comodel_name='hr.payroll.embargo.priority', )
    savings_account = fields.Char(string='Cuenta de ahorro', store=True, copy=True, tracking=0, )
    share = fields.Float(string='Cuota', store=True, copy=True, tracking=0, )
    smmlv_percentage = fields.Boolean(string='Porcentaje del salario minimo', store=True, copy=True, tracking=0, )
    type_id = fields.Many2one(string='Tipo', store=True, copy=True, tracking=0,
                              comodel_name='hr.payroll.embargo.type', )
    without_discount_percentage = fields.Boolean(string='Porcentaje Sin Descuento de Ley', store=True, copy=True,
                                                 tracking=0, )


class Incomerecords(models.Model):
    _name = 'income.records'
    _description = 'income.records'
    actual_date = fields.Date(string='Fecha:', store=True, copy=True, tracking=0, )
    date_from = fields.Date(string='Date From', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Date To', store=True, copy=True, tracking=0, )
    time = fields.Float(string='Registro Hora', store=True, copy=True, tracking=0, )
    user = fields.Many2one(string='Responsable', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Hrrostercambioupdate(models.Model):
    _name = 'hr.roster.cambio.update'
    _description = 'hr.roster.cambio.update'
    actual_horario = fields.Many2one(string='Horario actual', store=True, copy=True, tracking=0,
                                     comodel_name='hr.roster.horario', )
    cambio_id = fields.Many2one(string='Cambio', store=True, copy=True, tracking=0,
                                comodel_name='hr.roster.cambio.turno', )
    date = fields.Date(string='Fecha', store=True, required=True, copy=True, tracking=0, )
    new_horario = fields.Many2one(string='Nuevo horario', store=True, copy=True, tracking=0,
                                  comodel_name='hr.roster.horario', )


class Salequoterline(models.Model):
    _name = 'sale.quoter.line'
    _description = 'sale.quoter.line'
    add_communication_check = fields.Boolean(string='Agregar Comunicaciones', store=True, copy=True, tracking=0, )
    additional_dotation_id = fields.Many2one(string='Dotacion Adicional', store=True, copy=True, tracking=0,
                                             comodel_name='quoter.additional.dotation', )
    additional_dotation_value = fields.Float(string='Dotaciones Adicionales Anuales', readonly=True, tracking=0, )
    additional_nonsalary_bonus = fields.Float(string='Bono adicional no salarial', store=True, copy=True,
                                              tracking=0, )
    additional_pos_monthly = fields.Float(string='Dotacion Mensual', readonly=True, tracking=0, )
    additional_salary_bonus = fields.Float(string='Bono adicional salarial', store=True, copy=True, tracking=0, )
    amount_day_id = fields.Many2one(string='Cantidad de dias', store=True, copy=True, tracking=0,
                                    comodel_name='quoter.amount.day', )
    amount_people = fields.Float(string='Cantidad personas', store=True, copy=True, tracking=0, )
    bearing = fields.Float(string='Rodamiento', store=True, copy=True, tracking=0, )
    business_line = fields.Many2one(string='Linea de negocio', store=True, copy=True, tracking=0,
                                    comodel_name='project.linea.negocio', )
    canine_cost = fields.Float(string='Caninos', readonly=True, tracking=0, )
    canine_id = fields.Many2one(string='Canino', store=True, copy=True, tracking=0, comodel_name='quoter.canine', )
    canine_monthly = fields.Float(string='Dotacion Mensual', readonly=True, tracking=0, )
    city_id = fields.Many2one(string='Ciudad', store=True, copy=True, tracking=0, comodel_name='res.city', )
    claims_current = fields.Float(string='Siniestralidad', readonly=True, tracking=0, )
    claims_monthly = fields.Float(string='Siniestralidad', readonly=True, tracking=0, )
    claims = fields.Float(string='Siniestralidad', readonly=True, tracking=0, )
    commercial_distributcommercial_distribution_name = fields.Char(string='Nombre unidad de negocio', readonly=True,
                                                                   tracking=0, )
    commercial_distribution_id = fields.Many2one(string='Unidad de negocio', store=True, copy=True, tracking=0,
                                                 comodel_name='account.commercial.distribution', )
    communication_additionnal_monthly = fields.Float(string='Dotacion Mensual', readonly=True, tracking=0, )
    communication_aditional_cost = fields.Float(string='Comunicaciones', readonly=True, tracking=0, )
    communication_aditional_id = fields.Many2one(string='Comunicacion', store=True, copy=True, tracking=0,
                                                 comodel_name='quoter.communication', )
    communication_cost_current = fields.Float(string='Comunicaciones', readonly=True, tracking=0, )
    communication_cost_monthly = fields.Float(string='Comunicaciones', readonly=True, tracking=0, )
    communication_cost = fields.Float(string='Comunicaciones', readonly=True, tracking=0, )
    communication_id = fields.Many2one(string='Comunicacion', store=True, copy=True, tracking=0,
                                       comodel_name='quoter.communication', )
    company_id = fields.Many2one(string='Compañía', copy=True, tracking=0, comodel_name='res.company', )
    consulting_comission = fields.Float(string='Comisión Consultor', readonly=True, tracking=0, )
    date_start = fields.Date(string='Fecha Inicio del Contrato', readonly=True, tracking=100, )
    dias_facturables = fields.Integer(string='Dias mes', store=True, readonly=True, tracking=100, )
    direct_contribution = fields.Float(string='Directos y Contribución', readonly=True, tracking=0, )
    direct_tax_current = fields.Float(string='Impuestos Directos', readonly=True, tracking=0, )
    direct_tax_monthly = fields.Float(string='Impuestos Directos', readonly=True, tracking=0, )
    direct_tax = fields.Float(string='Impuestos Directos', readonly=True, tracking=0, )
    domain_business_line = fields.Char(string='domain_business_line', readonly=True, tracking=0, )
    domain_product = fields.Char(string='domain_product', readonly=True, tracking=0, )
    domain_service_type = fields.Char(string='domain_service_type', readonly=True, tracking=0, )
    domain_transport = fields.Char(string='domain_transport', readonly=True, tracking=0, )
    dotation_additional_monthly = fields.Float(string='Dotacion Mensual', readonly=True, tracking=0, )
    dotation_additional_pos_value = fields.Float(string='Dotación Adicional Puesto', readonly=True, tracking=0, )
    dotation_additional_position_id = fields.Many2one(string='Dotacion adicional puesto', store=True, copy=True,
                                                      tracking=0, comodel_name='quoter.dotation.additional.position', )
    dotation_id = fields.Many2one(string='dotacion', store=True, copy=True, tracking=0,
                                  comodel_name='quoter.dotation', )
    dotation_monthly = fields.Float(string='Dotacion Mensual', readonly=True, tracking=0, )
    dotation_pos_value = fields.Float(string='Dotación Puesto', readonly=True, tracking=0, )
    dotation_position_id = fields.Many2one(string='Dotacion puesto', store=True, copy=True, tracking=0,
                                           comodel_name='quoter.dotation.position', )
    dotation_protection_id = fields.Many2one(string='Dotacion proteccion personal', store=True, copy=True, tracking=0,
                                             comodel_name='quoter.dotation.protection', )
    dotation_protection_monthly = fields.Float(string='Dotacion Mensual', readonly=True, tracking=0, )
    dotation_value = fields.Float(string='Dotaciones Anuales', readonly=True, tracking=0, )
    ebtax_current = fields.Float(string='Antes de impuestos', readonly=True, tracking=0, )
    ebtax_monthly = fields.Float(string='Antes de impuestos', readonly=True, tracking=0, )
    ebtax = fields.Float(string='Antes de impuestos', readonly=True, tracking=0, )
    expected_profitability_percentage = fields.Float(string='Rentabilidad esperada en porcentaje', store=True,
                                                     copy=True,
                                                     tracking=0, )
    expected_profitability_pesos = fields.Float(string='Rentabilidad esperada en pesos', store=True, copy=True,
                                                tracking=0, )
    extra_hours = fields.Float(string='Horas Extra', store=True, copy=True, tracking=0, )
    feeding = fields.Float(string='Alimentacion', store=True, copy=True, tracking=0, )
    finantial_cost_current = fields.Float(string='Costos Financieros', readonly=True, tracking=0, )
    finantial_cost_monthly = fields.Float(string='Costos Financieros', readonly=True, tracking=0, )
    finantial_cost_payment_term = fields.Float(string='Costos financieros plazo de pago', store=True, readonly=True,
                                               tracking=0, )
    finantial_cost = fields.Float(string='Costos Financieros', readonly=True, tracking=0, )
    fp_cost = fields.Float(string='5P', readonly=True, tracking=0, )
    h_d = fields.Integer(string='Horas diurnas', readonly=True, tracking=0, )
    h_n = fields.Integer(string='Horas nocturnas', readonly=True, tracking=0, )
    hseq_current = fields.Float(string='HSEQ', readonly=True, tracking=0, )
    hseq_monthly = fields.Float(string='HSEQ', readonly=True, tracking=0, )
    hseq = fields.Float(string='HSEQ', readonly=True, tracking=0, )
    incidentals_cost = fields.Float(string='Imprevistos/Siniestros', readonly=True, tracking=0, )
    income_tax_current = fields.Float(string='Renta', readonly=True, tracking=0, )
    income_tax_monthly = fields.Float(string='Renta', readonly=True, tracking=0, )
    income_tax = fields.Float(string='Renta', readonly=True, tracking=0, )
    life_insurance = fields.Float(string='Prima seguro vida', store=True, copy=True, tracking=0, )
    location = fields.Char(string='Dirección Puesto', store=True, copy=True, tracking=0, )
    minimum_salary = fields.Float(string='Salario minimo', store=True, copy=True, tracking=0, )
    modality_id = fields.Many2one(string='Modalidad Padre', store=True, copy=True, tracking=0,
                                  comodel_name='hr.roster.modalidad', )
    net_result_current = fields.Float(string='Utilidad Neta Mensual', readonly=True, tracking=0, )
    net_result_monthly = fields.Float(string='Utilidad Neta Mensual', readonly=True, tracking=0, )
    net_result = fields.Float(string='Utilidad Neta', readonly=True, tracking=0, )
    night_charges = fields.Float(string='Recargos nocturnos', store=True, copy=True, tracking=0, )
    no_cost = fields.Boolean(string='Sin Costo', store=True, copy=True, tracking=0, )
    non_salary_bonus = fields.Float(string='Auxilio No Salarial', store=True, copy=True, tracking=0, )
    overhead_current = fields.Float(string='OverHead', readonly=True, tracking=0, )
    overhead_monthly = fields.Float(string='OverHead', readonly=True, tracking=0, )
    overhead = fields.Float(string='OverHead', readonly=True, tracking=0, )
    parafiscal = fields.Float(string='Parafiscales', readonly=True, tracking=0, )
    parent_modality_id = fields.Many2one(string='Modalidad Patron', store=True, copy=True, tracking=0,
                                         comodel_name='hr.roster.modalidad', )
    participation_percentage = fields.Float(string='Porcentaje de participacion', readonly=True, tracking=0, )
    payroll_financing = fields.Float(string='Financiacion Nomina', readonly=True, tracking=0, )
    pct_claims = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_direct_tax = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_ebtax = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_finantial_cost = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_hseq = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_income_tax = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_net_result = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_support_cost = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_total_additional_dotation_contract = fields.Float(string='Porcentaje Dotacion Contrato', readonly=True,
                                                          tracking=0, )
    pct_total_additional_pos_contract = fields.Float(string='Porcentaje Dotacion Contrato', readonly=True, tracking=0, )
    pct_total_additionals = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_total_canine_contract = fields.Float(string='Porcentaje Dotacion Contrato', readonly=True, tracking=0, )
    pct_total_communication_additionnal_contract = fields.Float(string='Porcentaje Dotacion Contrato', readonly=True,
                                                                tracking=0, )
    pct_total_communication = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_total_coordinador_total = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_total_coordinator_cost = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_total_coordinator = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_total_cost_general = fields.Float(string='Total Costos Directos', readonly=True, tracking=0, )
    pct_total_dedication = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_total_direct_cost = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_total_dotation_contract = fields.Float(string='Porcentaje Dotacion Contrato', readonly=True, tracking=0, )
    pct_total_dotation_protection_contract = fields.Float(string='Porcentaje Dotacion Contrato', readonly=True,
                                                          tracking=0, )
    pct_total_freelancers_contract = fields.Float(string='Porcentaje Dotacion Contrato', readonly=True, tracking=0, )
    pct_total_industrial_safety_equipment = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_total_labor_cost = fields.Float(string='Porcentaje carga salarial', readonly=True, tracking=0, )
    pct_total_other_cost = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_total_post_additional_staffing = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_total_post_staffing = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_total_rotation = fields.Float(string='pct rotation', readonly=True, tracking=0, )
    pct_total_salaries_benefist_social_parafiscal = fields.Float(string='Porcentaje carga salarial', readonly=True,
                                                                 tracking=0, )
    pct_total_selection = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_total_staffing = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_total_supplies_pos = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_total_supplies = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pct_total_vehicle_contract = fields.Float(string='Porcentaje Dotacion Contrato', readonly=True, tracking=0, )
    pct_total_weapon_contract = fields.Float(string='Porcentaje Dotacion Contrato', readonly=True, tracking=0, )
    pct_unforeseen = fields.Float(string='Porcentaje', readonly=True, tracking=0, )
    pos_qty = fields.Float(string='Número de Puestos', readonly=True, tracking=0, )
    position_id = fields.Many2one(string='Puesto', store=True, copy=True, tracking=0,
                                  comodel_name='quoter.position', )
    preliminary_profitability_percentage = fields.Float(string='Rentablidad preliminar porcentaje', readonly=True,
                                                        tracking=0, )
    preliminary_profitability_pesos = fields.Float(string='Rentabilidad preliminar en pesos', readonly=True,
                                                   tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.product', )
    rate_type_id = fields.Many2one(string='Tarifa servicio', readonly=True, tracking=0,
                                   comodel_name='quoter.rate.type', )
    risk_id = fields.Many2one(string='Riesgo ARL', store=True, copy=True, tracking=0,
                              comodel_name='hr.contract.risk', )
    risk_percentage = fields.Float(string='Porcentage de riesgo', readonly=True, tracking=0, )
    rotation = fields.Float(string='Rotación', store=True, copy=True, tracking=0, )
    salary_bonus = fields.Float(string='Bonificación Salarial', store=True, copy=True, tracking=0, )
    sale_quoter_id = fields.Many2one(string='Cotizador', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter', )
    sale_value_service_aux = fields.Float(string='Valor venta servicio', store=True, tracking=0, )
    sale_value_service = fields.Float(string='Valor venta por servicio', store=True, readonly=True, tracking=0, )
    selection_cost = fields.Float(string='Seleccion', readonly=True, tracking=0, )
    selection_id = fields.Many2one(string='Selección', store=True, copy=True, tracking=0,
                                   comodel_name='quoter.selection', )
    service_mod_id = fields.Many2one(string='Medio', readonly=True, tracking=0, comodel_name='quoter.service.mod', )
    service_num = fields.Float(string='Número de Servicios', store=True, readonly=True, tracking=0, )
    service_type = fields.Many2one(string='Tipo de servicio', store=True, copy=True, tracking=0,
                                   comodel_name='project.service.type', )
    supervision_cost = fields.Float(string='Supervision', readonly=True, tracking=0, )
    supplies_pos_monthly = fields.Float(string='Dotaciones Adicionales del Personal', readonly=True, tracking=0, )
    support_amount_day_id = fields.Many2one(string='Cantidad de dias', store=True, copy=True, tracking=0,
                                            comodel_name='quoter.amount.day', )
    support_amount_people = fields.Float(string='Cantidad personas', store=True, copy=True, tracking=0, )
    support_bearing = fields.Float(string='Rodamiento', store=True, copy=True, tracking=0, )
    support_communication_cost = fields.Float(string='Comunicaciones', readonly=True, tracking=0, )
    support_communication_id = fields.Many2one(string='Comunicacion', store=True, copy=True, tracking=0,
                                               comodel_name='quoter.communication', )
    support_cost_current = fields.Float(string='Apoyo', readonly=True, tracking=0, )
    support_cost_monthly = fields.Float(string='Apoyo', readonly=True, tracking=0, )
    support_cost = fields.Float(string='Apoyo', readonly=True, tracking=0, )
    support_dotation_id = fields.Many2one(string='Dotacion', store=True, copy=True, tracking=0,
                                          comodel_name='quoter.dotation', )
    support_dotation_position_id = fields.Many2one(string='Dotacion puesto', store=True, copy=True, tracking=0,
                                                   comodel_name='quoter.dotation.position', )
    support_dotation_protection_id = fields.Many2one(string='Dotacion proteccion personal', store=True, copy=True,
                                                     tracking=0, comodel_name='quoter.dotation.protection', )
    support_extra_hours = fields.Float(string='Horas Extra', store=True, copy=True, tracking=0, )
    support_feeding = fields.Float(string='Alimentacion', store=True, copy=True, tracking=0, )
    support_id = fields.Many2one(string='Apoyo', store=True, copy=True, tracking=0, comodel_name='quoter.support', )
    support_life_insurance = fields.Float(string='Prima seguro vida', store=True, copy=True, tracking=0, )
    support_minimum_salary = fields.Float(string='Salario minimo', store=True, copy=True, tracking=0, )
    support_night_charges = fields.Float(string='Recargos nocturnos', store=True, copy=True, tracking=0, )
    support_non_salary_bonus = fields.Float(string='Bonificación no Salarial', store=True, copy=True, tracking=0, )
    support_parafiscal = fields.Float(string='Parafiscales', readonly=True, tracking=0, )
    support_participation_percentage = fields.Float(string='Porcentaje de participacion', readonly=True, tracking=0, )
    support_rate_type_id = fields.Many2one(string='Tarifa servicio', store=True, copy=True, tracking=0,
                                           comodel_name='quoter.rate.type', )
    support_salary_bonus = fields.Float(string='Bonificación Salarial', store=True, copy=True, tracking=0, )
    support_salary_burden_percentage = fields.Float(string='Porcentaje carga salarial', readonly=True, tracking=0, )
    support_sale_value_service = fields.Float(string='Valor venta por servicio', readonly=True, tracking=0, )
    support_selection_cost = fields.Float(string='Seleccion', readonly=True, tracking=0, )
    support_selection_id = fields.Many2one(string='Selección', store=True, copy=True, tracking=0,
                                           comodel_name='quoter.selection', )
    support_service_mod_id = fields.Many2one(string='Modalidad de servicio', store=True, copy=True, tracking=0,
                                             comodel_name='quoter.service.mod', )
    support_service_num = fields.Float(string='Número de Servicios', store=True, copy=True, tracking=0, )
    support_staff_cost = fields.Float(string='Personal de Apoyo', readonly=True, tracking=0, )
    support_time_in = fields.Char(string='Hora entrada', store=True, copy=True, tracking=0, )
    support_time_out = fields.Char(string='Hora salida', store=True, copy=True, tracking=0, )
    support_total_benefits = fields.Float(string='Total Prestaciones', readonly=True, tracking=0, )
    support_total_cost_other_direct_cost = fields.Float(string='Total Costos Directos', readonly=True, tracking=0, )
    support_total_direct_cost = fields.Float(string='Total Costos Directos', readonly=True, tracking=0, )
    support_total_industrial_safety_equipment = fields.Float(string='Total Dotacion Seguridad Industrial(EPP)',
                                                             readonly=True, tracking=0, )
    support_total_other_cost = fields.Float(string='Total Otros Costos', readonly=True, tracking=0, )
    support_total_post_staffing = fields.Float(string='Total Dotacion del Puesto', readonly=True, tracking=0, )
    support_total_salaries = fields.Float(string='Total Salarios', readonly=True, tracking=0, )
    support_total_sale_value = fields.Float(string='Valor total de la venta', readonly=True, tracking=0, )
    support_total_social_security = fields.Float(string='Total Seguridad Social', readonly=True, tracking=0, )
    support_total_staffing = fields.Float(string='Total Dotacion del Personal', readonly=True, tracking=0, )
    support_training_cost = fields.Float(string='Capacitacion', readonly=True, tracking=0, )
    support_training_id = fields.Many2one(string='Capacitación', store=True, copy=True, tracking=0,
                                          comodel_name='quoter.training', )
    support_transportation_assistance = fields.Float(string='Auxilio de transporte', store=True, copy=True,
                                                     tracking=0, )
    time_in = fields.Char(string='Hora entrada', store=True, copy=True, tracking=0, )
    time_out = fields.Char(string='Hora salida', store=True, copy=True, tracking=0, )
    total_accrual = fields.Float(string='Total Devengado', readonly=True, tracking=0, )
    total_additional_dotation_contract = fields.Float(string='Total Dotacion Contrato', readonly=True, tracking=0, )
    total_additional_dotation_current = fields.Float(string='Total Dotacion Vigencia', readonly=True, tracking=0, )
    total_additional_dotation_line = fields.Float(string='Total Dotacion Adicional', readonly=True, tracking=0, )
    total_additional_dotation_monthly = fields.Float(string='Dotacion Mensual', readonly=True, tracking=0, )
    total_additional_dotation = fields.Float(string='Dotaciones additional Contrato', readonly=True, tracking=0, )
    total_additional_nonsalary_bonus = fields.Float(string='Total Bono adicional no salarial', readonly=True,
                                                    tracking=0, )
    total_additional_pos_contract = fields.Float(string='Total Dotacion Contrato', readonly=True, tracking=0, )
    total_additional_pos_current = fields.Float(string='Total Dotacion Vigencia', readonly=True, tracking=0, )
    total_additional_pos_monthly = fields.Float(string='Dotacion Mensual', readonly=True, tracking=0, )
    total_additional_salary_bonus = fields.Float(string='Total Bono adicional salarial', readonly=True, tracking=0, )
    total_additionals_current = fields.Float(string='Adicionales del Puesto y Guarda', readonly=True, tracking=0, )
    total_additionals_monthly = fields.Float(string='Adicionales del Puesto y Guarda', readonly=True, tracking=0, )
    total_additionals = fields.Float(string='Dotaciones Proteccion', readonly=True, tracking=0, )
    total_arl = fields.Float(string='Total ARL', readonly=True, tracking=0, )
    total_basic_salary = fields.Float(string='Total Salario', readonly=True, tracking=0, )
    total_bearing_value = fields.Float(string='Valor Rodamiento', readonly=True, tracking=0, )
    total_benefits = fields.Float(string='Total Prestaciones', readonly=True, tracking=0, )
    total_bonus = fields.Float(string='Primas', readonly=True, tracking=0, )
    total_canine_contract = fields.Float(string='Total Dotacion Contrato', readonly=True, tracking=0, )
    total_canine_cost = fields.Float(string='Caninos', readonly=True, tracking=0, )
    total_canine_current = fields.Float(string='Total Dotacion Vigencia', readonly=True, tracking=0, )
    total_canine_monthly = fields.Float(string='Dotacion Mensual', readonly=True, tracking=0, )
    total_commision_1invoice_current = fields.Float(string='Comisiones Primera Factura', readonly=True, tracking=0, )
    total_commision_1invoice_monthly = fields.Float(string='Comisiones Primera Factura', readonly=True, tracking=0, )
    total_commision_1invoice = fields.Float(string='Comisiones Primera Factura', readonly=True, tracking=0, )
    total_commision_manager_current = fields.Float(string='Comisiones Gerencia Comercial', readonly=True, tracking=0, )
    total_commision_manager_monthly = fields.Float(string='Comisiones Gerencia Comercial', readonly=True, tracking=0, )
    total_commision_manager = fields.Float(string='Comisiones Gerencia Comercial', readonly=True, tracking=0, )
    total_commision_sostent_current = fields.Float(string='Comisiones Sostenimiento', readonly=True, tracking=0, )
    total_commision_sostent_monthly = fields.Float(string='Comisiones Sostenimiento', readonly=True, tracking=0, )
    total_commision_sostent = fields.Float(string='Comisiones Sostenimiento', readonly=True, tracking=0, )
    total_commisions_current = fields.Float(string='Total Comisiones', readonly=True, tracking=0, )
    total_commisions_monthly = fields.Float(string='Total Comisiones', readonly=True, tracking=0, )
    total_commisions = fields.Float(string='Total Comisiones', readonly=True, tracking=0, )
    total_communication_additionnal_contract = fields.Float(string='Total Dotacion Contrato', readonly=True,
                                                            tracking=0, )
    total_communication_additionnal_current = fields.Float(string='Total Dotacion Vigencia', readonly=True,
                                                           tracking=0, )
    total_communication_additionnal_monthly = fields.Float(string='Dotacion Mensual', readonly=True, tracking=0, )
    total_communication_cost = fields.Float(string='Comunicaciones', readonly=True, tracking=0, )
    total_communication_current = fields.Float(string='Comunicaciones', readonly=True, tracking=0, )
    total_communication_monthly = fields.Float(string='Comunicaciones', readonly=True, tracking=0, )
    total_communication = fields.Float(string='Comunicaciones', readonly=True, tracking=0, )
    total_coordinador_total_cost = fields.Float(string='Totales Costos Cordinador', readonly=True, tracking=0, )
    total_coordinador_total_current = fields.Float(string='Totales Costos Cordinador', readonly=True, tracking=0, )
    total_coordinador_total_monthly = fields.Float(string='Totales Costos Cordinador', readonly=True, tracking=0, )
    total_coordinator_cost_current = fields.Float(string='Prestaciones Coordinador', readonly=True, tracking=0, )
    total_coordinator_cost_monthly = fields.Float(string='Prestaciones Coordinador', readonly=True, tracking=0, )
    total_coordinator_cost = fields.Float(string='Prestaciones Coordinador', readonly=True, tracking=0, )
    total_coordinator_current = fields.Float(string='Adicionales del Puesto y Guarda', readonly=True, tracking=0, )
    total_coordinator_monthly = fields.Float(string='Adicionales del Puesto y Guarda', readonly=True, tracking=0, )
    total_coordinator = fields.Float(string='Coordinador Dedicado', readonly=True, tracking=0, )
    total_cost_expense_service = fields.Float(string='Total costos y gastos del servicio', readonly=True, tracking=0, )
    total_cost_general_current = fields.Float(string='Total Costos Directos', readonly=True, tracking=0, )
    total_cost_general_monthly = fields.Float(string='Total Costos Directos', readonly=True, tracking=0, )
    total_cost_general = fields.Float(string='Total Costos Directos', readonly=True, tracking=0, )
    total_cost_other_direct_cost = fields.Float(string='Total Costos Directos', readonly=True, tracking=0, )
    total_cost_sale = fields.Float(string='Total costos de venta', readonly=True, tracking=0, )
    total_dedication_current = fields.Float(string='Dedicados', readonly=True, tracking=0, )
    total_dedication_monthly = fields.Float(string='Dedicados', readonly=True, tracking=0, )
    total_dedication = fields.Float(string='Dedicados', readonly=True, tracking=0, )
    total_direct_cost_current = fields.Float(string='Total Costos Directos', readonly=True, tracking=0, )
    total_direct_cost_monthly = fields.Float(string='Total Costos Directos', readonly=True, tracking=0, )
    total_direct_cost = fields.Float(string='Total Costos Directos', readonly=True, tracking=0, )
    total_dotation_additional_pos_value = fields.Float(string='Dotaciones Total Puesto', readonly=True, tracking=0, )
    total_dotation_additional_position_line = fields.Float(string='Total Dotacion Adicional posicion line',
                                                           readonly=True,
                                                           tracking=0, )
    total_dotation_contract = fields.Float(string='Total Dotacion Contrato', readonly=True, tracking=0, )
    total_dotation_current = fields.Float(string='Total Dotacion Vigencia', readonly=True, tracking=0, )
    total_dotation_line = fields.Float(string='Total Dotacion Anual', readonly=True, tracking=0, )
    total_dotation_monthly = fields.Float(string='Total Dotacion Mensual', readonly=True, tracking=0, )
    total_dotation_pos_value = fields.Float(string='Dotaciones Total Puesto', readonly=True, tracking=0, )
    total_dotation_position_line = fields.Float(string='Total Dotacion puesto', readonly=True, tracking=0, )
    total_dotation_protection_contract = fields.Float(string='Total Dotacion Contrato', readonly=True, tracking=0, )
    total_dotation_protection_current = fields.Float(string='Total Dotacion Vigencia', readonly=True, tracking=0, )
    total_dotation_protection_line = fields.Float(string='Total Dotacion proteccion personal', readonly=True,
                                                  tracking=0, )
    total_dotation_protection_monthly = fields.Float(string='Dotacion Mensual', readonly=True, tracking=0, )
    total_freelance_current = fields.Float(string='Freelance', readonly=True, tracking=0, )
    total_freelance_monthly = fields.Float(string='Freelance', readonly=True, tracking=0, )
    total_freelance = fields.Float(string='Freelance', readonly=True, tracking=0, )
    total_freelancers_contract = fields.Float(string='Total Dotacion Contrato', readonly=True, tracking=0, )
    total_freelancers_current = fields.Float(string='Total Dotacion Vigencia', readonly=True, tracking=0, )
    total_freelancers_monthly = fields.Float(string='Dotacion Mensual', readonly=True, tracking=0, )
    total_freelancers_value = fields.Float(string='Total', readonly=True, tracking=0, )
    total_hours = fields.Integer(string='Total horas', readonly=True, tracking=0, )
    total_income_current = fields.Float(string='Ingreso total', store=True, copy=True, tracking=0, )
    total_income = fields.Float(string='Ingreso total', store=True, copy=True, tracking=0, )
    total_industrial_safety_equipment = fields.Float(string='Dotaciones Seguridad Industrial(EPP)', readonly=True,
                                                     tracking=0, )
    total_labor_commision_current = fields.Float(string='Comisiones Gerencia Comercial', readonly=True, tracking=0, )
    total_labor_commision_monthly = fields.Float(string='Comisiones Gerencia Comercial', readonly=True, tracking=0, )
    total_labor_commision = fields.Float(string='Costo Laboral Comisiones', readonly=True, tracking=0, )
    total_labor_cost_monthly = fields.Float(string='Costo Laboral', store=True, copy=True, tracking=0, )
    total_labor_cost = fields.Float(string='Costo Laboral', store=True, copy=True, tracking=0, )
    total_labor_current = fields.Float(string='Costo Laboral', store=True, copy=True, tracking=0, )
    total_monitor_current = fields.Float(string='Monitoreo', readonly=True, tracking=0, )
    total_monitor_monthly = fields.Float(string='Monitoreo', readonly=True, tracking=0, )
    total_monitor = fields.Float(string='Monitoreo', readonly=True, tracking=0, )
    total_other_cost_current = fields.Float(string='Total Otros Costos', readonly=True, tracking=0, )
    total_other_cost_monthly = fields.Float(string='Total Otros Costos', readonly=True, tracking=0, )
    total_other_cost = fields.Float(string='Total Otros Costos', readonly=True, tracking=0, )
    total_other_direct_cost_admin_sale = fields.Float(string='Total otros costos directos', readonly=True, tracking=0, )
    total_other_direct_cost = fields.Float(string='Total otros costos directos', readonly=True, tracking=0, )
    total_people = fields.Float(string='Cantidad personas', readonly=True, tracking=0, )
    total_post_additional_staffing = fields.Float(string='Dotaciones Adicionales del Puesto', readonly=True,
                                                  tracking=0, )
    total_post_staffing = fields.Float(string='Dotaciones del Puesto', readonly=True, tracking=0, )
    total_rotation_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    total_rotation_monthly = fields.Float(string='Selección', readonly=True, tracking=0, )
    total_rotation = fields.Float(string='Selección', readonly=True, tracking=0, )
    total_salaries_benefist_social_parafiscal = fields.Float(string='Costos Total', readonly=True, tracking=0, )
    total_sale_value = fields.Float(string='Valor total de la venta', store=True, copy=True, tracking=0, )
    total_selection_current = fields.Float(string='Selección', readonly=True, tracking=0, )
    total_selection_line = fields.Float(string='Total Selección', readonly=True, tracking=0, )
    total_selection_monthly = fields.Float(string='Selección', readonly=True, tracking=0, )
    total_selection = fields.Float(string='Selección', readonly=True, tracking=0, )
    total_severance_int = fields.Float(string='Int de Cesantias', readonly=True, tracking=0, )
    total_severance = fields.Float(string='Cesancias', readonly=True, tracking=0, )
    total_social_security = fields.Float(string='Total Seguridad Social', readonly=True, tracking=0, )
    total_staffing = fields.Float(string='Dotaciones del Personal', readonly=True, tracking=0, )
    total_supplementary_work_value = fields.Float(string='Valor Trabajo Suplementario', readonly=True, tracking=0, )
    total_supplies_current = fields.Float(string='Dotaciones Adicionales del Personal', readonly=True, tracking=0, )
    total_supplies_monthly = fields.Float(string='Dotaciones Adicionales del Personal', readonly=True, tracking=0, )
    total_supplies_pos_current = fields.Float(string='Dotaciones Adicionales del Personal', readonly=True, tracking=0, )
    total_supplies_pos_monthly = fields.Float(string='Dotaciones Adicionales del Personal', readonly=True, tracking=0, )
    total_supplies_pos = fields.Float(string='Dotaciones Adicionales del Personal', readonly=True, tracking=0, )
    total_supplies = fields.Float(string='Dotaciones Adicionales del Personal', readonly=True, tracking=0, )
    total_support_cost = fields.Float(string='Apoyo', readonly=True, tracking=0, )
    total_transport_assistant = fields.Float(string='Auxilio de transporte', readonly=True, tracking=0, )
    total_vacation = fields.Float(string='Vacaciones', readonly=True, tracking=0, )
    total_vehicle_contract = fields.Float(string='Total Dotacion Contrato', readonly=True, tracking=0, )
    total_vehicle_current = fields.Float(string='Total Dotacion Vigencia', readonly=True, tracking=0, )
    total_vehicle_monthly = fields.Float(string='Dotacion Mensual', readonly=True, tracking=0, )
    total_vehicle_value = fields.Float(string='Total', readonly=True, tracking=0, )
    total_weapon_contract = fields.Float(string='Total Dotacion Contrato', readonly=True, tracking=0, )
    total_weapon_cost = fields.Float(string='Armamento', readonly=True, tracking=0, )
    total_weapon_current = fields.Float(string='Total Dotacion Vigencia', readonly=True, tracking=0, )
    total_weapon_monthly = fields.Float(string='Dotacion Mensual', readonly=True, tracking=0, )
    training_cost = fields.Float(string='Capacitacion', readonly=True, tracking=0, )
    training_id = fields.Many2one(string='Capacitación', store=True, copy=True, tracking=0,
                                  comodel_name='quoter.training', )
    transport_id = fields.Many2one(string='Medio de transporte', store=True, copy=True, tracking=0,
                                   comodel_name='quoter.transport', )
    transportation_assistance = fields.Float(string='Auxilio de transporte', store=True, copy=True, tracking=0, )
    uac_current = fields.Float(string='UAC', readonly=True, tracking=0, )
    uac_monthly = fields.Float(string='UAC', readonly=True, tracking=0, )
    uac = fields.Float(string='UAC', readonly=True, tracking=0, )
    unforeseen_current = fields.Float(string='Imprevistos', readonly=True, tracking=0, )
    unforeseen_monthly = fields.Float(string='Imprevistos', readonly=True, tracking=0, )
    unforeseen = fields.Float(string='Imprevistos', readonly=True, tracking=0, )
    use_parent_modality = fields.Boolean(string='Usa modalidad padre', readonly=True, tracking=0, )
    weapon_cost = fields.Float(string='Armamento', readonly=True, tracking=0, )
    weapon_type_id = fields.Many2one(string='Tipo de armamento', store=True, copy=True, tracking=0,
                                     comodel_name='quoter.weapon.type', )
    weekdays = fields.Many2many(relation='salequoterline_weekdays_rel', column1='salequoterline_id',
                                column2='weekdays_id', string='Dias de la semana', store=True, readonly=True,
                                tracking=0,
                                comodel_name='res.weekday', )


class Accountmoveprofile(models.Model):
    _name = 'account.move.profile'
    _description = 'account.move.profile'
    adicional = fields.Boolean(string='Costos adicionales', store=True, copy=True, tracking=0, )
    ays = fields.Boolean(string='A&S', store=True, copy=True, tracking=0, )
    city = fields.Boolean(string='Ciudad', store=True, copy=True, tracking=0, )
    detail = fields.Boolean(string='Detalle linea', store=True, copy=True, tracking=0, )
    dias_mes = fields.Boolean(string='Dias del mes', store=True, copy=True, tracking=0, )
    dias_resumen = fields.Boolean(string='Dias resumen', store=True, copy=True, tracking=0, )
    dias = fields.Boolean(string='Dias', store=True, copy=True, tracking=0, )
    distribution = fields.Boolean(string='Distribucion', store=True, copy=True, tracking=0, )
    dom_diur = fields.Boolean(string='Horas dom diurnas', store=True, copy=True, tracking=0, )
    dom_noct = fields.Boolean(string='Horas dom nocturnas', store=True, copy=True, tracking=0, )
    duracion = fields.Boolean(string='Duracion', store=True, copy=True, tracking=0, )
    fes_diur = fields.Boolean(string='Horas fes diurnas', store=True, copy=True, tracking=0, )
    fes_noct = fields.Boolean(string='Horas fes nocturnas', store=True, copy=True, tracking=0, )
    horario = fields.Boolean(string='Horario', store=True, copy=True, tracking=0, )
    horas_diurno = fields.Boolean(string='Horas diurno', store=True, copy=True, tracking=0, )
    horas_nocturno = fields.Boolean(string='Horas nocturnas', store=True, copy=True, tracking=0, )
    interventor = fields.Boolean(string='Interventor', store=True, copy=True, tracking=0, )
    medio = fields.Boolean(string='Medio', store=True, copy=True, tracking=0, )
    mod_servicio = fields.Boolean(string='Linea de negocio', store=True, copy=True, tracking=0, )
    modalidad = fields.Boolean(string='Modalidad', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Perfil', store=True, copy=True, tracking=0, )
    programacion = fields.Boolean(string='Programacion', store=True, copy=True, tracking=0, )
    puesto_int_code = fields.Boolean(string='Codigo interno cliente', store=True, copy=True, tracking=0, )
    puesto_int_zone = fields.Boolean(string='Zona interna cliente', store=True, copy=True, tracking=0, )
    puesto = fields.Boolean(string='Puesto', store=True, copy=True, tracking=0, )
    quantity = fields.Boolean(string='Cantidad', store=True, copy=True, tracking=0, )
    regional = fields.Boolean(string='Regional', store=True, copy=True, tracking=0, )
    service_quantity = fields.Boolean(string='# Serv', store=True, copy=True, tracking=0, )
    subtotal = fields.Boolean(string='Subtotal antes de A&S', store=True, copy=True, tracking=0, )
    tipo_servicio = fields.Boolean(string='Tipo de servicio', store=True, copy=True, tracking=0, )
    total_ays = fields.Boolean(string='Total A&S', store=True, copy=True, tracking=0, )
    total_validated = fields.Boolean(string='Total validado', store=True, copy=True, tracking=0, )
    total = fields.Boolean(string='Total general', store=True, copy=True, tracking=0, )
    valor_total = fields.Boolean(string='Valor total', store=True, copy=True, tracking=0, )
    valor = fields.Boolean(string='Valor antes de A&S', store=True, copy=True, tracking=0, )


class Hrrosteradicionalday(models.Model):
    _name = 'hr.roster.adicional.day'
    _description = 'hr.roster.adicional.day'
    adicional = fields.Many2one(string='Adicional', store=True, copy=True, tracking=0,
                                comodel_name='hr.roster.adicionales', )
    custom_time = fields.Boolean(string='Horario personalizado', store=True, copy=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    horario_id = fields.Many2one(string='Horario', store=True, copy=True, tracking=0,
                                 comodel_name='hr.roster.horario', )
    modalidad_id = fields.Many2one(string='Modalidad', store=True, copy=True, tracking=0,
                                   comodel_name='hr.roster.modalidad', )
    time_in = fields.Char(string='Entrada', store=True, required=True, copy=True, tracking=0, )
    time_out = fields.Char(string='Salida', store=True, required=True, copy=True, tracking=0, )


class Accountpaymentconfigline(models.Model):
    _name = 'account.payment.config.line'
    _description = 'account.payment.config.line'
    adjust = fields.Boolean(string='Ajuste a tamaño', store=True, copy=True, tracking=0, )
    advance_content = fields.Text(string='Contenido - Anticipos', store=True, copy=True, tracking=0, )
    content = fields.Text(string='Contenido', store=True, copy=True, tracking=0, )
    decimal_qty = fields.Integer(string='Número de decimales', store=True, copy=True, tracking=0, )
    fill = fields.Char(string='Caracter de relleno', store=True, copy=True, tracking=0, )
    footer_config_id = fields.Many2one(string='Configuracion Pie', store=True, copy=True, tracking=0,
                                       comodel_name='account.payment.file.config', )
    header_config_id = fields.Many2one(string='Configuracion encabezado', store=True, copy=True, tracking=0,
                                       comodel_name='account.payment.file.config', )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    payment_config_id = fields.Many2one(string='Configuracion detalle', store=True, copy=True, tracking=0,
                                        comodel_name='account.payment.file.config', )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )
    size = fields.Integer(string='Tamaño', store=True, copy=True, tracking=0, )


class Variableseconomicasretefuentemarginalline(models.Model):
    _name = 'variables.economicas.retefuente.marginal.line'
    _description = 'variables.economicas.retefuente.marginal.line'
    ajuste = fields.Float(string='Ajuste (UVT)', store=True, required=True, copy=True, tracking=0, )
    retefuente_id = fields.Many2one(string='Retefuente', store=True, copy=True, tracking=0,
                                    comodel_name='variables.economicas.retefuente', )
    tarifa = fields.Float(string='Tarifa (%)', store=True, required=True, copy=True, tracking=0, )
    valor_desde = fields.Float(string='Valor desde(UVT)', store=True, required=True, copy=True, tracking=0, )
    valor_hasta = fields.Float(string='Valor hasta (UVT)', store=True, required=True, copy=True, tracking=0, )


class Openpettycash(models.Model):
    _name = 'open.petty.cash'
    _description = 'open.petty.cash'
    ammount = fields.Float(string='Monto de apertura', store=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Responsable', store=True, copy=True, tracking=0,
                                  comodel_name='hr.employee', )


class Modelbasicpayslipnovelty(models.Model):
    _name = 'model.basic.payslip.novelty'
    _description = 'model.basic.payslip.novelty'
    amount = fields.Float(string='Valor', store=True, copy=True, tracking=100, )
    approve_date = fields.Date(string='Fecha de aprobación', store=True, copy=True, tracking=100, )
    company_id = fields.Many2one(string='Compañia', store=True, readonly=True, copy=True, tracking=100,
                                 comodel_name='res.company', )
    contract_group_id = fields.Many2one(string='Grupo de Contrato', readonly=True, tracking=100,
                                        comodel_name='hr.contract.group', )
    contract_id = fields.Many2one(string='Contrato', store=True, required=True, copy=True, tracking=100,
                                  comodel_name='hr.contract', )
    date_end = fields.Date(string='Fecha Final', store=True, copy=True, tracking=100, )
    date_start = fields.Date(string='Fecha Inicio', store=True, required=True, copy=True, tracking=100, )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=100,
                                  comodel_name='hr.employee', )
    name = fields.Char(string='Nombre', store=True, readonly=True, copy=True, tracking=100, )


class Accountbankmultitransaction(models.Model):
    _name = 'account.bank.multi.transaction'
    _description = 'account.bank.multi.transaction'
    amount = fields.Float(string='Valor', store=True, copy=True, tracking=0, )
    avancys_statement_id = fields.Many2one(string='Extracto', store=True, copy=True, tracking=0,
                                           comodel_name='account.bank.statement.avancys', )
    date = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )
    selected = fields.Boolean(string='Seleccionado', store=True, copy=True, tracking=0, )
    transaction_id = fields.Many2one(string='Transaccion bancaria', store=True, copy=True, tracking=0,
                                     comodel_name='account.bank.statement.line.avancys', )


class Certificadoreportingresosline(models.Model):
    _name = 'certificado.report.ingresos.line'
    _description = 'certificado.report.ingresos.line'
    amount = fields.Float(string='Valor %', store=True, copy=True, tracking=0, )
    concepts = fields.Char(string='Conceptos de nomina', store=True, copy=True, tracking=0, )
    condepts_ids = fields.Many2many(relation='certificadoreporting_condepts_ids_rel', column1='certificadoreporting_id',
                                    column2='condepts_ids_id', string='Conceptos de nomina', store=True, copy=True,
                                    tracking=0,
                                    comodel_name='hr.concept', )
    description = fields.Char(string='Descripcion', store=True, copy=True, tracking=0, )
    line_id = fields.Many2one(string='Parent', store=True, copy=True, tracking=0,
                              comodel_name='certificado.report.ingresos', )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )


class Certificadoingresoslineitem(models.Model):
    _name = 'certificado.ingresos.line.item'
    _description = 'certificado.ingresos.line.item'
    amount = fields.Float(string='amount', store=True, readonly=True, copy=True, tracking=0, )
    certificado_id = fields.Many2one(string='Certificado', store=True, readonly=True, required=True, copy=True,
                                     tracking=0, comodel_name='certificado.ingresos', )
    company_id = fields.Many2one(string='Compañia', store=True, readonly=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    concepto_id = fields.Many2one(string='Conceptos', store=True, readonly=True, copy=True, tracking=0,
                                  comodel_name='certificado.report.ingresos.line', )
    employee_id = fields.Many2one(string='Empleado', store=True, readonly=True, copy=True, tracking=0,
                                  comodel_name='hr.employee', )
    move_ids = fields.Text(string='Movimientos', store=True, readonly=True, copy=True, tracking=0, )
    name = fields.Char(string='Name', store=True, readonly=True, copy=True, tracking=0, )
    parent_id = fields.Many2one(string='Parent', store=True, readonly=True, copy=True, tracking=0,
                                comodel_name='certificado.ingresos.line', )


class Fpapygc(models.Model):
    _name = 'fpa.pyg.c'
    _description = 'fpa.pyg.c'
    amount_label_comparative = fields.Char(string='Etiqueta monto comparativo', store=True, copy=True, tracking=0, )
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha final', store=True, copy=True, tracking=0, )
    date = fields.Datetime(string='Fecha', store=True, copy=True, tracking=0, )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Fpaequitychanges(models.Model):
    _name = 'fpa.equity.changes'
    _description = 'fpa.equity.changes'
    amount_label_comparative = fields.Char(string='Etiqueta monto comparativo', store=True, copy=True, tracking=0, )
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha final', store=True, copy=True, tracking=0, )
    date = fields.Datetime(string='Fecha', store=True, copy=True, tracking=0, )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Projectserviceorderlineinvoice(models.Model):
    _name = 'project.service.order.line.invoice'
    _description = 'project.service.order.line.invoice'
    amount_total_invoiced = fields.Float(string='Total Facturado', store=True, readonly=True, tracking=0, )
    client_id = fields.Many2one(string='Cliente', index=True, store=True, readonly=True, tracking=0,
                                comodel_name='res.partner', )
    description = fields.Char(string='Description', store=True, copy=True, tracking=0, )
    end_date = fields.Datetime(string='Fecha fin servicio', store=True, copy=True, tracking=0, )
    fact_end_date = fields.Date(string='Fin Facturacion', store=True, copy=True, tracking=0, )
    fact_start_date = fields.Date(string='Inicio Facturacion', store=True, copy=True, tracking=0, )
    fecha_inicio = fields.Date(string='Fecha de programacion', store=True, copy=True, tracking=0, )
    info = fields.Char(string='Mensaje de cancelación', store=True, copy=True, tracking=100, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='projectserviceorderl_message_channel_ids_rel',
                                           column1='projectserviceorderl_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='projectserviceorderl_message_partner_ids_rel',
                                           column1='projectserviceorderl_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    order_id = fields.Many2one(string='Orden', index=True, store=True, copy=True, tracking=0,
                               comodel_name='project.service.order', )
    order_line_id = fields.Many2one(string='Linea de Orden', index=True, store=True, copy=True, tracking=0,
                                    comodel_name='project.service.order.line', )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.product', )
    project_id = fields.Many2one(string='Proyecto', index=True, store=True, readonly=True, tracking=100,
                                 comodel_name='project.project', )
    puesto_code = fields.Char(string='Puesto', store=True, readonly=True, tracking=0, )
    puesto_id = fields.Many2one(string='Puesto', index=True, store=True, copy=True, tracking=0,
                                comodel_name='hr.roster.puesto', )
    reason_to_cancel = fields.Many2one(string='Razon de cancelación', store=True, copy=True, tracking=100,
                                       comodel_name='project.service.order.line.item.cancel', )
    remaining_value = fields.Float(string='Valor residual', store=True, readonly=True, tracking=0, )
    start_date = fields.Datetime(string='Fecha inicio servicio', store=True, copy=True, tracking=0, )
    total_value = fields.Float(string='Valor total', store=True, copy=True, tracking=0, )
    valor_mensual = fields.Float(string='Valor mensual', store=True, copy=True, tracking=0, )


class Activospuestowiz(models.Model):
    _name = 'activos.puesto.wiz'
    _description = 'activos.puesto.wiz'
    analytic_account_id = fields.Many2one(string='Centro de costo', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    puesto_actual = fields.Many2one(string='Puesto actual', store=True, readonly=True, copy=True, tracking=0,
                                    comodel_name='hr.roster.puesto', )
    serial_id = fields.Many2one(string='Activo', store=True, required=True, copy=True, tracking=0,
                                comodel_name='account.asset', )
    tipo = fields.Char(string='Tipo de operacion permitido', readonly=True, tracking=0, )
    val_asign = fields.Boolean(string='Confirmar asignacion', store=True, copy=True, tracking=0, )
    val_desv = fields.Boolean(string='Desvincular activo', store=True, copy=True, tracking=0, )
    val_transf = fields.Boolean(string='Confirmar transferencia', store=True, copy=True, tracking=0, )


class Hrrostertimesheet(models.Model):
    _name = 'hr.roster.timesheet'
    _description = 'hr.roster.timesheet'
    analytic_account_id = fields.Many2one(string='Centro de costo', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    close_date = fields.Date(string='Fecha de cierre', store=True, copy=True, tracking=0, )
    contrait_id = fields.Many2one(string='Contrato', store=True, copy=True, tracking=0, comodel_name='hr.contract', )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    hours = fields.Float(string='Horas', store=True, copy=True, tracking=0, )
    modalidad_id = fields.Many2one(string='Modalidad', store=True, copy=True, tracking=0,
                                   comodel_name='hr.roster.modalidad', )
    name = fields.Char(string='Descripcion', store=True, copy=True, tracking=0, )
    value = fields.Float(string='Valor', store=True, copy=True, tracking=0, )


class Stockreportkardexdotline(models.Model):
    _name = 'stock.report.kardex.dot.line'
    _description = 'stock.report.kardex.dot.line'
    analytic_account_id = fields.Many2one(string='Centro de costo', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    date_dot_f = fields.Datetime(string='Fecha Dotacion Final', store=True, copy=True, tracking=0, )
    date_dot_i = fields.Datetime(string='Fecha Dotacion Inicial', store=True, copy=True, tracking=0, )
    date = fields.Datetime(string='Fecha', store=True, copy=True, tracking=0, )
    doc_orig = fields.Char(string='Documento Origen', store=True, copy=True, tracking=0, )
    dot_ret = fields.Char(string='DOT/RET', store=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    location_dest_id = fields.Many2one(string='Ubicacion Destino', store=True, copy=True, tracking=0,
                                       comodel_name='stock.location', )
    location_id = fields.Many2one(string='Ubicacion Origen', store=True, copy=True, tracking=0,
                                  comodel_name='stock.location', )
    move_id = fields.Many2one(string='Movimiento', store=True, copy=True, tracking=0, comodel_name='stock.picking', )
    num_ced = fields.Char(string='Cedula', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.product', )
    qty = fields.Float(string='Cantidad', store=True, copy=True, tracking=0, )
    type_move = fields.Char(string='Tipo de movimiento', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Payslipanalyticdistribution(models.Model):
    _name = 'payslip.analytic.distribution'
    _description = 'payslip.analytic.distribution'
    analytic_account_id = fields.Many2one(string='Cuenta analitica', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    payslip_id = fields.Many2one(string='Nomina relacionada', store=True, copy=True, tracking=0,
                                 comodel_name='hr.payslip', )
    rate = fields.Float(string='Distribucion', store=True, copy=True, tracking=0, )


class Hrrosterclosedistribution(models.Model):
    _name = 'hr.roster.close.distribution'
    _description = 'hr.roster.close.distribution'
    analytic_account_id = fields.Many2one(string='Cuenta analitica', store=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    date = fields.Date(string='Fecha de referencia', store=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Employee', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    name = fields.Char(string='Nombre', readonly=True, tracking=0, )
    rate = fields.Float(string='Distribucion', store=True, copy=True, tracking=0, )


class Projectdistributionline(models.Model):
    _name = 'project.distribution.line'
    _description = 'project.distribution.line'
    analytic_account_id = fields.Many2one(string='Cuenta Analítica', store=True, required=True, copy=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    name = fields.Char(string='Nombre', readonly=True, required=True, tracking=0, )
    project_distribution_id = fields.Many2one(string='Distribución', store=True, required=True, copy=True, tracking=0,
                                              comodel_name='project.distribution', )
    project_id = fields.Many2one(string='Proyecto', store=True, copy=True, tracking=0,
                                 comodel_name='project.project', )
    project_percentage = fields.Float(string='Porcentaje', store=True, required=True, copy=True, tracking=0, )


class Modelbasicpayslipnoveltytype(models.Model):
    _name = 'model.basic.payslip.novelty.type'
    _description = 'model.basic.payslip.novelty.type'
    apr_adm_credit = fields.Many2one(string='Credito Aprendiz Administrativo', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    apr_adm_debit = fields.Many2one(string='Debito Aprendiz Administrativo', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    apr_com_credit = fields.Many2one(string='Credito Aprendiz Comercial', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    apr_com_debit = fields.Many2one(string='Debito Aprendiz Comercial', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    apr_ope_credit = fields.Many2one(string='Credito Aprendiz Operativa', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    apr_ope_debit = fields.Many2one(string='Debito Aprendiz Operativa', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    apr_pro_credit = fields.Many2one(string='Credito Aprendiz Producción', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    apr_pro_debit = fields.Many2one(string='Debito Aprendiz Producción', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    code = fields.Char(string='Código', store=True, required=True, copy=True, tracking=0, )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    int_adm_credit = fields.Many2one(string='Credito Integral Administrativo', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    int_adm_debit = fields.Many2one(string='Debito Integral Administrativo', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    int_com_credit = fields.Many2one(string='Credito Integral Comercial', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    int_com_debit = fields.Many2one(string='Debito Integral Comercial', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    int_ope_credit = fields.Many2one(string='Credito Integral Operativa', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    int_ope_debit = fields.Many2one(string='Debito Integral Operativa', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    int_pro_credit = fields.Many2one(string='Credito Integral Producción', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    int_pro_debit = fields.Many2one(string='Debito Integral Producción', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Tercero', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    reg_adm_credit = fields.Many2one(string='Credito Regular Administrativo', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    reg_adm_debit = fields.Many2one(string='Debito Regular Administrativo', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    reg_com_credit = fields.Many2one(string='Credito Regular Comercial', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    reg_com_debit = fields.Many2one(string='Debito Regular Comercial', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    reg_ope_credit = fields.Many2one(string='Credito Regular Operativa', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    reg_ope_debit = fields.Many2one(string='Debito Regular Operativa', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )
    reg_pro_credit = fields.Many2one(string='Credito Regular Producción', store=True, copy=True, tracking=0,
                                     comodel_name='account.account', )
    reg_pro_debit = fields.Many2one(string='Debito Regular Producción', store=True, copy=True, tracking=0,
                                    comodel_name='account.account', )


class Accountassetclosewizard(models.Model):
    _name = 'account.asset.close.wizard'
    _description = 'account.asset.close.wizard'
    asset_id = fields.Many2one(string='Activo', store=True, copy=True, tracking=0, comodel_name='account.asset', )
    cliente_id = fields.Many2one(string='Cliente', store=True, copy=True, tracking=0, comodel_name='res.partner', )
    date_maturity = fields.Date(string='Fecha de Vencimiento', store=True, copy=True, tracking=0, )
    invoice_id = fields.Many2one(string='Factura', store=True, copy=True, tracking=0, comodel_name='account.move', )
    partner_id = fields.Many2one(string='Tercero', store=True, copy=True, tracking=0, comodel_name='res.partner', )


class Accountassetprocesswizard(models.Model):
    _name = 'account.asset.process.wizard'
    _description = 'account.asset.process.wizard'
    asset_ids = fields.Many2many(relation='accountassetprocessw_asset_ids_rel', column1='accountassetprocessw_id',
                                 column2='asset_ids_id', string='Activos a procesar', store=True, copy=True, tracking=0,
                                 comodel_name='account.asset', )
    date_to_process = fields.Date(string='Mes a procesar', store=True, required=True, copy=True, tracking=0, )


class Viewcenterbutton(models.Model):
    _name = 'view.center.button'
    _description = 'view.center.button'
    automation_id = fields.Many2one(string='Automation', store=True, copy=True, tracking=0,
                                    comodel_name='base.automation', )
    button_key = fields.Char(string='Button Key', store=True, required=True, copy=True, tracking=0, )


class Hremployeeaccreditation(models.Model):
    _name = 'hr.employee.accreditation'
    _description = 'hr.employee.accreditation'
    auxiliar_file = fields.Many2many(relation='hremployeeaccreditat_auxiliar_file_rel',
                                     column1='hremployeeaccreditat_id', column2='auxiliar_file_id', string='Adjunto',
                                     store=True, copy=True, tracking=0,
                                     comodel_name='ir.attachment', )
    course_code = fields.Char(string='Código curso (Antiguo)', store=True, copy=True, tracking=0,
                              comodel_name='ir.attachment', )
    course_type_id = fields.Many2one(string='Código curso', store=True, copy=True, tracking=0,
                                     comodel_name='security.course.type', )
    couse_number = fields.Char(string='Nro.', store=True, copy=True, tracking=0, comodel_name='ir.attachment', )
    days_to_expiration = fields.Integer(string='Días para vencer', store=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    end_date = fields.Datetime(string='Fecha fin', store=True, required=True, copy=True, tracking=0, )
    init_date = fields.Datetime(string='Fecha inicio', store=True, required=True, copy=True, tracking=0, )
    nit_school = fields.Char(string='NIT Escuela', store=True, copy=True, tracking=0, comodel_name='ir.attachment', )
    type_id = fields.Many2one(string='Tipo', store=True, copy=True, tracking=0,
                              comodel_name='hr.employee.accreditation.line', )
    x_auxiliar_file_url = fields.Char(string='Url Soporte', store=True, readonly=True, tracking=0, )
    x_estado = fields.Char(string='Estado', store=True, readonly=True, tracking=0, )
    x_fecha_de_radicacion = fields.Date(string='Fecha De Radicación', store=True, copy=True, tracking=0, )
    x_job_id = fields.Many2one(string='Cargo Empresa', tracking=0, comodel_name='hr.job', )
    x_numero_de_radicado = fields.Char(string='Número de Radicado', store=True, copy=True, tracking=0, )


class Hremployeecredentials(models.Model):
    _name = 'hr.employee.credentials'
    _description = 'hr.employee.credentials'
    auxiliar_file = fields.Many2many(relation='hremployeecredential_auxiliar_file_rel',
                                     column1='hremployeecredential_id', column2='auxiliar_file_id', string='Adjunto',
                                     store=True, copy=True, tracking=0,
                                     comodel_name='ir.attachment', )
    days_to_expiration = fields.Integer(string='Días para vencer', store=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    end_date = fields.Datetime(string='Fecha fin', store=True, required=True, copy=True, tracking=0, )
    init_date = fields.Datetime(string='Fecha inicio', store=True, required=True, copy=True, tracking=0, )
    type_id = fields.Many2one(string='Tipo de credencial', store=True, required=True, copy=True, tracking=0,
                              comodel_name='hr.employee.credentials.line', )
    x_auxiliar_file_url = fields.Char(string='URL del Adjunto', store=True, readonly=True, tracking=0, )
    x_city_partner_id = fields.Many2one(string='Ciudad', store=True, tracking=0, comodel_name='res.city', )
    x_estado = fields.Char(string='Estado', store=True, readonly=True, tracking=0, )
    x_regional_name = fields.Many2one(string='Regional', store=True, readonly=True, tracking=0,
                                      comodel_name='hr.branch', )


class Accountbankmultimove(models.Model):
    _name = 'account.bank.multi.move'
    _description = 'account.bank.multi.move'
    avancys_statement_id = fields.Many2one(string='Extracto', store=True, copy=True, tracking=0,
                                           comodel_name='account.bank.statement.avancys', )
    credit = fields.Float(string='Credito', store=True, copy=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copy=True, tracking=0, )
    move_line_id = fields.Many2one(string='Movimiento contable', store=True, copy=True, tracking=0,
                                   comodel_name='account.move.line', )
    selected = fields.Boolean(string='Seleccionado', store=True, copy=True, tracking=0, )


class Quoterfinancing(models.Model):
    _name = 'quoter.financing'
    _description = 'quoter.financing'
    balance = fields.Float(string='Saldo', store=True, copy=True, tracking=0, )
    capital = fields.Float(string='Capital', store=True, copy=True, tracking=0, )
    extra = fields.Float(string='Extras', store=True, copy=True, tracking=0, )
    interests = fields.Float(string='Intereses', store=True, copy=True, tracking=0, )
    quota_number = fields.Float(string='Cuota', store=True, copy=True, tracking=0, )
    quota = fields.Float(string='Cuota', store=True, copy=True, tracking=0, )
    sale_quoter_id = fields.Many2one(string='sale_quoter_id', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter', )


class Accountpaymentfileconfig(models.Model):
    _name = 'account.payment.file.config'
    _description = 'account.payment.file.config'
    bank_id = fields.Many2one(string='Banco', store=True, copy=True, tracking=0, comodel_name='res.bank', )
    footer = fields.Boolean(string='Footer instead header', store=True, copy=True, tracking=0, )


class Hrpayrollembargoline(models.Model):
    _name = 'hr.payroll.embargo.line'
    _description = 'hr.payroll.embargo.line'
    base_devengado = fields.Float(string='Base de devengo', store=True, copy=True, tracking=0, )
    category_id = fields.Many2one(string='Categoria', store=True, copy=True, tracking=0,
                                  comodel_name='hr.payroll.embargo.category', )
    contract_id = fields.Many2one(string='Contrato', store=True, readonly=True, tracking=0,
                                  comodel_name='hr.contract', )
    date = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )
    description = fields.Char(string='Nombre', readonly=True, tracking=0, )
    embargo_due = fields.Float(string='Deuda', readonly=True, tracking=0, )
    embargo_id = fields.Many2one(string='Embargo', store=True, copy=True, tracking=0,
                                 comodel_name='hr.payroll.embargo', )
    embargo_share = fields.Float(string='Cuota', readonly=True, tracking=0, )
    payslip_id = fields.Many2one(string='Nomina', store=True, copy=True, tracking=0, comodel_name='hr.payslip', )
    payslip_period_id = fields.Many2one(string='Periodo', store=True, copy=True, tracking=0,
                                        comodel_name='hr.period', )
    payslip_type_id = fields.Many2one(string='Tipo de nomina', store=True, copy=True, tracking=0,
                                      comodel_name='hr.payslip.type', )
    share_value = fields.Float(string='Valor de la cuota', store=True, copy=True, tracking=0, )


class Studioapprovalrule(models.Model):
    _name = 'studio.approval.rule'
    _description = 'studio.approval.rule'
    button_id = fields.Many2one(string='Button', store=True, copy=True, tracking=0, comodel_name='studio.button', )
    description = fields.Char(string='Description', store=True, copy=True, tracking=0, )
    group_id = fields.Many2one(string='Groups', store=True, copy=True, tracking=0, comodel_name='res.groups', )


class Hrrosterpuestocargo(models.Model):
    _name = 'hr.roster.puesto.cargo'
    _description = 'hr.roster.puesto.cargo'
    cargo_id = fields.Many2one(string='Cargo', store=True, required=True, copy=True, tracking=0,
                               comodel_name='hr.job', )
    puesto_id = fields.Many2one(string='Puesto', store=True, required=True, copy=True, tracking=0,
                                comodel_name='hr.roster.puesto', )


class Hrrosterpuestobono(models.Model):
    _name = 'hr.roster.puesto.bono'
    _description = 'hr.roster.puesto.bono'
    category_id = fields.Many2one(string='Categoria de novedad', store=True, copy=True, tracking=0,
                                  comodel_name='hr.novelty.type', )
    name = fields.Char(string='Descripcion', store=True, copy=True, tracking=0, )
    puesto_id = fields.Many2one(string='Puesto Asociado', store=True, copy=True, tracking=0,
                                comodel_name='hr.roster.puesto', )
    value = fields.Float(string='Valor', store=True, copy=True, tracking=0, )


class Hrpayrollembargopriorityline(models.Model):
    _name = 'hr.payroll.embargo.priority.line'
    _description = 'hr.payroll.embargo.priority.line'
    category_id = fields.Many2one(string='Categoria', store=True, copy=True, tracking=0,
                                  comodel_name='hr.payroll.embargo.category', )
    embargo_priority_id = fields.Many2one(string='Prioridad Embargo', store=True, copy=True, tracking=0,
                                          comodel_name='hr.payroll.embargo.priority', )
    priority = fields.Integer(string='Prioridad', store=True, copy=True, tracking=0, )


class Wizardcertificadoretencion(models.Model):
    _name = 'wizard.certificado.retencion'
    _description = 'wizard.certificado.retencion'
    cert_id = fields.Many2one(string='Certificado', store=True, required=True, copy=True, tracking=0,
                              comodel_name='certificado.report.retencion', )
    company_id = fields.Many2one(string='Compañia', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    date_expedition = fields.Date(string='Fecha de Expedicion', store=True, copy=True, tracking=0, )
    partner_ids = fields.Many2many(relation='wizardcertificadoret_partner_ids_rel', column1='wizardcertificadoret_id',
                                   column2='partner_ids_id', string='Terceros', store=True, copy=True, tracking=0,
                                   comodel_name='res.partner', )
    periodo_id = fields.Many2one(string='Periodo', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='certificado.report.retencion.periodicidad', )


class Fpainventariobalance(models.Model):
    _name = 'fpa.inventario.balance'
    _description = 'fpa.inventario.balance'
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha final', store=True, copy=True, tracking=0, )
    date = fields.Datetime(string='Fecha', store=True, copy=True, tracking=0, )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Fpaflujocaja(models.Model):
    _name = 'fpa.flujocaja'
    _description = 'fpa.flujocaja'
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha final', store=True, copy=True, tracking=0, )
    date = fields.Datetime(string='Fecha', store=True, copy=True, tracking=0, )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Fpapygccanalytic(models.Model):
    _name = 'fpa.pyg.cc.analytic'
    _description = 'fpa.pyg.cc.analytic'
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha final', store=True, copy=True, tracking=0, )
    date = fields.Datetime(string='Fecha', store=True, copy=True, tracking=0, )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Fpaauxiliarequivalente(models.Model):
    _name = 'fpa.auxiliar.equivalente'
    _description = 'fpa.auxiliar.equivalente'
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha final', store=True, copy=True, tracking=0, )
    date = fields.Datetime(string='Fecha', store=True, copy=True, tracking=0, )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Fpadiario(models.Model):
    _name = 'fpa.diario'
    _description = 'fpa.diario'
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha final', store=True, copy=True, tracking=0, )
    date = fields.Datetime(string='Fecha', store=True, copy=True, tracking=0, )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Fpaauxiliaranalitico(models.Model):
    _name = 'fpa.auxiliar.analitico'
    _description = 'fpa.auxiliar.analitico'
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha final', store=True, copy=True, tracking=0, )
    date = fields.Datetime(string='Fecha', store=True, copy=True, tracking=0, )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Fpaauxiliar(models.Model):
    _name = 'fpa.auxiliar'
    _description = 'fpa.auxiliar'
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha final', store=True, copy=True, tracking=0, )
    date = fields.Datetime(string='Fecha', store=True, copy=True, tracking=0, )
    detailed = fields.Boolean(string='Detallado', store=True, copy=True, tracking=0, )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    structure_id = fields.Many2one(string='Estructura', store=True, copy=True, tracking=0,
                                   comodel_name='account.financial.structure', )
    totalizado_por_tercero = fields.Boolean(string='Totalizado por tercero', store=True, copy=True, tracking=0, )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Fpaauxiliarfc(models.Model):
    _name = 'fpa.auxiliar.fc'
    _description = 'fpa.auxiliar.fc'
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha final', store=True, copy=True, tracking=0, )
    date = fields.Datetime(string='Fecha', store=True, copy=True, tracking=0, )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Fpabalancepruebas(models.Model):
    _name = 'fpa.balance.pruebas'
    _description = 'fpa.balance.pruebas'
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha final', store=True, copy=True, tracking=0, )
    date = fields.Datetime(string='Fecha', store=True, copy=True, tracking=0, )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Fpapyg(models.Model):
    _name = 'fpa.pyg'
    _description = 'fpa.pyg'
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha final', store=True, copy=True, tracking=0, )
    date = fields.Datetime(string='Fecha', store=True, copy=True, tracking=0, )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Fpamayorbalance(models.Model):
    _name = 'fpa.mayor.balance'
    _description = 'fpa.mayor.balance'
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha final', store=True, copy=True, tracking=0, )
    date = fields.Datetime(string='Fecha', store=True, copy=True, tracking=0, )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Fpapygcc(models.Model):
    _name = 'fpa.pyg.cc'
    _description = 'fpa.pyg.cc'
    chart_account_id = fields.Many2one(string='Plan Contable', store=True, required=True, copy=True, tracking=0,
                                       comodel_name='account.account', )
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    date_from = fields.Date(string='Fecha Inicial', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha final', store=True, copy=True, tracking=0, )
    date = fields.Datetime(string='Fecha', store=True, copy=True, tracking=0, )
    financial_id = fields.Many2one(string='Reporte', store=True, copy=True, tracking=0,
                                   comodel_name='fpa.financial.reports', )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Certificadoreportingresos(models.Model):
    _name = 'certificado.report.ingresos'
    _description = 'certificado.report.ingresos'
    city_id = fields.Many2one(string='Ciudad donde se practico', store=True, copy=True, tracking=0,
                              comodel_name='res.city', )
    company_id = fields.Many2one(string='Compania', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='res.company', )
    description = fields.Text(string='Descripcion', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    num = fields.Char(string='Numero Formulario', store=True, required=True, copy=True, tracking=0, )
    partner_id = fields.Many2one(string='Tercero', readonly=True, tracking=0, comodel_name='res.partner', )
    ref = fields.Char(string='Nit', readonly=True, tracking=0, )
    title = fields.Char(string='Titulo', store=True, required=True, copy=True, tracking=0, )


class Certificadoreportretencion(models.Model):
    _name = 'certificado.report.retencion'
    _description = 'certificado.report.retencion'
    city_id_1 = fields.Many2one(string='Ciudad donde se practico', store=True, copy=True, tracking=0,
                                comodel_name='res.city', )
    city_id_2 = fields.Many2one(string='Ciudad donde se consigno', store=True, copy=True, tracking=0,
                                comodel_name='res.city', )
    description = fields.Text(string='Notas', store=True, copy=True, tracking=0, )
    impuesto_compuesto = fields.Boolean(string='Impuesto Compuesto', store=True, copy=True, tracking=0, )
    is_ica = fields.Boolean(string='Impuesto ICA', store=True, copy=True, tracking=0, )
    is_ret_iva = fields.Boolean(string='Ret. IVA', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    title = fields.Char(string='Titulo', store=True, required=True, copy=True, tracking=0, )


class Prefacturacionwiz(models.Model):
    _name = 'prefacturacion.wiz'
    _description = 'prefacturacion.wiz'
    client_ids = fields.Many2many(relation='prefacturacionwiz_client_ids_rel', column1='prefacturacionwiz_id',
                                  column2='client_ids_id', string='Clientes', store=True, copy=True, tracking=0,
                                  comodel_name='res.partner', )
    distribuited = fields.Boolean(string='Con Distribucion', store=True, copy=True, tracking=0, )
    end_date = fields.Date(string='Hasta', store=True, copy=True, tracking=0, )
    invoice_date = fields.Date(string='Fecha de factura', store=True, copy=True, tracking=0, )
    journal_id = fields.Many2one(string='Diario', store=True, copy=True, tracking=0, comodel_name='account.journal', )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.product', )
    project_ids = fields.Many2many(relation='prefacturacionwiz_project_ids_rel', column1='prefacturacionwiz_id',
                                   column2='project_ids_id', string='Proyectos', store=True, copy=True, tracking=0,
                                   comodel_name='project.project', )
    start_date = fields.Date(string='Fecha inicio', store=True, copy=True, tracking=0, )


class Programacionmodalidadwiz(models.Model):
    _name = 'programacion.modalidad.wiz'
    _description = 'programacion.modalidad.wiz'
    cliente_contract_id = fields.Many2one(string='Contrato', store=True, required=True, copy=True, tracking=0,
                                          comodel_name='project.project', )
    company_id = fields.Many2one(string='Compañía', copy=True, tracking=0, comodel_name='res.company', )
    modalidad_id = fields.Many2one(string='Modalidad Patron', store=True, copy=True, tracking=0,
                                   comodel_name='hr.roster.modalidad', )
    parent_modality_id = fields.Many2one(string='Modalidad Padre', store=True, copy=True, tracking=0,
                                         comodel_name='hr.roster.modalidad', )
    puesto_id = fields.Many2one(string='Puesto', store=True, required=True, copy=True, tracking=0,
                                comodel_name='hr.roster.puesto', )
    use_parent_modality = fields.Boolean(string='Usa modalidad padre', readonly=True, tracking=0, )


class Variableseconomicas(models.Model):
    _name = 'variables.economicas'
    _description = 'variables.economicas'
    code = fields.Char(string='Codigo', store=True, copy=True, tracking=0, )
    currency_id = fields.Many2one(string='Moneda', store=True, required=True, copy=True, tracking=0,
                                  comodel_name='res.currency', )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class Hrpayslipconceptscode(models.Model):
    _name = 'hr.payslip.concepts.code'
    _description = 'hr.payslip.concepts.code'
    code = fields.Char(string='Código', store=True, required=True, copy=True, tracking=0, )
    column_line_id = fields.Many2one(string='Linea de Aplicación', store=True, required=True, copy=True, tracking=0,
                                     comodel_name='fpa.financial.reports.concepts.columns.lines', )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Fpafinancialreportscolumns(models.Model):
    _name = 'fpa.financial.reports.columns'
    _description = 'fpa.financial.reports.columns'
    code = fields.Char(string='Codigo concepto', store=True, copy=True, tracking=0, )


class Fpaniveles(models.Model):
    _name = 'fpa.niveles'
    _description = 'fpa.niveles'
    code = fields.Char(string='Código', store=True, required=True, copy=True, tracking=0, )
    financial_reports = fields.Many2one(string='Informe financiero', store=True, required=True, copy=True, tracking=0,
                                        comodel_name='fpa.financial.reports', )
    help = fields.Text(string='Ayuda', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Descripción', store=True, required=True, copy=True, tracking=0, )


class Hrrosterbono(models.Model):
    _name = 'hr.roster.bono'
    _description = 'hr.roster.bono'
    code = fields.Char(string='Codigo', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Descripcion', store=True, copy=True, tracking=0, )


class Fpafinancialreportsconceptscolumns(models.Model):
    _name = 'fpa.financial.reports.concepts.columns'
    _description = 'fpa.financial.reports.concepts.columns'
    code = fields.Char(string='Codigo concepto', store=True, copy=True, tracking=0, )
    financial_reports = fields.Many2one(string='Informe financiero', store=True, required=True, copy=True, tracking=0,
                                        comodel_name='fpa.financial.reports', )
    line_id = fields.Many2one(string='Concepto', store=True, copy=True, tracking=0,
                              comodel_name='fpa.financial.reports.concepts', )
    name = fields.Char(string='Concepto', store=True, required=True, copy=True, tracking=0, )


class Communicationquoter(models.Model):
    _name = 'communication.quoter'
    _description = 'communication.quoter'
    communication_id = fields.Many2one(string='Comunicacion', store=True, copy=True, tracking=0,
                                       comodel_name='quoter.communication', )
    quantity = fields.Integer(string='Cantidad', store=True, copy=True, tracking=0, )
    quoter_line_id = fields.Many2one(string='Linea de Cotizacion', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter.line', )


class Hrpayrollembargofilewizard(models.Model):
    _name = 'hr.payroll.embargo.file.wizard'
    _description = 'hr.payroll.embargo.file.wizard'
    company_id = fields.Many2one(string='Compañia', store=True, copy=True, tracking=0, comodel_name='res.company', )
    consecutive = fields.Char(string='CC', store=True, copy=True, tracking=0, )
    date_end = fields.Date(string='Fecha final', store=True, copy=True, tracking=0, )
    date_start = fields.Date(string='Fecha Inicial', store=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    employees_ids = fields.Many2many(relation='hrpayrollembargofile_employees_ids_rel',
                                     column1='hrpayrollembargofile_id', column2='employees_ids_id', string='Empleados',
                                     store=True, copy=True, tracking=0,
                                     comodel_name='hr.employee', )
    file_name = fields.Binary(string='Archivo', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre de archivo', store=True, copy=True, tracking=0, )
    payslip_period_id = fields.Many2one(string='Periodo', store=True, copy=True, tracking=0,
                                        comodel_name='hr.period', )


class Fpaexportwizardept(models.Model):
    _name = 'fpa.export.wizard.ept'
    _description = 'fpa.export.wizard.ept'
    concept_code = fields.Char(string='Codigo de concepto', store=True, copy=True, tracking=0, )
    contract_ids = fields.Many2many(relation='fpaexportwizardept_contract_ids_rel', column1='fpaexportwizardept_id',
                                    column2='contract_ids_id', string='Contratos', store=True, copy=True, tracking=0,
                                    comodel_name='hr.contract', )
    date_cut = fields.Date(string='Hasta', readonly=True, tracking=0, )
    date_from = fields.Date(string='Desde', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Hasta', store=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    export_contract = fields.Boolean(string='Contatos', store=True, copy=True, tracking=0, )
    export = fields.Boolean(string='Medios', store=True, copy=True, tracking=0, )
    is_payslip = fields.Boolean(string='Es Nomina', store=True, copy=True, tracking=0, )
    message = fields.Char(string='Message', store=True, readonly=True, copy=True, tracking=0, )
    payslip_type_id = fields.Many2one(string='Tipo de nomina', store=True, copy=True, tracking=0,
                                      comodel_name='hr.payslip.type', )
    run_id_1 = fields.Many2one(string='Lote de nomina', store=True, copy=True, tracking=0,
                               comodel_name='hr.payslip.processing', )
    workcenter = fields.Char(string='Centro de Trabajo', store=True, copy=True, tracking=0, )


class Hrrostersaledistribution(models.Model):
    _name = 'hr.roster.sale.distribution'
    _description = 'hr.roster.sale.distribution'
    concept_id = fields.Many2one(string='conceptos', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='hr.roster.sale.concept', )
    distribution = fields.Float(string='Distribucion', store=True, required=True, copy=True, tracking=0, )
    puesto_id = fields.Many2one(string='Puesto', store=True, copy=True, tracking=0, comodel_name='hr.roster.puesto', )


class Hrpayrollembargopriority(models.Model):
    _name = 'hr.payroll.embargo.priority'
    _description = 'hr.payroll.embargo.priority'
    contract_id = fields.Many2one(string='Contrato', store=True, copy=True, tracking=0, comodel_name='hr.contract', )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )


class Stockreportkardexline(models.Model):
    _name = 'stock.report.kardex.line'
    _description = 'stock.report.kardex.line'
    cost_move = fields.Float(string='Costo Unitario Movimiento', store=True, copy=True, tracking=0, )
    cost_promedio_total = fields.Float(string='Costo Valorizado', store=True, copy=True, tracking=0, )
    cost_promedio = fields.Float(string='Costo Promedio', store=True, copy=True, tracking=0, )
    cost_total_move = fields.Float(string='Costo Total Movimiento', store=True, copy=True, tracking=0, )
    date = fields.Datetime(string='Fecha', store=True, copy=True, tracking=0, )
    default_code = fields.Char(string='Referencia Interna', store=True, copy=True, tracking=0, )
    location_dest_id = fields.Char(string='Ubicacion Destino', store=True, copy=True, tracking=0, )
    location_id = fields.Char(string='Ubicacion Origen', store=True, copy=True, tracking=0, )
    move_id = fields.Many2one(string='Movimiento', store=True, copy=True, tracking=0, comodel_name='stock.move', )
    name = fields.Char(string='Documento Referencia', store=True, copy=True, tracking=0, )
    origin = fields.Char(string='Documento Origen', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.product', )
    product_name = fields.Char(string='Descripcion', store=True, copy=True, tracking=0, )
    qty_end = fields.Float(string='Saldo Final', store=True, copy=True, tracking=0, )
    qty_in = fields.Float(string='Entrada', store=True, copy=True, tracking=0, )
    qty_out = fields.Float(string='Salida', store=True, copy=True, tracking=0, )
    qty_start = fields.Float(string='Saldo Inicial', store=True, copy=True, tracking=0, )
    qty = fields.Float(string='Interno', store=True, copy=True, tracking=0, )
    type_move = fields.Char(string='Tipo de movimiento', store=True, copy=True, tracking=0, )


class Cierrenominawiz(models.Model):
    _name = 'cierre.nomina.wiz'
    _description = 'cierre.nomina.wiz'
    create_tarifario = fields.Boolean(string='Crear Tarifario', store=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    employees_ids = fields.Many2many(relation='cierrenominawiz_employees_ids_rel', column1='cierrenominawiz_id',
                                     column2='employees_ids_id', string='Empleados', store=True, copy=True, tracking=0,
                                     comodel_name='hr.employee', )
    fecha_cierre = fields.Date(string='Fecha de cierre', store=True, required=True, copy=True, tracking=0, )
    group_id = fields.Many2one(string='Grupo de contrato', store=True, copy=True, tracking=0,
                               comodel_name='hr.contract.group', )
    novelty_type_id = fields.Many2one(string='Categoria de novedad', store=True, copy=True, tracking=0,
                                      comodel_name='hr.novelty.type', )
    periodo_de_adicionales = fields.Many2one(string='Período de adicionales', store=True, copy=True, tracking=0,
                                             comodel_name='hr.period', )
    periodo = fields.Many2one(string='Periodo', store=True, required=True, copy=True, tracking=0,
                              comodel_name='hr.period', )
    politica_solo_adicionales = fields.Boolean(string='Politica solo adicionales', store=True, copy=True,
                                               tracking=0, )
    solo_adicionales = fields.Boolean(string='Cerrar solo adicionales?', store=True, copy=True, tracking=0, )


class Hrcontractreport(models.Model):
    _name = 'hr.contract.report'
    _description = 'hr.contract.report'
    currency_id = fields.Many2one(string='Currency', store=True, copy=True, tracking=0, comodel_name='res.currency', )
    name = fields.Char(string='Name', store=True, copy=True, tracking=0, )
    wage = fields.Monetary(string='Salario', store=True, copy=True, tracking=0, )


class Returnchangedifference(models.Model):
    _name = 'return.change.difference'
    _description = 'return.change.difference'
    date = fields.Date(string='Fecha de Contablización', store=True, copy=True, tracking=0, )
    difference_id = fields.Many2one(string='Diferencia en Cambio', store=True, copy=True, tracking=0,
                                    comodel_name='change.difference', )
    journal_id = fields.Many2one(string='Diario', store=True, copy=True, tracking=0, comodel_name='account.journal', )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_channel_ids = fields.Many2many(relation='returnchangedifferen_message_channel_ids_rel',
                                           column1='returnchangedifferen_id', column2='message_channel_ids_id',
                                           string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_partner_ids = fields.Many2many(relation='returnchangedifferen_message_partner_ids_rel',
                                           column1='returnchangedifferen_id', column2='message_partner_ids_id',
                                           string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    move_id = fields.Many2one(string='Asiento Contable', store=True, copy=True, tracking=0,
                              comodel_name='account.move', )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class Hrpayrollembargohistory(models.Model):
    _name = 'hr.payroll.embargo.history'
    _description = 'hr.payroll.embargo.history'
    date = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )
    history_embargo_id = fields.Many2one(string='History Embargo', store=True, copy=True, tracking=0,
                                         comodel_name='hr.payroll.embargo', )
    reason = fields.Text(string='Motivo de devolución', store=True, copy=True, tracking=0, )
    state = fields.Char(string='Estado', store=True, tracking=0, )


class Hrpayrollembargohistorywizard(models.Model):
    _name = 'hr.payroll.embargo.history.wizard'
    _description = 'hr.payroll.embargo.history.wizard'
    date = fields.Date(string='Fecha', store=True, copy=True, tracking=0, )
    reason = fields.Text(string='Motivo de cierre', store=True, copy=True, tracking=0, )


class Studioapprovaldetails(models.Model):
    _name = 'studio.approval.details'
    _description = 'studio.approval.details'
    date_accepted = fields.Datetime(string='Date Accepted', store=True, copy=True, tracking=0, )
    model_id = fields.Many2one('ir.model', string='Modelo', required=True, index=True, ondelete='cascade', )
    res_id = fields.Integer(string='Record Id', store=True, copy=True, tracking=0, )
    rule_id = fields.Many2one(string='Rule', store=True, copy=True, tracking=0, comodel_name='studio.approval.rule', )
    user_accepted = fields.Many2one(string='User Accepted', store=True, copy=True, tracking=0,
                                    comodel_name='res.users', )


class Certificadoreportretencionperiodicidad(models.Model):
    _name = 'certificado.report.retencion.periodicidad'
    _description = 'certificado.report.retencion.periodicidad'
    date_end = fields.Date(string='Hasta', store=True, required=True, copy=True, tracking=0, )
    date_start = fields.Date(string='Desde', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Stockreportkardexdotwizard(models.Model):
    _name = 'stock.report.kardex.dot.wizard'
    _description = 'stock.report.kardex.dot.wizard'
    date_end = fields.Datetime(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    date_start = fields.Datetime(string='Fecha Inicial', store=True, required=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    employee_ids = fields.Many2many(relation='stockreportkardexdot_employee_ids_rel', column1='stockreportkardexdot_id',
                                    column2='employee_ids_id', string='Empleados', store=True, copy=True, tracking=0,
                                    comodel_name='hr.employee', )
    employees = fields.Boolean(string='Varios Empleados', store=True, copy=True, tracking=0, )
    group_kardex_dot_location_ids = fields.Many2one(string='Ubicaciones', store=True, copy=True, tracking=0,
                                                    comodel_name='stock.report.sql.group.location', )
    location_id = fields.Many2one(string='Ubicacion', store=True, copy=True, tracking=0,
                                  comodel_name='stock.location', )
    warehouse_id = fields.Many2one(string='Bodega', store=True, copy=True, tracking=0,
                                   comodel_name='stock.warehouse', )


class Remplazonovedadwiz(models.Model):
    _name = 'remplazo.novedad.wiz'
    _description = 'remplazo.novedad.wiz'
    date_end = fields.Date(string='Fecha Fin', store=True, copy=True, tracking=0, )
    date_from = fields.Date(string='Fecha Inicio', store=True, copy=True, tracking=0, )
    day_from = fields.Integer(string='Dia desde', store=True, required=True, copy=True, tracking=0, )
    day_to = fields.Integer(string='Dia hasta', store=True, required=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    hour_restriction = fields.Boolean(string='Restriccion por horas', store=True, copy=True, tracking=0, )
    no_aditional = fields.Boolean(string='No adicional', store=True, copy=True, tracking=0, )
    novelty_support_file = fields.Binary(string='Soporte de novedad', store=True, copy=True, tracking=0, )
    observaciones = fields.Char(string='Observaciones', store=True, copy=True, tracking=0, )
    permanent = fields.Boolean(string='Novedad permanente', store=True, copy=True, tracking=0, )
    politica_adicional = fields.Boolean(string='Política adicional', readonly=True, tracking=0, )
    programacion_linea_temp_id = fields.Many2many(relation='remplazonovedadwiz_programacion_linea_t_rel',
                                                  column1='remplazonovedadwiz_id', column2='programacion_linea_t_id',
                                                  string='Lineas Programacion', store=True, copy=True, tracking=0,
                                                  comodel_name='hr.roster.programacion.line', )
    time_from = fields.Char(string='Hora desde', store=True, copy=True, tracking=0, )
    time_to = fields.Char(string='Hora hasta', store=True, copy=True, tracking=0, )
    type_id = fields.Many2one(string='Causa del remplazo', store=True, required=True, copy=True, tracking=0,
                              comodel_name='hr.leave.type', )
    type_name = fields.Char(string='Nombre', readonly=True, tracking=0, )
    yes_aditional = fields.Boolean(string='Si adicional', store=True, copy=True, tracking=0, )


class Stockreportkardexwizard(models.Model):
    _name = 'stock.report.kardex.wizard'
    _description = 'stock.report.kardex.wizard'
    date_end = fields.Datetime(string='Fecha Final', store=True, required=True, copy=True, tracking=0, )
    date_start = fields.Datetime(string='Fecha Inicial', store=True, required=True, copy=True, tracking=0, )
    location_ids = fields.Many2many(relation='stockreportkardexwiz_location_ids_rel', column1='stockreportkardexwiz_id',
                                    column2='location_ids_id', string='Ubicaciones', store=True, copy=True, tracking=0,
                                    comodel_name='stock.location', )
    product_ids = fields.Many2many(relation='stockreportkardexwiz_product_ids_rel', column1='stockreportkardexwiz_id',
                                   column2='product_ids_id', string='Productos', store=True, copy=True, tracking=0,
                                   comodel_name='product.product', )
    title = fields.Char(string='titulos', store=True, copy=True, tracking=0, )


class Remplazonovedadwizmasive(models.Model):
    _name = 'remplazo.novedad.wiz.masive'
    _description = 'remplazo.novedad.wiz.masive'
    date_end = fields.Date(string='Fecha Fin', store=True, copy=True, tracking=0, )
    date_from = fields.Date(string='Fecha Inicio', store=True, copy=True, tracking=0, )
    day_from = fields.Integer(string='Dia desde', store=True, required=True, copy=True, tracking=0, )
    day_to = fields.Integer(string='Dia hasta', store=True, required=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    hour_restriction = fields.Boolean(string='Restriccion por horas', store=True, copy=True, tracking=0, )
    novelty_support_file = fields.Binary(string='Soporte de novedad', store=True, copy=True, tracking=0, )
    permanent = fields.Boolean(string='Novedad permanente', store=True, copy=True, tracking=0, )
    programacion_linea_temp_id = fields.Many2many(relation='remplazonovedadwizma_programacion_linea_t_rel',
                                                  column1='remplazonovedadwizma_id', column2='programacion_linea_t_id',
                                                  string='Lineas Programacion', store=True, copy=True, tracking=0,
                                                  comodel_name='hr.roster.programacion.line', )
    time_from = fields.Char(string='Hora desde', store=True, copy=True, tracking=0, )
    time_to = fields.Char(string='Hora hasta', store=True, copy=True, tracking=0, )
    type_id = fields.Many2one(string='Causa del remplazo', store=True, required=True, copy=True, tracking=0,
                              comodel_name='hr.leave.type', )
    type_name = fields.Char(string='Nombre', readonly=True, tracking=0, )


class Variableseconomicasline(models.Model):
    _name = 'variables.economicas.line'
    _description = 'variables.economicas.line'
    date_from = fields.Datetime(string='Fecha desde', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Datetime(string='Fecha hasta', store=True, required=True, copy=True, tracking=0, )
    valor = fields.Float(string='Valor', store=True, required=True, copy=True, tracking=0, )
    variable_id = fields.Many2one(string='Variable', store=True, copy=True, tracking=0,
                                  comodel_name='variables.economicas', )


class Hrpayrolladvancewizard(models.Model):
    _name = 'hr.payroll.advance.wizard'
    _description = 'hr.payroll.advance.wizard'
    date_from = fields.Date(string='Fecha inicio', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha fin', store=True, required=True, copy=True, tracking=0, )


class Reportaccountbibudgetwizard(models.Model):
    _name = 'report.account.bi.budget.wizard'
    _description = 'report.account.bi.budget.wizard'
    date_from = fields.Date(string='Fecha Desde', store=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Fecha Hasta', store=True, copy=True, tracking=0, )


class Fpafinancialreportsperiod(models.Model):
    _name = 'fpa.financial.reports.period'
    _description = 'fpa.financial.reports.period'
    date_from = fields.Date(string='Desde', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Date(string='Hasta', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Etiqueta', store=True, required=True, copy=True, tracking=0, )
    range_ids = fields.Many2many(
        'fpa.financial.reports.period.range',
        relation='fpa_frp_frpr_rel',  # nombre corto para evitar overflow en PostgreSQL
        column1='period_id',
        column2='range_id',
        string='Rangos',
        copy=False,
    )


class Variableseconomicasretefuente(models.Model):
    _name = 'variables.economicas.retefuente'
    _description = 'variables.economicas.retefuente'
    date_from = fields.Datetime(string='Fecha desde', store=True, required=True, copy=True, tracking=0, )
    date_to = fields.Datetime(string='Fecha hasta', store=True, required=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class Facturacionwiz(models.Model):
    _name = 'facturacion.wiz'
    _description = 'facturacion.wiz'
    date_invoice = fields.Date(string='Fecha de facturacion', store=True, required=True, copy=True, tracking=0, )
    detalle = fields.Boolean(string='Detallado', store=True, copy=True, tracking=0, )
    product_id = fields.Many2one(string='Product', store=True, copy=True, tracking=0,
                                 comodel_name='product.product', )


class Accountsuppierpaymentwizard(models.Model):
    _name = 'account.suppier.payment.wizard'
    _description = 'account.suppier.payment.wizard'
    date_order = fields.Datetime(string='Order Date', store=True, required=True, copy=True, tracking=0, )
    file_text = fields.Binary(string='Archivo Pago Banco', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Archivo Pago Banco', store=True, copy=True, tracking=0, )


class Incomerecordsline(models.Model):
    _name = 'income.records.line'
    _description = 'income.records.line'
    date_scheduled = fields.Datetime(string='Fecha Prevista', store=True, copy=True, tracking=0, )
    employee_id = fields.Many2one(string='Employee', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    horario = fields.Char(string='Horario', store=True, copy=True, tracking=0, )
    justification_id = fields.Many2one(string='Justificación Hora Extra', store=True, copy=True, tracking=0,
                                       comodel_name='overtime.justification', )
    modality = fields.Many2one(string='Modality', store=True, copy=True, tracking=0,
                               comodel_name='hr.roster.modalidad', )
    ot_number = fields.Char(string='Numero OT', store=True, copy=True, tracking=0, )
    overtime_id = fields.Many2one(string='Hora Extra', store=True, copy=True, tracking=0,
                                  comodel_name='hr.overtime', )
    part = fields.Char(string='Parte', store=True, copy=True, tracking=0, )
    puesto_id = fields.Many2one(string='Puesto', store=True, copy=True, tracking=0, comodel_name='hr.roster.puesto', )
    time_dif = fields.Float(string='Diferencia', readonly=True, tracking=0, )
    time = fields.Float(string='Registro Hora', store=True, copy=True, tracking=0, )
    turno_id = fields.Many2one(string='Turno', store=True, copy=True, tracking=0, comodel_name='hr.roster.turno', )
    wiz_id = fields.Many2one(string='Wizard', store=True, copy=True, tracking=0, comodel_name='income.records', )


class Orderquoterlinedetail(models.Model):
    _name = 'order.quoter.line.detail'
    _description = 'order.quoter.line.detail'
    day = fields.Many2one(string='Dias de la semana', store=True, copy=True, tracking=0, comodel_name='res.weekday', )
    dummy_days = fields.Char(string='Dias calendario', store=True, copy=True, tracking=0, )
    hd_exe = fields.Float(string='Horas diurnas prestadas', store=True, copy=True, tracking=0, )
    hd = fields.Float(string='Horas diurnas', store=True, copy=True, tracking=0, )
    hn_exe = fields.Float(string='Horas nocturnas prestadas', store=True, copy=True, tracking=0, )
    hn = fields.Float(string='Horas nocturnas', store=True, copy=True, tracking=0, )
    order_line_id = fields.Many2one(string='Orden de servicio', store=True, copy=True, tracking=0,
                                    comodel_name='sale.quoter.line', )
    prefestivo = fields.Boolean(string='Prefestivo', store=True, copy=True, tracking=0, )
    repetition = fields.Integer(string='Repeticiones', store=True, copy=True, tracking=0, )
    rest_in = fields.Char(string='Salida a descanso', store=True, copy=True, tracking=0, )
    rest_out = fields.Char(string='Entrada de descanso', store=True, copy=True, tracking=0, )
    time_in = fields.Char(string='Hora de entrada', store=True, copy=True, tracking=0, )
    time_out = fields.Char(string='Hora de salida', store=True, copy=True, tracking=0, )


class Orderlinedetail(models.Model):
    _name = 'order.line.detail'
    _description = 'order.line.detail'
    day = fields.Many2one(string='Dias de la semana', store=True, copy=True, tracking=0, comodel_name='res.weekday', )
    dummy_days = fields.Char(string='Dias calendario', store=True, copy=True, tracking=0, )
    hd_exe = fields.Float(string='Horas diurnas prestadas', store=True, copy=True, tracking=0, )
    hd = fields.Float(string='Horas diurnas', store=True, copy=True, tracking=0, )
    hn_exe = fields.Float(string='Horas nocturnas prestadas', store=True, copy=True, tracking=0, )
    hn = fields.Float(string='Horas nocturnas', store=True, copy=True, tracking=0, )
    order_line_id = fields.Many2one(string='Orden de servicio', store=True, copy=True, tracking=0,
                                    comodel_name='project.service.order.line', )
    prefestivo = fields.Boolean(string='Prefestivo', store=True, copy=True, tracking=0, )
    repetition = fields.Integer(string='Repeticiones', store=True, copy=True, tracking=0, )
    rest_in = fields.Char(string='Salida a descanso', store=True, copy=True, tracking=0, )
    rest_out = fields.Char(string='Entrada de descanso', store=True, copy=True, tracking=0, )
    time_in = fields.Char(string='Hora de entrada', store=True, copy=True, tracking=0, )
    time_out = fields.Char(string='Hora de salida', store=True, copy=True, tracking=0, )


class Hrinductions(models.Model):
    _name = 'hr.inductions'
    _description = 'hr.inductions'
    days = fields.Integer(string='Dias de induccion', store=True, required=True, copy=True, tracking=0, )
    sol_id = fields.Many2one(string='Linea de servicio', store=True, copy=True, tracking=0,
                             comodel_name='project.service.order.line', )


class Hrrosterrest(models.Model):
    _name = 'hr.roster.rest'
    _description = 'hr.roster.rest'
    days = fields.Integer(string='Dias Descanso', store=True, copy=True, tracking=0, )
    modalidad_id = fields.Many2one(string='Modalidad', store=True, copy=True, tracking=0,
                                   comodel_name='hr.roster.modalidad', )
    name = fields.Char(string='Nombre', readonly=True, required=True, tracking=0, )


class Hrpayrollembargotype(models.Model):
    _name = 'hr.payroll.embargo.type'
    _description = 'hr.payroll.embargo.type'
    description = fields.Text(string='Descripcion', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class Prefacturacionwizdirect(models.Model):
    _name = 'prefacturacion.wiz.direct'
    _description = 'prefacturacion.wiz.direct'
    distribuited = fields.Boolean(string='Con Distribucion', store=True, copy=True, tracking=0, )
    end_date = fields.Date(string='Hasta', store=True, copy=True, tracking=0, )
    invoice_date = fields.Date(string='Fecha de factura', store=True, copy=True, tracking=0, )
    journal_id = fields.Many2one(string='Diario', store=True, copy=True, tracking=0, comodel_name='account.journal', )
    order_id = fields.Many2many(relation='prefacturacionwizdir_order_id_rel', column1='prefacturacionwizdir_id',
                                column2='order_id_id', string='Orden de servicio', store=True, copy=True, tracking=0,
                                comodel_name='project.service.order', )
    product_id = fields.Many2one(string='Producto', store=True, copy=True, tracking=0,
                                 comodel_name='product.product', )
    start_date = fields.Date(string='Fecha inicio', store=True, copy=True, tracking=0, )


class Hrrosterconceptdistribution(models.Model):
    _name = 'hr.roster.concept.distribution'
    _description = 'hr.roster.concept.distribution'
    distribution = fields.Float(string='Distribucion', store=True, copy=True, tracking=0, )
    modalidad_id = fields.Many2one(string='Modalidad', store=True, copy=True, tracking=0,
                                   comodel_name='hr.roster.modalidad', )
    overtime_type_id = fields.Many2one(string='Tipo Horas Extra', store=True, copy=True, tracking=0,
                                       comodel_name='hr.overtime.type', )
    puesto_id = fields.Many2one(string='Puesto', store=True, copy=True, tracking=0, comodel_name='hr.roster.puesto', )


class Hrpayslipembargoline(models.Model):
    _name = 'hr.payslip.embargo.line'
    _description = 'hr.payslip.embargo.line'
    embargo_amount = fields.Float(string='Valor', store=True, copy=True, tracking=0, )
    embargo_due = fields.Float(string='Cuota', store=True, copy=True, tracking=0, )
    embargo_id = fields.Many2one(string='Embargo', store=True, copy=True, tracking=0,
                                 comodel_name='hr.payroll.embargo', )
    embargo_line_id = fields.Many2one(string='Linea', store=True, copy=True, tracking=0,
                                      comodel_name='hr.payroll.embargo.line', )
    embargo_payslip_id = fields.Many2one(string='Embargo Payslip', store=True, copy=True, tracking=0,
                                         comodel_name='hr.payslip', )
    payslip_id = fields.Many2one(string='Nomina', store=True, copy=True, tracking=0, comodel_name='hr.payslip', )
    type_embargo = fields.Many2one(string='Tipo', store=True, copy=True, tracking=0,
                                   comodel_name='hr.payroll.embargo.type', )


class Hrpayrollembargoextra(models.Model):
    _name = 'hr.payroll.embargo.extra'
    _description = 'hr.payroll.embargo.extra'
    embargo_concept_id = fields.Many2one(string='Embargo Concept', store=True, copy=True, tracking=0,
                                         comodel_name='hr.payroll.embargo', )


class Hrpayrollembargolineextra(models.Model):
    _name = 'hr.payroll.embargo.line.extra'
    _description = 'hr.payroll.embargo.line.extra'
    embargo_id = fields.Many2one(string='Embargo', store=True, copy=True, tracking=0,
                                 comodel_name='hr.payroll.embargo', )
    extra_value = fields.Float(string='Valor extra', store=True, copy=True, tracking=0, )
    payslip_period_id = fields.Many2one(string='Periodo', store=True, copy=True, tracking=0,
                                        comodel_name='hr.period', )


class Hrrosterreverseclose(models.Model):
    _name = 'hr.roster.reverse.close'
    _description = 'hr.roster.reverse.close'
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    employees_ids = fields.Many2many(relation='hrrosterreverseclose_employees_ids_rel',
                                     column1='hrrosterreverseclose_id', column2='employees_ids_id', string='Empleados',
                                     store=True, copy=True, tracking=0,
                                     comodel_name='hr.employee', )
    group_id = fields.Many2one(string='Grupo de contrato', store=True, copy=True, tracking=0,
                               comodel_name='hr.contract.group', )
    period_id = fields.Many2one(string='Periodo', store=True, required=True, copy=True, tracking=0,
                                comodel_name='hr.period', )
    reverse_tarifario = fields.Boolean(string='Revertir Tarifarios?', store=True, copy=True, tracking=0, )
    revertir_solo_adicionales = fields.Boolean(string='Revertir solo adicionales?', store=True, copy=True,
                                               tracking=0, )


class Hrrosterdisponibles(models.Model):
    _name = 'hr.roster.disponibles'
    _description = 'hr.roster.disponibles'
    employee_id = fields.Many2one(string='Empleado', store=True, copy=True, tracking=0, comodel_name='hr.employee', )
    user_id = fields.Many2one(string='Usuario', store=True, copy=True, tracking=0, comodel_name='res.users', )


class Tarifariowiz(models.Model):
    _name = 'tarifario.wiz'
    _description = 'tarifario.wiz'
    employees_ids = fields.Many2many(relation='tarifariowiz_employees_ids_rel', column1='tarifariowiz_id',
                                     column2='employees_ids_id', string='Empleados', store=True, copy=True, tracking=0,
                                     comodel_name='hr.employee', )
    fecha_cierre = fields.Date(string='Fecha de cierre', store=True, required=True, copy=True, tracking=0, )
    from_close = fields.Boolean(string='Creado desde Cierre', store=True, copy=True, tracking=0, )
    group_id = fields.Many2one(string='Grupo de contrato', store=True, copy=True, tracking=0,
                               comodel_name='hr.contract.group', )
    novelty_type_id = fields.Many2one(string='Categoria de novedad', store=True, required=True, copy=True, tracking=0,
                                      comodel_name='hr.novelty.type', )
    periodo = fields.Many2one(string='Periodo', store=True, required=True, copy=True, tracking=0,
                              comodel_name='hr.period', )
    proyecto_ids = fields.Many2many(relation='tarifariowiz_proyecto_ids_rel', column1='tarifariowiz_id',
                                    column2='proyecto_ids_id', string='Proyectos', store=True, copy=True, tracking=0,
                                    comodel_name='project.project', )


class Accountmoveprojectorderline(models.Model):
    _name = 'account.move.project.order.line'
    _description = 'account.move.project.order.line'
    end_date = fields.Date(string='Fecha fin de facturación', store=True, readonly=True, required=True, copy=True,
                           tracking=0, )
    invoice_date = fields.Date(string='Fecha de factura', index=True, store=True, readonly=True, tracking=0, )
    journal_id = fields.Many2one(string='Diario', index=True, store=True, readonly=True, tracking=0,
                                 comodel_name='account.journal', )
    move_id = fields.Many2one(string='Factura', index=True, store=True, readonly=True, tracking=0,
                              comodel_name='account.move', )
    move_line_id = fields.Many2one(string='Linea de Factura', index=True, store=True, readonly=True, required=True,
                                   copy=True, tracking=0, comodel_name='account.move.line', )
    order_id = fields.Many2one(string='Orden', index=True, store=True, readonly=True, tracking=0,
                               comodel_name='project.service.order', )
    order_line_id = fields.Many2one(string='Linea de orden de servicio', index=True, store=True, readonly=True,
                                    required=True, copy=True, tracking=0, comodel_name='project.service.order.line', )
    project_id = fields.Many2one(string='Proyecto', index=True, store=True, readonly=True, tracking=0,
                                 comodel_name='project.project', )
    puesto_id = fields.Many2one(string='Puesto', index=True, store=True, readonly=True, tracking=0,
                                comodel_name='hr.roster.puesto', )
    start_date = fields.Date(string='Fecha inicio de facturación', store=True, readonly=True, required=True,
                             copy=True,
                             tracking=0, )


class Searchavailableemployee(models.Model):
    _name = 'search.available.employee'
    _description = 'search.available.employee'
    end_date = fields.Datetime(string='Fecha fin', store=True, required=True, copy=True, tracking=0, )
    start_date = fields.Datetime(string='Fecha inicio', store=True, required=True, copy=True, tracking=0, )


class Hrrosterpuestotarifaadicional(models.Model):
    _name = 'hr.roster.puesto.tarifa.adicional'
    _description = 'hr.roster.puesto.tarifa.adicional'
    end_date = fields.Date(string='Fin', store=True, required=True, copy=True, tracking=0, )
    puesto_id = fields.Many2one(string='Puesto', store=True, required=True, copy=True, tracking=0,
                                comodel_name='hr.roster.puesto', )
    rate_add_df = fields.Float(string='Tarifa Turno Adicional Diurno Dominical y Festivo', store=True, copy=True,
                               tracking=0, )
    rate_add_noc = fields.Float(string='Tarifa Turno Adicional Nocturno', store=True, copy=True, tracking=0, )
    rate_add_ord = fields.Float(string='Tarifa Turno Adicional Diurno Ordinario', store=True, copy=True, tracking=0, )
    rate_adn_df = fields.Float(string='Tarifa Turno Adicional Nocturno Dominical y Festivo', store=True, copy=True,
                               tracking=0, )
    start_date = fields.Date(string='Inicio', store=True, required=True, copy=True, tracking=0, )


class Quotertransport(models.Model):
    _name = 'quoter.transport'
    _description = 'quoter.transport'
    field_name_id = fields.Many2one(string='field_name', store=True, copy=True, tracking=0, comodel_name='_unknown', )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    project_service_type_ids = fields.Many2many(relation='quotertransport_project_service_type_rel',
                                                column1='quotertransport_id', column2='project_service_type_id',
                                                string='Tipo de servicio', store=True, copy=True, tracking=0,
                                                comodel_name='project.service.type', )


class Addfrominvoiceitems(models.Model):
    _name = 'add.from.invoice.items'
    _description = 'add.from.invoice.items'
    from_invoice_id = fields.Many2one(string='Factura', store=True, required=True, copy=True, tracking=0,
                                      comodel_name='account.move', )
    invoice_id = fields.Many2one(string='Factura', store=True, copy=True, tracking=0, comodel_name='account.move', )


class Hrrostersequence(models.Model):
    _name = 'hr.roster.sequence'
    _description = 'hr.roster.sequence'
    horario_id = fields.Many2one(string='Horario', store=True, copy=True, tracking=0,
                                 comodel_name='hr.roster.horario', )
    modalidad_id = fields.Many2one(string='Modalidad', store=True, copy=True, tracking=0,
                                   comodel_name='hr.roster.modalidad', )
    modalidad2_id = fields.Many2one(string='Modalidad2', store=True, copy=True, tracking=0,
                                    comodel_name='hr.roster.modalidad', )
    sequence = fields.Integer(string='Secuencia', store=True, copy=True, tracking=0, )


class Addinvoiceitems(models.Model):
    _name = 'add.invoice.items'
    _description = 'add.invoice.items'
    invoice_id = fields.Many2one(string='Factura', store=True, copy=True, tracking=0, comodel_name='account.move', )
    items_to_invoice_allow_ids = fields.Many2many(
        relation='add_inv_items_to_invoice_allow_rel',
        column1='wiz_id',
        column2='item_id',
        string='Ítems permitidos para facturar',
        copy=False,
    )
    items_to_invoice = fields.Many2many(
        relation='add_inv_items_to_invoice_rel',
        column1='wiz_id',
        column2='item_id',
        string='Ítems a facturar',
        copy=False,
    )
    partner_ids = fields.Many2many(relation='addinvoiceitems_partner_ids_rel', column1='addinvoiceitems_id',
                                   column2='partner_ids_id', string='Clientes', store=True, copy=True, tracking=0,
                                   comodel_name='res.partner', )


class Hrprogramationleaves(models.Model):
    _name = 'hr.programation.leaves'
    _description = 'hr.programation.leaves'
    leaves_ids = fields.Many2many(relation='hrprogramationleaves_leaves_ids_rel', column1='hrprogramationleaves_id',
                                  column2='leaves_ids_id', string='Leaves', store=True, copy=True, tracking=0,
                                  comodel_name='hr.leave', )
    programacion_id = fields.Many2one(string='Programación', store=True, copy=True, tracking=0,
                                      comodel_name='hr.roster.programacion', )


class Computeinvoiceitems(models.Model):
    _name = 'compute.invoice.items'
    _description = 'compute.invoice.items'
    limit_date = fields.Date(string='Fecha corte', store=True, required=True, copy=True, tracking=0, )
    order_line_ids = fields.Many2many(relation='computeinvoiceitems_order_line_ids_rel',
                                      column1='computeinvoiceitems_id', column2='order_line_ids_id',
                                      string='Order Lines', store=True, copy=True, tracking=0,
                                      comodel_name='project.service.order.line', )


class Hrrostercambioturno(models.Model):
    _name = 'hr.roster.cambio.turno'
    _description = 'hr.roster.cambio.turno'
    linea_id = fields.Many2one(string='Linea de programacion', store=True, copy=True, tracking=0,
                               comodel_name='hr.roster.programacion.line', )


class Stockreportsqlgrouplocation(models.Model):
    _name = 'stock.report.sql.group.location'
    _description = 'stock.report.sql.group.location'
    location_ids = fields.Many2many(relation='stockreportsqlgroupl_location_ids_rel', column1='stockreportsqlgroupl_id',
                                    column2='location_ids_id', string='Ubicaciones', store=True, required=True,
                                    copy=True, tracking=0,
                                    comodel_name='stock.location', )
    name = fields.Char(string='Name', store=True, required=True, copy=True, tracking=0, )


class Studiobutton(models.Model):
    _name = 'studio.button'
    _description = 'studio.button'
    model_id = fields.Many2one('ir.model', string='Modelo', required=True, index=True, ondelete='cascade', )
    name = fields.Char(string='Button Id', store=True, copy=True, tracking=0, )


class Quotervehicle(models.Model):
    _name = 'quoter.vehicle'
    _description = 'quoter.vehicle'
    monthly_value = fields.Float(string='Valor Mensual', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    quoter_line_id = fields.Many2one(string='linea de cotizador', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter.line', )


class Quoterfreelance(models.Model):
    _name = 'quoter.freelance'
    _description = 'quoter.freelance'
    monthly_value = fields.Float(string='Valor Mensual', store=True, copy=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    quoter_line_id = fields.Many2one(string='linea de cotizador', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter.line', )


class Projectserviceorderlineitemcancel(models.Model):
    _name = 'project.service.order.line.item.cancel'
    _description = 'project.service.order.line.item.cancel'
    name = fields.Char(string='Motivo de cancelación', store=True, copy=True, tracking=0, )


class Quotersegment(models.Model):
    _name = 'quoter.segment'
    _description = 'quoter.segment'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )


class FpafinancialreportsperiodRange(models.Model):
    _name = 'fpa.financial.reports.period.range'
    _description = 'fpa.financial.reports.period_range'
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    period_ids = fields.Many2many(
        'fpa.financial.reports.period',
        relation='fpa_frp_frpr_rel',  # mismo nombre de tabla rel
        column1='range_id',
        column2='period_id',
        string='Rango de Periodos',
        copy=False,
    )


class Quotercanine(models.Model):
    _name = 'quoter.canine'
    _description = 'quoter.canine'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    total_price_lines = fields.Float(string='Total', readonly=True, tracking=0, )


class Serviceorderlinesecuence(models.Model):
    _name = 'service.order.line.secuence'
    _description = 'service.order.line.secuence'
    name = fields.Many2one(string='Secuencia', store=True, copy=True, tracking=0, comodel_name='hr.roster.horario', )
    secuence = fields.Integer(string='secuencia', store=True, copy=True, tracking=0, )
    sol_id = fields.Many2one(string='Sol', store=True, copy=True, tracking=0,
                             comodel_name='project.service.order.line', )


class Quoterweapontype(models.Model):
    _name = 'quoter.weapon.type'
    _description = 'quoter.weapon.type'
    name = fields.Char(string='Nombre', store=True, copy=True, tracking=0, )
    total_price_lines = fields.Float(string='Total', readonly=True, tracking=0, )


class Hremployeecredentialsline(models.Model):
    _name = 'hr.employee.credentials.line'
    _description = 'hr.employee.credentials.line'
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Hrepscode(models.Model):
    _name = 'hr.eps.code'
    _description = 'hr.eps.code'
    name = fields.Char(string='Name', store=True, required=True, copy=True, tracking=0, )


class Hremployeeaccreditationline(models.Model):
    _name = 'hr.employee.accreditation.line'
    _description = 'hr.employee.accreditation.line'
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Hrrostersaleconcept(models.Model):
    _name = 'hr.roster.sale.concept'
    _description = 'hr.roster.sale.concept'
    name = fields.Char(string='Concepto', store=True, required=True, copy=True, tracking=0, )
    project_id = fields.Many2one(string='Proyecto', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='project.project', )


class Projectdistribution(models.Model):
    _name = 'project.distribution'
    _description = 'project.distribution'
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )
    x_partner_id = fields.Many2one(string='Cliente', store=True, copy=True, tracking=1, comodel_name='res.partner', )


class Accountcommercial(models.Model):
    _name = 'account.commercial'
    _description = 'account.commercial'
    name = fields.Char(string='Nombre', store=True, required=True, copy=True, tracking=0, )


class Hrrosteradicionales(models.Model):
    _name = 'hr.roster.adicionales'
    _description = 'hr.roster.adicionales'
    order_line_id = fields.Many2one(string='Orden de servicio', store=True, copy=True, tracking=0,
                                    comodel_name='project.service.order.line', )
    puesto_id = fields.Many2one(string='Puesto', store=True, copy=True, tracking=0, comodel_name='hr.roster.puesto', )


class Programationlinewiz(models.Model):
    _name = 'programation.line.wiz'
    _description = 'programation.line.wiz'
    programation_ids = fields.Many2many(relation='programationlinewiz_programation_ids_rel',
                                        column1='programationlinewiz_id', column2='programation_ids_id',
                                        string='Programaciones', store=True, readonly=True, tracking=0,
                                        comodel_name='hr.roster.programacion', )
    year = fields.Integer(string='Año', store=True, copy=True, tracking=0, )


class Wizardprojectserviceorderline(models.Model):
    _name = 'wizard.project.service.order.line'
    _description = 'wizard.project.service.order.line'
    project_id = fields.Many2one(string='Proyecto', store=True, required=True, copy=True, tracking=0,
                                 comodel_name='project.project', )


class Quoterpositionservice(models.Model):
    _name = 'quoter.position.service'
    _description = 'quoter.position.service'
    quoter_line_id = fields.Many2one(string='Linea de Servicio', store=True, copy=True, tracking=0,
                                     comodel_name='sale.quoter.line', )
    quoter_position_id = fields.Many2one(string='Puestos', store=True, copy=True, tracking=0,
                                         comodel_name='quoter.position', )
    service_number = fields.Integer(string='Numero de servicio', store=True, copy=True, tracking=0, )


class Replicarprogramacionwiz(models.Model):
    _name = 'replicar.programacion.wiz'
    _description = 'replicar.programacion.wiz'
    repeticiones = fields.Integer(string='Repeticiones', store=True, copy=True, tracking=0, )


class Reportcenter(models.Model):
    _name = 'report.center'
    _description = 'report.center'
    report_id = fields.Many2one(string='Report Id', store=True, copy=True, tracking=0,
                                comodel_name='ir.actions.report', )
    view_id = fields.Many2one(string='View id', store=True, copy=True, tracking=0, comodel_name='ir.ui.view', )
    xml = fields.Text(string='Xml', store=True, copy=True, tracking=0, )


class Variableseconomicasretefuenteline(models.Model):
    _name = 'variables.economicas.retefuente.line'
    _description = 'variables.economicas.retefuente.line'
    retefuente_id = fields.Many2one(string='Retefuente', store=True, copy=True, tracking=0,
                                    comodel_name='variables.economicas.retefuente', )
    valor_desde = fields.Float(string='Valor desde (UVT)', store=True, required=True, copy=True, tracking=0, )
    valor_hasta = fields.Float(string='Valor hasta (UVT)', store=True, required=True, copy=True, tracking=0, )
    valor_impuesto = fields.Float(string='Impuesto (UVT)', store=True, required=True, copy=True, tracking=0, )


class Orderpuestowiz(models.Model):
    _name = 'order.puesto.wiz'
    _description = 'order.puesto.wiz'
    service_order_line = fields.Many2one(string='Linea de orden de servicio', store=True, required=True, copy=True,
                                         tracking=0, comodel_name='project.service.order.line', )
