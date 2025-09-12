# -*- conding:utf-8 -*-

from odoo import fields, models, api


class Contacto(models.Model):
    _inherit = 'res.partner'


    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0, )
    active_lang_count = fields.Integer(string='Contador de idiomas activos', readonly=True, tracking=0, )
    activity_date_deadline = fields.Date(string='Siguiente plazo de actividad', readonly=True, tracking=0, )
    # activity_exception_decoration = fields.Selection(string='Decoración de Actividad  de Excepción', readonly=True, racking=0, )
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0, )
    # activity_state = fields.Selection(string='Estado de la actividad', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Resumen de la siguiente actividad', tracking=0, )
    activity_type_icon = fields.Char(string='Ícono de tipo de actvidad', readonly=True, tracking=0, )
    additional_info = fields.Char(string='Información adicional', store=True, copied=True, tracking=0, )
    afp = fields.Boolean(string='Es AFP', store=True, copied=True, tracking=0, )
    afp_code = fields.Char(string='Código de AFP', store=True, copied=True, tracking=0, )
    arl = fields.Boolean(string='Es ARL', store=True, copied=True, tracking=0, )
    arl_code = fields.Char(string='Código de ARL', store=True, copied=True, tracking=0, )
    bank_account_count = fields.Integer(string='Banco', readonly=True, tracking=0, )
    barcode = fields.Char(string='Código de barras', tracking=0, )
    calcula = fields.Char(string='Calculos', store=True, copied=True, tracking=1, )
    calendar_last_notif_ack = fields.Datetime(string='Última notificación marcada como leída desde el calendario base',
                                              store=True, copied=True, tracking=0, )
    can_publish = fields.Boolean(string='Puede publicar', readonly=True, tracking=0, )
    ccf = fields.Boolean(string='Es CCF', store=True, copied=True, tracking=0, )
    ccf_code = fields.Char(string='Código de CCF', store=True, copied=True, tracking=0, )
    certifications_company_count = fields.Integer(string='Recuento de certificaciones de la empresa', readonly=True,
                                                  tracking=0, )
    certifications_count = fields.Integer(string='Recuento de certificaciones', readonly=True, tracking=0, )
    city = fields.Char(string='Ciudad', store=True, copied=True, tracking=0, )
    claim_count = fields.Integer(string='# Reclamaciones', readonly=True, tracking=0, )
    coc_registration_number = fields.Char(string='Número de Registro de la CdC', tracking=0, )
    color = fields.Integer(string='Índice de Colores', store=True, copied=True, tracking=0, )
    comment = fields.Text(string='Notas', store=True, copied=True, tracking=0, )
    commercial_company_name = fields.Char(string='Entidad del nombre de la compañía', store=True, readonly=True,
                                          tracking=0, )
    commercial_name = fields.Char(string='Nombre Comercial', store=True, copied=True, tracking=0, )
    company_name = fields.Char(string='Nombre de la compañía', store=True, copied=True, tracking=0, )
    # company_type = fields.Selection(string='Tipo de compañía', tracking=0, )
    contact_address = fields.Char(string='Dirección completa', readonly=True, tracking=0, )
    country_code = fields.Char(string='Código de País', readonly=True, tracking=0, )
    country_enforce_cities = fields.Boolean(string='Forzar ciudades', readonly=True, tracking=0, )
    create_date = fields.Datetime(string='Creado', store=True, readonly=True, copied=True, tracking=0, )
    credit_control_count = fields.Integer(string='Líneas de control de crédito', readonly=True, tracking=0, )
    credit_limit = fields.Float(string='Crédito límite', store=True, copied=True, tracking=0, )
    customer = fields.Boolean(string='Cliente', store=True, copied=True, tracking=0, )
    customer_rank = fields.Integer(string='Rango del Cliente', store=True, tracking=0, )
    date = fields.Date(string='Fecha', index=True, store=True, copied=True, tracking=0, )
    date_localization = fields.Date(string='Fecha de Geolocalización', store=True, copied=True, tracking=0, )
    display_name = fields.Char(string='Nombre Público', index=True, store=True, readonly=True, tracking=0, )
    edit_is_einvoicing_agent_field = fields.Boolean(string='Editar Campo ¿Es Agente de Facturación Electrónica?',
                                                    readonly=True, tracking=0, )
    ei_email = fields.Char(string='E-mail Facturación Electrónica', store=True, copied=True, tracking=0, )
    einvoicing_email = fields.Char(string='Correo Electrónico de Facturación Electrónica', store=True, copied=True,
                                   tracking=0, )
    email = fields.Char(string='Correo electrónico', store=True, copied=True, tracking=1, )
    email_bounced = fields.Boolean(string='Correo rebotado', index=True, store=True, copied=True, tracking=0, )
    email_formatted = fields.Char(string='Email formateado', readonly=True, tracking=0, )
    email_normalized = fields.Char(string='Correo electrónico normalizado', store=True, readonly=True, tracking=0, )
    email_personal = fields.Char(string='Correo Personal', store=True, copied=True, tracking=0, )
    email_score = fields.Float(string='Reputación del correo', readonly=True, tracking=0, )
    employee = fields.Boolean(string='Empleado', store=True, copied=True, tracking=0, )
    eps = fields.Boolean(string='Es EPS', store=True, copied=True, tracking=0, )
    eps_code = fields.Char(string='Código de EPS', store=True, copied=True, tracking=0, )
    # extrahour_method = fields.Selection(string='Metodo cálculo extras', store=True, copied=True, tracking=0, )
    fax = fields.Char(string='Fax', store=True, copied=True, tracking=0, )
    first_name = fields.Char(string='Primer Nombre', store=True, copied=True, tracking=0, )
    first_surname = fields.Char(string='Primer Apellido', store=True, copied=True, tracking=0, )
    # followup_status = fields.Selection(string='Estado del seguimiento', readonly=True, tracking=0, )
    function = fields.Char(string='Puesto de trabajo', store=True, copied=True, tracking=0, )
    has_unreconciled_entries = fields.Boolean(string='Tiene apuntes no conciliados', readonly=True, tracking=0, )
    hour_invoicing = fields.Boolean(string='Facturacion por horas', store=True, copied=True, tracking=0, )
    hours_comp_turno = fields.Integer(string='Horas compensadas por turno', store=True, copied=True, tracking=0, )
    hours_work_day = fields.Float(string='Horas jornada laboral', store=True, copied=True, tracking=0, )
    id = fields.Integer(string='ID', store=True, readonly=True, copied=True, tracking=0, )
    im_status = fields.Char(string='Estado del chat', readonly=True, tracking=0, )

    #
    image_1024 = fields.Binary(string='Imagen 1024', store=True, readonly=True, tracking=0, )
    image_128 = fields.Binary(string='Imagen 128', store=True, readonly=True, tracking=0, )
    image_1920 = fields.Binary(string='Imagen', store=True, copied=True, tracking=0, )
    image_256 = fields.Binary(string='Imagen 256', store=True, readonly=True, tracking=0, )
    image_512 = fields.Binary(string='Imagen 512', store=True, readonly=True, tracking=0, )
    image_medium = fields.Text(string='Imagen de tamaño mediano', readonly=True, tracking=0, )
    # invoice_warn = fields.Selection(string='Factura', store=True, copied=True, tracking=0, )
    invoice_warn_msg = fields.Text(string='Mensaje para factura', store=True, copied=True, tracking=0, )
    is_blacklisted = fields.Boolean(string='Lista negra', readonly=True, tracking=0, )
    is_company = fields.Boolean(string='Es una compañia', store=True, copied=True, tracking=0, )
    # is_einvoicing_agent = fields.Selection(string='¿Es un Agente de Facturación Electrónica?', store=True, copied=True, racking=0, )
    is_published = fields.Boolean(string='Está publicado', index=True, store=True, tracking=0, )
    is_seo_optimized = fields.Boolean(string='Optimizado para SEO', readonly=True, tracking=0, )
    journal_item_count = fields.Integer(string='Apuntes contables', readonly=True, tracking=0, )
    # lang = fields.Selection(string='Idioma', store=True, copied=True, tracking=0, )
    last_time_entries_checked = fields.Datetime(string='Fecha de la última conciliación de facturas y pagos',
                                                store=True, readonly=True, tracking=0, )
    # legal_status_type = fields.Selection(string='Tipo de personería', store=True, copied=True, tracking=0, )
    manual_followup = fields.Boolean(string='Seguimiento manual', store=True, copied=True, tracking=0, )
    meeting_count = fields.Integer(string='Nº de reuniones', readonly=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Nº de archivos adjuntos', readonly=True, tracking=0, )
    message_bounce = fields.Integer(string='Rebote', store=True, copied=True, tracking=0, )
    message_has_error = fields.Boolean(string='Error de Envío de Mensaje', readonly=True, tracking=0, )
    message_has_error_counter = fields.Integer(string='Numero de errores', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='Error de entrega del SMS', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Es un seguidor', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Acción requerida', readonly=True, tracking=0, )
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Mensajes sin Leer', readonly=True, tracking=0, )
    message_unread_counter = fields.Integer(string='Nº de mensajes sin leer', readonly=True, tracking=0, )
    mobile = fields.Char(string='Celular', store=True, copied=True, tracking=0, )
    mobile_blacklisted = fields.Boolean(string='El teléfono de la lista negra es un celular', readonly=True,
                                        tracking=0, )
    my_activity_date_deadline = fields.Date(string='Mi fecha límite de actividad', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', index=True, store=True, copied=True, tracking=0, )
    on_time_rate = fields.Float(string='Tasa de entrega a tiempo', readonly=True, tracking=0, )
    only_xml = fields.Boolean(string='Recibe solo XML?', store=True, copied=True, tracking=0, )
    opportunity_count = fields.Integer(string='Oportunidad', readonly=True, tracking=0, )
    parent_name = fields.Char(string='Nombre del padre', readonly=True, tracking=0, )
    partner_gid = fields.Integer(string='ID de la base de datos de la empresa', store=True, copied=True, tracking=0, )
    partner_latitude = fields.Float(string='Geo latitud', store=True, copied=True, tracking=0, )
    partner_longitude = fields.Float(string='Geo longitud', store=True, copied=True, tracking=0, )
    partner_share = fields.Boolean(string='Compartir Contacto', store=True, readonly=True, tracking=0, )
    payment_next_action = fields.Text(string='Siguiente acción', store=True, copied=True, tracking=100, )
    payment_next_action_date = fields.Date(string='Fecha de la próxima acción', tracking=100, )
    payment_note = fields.Text(string='Promesa de pago del cliente', store=True, copied=True, tracking=100, )
    payment_token_count = fields.Integer(string='Cuenta Token de Pago', readonly=True, tracking=0, )
    # person_type = fields.Selection(string='Tipo de Persona', readonly=True, tracking=0, )
    phone = fields.Char(string='Teléfono', store=True, copied=True, tracking=2, )
    phone_blacklisted = fields.Boolean(string='El teléfono de la lista negra es un teléfono', readonly=True,
                                       tracking=0, )
    phone_sanitized = fields.Char(string='Número desinfectado', store=True, readonly=True, tracking=0, )
    phone_sanitized_blacklisted = fields.Boolean(string='Lista negra del Teléfono', readonly=True, tracking=0, )
    # picking_warn = fields.Selection(string='Selección de Exixtencias', store=True, copied=True, tracking=0, )
    picking_warn_msg = fields.Text(string='Mensaje para recolección de stock', store=True, copied=True, tracking=0, )
    plan_to_change_car = fields.Boolean(string='Plan para cambiar de automóvil', store=True, copied=True, tracking=0, )
    prospect = fields.Boolean(string='Prospecto', store=True, copied=True, tracking=0, )
    psvv = fields.Float(string='Poliza de seguro de vida', store=True, copied=True, tracking=0, )
    purchase_order_count = fields.Integer(string='Nº de pedidos de compra', readonly=True, tracking=0, )
    # purchase_warn = fields.Selection(string='Orden de Compra', store=True, copied=True, tracking=0, )
    purchase_warn_msg = fields.Text(string='Mensaje para el pedido de compra', store=True, copied=True, tracking=0, )
    receipt_reminder_email = fields.Boolean(string='Recordatorio de recibo', tracking=0, )
    ref = fields.Char(string='Referencia', index=True, store=True, copied=True, tracking=0, )
    ref_num = fields.Char(string='Número de identificación', index=True, store=True, copied=True, tracking=0, )
    ref_type_required = fields.Boolean(string='Obligatorio', store=True, copied=True, tracking=0, )
    reminder_date_before_receipt = fields.Integer(string='Días antes de la recepción', tracking=0, )
    rut_file = fields.Binary(string='Rut', store=True, tracking=0, )
    rut_file_name = fields.Char(string='Rut Name', store=True, tracking=0, )
    sale_order_count = fields.Integer(string='Nº de pedidos de venta', readonly=True, tracking=0, )
    # sale_warn = fields.Selection(string='Advertencias de ventas', store=True, copied=True, tracking=0, )
    sale_warn_msg = fields.Text(string='Mensaje para el pedido de venta', store=True, copied=True, tracking=0, )
    second_name = fields.Char(string='Segundo Nombre', store=True, copied=True, tracking=0, )
    second_surname = fields.Char(string='Segundo Apellido', store=True, copied=True, tracking=0, )
    seo_name = fields.Char(string='Nombre SEO', store=True, copied=True, tracking=0, )
    signup_expiration = fields.Datetime(string='Expiración del ingreso', store=True, tracking=0, )
    signup_token = fields.Char(string='Palabra de ingreso', store=True, tracking=0, )
    signup_type = fields.Char(string='Tipo de la palabra de ingreso', store=True, tracking=0, )
    signup_url = fields.Char(string='URL de ingreso', readonly=True, tracking=0, )
    signup_valid = fields.Boolean(string='La palabra de ingreso es válida', readonly=True, tracking=0, )
    street = fields.Char(string='Calle', store=True, copied=True, tracking=0, )
    street2 = fields.Char(string='Calle2', store=True, copied=True, tracking=0, )
    sub_activity = fields.Char(string='Sub actividad economica', store=True, copied=True, tracking=0, )
    supplier = fields.Boolean(string='Proveedor', store=True, copied=True, tracking=0, )
    supplier_invoice_count = fields.Integer(string='# de Facturas del Proveedor', readonly=True, tracking=0, )
    supplier_rank = fields.Integer(string='Rango de proveedor', store=True, tracking=0, )
    tar_decreto = fields.Boolean(string='Tarifa decreto', store=True, copied=True, tracking=0, )
    tar_plana = fields.Boolean(string='Tarifa plana', store=True, copied=True, tracking=0, )
    task_count = fields.Integer(string='N° Tareas', readonly=True, tracking=0, )
    tracking_emails_count = fields.Integer(string='Contador de correos con seguimiento', readonly=True, tracking=0, )
    # trust = fields.Selection(string='Grado de confianza para este deudor', tracking=0, )
    # type = fields.Selection(string='Tipo de dirección', store=True, copied=True, tracking=0, )
    # type_payment_payroll = fields.Selection(string='Metodo de Pago Nomina E.', store=True, copied=True, tracking=0, )
    # tz = fields.Selection(string='Zona horaria', store=True, copied=True, tracking=0, )
    tz_offset = fields.Char(string='Compensación de zona horaria', readonly=True, tracking=0, )
    validate_einvoicing_email = fields.Boolean(string='¿Validar el Correo Electrónico de Facturación Electrónica?',
                                               readonly=True, tracking=0, )
    vat = fields.Char(string='NIF', index=True, store=True, copied=True, tracking=0, )
    verification_code = fields.Integer(string='Código de verificación', store=True, readonly=True, tracking=0, )
    view_einvoicing_email_field = fields.Boolean(
        string="Ver Campos de 'Correo Electrónico de Facturación Electrónica '", readonly=True, tracking=0, )
    website = fields.Char(string='Enlace a página web', store=True, copied=True, tracking=0, )
    website_description = fields.Html(string='Descripción Completa del Sitio Web del Asociado', store=True, copied=True,
                                      tracking=0, )
    website_meta_description = fields.Text(string='Meta descripción del sitio web', store=True, copied=True,
                                           tracking=0, )
    website_meta_keywords = fields.Char(string='Meta palabras clave del sitio web', store=True, copied=True,
                                        tracking=0, )
    website_meta_og_img = fields.Char(string='Imagen del Open Graph del sitio', store=True, copied=True, tracking=0, )
    website_meta_title = fields.Char(string='Meta título del sitio web', store=True, copied=True, tracking=0, )
    website_published = fields.Boolean(string='Visible en el sitio web actual', tracking=0, )
    website_short_description = fields.Text(string='Descripción Corta del Sitio Web del Asociado', store=True,
                                            copied=True, tracking=0, )
    website_url = fields.Char(string='URL del Sitio Web', readonly=True, tracking=0, )
    write_date = fields.Datetime(string='Actualizado', store=True, readonly=True, copied=True, tracking=0, )
    zip = fields.Char(string='C.P.', store=True, copied=True, tracking=0, )


class AbstractDmsMixin(models.Model):
    _name = 'abstract.dms.mixin'
    _description = 'Abstract DMS Mixin'

    color = fields.Integer(string='Color', store=True, copied=True, tracking=0, )
    display_name = fields.Char(string='Nombre a mostrar', readonly=True, tracking=0, )
    id = fields.Integer(string='ID', store=True, readonly=True, copied=True, tracking=0, )
    is_hidden = fields.Boolean(string='Almacenamiento está oculto', store=True, readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', index=True, store=True, required=True, copied=True, tracking=0, )
    # storage_id_save_type = fields.Selection(string='Tipo guardado', readonly=True, tracking=0, )
    category_id = fields.Many2one(string='Categoría', store=True, copied=True, tracking=0,
                                  comodel_name='dms.category', )
    company_id = fields.Many2one(string='Compañía', index=True, store=True, readonly=True, tracking=0,
                                 comodel_name='res.company', )
    storage_id = fields.Many2one(string='Almacenamiento', store=True, copied=True, tracking=0,
                                 comodel_name='dms.storage', )



class Academia(models.Model):
    _name = 'academia'
    _description = 'Academia'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )
    nit = fields.Char(string='Nit', store=True, required=True, copied=True, tracking=0, )


class Cuenta(models.Model):
    _inherit = 'account.account'
    _description = 'Cuenta contable'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0, )
    amount_change = fields.Float(string='Diferencia Acumulada', store=True, readonly=True, tracking=0, )
    centralized = fields.Boolean(string='Centralizado', store=True, copied=True, tracking=0, )
    code = fields.Char(string='Código', index=True, store=True, required=True, copied=True, tracking=0, )
    deprecated = fields.Boolean(string='Descatalogado', index=True, store=True, copied=True, tracking=0, )
    diff_amount_divisa = fields.Float(string='Saldo divisa', store=True, readonly=True, tracking=0, )
    diff_amount_local = fields.Float(string='Saldo Local', store=True, readonly=True, tracking=0, )
    diff_amount_trm = fields.Float(string='TRM', store=True, readonly=True, tracking=0, )
    diff_process = fields.Char(string='Ultimo Proceso', store=True, readonly=True, copied=True, tracking=0, )
    is_off_balance = fields.Boolean(string='Está fuera de balance', store=True, readonly=True, tracking=0, )
    name = fields.Char(string='Nombre de la cuenta', index=True, store=True, required=True, copied=True, tracking=0, )
    niif = fields.Boolean(string='Es NIIF', store=True, copied=True, tracking=0, )
    note = fields.Text(string='Notas internas', store=True, copied=True, tracking=0, )
    reconcile = fields.Boolean(string='Permitir conciliación', store=True, copied=True, tracking=0, )
    used = fields.Boolean(string='Usado', readonly=True, tracking=0, )
    account_analytic_change_id = fields.Many2one(string='Cuenta Analitica', store=True, copied=True, tracking=0,
                                                 comodel_name='account.analytic.account', )
    account_change_ids = fields.One2many(string='Movimientos de Diferencia en Cambio', readonly = True, inverse_name='move_id', comodel_name='account.move.line')
    account_diff_niif_id = fields.Many2one(string='Cuenta Consolidada NIIF', store=True, copied=True, tracking=0,
                                           comodel_name='account.account', )
    account_expense_niif_id = fields.Many2one(string='Cuenta Gasto NIIF', store=True, copied=True, tracking=0,
                                              comodel_name='account.account', )
    account_income_niif_id = fields.Many2one(string='Cuenta Ingresos NIIF', store=True, copied=True, tracking=0,
                                             comodel_name='account.account', )
    allowed_journal_ids = fields.Many2many(string='Diarios permitidos', store=True, copied=True, tracking=0,
                                           comodel_name='account.journal', )
    asset_profile_id = fields.Many2one(string='Categoría de activo', store=True, copied=True, tracking=0,
                                       comodel_name='account.asset.profile', )
    change_ids = fields.Many2many(string='Cuentas', store=True, copied=True, tracking=0,
                                  comodel_name='change.difference', )
    company_id = fields.Many2one(string='Compañía', store=True, readonly=True, required=True, copied=True, tracking=0,
                                 comodel_name='res.company', )
    credit_control_line_ids = fields.One2many(string='Líneas de crédito', comodel_name='credit.control.line', inverse_name='partner_id', readonly=True,)
    currency_id = fields.Many2one(string='Cuenta de la moneda', store=True, copied=True, tracking=0,
                                  comodel_name='res.currency', )
    diff_partner_id = fields.Many2one(string='Tercero', store=True, copied=True, tracking=0,
                                      comodel_name='res.partner', )
    exclude_provision_currency_ids = fields.Many2many(string='Exclude Provision Currency', store=True, copied=True,
                                                      tracking=0, comodel_name='res.currency', )
    group_id = fields.Many2one(string='Grupo', store=True, readonly=True, tracking=0, comodel_name='account.group', )
    ifrs_group_id = fields.Many2one(string='Grupo NIIF', store=True, copied=True, tracking=0,
                                    comodel_name='account.group', )
    opening_balance = fields.Monetary(string='Saldo de apertura', readonly=True, tracking=0, )
    opening_credit = fields.Monetary(string='Crédito de apertura', tracking=0, )
    opening_debit = fields.Monetary(string='Débito inicial', tracking=0, )
    root_id = fields.Many2one(string='Raíz', store=True, readonly=True, tracking=0, comodel_name='account.root', )
    structure_id = fields.One2many(string='Estructura', store=True, tracking=0, inverse_name='account_id',
                                   comodel_name='account.account.estructure', )
    tag_ids = fields.Many2many(string='Categorías', store=True, copied=True, tracking=0,
                               comodel_name='account.account.tag', )
    tax_ids = fields.Many2many(string='Impuestos por defecto', store=True, copied=True, tracking=0,
                               comodel_name='account.tax', )
    user_type_id = fields.Many2one(string='Tipo', store=True, required=True, copied=True, tracking=0,
                                   comodel_name='account.account.type', )

    @api.depends('line_ids.amount_currency', 'line_ids.balance', 'line_ids.currency_id')
    def _compute_account_change_ids(self):
        for move in self:
            # Ejemplo de filtro: ajusta a tu criterio real de “diferencia en cambio”
            move.account_change_ids = move.line_ids.filtered(
                lambda l: l.currency_id and abs(l.amount_currency) > 0 and abs(l.balance) > 0
            )

class AccountAccountEstructure(models.Model):
    _name = 'account.account.estructure'
    _description = 'Estructura de la cuenta contable'

    description = fields.Char(string='Descripcion', store=True, required=True, copied=True, tracking=0, )
    digits = fields.Integer(string='Digitos', store=True, required=True, copied=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, required=True, copied=True, tracking=0, )
    account_id = fields.Many2one(string='Cuenta', store=True, copied=True, tracking=0, comodel_name='account.account', )


class EtiquetadeCuenta(models.Model):
    _inherit = 'account.account.tag'
    _description = 'Etiqueta de la cuenta contable'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0, )
    color = fields.Integer(string='Índice de Colores', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre de etiqueta', store=True, required=True, copied=True, tracking=0, )
    tanegate = fields.Boolean(string='Saldo fiscal negativo', store=True, copied=True, tracking=0, )
    account_ids = fields.Many2many(string='Cuentas', store=True, copied=True, tracking=0,
                                   comodel_name='account.account', )
    country_id = fields.Many2one(string='País', store=True, copied=True, tracking=0, comodel_name='res.country', )
    tax_report_line_ids = fields.Many2many(string='Líneas de informe de impuestos', store=True, copied=True, tracking=0,
                                           comodel_name='account.tax.report.line', )


class PlantillasdeCuentas(models.Model):
    _inherit = 'account.account.template'
    _description = 'Plantilla de cuentas contables'

    code = fields.Char(string='Código', index=True, store=True, required=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', index=True, store=True, required=True, copied=True, tracking=0, )
    nocreate = fields.Boolean(string='Crear opcional', store=True, copied=True, tracking=0, )
    note = fields.Text(string='Nota', store=True, copied=True, tracking=0, )
    reconcile = fields.Boolean(string='Permitir la conciliación de facturas y pagos', store=True, copied=True,
                               tracking=0, )
    chart_template_id = fields.Many2one(string='Plantilla plan contable', store=True, copied=True, tracking=0,
                                        comodel_name='account.chart.template', )
    currency_id = fields.Many2one(string='Cuenta de la moneda', store=True, copied=True, tracking=0,
                                  comodel_name='res.currency', )
    tag_ids = fields.Many2many(string='Etiqueta de cuenta', store=True, copied=True, tracking=0,
                               comodel_name='account.account.tag', )
    tax_ids = fields.Many2many(string='Impuestos por defecto', store=True, copied=True, tracking=0,
                               comodel_name='account.tax.template', )
    user_type_id = fields.Many2one(string='Tipo', store=True, required=True, copied=True, tracking=0,
                                   comodel_name='account.account.type', )


class TipodeCuenta(models.Model):
    _inherit = 'account.account.type'
    _description = 'Tipo de cuenta contable'

    include_initial_balance = fields.Boolean(string='Adelantar balance de cuentas', store=True, copied=True,
                                             tracking=0, )
    name = fields.Char(string='Tipo de cuenta', store=True, required=True, copied=True, tracking=0, )
    note = fields.Text(string='Descripción', store=True, copied=True, tracking=0, )


class AccountingReportHelper(models.Model):
    _name = 'account.accounting.report'
    _description = 'Accounting Report Helper'

    date = fields.Date(string='Date', store=True, copied=True, tracking=0, )
    display_type = fields.Char(string='Display Type', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Name', store=True, copied=True, tracking=0, )
    account_id = fields.Many2one(string='Account', store=True, copied=True, tracking=0,
                                 comodel_name='account.account', )
    analytic_account_id = fields.Many2one(string='Analytic Account', store=True, copied=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    analytic_tag_ids = fields.Many2many(string='Analytic Tag', store=True, copied=True, tracking=0,
                                        comodel_name='account.analytic.tag', )
    balance = fields.Monetary(string='Saldo', store=True, copied=True, tracking=0, )
    company_id = fields.Many2one(string='Company', store=True, copied=True, tracking=0, comodel_name='res.company', )
    credit = fields.Monetary(string='Credit', store=True, copied=True, tracking=0, )
    currency_id = fields.Many2one(string='Moneda', store=True, copied=True, tracking=0, comodel_name='res.currency', )
    debit = fields.Monetary(string='Debit', store=True, copied=True, tracking=0, )
    journal_id = fields.Many2one(string='Journal', store=True, copied=True, tracking=0,
                                 comodel_name='account.journal', )
    move_id = fields.Many2one(string='Move', store=True, copied=True, tracking=0, comodel_name='account.move', )


class AnticipoCliente(models.Model):
    _name = 'account.advance.customer'
    _description = 'Anticipo del cliente'

    amount = fields.Float(string='Valor', store=True, copied=True, tracking=100, )
    amount_local = fields.Float(string='Valor Moneda Local', store=True, readonly=True, tracking=0, )
    crossed = fields.Boolean(string='Cruzado', store=True, copied=True, tracking=0, )
    description = fields.Text(string='Descripción', store=True, copied=True, tracking=100, )
    exchange_rate = fields.Float(string='Tasa de Cambio', store=True, copied=True, tracking=100, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    move_nama = fields.Char(string='Nombre del comprobante', store=True, copied=True, tracking=0, )
    multicurrency = fields.Boolean(string='Multimoneda', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=100, )
    pay_date = fields.Date(string='Fecha de Pago', store=True, copied=True, tracking=100, )
    planned_date = fields.Date(string='Fecha planificada', store=True, copied=True, tracking=100, )
    remaining = fields.Float(string='Balance', readonly=True, tracking=0, )
    request_date = fields.Date(string='Fecha de solicitud', store=True, copied=True, tracking=100, )
    account_analytic_id = fields.Many2one(string='Centro de costo', store=True, copied=True, tracking=100,
                                          comodel_name='account.analytic.account', )
    account_id = fields.Many2one(string='Cuenta de Anticipo', store=True, copied=True, tracking=100,
                                 comodel_name='account.account', )
    company_id = fields.Many2one(string='Compañia', store=True, copied=True, tracking=100, comodel_name='res.company', )
    currency_id = fields.Many2one(string='Moneda', store=True, copied=True, tracking=100, comodel_name='res.currency', )
    full_reconcile_id = fields.Many2one(string='Conciliación', store=True, readonly=True, tracking=0,
                                        comodel_name='account.full.reconcile', )
    journal_id = fields.Many2one(string='Diario', store=True, copied=True, tracking=100,
                                 comodel_name='account.journal', )
    local_currency_id = fields.Many2one(string='Moneda Local', store=True, readonly=True, tracking=0,
                                        comodel_name='res.currency', )
    message_channel_ids = fields.Many2many(string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_partner_ids = fields.Many2many(string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    move_id = fields.Many2one(string='Comprobante', store=True, copied=True, tracking=100,
                              comodel_name='account.move', )
    move_line_id = fields.Many2one(string='Linea a reconciliar', store=True, copied=True, tracking=100,
                                   comodel_name='account.move.line', )
    partner_id = fields.Many2one(string='Cliente', store=True, copied=True, tracking=100, comodel_name='res.partner', )
    sale_id = fields.Many2one(string='Pedido de venta', store=True, copied=True, tracking=100,
                              comodel_name='sale.order', )
    user_id = fields.Many2one(string='Usuario', store=True, copied=True, tracking=100, comodel_name='res.users', )

    failed_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Failed Messages', readonly=True,
        domain=lambda self: [
            ('model', '=', self._name),
            ('message_type', '=', 'email'),
            ('failure_type', '!=', False),
        ],)
    message_follower_ids = fields.One2many(comodel_name='mail.followers', inverse_name='res_id', string='Followers', readonly=True, domain=lambda self: [('res_model', '=', self._name)],)
    message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Messages', readonly=True, domain=lambda self: [('model', '=', self._name)],)
    website_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Website Messages', readonly=True,
        domain=lambda self: [
            ('model', '=', self._name),
            ('message_type', '=', 'comment'),
        ],)


class AnticipoProveedor(models.Model):
    _name = 'account.advance.supplier'
    _description = 'Anticipo del proveedor'

    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    amount = fields.Float(string='Valor', store=True, copied=True, tracking=100, )
    amount_local = fields.Float(string='Valor Moneda Local', store=True, readonly=True, tracking=0, )
    crossed = fields.Boolean(string='Cruzado', store=True, copied=True, tracking=0, )
    description = fields.Text(string='Descripción', store=True, copied=True, tracking=100, )
    exchange_rate = fields.Float(string='Tasa de Cambio', store=True, copied=True, tracking=100, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    move_nama = fields.Char(string='Nombre del comprobante', store=True, copied=True, tracking=0, )
    multicurrency = fields.Boolean(string='Multimoneda', store=True, copied=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=100, )
    pay_date = fields.Date(string='Fecha de Pago', store=True, copied=True, tracking=100, )
    planned_date = fields.Date(string='Fecha planificada', store=True, copied=True, tracking=100, )
    reference = fields.Char(string='Referencia de Pago', store=True, copied=True, tracking=100, )
    remaining = fields.Float(string='Balance', readonly=True, tracking=0, )
    request_date = fields.Date(string='Fecha de solicitud', store=True, copied=True, tracking=100, )

    account_analytic_id = fields.Many2one(string='Centro de costo', store=True, copied=True, tracking=100,
                                          comodel_name='account.analytic.account', )
    activity_type_id = fields.Many2one(string='Next Activity Type', tracking=0, comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    bank_account_id = fields.Many2one(string='Cuenta Banco Beneficiario', store=True, copied=True, tracking=100,
                                      comodel_name='res.partner.bank', )
    company_id = fields.Many2one(string='Compañia', store=True, copied=True, tracking=100, comodel_name='res.company', )
    currency_id = fields.Many2one(string='Moneda', store=True, copied=True, tracking=100, comodel_name='res.currency', )
    full_reconcile_id = fields.Many2one(string='Conciliación', store=True, readonly=True, tracking=0,
                                        comodel_name='account.full.reconcile', )
    journal_bank_id = fields.Many2one(string='Diario Banco', store=True, copied=True, tracking=100,
                                      comodel_name='account.journal', )
    local_currency_id = fields.Many2one(string='Moneda Local', store=True, readonly=True, tracking=0,
                                        comodel_name='res.currency', )
    message_channel_ids = fields.Many2many(string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_partner_ids = fields.Many2many(string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    move_id = fields.Many2one(string='Comprobante', store=True, copied=True, tracking=100,
                              comodel_name='account.move', )
    move_line_id = fields.Many2one(string='Linea a reconciliar', store=True, copied=True, tracking=100,
                                   comodel_name='account.move.line', )
    other_partner_id = fields.Many2one(string='Benificiario', store=True, copied=True, tracking=100,
                                       comodel_name='res.partner', )
    partner_id = fields.Many2one(string='Proveedor', store=True, copied=True, tracking=100,
                                 comodel_name='res.partner', )
    payment_mode_id = fields.Many2one(string='Modo de Pago', store=True, copied=True, tracking=100,
                                      comodel_name='account.payment.mode', )
    purchase_order_id = fields.Many2one(string='Orden de compra', store=True, copied=True, tracking=100,
                                        comodel_name='purchase.order', )
    user_id = fields.Many2one(string='Usuario', store=True, copied=True, tracking=100, comodel_name='res.users', )

    activity_ids = fields.One2many(comodel_name='mail.activity', inverse_name='res_id', string='Activities', readonly=True, domain=lambda self: [('res_model', '=', self._name)],)
    failed_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Failed Messages', readonly=True,
        domain=lambda self: [
            ('model', '=', self._name),
            ('message_type', '=', 'email'),
            ('failure_type', '!=', False),
        ],)
    message_follower_ids = fields.One2many(comodel_name='mail.followers', inverse_name='res_id', string='Followers', readonly=True, domain=lambda self: [('res_model', '=', self._name)],)
    message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Messages', readonly=True, domain=lambda self: [('model', '=', self._name)],)
    website_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Website Messages', readonly=True,
        domain=lambda self: [
            ('model', '=', self._name),
            ('message_type', '=', 'comment'),
        ],)


class AgedPartnerBalances(models.Model):
    _name = 'account.aged.partner'
    _description = 'Aged Partner Balances'

    account_code = fields.Char(string='Account Code', store=True, copied=True, tracking=0, )
    account_name = fields.Char(string='Account Name', store=True, copied=True, tracking=0, )
    date = fields.Date(string='Date', store=True, copied=True, tracking=0, )
    display_type = fields.Char(string='Display Type', store=True, copied=True, tracking=0, )
    expected_pay_date = fields.Date(string='Exp. Date', store=True, copied=True, tracking=0, )
    journal_code = fields.Char(string='Journal Code', store=True, copied=True, tracking=0, )
    move_name = fields.Char(string='Move Name', store=True, copied=True, tracking=0, )
    move_type = fields.Char(string='Move Type', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Name', store=True, copied=True, tracking=0, )
    partner_name = fields.Char(string='Partner Name', store=True, copied=True, tracking=0, )
    partner_trust = fields.Char(string='Partner Trust', store=True, copied=True, tracking=0, )
    report_date = fields.Date(string='Report Date', store=True, copied=True, tracking=0, )
    account_id = fields.Many2one(string='Account', store=True, copied=True, tracking=0,
                                 comodel_name='account.account', )
    analytic_account_id = fields.Many2one(string='Analytic Account', store=True, copied=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    analytic_tag_ids = fields.Many2many(string='Analytic Tag', store=True, copied=True, tracking=0,
                                        comodel_name='account.analytic.tag', )
    balance = fields.Monetary(string='Saldo', store=True, copied=True, tracking=0, )
    company_id = fields.Many2one(string='Company', store=True, copied=True, tracking=0, comodel_name='res.company', )
    credit = fields.Monetary(string='Credit', store=True, copied=True, tracking=0, )
    currency_id = fields.Many2one(string='Moneda', store=True, copied=True, tracking=0, comodel_name='res.currency', )
    debit = fields.Monetary(string='Debit', store=True, copied=True, tracking=0, )
    journal_id = fields.Many2one(string='Journal', store=True, copied=True, tracking=0,
                                 comodel_name='account.journal', )
    move_id = fields.Many2one(string='Move', store=True, copied=True, tracking=0, comodel_name='account.move', )
    partner_id = fields.Many2one(string='Asociado', store=True, copied=True, tracking=0, comodel_name='res.partner', )
    payment_id = fields.Many2one(string='Payment', store=True, copied=True, tracking=0,
                                 comodel_name='account.payment', )
    period0 = fields.Monetary(string='As of: ', store=True, copied=True, tracking=0, )
    period1 = fields.Monetary(string='1 - 30', store=True, copied=True, tracking=0, )
    period2 = fields.Monetary(string='31 - 60', store=True, copied=True, tracking=0, )
    period3 = fields.Monetary(string='61 - 90', store=True, copied=True, tracking=0, )
    period4 = fields.Monetary(string='91 - 120', store=True, copied=True, tracking=0, )
    period5 = fields.Monetary(string='Older', store=True, copied=True, tracking=0, )
    report_currency_id = fields.Many2one(string='Report Currency', store=True, copied=True, tracking=0,
                                         comodel_name='res.currency', )


class VencidaporPagar(models.Model):
    _name = 'account.aged.payable'
    _description = 'Vencida por Pagar'

    account_code = fields.Char(string='Account Code', store=True, copied=True, tracking=0, )
    account_name = fields.Char(string='Account Name', store=True, copied=True, tracking=0, )
    date = fields.Date(string='Date', store=True, copied=True, tracking=0, )
    display_type = fields.Char(string='Display Type', store=True, copied=True, tracking=0, )
    expected_pay_date = fields.Date(string='Exp. Date', store=True, copied=True, tracking=0, )
    journal_code = fields.Char(string='Journal Code', store=True, copied=True, tracking=0, )
    move_name = fields.Char(string='Move Name', store=True, copied=True, tracking=0, )
    move_type = fields.Char(string='Move Type', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Name', store=True, copied=True, tracking=0, )
    partner_name = fields.Char(string='Partner Name', store=True, copied=True, tracking=0, )
    partner_trust = fields.Char(string='Partner Trust', store=True, copied=True, tracking=0, )
    report_date = fields.Date(string='Report Date', store=True, copied=True, tracking=0, )
    account_id = fields.Many2one(string='Account', store=True, copied=True, tracking=0,
                                 comodel_name='account.account', )
    analytic_account_id = fields.Many2one(string='Analytic Account', store=True, copied=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    analytic_tag_ids = fields.Many2many(string='Analytic Tag', store=True, copied=True, tracking=0,
                                        comodel_name='account.analytic.tag', )
    balance = fields.Monetary(string='Saldo', store=True, copied=True, tracking=0, )
    company_id = fields.Many2one(string='Company', store=True, copied=True, tracking=0, comodel_name='res.company', )
    credit = fields.Monetary(string='Credit', store=True, copied=True, tracking=0, )
    currency_id = fields.Many2one(string='Moneda', store=True, copied=True, tracking=0, comodel_name='res.currency', )
    debit = fields.Monetary(string='Debit', store=True, copied=True, tracking=0, )
    journal_id = fields.Many2one(string='Journal', store=True, copied=True, tracking=0,
                                 comodel_name='account.journal', )
    move_id = fields.Many2one(string='Move', store=True, copied=True, tracking=0, comodel_name='account.move', )
    partner_id = fields.Many2one(string='Asociado', store=True, copied=True, tracking=0, comodel_name='res.partner', )
    payment_id = fields.Many2one(string='Payment', store=True, copied=True, tracking=0,
                                 comodel_name='account.payment', )
    period0 = fields.Monetary(string='As of: ', store=True, copied=True, tracking=0, )
    period1 = fields.Monetary(string='1 - 30', store=True, copied=True, tracking=0, )
    period2 = fields.Monetary(string='31 - 60', store=True, copied=True, tracking=0, )
    period3 = fields.Monetary(string='61 - 90', store=True, copied=True, tracking=0, )
    period4 = fields.Monetary(string='91 - 120', store=True, copied=True, tracking=0, )
    period5 = fields.Monetary(string='Older', store=True, copied=True, tracking=0, )
    report_currency_id = fields.Many2one(string='Report Currency', store=True, copied=True, tracking=0,
                                         comodel_name='res.currency', )


class VencidaporCobrar(models.Model):
    _name = 'account.aged.receivable'
    _descripcion = 'Vencida por Cobrar'

    account_code = fields.Char(string='Account Code', store=True, copied=True, tracking=0, )
    account_name = fields.Char(string='Account Name', store=True, copied=True, tracking=0, )
    date = fields.Date(string='Date', store=True, copied=True, tracking=0, )
    display_type = fields.Char(string='Display Type', store=True, copied=True, tracking=0, )
    expected_pay_date = fields.Date(string='Exp. Date', store=True, copied=True, tracking=0, )
    journal_code = fields.Char(string='Journal Code', store=True, copied=True, tracking=0, )
    move_name = fields.Char(string='Move Name', store=True, copied=True, tracking=0, )
    move_type = fields.Char(string='Move Type', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Name', store=True, copied=True, tracking=0, )
    partner_name = fields.Char(string='Partner Name', store=True, copied=True, tracking=0, )
    partner_trust = fields.Char(string='Partner Trust', store=True, copied=True, tracking=0, )
    report_date = fields.Date(string='Report Date', store=True, copied=True, tracking=0, )
    account_id = fields.Many2one(string='Account', store=True, copied=True, tracking=0,
                                 comodel_name='account.account', )
    analytic_account_id = fields.Many2one(string='Analytic Account', store=True, copied=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    analytic_tag_ids = fields.Many2many(string='Analytic Tag', store=True, copied=True, tracking=0,
                                        comodel_name='account.analytic.tag', )
    balance = fields.Monetary(string='Saldo', store=True, copied=True, tracking=0, )
    company_id = fields.Many2one(string='Company', store=True, copied=True, tracking=0, comodel_name='res.company', )
    credit = fields.Monetary(string='Credit', store=True, copied=True, tracking=0, )
    currency_id = fields.Many2one(string='Moneda', store=True, copied=True, tracking=0, comodel_name='res.currency', )
    debit = fields.Monetary(string='Debit', store=True, copied=True, tracking=0, )
    journal_id = fields.Many2one(string='Journal', store=True, copied=True, tracking=0,
                                 comodel_name='account.journal', )
    move_id = fields.Many2one(string='Move', store=True, copied=True, tracking=0, comodel_name='account.move', )
    partner_id = fields.Many2one(string='Asociado', store=True, copied=True, tracking=0, comodel_name='res.partner', )
    payment_id = fields.Many2one(string='Payment', store=True, copied=True, tracking=0,
                                 comodel_name='account.payment', )
    period0 = fields.Monetary(string='As of: ', store=True, copied=True, tracking=0, )
    period1 = fields.Monetary(string='1 - 30', store=True, copied=True, tracking=0, )
    period2 = fields.Monetary(string='31 - 60', store=True, copied=True, tracking=0, )
    period3 = fields.Monetary(string='61 - 90', store=True, copied=True, tracking=0, )
    period4 = fields.Monetary(string='91 - 120', store=True, copied=True, tracking=0, )
    period5 = fields.Monetary(string='Older', store=True, copied=True, tracking=0, )
    report_currency_id = fields.Many2one(string='Report Currency', store=True, copied=True, tracking=0,
                                         comodel_name='res.currency', )


class CuentaAnalitica(models.Model):
    _inherit = 'account.analytic.account'
    _description = 'Cuenta Analítica'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0, )
    code = fields.Char(string='Referencia', index=True, store=True, copied=True, tracking=100, )
    message_attachment_count = fields.Integer(string='Nº de archivos adjuntos', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Error de Envío de Mensaje', readonly=True, tracking=0, )
    message_has_error_counter = fields.Integer(string='Numero de errores', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='Error de entrega del SMS', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Es un seguidor', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Acción requerida', readonly=True, tracking=0, )
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Mensajes sin leer', readonly=True, tracking=0, )
    message_unread_counter = fields.Integer(string='Nº de mensajes sin leer', readonly=True, tracking=0, )
    name = fields.Char(string='Cuenta Analítica', index=True, store=True, required=True, copied=True, tracking=100, )
    name_ref = fields.Char(string='Nombre', readonly=True, tracking=100, )
    project_count = fields.Integer(string='Cuenta de proyecto', readonly=True, tracking=0, )
    puesto = fields.Char(string='Puesto', store=True, copied=True, tracking=0, )
    sede = fields.Char(string='Sede', store=True, copied=True, tracking=0, )
    balance = fields.Monetary(string='Balance', readonly=True, tracking=0, )
    city_id = fields.Many2one(string='Ciudad', store=True, copied=True, tracking=0, comodel_name='res.city', )
    company_id = fields.Many2one(string='Compañía', store=True, copied=True, tracking=0, comodel_name='res.company', )
    credit = fields.Monetary(string='Haber', readonly=True, tracking=0, )
    crossovered_budget_line_ids = fields.One2many(comodel_name='crossovered.budget.lines', inverse_name='general_budget_id', string='Líneas de Presupuesto', store=True, tracking=False,)
    currency_id = fields.Many2one(string='Moneda', readonly=True, tracking=0, comodel_name='res.currency', )
    debit = fields.Monetary(string='Debe', readonly=True, tracking=0, )
    failed_message_ids = fields.One2many(comodel_name='mail.message',
                                        inverse_name='res_id',  # Ajusta según el campo Many2one en mail.message que apunta al modelo actual
                                        string='Failed Messages',
                                        store=True,
                                        tracking=False,)
    group_id = fields.Many2one(string='Grupo', store=True, copied=True, tracking=0,
                               comodel_name='account.analytic.group', )
    linea_servicio_id = fields.Many2one(string='Linea de servicio', store=True, copied=True, tracking=0,
                                        comodel_name='project.linea.negocio', )
    line_ids = fields.One2many(comodel_name='account.analytic.line',
                                inverse_name='account_id',
                                string='Líneas analíticas',
                                store=True,
                                tracking=False,)
    message_channel_ids = fields.Many2many(string='Seguidores (Canales)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_follower_ids = fields.One2many(comodel_name='mail.followers',
                                            inverse_name='res_id',
                                            string='Seguidores',
                                            store=True,
                                            tracking=False,)
    message_ids = fields.One2many(comodel_name='mail.message',
                                inverse_name='res_id',
                                string='Mensajes',
                                store=True,
                                tracking=False,)
    message_main_attachment_id = fields.Many2one(string='Adjuntos principales', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_partner_ids = fields.Many2many(string='Seguidores (Contactos)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    partner_id = fields.Many2one(string='Cliente', store=True, copied=True, tracking=100, comodel_name='res.partner', )
    project_ids = fields.One2many(comodel_name='project.project',
                                inverse_name='analytic_account_id',
                                string='Proyectos',
                                store=True,
                                tracking=False,)
    regional_id = fields.Many2one(string='Regional', store=True, copied=True, tracking=0, comodel_name='res.regional', )
    website_message_ids = fields.One2many(comodel_name='mail.message',
                                        inverse_name='res_id',
                                        string='Mensajes del sitio web',
                                        store=True,
                                        tracking=False,)


class DistribucionAnalitica(models.Model):
    _inherit = 'account.analytic.default'
    _description = 'Distribución Analítica'

    date_start = fields.Date(string='Fecha de inicio', store=True, copied=True, tracking=0, )
    date_stop = fields.Date(string='Fecha final', store=True, copied=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0, )
    account_id = fields.Many2one(string='Cuenta', store=True, copied=True, tracking=0, comodel_name='account.account', )
    analytic_id = fields.Many2one(string='Cuenta Analítica', store=True, copied=True, tracking=0,
                                  comodel_name='account.analytic.account', )
    analytic_tag_ids = fields.Many2many(string='Etiquetas analíticas', store=True, copied=True, tracking=0,
                                        comodel_name='account.analytic.tag', )
    company_id = fields.Many2one(string='Compañía', store=True, copied=True, tracking=0, comodel_name='res.company', )
    partner_id = fields.Many2one(string='Asociado', store=True, copied=True, tracking=0, comodel_name='res.partner', )
    product_id = fields.Many2one(string='Producto', store=True, copied=True, tracking=0,
                                 comodel_name='product.product', )
    user_id = fields.Many2one(string='Usuario', store=True, copied=True, tracking=0, comodel_name='res.users', )


class LineaAnalitica(models.Model):
    _inherit = 'account.analytic.line'
    _description = 'Línea Analítica'

    code = fields.Char(string='Código', store=True, copied=True, tracking=0, )
    date = fields.Date(string='Fecha', index=True, store=True, required=True, copied=True, tracking=0, )
    end_date = fields.Datetime(string='Fecha final', store=True, copied=True, tracking=0, )
    is_so_line_edited = fields.Boolean(string='Is So Line Edited', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Descripción', store=True, required=True, copied=True, tracking=0, )
    non_allow_billable = fields.Boolean(string='No facturable', store=True, copied=True, tracking=0, )
    ref = fields.Char(string='Ref.', store=True, copied=True, tracking=0, )
    start_date = fields.Datetime(string='Fecha de inicio', store=True, copied=True, tracking=0, )
    unit_amount = fields.Float(string='Cantidad', store=True, copied=True, tracking=0, )
    account_id = fields.Many2one(string='Cuenta Analítica', index=True, store=True, required=True, copied=True,
                                 tracking=0, comodel_name='account.analytic.account', )
    amount = fields.Monetary(string='Importe', store=True, required=True, copied=True, tracking=0, )
    change_id = fields.Many2one(string='Generador de Diferencia en Cambio', store=True, copied=True, tracking=0,
                                comodel_name='change.difference', )
    commercial_id = fields.Many2one(string='Comercial', store=True, copied=True, tracking=0,
                                    comodel_name='account.commercial', )
    company_id = fields.Many2one(string='Compañía', store=True, readonly=True, required=True, copied=True, tracking=0,
                                 comodel_name='res.company', )
    currency_id = fields.Many2one(string='Moneda', store=True, readonly=True, tracking=0, comodel_name='res.currency', )
    department_id = fields.Many2one(string='Área/Departamento/Contrato', store=True, readonly=True, tracking=0,
                                    comodel_name='hr.department', )
    dimension_project_id = fields.Many2one(string='Proyecto', store=True, copied=True, tracking=0,
                                           comodel_name='project.project', )
    employee_id = fields.Many2one(string='Empleado', store=True, copied=True, tracking=0, comodel_name='hr.employee', )
    encoding_uom_id = fields.Many2one(string='Codificación de UdM', readonly=True, tracking=0, comodel_name='uom.uom', )
    general_account_id = fields.Many2one(string='Cuenta financiera', store=True, readonly=True, tracking=0,
                                         comodel_name='account.account', )
    group_id = fields.Many2one(string='Grupo', store=True, readonly=True, tracking=0,
                               comodel_name='account.analytic.group', )
    move_id = fields.Many2one(string='Apunte contable', index=True, store=True, copied=True, tracking=0,
                              comodel_name='account.move.line', )
    partner_id = fields.Many2one(string='Asociado', store=True, copied=True, tracking=0, comodel_name='res.partner', )
    product_id = fields.Many2one(string='Producto', store=True, copied=True, tracking=0,
                                 comodel_name='product.product', )
    product_uom_category_id = fields.Many2one(string='Categoría', readonly=True, tracking=0,
                                              comodel_name='uom.category', )
    product_uom_id = fields.Many2one(string='Unidad de medida', store=True, copied=True, tracking=0,
                                     comodel_name='uom.uom', )
    project_id = fields.Many2one(string='Proyecto', store=True, copied=True, tracking=0,
                                 comodel_name='project.project', )
    regional_id = fields.Many2one(string='Sucursal', store=True, copied=True, tracking=0, comodel_name='res.regional', )
    so_line = fields.Many2one(string='Elemento del pedido de venta', store=True, copied=True, tracking=0,
                              comodel_name='sale.order.line', )
    tag_ids = fields.Many2many(string='Categorías', store=True, copied=True, tracking=0,
                               comodel_name='account.analytic.tag', )
    task_id = fields.Many2one(string='Tarea', index=True, store=True, copied=True, tracking=0,
                              comodel_name='project.task', )
    ticket_id = fields.Many2one(string='Ticket de servicio de ayuda', store=True, copied=True, tracking=0,
                                comodel_name='helpdesk.ticket', )
    timesheet_invoice_id = fields.Many2one(string='Facturas de clientes', store=True, readonly=True, tracking=0,
                                           comodel_name='account.move', )
    user_id = fields.Many2one(string='Usuario', store=True, copied=True, tracking=0, comodel_name='res.users', )


class Activo(models.Model):
    _name = 'account.asset'
    _description = 'Activo'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    accumulated_value = fields.Float(string='Valor depreciación acumulada', store=True, copied=True, tracking=0, )
    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0, )
    code = fields.Char(string='Referencia', store=True, copied=True, tracking=0, )
    date_remove = fields.Date(string='Fecha de eliminación de activo', store=True, readonly=True, copied=True,
                              tracking=0, )
    date_remove_niff = fields.Date(string='Asset Removal Date', store=True, readonly=True, copied=True, tracking=0, )
    date_start = fields.Date(string='Fecha de inicio del activo', store=True, required=True, copied=True, tracking=0, )
    date_start_niff = fields.Date(string='Fecha de inicio del activo Niif', store=True, copied=True, tracking=0, )
    days_calc = fields.Boolean(string='Calcular por días', store=True, copied=True, tracking=0, )
    days_calc_niff = fields.Boolean(string='Calcular por días Niif', store=True, copied=True, tracking=0, )
    depreciation_base = fields.Float(string='Base Amortización', store=True, readonly=True, tracking=0, )
    depreciation_base_niff = fields.Float(string='Base amortización Niif', store=True, readonly=True, tracking=0, )
    depresiation_value_niif = fields.Float(string='Valor depreciación acumulada Niif', store=True, copied=True,
                                           tracking=0, )
    historic_value = fields.Float(string='Valor histórico compra', store=True, copied=True, tracking=0, )
    is_copy = fields.Boolean(string='Is Copy', readonly=True, tracking=0, )
    is_visible = fields.Boolean(string='visible', readonly=True, tracking=0, )
    marca = fields.Char(string='Marca', store=True, copied=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    method_end = fields.Date(string='Fecha de finalización', store=True, copied=True, tracking=0, )
    method_end_niff = fields.Date(string='Fecha de finalización Niif', store=True, copied=True, tracking=0, )
    method_number = fields.Integer(string='Número de años', store=True, copied=True, tracking=0, )
    method_number_niff = fields.Integer(string='Número de periodos', store=True, copied=True, tracking=0, )
    method_progress_factor = fields.Float(string='Factor decreciente', store=True, copied=True, tracking=0, )
    method_progress_factor_niff = fields.Float(string='Factor decreciente Niif', store=True, copied=True, tracking=0, )
    modelo = fields.Char(string='Modelo', store=True, copied=True, tracking=0, )
    move_line_check = fields.Boolean(string='Tiene asientos contables', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre de activo', store=True, required=True, copied=True, tracking=0, )
    note = fields.Text(string='Nota', store=True, copied=True, tracking=0, )
    placa = fields.Char(string='Placa', store=True, copied=True, tracking=0, )
    prorata = fields.Boolean(string='Tiempo prorrateado', store=True, copied=True, tracking=0, )
    prorata_niff = fields.Boolean(string='Tiempo prorrateado Niif', store=True, copied=True, tracking=0, )
    purchase_value = fields.Float(string='Valor de compra', store=True, required=True, copied=True, tracking=0, )
    purchase_value_niff = fields.Float(string='Valor de compra Niif', store=True, copied=True, tracking=0, )
    salvage_value = fields.Float(string='Valor de rescate', store=True, copied=True, tracking=0, )
    salvage_value_niff = fields.Float(string='Valor de rescate Niif', store=True, copied=True, tracking=0, )
    use_leap_years = fields.Boolean(string='Use años bisiestos', store=True, copied=True, tracking=0, )
    use_leap_years_niff = fields.Boolean(string='Usar años bisiestos Niif', store=True, copied=True, tracking=0, )
    value_depreciated = fields.Float(string='Valor amortizado', store=True, readonly=True, tracking=0, )
    value_depreciated_niff = fields.Float(string='Valor amortizado Niif', store=True, readonly=True, tracking=0, )
    value_residual = fields.Float(string='Valor residual', store=True, readonly=True, tracking=0, )
    value_residual_niff = fields.Float(string='Valor residual Niif', store=True, readonly=True, tracking=0, )
    account_analytic_id = fields.Many2one(string='Cuenta analítica', store=True, copied=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    analytic_account_id_niff = fields.Many2one(string='Cuenta analítica Niif', store=True, copied=True, tracking=0,
                                               comodel_name='account.analytic.account', )
    analytic_tag_ids = fields.Many2many(string='Analytic tags', store=True, copied=True, tracking=0,
                                        comodel_name='account.analytic.tag', )
    centrocosto_id = fields.Many2one(string='Centro de costo', store=True, copied=True, tracking=0,
                                     comodel_name='account.analytic.account', )
    commercial_distribution_id = fields.Many2one(string='Distribución por comercial', store=True, copied=True,
                                                 tracking=0, comodel_name='account.commercial.distribution', )
    company_currency_id = fields.Many2one(string='Moneda la compañía', store=True, readonly=True, tracking=0,
                                          comodel_name='res.currency', )
    company_id = fields.Many2one(string='Compañía', store=True, readonly=True, required=True, copied=True, tracking=0,
                                 comodel_name='res.company', )
    group_ids = fields.Many2many(string='Grupos de activo', store=True, copied=True, tracking=0,
                                 comodel_name='account.asset.group', )
    lot_ids = fields.Many2many(string='Lotes', store=True, copied=True, tracking=0,
                               comodel_name='stock.production.lot', )
    message_channel_ids = fields.Many2many(string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_partner_ids = fields.Many2many(string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    move_eliminated_id = fields.Many2one(string='Baja Inventario Fiscal', store=True, readonly=True, tracking=0,
                                         comodel_name='account.move', )
    move_eliminated_niif_id = fields.Many2one(string='Baja Inventario Fiscal Niif', store=True, readonly=True,
                                              tracking=0, comodel_name='account.move', )
    partner_id = fields.Many2one(string='Empresa', store=True, copied=True, tracking=0, comodel_name='res.partner', )
    partner_id_niff = fields.Many2one(string='Partner', store=True, copied=True, tracking=0,
                                      comodel_name='res.partner', )
    prodlot_id = fields.Many2one(string='Serial', store=True, copied=True, tracking=0,
                                 comodel_name='stock.production.lot', )
    product_id = fields.Many2one(string='Producto', store=True, copied=True, tracking=0,
                                 comodel_name='product.product', )
    profile_id = fields.Many2one(string='Categoría de activo', store=True, required=True, copied=True, tracking=0,
                                 comodel_name='account.asset.profile', )
    profile_id_niff = fields.Many2one(string='Categoría de activo Niif', store=True, copied=True, tracking=0,
                                      comodel_name='account.asset.profile', )
    project_distribution_id = fields.Many2one(string='Distribución', store=True, copied=True, tracking=0,
                                              comodel_name='project.distribution', )
    puesto_id = fields.Many2one(string='Puesto', store=True, copied=True, tracking=0, comodel_name='hr.roster.puesto', )
    regional_id = fields.Many2one(string='Sucursal', store=True, copied=True, tracking=0, comodel_name='res.regional', )
    user_id = fields.Many2one(string='Responsable', store=True, copied=True, tracking=0, comodel_name='res.partner', )
    x_city_id = fields.Many2one(string='Ciudad', store=True, copied=True, tracking=1, comodel_name='res.city', )

    account_move_line_ids = fields.One2many(string='Asientos', comodel_name='account.move.line', inverse_name='move_id', readonly=True, copy=False,)
    depreciation_line_niff_ids = fields.One2many(string='Depreciation Lines (NIIF)', comodel_name='account.asset.line.niff', inverse_name='asset_id', copy=False, tracking=True,)
    depreciation_line_ids = fields.One2many(string='Líneas de amortización', comodel_name='account.asset.line', inverse_name='asset_id', copy=False, tracking=True,)


class AccountAssetAloseWizard(models.Model):
    _name = 'account.asset.alose.wizard'
    _description = 'Account Asset Alose Wizard'

    date_maturity = fields.Date(string='Fecha de Vencimiento', store=True, copied=True, tracking=0, )


class AccountAssetCloseWizard(models.Model):
    _name = 'account.asset.close.wizard'
    _description = 'AccountAssetCloseWizard'

    date_maturity = fields.Date(string='Fecha de Vencimiento', store=True, copied=True, tracking=0)

class CalcularAmortizaciones(models.Model):
    _name = 'account.asset.compute'
    _description = 'Calcular Amortizaciones'

    date_end = fields.Date(string='Fecha', store=True, required=True, copied=True, tracking=0, )
    note = fields.Text(string='Nota', store=True, copied=True, tracking=0, )


class Etiquetasanaliticas(models.Model):
    _name = 'account.asset.group'
    _description = 'Etiquetas analíticas'

    code = fields.Char(string='Código', index=True, store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', index=True, store=True, required=True, copied=True, tracking=0, )
    parent_path = fields.Char(string='Ruta padre', index=True, store=True, copied=True, tracking=0, )


class LineaActivo(models.Model):
    _name = 'account.asset.line'
    _description = 'Línea de activo'

    amount = fields.Float(string='Importe', store=True, required=True, copied=True, tracking=0, )
    depreciated_value = fields.Float(string='Importe ya amortizado', store=True, readonly=True, tracking=0, )
    depreciation_base = fields.Float(string='Base Amortización', readonly=True, tracking=0, )
    init_entry = fields.Boolean(string='Asiento de saldo inicial', store=True, copied=True, tracking=0, )
    line_date = fields.Date(string='Fecha', store=True, required=True, copied=True, tracking=0, )
    line_days = fields.Integer(string='Dias', store=True, readonly=True, copied=True, tracking=0, )
    move_check = fields.Boolean(string='Asentado', store=True, readonly=True, tracking=0, )
    name = fields.Char(string='Nombre de la amortización', store=True, readonly=True, copied=True, tracking=0, )
    remaining_value = fields.Float(string='Amortización del siguiente período', store=True, readonly=True, tracking=0, )
    asset_id = fields.Many2one(string='Activo', store=True, required=True, copied=True, tracking=0,
                               comodel_name='account.asset', )
    move_id = fields.Many2one(string='Asiento de amortización', store=True, readonly=True, copied=True, tracking=0,
                              comodel_name='account.move', )
    previous_id = fields.Many2one(string='Línea de amortización previa', store=True, readonly=True, copied=True,
                                  tracking=0, comodel_name='account.asset.line', )


class GrupoActivo(models.Model):
    _name = 'account.asset.line.niff'
    _description = 'Grupo de activo'

    amount = fields.Float(string='Amount', store=True, required=True, copied=True, tracking=0, )
    depreciated_value = fields.Float(string='Amount Already Depreciated', store=True, readonly=True, tracking=0, )
    depreciation_base = fields.Float(string='Depreciation Base', store=True, readonly=True, copied=True, tracking=0, )
    hide_button = fields.Boolean(string='Hide Button', readonly=True, tracking=0, )
    init_entry = fields.Boolean(string='Initial Balance Entry', store=True, copied=True, tracking=0, )
    line_date = fields.Date(string='Date', store=True, required=True, copied=True, tracking=0, )
    line_days = fields.Integer(string='Days', store=True, readonly=True, copied=True, tracking=0, )
    move_check = fields.Boolean(string='Posted', store=True, readonly=True, tracking=0, )
    name = fields.Char(string='Depreciation Name', store=True, readonly=True, copied=True, tracking=0, )
    remaining_value = fields.Float(string='Next Period Depreciation', store=True, readonly=True, tracking=0, )
    asset_id = fields.Many2one(string='Activo', store=True, required=True, copied=True, tracking=0,
                               comodel_name='account.asset', )
    move_id = fields.Many2one(string='Depreciation Entry', store=True, readonly=True, copied=True, tracking=0,
                              comodel_name='account.move', )
    previous_id = fields.Many2one(string='Previous Depreciation Line', store=True, readonly=True, copied=True,
                                  tracking=0, comodel_name='account.asset.line.niff', )


class AccountAssetProcessWizard(models.Model):
    _name = 'account.asset.process.wizard'
    _description = 'Account Asset Process Wizard'

    date_to_process = fields.Date(string='Mes a procesar', store=True, required=True, copied=True, tracking=0, )
    asset_ids = fields.Many2many(string='Activos a procesar', store=True, copied=True, tracking=0,
                                 comodel_name='account.asset', )


class LineaAmortizacionActivo(models.Model):
    _name = 'account.asset.profile'
    _description = 'Línea de amortización del activo'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0, )
    asset_product_item = fields.Boolean(string='Crear un activo por artículo de producto', store=True, copied=True,
                                        tracking=0, )
    days_calc = fields.Boolean(string='Calcular por días', store=True, copied=True, tracking=0, )
    method_number = fields.Integer(string='Número de años', store=True, copied=True, tracking=0, )
    method_progress_factor = fields.Float(string='Factor decreciente', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', index=True, store=True, required=True, copied=True, tracking=0, )
    note = fields.Text(string='Nota', store=True, copied=True, tracking=0, )
    open_asset = fields.Boolean(string='Omitir estado borrador', store=True, copied=True, tracking=0, )
    prorata = fields.Boolean(string='Tiempo prorrateado', store=True, copied=True, tracking=0, )
    use_leap_years = fields.Boolean(string='Use años bisiestos', store=True, copied=True, tracking=0, )


class AccountAssetRecomputeTrigger(models.Model):
    _name = 'account.asset.recompute.trigger'
    _description = 'Disparador de recálculo de activos'

    date_completed = fields.Datetime(string='Fecha de terminación', store=True, readonly=True, copied=True,
                                     tracking=0, )
    date_trigger = fields.Datetime(string='Fecha de disparo', store=True, readonly=True, copied=True, tracking=0, )
    reason = fields.Char(string='Razón', store=True, required=True, copied=True, tracking=0, )


class AccountAssetRemove(models.Model):
    _name = 'account.asset.remove'
    _description = 'Eliminación de Archivos'

    date_remove = fields.Date(string='Fecha de eliminación de activo', store=True, required=True, copied=True,
                              tracking=0, )
    force_date = fields.Date(string='Forzar fecha contable', store=True, copied=True, tracking=0, )
    note = fields.Text(string='Notas', store=True, copied=True, tracking=0, )
    sale_value = fields.Float(string='Valor de venta', store=True, copied=True, tracking=0, )


class AccountBankMultiMove(models.Model):
    _name = 'account.bank.multi.move'
    _description = 'Account Bank Multi Move'

    credit = fields.Float(string='Credito', store=True, copied=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copied=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copied=True, tracking=0, )
    selected = fields.Boolean(string='Seleccionado', store=True, copied=True, tracking=0, )


class AccountBankMultiTransaction(models.Model):
    _name = 'account.bank.multi.transaction'
    _description = 'Account Bank Multi Transaction'

    amount = fields.Float(string='Valor', store=True, copied=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copied=True, tracking=0, )
    selected = fields.Boolean(string='Seleccionado', store=True, copied=True, tracking=0, )


class AccountBankStatementAvancys(models.Model):
    _name = 'account.bank.statement.avancys'
    _description = 'Account Bank Statement Avancys'

    balance_account = fields.Float(string='Saldo Cuenta', store=True, copied=True, tracking=0, )
    balance_end_real = fields.Float(string='Ending Balance', store=True, copied=True, tracking=0, )
    balance_start = fields.Float(string='Starting Balance', store=True, copied=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, required=True, copied=True, tracking=0, )
    balance_account_end = fields.Float(string='Saldo Cuenta Libro Mayor a Fecha Final', readonly=True, tracking=0)
    date_from = fields.Date(string='Fecha desde', store=True, copied=True, tracking=0, )
    date_multi_get = fields.Date(string='Filtro fecha', store=True, copied=True, tracking=0, )
    date_to = fields.Date(string='Fecha hasta', store=True, copied=True, tracking=0, )
    file = fields.Binary(string='Archivo', store=True, readonly=True, copied=True, tracking=0, )
    file_name = fields.Char(string='Archivo', store=True, copied=True, tracking=0, )
    match_cheque = fields.Boolean(string='Concilar cheques', store=True, copied=True, tracking=0, )
    match_dom = fields.Char(string='Dominio adicional', store=True, copied=True, tracking=0, )
    multi_move_amount = fields.Float(string='Total movimientos seleccionados', store=True, copied=True, tracking=0, )
    multi_trans_amount = fields.Float(string='Total transacciones seleccionadas', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )
    nc_not_account = fields.Float(string='N/C no contabilizadas', store=True, copied=True, tracking=0, )
    nd_not_account = fields.Float(string='N/D no contabilizadas', store=True, copied=True, tracking=0, )
    payment_pending = fields.Float(string='Pagos Pendientes', store=True, copied=True, tracking=0, )
    pending_consing = fields.Float(string='Consignaciones Pendientes', store=True, copied=True, tracking=0, )
    pending_consing_calculated = fields.Float(string='Ingresos Pendientes de Contabilizar (Calculado)', readonly=True,
                                              tracking=0, )
    rotated_check = fields.Float(string='Cheques Pendientes', store=True, copied=True, tracking=0, )
    simple_ref = fields.Char(string='Referencia omision cheque', store=True, copied=True, tracking=0, )
    trans_balance = fields.Float(string='Saldo calculado', store=True, copied=True, tracking=0, )
    value_multi_get = fields.Float(string='Filtro valor', store=True, copied=True, tracking=0, )


class AccountBankStatementLine(models.Model):
    _inherit = 'account.bank.statement.line'
    _description = 'Línea del extracto bancario'

    accepted_rejected_datetime = fields.Datetime(string='Fecha y Hora de Aceptado/Rechazado', tracking=0, )
    allow_draft_delete = fields.Boolean(string='Eliminar en borrador', copied=True, tracking=0, )
    amount_to_text = fields.Char(string='Monto en letras', copied=True, tracking=0, )
    bank_account_required = fields.Boolean(string='Cuenta bancaria requerida', readonly=True, tracking=0, )
    date_of_service = fields.Date(string='Fecha de servicio', copied=True, tracking=0, )
    dbname = fields.Char(string='Nombre de la BD', readonly=True, tracking=0, )
    debit_note_count = fields.Integer(string='Numero de Notas Débito', readonly=True, tracking=0, )
    delivery_datetime = fields.Datetime(string='Fecha y Hora de Entrega', tracking=0, )
    e_invoice_cufe = fields.Char(string='E-Invoice Cufe', tracking=0, )
    e_invoice_reference = fields.Char(string='E-Invoice Reference', tracking=0, )
    ei_app_response = fields.Text(string='Contenido XML Application Response', tracking=0, )
    ei_cude = fields.Char(string='CUDE', readonly=True, tracking=0, )
    ei_cufe = fields.Char(string='CUFE', readonly=True, tracking=0, )
    ei_email_sent = fields.Boolean(string='Email Enviado', tracking=0, )
    ei_generation_date = fields.Char(string='Hora de Generación', readonly=True, tracking=0, )
    ei_qr = fields.Char(string='Informacion QR', readonly=True, tracking=0, )
    ei_validation_date = fields.Char(string='Hora de Validacion', readonly=True, tracking=0, )
    ei_xml_content = fields.Text(string='Contenido XML', tracking=0, )
    end_date = fields.Date(string='Fecha fin', copied=True, tracking=0, )
    invoice_datetime = fields.Datetime(string='Fecha y Hora de la Factura', tracking=0, )
    invoice_reference = fields.Char(string='No. Orden / Referencia', copied=True, tracking=0, )
    invoice_type_code_attrs = fields.Boolean(string='Invoice Type Code Attrs', readonly=True, tracking=0, )
    is_a_claim = fields.Boolean(string='Is a Claim?', tracking=0, )
    is_accepted_rejected = fields.Boolean(string='¿Esta Aceptada/Rechazada?', tracking=0, )
    landed_costs_visible = fields.Boolean(string='Costes en destino visibles', readonly=True, tracking=0, )
    manual_tax = fields.Boolean(string='Ingresar Manualmente los impuestos', copied=True, tracking=0, )
    merge_with_sale_order = fields.Boolean(string='¿Combinar con Pedido de Venta?', readonly=True, tracking=0, )
    move_name = fields.Char(string='Forzar número', tracking=0, )
    move_state_note = fields.Text(string='Nota de Estado', copied=True, tracking=0, )
    payment_date = fields.Date(string='Fecha del pago', readonly=True, tracking=0, )
    payment_mode_filter_type_domain = fields.Char(string='Payment Mode Filter Type Domain', readonly=True, tracking=0, )
    payment_order_ok = fields.Boolean(string='Orden de Pago correcta', readonly=True, tracking=0, )
    payment_state_before_switch = fields.Char(string='Payment State Before Switch', tracking=0, )
    receipt_document_reference = fields.Char(string='Documento de recibo de mercancía / servicio', tracking=0, )
    recoup = fields.Boolean(string='Recobro', copied=True, tracking=0, )
    ref_description = fields.Char(string='Referencia / Descripción', copied=True, tracking=0, )
    reference_date = fields.Date(string='Fecha de Referencia', copied=True, tracking=0, )
    reference_id = fields.Char(string='CUFE de Referencia', copied=True, tracking=0, )
    reference_uuid = fields.Char(string='Número de Referencia', copied=True, tracking=0, )
    start_date = fields.Date(string='Fecha de inicio', copied=True, tracking=0, )
    x_start_date = fields.Date(string='Fecha Inicio Servicio', copied=True, tracking=0, )
    supplier_invoice = fields.Char(string='No. Factura Proveedor', tracking=0, )
    taclosing_end_date = fields.Date(string='Tax Closing End Date', copied=True, tracking=0, )
    talock_date_message = fields.Char(string='Mensaje de fecha de bloqueo de impuestos', readonly=True, tracking=0, )
    tareport_control_error = fields.Boolean(string='Tax Report Control Error', copied=True, tracking=0, )
    ticket_count = fields.Integer(string='Tickets', readonly=True, tracking=0, )
    timesheet_count = fields.Integer(string='Número de partes de tiempo', readonly=True, tracking=0, )
    total_rows = fields.Integer(string='Rowspan Dinámico', copied=True, tracking=0, )
    summary_amount_tax = fields.Monetary(string='Impuesto', readonly=True, tracking=0, )
    summary_amount_total = fields.Monetary(string='Total', readonly=True, tracking=0, )
    summary_amount_untaxed = fields.Monetary(string='Importe libre de impuestos', readonly=True, tracking=0, )
    tax_closing_end_date = fields.Date(string='Tax Closing End Date', copied=True, tracking=0, )
    tax_report_control_error = fields.Boolean(string='Tax Report Control Error', copied=True, tracking=0, )
    total_rows = fields.Integer(string='Rowspan Dinámico', copied=True, tracking=0, )
    warn_inactive_certificate = fields.Boolean(string='¿Advertir Sobre el Certificado Inactivo?', readonly=True,
                                               tracking=0, )
    warn_inactive_resolution = fields.Boolean(string='¿Advertir Sobre Resolución Inactiva?', readonly=True,
                                              tracking=0, )
    warn_remaining = fields.Boolean(string='¿Advertir Sobre lo Restante?', readonly=True, tracking=0, )
    warn_remaining_certificate = fields.Boolean(string='¿Advertir Sobre los Restantes?', readonly=True, tracking=0, )


class AccountBankStatementLineAvancys(models.Model):
    _name = 'account.bank.statement.line.avancys'
    _description = 'Account Bank Statement Line Avancys'

    account_number = fields.Char(string='Bank Account Number', store=True, copied=True, tracking=0, )
    balance = fields.Float(string='Balance', store=True, readonly=True, copied=True, tracking=0, )
    date = fields.Date(string='Date', store=True, required=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )
    new_active_id = fields.Integer(string='New active id', store=True, copied=True, tracking=0, )
    partner_name = fields.Char(string='Partner Name', store=True, copied=True, tracking=0, )
    ref = fields.Char(string='Ref', store=True, copied=True, tracking=0, )
    select = fields.Boolean(string='Select', store=True, readonly=True, copied=True, tracking=0, )
    sequence = fields.Integer(string='Sequence', index=True, store=True, copied=True, tracking=0, )
    #amount = fields.Monetary(string='Amount', store=True, copied=True, tracking=0, )


class AccountBankingBankImport(models.Model):
    _name = 'account.banking.bank.import'
    _description = 'Import Bank Statement'

    date_from = fields.Date(string='Fecha desde', store=True, required=True, copied=True, tracking=0, )
    date_to = fields.Date(string='Fecha hasta', store=True, required=True, copied=True, tracking=0, )
    file = fields.Text(string='Archivo', store=True, required=True, copied=True, tracking=0, )
    log = fields.Text(string='Log', store=True, readonly=True, copied=True, tracking=0, )


class AccountBankingParser(models.Model):
    _name = 'account.banking.parser'
    _description = 'Parser Configuracion'

    account_pos = fields.Char(string='Posicion cuenta', store=True, copied=True, tracking=0, )
    amount_pos = fields.Char(string='Posicion valor', store=True, copied=True, tracking=0, )
    date_format = fields.Char(string='Formato de fecha', store=True, copied=True, tracking=0, )
    date_pos = fields.Char(string='Posicion fecha', store=True, copied=True, tracking=0, )
    line_len = fields.Integer(string='Largo de linea', store=True, copied=True, tracking=0, )
    match_dom = fields.Char(string='Dominio adicional', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Formato de banco', store=True, copied=True, tracking=0, )
    name_pos = fields.Char(string='Posicion comunicacion', store=True, copied=True, tracking=0, )
    ref_pos = fields.Char(string='Posicion referencia', store=True, copied=True, tracking=0, )
    separator = fields.Char(string='Separador', store=True, copied=True, tracking=0, )
    signal_bool = fields.Boolean(string='Signo fuera del valor', store=True, copied=True, tracking=0, )
    signal_declaration = fields.Char(string='Declaracion de signo', store=True, copied=True, tracking=0, )
    signal_position = fields.Char(string='Posicion signo', store=True, copied=True, tracking=0, )


class AccountBudgetPost(models.Model):
    _name = 'account.budget.post'
    _description = 'Posición Presupuestaria'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )


class AccountCashboline(models.Model):
    _name = 'account.cashboline'
    _description = 'Account Cash Rounding'

    coin_value = fields.Float(string='Valor moneda/factura', store=True, required=True, copied=True, tracking=0, )
    number = fields.Integer(string='#Moneda/Billetes', store=True, copied=True, tracking=0, )
    subtotal = fields.Float(string='Subtotal', readonly=True, tracking=0, )


class AccountChangeLockDate(models.Model):
    _name = 'account.change.lock.date'
    _description = 'Cambiar fecha de bloqueo'

    fiscalyear_lock_date = fields.Date(string='Fecha de bloqueo para todos los usuarios', store=True, copied=True,
                                       tracking=0, )
    period_lock_date = fields.Date(string='Fecha establecida para no asesores', store=True, copied=True, tracking=0, )
    talock_date = fields.Date(string='Fecha de bloqueo de impuestos', store=True, copied=True, tracking=0, )
    tax_lock_date = fields.Date(string='Fecha de bloqueo de impuestos', store=True, copied=True, tracking=0, )


class AccountChartTemplate(models.Model):
    _inherit = 'account.chart.template'

    complete_taset = fields.Boolean(string='Conjunto de impuestos completo', store=True, copied=True, tracking=0, )


class AccountCommercial(models.Model):
    _name = 'account.commercial'
    _description = 'account.commercial'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )


class AccountCommercialDistribution(models.Model):
    _name = 'account.commercial.distribution'
    _description = 'Distribución Comercial'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )


class AccountCommercialDistributionLine(models.Model):
    _name = 'account.commercial.distribution.line'
    _description = 'Línea de distribución comercial'

    commercial_percentage = fields.Float(string='Porcentaje', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', readonly=True, required=True, tracking=0, )


class AccountConsignment(models.Model):
    _name = 'account.consignment'
    _description = 'Consignación'

    activity_date_deadline = fields.Date(string='Siguiente plazo de actividad', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Resumen de la siguiente actividad', tracking=0, )
    activity_type_icon = fields.Char(string='Ícono de tipo de actvidad', readonly=True, tracking=0, )
    consignment_block = fields.Boolean(string='Bloquear', store=True, tracking=0, )
    consignment_date = fields.Date(string='Fecha de Consignación', store=True, copied=True, tracking=0, )
    consignment_reference = fields.Char(string='Referencia de Consignación', store=True, copied=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copied=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Nº de archivos adjuntos', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Error de Envío de Mensaje', readonly=True, tracking=0, )
    message_has_error_counter = fields.Integer(string='Numero de errores', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Es un seguidor', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Acción requerida', readonly=True, tracking=0, )
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Mensajes sin leer', readonly=True, tracking=0, )
    message_unread_counter = fields.Integer(string='Nº de mensajes sin leer', readonly=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, readonly=True, required=True, tracking=0, )
    number = fields.Char(string='Número', store=True, tracking=0, )
    readonly_partner = fields.Boolean(string='Tercero Solo Lectura', store=True, tracking=0, )
    reference = fields.Char(string='Referencia', store=True, copied=True, tracking=0, )
    show_available = fields.Boolean(string='Mostrar Disponible', readonly=True, tracking=0, )
    show_exchange = fields.Boolean(string='Mostrar Canje', readonly=True, tracking=0, )
    # amount = fields.Monetary(string='Valor', store=True, copied=True, tracking=100, )


class AccountContainerGroup(models.Model):
    _name = 'account.container.group'
    _description = 'Grupo de contenedores'

    is_container = fields.Boolean(string='Es grupo contenedor?', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Name', store=True, required=True, copied=True, tracking=0, )
    report_group = fields.Boolean(string='Es grupo de reporte?', store=True, copied=True, tracking=0, )
    sequence = fields.Integer(string='Sequence', store=True, copied=True, tracking=0, )


class AccountDebitNote(models.Model):
    _name = 'account.debit.note'
    _description = 'Nota de Débito'

    copy_lines = fields.Boolean(string='Copiar Lineas', store=True, copied=True, tracking=0, )
    country_code = fields.Char(string='Country Code', readonly=True, tracking=0, )
    date = fields.Date(string='Fecha Nota Débito', store=True, required=True, copied=True, tracking=0, )
    journal_type = fields.Char(string='Tipo de Diario', readonly=True, tracking=0, )
    move_type = fields.Char(string='Tipo de Movimiento', readonly=True, tracking=0, )
    reason = fields.Char(string='Motivo', store=True, copied=True, tracking=0, )


class AccountFinancialHtmlReport(models.Model):
    _name = 'account.financial.html.report'
    _description = 'Account Financial Html Report'

    analytic = fields.Boolean(string='Allow analytic filters', store=True, copied=True, tracking=0, )
    comparison = fields.Boolean(string='Allow comparison', store=True, copied=True, tracking=0, )
    date_range = fields.Boolean(string='Based on date ranges', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Name', store=True, copied=True, tracking=0, )
    show_journal_filter = fields.Boolean(string='Allow filtering by journals', store=True, copied=True, tracking=0, )
    tareport = fields.Boolean(string='Reporte Impuestos', store=True, copied=True, tracking=0, )
    unfold_all_filter = fields.Boolean(string='Show unfold all filter', store=True, copied=True, tracking=0, )
    tax_report = fields.Boolean(string='Reporte Impuestos', store=True, copied=True, tracking=0, )


class AccountFinancialHtmlReportLine(models.Model):
    _name = 'account.financial.html.report.line'
    _description = 'Account Financial Html Report Line'

    code = fields.Char(string='Code', store=True, copied=True, tracking=0, )
    domain = fields.Char(string='Domain', store=True, copied=True, tracking=0, )
    formulas = fields.Char(string='Formulas', store=True, copied=True, tracking=0, )
    green_on_positive = fields.Boolean(string='Is growth good when positive', store=True, copied=True, tracking=0, )
    groupby = fields.Char(string='Group by', store=True, copied=True, tracking=0, )
    hide_if_empty = fields.Boolean(string='Hide If Empty', store=True, copied=True, tracking=0, )
    hide_if_zero = fields.Boolean(string='Hide If Zero', store=True, copied=True, tracking=0, )
    level = fields.Integer(string='Level', store=True, required=True, copied=True, tracking=0, )
    name = fields.Char(string='Section Name', store=True, copied=True, tracking=0, )
    parent_path = fields.Char(string='Parent Path', index=True, store=True, copied=True, tracking=0, )
    print_on_new_page = fields.Boolean(string='Print On New Page', store=True, copied=True, tracking=0, )
    sequence = fields.Integer(string='Sequence', store=True, copied=True, tracking=0, )


class AccountFinancialLevels(models.Model):
    _name = 'account.financial.levels'
    _description = 'Account Financial Levels'

    code = fields.Char(string='Código', store=True, copied=True, tracking=0, )
    help = fields.Char(string='Ayuda', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0, )


class AccountFinancialReportAssistant(models.Model):
    _name = 'account.financial.report.assistant'
    _description = 'Account Financial Report Assistant'

    date_end = fields.Date(string='Fecha Fin', store=True, copied=True, tracking=0, )
    date_start = fields.Date(string='Fecha Inicio', store=True, copied=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copied=True, tracking=0, )


class AccountFinancialReportAssistantLine(models.Model):
    _name = 'account.financial.report.assistant.line'
    _description = 'Account Financial Report Assistant Line'

    amount_final = fields.Float(string='Saldo Final', store=True, copied=True, tracking=0, )
    amount_initial = fields.Float(string='Saldo Inicial', store=True, copied=True, tracking=0, )
    bold = fields.Boolean(string='Negrilla', store=True, copied=True, tracking=0, )
    code = fields.Char(string='Code', store=True, copied=True, tracking=0, )
    credit = fields.Float(string='Credito', store=True, copied=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copied=True, tracking=0, )
    level = fields.Integer(string='Nivel', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre Cuenta', store=True, copied=True, tracking=0, )


class AccountFinancialReportAssistantWizard(models.Model):
    _name = 'account.financial.report.assistant.wizard'
    _description = 'Account Financial Report Assistant Wizard'

    date_from = fields.Date(string='Fecha Inicio', store=True, copied=True, tracking=0, )
    date_to = fields.Date(string='Fecha Fin', store=True, copied=True, tracking=0, )
    initial_balance = fields.Boolean(string='Incluir saldo inicial', store=True, copied=True, tracking=0, )


class AccountFinancialReportBalance(models.Model):
    _name = 'account.financial.report.balance'
    _description = 'Account Financial Report Balance'

    date_end = fields.Date(string='Fecha Fin', store=True, copied=True, tracking=0, )
    date_start = fields.Date(string='Fecha Inicio', store=True, copied=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copied=True, tracking=0, )


class AccountFinancialReportBalanceGeneral(models.Model):
    _name = 'account.financial.report.balance.general'
    _description = 'Account Financial Report Balance General'

    date_end = fields.Date(string='Fecha Fin', store=True, copied=True, tracking=0, )
    date_start = fields.Date(string='Fecha Inicio', store=True, copied=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copied=True, tracking=0, )


class AccountFinancialReportBalanceGeneralLine(models.Model):
    _name = 'account.financial.report.balance.general.line'
    _description = 'Account Financial Report Balance General Line'

    amount = fields.Float(string='Saldo Final', store=True, copied=True, tracking=0, )
    bold = fields.Boolean(string='Negrilla', store=True, copied=True, tracking=0, )
    code = fields.Char(string='Code', store=True, copied=True, tracking=0, )
    credit = fields.Float(string='Credito', store=True, copied=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copied=True, tracking=0, )
    has_value = fields.Boolean(string='Tiene Valor', store=True, copied=True, tracking=0, )
    identation = fields.Integer(string='Identacion', store=True, copied=True, tracking=0, )
    is_total = fields.Boolean(string='Es Total', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre Cuenta', store=True, copied=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0, )
    signo_en_reporte = fields.Char(string='Signo en Reporte', store=True, copied=True, tracking=0, )


class AccountFinancialReportBalanceGeneralWizard(models.Model):
    _name = 'account.financial.report.balance.general.wizard'
    _description = 'Account Financial Report Balance General Wizard'

    date_end = fields.Date(string='Fecha de Corte', store=True, copied=True, tracking=0, )


class AccountFinancialReportBalanceInventoryWizard(models.Model):
    _name = 'account.financial.report.balance.inventory.wizard'
    _description = 'Account Financial Report Balance Inventory Wizard'

    date_end = fields.Date(string='Fecha Fin', store=True, copied=True, tracking=0, )
    date_start = fields.Date(string='Fecha Inicio', store=True, copied=True, tracking=0, )


class AccountFinancialReportBalanceLine(models.Model):
    _name = 'account.financial.report.balance.line'
    _description = 'Account Financial Report Balance Line'

    amount_final = fields.Float(string='Saldo Final', store=True, copied=True, tracking=0, )
    amount_initial = fields.Float(string='Saldo Inicial', store=True, copied=True, tracking=0, )
    bold = fields.Boolean(string='Negrilla', store=True, copied=True, tracking=0, )
    code = fields.Char(string='Code', store=True, copied=True, tracking=0, )
    credit = fields.Float(string='Credito', store=True, copied=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copied=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copied=True, tracking=0, )
    level = fields.Integer(string='Nivel', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre Cuenta', store=True, copied=True, tracking=0, )
    period_move = fields.Float(string='Movimiento de Periodo', store=True, copied=True, tracking=0, )


class AccountFinancialReportBalanceWizard(models.Model):
    _name = 'account.financial.report.balance.wizard'
    _description = 'Account Financial Report Balance Wizard'

    date_end = fields.Date(string='Fecha Fin', store=True, copied=True, tracking=0, )
    date_start = fields.Date(string='Fecha Inicio', store=True, copied=True, tracking=0, )


class AccountFinancialReportDiarioWizard(models.Model):
    _name = 'account.financial.report.diario.wizard'
    _description = 'Account Financial Report Diario Wizard'

    date_end = fields.Date(string='Fecha Fin', store=True, copied=True, tracking=0, )
    date_start = fields.Date(string='Fecha Inicio', store=True, copied=True, tracking=0, )


class AccountFinancialReportMajorBalanceWizard(models.Model):
    _name = 'account.financial.report.major.balance.wizard'
    _description = 'Account Financial Report Major Balance Wizard'

    date_end = fields.Date(string='Fecha Fin', store=True, copied=True, tracking=0, )
    date_start = fields.Date(string='Fecha Inicio', store=True, copied=True, tracking=0, )


class AccountFinancialReportsExportWizard(models.Model):
    _name = 'account.financial.reports.export.wizard'
    _description = 'Account Financial Reports Export Wizard'

    doc_name = fields.Char(string='Documents Name', store=True, copied=True, tracking=0, )
    report_id = fields.Integer(string='Parent Report Id', store=True, required=True, copied=True, tracking=0, )
    report_model = fields.Char(string='Report Model', store=True, required=True, copied=True, tracking=0, )


class AccountFinancialReportsExportWizardFormat(models.Model):
    _name = 'account.financial.reports.export.wizard.format'
    _description = 'Account Financial Reports Export Wizard Format'

    fun_to_call = fields.Char(string='Function to Call', store=True, required=True, copied=True, tracking=0, )
    name = fields.Char(string='Name', store=True, required=True, copied=True, tracking=0, )


class AccountFinancialReportStateIncome(models.Model):
    _name = 'account.financial.report.state.income'
    _description = 'Account Financial Report State Income'

    date_end = fields.Date(string='Fecha Fin', store=True, copied=True, tracking=0, )
    date_start = fields.Date(string='Fecha Inicio', store=True, copied=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copied=True, tracking=0, )


class AccountFinancialReportStateIncomeLine(models.Model):
    _name = 'account.financial.report.state.income.line'
    _description = 'Account Financial Report State Income Line'

    amount = fields.Float(string='Saldo Final', store=True, copied=True, tracking=0, )
    bold = fields.Boolean(string='Negrilla', store=True, copied=True, tracking=0, )
    code = fields.Char(string='Code', store=True, copied=True, tracking=0, )
    credit = fields.Float(string='Credito', store=True, copied=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copied=True, tracking=0, )
    has_value = fields.Boolean(string='Tiene Valor', store=True, copied=True, tracking=0, )
    is_total = fields.Boolean(string='Es Total', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre Cuenta', store=True, copied=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0, )
    signo_en_reporte = fields.Char(string='Signo en Reporte', store=True, copied=True, tracking=0, )


class AccountFinancialReportStateIncomeWizard(models.Model):
    _name = 'account.financial.report.state.income.wizard'
    _description = 'Account Financial Report State Income Wizard'

    date_from = fields.Date(string='Fecha Inicio', store=True, copied=True, tracking=0, )
    date_to = fields.Date(string='Fecha Fin', store=True, copied=True, tracking=0, )

class AccountFinancialReportTaxes(models.Model):
    _name = 'account.financial.report.taxes'
    _description = 'Account Financial Report Taxes'

    date_from = fields.Date(string='Fecha Inicial', store=True, copied=True, tracking=0, )
    date_to = fields.Date(string='Fecha Final', store=True, copied=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copied=True, tracking=0, )

class AccountFinancialReportTaxesLine(models.Model):
    _name = 'account.financial.report.taxes.line'
    _description = 'Account Financial Report Taxes Line'

    account = fields.Char(string='Código', store=True, copied=True, tracking=0, )
    amount_final = fields.Float(string='Saldo Final', store=True, copied=True, tracking=0, )
    bold = fields.Boolean(string='bold', store=True, copied=True, tracking=0, )
    credit = fields.Float(string='Credito', store=True, copied=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copied=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copied=True, tracking=0, )
    taamount = fields.Float(string='Base', store=True, copied=True, tracking=0, )
    tabase_amount = fields.Float(string='Retención', store=True, copied=True, tracking=0, )
    tax_amount = fields.Float(string='Base', store=True, copied=True, tracking=0, )
    tax_base_amount = fields.Float(string='Retención', store=True, copied=True, tracking=0, )


class SaldoInicialDelEjercicioFiscal(models.Model):
    _name = 'account.financial.year.op'
    _description ='Saldo Inicial Del Ejercicio Fiscal'

    account_tax_periodicity_reminder_day = fields.Integer(string='Reminder', required=True, tracking=0, )


class AccountFiscalPositionPartyTaxScheme(models.Model):
    _name='account.fiscal.position.party.tax.scheme'
    _description = 'Account Fiscal Position Party Tax Scheme'

    code = fields.Char(string='Código', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0, )


class AccountFiscalPositionTaxLevelCode(models.Model):
    _name = 'account.fiscal.position.tax.level.code'
    _description = 'Account Fiscal Position Tax Level Code'

    code = fields.Char(string='Código', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0, )


class AccountFinancialReportTaxesWizard(models.Model):
    _name = 'account.financial.report.taxes.wizard'
    _description = 'Account Financial Report Taxes Wizard'

    date_from = fields.Date(string='Fecha Inical', store=True, copied=True, tracking=0, )
    date_to = fields.Date(string='Fecha Final', store=True, copied=True, tracking=0, )


class AccountFinancialReportTrial(models.Model):
    _name = 'account.financial.report.trial'
    _description = 'Account Financial Report Trial'
    date_end = fields.Date(string='Fecha Fin', store=True, copied=True, tracking=0, )
    date_start = fields.Date(string='Fecha Inicio', store=True, copied=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, copied=True, tracking=0, )


class AccountFinancialReportTrialLine(models.Model):
    _name = 'account.financial.report.trial.line'
    _description = 'Account Financial Report Trial Line'
    amount_final = fields.Float(string='Saldo Final', store=True, copied=True, tracking=0, )
    amount_initial = fields.Float(string='Saldo Inicial', store=True, copied=True, tracking=0, )
    bold = fields.Boolean(string='Negrilla', store=True, copied=True, tracking=0, )
    code = fields.Char(string='Code', store=True, copied=True, tracking=0, )
    credit = fields.Float(string='Credito', store=True, copied=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copied=True, tracking=0, )
    level = fields.Integer(string='Nivel', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre Cuenta', store=True, copied=True, tracking=0, )


class AccountFinancialStructure(models.Model):
    _name = 'account.financial.structure'
    _description = 'Estructura Financiera'
    is_active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0, )


class AccountFinancialStructureLine(models.Model):
    _name = 'account.financial.structure.line'
    description = fields.Char(string='Descripción', store=True, copied=True, tracking=0, )
    digits = fields.Integer(string='Digitos', store=True, copied=True, tracking=0, )
    sequence = fields.Integer(string='Secuenca', store=True, copied=True, tracking=0, )


class AccountFinancialYearOp(models.Model):
    _name = 'account.fiscalyear'
    _description = 'Año Fiscal Operaciones'

    account_taperiodicity_reminder_day = fields.Integer(string='Reminder', required=True, tracking=0, )


class AccountFiscalPositionPartyTascheme(models.Model):
    _name = 'account.fiscal.position.party.tascheme'
    _description = 'Account Fiscal Position Party Tascheme'
    code = fields.Char(string='Código', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0, )


class AccountFiscalPositionTalevelCode(models.Model):
    _name = 'account.fiscal.position.talevel.code'
    _description = 'Account Fiscal Position Talevel Code'
    code = fields.Char(string='Código', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0, )


class AccountFiscalPositionTax(models.Model):
    _inherit = 'account.fiscal.position.tax'

    value = fields.Float(string='Valor', store=True, copied=True, tracking=0, )


class AccountFiscalYear(models.Model):
    _name = 'account.fiscal.year'
    _description = 'Año Fiscal'
    date_from = fields.Date(string='Fecha de inicio', store=True, required=True, copied=True, tracking=0, )
    date_to = fields.Date(string='Fecha final', store=True, required=True, copied=True, tracking=0, )
    in_invoice_sent = fields.Integer(string='Documentos Soporte Enviados', store=True, copied=True, tracking=0, )
    in_refund_sent = fields.Integer(string='Notas Crédito de Documento Soporte Enviadas', store=True, copied=True,
                                    tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )
    niae_sent = fields.Integer(string='NIAE Sent', store=True, copied=True, tracking=0, )
    nie_sent = fields.Integer(string='NIE Sent', store=True, copied=True, tracking=0, )
    out_invoice_sent = fields.Integer(string='Facturas Enviadas', store=True, copied=True, tracking=0, )
    out_refund_credit_sent = fields.Integer(string='Notas de Crédito Enviadas', store=True, copied=True, tracking=0, )
    out_refund_debit_sent = fields.Integer(string='Notas de Débito Enviadas', store=True, copied=True, tracking=0, )


class AccountFiscalyearCloseAccount(models.Model):
    _name = 'account.fiscalyear.close.account'
    _description = 'Account Fiscalyear Close Account'

    date_from = fields.Date(string='Desde', store=True, required=True, copied=True, tracking=0, )
    date_maturity = fields.Date(string='Fecha de vencimiento', store=True, required=True, copied=True, tracking=0, )
    date_to = fields.Date(string='Hasta', store=True, required=True, copied=True, tracking=0, )
    detail = fields.Boolean(string='Detalle', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Descripción', store=True, required=True, copied=True, tracking=0, )
    partner = fields.Boolean(string='Por tercero', store=True, copied=True, tracking=0, )
    period_id = fields.Integer(string='Periodo', store=True, readonly=True, copied=True, tracking=0, )


class AccountGroup(models.Model):
    _inherit = 'account.group'

    code_prefiend = fields.Char(string='Fin de prefijo de código', store=True, copied=True, tracking=0, )
    code_prefistart = fields.Char(string='Inicio de prefijo de código', store=True, copied=True, tracking=0, )
    code = fields.Char(string='Código', index=True, store=True, required=True, copied=True, tracking=0, )
    complete_code = fields.Char(string='Código Completo', readonly=True, tracking=0, )
    complete_name = fields.Char(string='Nombre completo', readonly=True, tracking=0, )
    ifrs_bool = fields.Boolean(string='Es NIIF', store=True, tracking=0, )
    invertir_valores = fields.Boolean(string='Invertir valores?', store=True, copied=True, tracking=0, )
    level = fields.Integer(string='Nivel', readonly=True, tracking=0, )


class AccountGroupTemplate(models.Model):
    _inherit = 'account.group.template'

    code_prefiend = fields.Char(string='Fin de prefijo de código', store=True, copied=True, tracking=0, )
    code_prefistart = fields.Char(string='Inicio de prefijo de código', store=True, copied=True, tracking=0, )


class AccountInvoiceSend(models.TransientModel):
    _inherit = 'account.invoice.send'
    body_str = fields.Html(string='Cuerpo', copied=True, tracking=0, )
    is_wp = fields.Boolean(string='WhatsApp?', copied=True, tracking=0, )


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    allow_date = fields.Boolean(string='Validar Fecha en Periodo', store=True, copied=True, tracking=0, )
    debit_note_sequence = fields.Boolean(string='Secuencia de Nota Débito Dedicada', store=True, copied=True, tracking=0, )
    fondo = fields.Float(string='Fondo', store=True, copied=True, tracking=0, )
    inbound_payment_order_only = fields.Boolean(string='Orden de Pago correcta', store=True, readonly=True, tracking=0, )
    outbound_payment_order_only = fields.Boolean(string='Orden de Pago correcta', store=True, readonly=True, tracking=0, )
    petty_cash = fields.Boolean(string='Caja menor', store=True, copied=True, tracking=0, )
    resolution = fields.Char(string='Resolución', store=True, copied=True, tracking=0, )
    terms = fields.Text(string='Términos', store=True, copied=True, tracking=0, )
    total_credit = fields.Float(string='Total credito', readonly=True, tracking=0, )
    total_debit = fields.Float(string='Total debito', readonly=True, tracking=0, )
    update_posted = fields.Boolean(string='Permitir Cancelación de Asientos', store=True, copied=True, tracking=0, )


class AccountLoan(models.Model):
    _name = 'account.loan'
    _description = 'Préstamo'
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0, )
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0, )
    balance_debt = fields.Float(string='Saldo por amortizar', readonly=True, tracking=0, )
    balance = fields.Float(string='Valor inicial de obligacion', store=True, required=True, copied=True, tracking=0, )
    final_payment = fields.Float(string='Pago final', store=True, copied=True, tracking=100, )
    first_payment = fields.Float(string='Primer desembolso', store=True, copied=True, tracking=0, )
    intrest_per_period = fields.Float(string='Interes', store=True, required=True, copied=True, tracking=100, )
    loan_no = fields.Char(string='Numero de Obligacion', store=True, required=True, copied=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    payment_date = fields.Date(string='Fecha de desembolso', store=True, required=True, copied=True, tracking=0, )
    period_no = fields.Integer(string='Meses Entre Periodos', store=True, required=True, copied=True, tracking=0, )
    periods_to_pay = fields.Integer(string='Plazo Inicial', store=True, required=True, copied=True, tracking=0, )
    remain_period = fields.Integer(string='Periodos por pagar', readonly=True, tracking=0, )
    start_period = fields.Integer(string='Periodos de Gracia', store=True, copied=True, tracking=0, )
    tir_contable = fields.Float(string='TIR Contable', store=True, copied=True, tracking=0, )
    tir = fields.Float(string='TIR Fiscal', store=True, copied=True, tracking=0, )


class AccountLoanDistribution(models.Model):
    _name = 'account.loan.distribution'
    _description = 'Distribución de Préstamo'
    name = fields.Char(string='Comentario', store=True, copied=True, tracking=0, )
    rate = fields.Float(string='(%)', store=True, required=True, copied=True, tracking=0, )


class AccountLoanPrepaid(models.Model):
    _name = 'account.loan.prepaid'
    _description = 'Cuenta de Préstamo Prepagado'
    approve_date = fields.Date(string='Fecha de Aprobacion', store=True, readonly=True, copied=True, tracking=0, )
    date = fields.Date(string='Fecha de Pago', store=True, readonly=True, required=True, copied=True, tracking=0, )
    description = fields.Text(string='Descripcion', store=True, copied=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    name = fields.Char(string='Codigo', store=True, readonly=True, copied=True, tracking=0, )
    numero_cuotas = fields.Integer(string='Cuotas a Modificar', store=True, readonly=True, copied=True, tracking=0, )
    value = fields.Float(string='Valor', store=True, readonly=True, required=True, copied=True, tracking=0, )


class AccountMove(models.Model):
    _inherit = 'account.move'

    accepted_rejected_datetime = fields.Datetime(string='Fecha y Hora de Aceptado/Rechazado', store=True, tracking=0, )
    allow_draft_delete = fields.Boolean(string='Eliminar en borrador', store=True, copied=True, tracking=0, )
    amount_to_text = fields.Char(string='Monto en letras', store=True, copied=True, tracking=0, )
    bank_account_required = fields.Boolean(string='Cuenta bancaria requerida', readonly=True, tracking=0, )
    date_of_service = fields.Date(string='Fecha de servicio', store=True, copied=True, tracking=0, )
    dbname = fields.Char(string='Nombre de la BD', readonly=True, tracking=0, )
    debit_note_count = fields.Integer(string='Numero de Notas Débito', readonly=True, tracking=0, )
    delivery_datetime = fields.Datetime(string='Fecha y Hora de Entrega', store=True, tracking=0, )
    e_invoice_cufe = fields.Char(string='E-Invoice Cufe', store=True, tracking=0, )
    e_invoice_reference = fields.Char(string='E-Invoice Reference', store=True, tracking=0, )
    ei_app_response = fields.Text(string='Contenido XML Application Response', store=True, tracking=0, )
    ei_cude = fields.Char(string='CUDE', store=True, readonly=True, tracking=100, )
    ei_cufe = fields.Char(string='CUFE', store=True, readonly=True, tracking=100, )
    ei_email_sent = fields.Boolean(string='Email Enviado', store=True, tracking=0, )
    ei_generation_date = fields.Char(string='Hora de Generación', store=True, readonly=True, tracking=0, )
    ei_qr = fields.Char(string='Informacion QR', store=True, readonly=True, tracking=0, )
    ei_validation_date = fields.Char(string='Hora de Validacion', store=True, readonly=True, tracking=0, )
    ei_xml_content = fields.Text(string='Contenido XML', store=True, tracking=0, )
    end_date = fields.Date(string='Fecha fin', store=True, copied=True, tracking=0, )
    invoice_datetime = fields.Datetime(string='Fecha y Hora de la Factura', store=True, tracking=0, )
    invoice_reference = fields.Char(string='No. Orden / Referencia', store=True, copied=True, tracking=0, )
    invoice_type_code_attrs = fields.Boolean(string='Invoice Type Code Attrs', readonly=True, tracking=0, )
    is_a_claim = fields.Boolean(string='Is a Claim?', store=True, tracking=0, )
    is_accepted_rejected = fields.Boolean(string='¿Esta Aceptada/Rechazada?', store=True, tracking=0, )
    landed_costs_visible = fields.Boolean(string='Costes en destino visibles', readonly=True, tracking=0, )
    manual_tax = fields.Boolean(string='Ingresar Manualmente los impuestos', store=True, copied=True, tracking=0, )
    merge_with_sale_order = fields.Boolean(string='¿Combinar con Pedido de Venta?', store=True, readonly=True, tracking=0, )
    move_name = fields.Char(string='Forzar número', store=True, tracking=0, )
    move_state_note = fields.Text(string='Nota de Estado', store=True, copied=True, tracking=0, )
    payment_date = fields.Date(string='Fecha del pago', readonly=True, tracking=0, )
    payment_mode_filter_type_domain = fields.Char(string='Payment Mode Filter Type Domain', readonly=True, tracking=0, )
    payment_order_ok = fields.Boolean(string='Orden de Pago correcta', readonly=True, tracking=0, )
    payment_state_before_switch = fields.Char(string='Payment State Before Switch', store=True, tracking=0, )
    receipt_document_reference = fields.Char(string='Documento de recibo de mercancía / servicio', store=True, tracking=0, )
    recoup = fields.Boolean(string='Recobro', store=True, copied=True, tracking=0, )
    ref_description = fields.Char(string='Referencia / Descripción', store=True, copied=True, tracking=0, )
    reference_date = fields.Date(string='Fecha de Referencia', store=True, copied=True, tracking=0, )
    reference_id = fields.Char(string='CUFE de Referencia', store=True, copied=True, tracking=0, )
    reference_uuid = fields.Char(string='Número de Referencia', store=True, copied=True, tracking=0, )
    start_date = fields.Date(string='Fecha de inicio', store=True, copied=True, tracking=0, )
    start_date = fields.Date(string='Fecha Inicio Servicio', store=True, copied=True, tracking=1, )
    supplier_invoice = fields.Char(string='No. Factura Proveedor', store=True, tracking=0, )
    taclosing_end_date = fields.Date(string='Tax Closing End Date', store=True, copied=True, tracking=0, )
    talock_date_message = fields.Char(string='Mensaje de fecha de bloqueo de impuestos', readonly=True, tracking=0, )
    tareport_control_error = fields.Boolean(string='Tax Report Control Error', store=True, copied=True, tracking=0, )
    ticket_count = fields.Integer(string='Tickets', readonly=True, tracking=0, )
    timesheet_count = fields.Integer(string='Número de partes de tiempo', readonly=True, tracking=0, )
    warn_inactive_certificate = fields.Boolean(string='¿Advertir Sobre el Certificado Inactivo?', readonly=True,
                                               tracking=0, )
    warn_inactive_resolution = fields.Boolean(string='¿Advertir Sobre Resolución Inactiva?', readonly=True, tracking=0, )
    warn_remaining_certificate = fields.Boolean(string='¿Advertir Sobre los Restantes?', readonly=True, tracking=0, )
    warn_remaining = fields.Boolean(string='¿Advertir Sobre lo Restante?', readonly=True, tracking=0, )
    tax_closing_end_date = fields.Date(string='Tax Closing End Date', store=True, copied=True, tracking=0, )
    tax_report_control_error = fields.Boolean(string='Tax Report Control Error', store=True, copied=True, tracking=0, )
    start_date = fields.Date(string='Fecha Inicio Servicio', store=True, copied=True, tracking=1, )


class AccountMoveDianDocument(models.Model):
    _name = 'account.move.dian.document'
    _description = 'Documento DIAN de la Cuenta Mayor'
    ad_zipped_file = fields.Text(string='Archivo Comprimido del AttachedDocument', store=True, copied=True,
                                 tracking=0, )
    ad_zipped_filename = fields.Char(string='Nombre de Archivo Comprimido del AttachedDocument', store=True, copied=True,
                                     tracking=0, )
    application_response_code = fields.Char(string='Application Response Code', store=True, copied=True, tracking=0, )
    ar_xml_file = fields.Text(string='Archivo XML del ApplicationResponse', store=True, copied=True, tracking=0, )
    ar_xml_filename = fields.Char(string='Nombre de archivo XML del ApplicationResponse', store=True, copied=True,
                                  tracking=0, )
    cufe_cude_uncoded = fields.Char(string='CUFE/CUDE Sin Codificar', store=True, copied=True, tracking=0, )
    cufe_cude = fields.Char(string='CUFE/CUDE', store=True, copied=True, tracking=0, )
    get_status_zip_response = fields.Text(string='Respuesta', store=True, copied=True, tracking=0, )
    invoice_url = fields.Char(string='URL de Factura', store=True, copied=True, tracking=0, )
    is_supplier_response = fields.Boolean(string='Is Supplier Response?', store=True, copied=True, tracking=0, )
    mail_sent = fields.Boolean(string='¿Correo Enviado?', store=True, copied=True, tracking=0, )
    qr_image = fields.Text(string='Código QR', readonly=True, tracking=0, )
    software_security_code_uncoded = fields.Char(string='SoftwareSecurityCode Sin Codificar', store=True, copied=True,
                                                 tracking=0, )
    software_security_code = fields.Char(string='SoftwareSecurityCode', store=True, copied=True, tracking=0, )
    validation_datetime = fields.Datetime(string='Fecha y Hora de Validación', store=True, copied=True, tracking=0, )
    xml_file = fields.Text(string='Archivo XML de Factura', store=True, copied=True, tracking=0, )
    xml_filename = fields.Char(string='Nombre de Archivo XML de la Factura', store=True, copied=True, tracking=0, )
    zip_key = fields.Char(string='ZipKey', store=True, copied=True, tracking=0, )
    zipped_file = fields.Text(string='Archivo Comprimido', store=True, copied=True, tracking=0, )
    zipped_filename = fields.Char(string='Nombre de Archivo Comprimido', store=True, copied=True, tracking=0, )


class AccountMoveDianDocumentLine(models.Model):
    _name = 'account.move.dian.document.line'
    _description = 'Línea de Documento DIAN de la Cuenta Mayor'
    send_async_reason = fields.Char(string='Motivo', store=True, copied=True, tracking=0, )
    send_async_response = fields.Text(string='Respuesta', store=True, copied=True, tracking=0, )
    send_async_status_code = fields.Char(string='Código de Estado', store=True, copied=True, tracking=0, )


class AccountMoveDiscrepancyResponseCode(models.Model):
    _name = 'account.move.discrepancy.response.code'
    _description = 'Código de Respuesta de Discrepancia de Cuenta Mayor'
    code = fields.Char(string='Código', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0, )


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    amount_change = fields.Float(string='Diferencia Acumulada', store=True, readonly=True, tracking=0, )
    change_not = fields.Boolean(string='No Diff', store=True, copied=True, tracking=0, )
    cost_price = fields.Float(string='Precio de Coste', store=True, copied=True, tracking=0, )
    diff_amount_divisa = fields.Float(string='Saldo Divisa', store=True, readonly=True, tracking=0, )
    diff_amount_local = fields.Float(string='Saldo Local', store=True, readonly=True, tracking=0, )
    diff_amount_trm = fields.Float(string='TRM', store=True, readonly=True, tracking=0, )
    diff_process = fields.Char(string='Ultimo Proceso', store=True, readonly=True, copied=True, tracking=0, )
    expected_pay_date = fields.Date(string='Fecha esperada de pago', store=True, copied=True, tracking=0, )
    followup_date = fields.Date(string='Seguimiento más reciente', index=True, store=True, tracking=0, )
    hr_ref = fields.Char(string='Referencia RRHH', store=True, tracking=0, )
    internal_note = fields.Text(string='Internal Note', store=True, copied=True, tracking=0, )
    is_landed_costs_line = fields.Boolean(string='Es la línea de costes en destino', store=True, copied=True, tracking=0, )
    next_action_date = fields.Date(string='Next Action Date', store=True, copied=True, tracking=0, )
    not_voucher = fields.Boolean(string='No aplica para pagos y recaudos', store=True, copied=True, tracking=0, )
    purchase_date = fields.Datetime(string='Fecha de Compra', readonly=True, tracking=0, )
    recompute_taline = fields.Boolean(string='Recálculo de líneas de impuestos', readonly=True, copied=True, tracking=0, )
    recoup = fields.Boolean(string='Recobro', store=True, copied=True, tracking=0, )
    ref1 = fields.Char(string='Ref1', store=True, copied=True, tracking=0, )
    ref2 = fields.Char(string='Ref2', store=True, copied=True, tracking=0, )
    reference_price = fields.Float(string='Precio de Referencia', store=True, copied=True, tracking=0, )
    taamount = fields.Float(string='Monto Impuestos', store=True, readonly=True, tracking=0, )
    taaudit = fields.Char(string='Cadena de auditoría fiscal', store=True, readonly=True, tracking=0, )
    taexigible = fields.Boolean(string='Aparece en el informe de impuestos', store=True, readonly=True, copied=True,
                                tracking=0, )
    vat_amount = fields.Float(string='IVA', readonly=True, tracking=0, )
    tax_amount = fields.Float(string='Monto Impuestos', store=True, readonly=True, tracking=0, )
    tax_amount = fields.Float(string='Monto Impuestos', store=True, readonly=True, tracking=0, )
    tax_amount = fields.Float(string='Monto Impuestos', store=True, readonly=True, tracking=0, )
    tax_amount = fields.Float(string='Monto Impuestos', store=True, readonly=True, tracking=0, )
    tax_amount = fields.Float(string='Monto Impuestos', store=True, readonly=True, tracking=0, )

class AccountMoveLinePrint(models.Model):
    _name = 'account.move.line.print'
    _description = 'Impresión de línea de cuenta mayor'
    name = fields.Char(string='Descripcion', store=True, copied=True, tracking=0, )
    quantity = fields.Integer(string='Cantidad', store=True, copied=True, tracking=0, )
    total = fields.Float(string='Monto total', store=True, copied=True, tracking=0, )


class AccountMoveProfile(models.Model):
    _name = 'account.move.profile'
    _description = 'Perfil de Cuenta Mayor'
    adicional = fields.Boolean(string='Costos adicionales', store=True, copied=True, tracking=0, )
    ays = fields.Boolean(string='A&S', store=True, copied=True, tracking=0, )
    city = fields.Boolean(string='Ciudad', store=True, copied=True, tracking=0, )
    detail = fields.Boolean(string='Detalle linea', store=True, copied=True, tracking=0, )
    dias_mes = fields.Boolean(string='Dias del mes', store=True, copied=True, tracking=0, )
    dias_resumen = fields.Boolean(string='Dias resumen', store=True, copied=True, tracking=0, )
    dias = fields.Boolean(string='Dias', store=True, copied=True, tracking=0, )
    distribution = fields.Boolean(string='Distribucion', store=True, copied=True, tracking=0, )
    dom_diur = fields.Boolean(string='Horas dom diurnas', store=True, copied=True, tracking=0, )
    dom_noct = fields.Boolean(string='Horas dom nocturnas', store=True, copied=True, tracking=0, )
    duracion = fields.Boolean(string='Duracion', store=True, copied=True, tracking=0, )
    fes_diur = fields.Boolean(string='Horas fes diurnas', store=True, copied=True, tracking=0, )
    fes_noct = fields.Boolean(string='Horas fes nocturnas', store=True, copied=True, tracking=0, )
    horario = fields.Boolean(string='Horario', store=True, copied=True, tracking=0, )
    horas_diurno = fields.Boolean(string='Horas diurno', store=True, copied=True, tracking=0, )
    horas_nocturno = fields.Boolean(string='Horas nocturnas', store=True, copied=True, tracking=0, )
    interventor = fields.Boolean(string='Interventor', store=True, copied=True, tracking=0, )
    medio = fields.Boolean(string='Medio', store=True, copied=True, tracking=0, )
    mod_servicio = fields.Boolean(string='Linea de negocio', store=True, copied=True, tracking=0, )
    modalidad = fields.Boolean(string='Modalidad', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Perfil', store=True, copied=True, tracking=0, )
    programacion = fields.Boolean(string='Programacion', store=True, copied=True, tracking=0, )
    puesto_int_code = fields.Boolean(string='Codigo interno cliente', store=True, copied=True, tracking=0, )
    puesto_int_zone = fields.Boolean(string='Zona interna cliente', store=True, copied=True, tracking=0, )
    puesto = fields.Boolean(string='Puesto', store=True, copied=True, tracking=0, )
    quantity = fields.Boolean(string='Cantidad', store=True, copied=True, tracking=0, )
    regional = fields.Boolean(string='Regional', store=True, copied=True, tracking=0, )
    service_quantity = fields.Boolean(string='# Serv', store=True, copied=True, tracking=0, )
    subtotal = fields.Boolean(string='Subtotal antes de A&S', store=True, copied=True, tracking=0, )
    tipo_servicio = fields.Boolean(string='Tipo de servicio', store=True, copied=True, tracking=0, )
    total_ays = fields.Boolean(string='Total A&S', store=True, copied=True, tracking=0, )
    total_validated = fields.Boolean(string='Total validado', store=True, copied=True, tracking=0, )
    total = fields.Boolean(string='Total general', store=True, copied=True, tracking=0, )
    valor_total = fields.Boolean(string='Valor total', store=True, copied=True, tracking=0, )
    valor = fields.Boolean(string='Valor antes de A&S', store=True, copied=True, tracking=0, )


class AccountMoveProjectOrderLine(models.Model):
    _name = 'account.move.project.order.line'
    _description = 'Línea de Pedido de Proyecto de Cuenta Mayor'
    end_date = fields.Date(string='Fecha fin de facturación', store=True, readonly=True, required=True, copied=True,
                           tracking=0, )
    invoice_date = fields.Date(string='Fecha de factura', index=True, store=True, readonly=True, tracking=0, )
    start_date = fields.Date(string='Fecha inicio de facturación', store=True, readonly=True, required=True, copied=True,
                             tracking=0, )


class AccountMoveRecoup(models.Model):
    _name = 'account.move.recoup'
    _description = 'Recobro de Cuenta Mayor'
    invoices = fields.Text(string='Facturas por agrupar', store=True, readonly=True, copied=True, tracking=0, )


class AccountMoveRecoupLine(models.Model):
    _name = 'account.move.recoup.line'
    _description = 'Línea de Recobro de Cuenta Mayor'
    description = fields.Text(string='Descripción', store=True, copied=True, tracking=0, )
    taadd = fields.Boolean(string='Añadir impuestos', store=True, copied=True, tracking=0, )
    tax_add = fields.Boolean(string='Añadir impuestos', store=True, copied=True, tracking=0, )


class AccountMoveSummaryLine(models.Model):
    _name = 'account.move.summary.line'
    _description = 'Línea Resumen de Cuenta Mayor'
    cost_price = fields.Float(string='Precio de Coste', store=True, copied=True, tracking=0, )
    discount = fields.Float(string='Descuento (%)', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Etiqueta', store=True, copied=True, tracking=100, )
    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0, )
    quantity = fields.Float(string='Cantidad', store=True, copied=True, tracking=0, )
    reference_price = fields.Float(string='Precio de Referencia', store=True, copied=True, tracking=0, )


class AccountMoveTax(models.Model):
    _name = 'account.move.tax'
    _description = 'Impuesto de Cuenta Mayor'
    credit = fields.Float(string='Credito', store=True, copied=True, tracking=0, )
    debit = fields.Float(string='Debito', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Descripción', store=True, copied=True, tracking=0, )
    tabase_amount = fields.Float(string='Importe Base', store=True, copied=True, tracking=0, )
    tax_base_amount = fields.Float(string='Importe Base', store=True, copied=True, tracking=0, )

class AccountMulticurrencyRevaluation(models.Model):
    _name = 'account.multicurrency.revaluation'
    _description = 'Revaluación Multimoneda'
    account_code = fields.Char(string='Account Code', store=True, copied=True, tracking=0, )
    account_name = fields.Char(string='Account Name', store=True, copied=True, tracking=0, )
    currency_code = fields.Char(string='Currency Code', store=True, copied=True, tracking=0, )
    date = fields.Date(string='Date', store=True, copied=True, tracking=0, )
    display_type = fields.Char(string='Display Type', store=True, copied=True, tracking=0, )
    move_name = fields.Char(string='Move Name', store=True, copied=True, tracking=0, )
    move_ref = fields.Char(string='Move Ref', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Name', store=True, copied=True, tracking=0, )
    report_include = fields.Boolean(string='Report Include', store=True, copied=True, tracking=0, )


class AccountMulticurrencyRevaluationWizard(models.Model):
    _name = 'account.multicurrency.revaluation.wizard'
    date = fields.Date(string='Date', store=True, required=True, copied=True, tracking=0, )
    preview_data = fields.Text(string='Preview Data', readonly=True, tracking=0, )
    reversal_date = fields.Date(string='Reversal Date', store=True, required=True, copied=True, tracking=0, )


class AccountPartialReconcile(models.Model):
    _inherit = 'account.partial.reconcile'
    madate = fields.Date(string='Fecha máxima de lineas asociadas', store=True, readonly=True, tracking=0, )


class GrupoDeImpuestos(models.Model):
    _name = 'account.tax.group'
    _description = 'Grupo deI mpuestos'

    name = fields.Char(string="Nombre", required=True, store=True, copied=True)
    display_report = fields.Boolean(string='Imprimir en Representación Gráfica', store=True, copied=True, tracking=0, )
    is_einvoicing = fields.Boolean(string='¿Aplica para la Facturación Electrónica?', store=True, copied=True,
                                   tracking=0, )
    sequence = fields.Integer(string="Secuencia", default=10, index=True)




class AccountTaxGroupType(models.Model):
    _name = 'account.tax.group.type'
    _description = 'Account Tax Group Type'

    code = fields.Char(string='Código', store=True, required=True, copied=True, tracking=0, )
    description = fields.Char(string='Descripción', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )


class AccountPayment(models.Model):
    _inherit = 'account.payment'
    accepted_rejected_datetime = fields.Datetime(string='Fecha y Hora de Aceptado/Rechazado', tracking=0, )
    allow_draft_delete = fields.Boolean(string='Eliminar en borrador', copied=True, tracking=0, )
    amount_to_text = fields.Char(string='Monto en letras', copied=True, tracking=0, )
    bank_account_required = fields.Boolean(string='Cuenta bancaria requerida', readonly=True, tracking=0, )
    date_of_service = fields.Date(string='Fecha de servicio', copied=True, tracking=0, )
    dbname = fields.Char(string='Nombre de la BD', readonly=True, tracking=0, )
    debit_note_count = fields.Integer(string='Numero de Notas Débito', readonly=True, tracking=0, )
    delivery_datetime = fields.Datetime(string='Fecha y Hora de Entrega', tracking=0, )
    e_invoice_cufe = fields.Char(string='E-Invoice Cufe', tracking=0, )
    e_invoice_reference = fields.Char(string='E-Invoice Reference', tracking=0, )
    ei_app_response = fields.Text(string='Contenido XML Application Response', tracking=0, )
    ei_cude = fields.Char(string='CUDE', readonly=True, tracking=100, )
    ei_cufe = fields.Char(string='CUFE', readonly=True, tracking=100, )
    ei_email_sent = fields.Boolean(string='Email Enviado', tracking=0, )
    ei_generation_date = fields.Char(string='Hora de Generación', readonly=True, tracking=0, )
    ei_qr = fields.Char(string='Informacion QR', readonly=True, tracking=0, )
    ei_validation_date = fields.Char(string='Hora de Validacion', readonly=True, tracking=0, )
    ei_xml_content = fields.Text(string='Contenido XML', tracking=0, )
    end_date = fields.Date(string='Fecha fin', copied=True, tracking=0, )
    invoice_datetime = fields.Datetime(string='Fecha y Hora de la Factura', tracking=0, )
    invoice_reference = fields.Char(string='No. Orden / Referencia', copied=True, tracking=0, )
    invoice_type_code_attrs = fields.Boolean(string='Invoice Type Code Attrs', readonly=True, tracking=0, )
    is_a_claim = fields.Boolean(string='Is a Claim?', tracking=0, )
    is_accepted_rejected = fields.Boolean(string='¿Esta Aceptada/Rechazada?', tracking=0, )
    landed_costs_visible = fields.Boolean(string='Costes en destino visibles', readonly=True, tracking=0, )
    manual_tax = fields.Boolean(string='Ingresar Manualmente los impuestos', copied=True, tracking=0, )
    merge_with_sale_order = fields.Boolean(string='¿Combinar con Pedido de Venta?', readonly=True, tracking=0, )
    move_name = fields.Char(string='Forzar número', tracking=0, )
    move_state_note = fields.Text(string='Nota de Estado', copied=True, tracking=0, )
    payment_date = fields.Date(string='Fecha del pago', readonly=True, tracking=0, )
    payment_mode_filter_type_domain = fields.Char(string='Payment Mode Filter Type Domain', readonly=True, tracking=0, )
    payment_order_ok = fields.Boolean(string='Orden de Pago correcta', readonly=True, tracking=0, )
    payment_state_before_switch = fields.Char(string='Payment State Before Switch', tracking=0, )
    receipt_document_reference = fields.Char(string='Documento de recibo de mercancía / servicio', tracking=0, )
    recoup = fields.Boolean(string='Recobro', copied=True, tracking=0, )
    ref_description = fields.Char(string='Referencia / Descripción', copied=True, tracking=0, )
    reference_date = fields.Date(string='Fecha de Referencia', copied=True, tracking=0, )
    reference_id = fields.Char(string='CUFE de Referencia', copied=True, tracking=0, )
    reference_uuid = fields.Char(string='Número de Referencia', copied=True, tracking=0, )
    start_date = fields.Date(string='Fecha de inicio', copied=True, tracking=0, )
    start_date = fields.Date(string='Fecha Inicio Servicio', copied=True, tracking=1, )
    supplier_invoice = fields.Char(string='No. Factura Proveedor', tracking=0, )
    taclosing_end_date = fields.Date(string='Tax Closing End Date', copied=True, tracking=0, )
    talock_date_message = fields.Char(string='Mensaje de fecha de bloqueo de impuestos', readonly=True, tracking=0, )
    tareport_control_error = fields.Boolean(string='Tax Report Control Error', copied=True, tracking=0, )
    ticket_count = fields.Integer(string='Tickets', readonly=True, tracking=0, )
    timesheet_count = fields.Integer(string='Número de partes de tiempo', readonly=True, tracking=0, )
    total_rows = fields.Integer(string='Rowspan Dinámico', copied=True, tracking=1, )
    warn_inactive_certificate = fields.Boolean(string='¿Advertir Sobre el Certificado Inactivo?', readonly=True,
                                               tracking=0, )
    warn_inactive_resolution = fields.Boolean(string='¿Advertir Sobre Resolución Inactiva?', readonly=True, tracking=0, )
    warn_remaining_certificate = fields.Boolean(string='¿Advertir Sobre los Restantes?', readonly=True, tracking=0, )
    warn_remaining = fields.Boolean(string='¿Advertir Sobre lo Restante?', readonly=True, tracking=0, )
    tax_closing_end_date = fields.Date(string='Tax Closing End Date', copied=True, tracking=0, )
    tax_report_control_error = fields.Boolean(string='Tax Report Control Error', copied=True, tracking=0, )
    start_date = fields.Date(string='Fecha Inicio Servicio', copied=True, tracking=1, )
    total_rows = fields.Integer(string='Rowspan Dinámico', copied=True, tracking=1, )


class AccountPaymentConfigLine(models.Model):
    _name = 'account.payment.config.line'
    _description = 'Línea de Configuración de Pago'
    adjust = fields.Boolean(string='Ajuste a tamaño', store=True, copied=True, tracking=0, )
    advance_content = fields.Text(string='Contenido - Anticipos', store=True, copied=True, tracking=0, )
    content = fields.Text(string='Contenido', store=True, copied=True, tracking=0, )
    decimal_qty = fields.Integer(string='Número de decimales', store=True, copied=True, tracking=0, )
    fill = fields.Char(string='Caracter de relleno', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0, )
    size = fields.Integer(string='Tamaño', store=True, copied=True, tracking=0, )


class AccountPaymentFileConfig(models.Model):
    _name = 'account.payment.file.config'
    _description = 'Configuración de archivo de pago'
    footer = fields.Boolean(string='Footer instead header', store=True, copied=True, tracking=0, )


class AccountPaymentLine(models.Model):
    _name = 'account.payment.line'
    _description = 'Línea de Pago'
    amount_to_text = fields.Char(string='Monto en letras', readonly=True, tracking=0, )
    bank_account_required = fields.Boolean(string='Cuenta bancaria requerida', readonly=True, tracking=0, )
    communication = fields.Char(string='Comunicación', store=True, required=True, copied=True, tracking=0, )
    date = fields.Date(string='Fecha de pago', store=True, copied=True, tracking=0, )
    ml_maturity_date = fields.Date(string='Fecha de vencimiento', readonly=True, tracking=0, )
    name = fields.Char(string='Referencia de pago', store=True, readonly=True, tracking=0, )
    numero_cheque = fields.Char(string='Numero de Cheque', store=True, copied=True, tracking=0, )


class AccountPaymentLineCreate(models.Model):
    _name = 'account.payment.line.create'
    _description = 'Crear línea de pago'
    allow_blocked = fields.Boolean(string='Permitir apuntes en litigio', store=True, copied=True, tracking=0, )
    due_date = fields.Date(string='Fecha de vencimiento', store=True, copied=True, tracking=0, )
    invoice = fields.Boolean(string='Vinculado a una factura o factura rectificativa', store=True, copied=True,
                             tracking=0, )
    move_date = fields.Date(string='Fecha del asiento', store=True, copied=True, tracking=0, )


class AccountPaymentMean(models.Model):
    _name = 'account.payment.mean'
    _description = 'Medio de Pago'
    code = fields.Char(string='Código', store=True, required=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )


class AccountPaymentMeanCode(models.Model):
    _name = 'account.payment.mean.code'
    _description = 'Código de Medio de Pago'
    code = fields.Char(string='Código', store=True, required=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )


class AccountPaymentMethod(models.Model):
    _inherit = 'account.payment.method'
    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0, )
    bank_account_required = fields.Boolean(string='Cuenta bancaria requerida', store=True, copied=True, tracking=0, )
    payment_order_only = fields.Boolean(string='Opciones para las órdenes', store=True, copied=True, tracking=0, )


class AccountPaymentMode(models.Model):
    _name = 'account.payment.mode'
    _description = 'Modo de Pago'
    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0, )
    default_invoice = fields.Boolean(string='Vinculado a una factura o factura rectificativa', store=True, copied=True,
                                     tracking=0, )
    generate_move = fields.Boolean(string='Generar asientos contables al subir el archivo', store=True, copied=True,
                                   tracking=0, )
    group_lines = fields.Boolean(string='Agrupar transacciones en las órdenes de pago', store=True, copied=True,
                                 tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )
    no_debit_before_maturity = fields.Boolean(string='No permitir el adeudo antes de la fecha de vencimiento', store=True,
                                              copied=True, tracking=0, )
    note = fields.Text(string='Nota', store=True, copied=True, tracking=0, )
    payment_method_code = fields.Char(string='Code (Do Not Modify)', store=True, readonly=True, tracking=0, )
    payment_order_ok = fields.Boolean(string='Seleccionable en las órdenes', store=True, copied=True, tracking=0, )
    post_move = fields.Boolean(string='Publicar movimiento', store=True, copied=True, tracking=0, )
    show_bank_account_chars = fields.Integer(string='Nº de dígitos de cuenta bancaria del cliente', store=True, copied=True,
                                             tracking=0, )
    show_bank_account_from_journal = fields.Boolean(string='Cuenta bancaria de los diarios', store=True, copied=True,
                                                    tracking=0, )


class AccountPaymentOrder(models.Model):
    _name = 'account.payment.order'
    _description = 'Orden de Pago'

    bank_line_count = fields.Integer(string='Número de líneas bancarias', readonly=True, tracking=0, )
    cheque = fields.Char(string='Cheque', store=True, copied=True, tracking=100, )
    date_done = fields.Date(string='Fecha de realización', store=True, readonly=True, copied=True, tracking=0, )
    date_generated = fields.Date(string='Fecha del fichero generado', store=True, readonly=True, copied=True, tracking=0, )
    date_scheduled = fields.Date(string='Fecha de ejecución del pago', store=True, readonly=True, copied=True,
                                 tracking=100, )
    date_uploaded = fields.Date(string='Fecha de subida del fichero', store=True, readonly=True, copied=True, tracking=0, )
    description = fields.Char(string='Descripción', store=True, copied=True, tracking=0, )
    file_name = fields.Char(string='Archivo Pago Banco', store=True, readonly=True, copied=True, tracking=100, )
    file_text = fields.Text(string='Archivo Pago Banco', store=True, readonly=True, copied=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Adjuntos', readonly=True, tracking=0, )
    message_has_error_counter = fields.Integer(string='Número de líneas bancarias', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Error de Envío de Mensaje', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='Error de entrega del SMS', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Es un seguidor', readonly=True, tracking=0, )
    message_needaction_counter = fields.Integer(string='Número de líneas bancarias', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Acción requerida', readonly=True, tracking=0, )
    message_unread_counter = fields.Integer(string='Contador de mensajes sin leer', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Mensajes sin leer', readonly=True, tracking=0, )
    move_name = fields.Char(string='Nombre Comprobante', store=True, readonly=True, copied=True, tracking=0, )
    name = fields.Char(string='Número', store=True, readonly=True, tracking=0, )
    narration = fields.Text(string='Notes', store=True, readonly=True, copied=True, tracking=0, )
    payment_order_date = fields.Date(string='Fecha de Pago', store=True, readonly=True, required=True, copied=True,
                                     tracking=0, )
    time_of_process = fields.Datetime(string='Fecha Transmision', store=True, readonly=True, copied=True, tracking=0, )


class AccountPaymentTerm(models.Model):
    _inherit = 'account.payment.term'
    finantial_cost = fields.Float(string='Costo Financiero', store=True, copied=True, tracking=0, )


class AccountReconcileModelLine(models.Model):
    _inherit = 'account.reconcile.model.line'
    force_taincluded = fields.Boolean(string='Impuesto incluido en el precio', store=True, copied=True, tracking=0, )
    show_force_taincluded = fields.Boolean(string='Mostrar Forzar Impuestos Incluidos', readonly=True, tracking=0, )


class AccountReconcileModelLineTemplate(models.Model):
    _inherit = 'account.reconcile.model.line.template'
    force_taincluded = fields.Boolean(string='Impuesto incluido en el precio', store=True, copied=True, tracking=0, )


class AccountReportFootnote(models.Model):
    _name = 'account.report.footnote'
    _description = 'Nota al pie del informe contable'
    line = fields.Char(string='Line', index=True, store=True, copied=True, tracking=0, )
    text = fields.Char(string='Text', store=True, copied=True, tracking=0, )


class AccountReportManager(models.Model):
    _name = 'account.report.manager'
    report_name = fields.Char(string='Report Name', store=True, required=True, copied=True, tracking=0, )
    summary = fields.Char(string='Summary', store=True, copied=True, tracking=0, )


class AccountSetupBankManualConfig(models.TransientModel):
    _inherit = 'account.setup.bank.manual.config'
    cupo_endeudamiento = fields.Float(string='Cupo de endeudamiento', copied=True, tracking=0, )
    date_renovacion = fields.Date(string='Fecha de renovacion de cupo', copied=True, tracking=0, )
    oficina_nombre = fields.Char(string='Nombre de la oficina', copied=True, tracking=0, )


class AccountSuppierPaymentWizard(models.Model):
    _name = 'account.suppier.payment.wizard'
    _description = 'Asistente de pago al proveedor'
    date_order = fields.Datetime(string='Order Date', store=True, required=True, copied=True, tracking=0, )
    file_text = fields.Text(string='Archivo Pago Banco', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Archivo Pago Banco', store=True, copied=True, tracking=0, )


class AccountTagroup(models.Model):
    _name = 'account.tagroup'
    _description = 'Grupo de Etiquetas'
    display_report = fields.Boolean(string='Imprimir en Representación Gráfica', store=True, copied=True, tracking=0, )
    is_einvoicing = fields.Boolean(string='¿Aplica para la Facturación Electrónica?', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0, )


class AccountTagroupType(models.Model):
    _name = 'account.tagroup.type'
    _description = 'Tipo de Grupo de Etiquetas'
    code = fields.Char(string='Código', store=True, required=True, copied=True, tracking=0, )
    description = fields.Char(string='Descripción', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )


class AccountTarepartitionLine(models.Model):
    _name = 'account.tarepartition.line'
    _description = 'Línea de Reparto de Impuestos'
    factor_percent = fields.Float(string='%', store=True, required=True, copied=True, tracking=0, )
    factor = fields.Float(string='Proporción de Factor', readonly=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0, )
    use_in_taclosing = fields.Boolean(string='Entrada de cierre de impuestos', store=True, copied=True, tracking=0, )


class AccountTarepartitionLineTemplate(models.Model):
    _name = 'account.tarepartition.line.template'
    _description = 'Línea de Plantilla de Reparto de Impuestos'
    factor_percent = fields.Float(string='%', store=True, required=True, copied=True, tracking=0, )
    use_in_taclosing = fields.Boolean(string='Entrada de cierre de impuestos', store=True, copied=True, tracking=0, )


class AccountTareport(models.Model):
    _name = 'account.tareport'
    _description = 'Informe de Impuestos'
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )


class AccountTareportLine(models.Model):
    _name = 'account.tareport.line'
    _description = 'Línea de Informe de Impuestos'
    code = fields.Char(string='Código', store=True, copied=True, tracking=0, )
    formula = fields.Char(string='Fórmula', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )
    parent_path = fields.Char(string='Ruta padre', index=True, store=True, copied=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, required=True, copied=True, tracking=0, )
    tag_name = fields.Char(string='Nombre de etiqueta', store=True, copied=True, tracking=0, )


class AccountTatemplate(models.Model):
    _name = 'account.tatemplate'
    _description = 'Plantilla de Impuestos'
    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0, )
    amount = fields.Float(string='Importe', store=True, required=True, copied=True, tracking=0, )
    analytic = fields.Boolean(string='Analítica de costes', store=True, copied=True, tracking=0, )
    description = fields.Char(string='Mostrar en facturas', store=True, copied=True, tracking=0, )
    include_base_amount = fields.Boolean(string='Impuestos subsiguientes aplicados', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre del impuesto', store=True, required=True, copied=True, tracking=0, )
    price_include = fields.Boolean(string='Incluir en el precio', store=True, copied=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', store=True, required=True, copied=True, tracking=0, )


class AccountTax(models.Model):
    _inherit = 'account.tax'
    aiu_tax = fields.Boolean(string='Impuesto AIU', store=True, copied=True, tracking=0, )
    check_lines = fields.Boolean(string='Impuesto ICA', store=True, copied=True, tracking=0, )
    hide_taexigibility = fields.Boolean(string='Ocultar opción de base de efectivo', readonly=True, tracking=0, )


class AccountTourUploadBill(models.TransientModel):
    _inherit = 'account.tour.upload.bill'
    body_str = fields.Html(string='Cuerpo', copied=True, tracking=0, )
    is_wp = fields.Boolean(string='WhatsApp?', copied=True, tracking=0, )


class AccountVoucher(models.Model):
    _name = 'account.voucher'
    _description = 'Comprobante de Pago'
    access_token = fields.Char(string='Token de seguridad', store=True, tracking=0, )
    access_url = fields.Char(string='URL de acceso al portal', readonly=True, tracking=0, )
    access_warning = fields.Text(string='Advertencia de acceso', readonly=True, tracking=0, )
    activity_date_deadline = fields.Date(string='Siguiente plazo de actividad', readonly=True, tracking=0, )
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0, )
    activity_summary = fields.Char(string='Resumen de la siguiente actividad', tracking=0, )
    activity_type_icon = fields.Char(string='Ícono de tipo de actvidad', readonly=True, tracking=0, )
    audit = fields.Boolean(string='Por Revisar', store=True, copied=True, tracking=100, )
    authorization = fields.Char(string='Autorización', store=True, tracking=100, )
    compensation_customer = fields.Boolean(string='Pago de compensación', store=True, copied=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, required=True, tracking=0, )
    exchange_rate = fields.Float(string='Tasa de conversión', store=True, copied=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Nº de archivos adjuntos', readonly=True, tracking=0, )
    message_has_error_counter = fields.Integer(string='Numero de errores', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Error de Envío de Mensaje', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Es un seguidor', readonly=True, tracking=0, )
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Acción requerida', readonly=True, tracking=0, )
    message_unread_counter = fields.Integer(string='Nº de mensajes sin leer', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Mensajes sin leer', readonly=True, tracking=0, )
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0, )
    number = fields.Char(string='Numero', store=True, copied=True, tracking=100, )
    reference = fields.Char(string='Ref. Pago', store=True, copied=True, tracking=100, )
    voucher_date = fields.Date(string='Fecha del Pago', store=True, tracking=0, )
    voucher_reference = fields.Char(string='Referencia del Pago', store=True, tracking=0, )
    writeoff_comment = fields.Char(string='Comentario de la contrapartida', store=True, copied=True, tracking=0, )


class AccountVoucherLine(models.Model):
    _name = 'account.voucher.line'
    _description = 'Línea de Comprobante de Pago'
    comment = fields.Char(string='Comentario de la contrapartida', store=True, copied=True, tracking=0, )
    date_due = fields.Date(string='Fecha de Vencimiento', readonly=True, tracking=0, )
    date_original = fields.Date(string='Fecha', readonly=True, tracking=0, )
    date = fields.Date(string='Date', readonly=True, tracking=0, )
    name = fields.Char(string='Descripción', store=True, copied=True, tracking=0, )
    reconcile = fields.Boolean(string='Reconciliación total', store=True, copied=True, tracking=0, )
    amount = fields.Float(string='Valor', store=True, copied=True, tracking=0, )
    amount_original = fields.Float(string='Cantidad original', store=True, readonly=True, tracking=0, )
    amount_unreconciled = fields.Float(string='Saldo abierto', store=True, readonly=True, tracking=0, )
    amount_untax = fields.Float(string='Importe base', store=True, copied=True, tracking=0, )





class AccountVoucherWizard(models.Model):
    _name = 'account.voucher.wizard'
    _description = 'Asistente de Comprobante de Pago'
    active_bool = fields.Boolean(string='Muchos', store=True, copied=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, required=True, copied=True, tracking=0, )
    voucher_reference = fields.Char(string='Referencia del Pago', store=True, copied=True, tracking=0, )


class AcreditacionTipo(models.Model):
    _name = 'acreditacion.tipo'
    _description = 'Tipo de Acreditación'
    cargo_codigo = fields.Char(string='Cargo código', store=True, required=True, copied=True, tracking=0, )
    codigo = fields.Char(string='Código', store=True, required=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )


class ActivosPuestoWiz(models.Model):
    _name = 'activos.puesto.wiz'
    _description = 'Asistente de Puesto de Activos'
    tipo = fields.Char(string='Tipo de operacion permitido', readonly=True, tracking=0, )
    val_asign = fields.Boolean(string='Confirmar asignacion', store=True, copied=True, tracking=0, )
    val_desv = fields.Boolean(string='Desvincular activo', store=True, copied=True, tracking=0, )
    val_transf = fields.Boolean(string='Confirmar transferencia', store=True, copied=True, tracking=0, )


class AgedPartnerBalanceReportWizard(models.Model):
    _name = 'aged.partner.balance.report.wizard'
    _description = 'Asistente de Informe de Saldo Antigüo de Socios'
    date_at = fields.Date(string='Fecha a', store=True, required=True, copied=True, tracking=0, )
    date_from = fields.Date(string='Fecha de inicio', store=True, copied=True, tracking=0, )
    payable_accounts_only = fields.Boolean(string='Sólo cuentas a pagar', store=True, copied=True, tracking=0, )
    receivable_accounts_only = fields.Boolean(string='Sólo cuentas a cobrar', store=True, copied=True, tracking=0, )
    show_move_line_details = fields.Boolean(string='Mostrar Detalles Apuntes', store=True, copied=True, tracking=0, )


class ApFileSequence(models.Model):
    _name = 'ap.file.sequence'
    _description = 'Secuencia de Archivo AP'
    date = fields.Date(string='Fecha', store=True, required=True, copied=True, tracking=0, )
    sequence_number = fields.Integer(string='Número de Secuencia', store=True, required=True, copied=True, tracking=0, )


class AsignacionCelular(models.Model):
    _name = 'asignacion.celular'
    _description = 'Asignación de Celular'
    es_editable = fields.Boolean(string='Es Editable', store=True, tracking=1, )
    fecha_transaccion = fields.Datetime(string='Fecha', store=True, copied=True, tracking=1, )
    name = fields.Char(string='Name', store=True, copied=True, tracking=1, )
    puesto = fields.Char(string='Puesto', store=True, copied=True, tracking=1, )

class AuditAction(models.Model):
    _name = 'audit.action'
    _description = 'Acción de Auditoría'
    date_end = fields.Datetime(string='Fecha Limite', store=True, required=True, copied=True, tracking=0, )
    description = fields.Text(string='Descripcion', store=True, required=True, copied=True, tracking=0, )
    enviado = fields.Boolean(string='Notificacion Mail Enviada', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )


class AuditAudit(models.Model):
    _name = 'audit.audit'
    _description = 'Auditoría'
    conclusiones = fields.Text(string='Conclusion', store=True, copied=True, tracking=0, )
    conformidad = fields.Float(string='Conformidad(%)', store=True, readonly=True, tracking=0, )
    date_end_planning = fields.Datetime(string='Fecha Final Planificada', store=True, required=True, copied=True,
                                        tracking=0, )
    date_end = fields.Datetime(string='Fecha Final Ejecutada', store=True, copied=True, tracking=0, )
    date_start_planning = fields.Datetime(string='Fecha Inicial Planificada', store=True, required=True, copied=True,
                                          tracking=0, )
    date_start = fields.Datetime(string='Fecha Inicial Ejecutada', store=True, copied=True, tracking=0, )
    duracion = fields.Float(string='Duracion(horas)', store=True, readonly=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )
    observaciones = fields.Text(string='Observaciones y Recomendaciones', store=True, copied=True, tracking=0, )
    period = fields.Char(string='Periodo de Rastreo', store=True, copied=True, tracking=0, )
    reference = fields.Char(string='Codigo', store=True, readonly=True, copied=True, tracking=0, )


class AuditCause(models.Model):
    _name = 'audit.cause'
    _description = 'Causa de Auditoría'
    description = fields.Text(string='Descripcion', store=True, required=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )


class AuditCauseClasification(models.Model):
    _name = 'audit.cause.clasification'
    _description = 'Clasificación de Causa de Auditoría'
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )


class AuditEvaluation(models.Model):
    _name = 'audit.evaluation'
    _description = 'Evaluación de Auditoría'
    date_evaluation = fields.Datetime(string='Fecha de Evaluacion', store=True, required=True, copied=True,
                                      tracking=0, )
    description = fields.Text(string='Descripcion', store=True, required=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )


class AuditIndicator(models.Model):
    _name = 'audit.indicator'
    _description = 'Indicador de Auditoría'
    definicion = fields.Text(string='Definicion', store=True, required=True, copied=True, tracking=0, )
    formula = fields.Char(string='Formula de Calculo', store=True, required=True, copied=True, tracking=0, )
    frecuencia_r = fields.Float(string='Frecuencia Recoleccion', store=True, required=True, copied=True, tracking=0, )
    frecuencia_s = fields.Float(string='Frecuencia Revision', store=True, required=True, copied=True, tracking=0, )
    fuente_info = fields.Text(string='Fuente de la Informacion', store=True, required=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )
    object_specific = fields.Char(string='Objetivo Especifico', store=True, required=True, copied=True, tracking=0, )
    objectivo = fields.Text(string='Objetivo', store=True, required=True, copied=True, tracking=0, )
    observaciones = fields.Text(string='Observaciones', store=True, copied=True, tracking=0, )


class AuditIndicatorRango(models.Model):
    _name = 'audit.indicator.rango'
    _description = 'Rango de Indicador de Auditoría'
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )
    rang_inf = fields.Float(string='Rango Inferior', store=True, required=True, copied=True, tracking=0, )
    rang_sup = fields.Float(string='Rango Supeior', store=True, required=True, copied=True, tracking=0, )


class AuditIndicatorResult(models.Model):
    _name = 'audit.indicator.result'
    _description = 'Resultado de Indicador de Auditoría'
    analysis = fields.Text(string='Analisis', store=True, copied=True, tracking=0, )
    date = fields.Date(string='Fecha Analisis', store=True, required=True, copied=True, tracking=0, )
    indicator_name = fields.Char(string='Nombre indicador', readonly=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    name = fields.Float(string='Resultado', store=True, required=True, copied=True, tracking=0, )


class AuditIndicatorType(models.Model):
    _name = 'audit.indicator.type'
    _description = 'Tipo de Indicador de Auditoría'
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )


class AuditList(models.Model):
    _name  = 'audit.list'
    _description = 'Lista de Auditoría'
    hallazgo = fields.Text(string='Hallazgo', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Numeral', store=True, required=True, copied=True, tracking=0, )
    pregunta = fields.Char(string='Aspecto a examinar', store=True, required=True, copied=True, tracking=0, )


class AuditlogHttpRequest(models.Model):
    _name = 'auditlog.http.request'
    _description = 'Solicitud HTTP de Auditoría'
    name = fields.Char(string='Ruta', store=True, copied=True, tracking=0, )
    root_url = fields.Char(string='URL raíz', store=True, copied=True, tracking=0, )
    user_context = fields.Char(string='Contexto', store=True, copied=True, tracking=0, )


class AuditlogHttpSession(models.Model):
    _name = 'auditlog.http.session'
    _description = 'Sesión HTTP de Auditoría'
    name = fields.Char(string='ID de sesión', index=True, store=True, copied=True, tracking=0, )


class AuditlogLog(models.Model):
    _name = 'auditlog.log'
    _description = 'Registro de Auditoría'
    method = fields.Char(string='Método', store=True, copied=True, tracking=0, )
    model_model = fields.Char(string='Technical Model Name', store=True, readonly=True, copied=True, tracking=0, )
    model_name = fields.Char(string='Model Name', store=True, readonly=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre del recurso', store=True, copied=True, tracking=0, )
    res_id = fields.Integer(string='ID del recurso', store=True, copied=True, tracking=0, )


class AuditlogLogLine(models.Model):
    _name = 'auditlog.log.line'
    _description = 'Línea de Registro de Auditoría'
    field_description = fields.Char(string='Descripción', store=True, readonly=True, copied=True, tracking=0, )
    field_name = fields.Char(string='Nombre técnico', store=True, readonly=True, copied=True, tracking=0, )
    new_value_text = fields.Text(string='Text del valor nuevo', store=True, copied=True, tracking=0, )
    new_value = fields.Text(string='Valor nuevo', store=True, copied=True, tracking=0, )
    old_value_text = fields.Text(string='Text del valor anterior', store=True, copied=True, tracking=0, )
    old_value = fields.Text(string='Valor anterior', store=True, copied=True, tracking=0, )


class AuditlogLogLineView(models.Model):
    _name = 'auditlog.log.line.view'
    _description = 'Vista de Línea de Registro de Auditoría'
    field_description = fields.Char(string='Descripción', store=True, readonly=True, copied=True, tracking=0, )
    field_name = fields.Char(string='Nombre técnico', store=True, readonly=True, copied=True, tracking=0, )
    method = fields.Char(string='Método', store=True, copied=True, tracking=0, )
    model_model = fields.Char(string='Model Model', store=True, copied=True, tracking=0, )
    model_name = fields.Char(string='Model Name', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0, )
    new_value_text = fields.Text(string='Text del valor nuevo', store=True, copied=True, tracking=0, )
    new_value = fields.Text(string='Valor nuevo', store=True, copied=True, tracking=0, )
    old_value_text = fields.Text(string='Text del valor anterior', store=True, copied=True, tracking=0, )
    old_value = fields.Text(string='Valor anterior', store=True, copied=True, tracking=0, )
    res_id = fields.Integer(string='Res', store=True, copied=True, tracking=0, )


class AuditlogRule(models.Model):
    _name = 'auditlog.rule'
    _description = 'Regla de Auditoría'
    capture_record = fields.Boolean(string='Capture Record', store=True, copied=True, tracking=0, )
    log_create = fields.Boolean(string='Crear registros', store=True, copied=True, tracking=0, )
    log_read = fields.Boolean(string='Registrar lecturas', store=True, copied=True, tracking=0, )
    log_unlink = fields.Boolean(string='Borrar registros', store=True, copied=True, tracking=0, )
    log_write = fields.Boolean(string='Registrar modificaciones', store=True, copied=True, tracking=0, )
    model_model = fields.Char(string='Technical Model Name', store=True, readonly=True, copied=True, tracking=0, )
    model_name = fields.Char(string='Model Name', store=True, readonly=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )


class AuditNonconformity(models.Model):
    _name = 'audit.nonconformity'
    _description = 'No Conformidad de Auditoría'
    cause = fields.Text(string='Causa Raiz', store=True, tracking=0, )
    correccion = fields.Text(string='Correccion', store=True, copied=True, tracking=0, )
    date_done = fields.Date(string='Fecha de Cierre', store=True, readonly=True, copied=True, tracking=0, )
    date_validate = fields.Date(string='Fecha de Validacion', store=True, copied=True, tracking=0, )
    date = fields.Date(string='Fecha', store=True, required=True, tracking=0, )
    description = fields.Text(string='Descripcion', store=True, required=True, tracking=0, )
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0, )
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0, )
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0, )
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0, )
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0, )
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0, )
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0, )
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0, )
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, readonly=True, tracking=0, )
    observaciones = fields.Text(string='Observaciones', store=True, copied=True, tracking=0, )
    reference = fields.Char(string='En relacion con', store=True, copied=True, tracking=0, )
    req_incumple = fields.Text(string='Requisito Incumple', store=True, required=True, tracking=0, )


class AuditNonconformityOrigin(models.Model):
    _name = 'audit.nonconformity.origin'
    _description = 'Origen de No Conformidad de Auditoría'
    description = fields.Text(string='Descripcion', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )

class AuditObjectives(models.Model):
    _name = 'audit.objectives'
    _description = 'Objetivos de Auditoría'
    description = fields.Text(string='Descripcion', store=True, required=True, copied=True, tracking=0, )
    name = fields.Char(string='Objetivo', store=True, required=True, copied=True, tracking=0, )


class AuditPlanning(models.Model):
    _name = 'audit.planning'
    _description = 'Planificación de Auditoría'
    alcance = fields.Text(string='Alcance', store=True, required=True, copied=True, tracking=0, )
    date_end = fields.Datetime(string='Fecha Final', store=True, required=True, copied=True, tracking=0, )
    date_start = fields.Datetime(string='Fecha Inicial', store=True, required=True, copied=True, tracking=0, )
    duracion = fields.Float(string='Duracion(horas)', store=True, readonly=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )
    observaciones = fields.Text(string='Observaciones', store=True, copied=True, tracking=0, )
    reference = fields.Char(string='Codigo', store=True, readonly=True, copied=True, tracking=0, )


class AuditProcess(models.Model):
    _name = 'audit.process'
    _description = 'Proceso de Auditoría'
    description = fields.Text(string='Descripcion', store=True, required=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )
    reference = fields.Char(string='Referencia', store=True, required=True, copied=True, tracking=0, )

class AuditSystem(models.Model):
    _name = 'audit.system'
    _description = 'Sistema de Auditoría'
    description = fields.Text(string='Descripcion', store=True, required=True, copied=True, tracking=0, )
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )
    reference = fields.Char(string='Referencia', store=True, required=True, copied=True, tracking=0, )


class AuthTotpWizard(models.Model):
    _name = 'auth.totp.wizard'
    _description = 'Asistente de Autenticación TOTP'
    code = fields.Char(string='Código de verificación', store=True, copied=True, tracking=0, )
    qrcode = fields.Text(string='Código QR', store=True, readonly=True, tracking=0, )
    secret = fields.Char(string='Secreto', store=True, readonly=True, required=True, copied=True, tracking=0, )
    url = fields.Char(string='URL', store=True, readonly=True, tracking=0, )


class AvancysAccountFollowupFollowupLine(models.Model):
    _name = 'avancys.account.followup.followup.line'
    _description = 'Línea de Seguimiento de Cuenta Avancys'
    auto_execute = fields.Boolean(string='Auto Execute', store=True, copied=True, tracking=0, )
    delay = fields.Integer(string='Días de vencimiento', store=True, required=True, copied=True, tracking=0, )
    description = fields.Text(string='Printed Message', store=True, copied=True, tracking=0, )
    join_invoices = fields.Boolean(string='Join open Invoices', store=True, copied=True, tracking=0, )
    manual_action_note = fields.Text(string='Action To Do', store=True, copied=True, tracking=0, )
    manual_action = fields.Boolean(string='Manual Action', store=True, copied=True, tracking=0, )
    name = fields.Char(string='Criterios de seguimiento', store=True, required=True, copied=True, tracking=0, )
    print_letter = fields.Boolean(string='Imprimir una carta', store=True, copied=True, tracking=0, )
    send_email = fields.Boolean(string='Enviar un correo', store=True, copied=True, tracking=0, )
    send_sms = fields.Boolean(string='Send an SMS Message', store=True, copied=True, tracking=0, )
    sms_description = fields.Char(string='SMS Text Message', store=True, copied=True, tracking=0, )


class BankPaymentLine(models.Model):
    _name = 'bank.payment.line'
    _description = 'Línea de Pago Bancario'

    communication = fields.Char(string='Comunicación', store=True, readonly=True, required=True, copied=True,
                                tracking=0, )
    date = fields.Date(string='Fecha de pago', readonly=True, tracking=0, )
    name = fields.Char(string='Ref. de la línea de pago bancario', store=True, readonly=True, required=True, copied=True,
                       tracking=0, )


class BankTransactionWiz(models.Model):
    _name = 'bank.transaction.wiz'
    _description = 'Asistente de Transacción Bancaria'
    date = fields.Date(string='Fecha movimiento', store=True, copied=True, tracking=0, )


class BarcodesBarcodeEventsMixin(models.Model):
    _name = 'barcodes.barcode.events.mixin'
    _description = 'Mixin de Eventos de Código de Barras'
    _barcode_scanned = fields.Char(string='Código de barras escaneado', copied=True, tracking=0, )


class BaseAutomation(models.Model):
    _name  = 'base.automation'
    _description = 'Base Automation'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0, )
    activity_date_deadline_range = fields.Integer(string='Fecha límite el', copied=True, tracking=0, )
    activity_note = fields.Html(string='Nota', copied=True, tracking=0, )
    activity_summary = fields.Char(string='Resumen', copied=True, tracking=0, )
    activity_user_field_name = fields.Char(string='Nombre del campo de usuario', copied=True, tracking=0, )
    binding_view_types = fields.Char(string='Tipos de vista de enlace', copied=True, tracking=0, )
    code = fields.Text(string='Código Python', copied=True, tracking=0, )
    crud_model_name = fields.Char(string='Nombre del modelo destino', readonly=True, tracking=0, )
    filter_domain = fields.Char(string='Aplicar en', store=True, copied=True, tracking=0, )
    filter_pre_domain = fields.Char(string='Antes de actualizar el dominio', store=True, copied=True, tracking=0, )
    help = fields.Html(string='Descripción de la acción', copied=True, tracking=0, )
    last_run = fields.Datetime(string='Última ejecución', store=True, readonly=True, tracking=0, )
    least_delay_msg = fields.Char(string='Mínimo de retraso del mensaje', readonly=True, tracking=0, )
    model_name = fields.Char(string='Nombre del modelo', readonly=True, tracking=0, )
    name = fields.Char(string='Nombre de acción', required=True, copied=True, tracking=0, )
    sequence = fields.Integer(string='Secuencia', copied=True, tracking=0, )
    sms_mass_keep_log = fields.Boolean(string='Registrar como nota...', copied=True, tracking=0, )
    trg_date_range = fields.Integer(string='Retraso después de la fecha de activación', store=True, copied=True,
                                    tracking=0, )
    type = fields.Char(string='Tipo de acción', required=True, copied=True, tracking=0, )
    website_path = fields.Char(string='Ruta del Sitio Web', copied=True, tracking=0, )
    website_published = fields.Boolean(string='Disponible en el Sitio Web', tracking=0, )
    website_url = fields.Char(string='URL del lloc web', readonly=True, tracking=0, )
    xml_id = fields.Char(string='ID externo', readonly=True, tracking=0, )


class BaseGeoProvider(models.Model):
    _name = 'base.geo.provider'
    _description = 'Base Geo Provider'
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0, )
    tech_name = fields.Char(string='Nombre Técnico', store=True, copied=True, tracking=0, )


class BaseImportImport(models.Model):
    _name = 'base.import.import'
    _description = 'Base Import Import'
    file_name = fields.Char(string='Nombre del archivo', store=True, copied=True, tracking=0, )
    file_type = fields.Char(string='Tipo de archivo', store=True, copied=True, tracking=0, )
    file = fields.Text(string='Archivo', store=True, copied=True, tracking=0, )
    res_model = fields.Char(string='Modelo', store=True, copied=True, tracking=0, )
    

class BaseImportMapping(models.Model):
    _name = 'base.import.mapping'
    _description = "Base Import Mapping"
    column_name = fields.Char(string='Nombre de columna', store=True, copied=True, tracking=0, )
    field_name = fields.Char(string='Nombre de campo', store=True, copied=True, tracking=0, )
    res_model = fields.Char(string='Res Model', index=True, store=True, copied=True, tracking=0, )


class BaseImportTestsModelsChar(models.Model):
    _name = 'base.import.tests.models.char'
    _description = 'Base Import Tests Models Char'
    value = fields.Char(string='Valor', store=True, copied=True, tracking=0, )


class BaseImportTestsModelsCharNoreadonly(models.Model):
    _name = 'base.import.tests.models.char.noreadonly'
    _description = 'Base Import Tests Models Char Noreadonly'
    value = fields.Char(string='Valor', store=True, readonly=True, copied=True, tracking=0, )

class BaseImportTestsModelsCharReadonly(models.Model):
    _name = 'base.import.tests.models.char.readonly'
    _description = 'Base Import Tests Models Char Readonly'
    value = fields.Char(string='Valor', store=True, readonly=True, copied=True, tracking=0, )


class BaseImportTestsModelsCharRequired(models.Model):
    _name = 'base.import.tests.models.char.required'
    _description = 'Base Import Tests Models Char Required'
    value = fields.Char(string='Valor', store=True, required=True, copied=True, tracking=0, )


class BaseImportTestsModelsCharStates(models.Model):
    _name = 'base.import.tests.models.char.states'
    _description = 'Base Import Tests Models Char States'
    value = fields.Char(string='Valor', store=True, readonly=True, copied=True, tracking=0, )


class BaseImportTestsModelsCharStillreadonly(models.Model):
    _name = 'base.import.tests.models.char.stillreadonly'
    _description = 'Base Import Tests Models Char Stillreadonly'
    value = fields.Char(string='Valor', store=True, readonly=True, copied=True, tracking=0, )


class BaseImportTestsModelsComplex(models.Model):
    _name = 'base.import.tests.models.complex'
    _description = 'Base Import Tests Models Complex'
    c = fields.Char(string='C', store=True, copied=True, tracking=0, )
    d = fields.Date(string='D', store=True, copied=True, tracking=0, )
    dt = fields.Datetime(string='Dt', store=True, copied=True, tracking=0, )
    f = fields.Float(string='F', store=True, copied=True, tracking=0, )


class BaseImportTestsModelsFloat(models.Model):
    _name = 'base.import.tests.models.float'
    _description = 'Modelo de prueba para campos Float'

    value = fields.Float(string='Valor', store=True, copied=True, tracking=0)

class BaseImportTestsModelsM2ORelated(models.Model):
    _name = 'base.import.tests.models.m2o.related'
    _description = 'Modelo de prueba para campos Many2one relacionados'

    value = fields.Integer(string='Valor', store=True, copied=True, tracking=0)

class BaseImportTestsModelsM2ORequiredRelated(models.Model):
    _name = 'base.import.tests.models.m2o.required.related'
    _description = 'Modelo de prueba para campos Many2one requeridos y relacionados'

    value = fields.Integer(string='Valor', store=True, copied=True, tracking=0)

class BaseImportTestsModelsO2M(models.Model):
    _name = 'base.import.tests.models.o2m'
    _description = 'Modelo de prueba para campos One2many'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class BaseImportTestsModelsO2MChild(models.Model):
    _name = 'base.import.tests.models.o2m.child'
    _description = 'Modelo hijo de prueba para campos One2many'

    value = fields.Integer(string='Valor', store=True, copied=True, tracking=0)

class BaseImportTestsModelsPreview(models.Model):
    _name = 'base.import.tests.models.preview'
    _description = 'Modelo de prueba para vista previa'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    othervalue = fields.Integer(string='Otra variable', store=True, copied=True, tracking=0)
    somevalue = fields.Integer(string='Algún valor', store=True, required=True, copied=True, tracking=0)


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'
    google_id = fields.Char(string='Id del evento del Calendario de Google', store=True, tracking=0, )
    need_sync = fields.Boolean(string='Necesita sincronización', store=True, tracking=0, )


class CalendarRecurrence(models.Model):
    _inherit = 'calendar.recurrence'
    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0, )
    google_id = fields.Char(string='ID de Calendario de Google', store=True, tracking=0, )
    need_sync = fields.Boolean(string='Necesita sincronización', store=True, tracking=0, )


class CargosSvsp(models.Model):
    _name = 'cargos.svsp'
    _description = 'Modelo para gestión de cargos SVSP'

    activity_date_deadline = fields.Date(string='Siguiente plazo de actividad', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Resumen de la siguiente actividad', tracking=0)
    activity_type_icon = fields.Char(string='Ícono de tipo de actividad', readonly=True, tracking=0)
    codigo_cargo_svsp = fields.Integer(string='Código Cargo Svsp', store=True, required=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Nº de archivos adjuntos', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Número de errores', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Error de Envío de Mensaje', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='Error de entrega del SMS', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Es un seguidor', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Acción requerida', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Nº de mensajes sin leer', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Mensajes sin leer', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='Mi fecha límite de actividad', readonly=True, tracking=0)
    name = fields.Char(string='Name', store=True, required=True, copied=True, tracking=0)

class CarteraAvancysExtended(models.Model):
    _name = 'cartera.avancys.extended'
    _description = 'Extensión de cartera Avancys'

    date = fields.Date(string='Fecha de Corte', store=True, copied=True, tracking=0)
    rate = fields.Float(string='Tasa', store=True, copied=True, tracking=0)

class CarteraAvancysLine(models.Model):
    _name = 'cartera.avancys.line'
    _description = 'Líneas de cartera Avancys'

    currency_facturado_rate = fields.Float(string='Valor Facturado Currency Rate', store=True, copied=True, tracking=0)
    currency_facturado = fields.Float(string='Valor Facturado Currency', store=True, copied=True, tracking=0)
    currency_residual_rate = fields.Float(string='Valor Adeudado Currency Rate', store=True, copied=True, tracking=0)
    currency_residual = fields.Float(string='Valor Adeudado Currency', store=True, copied=True, tracking=0)
    date_emision = fields.Datetime(string='Fecha Emisión Informe', store=True, copied=True, tracking=0)
    date = fields.Date(string='Fecha de Corte', store=True, copied=True, tracking=0)
    en_mora = fields.Boolean(string='En Mora', store=True, copied=True, tracking=0)
    fecha_elaboracion = fields.Date(string='Fecha de elaboración', store=True, copied=True, tracking=0)
    fecha_vencimiento = fields.Date(string='Fecha de vencimiento', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    numero_dias_expedicion = fields.Integer(string='Número de días de Expedición', store=True, copied=True, tracking=0)
    numero_dias_vencidos = fields.Integer(string='Número de días Vencidos', store=True, copied=True, tracking=0)
    rango = fields.Char(string='Rango', store=True, copied=True, tracking=0)
    valor_facturado = fields.Float(string='Valor Facturado', store=True, copied=True, tracking=0)
    valor_residual = fields.Float(string='Valor Adeudado', store=True, copied=True, tracking=0)

class CashBoout(models.Model):
    _name = 'cash.boout'
    _description = 'Modelo para gestión de salidas de efectivo'

    amount = fields.Float(string='Importe', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Motivo', store=True, required=True, copied=True, tracking=0)

class CategoriaFlujoCajaVise(models.Model):
    _name = 'categoria.flujo.caja.vise'
    _description = 'Categorías de flujo de caja VISE'

    activity_date_deadline = fields.Date(string='Siguiente plazo de actividad', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Resumen de la siguiente actividad', tracking=0)
    activity_type_icon = fields.Char(string='Ícono de tipo de actividad', readonly=True, tracking=0)
    message_attachment_count = fields.Integer(string='Nº de archivos adjuntos', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Número de errores', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Error de Envío de Mensaje', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='Error de entrega del SMS', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Es un seguidor', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Acción requerida', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Nº de mensajes sin leer', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Mensajes sin leer', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='Mi fecha límite de actividad', readonly=True, tracking=0)
    name = fields.Char(string='Name', store=True, copied=True, tracking=0)
    PD09975316748215501 = fields.Integer(string='Código', store=True, copied=True, tracking=0)

class CertificadoIngresos(models.Model):
    _name = 'certificado.ingresos'
    _description = 'Certificado de ingresos'

    name = fields.Char(string='Name', store=True, readonly=True, copied=True, tracking=0)

class CertificadoIngresosLine(models.Model):
    _name = 'certificado.ingresos.line'
    _description = 'Líneas de certificado de ingresos'

    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    date_from = fields.Date(string='Desde', store=True, copied=True, tracking=0)
    date_to = fields.Date(string='Hasta', store=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)

class CertificadoIngresosLineItem(models.Model):
    _name = 'certificado.ingresos.line.item'
    _description = 'Ítems de líneas de certificado de ingresos'

    amount = fields.Float(string='amount', store=True, readonly=True, copied=True, tracking=0)
    move_ids = fields.Text(string='Movimientos', store=True, readonly=True, copied=True, tracking=0)
    name = fields.Char(string='Name', store=True, readonly=True, copied=True, tracking=0)

class CertificadoReportIngresos(models.Model):
    _name = 'certificado.report.ingresos'
    _description = 'Reporte de certificado de ingresos'

    description = fields.Text(string='Descripción', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    num = fields.Char(string='Número Formulario', store=True, required=True, copied=True, tracking=0)
    ref = fields.Char(string='Nit', readonly=True, tracking=0)
    title = fields.Char(string='Título', store=True, required=True, copied=True, tracking=0)

class CertificadoReportIngresosLine(models.Model):
    _name = 'certificado.report.ingresos.line'
    _description = 'Líneas de reporte de certificado de ingresos'

    amount = fields.Float(string='Valor %', store=True, copied=True, tracking=0)
    concepts = fields.Char(string='Conceptos de nómina', store=True, copied=True, tracking=0)
    description = fields.Char(string='Descripción', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)

class CertificadoReportRetencion(models.Model):
    _name = 'certificado.report.retencion'
    _description = 'Reporte de certificado de retención'

    description = fields.Text(string='Notas', store=True, copied=True, tracking=0)
    impuesto_compuesto = fields.Boolean(string='Impuesto Compuesto', store=True, copied=True, tracking=0)
    is_ica = fields.Boolean(string='Impuesto ICA', store=True, copied=True, tracking=0)
    is_ret_iva = fields.Boolean(string='Ret. IVA', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    title = fields.Char(string='Título', store=True, required=True, copied=True, tracking=0)

class CertificadoReportRetencionLine(models.Model):
    _name = 'certificado.report.retencion.line'
    _description = 'Líneas de reporte de certificado de retención'

    ciudad_tercero = fields.Char(string='Ciudad', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    porcentaje = fields.Float(string='Porcentaje', readonly=True, tracking=0)

class CertificadoReportRetencionPeriodicidad(models.Model):
    _name = 'certificado.report.retencion.periodicidad'
    _description = 'Periodicidad de reporte de certificado de retención'

    date_end = fields.Date(string='Hasta', store=True, required=True, copied=True, tracking=0)
    date_start = fields.Date(string='Desde', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)

class ChangeDifference(models.Model):
    _name = 'change.difference'
    _description = 'Diferencias de cambio'

    date = fields.Date(string='Fecha', store=True, readonly=True, required=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    name = fields.Char(string='Name', store=True, readonly=True, copied=True, tracking=0)
    rate = fields.Float(string='Tasa', store=True, readonly=True, required=True, copied=True, tracking=0)

class ChooseDeliveryCarrier(models.Model):
    _name = 'choose.delivery.carrier'
    _description = 'Selección de transportista de entrega'

    delivery_message = fields.Text(string='Mensaje de entrega', store=True, readonly=True, copied=True, tracking=0)
    delivery_price = fields.Float(string='Precio de envío', store=True, copied=True, tracking=0)
    display_price = fields.Float(string='Costo', store=True, readonly=True, copied=True, tracking=0)
    invoicing_message = fields.Text(string='Mensaje de facturación', readonly=True, tracking=0)

class ChooseDeliveryPackage(models.Model):
    _name = 'choose.delivery.package'
    _description = 'Selección de paquete de entrega'

    shipping_weight = fields.Float(string='Peso del envío', store=True, copied=True, tracking=0)
    weight_uom_name = fields.Char(string='Etiqueta de unidad de medida de peso', readonly=True, tracking=0)

class CierreNominaWiz(models.Model):
    _name = 'cierre.nomina.wiz'
    _description = 'Asistente de cierre de nómina'

    create_tarifario = fields.Boolean(string='Crear Tarifario', store=True, copied=True, tracking=0)
    fecha_cierre = fields.Date(string='Fecha de cierre', store=True, required=True, copied=True, tracking=0)
    politica_solo_adicionales = fields.Boolean(string='Política solo adicionales', store=True, copied=True, tracking=0)
    solo_adicionales = fields.Boolean(string='Cerrar solo adicionales?', store=True, copied=True, tracking=0)

class CierreProgramacionWiz(models.Model):
    _name = 'cierre.programacion.wiz'
    _description = 'Asistente de cierre de programación'

    fecha_cierre = fields.Date(string='Fecha de cierre', store=True, required=True, copied=True, tracking=0)

class CommunicationQuoter(models.Model):
    _name = 'communication.quoter'
    _description = 'Cotizador de comunicaciones'

    quantity = fields.Integer(string='Cantidad', store=True, copied=True, tracking=0)

class ComputeInvoiceItems(models.Model):
    _name = 'compute.invoice.items'
    _description = 'Cálculo de ítems de factura'

    limit_date = fields.Date(string='Fecha corte', store=True, required=True, copied=True, tracking=0)

class ComunicacionesConfiguracion(models.Model):
    _name = 'comunicaciones.configuracion'
    _description = 'Configuración de comunicaciones'

    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Name', store=True, copied=True, tracking=1)

class ContactoEmergencia(models.Model):
    _name = 'contacto.emergencia'
    _description = 'Contacto de emergencia'

    direccion = fields.Char(string='Dirección', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombres', store=True, required=True, copied=True, tracking=0)
    parentesco = fields.Char(string='Parentesco', store=True, copied=True, tracking=0)
    telefono = fields.Char(string='Teléfono', store=True, required=True, copied=True, tracking=0)

class ContractHoursJob(models.Model):
    _name = 'contract.hours.job'
    _description = 'Horas de contrato por trabajo'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class CoordinadorDeApoyo(models.Model):
    _name = 'coordinador.de.apoyo'
    _description = 'Coordinador de apoyo'

    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    email = fields.Char(string='Dirección de Email', tracking=1)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    ref_num = fields.Char(string='Número de identificación', tracking=1)
    work_phone = fields.Char(string='Teléfono trabajo', tracking=1)

class CreateHrPayslipDianDocument(models.Model):
    _name = 'create.hr.payslip.dian.document'
    _description = 'Creación de documento DIAN para nómina'

    date_end = fields.Date(string='Date End', store=True, tracking=0)
    date_start = fields.Date(string='Date Start', store=True, tracking=0)

class CreditControlAnalysis(models.Model):
    _name = 'credit.control.analysis'
    _description = 'Análisis de control de crédito'

    level = fields.Integer(string='Nivel', store=True, readonly=True, copied=True, tracking=0)
    open_balance = fields.Float(string='Saldo vencido', store=True, readonly=True, copied=True, tracking=0)
    partner_ref = fields.Char(string='Empresa', store=True, readonly=True, copied=True, tracking=0)

class CreditControlCommunication(models.Model):
    _name = 'credit.control.communication'
    _description = 'Comunicación de control de crédito'

    activity_date_deadline = fields.Date(string='Fecha de la siguiente acción', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Siguiente acción', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Seguimiento', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Siguiente acción', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    report_date = fields.Date(string='Fecha del informe', store=True, copied=True, tracking=0)
    total_due = fields.Float(string='Total debido', readonly=True, tracking=0)
    total_invoiced = fields.Float(string='Total facturado', readonly=True, tracking=0)

class CreditControlLine(models.Model):
    _name = 'credit.control.line'
    _description = 'Líneas de control de crédito'

    activity_date_deadline = fields.Date(string='Fecha de la siguiente acción', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    amount_due = fields.Float(string='Importe vencido con imp.', store=True, readonly=True, required=True, copied=True, tracking=0)
    balance_due = fields.Float(string='Saldo vencido', store=True, readonly=True, required=True, copied=True, tracking=0)
    date_due = fields.Date(string='Fecha de vencimiento', store=True, readonly=True, required=True, copied=True, tracking=0)
    date_entry = fields.Date(string='Fecha del asiento', store=True, readonly=True, tracking=0)
    date_sent = fields.Date(string='Fecha de ejecución', store=True, readonly=True, copied=True, tracking=0)
    date = fields.Date(string='Fecha del control', index=True, store=True, readonly=True, required=True, copied=True, tracking=0)
    level = fields.Integer(string='Nivel', store=True, readonly=True, tracking=0)
    manual_followup = fields.Boolean(string='Seguimiento manual', store=True, copied=True, tracking=0)
    manually_overridden = fields.Boolean(string='Sobreescrito manualmente', store=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Siguiente acción', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Seguimiento', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Siguiente acción', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    account_id = fields.Many2one(string='Cuenta', store=True, readonly=True, tracking=100,
                                 comodel_name='account.account', )
    activity_type_id = fields.Many2one(string='Fecha de la siguiente acción', tracking=0,
                                       comodel_name='mail.activity.type', )
    activity_user_id = fields.Many2one(string='Responsible User', tracking=0, comodel_name='res.users', )
    commercial_partner_id = fields.Many2one(string='Commercial Entity', index=True, store=True, readonly=True,
                                            tracking=0, comodel_name='res.partner', )
    communication_id = fields.Many2one(string='Communication process', store=True, copied=True, tracking=0,
                                       comodel_name='credit.control.communication', )
    company_id = fields.Many2one(string='Compañía', store=True, readonly=True, tracking=0, comodel_name='res.company', )
    currency_id = fields.Many2one(string='Divisa', store=True, readonly=True, tracking=0, comodel_name='res.currency', )
    invoice_id = fields.Many2one(string='Factura', store=True, readonly=True, copied=True, tracking=0,
                                 comodel_name='account.move', )
    message_channel_ids = fields.Many2many(string='Followers (Channels)', readonly=True, tracking=0,
                                           comodel_name='mail.channel', )
    message_main_attachment_id = fields.Many2one(string='Main Attachment', index=True, store=True, tracking=0,
                                                 comodel_name='ir.attachment', )
    message_partner_ids = fields.Many2many(string='Followers (Partners)', readonly=True, tracking=0,
                                           comodel_name='res.partner', )
    move_line_id = fields.Many2one(string='Apunte', index=True, store=True, readonly=True, required=True, copied=True,
                                   tracking=0, comodel_name='account.move.line', )
    partner_id = fields.Many2one(string='Empresa', store=True, readonly=True, required=True, copied=True, tracking=0,
                                 comodel_name='res.partner', )
    partner_user_id = fields.Many2one(string='Salesperson', store=True, readonly=True, tracking=0,
                                      comodel_name='res.users', )
    policy_id = fields.Many2one(string='Política asociada', store=True, readonly=True, tracking=0,
                                comodel_name='credit.control.policy', )
    policy_level_id = fields.Many2one(string='Nivel de retraso', store=True, readonly=True, required=True, copied=True,
                                      tracking=0, comodel_name='credit.control.policy.level', )
    run_id = fields.Many2one(string='Origen', store=True, copied=True, tracking=0, comodel_name='credit.control.run', )



    # activity_ids = fields.One2many(string='Activa', store=True, tracking=0, comodel_name='mail.activity', )
    # failed_message_ids = fields.One2many(string='Failed Messages', store=True, tracking=0,
    #                                      comodel_name='mail.message', )
    # message_follower_ids = fields.One2many(string='Seguimiento', store=True, tracking=0,
    #                                        comodel_name='mail.followers', )
    # message_ids = fields.One2many(string='Mensaje personalizado', store=True, tracking=0, comodel_name='mail.message', )
    # website_message_ids = fields.One2many(string='Mensaje personalizado', store=True, tracking=0,
    #                                       comodel_name='mail.message', )


class CreditControlPolicy(models.Model):
    _name = 'credit.control.policy'
    _description = 'Política de control de crédito'

    active = fields.Boolean(string='Activa', store=True, copied=True, tracking=0)
    do_nothing = fields.Boolean(string='No hace nada', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)

class CreditControlPolicyChanger(models.Model):
    _name = 'credit.control.policy.changer'
    _description = 'Cambiador de política de control de crédito'

    do_nothing = fields.Boolean(string='Sin política de seguimiento', store=True, copied=True, tracking=0)

class CreditControlPolicyLevel(models.Model):
    _name = 'credit.control.policy.level'
    _description = 'Niveles de política de control de crédito'

    custom_mail_text = fields.Html(string='Mensaje de correo electrónico personalizado', store=True, required=True, copied=True, tracking=0)
    custom_text_after_details = fields.Text(string='Mensaje personalizado después de los detalles', store=True, copied=True, tracking=0)
    custom_text = fields.Text(string='Mensaje personalizado', store=True, required=True, copied=True, tracking=0)
    delay_days = fields.Integer(string='Retardo (en días)', store=True, required=True, copied=True, tracking=0)
    level = fields.Integer(string='Nivel', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)

class CreditControlPrinter(models.Model):
    _name = 'credit.control.printer'
    _description = 'Impresora de control de crédito'

    mark_as_sent = fields.Boolean(string='Marcar líneas de carta como enviadas', store=True, copied=True, tracking=0)

class CreditControlRun(models.Model):
    _name = 'credit.control.run'
    _description = 'Ejecución de control de crédito'

    credit_control_communication_count = fields.Integer(string='# of Credit Control Communications', readonly=True, tracking=0)
    credit_control_count = fields.Integer(string='Líneas de control de crédito', readonly=True, tracking=0)
    date = fields.Date(string='Fecha del control', store=True, readonly=True, required=True, copied=True, tracking=0)
    hide_change_state_button = fields.Boolean(string='Hide Change State Button', store=True, copied=True, tracking=0)
    report = fields.Html(string='Informe', store=True, readonly=True, tracking=0)

class CrmClaim(models.Model):
    _name = 'crm.claim'
    _description = 'Reclamaciones CRM'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0)
    activity_date_deadline = fields.Date(string='Siguiente →', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    cause = fields.Text(string='Causa principal', store=True, copied=True, tracking=0)
    date_closed = fields.Datetime(string='Cerrada', store=True, readonly=True, copied=True, tracking=0)
    date_deadline = fields.Date(string='Fecha límite', store=True, copied=True, tracking=0)
    date = fields.Datetime(string='Fecha de Reclamación', index=True, store=True, copied=True, tracking=0)
    description = fields.Text(string='Descripción', store=True, copied=True, tracking=0)
    email_cc = fields.Text(string='Email de los observadores', store=True, copied=True, tracking=0)
    email_from = fields.Char(string='Email', store=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Número de adjuntos', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Número de error', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Error en la entrega del mensaje', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='Error en la entrega del mensaje', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Es seguidor', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Tipo de Acción', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Contador de mensajes no leídos', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Mensajes no leídos', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Objeto de la reclamación', store=True, required=True, copied=True, tracking=0)
    partner_phone = fields.Char(string='Teléfono', store=True, copied=True, tracking=0)
    resolution = fields.Text(string='Resolución', store=True, copied=True, tracking=0)
    user_fault = fields.Char(string='Responsable problema', store=True, copied=True, tracking=0)

class CrmClaimCategory(models.Model):
    _name = 'crm.claim.category'
    _description = 'Categorías de reclamaciones CRM'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    count_sale_quter = fields.Integer(string='count_sale_quter', readonly=True, tracking=0, )
    ticket_count = fields.Integer(string='Tickets', readonly=True, tracking=0, )


class CrmClaimReport(models.Model):
    _name = 'crm.claim.report'
    _description = 'Reporte de reclamaciones CRM'

    claim_date = fields.Datetime(string='Fecha de Reclamación', store=True, readonly=True, copied=True, tracking=0)
    date_closed = fields.Datetime(string='Fecha cierre', index=True, store=True, readonly=True, copied=True, tracking=0)
    date_deadline = fields.Date(string='Fecha límite', index=True, store=True, readonly=True, copied=True, tracking=0)
    delay_close = fields.Float(string='Demora cierre', store=True, readonly=True, copied=True, tracking=0)
    delay_expected = fields.Float(string='Fecha límite excedida', store=True, readonly=True, copied=True, tracking=0)
    email = fields.Integer(string='# Emails', store=True, readonly=True, copied=True, tracking=0)
    nbr_claims = fields.Integer(string='# de Reclamaciones', store=True, readonly=True, copied=True, tracking=0)
    subject = fields.Char(string='Objeto de la reclamación', store=True, readonly=True, copied=True, tracking=0)

class CrmClaimStage(models.Model):
    _name = 'crm.claim.stage'
    _description = 'Etapas de reclamaciones CRM'

    case_default = fields.Boolean(string='Común a todos los equipos', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre de la etapa', store=True, required=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)

class CrossoveredBudget(models.Model):
    _name = 'crossovered.budget'
    _description = 'Presupuestos cruzados'

    date_from = fields.Date(string='Fecha de inicio', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha final', store=True, required=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Cuenta de adjunto', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Error en la entrega del mensaje', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Es seguidor', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Acción necesaria', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Contador de mensajes no leídos', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Mensajes no leídos', readonly=True, tracking=0)
    name = fields.Char(string='Nombre del Presupuesto', store=True, required=True, copied=True, tracking=0)

class CrossoveredBudgetLines(models.Model):
    _name = 'crossovered.budget.lines'
    _description = 'Líneas de presupuestos cruzados'

    date_from = fields.Date(string='Fecha de inicio', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha final', store=True, required=True, copied=True, tracking=0)
    paid_date = fields.Date(string='Fecha Pago', store=True, copied=True, tracking=0)
    percentage = fields.Float(string='Logro', readonly=True, tracking=0)
    planned_amount = fields.Float(string='Importe Planificado', store=True, required=True, copied=True, tracking=0)
    practical_amount = fields.Float(string='Importe Real', store=True, readonly=True, tracking=0)
    theoretical_amount = fields.Float(string='Importe teórico', readonly=True, tracking=0)
    analytic_account_id = fields.Many2one(string='Cuenta Analítica', store=True, copied=True, tracking=0,
                                          comodel_name='account.analytic.account', )
    company_id = fields.Many2one(string='Compañía', store=True, readonly=True, tracking=0, comodel_name='res.company', )
    crossovered_budget_id = fields.Many2one(string='Presupuesto', index=True, store=True, required=True, copied=True,
                                            tracking=0, comodel_name='crossovered.budget', )
    general_budget_id = fields.Many2one(string='Posición Presupuestaria', store=True, required=True, copied=True,
                                        tracking=0, comodel_name='account.budget.post', )
    project_service_order_id = fields.Many2one(string='Orden de servicio', store=True, copied=True, tracking=0,
                                               comodel_name='project.service.order', )


class CursosPeis(models.Model):
    _name = 'cursos.peis'
    _description = 'Cursos PEIS'

    activity_date_deadline = fields.Date(string='Siguiente plazo de actividad', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Resumen de la siguiente actividad', tracking=0)
    activity_type_icon = fields.Char(string='Ícono de tipo de actividad', readonly=True, tracking=0)
    codigo_cargo_svsp = fields.Integer(string='Código Cargo Svsp', store=True, tracking=0)
    codigo_curso_peis_svsp = fields.Integer(string='Código Curso Peis Svsp', store=True, required=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Nº de archivos adjuntos', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Número de errores', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Error de Envío de Mensaje', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='Error de entrega del SMS', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Es un seguidor', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Acción requerida', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Nº de mensajes sin leer', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Mensajes sin leer', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='Mi fecha límite de actividad', readonly=True, tracking=0)
    name = fields.Char(string='Name', store=True, required=True, copied=True, tracking=0)

class CursosvigilanciaVsAcreditacion(models.Model):
    _name = 'cursos.vigilancia.vs.acreditacion'
    _description = 'Cursos de vigilancia vs. acreditación'

    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    cargo = fields.Char(string='Cargo', store=True, readonly=True, tracking=0)
    comentario = fields.Text(string='Comentario', store=True, copied=True, tracking=0)
    fecha_realizacion_curso = fields.Date(string='Fecha de realización curso', store=True, required=True, copied=True, tracking=0)
    fecha_registro_sistema = fields.Date(string='Fecha de registro en el sistema', store=True, readonly=True, copied=True, tracking=0)
    fecha_vencimiento_acreditacion = fields.Date(string='Fecha de vencimiento acreditación', store=True, copied=True, tracking=0)
    fecha_vencimiento_curso = fields.Date(string='Fecha de vencimiento curso', store=True, copied=True, tracking=0)
    has_attachments = fields.Boolean(string='Tiene Archivos', readonly=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    numero_identificacion = fields.Char(string='Número de Identificación', store=True, copied=True, tracking=0)
    numero_registro = fields.Text(string='Número registro', store=True, required=True, copied=True, tracking=0)

class DateRange(models.Model):
    _name = 'date.range'
    _description = 'Rango de fechas'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0)
    date_end = fields.Date(string='Fecha final', store=True, required=True, copied=True, tracking=0)
    date_start = fields.Date(string='Fecha de inicio', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    type_name = fields.Char(string='Nombre', store=True, readonly=True, tracking=0)

class DateRangeGenerator(models.Model):
    _name = 'date.range.generator'
    _description = 'Generador de rangos de fechas'

    count = fields.Integer(string='Número de rangos a generar', store=True, required=True, copied=True, tracking=0)
    date_start = fields.Date(string='Fecha de inicio', store=True, required=True, copied=True, tracking=0)
    duration_count = fields.Integer(string='Duración', store=True, required=True, copied=True, tracking=0)
    name_prefix = fields.Char(string='Prefijo del nombre del rango', store=True, required=True, copied=True, tracking=0)

class DateRangeType(models.Model):
    _name = 'date.range.type'
    _description = 'Tipos de rango de fechas'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0)
    allow_overlap = fields.Boolean(string='Permitir solapamiento', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)

class Decision(models.Model):
    _name = 'decision'
    _description = 'Decisión'

    name = fields.Char(string='Name', store=True, copied=True, tracking=1)

class DeliveryCarrier(models.Model):
    _name = 'delivery.carrier'
    _description = 'Transportistas de entrega'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0)
    amount = fields.Float(string='Importe', store=True, copied=True, tracking=0)
    can_generate_return = fields.Boolean(string='Puedes generar una devolución', readonly=True, tracking=0)
    debug_logging = fields.Boolean(string='Registro de debug', store=True, copied=True, tracking=0)
    fixed_price = fields.Float(string='Precio fijo', store=True, tracking=0)
    free_over = fields.Boolean(string='Gratuito si el importe del pedido es superior a', store=True, copied=True, tracking=0)
    get_return_label_from_portal = fields.Boolean(string='Etiqueta de devolución accesible desde el portal de clientes', store=True, copied=True, tracking=0)
    margin = fields.Float(string='Margen', store=True, copied=True, tracking=0)
    name = fields.Char(string='Método entrega', store=True, required=True, copied=True, tracking=0)
    prod_environment = fields.Boolean(string='Entorno', store=True, copied=True, tracking=0)
    return_label_on_delivery = fields.Boolean(string='Generar etiqueta de devolución', store=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)
    zip_from = fields.Char(string='CP desde', store=True, copied=True, tracking=0)
    zip_to = fields.Char(string='CP hasta', store=True, copied=True, tracking=0)

class DeliveryGuide(models.Model):
    _name = 'delivery.guide'
    _description = 'Guías de entrega'

    activity_date_deadline = fields.Date(string='Siguiente plazo de actividad', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Resumen de la siguiente actividad', tracking=0)
    activity_type_icon = fields.Char(string='Ícono de tipo de actividad', readonly=True, tracking=0)
    consignment = fields.Char(string='Remesa', store=True, copied=True, tracking=0)
    date_checked = fields.Date(string='Fecha de Revisión', store=True, copied=True, tracking=0)
    date_delivered = fields.Date(string='Fecha de Entrega', store=True, copied=True, tracking=0)
    date_invoiced = fields.Date(string='Fecha de Factura', store=True, copied=True, tracking=0)
    date_progress = fields.Date(string='Fecha en Progreso', store=True, copied=True, tracking=0)
    date_scheduled = fields.Date(string='Fecha Programada', store=True, required=True, copied=True, tracking=0)
    driver_comment = fields.Text(string='Comentario', readonly=True, tracking=0)
    driver_mobile = fields.Char(string='Celular', readonly=True, tracking=0)
    driver_name = fields.Char(string='Nombre', readonly=True, tracking=0)
    driver_plate = fields.Char(string='Placa', readonly=True, tracking=0)
    driver_vat = fields.Char(string='NIT', readonly=True, tracking=0)
    file_data = fields.Text(string='Archivo', store=True, copied=True, tracking=0)
    file_name = fields.Char(string='Nombre Público', store=True, copied=True, tracking=0)
    guide_bool = fields.Boolean(string='Tiene devoluciones', store=True, tracking=0)
    guide_update = fields.Boolean(string='Actualizar', store=True, tracking=0)
    message_attachment_count = fields.Integer(string='Nº de archivos adjuntos', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Número de errores', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Error de Envío de Mensaje', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Es un seguidor', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Número de Acciones', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Acción requerida', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Nº de mensajes sin leer', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Mensajes sin leer', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='Mis Actividades Vencidas', readonly=True, tracking=0)
    name = fields.Char(string='Número', store=True, readonly=True, required=True, tracking=0)
    notes = fields.Text(string='Términos y condiciones', store=True, copied=True, tracking=0)
    payment_boolean = fields.Boolean(string='Pagado', store=True, copied=True, tracking=100)
    price_tolerance = fields.Float(string='Tolerancia', readonly=True, tracking=0)
    price_total = fields.Float(string='Costo Total', store=True, readonly=True, tracking=0)
    price = fields.Float(string='Precio Ajustado', store=True, tracking=100)
    rate_tolerance = fields.Float(string='Tolerancia (%)', readonly=True, tracking=0)
    show_update_price_kg = fields.Boolean(string='Actualizando precio(Kg)', store=True, copied=True, tracking=0)
    show_update_weight_manual = fields.Boolean(string='Ha cambiado el precio (kg)', store=True, copied=True, tracking=0)
    weight_adjust = fields.Float(string='Peso Ajustado', store=True, copied=True, tracking=0)
    weight_invoice = fields.Float(string='Peso Entregado', store=True, readonly=True, tracking=0)
    weight_manual = fields.Float(string='Peso Manual', store=True, copied=True, tracking=100)
    weight_move = fields.Float(string='Peso de Movimientos', store=True, readonly=True, tracking=0)
    weight_return = fields.Float(string='Peso Retornado', store=True, readonly=True, tracking=0)
    weight_theoretical = fields.Float(string='Peso Teórico', store=True, copied=True, tracking=0)
    weight_total = fields.Float(string='Peso Total', store=True, readonly=True, tracking=0)

class DeliveryGuideLine(models.Model):
    _name = 'delivery.guide.line'
    _description = 'Líneas de guías de entrega'

    account_date = fields.Date(string='Fecha de Factura/Recibo', readonly=True, tracking=0)
    account_delivery_bool = fields.Boolean(string='Tiene Novedad', store=True, copied=True, tracking=0)
    account_name = fields.Char(string='Número', readonly=True, tracking=0)
    stock_date = fields.Datetime(string='Fecha programada', readonly=True, tracking=0)
    stock_product_qty = fields.Float(string='Cantidad', store=True, copied=True, tracking=0)
    stock_product_uom_qty = fields.Float(string='Demanda', store=True, copied=True, tracking=0)
    stock_weight = fields.Float(string='Peso movimiento', store=True, readonly=True, tracking=0)

class DeliveryInvoice(models.Model):
    _name = 'delivery.invoice'
    _description = 'Facturas de entrega'

    activity_date_deadline = fields.Date(string='Siguiente plazo de actividad', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Resumen de la siguiente actividad', tracking=0)
    activity_type_icon = fields.Char(string='Ícono de tipo de actividad', readonly=True, tracking=0)
    message_attachment_count = fields.Integer(string='Nº de archivos adjuntos', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Número de errores', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Error de Envío de Mensaje', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Es un seguidor', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Número de Acciones', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Acción requerida', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Nº de mensajes sin leer', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Mensajes sin leer', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='Mis Actividades Vencidas', readonly=True, tracking=0)
    notes = fields.Text(string='Notas', store=True, copied=True, tracking=0)
    weight_invoiced = fields.Float(string='Peso', readonly=True, tracking=0)
    weight_returned = fields.Float(string='Peso Retornado', readonly=True, tracking=0)

class DeliveryPriceRule(models.Model):
    _name = 'delivery.price.rule'
    _description = 'Reglas de precios de entrega'

    list_base_price = fields.Float(string='Precio de venta base', store=True, required=True, copied=True, tracking=0)
    list_price = fields.Float(string='Precio de venta', store=True, required=True, copied=True, tracking=0)
    mavalue = fields.Float(string='Valor máximo', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', readonly=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, required=True, copied=True, tracking=0)

class DeliveryRate(models.Model):
    _name = 'delivery.rate'
    _description = 'Tarifas de entrega'

    name = fields.Char(string='Título', store=True, copied=True, tracking=0)
    notes = fields.Text(string='Términos y condiciones', store=True, copied=True, tracking=0)
    tolerance = fields.Float(string='Tolerancia (%)', store=True, copied=True, tracking=0)

class DeliveryRateLine(models.Model):
    _name = 'delivery.rate.line'
    _description = 'Líneas de tarifas de entrega'

    observation = fields.Char(string='Observación', store=True, copied=True, tracking=0)

class DeliveryVehicle(models.Model):
    _name = 'delivery.vehicle'
    _description = 'Vehículos de entrega'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)

class DeliveryVehicleCondition(models.Model):
    _name = 'delivery.vehicle.condition'
    _description = 'Condiciones de vehículos de entrega'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)

class DmsAccessGroup(models.Model):
    _name = 'dms.access.group'
    _description = 'Grupos de acceso DMS'

    count_directories = fields.Integer(string='Nº de carpetas', readonly=True, tracking=0)
    count_users = fields.Integer(string='Usuarios', store=True, readonly=True, tracking=0)
    name = fields.Char(string='Nombre del grupo', store=True, required=True, copied=True, tracking=0)
    parent_path = fields.Char(string='Modelo padre', index=True, store=True, copied=True, tracking=0)
    perm_create = fields.Boolean(string='Acceso de creación', store=True, copied=True, tracking=0)
    perm_inclusive_create = fields.Boolean(string='Inherited Create Access', store=True, readonly=True, tracking=0)
    perm_inclusive_unlink = fields.Boolean(string='Inherited Unlink Access', store=True, readonly=True, tracking=0)
    perm_inclusive_write = fields.Boolean(string='Inherited Write Access', store=True, readonly=True, tracking=0)
    perm_unlink = fields.Boolean(string='Acceso de eliminación', store=True, copied=True, tracking=0)
    perm_write = fields.Boolean(string='Acceso de escritura', store=True, copied=True, tracking=0)

class DmsCategory(models.Model):
    _name = 'dms.category'
    _description = 'Categorías DMS'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0)
    complete_name = fields.Char(string='Nombre completo', store=True, readonly=True, tracking=0)
    count_categories = fields.Integer(string='Nº de subcategorías', readonly=True, tracking=0)
    count_directories = fields.Integer(string='Nº de carpetas', readonly=True, tracking=0)
    count_files = fields.Integer(string='Nº de archivos', readonly=True, tracking=0)
    count_tags = fields.Integer(string='Nº de etiquetas', readonly=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    parent_path = fields.Char(string='Modelo padre', index=True, store=True, copied=True, tracking=0)

class DmsDirectory(models.Model):
    _name = 'dms.directory'
    _description = 'Directorios DMS'

    access_token = fields.Char(string='Token de seguridad', store=True, tracking=0)
    access_url = fields.Char(string='URL de acceso al portal', readonly=True, tracking=0)
    access_warning = fields.Text(string='Aviso de acceso', readonly=True, tracking=0)
    activity_date_deadline = fields.Date(string='Fecha fin siguiente actividad', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Resumen de siguiente actividad', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    alias_bounced_content = fields.Html(string='Custom Bounced Message', copied=True, tracking=0)
    alias_defaults = fields.Text(string='Valores por defecto', required=True, copied=True, tracking=0)
    alias_domain = fields.Char(string='Dominio de alias', readonly=True, tracking=0)
    alias_force_thread_id = fields.Integer(string='ID de hilo de registro', copied=True, tracking=0)
    alias_name = fields.Char(string='Nombre del alias', tracking=0)
    alias_parent_thread_id = fields.Integer(string='Ruta padre', copied=True, tracking=0)
    color = fields.Integer(string='Color', store=True, copied=True, tracking=0)
    complete_name = fields.Char(string='Nombre completo', store=True, readonly=True, tracking=0)
    count_directories_title = fields.Char(string='Nº de subcarpetas', readonly=True, tracking=0)
    count_directories = fields.Integer(string='Título de las carpetas de recuento', readonly=True, tracking=0)
    count_elements = fields.Integer(string='Nº de elementos', readonly=True, tracking=0)
    count_files_title = fields.Char(string='Nº de archivos', readonly=True, tracking=0)
    count_files = fields.Integer(string='Título de los archivos de recuento', readonly=True, tracking=0)
    count_total_directories = fields.Integer(string='Total subcarpetas', readonly=True, tracking=0)
    count_total_elements = fields.Integer(string='Total elementos', readonly=True, tracking=0)
    count_total_files = fields.Integer(string='Total archivos', readonly=True, tracking=0)
    icon_url = fields.Char(string='Icon URL', readonly=True, tracking=0)
    image_1024 = fields.Text(string='Image 1024', store=True, readonly=True, tracking=0)
    image_128 = fields.Text(string='Image 128', store=True, readonly=True, tracking=0)
    image_1920 = fields.Text(string='Image', store=True, copied=True, tracking=0)
    image_256 = fields.Text(string='Image 256', store=True, readonly=True, tracking=0)
    image_512 = fields.Text(string='Image 512', store=True, readonly=True, tracking=0)
    inherit_group_ids = fields.Boolean(string='Grupos heredados', store=True, copied=True, tracking=0)
    is_hidden = fields.Boolean(string='Almacenamiento está oculto', store=True, readonly=True, tracking=0)
    is_root_directory = fields.Boolean(string='Es carpeta raíz', store=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Nº de adjuntos', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Número de error', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Error de entrega de mensaje', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='Error de entrega de SMS', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Es seguidor', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Acción necesaria', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Nº de mensajes no leídos', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Mensajes no leídos', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Nombre', index=True, store=True, required=True, copied=True, tracking=0)
    parent_path = fields.Char(string='Modelo padre', index=True, store=True, copied=True, tracking=0)
    permission_create = fields.Boolean(string='Acceso de creación', readonly=True, tracking=0)
    permission_read = fields.Boolean(string='Acceso de lectura', readonly=True, tracking=0)
    permission_unlink = fields.Boolean(string='Acceso de eliminación', readonly=True, tracking=0)
    permission_write = fields.Boolean(string='Acceso de escritura', readonly=True, tracking=0)
    res_id = fields.Integer(string='ID de registro de archivos adjuntos vinculados', index=True, store=True, copied=True, tracking=0)
    res_model = fields.Char(string='Modelo de adjuntos vinculado', index=True, store=True, copied=True, tracking=0)
    size = fields.Integer(string='Tamaño', readonly=True, tracking=0)
    starred = fields.Boolean(string='Destacado', tracking=0)
    storage_id_inherit_access_from_parent_record = fields.Boolean(string='Inherit permissions from related record', store=True, readonly=True, tracking=0)

class DmsFile(models.Model):
    _name = 'dms.file'
    _description = 'Archivos DMS'

    access_token = fields.Char(string='Token de seguridad', store=True, tracking=0)
    access_url = fields.Char(string='URL de acceso al portal', readonly=True, tracking=0)
    access_warning = fields.Text(string='Aviso de acceso', readonly=True, tracking=0)
    active = fields.Boolean(string='Archivado', store=True, copied=True, tracking=0)
    activity_date_deadline = fields.Date(string='Fecha fin siguiente actividad', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Resumen de siguiente actividad', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    checksum = fields.Char(string='Checksum/SHA1', index=True, store=True, readonly=True, copied=True, tracking=0)
    color = fields.Integer(string='Color', store=True, copied=True, tracking=0)
    content_file = fields.Text(string='Contenido de archivo', store=True, copied=True, tracking=0)
    content_Text = fields.Text(string='Contenido binario', store=True, copied=True, tracking=0)
    content = fields.Text(string='Contenido', required=True, tracking=0)
    extension = fields.Char(string='Extensión', store=True, readonly=True, tracking=0)
    icon_url = fields.Char(string='Icon URL', readonly=True, tracking=0)
    image_1024 = fields.Text(string='Image 1024', store=True, readonly=True, tracking=0)
    image_128 = fields.Text(string='Image 128', store=True, readonly=True, tracking=0)
    image_1920 = fields.Text(string='Image', store=True, copied=True, tracking=0)
    image_256 = fields.Text(string='Image 256', store=True, readonly=True, tracking=0)
    image_512 = fields.Text(string='Image 512', store=True, readonly=True, tracking=0)
    is_hidden = fields.Boolean(string='Almacenamiento está oculto', store=True, readonly=True, tracking=0)
    is_lock_editor = fields.Boolean(string='Editor', readonly=True, tracking=0)
    is_locked = fields.Boolean(string='Bloqueado', readonly=True, tracking=0)
    message_attachment_count = fields.Integer(string='Nº de adjuntos', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Número de error', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Error de entrega de mensaje', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='Error de entrega de SMS', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Es seguidor', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Acción necesaria', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Nº de mensajes no leídos', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Mensajes no leídos', readonly=True, tracking=0)
    migration = fields.Char(string='Estado de migración', readonly=True, tracking=0)
    mimetype = fields.Char(string='Tipo', store=True, readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Nombre', index=True, store=True, required=True, copied=True, tracking=0)
    path_json = fields.Text(string='Path Json', readonly=True, tracking=0)
    path_names = fields.Char(string='Nombres de ruta', readonly=True, tracking=0)
    permission_create = fields.Boolean(string='Acceso de creación', readonly=True, tracking=0)
    permission_read = fields.Boolean(string='Acceso de lectura', readonly=True, tracking=0)
    permission_unlink = fields.Boolean(string='Acceso de eliminación', readonly=True, tracking=0)
    permission_write = fields.Boolean(string='Acceso de escritura', readonly=True, tracking=0)
    require_migration = fields.Boolean(string='Requiere migración', store=True, readonly=True, tracking=0)
    res_id = fields.Integer(string='ID de registro de archivos adjuntos vinculados', index=True, store=True, readonly=True, tracking=0)
    res_model = fields.Char(string='Modelo de adjuntos vinculado', index=True, store=True, readonly=True, tracking=0)
    save_type = fields.Char(string='Tipo de guardado actual', readonly=True, tracking=0)
    size = fields.Integer(string='Tamaño', store=True, readonly=True, copied=True, tracking=0)

class DmsMixinsThumbnail(models.Model):
    _name = 'dms.mixins.thumbnail'
    _description = 'Miniaturas DMS'

    icon_url = fields.Char(string='Icon URL', readonly=True, tracking=0)
    image_1024 = fields.Text(string='Image 1024', store=True, readonly=True, tracking=0)
    image_128 = fields.Text(string='Image 128', store=True, readonly=True, tracking=0)
    image_1920 = fields.Text(string='Image', store=True, copied=True, tracking=0)
    image_256 = fields.Text(string='Image 256', store=True, readonly=True, tracking=0)
    image_512 = fields.Text(string='Image 512', store=True, readonly=True, tracking=0)

class DmsSecurityMixin(models.Model):
    _name = 'dms.security.mixin'
    _description = 'Mezcla de seguridad DMS'

    permission_create = fields.Boolean(string='Acceso de creación', readonly=True, tracking=0)
    permission_read = fields.Boolean(string='Acceso de lectura', readonly=True, tracking=0)
    permission_unlink = fields.Boolean(string='Acceso de eliminación', readonly=True, tracking=0)
    permission_write = fields.Boolean(string='Acceso de escritura', readonly=True, tracking=0)
    res_id = fields.Integer(string='ID de registro de archivos adjuntos vinculados', index=True, store=True, copied=True, tracking=0)
    res_model = fields.Char(string='Modelo de adjuntos vinculado', index=True, store=True, copied=True, tracking=0)

class DmsStorage(models.Model):
    _name = 'dms.storage'
    _description = 'Almacenamiento DMS'

    count_storage_directories = fields.Integer(string='Nº de carpetas', readonly=True, tracking=0)
    count_storage_files = fields.Integer(string='Nº de archivos', readonly=True, tracking=0)
    include_message_attachments = fields.Boolean(string='Create files from message attachments', store=True, copied=True, tracking=0)
    inherit_access_from_parent_record = fields.Boolean(string='Inherit permissions from related record', store=True, copied=True, tracking=0)
    is_hidden = fields.Boolean(string='Almacenamiento está oculto', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)

class DmsTag(models.Model):
    _name = 'dms.tag'
    _description = 'Etiquetas DMS'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0)
    color = fields.Integer(string='Índice de color', store=True, copied=True, tracking=0)
    count_directories = fields.Integer(string='Nº de carpetas', readonly=True, tracking=0)
    count_files = fields.Integer(string='Nº de archivos', readonly=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)

class DocumentPage(models.Model):
    _name = 'document.page'
    _description = 'Páginas de documento'

    active = fields.Boolean(string='Active', store=True, copied=True, tracking=0)
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    backend_url = fields.Char(string='Backend URL', readonly=True, tracking=0)
    content_date = fields.Datetime(string='Last Contribution Date', index=True, store=True, readonly=True, tracking=0)
    content = fields.Text(string='Contenido', tracking=0)
    draft_name = fields.Char(string='Nombre', tracking=0)
    draft_summary = fields.Char(string='Resumen', tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='Error de entrega del SMS', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Título', store=True, required=True, copied=True, tracking=0)
    template = fields.Html(string='Plantilla', store=True, copied=True, tracking=0)

class DocumentPageCreateMenu(models.Model):
    _name = 'document.page.create.menu'
    _description = 'Menú de creación de páginas de documento'

    menu_name = fields.Char(string='Nombre del menú', store=True, required=True, copied=True, tracking=0)

class DocumentPageHistory(models.Model):
    _name = 'document.page.history'
    _description = 'Historial de páginas de documento'

    content = fields.Text(string='Contenido', store=True, copied=True, tracking=0)
    diff = fields.Text(string='Diff', readonly=True, tracking=0)
    name = fields.Char(string='Nombre', index=True, store=True, copied=True, tracking=0)
    summary = fields.Char(string='Resumen', index=True, store=True, copied=True, tracking=0)

class EconomicVariable(models.Model):
    _name = 'economic.variable'
    _description = 'Variables económicas'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0)
    code = fields.Char(string='Código', store=True, readonly=True, required=True, copied=True, tracking=0)
    compute_value = fields.Boolean(string='Valor calculado', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, readonly=True, required=True, copied=True, tracking=0)

class EconomicVariableLine(models.Model):
    _name = 'economic.variable.line'
    _description = 'Líneas de variables económicas'

    compute_value = fields.Boolean(string='Valor calculado', readonly=True, tracking=0)
    value = fields.Float(string='Valor', store=True, copied=True, tracking=0)

class EconomicVariableLineDetail(models.Model):
    _name = 'economic.variable.line.detail'
    _description = 'Detalles de líneas de variables económicas'

    add = fields.Float(string='UVTs a Sumar', store=True, copied=True, tracking=0)
    has_lower_limit = fields.Boolean(string='Tiene límite inferior', store=True, copied=True, tracking=0)
    has_upper_limit = fields.Boolean(string='Tiene límite superior', store=True, copied=True, tracking=0)
    lower_limit = fields.Float(string='Límite inferior', store=True, copied=True, tracking=0)
    rate = fields.Float(string='Porcentaje', store=True, copied=True, tracking=0)
    subtract = fields.Float(string='UVTs a Restar', store=True, copied=True, tracking=0)
    upper_limit = fields.Float(string='Límite superior', store=True, copied=True, tracking=0)

class EiMultiProcess(models.Model):
    _name = 'ei.multi.process'
    _description = 'Procesos múltiples de facturación electrónica'

    invoices = fields.Text(string='Facturas por Procesar', store=True, readonly=True, copied=True, tracking=0)

class EinvoiceNotificationGroup(models.Model):
    _name = 'einvoice.notification.group'
    _description = 'Grupos de notificación de facturación electrónica'

    email = fields.Char(string='Correo electrónico', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class EiTransactionLog(models.Model):
    _name = 'ei.transaction.log'
    _description = 'Registro de transacciones de facturación electrónica'

    content = fields.Text(string='Contenido', store=True, readonly=True, copied=True, tracking=0)
    date = fields.Datetime(string='Fecha', store=True, readonly=True, copied=True, tracking=0)

class ElectronicInvoiceResolution(models.Model):
    _name = 'electronic.invoice.resolution'
    _description = 'Resoluciones de facturación electrónica'

    description = fields.Text(string='Texto de Resolución', store=True, copied=True, tracking=0)
    from_number = fields.Integer(string='Numeración Desde', store=True, tracking=0)
    id_param = fields.Integer(string='ID Resolución', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    number = fields.Char(string='Número de Resolución', store=True, copied=True, tracking=0)
    prefix = fields.Char(string='Prefijo', store=True, required=True, copied=True, tracking=0)
    technical_key = fields.Char(string='Clave Técnica', store=True, tracking=0)
    to_number = fields.Integer(string='Numeración Hasta', store=True, tracking=0)
    valid_date_from = fields.Date(string='Fecha Inicio Resolución', store=True, tracking=0)
    valid_date_to = fields.Date(string='Fecha Fin Resolución', store=True, tracking=0)

class EmailCelulares(models.Model):
    _name = 'email.celulares'
    _description = 'Emails para celulares'

    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Name', store=True, copied=True, tracking=1)
    x_pass = fields.Char(string='Contraseña Correo', store=True, copied=True, tracking=1)

class EpidemiologicalSurveillanceProgram(models.Model):
    _name = 'epidemiological.surveillance.program'
    _description = 'Programas de vigilancia epidemiológica'

    activity_date_deadline = fields.Date(string='Siguiente plazo de actividad', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Resumen de la siguiente actividad', tracking=0)
    activity_type_icon = fields.Char(string='Ícono de tipo de actividad', readonly=True, tracking=0)
    message_attachment_count = fields.Integer(string='Nº de archivos adjuntos', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Número de errores', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Error de Envío de Mensaje', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='Error de entrega del SMS', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Es un seguidor', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Acción requerida', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Nº de mensajes sin leer', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Mensajes sin leer', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='Mi fecha límite de actividad', readonly=True, tracking=0)
    name = fields.Char(string='Programa De Vigilancia Epidemiológica', store=True, copied=True, tracking=0)

class EpsUpdateHistory(models.Model):
    _name = 'eps.update.history'
    _description = 'Historial de actualizaciones de EPS'

    date = fields.Date(string='Fecha', store=True, required=True, copied=True, tracking=0)

class EstadoDeLinea(models.Model):
    _name = 'estado.de.linea'
    _description = 'Estados de línea'

    name = fields.Char(string='Name', store=True, copied=True, tracking=1)

class EstadoDispositivo(models.Model):
    _name = 'estado.dispositivo'
    _description = 'Estados de dispositivo'

    name = fields.Char(string='Name', store=True, copied=True, tracking=1)

class EstadoEstudiosCapacitaciones(models.Model):
    _name = 'estado.estudios.capacitaciones'
    _description = 'Estados de estudios y capacitaciones'

    name = fields.Char(string='Estado', store=True, required=True, copied=True, tracking=0)

class EstudiosCapacitaciones(models.Model):
    _name = 'estudios.capacitaciones'
    _description = 'Estudios y capacitaciones'

    comentarios = fields.Text(string='Comentarios', store=True, copied=True, tracking=0)
    duracion = fields.Float(string='Duración', store=True, copied=True, tracking=0)
    fecha_inicio = fields.Date(string='Fecha de Inicio', store=True, copied=True, tracking=0)
    fecha_terminacion = fields.Date(string='Fecha de Terminación', store=True, copied=True, tracking=0)
    fecha_vencimiento = fields.Date(string='Fecha Vencimiento Estudio/Curso', store=True, copied=True, tracking=0)
    numero_registro = fields.Char(string='Número de Registro', store=True, copied=True, tracking=0)
    periodo_curso = fields.Char(string='Periodo en Curso', store=True, copied=True, tracking=0)

class ExamenesMedicos(models.Model):
    _name = 'examenes.medicos'
    _description = 'Exámenes médicos'

    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    cargo = fields.Char(string='Cargo', store=True, readonly=True, tracking=0)
    celular = fields.Char(string='Celular', store=True, readonly=True, tracking=0)
    dias_incapacidad = fields.Integer(string='Días de incapacidad', store=True, copied=True, tracking=0)
    edad = fields.Integer(string='Edad', store=True, readonly=True, tracking=0)
    eps = fields.Char(string='Eps', store=True, readonly=True, tracking=0)
    especificas_temporalidad = fields.Integer(string='Temporalidad en meses', store=True, copied=True, tracking=0)
    fecha_ingreso = fields.Char(string='Fecha de Ingreso a la Empresa', store=True, readonly=True, tracking=0)
    fecha_nacimiento = fields.Char(string='Fecha de Nacimiento', store=True, readonly=True, tracking=0)
    fecha_probable_seguimiento = fields.Date(string='Fecha probable de seguimiento', store=True, readonly=True, tracking=0)
    fecha_realizacion = fields.Date(string='Fecha de Realización', store=True, required=True, copied=True, tracking=0)
    fecha_vencimiento = fields.Date(string='Fecha de vencimiento', store=True, copied=True, tracking=0)
    fondo_pension = fields.Char(string='Fondo de pensión', store=True, readonly=True, tracking=0)
    imc = fields.Float(string='Ingrese el IMC', store=True, copied=True, tracking=0)
    ips = fields.Text(string='Ips', store=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    numero_identificacion = fields.Char(string='Número de Identificación', store=True, required=True, copied=True, tracking=0)
    observaciones = fields.Text(string='Observaciones', store=True, copied=True, tracking=0)
    otro_programa = fields.Text(string='Otro programa', store=True, copied=True, tracking=0)
    programas_seleccionados = fields.Char(string='Programas Seleccionados', store=True, readonly=True, tracking=0)
    recomendacion_permanente = fields.Boolean(string='Recomendación permanente', store=True, copied=True, tracking=0)
    recomendaciones_especificas_Text = fields.Text(string='Recomendaciones específicas Text', store=True, copied=True, tracking=0)
    recomendaciones_generales_Text = fields.Text(string='Recomendaciones generales Text', store=True, copied=True, tracking=0)
    remisiones_medicas = fields.Text(string='Remisiones médicas', store=True, copied=True, tracking=0)
    restriccion_permanente = fields.Boolean(string='Restricción permanente', store=True, copied=True, tracking=0)
    restricciones_temporalidad = fields.Integer(string='Temporalidad en meses', store=True, copied=True, tracking=0)
    restricciones_Text = fields.Text(string='Restricciones', store=True, copied=True, tracking=0)
    subzona = fields.Char(string='Subzona', store=True, readonly=True, tracking=0)
    telefono = fields.Char(string='Teléfono', store=True, readonly=True, tracking=0)
    tipo_contrato = fields.Char(string='Tipo de contrato', store=True, readonly=True, tracking=0)
    valor_imc = fields.Char(string='El IMC es', store=True, readonly=True, tracking=0)
    zona = fields.Char(string='Zona', store=True, readonly=True, tracking=0)

class ExamenesMedicosSeguimiento(models.Model):
    _name = 'examenes.medicos.seguimiento'
    _description = 'Seguimiento de exámenes médicos'

    fecha_seguimiento = fields.Date(string='Fecha de Seguimiento', store=True, required=True, copied=True, tracking=0)
    observacion = fields.Text(string='Observación', store=True, copied=True, tracking=0)

class ExcelReportAvancys(models.Model):
    _name = 'excel.report.avancys'
    _description = 'Reportes Excel Avancys'

    excel_file = fields.Text(string='Reporte Excel', store=True, copied=True, tracking=0)
    file_name = fields.Char(string='Archivo Excel', store=True, copied=True, tracking=0)

class ExpiryPickingConfirmation(models.Model):
    _name = 'expiry.picking.confirmation'
    _description = 'Confirmación de picking por vencimiento'

    description = fields.Char(string='Descripción', readonly=True, tracking=0)
    show_lots = fields.Boolean(string='Mostrar lotes', readonly=True, tracking=0)

class FacturacionWiz(models.Model):
    _name = 'facturacion.wiz'
    _description = 'Asistente de facturación'

    date_invoice = fields.Date(string='Fecha de facturación', store=True, required=True, copied=True, tracking=0)
    detalle = fields.Boolean(string='Detallado', store=True, copied=True, tracking=0)

class FivepState(models.Model):
    _name = 'fivep.state'
    _description = 'Estados FiveP'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class FleetVehicleSubState(models.Model):
    _name = 'fleet.vehicle.sub.state'
    _description = 'Subestados de vehículos de flota'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=1)

class FpaAuxiliar(models.Model):
    _name = 'fpa.auxiliar'
    _description = 'Auxiliar FPA'

    date_from = fields.Date(string='Fecha Inicial', store=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha Final', store=True, copied=True, tracking=0)
    date = fields.Datetime(string='Fecha', store=True, copied=True, tracking=0)

class FpaAuxiliarAnalitico(models.Model):
    _name = 'fpa.auxiliar.analitico'
    _description = 'Auxiliar analítico FPA'

    date_from = fields.Date(string='Fecha Inicial', store=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha Final', store=True, copied=True, tracking=0)
    date = fields.Datetime(string='Fecha', store=True, copied=True, tracking=0)

class FpaAuxiliarAnaliticoLine(models.Model):
    _name = 'fpa.auxiliar.analitico.line'
    _description = 'Líneas de auxiliar analítico FPA'

    amount_currency = fields.Float(string='Monto moneda', store=True, copied=True, tracking=0)
    amount_final = fields.Float(string='Saldo Final', store=True, copied=True, tracking=0)
    amount_inicial = fields.Float(string='Saldo Inicial', store=True, copied=True, tracking=0)
    asiento = fields.Char(string='Asiento', store=True, copied=True, tracking=0)
    bold = fields.Boolean(string='bold', store=True, copied=True, tracking=0)
    credit = fields.Float(string='Crédito', store=True, copied=True, tracking=0)
    cuenta = fields.Char(string='Cuenta', store=True, copied=True, tracking=0)
    debit = fields.Float(string='Débito', store=True, copied=True, tracking=0)
    fecha = fields.Date(string='Fecha', store=True, copied=True, tracking=0)
    nivel = fields.Integer(string='Nivel', store=True, copied=True, tracking=0)
    resume = fields.Boolean(string='Resumen', store=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)

class FpaAuxiliarAnaliticoWizard(models.Model):
    _name = 'fpa.auxiliar.analitico.wizard'
    _description = 'Asistente de auxiliar analítico FPA'

    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copied=True, tracking=0)
    analytic_filter = fields.Boolean(string='Filtro adicional de cuenta analítica', store=True, copied=True, tracking=0)
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha final', store=True, required=True, copied=True, tracking=0)
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copied=True, tracking=0)
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copied=True, tracking=0)
    show_currency = fields.Boolean(string='Mostrar valor en otra moneda', store=True, copied=True, tracking=0)

class FpaAuxiliarEquivalente(models.Model):
    _name = 'fpa.auxiliar.equivalente'
    _description = 'Auxiliar equivalente FPA'

    date_from = fields.Date(string='Fecha Inicial', store=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha Final', store=True, copied=True, tracking=0)
    date = fields.Datetime(string='Fecha', store=True, copied=True, tracking=0)

class FpaAuxiliarEquivalenteLine(models.Model):
    _name = 'fpa.auxiliar.equivalente.line'
    _description = 'Líneas de auxiliar equivalente FPA'

    amount_final = fields.Float(string='Saldo Final', store=True, copied=True, tracking=0)
    amount_inicial = fields.Float(string='Saldo Inicial', store=True, copied=True, tracking=0)
    asiento = fields.Char(string='Asiento', store=True, copied=True, tracking=0)
    bold = fields.Boolean(string='bold', store=True, copied=True, tracking=0)
    credit_c = fields.Float(string='Crédito', store=True, copied=True, tracking=0)
    credit = fields.Float(string='Crédito', store=True, copied=True, tracking=0)
    cuenta = fields.Char(string='Cuenta', store=True, copied=True, tracking=0)
    debit_c = fields.Float(string='Débito', store=True, copied=True, tracking=0)
    debit = fields.Float(string='Débito', store=True, copied=True, tracking=0)
    fecha = fields.Date(string='Fecha', store=True, copied=True, tracking=0)
    nivel = fields.Integer(string='Nivel', store=True, copied=True, tracking=0)
    resume = fields.Boolean(string='Resumen', store=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)

class FpaAuxiliarEquivalenteWizard(models.Model):
    _name = 'fpa.auxiliar.equivalente.wizard'
    _description = 'Asistente de auxiliar equivalente FPA'

    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copied=True, tracking=0)
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha final', store=True, required=True, copied=True, tracking=0)
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copied=True, tracking=0)
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copied=True, tracking=0)
    sp_periods = fields.Boolean(string='Apertura/Cierre', store=True, copied=True, tracking=0)

class FpaAuxiliarFc(models.Model):
    _name = 'fpa.auxiliar.fc'
    _description = 'Auxiliar FC FPA'

    date_from = fields.Date(string='Fecha Inicial', store=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha Final', store=True, copied=True, tracking=0)
    date = fields.Datetime(string='Fecha', store=True, copied=True, tracking=0)

class FpaAuxiliarFcLine(models.Model):
    _name = 'fpa.auxiliar.fc.line'
    _description = 'Líneas de auxiliar FC FPA'

    af_fc = fields.Float(string='SF - ME', store=True, copied=True, tracking=0)
    ai_fc = fields.Float(string='SI - ME', store=True, copied=True, tracking=0)
    amount_final = fields.Float(string='Saldo Final', store=True, copied=True, tracking=0)
    amount_inicial = fields.Float(string='Saldo Inicial', store=True, copied=True, tracking=0)
    asiento = fields.Char(string='Asiento', store=True, copied=True, tracking=0)
    bold = fields.Boolean(string='bold', store=True, copied=True, tracking=0)
    credit = fields.Float(string='Crédito', store=True, copied=True, tracking=0)
    cuenta = fields.Char(string='Cuenta', store=True, copied=True, tracking=0)
    debit = fields.Float(string='Débito', store=True, copied=True, tracking=0)
    fecha = fields.Date(string='Fecha', store=True, copied=True, tracking=0)
    linea = fields.Char(string='Línea', store=True, copied=True, tracking=0)
    mv_fc = fields.Float(string='DC - ME', store=True, copied=True, tracking=0)
    nivel = fields.Integer(string='Nivel', store=True, copied=True, tracking=0)
    resume = fields.Boolean(string='Resumen', store=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)

class FpaAuxiliarFcWizard(models.Model):
    _name = 'fpa.auxiliar.fc.wizard'
    _description = 'Asistente de auxiliar FC FPA'

    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copied=True, tracking=0)
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha final', store=True, required=True, copied=True, tracking=0)
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copied=True, tracking=0)
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copied=True, tracking=0)
    sp_periods = fields.Boolean(string='Apertura/Cierre', store=True, copied=True, tracking=0)

class FpaAuxiliarLine(models.Model):
    _name = 'fpa.auxiliar.line'
    _description = 'Líneas de auxiliar FPA'

    amount_final = fields.Float(string='Saldo Final', store=True, copied=True, tracking=0)
    amount_inicial = fields.Float(string='Saldo Inicial', store=True, copied=True, tracking=0)
    asiento = fields.Char(string='Asiento', store=True, copied=True, tracking=0)
    bold = fields.Boolean(string='bold', store=True, copied=True, tracking=0)
    credit = fields.Float(string='Crédito', store=True, copied=True, tracking=0)
    cuenta = fields.Char(string='Cuenta', store=True, copied=True, tracking=0)
    debit = fields.Float(string='Débito', store=True, copied=True, tracking=0)
    fecha = fields.Date(string='Fecha', store=True, copied=True, tracking=0)
    linea = fields.Char(string='Línea', store=True, copied=True, tracking=0)
    nivel = fields.Integer(string='Nivel', store=True, copied=True, tracking=0)
    resume = fields.Boolean(string='Resumen', store=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)
    sucursal_name = fields.Char(string='Sucursal', store=True, copied=True, tracking=0)

class FpaAuxiliarWizard(models.Model):
    _name = 'fpa.auxiliar.wizard'
    _description = 'Asistente de auxiliar FPA'

    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copied=True, tracking=0)
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha final', store=True, required=True, copied=True, tracking=0)
    detailed = fields.Boolean(string='Detallado', store=True, copied=True, tracking=0)
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copied=True, tracking=0)
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copied=True, tracking=0)
    sp_periods = fields.Boolean(string='Apertura/Cierre', store=True, copied=True, tracking=0)
    totalizado_por_tercero = fields.Boolean(string='Totalizador por tercero', store=True, copied=True, tracking=0)

class FpaBalancePruebas(models.Model):
    _name = 'fpa.balance.pruebas'
    _description = 'Balance de pruebas FPA'

    date_from = fields.Date(string='Fecha Inicial', store=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha Final', store=True, copied=True, tracking=0)
    date = fields.Datetime(string='Fecha', store=True, copied=True, tracking=0)

class FpaBalancePruebasLine(models.Model):
    _name = 'fpa.balance.pruebas.line'
    _description = 'Líneas de balance de pruebas FPA'

    amount_final = fields.Float(string='Saldo Final', store=True, copied=True, tracking=0)
    amount_inicial = fields.Float(string='Saldo Inicial', store=True, copied=True, tracking=0)
    bold = fields.Boolean(string='bold', store=True, copied=True, tracking=0)
    credit = fields.Float(string='Crédito', store=True, copied=True, tracking=0)
    cuenta = fields.Char(string='Cuenta', store=True, copied=True, tracking=0)
    debit = fields.Float(string='Débito', store=True, copied=True, tracking=0)
    nivel = fields.Integer(string='Nivel', store=True, copied=True, tracking=0)
    resume = fields.Boolean(string='Resumen', store=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)
    sucursal_name = fields.Char(string='Sucursal', store=True, copied=True, tracking=0)

class FpaBalancePruebasWizard(models.Model):
    _name = 'fpa.balance.pruebas.wizard'
    _description = 'Asistente de balance de pruebas FPA'

    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copied=True, tracking=0)
    cierre = fields.Boolean(string='Cierre', store=True, copied=True, tracking=0)
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha final', store=True, required=True, copied=True, tracking=0)
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copied=True, tracking=0)
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copied=True, tracking=0)
    resume = fields.Boolean(string='Resumen', store=True, copied=True, tracking=0)
    sp_periods = fields.Boolean(string='Apertura/Cierre', store=True, copied=True, tracking=0)

class FpaDiario(models.Model):
    _name = 'fpa.diario'
    _description = 'Diario FPA'

    date_from = fields.Date(string='Fecha Inicial', store=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha Final', store=True, copied=True, tracking=0)
    date = fields.Datetime(string='Fecha', store=True, copied=True, tracking=0)

class FpaDiarioLine(models.Model):
    _name = 'fpa.diario.line'
    _description = 'Líneas de diario FPA'

    asiento = fields.Char(string='Asiento', store=True, copied=True, tracking=0)
    bold = fields.Boolean(string='bold', store=True, copied=True, tracking=0)
    credit = fields.Float(string='Crédito', store=True, copied=True, tracking=0)
    cuenta = fields.Char(string='Cuenta', store=True, copied=True, tracking=0)
    debit = fields.Float(string='Débito', store=True, copied=True, tracking=0)
    fecha = fields.Date(string='Fecha', store=True, copied=True, tracking=0)
    nivel = fields.Integer(string='Nivel', store=True, copied=True, tracking=0)
    resume = fields.Boolean(string='Resumen', store=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)

class FpaDiarioWizard(models.Model):
    _name = 'fpa.diario.wizard'
    _description = 'Asistente de diario FPA'

    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copied=True, tracking=0)
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha final', store=True, required=True, copied=True, tracking=0)
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copied=True, tracking=0)
    sp_periods = fields.Boolean(string='Apertura/Cierre', store=True, copied=True, tracking=0)

class FpaEquityChanges(models.Model):
    _name = 'fpa.equity.changes'
    _description = 'Cambios de patrimonio FPA'

    amount_label_comparative = fields.Char(string='Etiqueta monto comparativo', store=True, copied=True, tracking=0)
    date_from = fields.Date(string='Fecha Inicial', store=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha Final', store=True, copied=True, tracking=0)
    date = fields.Datetime(string='Fecha', store=True, copied=True, tracking=0)

class FpaEquityChangesLine(models.Model):
    _name = 'fpa.equity.changes.line'
    _description = 'Líneas de cambios de patrimonio FPA'

    amount_comparative = fields.Float(string='Saldo Comparativo', store=True, copied=True, tracking=0)
    amount_final = fields.Float(string='Saldo Final', store=True, copied=True, tracking=0)
    aumentos = fields.Float(string='Aumento', store=True, copied=True, tracking=0)
    bold = fields.Boolean(string='bold', store=True, copied=True, tracking=0)
    credit = fields.Float(string='Crédito', store=True, copied=True, tracking=0)
    cuenta = fields.Char(string='Cuenta', store=True, copied=True, tracking=0)
    debit = fields.Float(string='Débito', store=True, copied=True, tracking=0)
    disminuciones = fields.Float(string='Disminuciones', store=True, copied=True, tracking=0)
    nivel = fields.Integer(string='Nivel', store=True, copied=True, tracking=0)
    resume = fields.Boolean(string='Resumen', store=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)

class FpaEquityChangesWizard(models.Model):
    _name = 'fpa.equity.changes.wizard'
    _description = 'Asistente de cambios de patrimonio FPA'

    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copied=True, tracking=0)
    analytic_filter = fields.Boolean(string='Filtro adicional de cuenta analítica', store=True, copied=True, tracking=0)
    cierre = fields.Boolean(string='Cierre', store=True, copied=True, tracking=0)
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha final', store=True, required=True, copied=True, tracking=0)
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copied=True, tracking=0)
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copied=True, tracking=0)

class FpaExportWizardEpt(models.Model):
    _name = 'fpa.export.wizard.ept'
    _description = 'Asistente de exportación EPT FPA'

    concept_code = fields.Char(string='Código de concepto', store=True, copied=True, tracking=0)
    date_cut = fields.Date(string='Hasta', readonly=True, tracking=0)
    date_from = fields.Date(string='Desde', store=True, copied=True, tracking=0)
    date_to = fields.Date(string='Hasta', store=True, copied=True, tracking=0)
    export_contract = fields.Boolean(string='Contatos', store=True, copied=True, tracking=0)
    export = fields.Boolean(string='Medios', store=True, copied=True, tracking=0)
    is_payslip = fields.Boolean(string='Es Nómina', store=True, copied=True, tracking=0)
    message = fields.Char(string='Message', store=True, readonly=True, copied=True, tracking=0)
    workcenter = fields.Char(string='Centro de trabajo', store=True, copied=True, tracking=0)

# class FpaFinancialReports(models.Model):
#     _name = 'fpa.financial.reports'
#     _description = 'Reportes financieros FPA'
#
#     account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copied=True, tracking=0)
#     accumulated = fields.Boolean(string='Acumulado', store=True, copied=True, tracking=0)
#     action = fields.Char(string='Acción', store=True, copied=True, tracking=0)
#     analytic_filter = fields.Boolean(string='Filtro adicional de cuentas analíticas', store=True, copied=True, tracking=0)
#     analyze = fields.Boolean(string='Analizar', store=True, copied=True, tracking=0)
#     cierre = fields.Boolean(string='Cierre', store=True, copied=True, tracking=0)
#     clase = fields.Boolean(string='Clase', store=True, copied=True, tracking=0)
#     codigo = fields.Boolean(string='Código', store=True, copied=True, tracking=0)
#     consulta_xlsx = fields.Text(string='Consulta XLSX', store=True, copied=True, tracking=0)
#     consulta = fields.Text(string='Consulta PDF', store=True, copied=True, tracking=0)
#     detailed = fields.Boolean(string='Detallado', store=True, copied=True, tracking=0)
#     detalle = fields.Boolean(string='Detalle', store=True, copied=True, tracking=0)
#     domain = fields.Char(string='Dominio vista tree', store=True, copied=True, tracking=0)
#     equivalente = fields.Boolean(string='Equivalente NIIF', store=True, copied=True, tracking=0)
#     export_contract = fields.Boolean(string='Contatos', store=True, copied=True, tracking=0)
#     export = fields.Boolean(string='Exportación', store=True, copied=True, tracking=0)
#     field_hidden = fields.Char(string='Campos a ocultar', store=True, copied=True, tracking=0)
#     fields = fields.Char(string='Campos', store=True, copied=True, tracking=0)
#     # form = fields.Char(string='Form', store=True, copied=True, tracking=0)
#     # format_date = fields.Char(string='Formato Fecha', store=True, copied=True, tracking=0)
#     # format_money = fields.Char(string='Formato Dinero', store=True, copied=True, tracking=0)
#     # formato = fields.Char(string='Formato', store=True, copied=True, tracking=0)
#     # indentacion = fields.Integer(string='Indentación', store=True, copied=True, tracking=0)
#     # is_payslip = fields.Boolean(string='Es Nómina', store=True, copied=True, tracking=0)
#     journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copied=True, tracking=0)
#     message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
#     message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
#     message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
#     message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
#     message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
#     message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
#     message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
#     message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
#     message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
#     mode = fields.Char(string='Modo de vista', store=True, required=True, copied=True, tracking=0)
#     model_wzr = fields.Char(string='Modelo Wizard', store=True, copied=True, tracking=0)
#     model = fields.Char(string='Modelo', store=True, copied=True, tracking=0)
#     name = fields.Char(string='Nombre del reporte', store=True, copied=True, tracking=0)
#     numeric = fields.Char(string='Columnas moneda', store=True, copied=True, tracking=0)
#     partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copied=True, tracking=0)
#     porc = fields.Char(string='Columnas %', store=True, copied=True, tracking=0)
#     query = fields.Text(string='Consulta SQL', store=True, copied=True, tracking=0)
#     search_default = fields.Char(string='Search por defecto (tree)', store=True, copied=True, tracking=0)
#     sign = fields.Boolean(string='Invertir signo', store=True, copied=True, tracking=0)
#     sum_column = fields.Boolean(string='Totalizar', store=True, copied=True, tracking=0)
#     template = fields.Char(string='Plantilla QWEB', store=True, copied=True, tracking=0)
#     title_color = fields.Char(string='Color títulos', store=True, copied=True, tracking=0)
#     title = fields.Char(string='Título', store=True, copied=True, tracking=0)
#     tope_min = fields.Float(string='Tope mínimo', store=True, copied=True, tracking=0)
#     totalizado_por_tercero = fields.Boolean(string='Totalizado por Tercero', store=True, copied=True, tracking=0)
#     tree = fields.Char(string='Tree', store=True, copied=True, tracking=0)
#     unidades = fields.Char(string='Unidades', store=True, copied=True, tracking=0)
#     view_color = fields.Char(string='Color resumen', store=True, copied=True, tracking=0)
#     view = fields.Char(string='Vista', store=True, copied=True, tracking=0)
#     with_exlusion = fields.Boolean(string='Con Exclusión', store=True, copied=True, tracking=0)
#     with_min_cuantias = fields.Boolean(string='Con CUANTÍAS MENORES', store=True, copied=True, tracking=0)

class FpaFinancialReportsColumns(models.Model):
    _name = 'fpa.financial.reports.columns'
    _description = 'Columnas de reportes financieros FPA'

    code = fields.Char(string='Código concepto', store=True, copied=True, tracking=0)

class FpaFinancialReportsConcepts(models.Model):
    _name = 'fpa.financial.reports.concepts'
    _description = 'Conceptos de reportes financieros FPA'

    accumulated = fields.Boolean(string='¿Acumulado?', store=True, copied=True, tracking=0)
    before = fields.Boolean(string='¿Antes del detalle?', store=True, copied=True, tracking=0)
    cierre = fields.Boolean(string='Cierre', store=True, copied=True, tracking=0)
    code = fields.Char(string='Código concepto', store=True, copied=True, tracking=0)
    detail = fields.Boolean(string='¿Con detalle?', store=True, copied=True, tracking=0)
    name = fields.Char(string='Concepto', store=True, required=True, copied=True, tracking=0)
    resume = fields.Boolean(string='¿Solo en Resumen?', store=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, required=True, copied=True, tracking=0)
    tipo = fields.Boolean(string='¿Filtrar por tipo de cuenta?', store=True, copied=True, tracking=0)



class FpaFinancialReportsConceptsColumns(models.Model):
    _name = 'fpa.financial.reports.concepts.columns'
    _description = 'Columnas de conceptos de reportes financieros FPA'

    code = fields.Char(string='Código concepto', store=True, copied=True, tracking=0)
    name = fields.Char(string='Concepto', store=True, required=True, copied=True, tracking=0)

class FpaFinancialReportsConceptsColumnsLines(models.Model):
    _name = 'fpa.financial.reports.concepts.columns.lines'
    _description = 'Líneas de columnas de conceptos de reportes financieros FPA'

    name = fields.Char(string='Descripción', store=True, copied=True, tracking=0)

class FpaFinancialReportsPeriod(models.Model):
    _name = 'fpa.financial.reports.period'
    _description = 'Períodos de reportes financieros FPA'

    date_from = fields.Date(string='Desde', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Hasta', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Etiqueta', store=True, required=True, copied=True, tracking=0)

class FpaFinancialReportsPeriodRange(models.Model):
    _name = 'fpa.financial.reports.period.range'
    _description = 'Rango de períodos de reportes financieros FPA'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)

class FpaFlujocaja(models.Model):
    _name = 'fpa.flujocaja'
    _description = 'Flujo de caja FPA'

    date_from = fields.Date(string='Fecha Inicial', store=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha Final', store=True, copied=True, tracking=0)
    date = fields.Datetime(string='Fecha', store=True, copied=True, tracking=0)

class FpaFlujocajaLine(models.Model):
    _name = 'fpa.flujocaja.line'
    _description = 'Líneas de flujo de caja FPA'

    amount_01 = fields.Float(string='Enero', store=True, copied=True, tracking=0)
    amount_02 = fields.Float(string='Febrero', store=True, copied=True, tracking=0)
    amount_03 = fields.Float(string='Marzo', store=True, copied=True, tracking=0)
    amount_04 = fields.Float(string='Abril', store=True, copied=True, tracking=0)
    amount_05 = fields.Float(string='Mayo', store=True, copied=True, tracking=0)
    amount_06 = fields.Float(string='Junio', store=True, copied=True, tracking=0)
    amount_07 = fields.Float(string='Julio', store=True, copied=True, tracking=0)
    amount_08 = fields.Float(string='Agosto', store=True, copied=True, tracking=0)
    amount_09 = fields.Float(string='Septiembre', store=True, copied=True, tracking=0)
    amount_10 = fields.Float(string='Octubre', store=True, copied=True, tracking=0)
    amount_11 = fields.Float(string='Noviembre', store=True, copied=True, tracking=0)
    amount_12 = fields.Float(string='Diciembre', store=True, copied=True, tracking=0)
    amount_total = fields.Float(string='Monto total', store=True, copied=True, tracking=0)
    bold = fields.Boolean(string='bold', store=True, copied=True, tracking=0)
    cuenta = fields.Char(string='Cuenta', store=True, copied=True, tracking=0)
    description = fields.Text(string='Descripción', store=True, copied=True, tracking=0)
    nivel = fields.Integer(string='Nivel', store=True, copied=True, tracking=0)
    resume = fields.Boolean(string='Resumen', store=True, copied=True, tracking=0)

class FpaFlujocajaWizard(models.Model):
    _name = 'fpa.flujocaja.wizard'
    _description = 'Asistente de flujo de caja FPA'

    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copied=True, tracking=0)
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copied=True, tracking=0)
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copied=True, tracking=0)

class FpaInventarioBalance(models.Model):
    _name = 'fpa.inventario.balance'
    _description = 'Balance de inventario FPA'

    date_from = fields.Date(string='Fecha Inicial', store=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha Final', store=True, copied=True, tracking=0)
    date = fields.Datetime(string='Fecha', store=True, copied=True, tracking=0)

class FpaInventarioBalanceLine(models.Model):
    _name = 'fpa.inventario.balance.line'
    _description = 'Líneas de balance de inventario FPA'

    amount_final = fields.Float(string='Saldo Final', store=True, copied=True, tracking=0)
    amount_inicial = fields.Float(string='Saldo', store=True, copied=True, tracking=0)
    bold = fields.Boolean(string='bold', store=True, copied=True, tracking=0)
    credit = fields.Float(string='Crédito', store=True, copied=True, tracking=0)
    cuenta = fields.Char(string='Cuenta', store=True, copied=True, tracking=0)
    debit = fields.Float(string='Débito', store=True, copied=True, tracking=0)
    nivel = fields.Integer(string='Nivel', store=True, copied=True, tracking=0)
    resume = fields.Boolean(string='Resumen', store=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)

class FpaInventarioBalanceWizard(models.Model):
    _name = 'fpa.inventario.balance.wizard'
    _description = 'Asistente de balance de inventario FPA'

    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copied=True, tracking=0)
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha final', store=True, required=True, copied=True, tracking=0)
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copied=True, tracking=0)
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copied=True, tracking=0)
    sp_periods = fields.Boolean(string='Apertura/Cierre', store=True, copied=True, tracking=0)

class FpaMayorBalance(models.Model):
    _name = 'fpa.mayor.balance'
    _description = 'Mayor balance FPA'

    date_from = fields.Date(string='Fecha Inicial', store=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha Final', store=True, copied=True, tracking=0)
    date = fields.Datetime(string='Fecha', store=True, copied=True, tracking=0)

class FpaMayorBalanceLine(models.Model):
    _name = 'fpa.mayor.balance.line'
    _description = 'Líneas de mayor balance FPA'

    amount_final_credit = fields.Float(string='Saldo Final Crédito', store=True, copied=True, tracking=0)
    amount_final_debit = fields.Float(string='Saldo Final Débito', store=True, copied=True, tracking=0)
    amount_inicial_credit = fields.Float(string='Saldo Inicial Crédito', store=True, copied=True, tracking=0)
    amount_inicial_debit = fields.Float(string='Saldo Inicial Débito', store=True, copied=True, tracking=0)
    bold = fields.Boolean(string='bold', store=True, copied=True, tracking=0)
    credit = fields.Float(string='Crédito', store=True, copied=True, tracking=0)
    cuenta = fields.Char(string='Cuenta', store=True, copied=True, tracking=0)
    debit = fields.Float(string='Débito', store=True, copied=True, tracking=0)
    nivel = fields.Integer(string='Nivel', store=True, copied=True, tracking=0)
    resume = fields.Boolean(string='Resumen', store=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)

class FpaMayorBalanceWizard(models.Model):
    _name = 'fpa.mayor.balance.wizard'
    _description = 'Asistente de mayor balance FPA'

    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copied=True, tracking=0)
    cierre = fields.Boolean(string='Cierre', store=True, copied=True, tracking=0)
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha final', store=True, required=True, copied=True, tracking=0)
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copied=True, tracking=0)
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copied=True, tracking=0)
    sp_periods = fields.Boolean(string='Apertura/Cierre', store=True, copied=True, tracking=0)

class FpaNiveles(models.Model):
    _name = 'fpa.niveles'
    _description = 'Niveles FPA'

    code = fields.Char(string='Código', store=True, required=True, copied=True, tracking=0)
    help = fields.Text(string='Ayuda', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Descripción', store=True, required=True, copied=True, tracking=0)

class FpaPyg(models.Model):
    _name = 'fpa.pyg'
    _description = 'Pérdidas y ganancias FPA'

    date_from = fields.Date(string='Fecha Inicial', store=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha Final', store=True, copied=True, tracking=0)
    date = fields.Datetime(string='Fecha', store=True, copied=True, tracking=0)

class FpaPygC(models.Model):
    _name = 'fpa.pyg.c'
    _description = 'Pérdidas y ganancias comparativas FPA'

    amount_label_comparative = fields.Char(string='Etiqueta monto comparativo', store=True, copied=True, tracking=0)
    date_from = fields.Date(string='Fecha Inicial', store=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha Final', store=True, copied=True, tracking=0)
    date = fields.Datetime(string='Fecha', store=True, copied=True, tracking=0)

class FpaPygCc(models.Model):
    _name = 'fpa.pyg.cc'
    _description = 'Pérdidas y ganancias por centro de costo FPA'

    date_from = fields.Date(string='Fecha Inicial', store=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha Final', store=True, copied=True, tracking=0)
    date = fields.Datetime(string='Fecha', store=True, copied=True, tracking=0)

class FpaPygCcAnalytic(models.Model):
    _name = 'fpa.pyg.cc.analytic'
    _description = 'Pérdidas y ganancias por centro de costo analítico FPA'

    date_from = fields.Date(string='Fecha Inicial', store=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha Final', store=True, copied=True, tracking=0)
    date = fields.Datetime(string='Fecha', store=True, copied=True, tracking=0)

class FpaPygCcAnalyticLine(models.Model):
    _name = 'fpa.pyg.cc.analytic.line'
    _description = 'Líneas de pérdidas y ganancias por centro de costo analítico FPA'

    amount_1 = fields.Float(string='Saldo Año 1', store=True, copied=True, tracking=0)
    amount_2 = fields.Float(string='Saldo Año 2', store=True, copied=True, tracking=0)
    amount_3 = fields.Float(string='Saldo Año 3', store=True, copied=True, tracking=0)
    amount_4 = fields.Float(string='Saldo Año 4', store=True, copied=True, tracking=0)
    amount_5 = fields.Float(string='Saldo Año 5', store=True, copied=True, tracking=0)
    amount_final = fields.Float(string='Saldo Final', store=True, copied=True, tracking=0)
    amount_inicial = fields.Float(string='Saldo Inicial', store=True, copied=True, tracking=0)
    bold = fields.Boolean(string='bold', store=True, copied=True, tracking=0)
    cc1 = fields.Char(string='cc1', store=True, copied=True, tracking=0)
    cc2 = fields.Char(string='cc2', store=True, copied=True, tracking=0)
    cc3 = fields.Char(string='cc3', store=True, copied=True, tracking=0)
    cc4 = fields.Char(string='cc4', store=True, copied=True, tracking=0)
    cc5 = fields.Char(string='cc5', store=True, copied=True, tracking=0)
    credit = fields.Float(string='Crédito', store=True, copied=True, tracking=0)
    cuenta = fields.Char(string='Cuenta', store=True, copied=True, tracking=0)
    debit = fields.Float(string='Débito', store=True, copied=True, tracking=0)
    nivel = fields.Integer(string='Nivel', store=True, copied=True, tracking=0)
    resume = fields.Boolean(string='Resumen', store=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)

class FpaPygCcAnalyticWizard(models.Model):
    _name = 'fpa.pyg.cc.analytic.wizard'
    _description = 'Asistente de pérdidas y ganancias por centro de costo analítico FPA'

    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copied=True, tracking=0)
    analytic_filter = fields.Boolean(string='Filtro adicional de cuenta analítica', store=True, copied=True, tracking=0)
    cierre = fields.Boolean(string='Cierre', store=True, copied=True, tracking=0)
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha final', store=True, required=True, copied=True, tracking=0)
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copied=True, tracking=0)
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copied=True, tracking=0)

class FpaPygCcLine(models.Model):
    _name = 'fpa.pyg.cc.line'
    _description = 'Líneas de pérdidas y ganancias por centro de costo FPA'

    amount_1 = fields.Float(string='Saldo Año 1', store=True, copied=True, tracking=0)
    amount_2 = fields.Float(string='Saldo Año 2', store=True, copied=True, tracking=0)
    amount_3 = fields.Float(string='Saldo Año 3', store=True, copied=True, tracking=0)
    amount_4 = fields.Float(string='Saldo Año 4', store=True, copied=True, tracking=0)
    amount_5 = fields.Float(string='Saldo Año 5', store=True, copied=True, tracking=0)
    amount_final = fields.Float(string='Saldo Final', store=True, copied=True, tracking=0)
    amount_inicial = fields.Float(string='Saldo Inicial', store=True, copied=True, tracking=0)
    bold = fields.Boolean(string='bold', store=True, copied=True, tracking=0)
    cc1 = fields.Char(string='cc1', store=True, copied=True, tracking=0)
    cc2 = fields.Char(string='cc2', store=True, copied=True, tracking=0)
    cc3 = fields.Char(string='cc3', store=True, copied=True, tracking=0)
    cc4 = fields.Char(string='cc4', store=True, copied=True, tracking=0)
    cc5 = fields.Char(string='cc5', store=True, copied=True, tracking=0)
    credit = fields.Float(string='Crédito', store=True, copied=True, tracking=0)
    cuenta = fields.Char(string='Cuenta', store=True, copied=True, tracking=0)
    debit = fields.Float(string='Débito', store=True, copied=True, tracking=0)
    nivel = fields.Integer(string='Nivel', store=True, copied=True, tracking=0)
    resume = fields.Boolean(string='Resumen', store=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)

class FpaPygCcWizard(models.Model):
    _name = 'fpa.pyg.cc.wizard'
    _description = 'Asistente de pérdidas y ganancias por centro de costo FPA'

    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copied=True, tracking=0)
    analytic_filter = fields.Boolean(string='Filtro adicional de cuenta analítica', store=True, copied=True, tracking=0)
    cierre = fields.Boolean(string='Apertura/Cierre', store=True, copied=True, tracking=0)
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha final', store=True, required=True, copied=True, tracking=0)
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copied=True, tracking=0)
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copied=True, tracking=0)

class FpaPygCLine(models.Model):
    _name = 'fpa.pyg.c.line'
    _description = 'Líneas de pérdidas y ganancias comparativas FPA'

    amount_comparative = fields.Float(string='Saldo Comparativo', store=True, copied=True, tracking=0)
    amount_final = fields.Float(string='Saldo Final', store=True, copied=True, tracking=0)
    amount_inicial = fields.Float(string='Saldo Inicial', store=True, copied=True, tracking=0)
    bold = fields.Boolean(string='bold', store=True, copied=True, tracking=0)
    credit = fields.Float(string='Crédito', store=True, copied=True, tracking=0)
    cuenta = fields.Char(string='Cuenta', store=True, copied=True, tracking=0)
    debit = fields.Float(string='Débito', store=True, copied=True, tracking=0)
    nivel = fields.Integer(string='Nivel', store=True, copied=True, tracking=0)
    porc_variation = fields.Float(string='% Variación', store=True, copied=True, tracking=0)
    resume = fields.Boolean(string='Resumen', store=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)
    variation = fields.Float(string='Variación', store=True, copied=True, tracking=0)

class FpaPygCWizard(models.Model):
    _name = 'fpa.pyg.c.wizard'
    _description = 'Asistente de pérdidas y ganancias comparativas FPA'

    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copied=True, tracking=0)
    analytic_filter = fields.Boolean(string='Filtro adicional de cuenta analítica', store=True, copied=True, tracking=0)
    cierre = fields.Boolean(string='Cierre', store=True, copied=True, tracking=0)
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha final', store=True, required=True, copied=True, tracking=0)
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copied=True, tracking=0)
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copied=True, tracking=0)

class FpaPygLine(models.Model):
    _name = 'fpa.pyg.line'
    _description = 'Líneas de pérdidas y ganancias FPA'

    amount_1 = fields.Float(string='Saldo Comparativo', store=True, copied=True, tracking=0)
    amount_final = fields.Float(string='Saldo Final', store=True, copied=True, tracking=0)
    amount_inicial = fields.Float(string='Saldo Inicial', store=True, copied=True, tracking=0)
    bold = fields.Boolean(string='bold', store=True, copied=True, tracking=0)
    credit = fields.Float(string='Crédito', store=True, copied=True, tracking=0)
    cuenta = fields.Char(string='Cuenta', store=True, copied=True, tracking=0)
    debit = fields.Float(string='Débito', store=True, copied=True, tracking=0)
    nivel = fields.Integer(string='Nivel', store=True, copied=True, tracking=0)
    resume = fields.Boolean(string='Resumen', store=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)

class FpaPygWizard(models.Model):
    _name = 'fpa.pyg.wizard'
    _description = 'Asistente de pérdidas y ganancias FPA'

    account_filter = fields.Boolean(string='Filtro adicional de cuentas', store=True, copied=True, tracking=0)
    analytic_filter = fields.Boolean(string='Filtro adicional de cuenta analítica', store=True, copied=True, tracking=0)
    cierre = fields.Boolean(string='Cierre', store=True, copied=True, tracking=0)
    date_from = fields.Date(string='Fecha Inicial', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha final', store=True, required=True, copied=True, tracking=0)
    journal_filter = fields.Boolean(string='Filtro adicional de diarios', store=True, copied=True, tracking=0)
    partner_filter = fields.Boolean(string='Filtro adicional de terceros', store=True, copied=True, tracking=0)

class GamificationBadge(models.Model):
    _inherit = 'gamification.badge'
    # No se agrega _name ni _description porque hereda de otra clase

    rule_manumber = fields.Integer(string='Limitar número', store=True, copied=True, tracking=0)

class GeneralLedgerReportWizard(models.Model):
    _name = 'general.ledger.report.wizard'
    _description = 'Asistente de reporte de libro mayor general'

    centralize = fields.Boolean(string='Activar centralización', store=True, copied=True, tracking=0)
    date_from = fields.Date(string='Fecha de inicio', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha final', store=True, required=True, copied=True, tracking=0)
    domain = fields.Char(string='Journal Items Domain', store=True, copied=True, tracking=0)
    foreign_currency = fields.Boolean(string='Mostrar Moneda Extranjera', store=True, copied=True, tracking=0)
    fy_start_date = fields.Date(string='Fecha Inicio', readonly=True, tracking=0)
    hide_account_at_0 = fields.Boolean(string='Ocultar saldos finales con valor a 0', store=True, copied=True, tracking=0)
    not_only_one_unaffected_earnings_account = fields.Boolean(string='No solo una cuenta de ganancias no afectadas', store=True, readonly=True, copied=True, tracking=0)
    payable_accounts_only = fields.Boolean(string='Sólo cuentas a pagar', store=True, copied=True, tracking=0)
    receivable_accounts_only = fields.Boolean(string='Sólo cuentas a cobrar', store=True, copied=True, tracking=0)
    show_analytic_tags = fields.Boolean(string='Mostrar etiquetas analíticas', store=True, copied=True, tracking=0)
    show_cost_center = fields.Boolean(string='Mostrar centro de costo', store=True, copied=True, tracking=0)

class GoogleCalendarSync(models.Model):
    _name = 'google.calendar.sync'
    _description = 'Sincronización de calendario de Google'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0)
    google_id = fields.Char(string='ID de Calendario de Google', store=True, tracking=0)
    need_sync = fields.Boolean(string='Necesita sincronización', store=True, tracking=0)

class GoogleDriveConfig(models.Model):
    _name = 'google.drive.config'
    _description = 'Configuración de Google Drive'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0)
    google_drive_client_id = fields.Char(string='Cliente de Google', readonly=True, tracking=0)
    google_drive_resource_id = fields.Char(string='Id del recurso', readonly=True, tracking=0)
    google_drive_template_url = fields.Char(string='URL de la plantilla', store=True, required=True, copied=True, tracking=0)
    model = fields.Char(string='Modelo relacionado', readonly=True, tracking=0)
    name_template = fields.Char(string='Patrón de nombres de Google Drive', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre de la plantilla', store=True, required=True, copied=True, tracking=0)

class GoogleGmailMixin(models.Model):
    _name = 'google.gmail.mixin'
    _description = 'Mezcla de Google Gmail'

    google_gmail_access_token_expiration = fields.Integer(string='Access Token Expiration Timestamp', store=True, tracking=0)
    google_gmail_access_token = fields.Char(string='Access Token', store=True, tracking=0)
    google_gmail_authorization_code = fields.Char(string='Authorization Code', store=True, tracking=0)
    google_gmail_refresh_token = fields.Char(string='Refresh Token', store=True, tracking=0)
    google_gmail_uri = fields.Char(string='URI', readonly=True, tracking=0)
    use_google_gmail_service = fields.Boolean(string='Gmail Authentication', store=True, copied=True, tracking=0)

class GroupUpdateHistory(models.Model):
    _name = 'group.update.history'
    _description = 'Historial de actualización de grupos'

    date = fields.Date(string='Fecha', store=True, required=True, copied=True, tracking=0)

class HelpdeskCategory(models.Model):
    _name = 'helpdesk.category'
    _description = 'Categorías de helpdesk'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)

class HelpdeskPriority(models.Model):
    _name = 'helpdesk.priority'
    _description = 'Prioridades de helpdesk'

    color = fields.Char(string='Color', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)

class HelpdeskRelease(models.Model):
    _name = 'helpdesk.release'
    _description = 'Versiones de helpdesk'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class HelpdeskStages(models.Model):
    _name = 'helpdesk.stages'
    _description = 'Etapas de helpdesk'

    is_cancel_button_visible = fields.Boolean(string='¿Es visible el botón Cancelar?', store=True, copied=True, tracking=0)
    is_closed_stage = fields.Boolean(string='Is Closed Stage?', store=True, copied=True, tracking=0)
    is_done_button_visible = fields.Boolean(string='¿Es visible el botón resuelto?', store=True, copied=True, tracking=0)
    is_pause_stage = fields.Boolean(string='Is Pause Stage?', store=True, copied=True, tracking=0)
    is_reopen_stage = fields.Boolean(string='Is Reopen Stage?', store=True, copied=True, tracking=0)
    is_validated_stage = fields.Boolean(string='Is Validated Stage?', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)

class HelpdeskSubcategory(models.Model):
    _name = 'helpdesk.subcategory'
    _description = 'Subcategorías de helpdesk'

    name = fields.Char(string='Nombre de la subcategoría', store=True, required=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)

class HelpdeskSubType(models.Model):
    _name = 'helpdesk.sub.type'
    _description = 'Subtipos de helpdesk'

    is_technical = fields.Boolean(string='Equipo Técnico', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)

class HelpdeskTags(models.Model):
    _name = 'helpdesk.tags'
    _description = 'Etiquetas de helpdesk'

    color = fields.Integer(string='Índice de color', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)

class HelpdeskTeam(models.Model):
    _name = 'helpdesk.team'
    _description = 'Equipos de helpdesk'

    alias_bounced_content = fields.Html(string='Mensaje rebotado personalizado', copied=True, tracking=0)
    alias_defaults = fields.Text(string='Valores predeterminados', required=True, copied=True, tracking=0)
    alias_domain = fields.Char(string='Dominio de alias', readonly=True, tracking=0)
    alias_force_thread_id = fields.Integer(string='Registro de identificación de hilo', copied=True, tracking=0)
    alias_name = fields.Char(string='Sobre nombre', tracking=0)
    alias_parent_thread_id = fields.Integer(string='ID de hilo de registro principal', copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    sla_count = fields.Integer(string='Conteo de SLA', readonly=True, tracking=0)

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Tickets de helpdesk'

    access_token = fields.Char(string='Token de seguridad', store=True, tracking=0)
    access_url = fields.Char(string='URL de acceso al portal', readonly=True, tracking=0)
    access_warning = fields.Text(string='Advertencia de acceso', readonly=True, tracking=0)
    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0)
    activity_date_deadline = fields.Date(string='Fecha límite de la próxima actividad', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Siguiente resumen de actividad', tracking=0)
    activity_type_icon = fields.Char(string='Icono de tipo de actividad', readonly=True, tracking=0)
    bussines_name = fields.Char(string='Bussines Name', store=True, copied=True, tracking=100)
    cancel_button_boolean = fields.Boolean(string='Botón de cancelación', readonly=True, tracking=0)
    cancel_date = fields.Datetime(string='Fecha cancelada', store=True, copied=True, tracking=100)
    cancel_reason = fields.Char(string='Cancelar razón', store=True, copied=True, tracking=100)
    cancel_stage_boolean = fields.Boolean(string='Cancelar etapa', store=True, readonly=True, tracking=0)
    category_bool = fields.Boolean(string='Configuración de categoría', store=True, readonly=True, tracking=0)
    client_validate = fields.Boolean(string='Validado por el cliente', store=True, copied=True, tracking=0)
    close_date = fields.Datetime(string='Fecha de cierre', store=True, copied=True, tracking=100)
    closed_stage_boolean = fields.Boolean(string='Etapa cerrada', store=True, readonly=True, tracking=0)
    color = fields.Integer(string='Índice de color', store=True, copied=True, tracking=0)
    comment = fields.Text(string='Comentario', store=True, copied=True, tracking=100)
    cumple_lo_requerido = fields.Boolean(string='Cumple lo requerido', store=True, copied=True, tracking=0)
    customer_comment = fields.Text(string='Comentario del cliente', store=True, copied=True, tracking=100)
    description = fields.Html(string='Descripción', store=True, copied=True, tracking=100)
    done_button_boolean = fields.Boolean(string='Botón hecho', readonly=True, tracking=0)
    done_stage_boolean = fields.Boolean(string='Etapa de hecho', store=True, readonly=True, tracking=0)
    duration_dev = fields.Float(string='Tiempo previsto', store=True, copied=True, tracking=0)
    duration = fields.Float(string='Duración real', readonly=True, tracking=0)
    email_subject = fields.Char(string='Tema', store=True, copied=True, tracking=0)
    email = fields.Char(string='Correo electrónico', store=True, copied=True, tracking=100)
    end_time = fields.Datetime(string='Hora de finalización', store=True, tracking=0)
    form_url = fields.Char(string='Forma URL', readonly=True, tracking=0)
    invoice_count = fields.Integer(string='Factura', readonly=True, tracking=0)
    invoice_hours = fields.Float(string='Tiempo facturable', store=True, copied=True, tracking=0)
    is_stage_new = fields.Boolean(string='New Stage', readonly=True, tracking=0)
    last_update = fields.Datetime(string='Last Update', store=True, readonly=True, tracking=0)
    lead_count = fields.Integer(string='Guiar', readonly=True, tracking=0)
    message_attachment_count = fields.Integer(string='Recuento de adjuntos', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Número de errores', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Error de entrega de mensajes', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='Error de entrega de SMS', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Es seguidor', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Acción necesaria', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Contador de mensajes no leídos', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Mensajes no leídos', readonly=True, tracking=0)
    mobile_no = fields.Char(string='Teléfono', store=True, copied=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='Mi fecha límite de actividad', readonly=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=100)
    open_boolean = fields.Boolean(string='Ticket abierto', store=True, readonly=True, tracking=0)
    opportunity_count = fields.Integer(string='Oportunidad', readonly=True, tracking=0)
    person_name = fields.Char(string='Nombre de la persona', store=True, copied=True, tracking=100)
    portal_ticket_url_wp = fields.Char(string='URL de ticket portal WP', readonly=True, tracking=0)
    purchase_order_count = fields.Integer(string='Pedido de compra', readonly=True, tracking=0)
    rating_bool = fields.Boolean(string='Configuración de calificación', store=True, readonly=True, tracking=0)
    real_time = fields.Float(string='Tiempo Real', store=True, copied=True, tracking=0)
    reopen_stage_boolean = fields.Boolean(string='Etapa reabrida', store=True, readonly=True, tracking=0)
    replied_date = fields.Datetime(string='Fecha de respuesta', store=True, copied=True, tracking=100)
    report_token = fields.Char(string='Token de acceso', store=True, copied=True, tracking=0)
    resolution_detail = fields.Html(string='Realización Interna', store=True, copied=True, tracking=100)
    sale_order_count = fields.Integer(string='Ordenar', readonly=True, tracking=0)
    sh_days_to_late = fields.Float(string='SLA Duración tardía', store=True, readonly=True, tracking=0)
    sh_days_to_reach = fields.Float(string='SLA alcanzó la duración', store=True, readonly=True, tracking=0)
    sh_display_multi_user = fields.Boolean(string='SH Display Multi User', readonly=True, tracking=0)
    sh_display_product = fields.Boolean(string='Producto de pantalla SH', readonly=True, tracking=0)
    sh_due_date = fields.Datetime(string='Fecha Entrega', store=True, copied=True, tracking=0)
    sh_merge_ticket_count = fields.Integer(string='SH MERGE RECTURA', readonly=True, tracking=0)
    sh_planned_date = fields.Datetime(string='Fecha Inicio Solicitud', store=True, copied=True, tracking=0)
    sh_sla_deadline = fields.Datetime(string='Fecha límite de SLA', store=True, readonly=True, tracking=0)
    sh_status_boolean = fields.Boolean(string='Sh status boolean', readonly=True, tracking=0)
    sh_ticket_report_url = fields.Char(string='URL de informe de tickets de SH', readonly=True, tracking=0)
    solucion_inmediata = fields.Boolean(string='Solución inmediata', store=True, copied=True, tracking=0)
    solution_done = fields.Html(string='Solución propuesta cliente', store=True, copied=True, tracking=100)
    start_time = fields.Datetime(string='Hora de inicio', store=True, tracking=0)
    sub_category_bool = fields.Boolean(string='Configuración de subcategorías', store=True, readonly=True, tracking=0)
    task_count = fields.Integer(string='Tareas', readonly=True, tracking=0)
    ticket_allocated = fields.Boolean(string='Asignado', store=True, copied=True, tracking=0)
    ticket_from_portal = fields.Boolean(string='Ticket desde portal', store=True, copied=True, tracking=0)
    ticket_from_website = fields.Boolean(string='Ticket del sitio web', store=True, copied=True, tracking=0)
    ticket_running = fields.Boolean(string='Ticket', store=True, copied=True, tracking=0)
    total_time = fields.Char(string='Tiempo Total', store=True, tracking=0)
    video_link = fields.Char(string='Video Link', store=True, copied=True, tracking=100)

class HelpdeskTicketType(models.Model):
    _name = 'helpdesk.ticket.type'
    _description = 'Tipos de tickets de helpdesk'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    sla_count = fields.Integer(string='Conteo de SLA', readonly=True, tracking=0)

class HrApplicant(models.Model):
    _inherit = 'hr.applicant'
    # No se agrega _name ni _description porque hereda de otra clase

    fecha_proceso = fields.Date(string='Fecha Proceso', store=True, copied=True, tracking=1)

class HrBranch(models.Model):
    _name = 'hr.branch'
    _description = 'Sucursales de RRHH'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0)
    code = fields.Char(string='Código', store=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)

class HrCapacitaciones(models.Model):
    _name = 'hr.capacitaciones'
    _description = 'Capacitaciones de RRHH'

    adj_capacitacion = fields.Text(string='Soporte Físico', store=True, copied=True, tracking=0)
    date_start = fields.Datetime(string='Fecha de inicio', store=True, required=True, copied=True, tracking=0)
    date_stop = fields.Datetime(string='Fecha de Finalización', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    size = fields.Integer(string='Duración', store=True, required=True, copied=True, tracking=0)

class HrConcept(models.Model):
    _name = 'hr.concept'
    _description = 'Conceptos de RRHH'

    code = fields.Char(string='Código', store=True, required=True, copied=True, tracking=0)
    disability_for_embargo = fields.Boolean(string='Incapacidad para embargos', store=True, copied=True, tracking=0)
    documentation = fields.Char(string='Información', store=True, copied=True, tracking=0)
    is_retention = fields.Boolean(string='Es Retención', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)

class HrConceptLog(models.Model):
    _name = 'hr.concept.log'
    _description = 'Registro de conceptos de RRHH'

    name = fields.Char(string='Descripción', store=True, copied=True, tracking=0)
    value = fields.Float(string='Valor', store=True, copied=True, tracking=0)

class HrContractAnalyticDistribution(models.Model):
    _name = 'hr.contract.analytic.distribution'
    _description = 'Distribución analítica de contratos de RRHH'

    rate = fields.Float(string='Distribución (%)', store=True, copied=True, tracking=0)

class HrContractExtension(models.Model):
    _name = 'hr.contract.extension'
    _description = 'Extensiones de contrato de RRHH'

    date_from = fields.Date(string='Fecha de Inicio Prórroga', store=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha de Fin Prórroga', store=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Número de Prórroga', store=True, copied=True, tracking=0)

class HrContractGroup(models.Model):
    _name = 'hr.contract.group'
    _description = 'Grupos de contrato de RRHH'

    name = fields.Char(string='Nombre de Grupo', store=True, copied=True, tracking=0)
    transport_second_fortnight = fields.Boolean(string='Auxilio Transporte Segunda Quincena', store=True, copied=True, tracking=0)

class HrContractHourLimit(models.Model):
    _name = 'hr.contract.hour.limit'
    _description = 'Límites de horas de contrato de RRHH'

    extra_hours_max = fields.Float(string='Máximo de horas extra', store=True, copied=True, tracking=0)
    limit = fields.Float(string='Tope de horas', store=True, copied=True, tracking=0)

class HrContractJobDo(models.Model):
    _name = 'hr.contract.job.do'
    _description = 'Trabajos de contrato de RRHH'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class HrContractRisk(models.Model):
    _name = 'hr.contract.risk'
    _description = 'Riesgos de contrato de RRHH'

    name = fields.Char(string='Riesgo', store=True, copied=True, tracking=0)
    risk_percentage = fields.Float(string='Porcentaje de Riesgo', store=True, copied=True, tracking=0)
    sub_activity = fields.Char(string='Sub actividad económica', store=True, copied=True, tracking=0)

class HrContractSubzone(models.Model):
    _name = 'hr.contract.subzone'
    _description = 'Subzonas de contrato de RRHH'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class HrContractWithholdingLog(models.Model):
    _name = 'hr.contract.withholding.log'
    _description = 'Registro de retenciones de contrato de RRHH'

    name = fields.Char(string='Descripción', store=True, copied=True, tracking=0)
    value = fields.Char(string='Detalle', store=True, copied=True, tracking=0)

class HrContractZone(models.Model):
    _name = 'hr.contract.zone'
    _description = 'Zonas de contrato de RRHH'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class HrContributionForm(models.Model):
    _name = 'hr.contribution.form'
    _description = 'Formularios de aportes de RRHH'

    branch_code = fields.Char(string='Código de sucursal', store=True, copied=True, tracking=0)
    error_log = fields.Text(string='Errores', store=True, readonly=True, copied=True, tracking=0)
    file_name = fields.Char(string='Nombre del Archivo', store=True, readonly=True, copied=True, tracking=0)
    file_pila = fields.Text(string='Archivo plano', store=True, readonly=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, readonly=True, copied=True, tracking=0)

class HrCourtEmbargoes(models.Model):
    _name = 'hr.court.embargoes'
    _description = 'Embargos judiciales de RRHH'

    name = fields.Char(string='Número de cuenta', store=True, copied=True, tracking=0)

class HrCourtEmbargoesCode(models.Model):
    _name = 'hr.court.embargoes.code'
    _description = 'Códigos de embargos judiciales de RRHH'

    name = fields.Char(string='Código del juzgado', store=True, copied=True, tracking=0)

class HrCourtEmbargoesDestination(models.Model):
    _name = 'hr.court.embargoes.destination'
    _description = 'Destinos de embargos judiciales de RRHH'

    name = fields.Char(string='Código del juzgado', store=True, copied=True, tracking=0)

class HrDisability(models.Model):
    _name = 'hr.disability'
    _description = 'Discapacidades de RRHH'

    name = fields.Char(string='Discapacidades', store=True, copied=True, tracking=0)

class HrDotacion(models.Model):
    _name = 'hr.dotacion'
    _description = 'Dotaciones de RRHH'

    document = fields.Char(string='Cantidad', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)

class HrEdInstitution(models.Model):
    _name = 'hr.ed.institution'
    _description = 'Instituciones educativas de RRHH'

    name = fields.Char(string='Institución educativa', store=True, copied=True, tracking=0)

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    display_name = fields.Char(
        string='Display Name',
        compute='_compute_display_name',
        store=False,
        copied=False,
        tracking=0
    )
    address_home = fields.Char(string='Direccion', store=True, copied=True, tracking=0, )
    adj_adp = fields.Text(string='A. Datos personales', store=True, copied=True, tracking=0, )
    adj_ced = fields.Text(string='Cedula', store=True, copied=True, tracking=0, )
    adj_db = fields.Text(string='D. Bachiller', store=True, copied=True, tracking=0, )
    adj_ee = fields.Text(string='E. Especifico', store=True, copied=True, tracking=0, )
    adj_fh = fields.Text(string='F. Huella', store=True, copied=True, tracking=0, )
    adj_hv = fields.Text(string='H.V.', store=True, copied=True, tracking=0, )
    adj_lm = fields.Text(string='L. Militar', store=True, copied=True, tracking=0, )
    adj_obser = fields.Text(string='Observaciones', store=True, copied=True, tracking=0, )
    adj_pj = fields.Text(string='P. Judicial', store=True, copied=True, tracking=0, )
    adj_ps = fields.Text(string='P. Psicotecnicas', store=True, copied=True, tracking=0, )
    adj_ri = fields.Text(string='R. Induccion', store=True, copied=True, tracking=0, )
    age = fields.Integer(string='Edad', readonly=True, tracking=0, )
    aplica_transporte = fields.Boolean(string='Aplica para tarifario de transporte adicional?', store=True, copied=True,
                                       tracking=0, )
    auditor = fields.Boolean(string='Auditor', store=True, copied=True, tracking=0, )
    blood_pressure = fields.Char(string='Presion Arterial', store=True, copied=True, tracking=0, )
    cellphone = fields.Char(string='Celular', store=True, copied=True, tracking=0, )
    codigo = fields.Char(string='Codigo Interno', store=True, required=True, copied=True, tracking=0, )
    cohabit_children_amount = fields.Integer(string='Hijos cohabitantes', readonly=True, tracking=0, )
    commodity = fields.Boolean(string='Commodity', store=True, copied=True, tracking=0, )
    cruso_vigilancia = fields.Char(string='Curso Vigilancia Validador', store=True, readonly=True, tracking=0, )
    cultural_activities = fields.Char(string='Actividades culturales', store=True, copied=True, tracking=0, )
    date_end = fields.Date(string='Fecha Final', store=True, tracking=0, )
    date_vis_end = fields.Datetime(string='Fecha de finalizacion', store=True, copied=True, tracking=0, )
    date_vis_ini = fields.Datetime(string='Fecha de inicio', store=True, copied=True, tracking=0, )
    depending_relatives = fields.Integer(string='Personas dependientes', readonly=True, tracking=0, )
    descripcion_recomendaciones = fields.Text(string='Descripcion de las restricciones o recomendaciones', store=True,
                                              copied=True, tracking=0, )
    email_personal = fields.Char(string='Email Personal', store=True, readonly=True, tracking=0, )
    email = fields.Char(string='Email Corporativo', store=True, readonly=True, tracking=0, )
    employee_charge = fields.Char(string='Nombre del cargo del empleado', readonly=True, tracking=0, )
    estado_contrato = fields.Char(string='Estado del Contrato', store=True, readonly=True, tracking=0, )
    estado_curso_svsp = fields.Char(string='Estado Curso Svsp', store=True, tracking=0, )
    estatura = fields.Integer(string='Estatura (en centímetros)', store=True, copied=True, tracking=0, )
    fecha_expedicion_documento = fields.Date(string='Fecha de expedición del documento de identidad', store=True,
                                             copied=True, tracking=0, )
    fecha_pcl_arl_Jnc = fields.Date(string='Fecha Pcl Arl Jnc (Junta Nacional Calificación)', store=True, copied=True,
                                    tracking=0, )
    fecha_pcl_arl_Jrc = fields.Date(string='Fecha Pcl Arl Jrc (Junta Regional Calificación)', store=True, copied=True,
                                    tracking=0, )
    fecha_pcl_arl = fields.Date(string='Fecha PCL ARL', store=True, copied=True, tracking=0, )
    food_habits = fields.Char(string='Alimentación', store=True, copied=True, tracking=0, )
    home_contributor_amount = fields.Integer(string='Personas aportantes', readonly=True, tracking=0, )
    horas = fields.Float(string='Horas de Auditoria', readonly=True, tracking=0, )
    last_health_check = fields.Datetime(string='Ultimo examen ocupacional', store=True, copied=True, tracking=0, )
    leasure_activities = fields.Char(string='Actividades de tiempo libre', store=True, copied=True, tracking=0, )
    neighborhood = fields.Char(string='Barrio', store=True, copied=True, tracking=0, )
    no_ordenar = fields.Char(string='No Ordenar', copied=True, tracking=0, )
    permiso_especial = fields.Text(string='Permiso especial', store=True, copied=True, tracking=0, )
    peso = fields.Integer(string='Peso (en kilogramos)', store=True, copied=True, tracking=0, )
    porcentaje_pcl_arl = fields.Text(string='% Pcl Arl', store=True, copied=True, tracking=0, )
    practice_sports_period = fields.Char(string='Periodicidad de practica', store=True, copied=True, tracking=0, )
    responsable_caja = fields.Boolean(string='Responsable de Caja', store=True, copied=True, tracking=0, )
    street = fields.Char(string='Street', tracking=0, )
    street2 = fields.Char(string='Street2', tracking=0, )
    temp_date_ini = fields.Datetime(string='Fecha de Ingreso', store=True, copied=True, tracking=0, )
    temp_date_start = fields.Datetime(string='Fecha Primer Ingreso', store=True, copied=True, tracking=0, )
    temp_salario = fields.Float(string='Asignacion salarial', store=True, copied=True, tracking=0, )
    tipo_identificacion_id = fields.Char(string='Tipo de Identificación', store=True, readonly=True, tracking=0, )
    transport_mean_other = fields.Char(string='¿Cual?', store=True, copied=True, tracking=0, )
    type_allergies = fields.Char(string='¿Que alergias?', store=True, copied=True, tracking=0, )
    vaccination = fields.Char(string='Vacunas', store=True, copied=True, tracking=0, )
    vigencia_recomendaciones = fields.Text(string='Vigencia de las recomendaciones o restricciones', store=True,
                                           copied=True, tracking=0, )
    visita = fields.Text(string='V. Domiciliaria', store=True, copied=True, tracking=0, )
    work_experience = fields.Float(string='Años de experienca ocupacional', store=True, copied=True, tracking=0, )
    work_health_diagnosis = fields.Char(string='Diagnósticos de Enfermedad Laboral', store=True, copied=True, tracking=0, )

    @api.depends('name', 'identification_id')
    def _compute_display_name(self):
        for employee in self:
            # Manejar casos donde los campos puedan estar vacíos
            id_part = f"[{employee.identification_id or ''}] " if employee.identification_id else ''
            name_part = employee.name or ''
            employee.display_name = f"{id_part} {name_part}".strip()

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        if not args:
            args = []
        if name:
            args += ['|', ('identification_id', operator, name), ('name', operator, name)]
        return self.search(args, limit=limit).name_get()

class HrEmployeeAccreditation(models.Model):
    _name = 'hr.employee.accreditation'
    _description = 'Acreditaciones del empleado'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    auxiliar_file_url = fields.Char(string='Url Soporte', store=True, readonly=True, tracking=0, )
    course_code = fields.Char(string='Código curso (Antiguo)', store=True, copied=True, tracking=0,
                              comodel_name='ir.attachment', )
    couse_number = fields.Char(string='Nro.', store=True, copied=True, tracking=0, comodel_name='ir.attachment', )
    days_to_expiration = fields.Integer(string='Días para vencer', store=True, copied=True, tracking=0, )
    end_date = fields.Datetime(string='Fecha fin', store=True, required=True, copied=True, tracking=0, )
    estado = fields.Char(string='Estado', store=True, readonly=True, tracking=0, )
    fecha_de_radicacion = fields.Date(string='Fecha De Radicación', store=True, copied=True, tracking=0, )
    init_date = fields.Datetime(string='Fecha inicio', store=True, required=True, copied=True, tracking=0, )
    nit_school = fields.Char(string='NIT Escuela', store=True, copied=True, tracking=0, comodel_name='ir.attachment', )
    numero_de_radicado = fields.Char(string='Número de Radicado', store=True, copied=True, tracking=0, )


class HrEmployeeAccreditationLine(models.Model):
    _name = 'hr.employee.accreditation.line'
    _description = 'Líneas de acreditaciones del empleado'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0, )


class HrEmployeeCredentials(models.Model):
    _name = 'hr.employee.credentials'
    _description = 'Credenciales del empleado'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    auxiliar_file_url = fields.Char(string='URL del Adjunto', store=True, readonly=True, tracking=0, )
    days_to_expiration = fields.Integer(string='Días para vencer', store=True, copied=True, tracking=0, )
    end_date = fields.Datetime(string='Fecha fin', store=True, required=True, copied=True, tracking=0, )
    estado = fields.Char(string='Estado', store=True, readonly=True, tracking=0, )
    init_date = fields.Datetime(string='Fecha inicio', store=True, required=True, copied=True, tracking=0, )


class HrEmployeeCredentialsLine(models.Model):
    _name = 'hr.employee.credentials.line'
    _description = 'Líneas de credenciales de empleados'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)


class HrEmployeeDisciplinaryAction(models.Model):
    _name = 'hr.employee.disciplinary.action'
    _description = 'Acciones disciplinarias de empleados'

    date = fields.Datetime(string='Fecha de ocurrencia', store=True, required=True, copied=True, tracking=0)
    description = fields.Text(string='Decisión', store=True, copied=True, tracking=0)


class HrEmployeeDisciplinaryActionLine(models.Model):
    _name = 'hr.employee.disciplinary.action.line'
    _description = 'Líneas de acciones disciplinarias de empleados'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)


class HrEmployeeEpayrollSubtype(models.Model):
    _name = 'hr.employee.epayroll.subtype'
    _description = 'Subtipos de nómina electrónica de empleados'

    code = fields.Char(string='Código', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)


class HrEmployeeEpayrollType(models.Model):
    _name = 'hr.employee.epayroll.type'
    _description = 'Tipos de nómina electrónica de empleados'

    code = fields.Char(string='Código', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)


class HrEmployeeRh(models.Model):
    _name = 'hr.employee.rh'
    _description = 'Recursos humanos de empleados'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)


class HrEpsCode(models.Model):
    _name = 'hr.eps.code'
    _description = 'Códigos de EPS'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)


class HrEquipment(models.Model):
    _name = 'hr.equipment'
    _description = 'Equipos de RRHH'

    amount_info = fields.Char(string='Cantidad/Información', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)


class HrExpenseExpense(models.Model):
    _name = 'hr.expense.expense'
    _description = 'Gastos de RRHH'

    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    amount_total2 = fields.Float(string='Total con Impuestos', store=True, readonly=True, tracking=0)
    amount = fields.Float(string='Total', readonly=True, tracking=0)
    background_minor_borelated = fields.Float(string='Fondo Caja Menor', readonly=True, tracking=100)
    background_minor_box = fields.Float(string='Fondo Caja Menor', store=True, copied=True, tracking=100)
    balance_minor_box = fields.Float(string='Saldo Caja Menor', store=True, readonly=True, tracking=100)
    date_move = fields.Date(string='Fecha de Contabilización', store=True, copied=True, tracking=100)
    date_valid = fields.Date(string='Fecha de Validación', store=True, copied=True, tracking=100)
    description = fields.Char(string='Descripción', store=True, copied=True, tracking=100)
    is_paid = fields.Boolean(string='¿Está pagado?', readonly=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    partial_reconciled = fields.Boolean(string='Partial Reconcile', readonly=True, tracking=0)


class HrExpenseLine(models.Model):
    _name = 'hr.expense.line'
    _description = 'Líneas de gastos de RRHH'

    amount = fields.Float(string='Total', store=True, readonly=True, tracking=0)
    base_amount = fields.Float(string='Total Base', store=True, readonly=True, tracking=0)
    date = fields.Date(string='Fecha', store=True, copied=True, tracking=0)
    impuestos_asumidos = fields.Float(string='Importe Total', store=True, readonly=True, tracking=0)
    journal_consecutive = fields.Char(string='Consecutivo', store=True, copied=True, tracking=0)
    manual_taxes = fields.Boolean(string='Impuestos manuales', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nota de Gasto', store=True, copied=True, tracking=0)
    no_tax = fields.Float(string='Rubro Adicional', store=True, copied=True, tracking=0)
    note = fields.Text(string='Nota', store=True, copied=True, tracking=0)
    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)
    quantity = fields.Float(string='Cantidad', store=True, copied=True, tracking=0)
    recoup = fields.Boolean(string='Recobro', store=True, copied=True, tracking=0)
    recovery = fields.Boolean(string='Recobro', store=True, copied=True, tracking=0)
    ref1 = fields.Char(string='Referencia 1', store=True, copied=True, tracking=0)
    ref2 = fields.Char(string='Referencia 2', store=True, copied=True, tracking=0)
    taamount_assumed = fields.Float(string='Total Impuestos Asumidos', store=True, readonly=True, tracking=0)
    taamount = fields.Float(string='Total Impuestos', store=True, readonly=True, tracking=0)
    vat_amount = fields.Float(string='IVA', readonly=True, tracking=0)


class HrExpenseLineRecoup(models.Model):
    _name = 'hr.expense.line.recoup'
    _description = 'Recobros de líneas de gastos de RRHH'

    description = fields.Text(string='Descripción', store=True, copied=True, tracking=0)
    taadd = fields.Boolean(string='Añadir impuestos', store=True, copied=True, tracking=0)


class HrExpenseTax(models.Model):
    _name = 'hr.expense.tax'
    _description = 'Impuestos de gastos de RRHH'

    amount_base = fields.Float(string='Código base', store=True, copied=True, tracking=0)
    amount = fields.Float(string='Total', store=True, copied=True, tracking=0)
    base = fields.Float(string='Base', store=True, copied=True, tracking=0)
    manual = fields.Boolean(string='Manual', store=True, copied=True, tracking=0)
    name = fields.Char(string='Descripción', store=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)
    taamount = fields.Float(string='Impuesto código base', store=True, copied=True, tracking=0)
    taken = fields.Boolean(string='Asumido', store=True, copied=True, tracking=0)


class HrFamiliar(models.Model):
    _name = 'hr.familiar'
    _description = 'Familiares de empleados'

    date = fields.Date(string='Fecha de Nacimiento', store=True, required=True, copied=True, tracking=0)
    depends = fields.Boolean(string='¿Dependiente?', store=True, copied=True, tracking=0)
    document = fields.Char(string='Documento', store=True, copied=True, tracking=0)
    home_contributor = fields.Boolean(string='Aporta ingresos al Hogar', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    parent = fields.Char(string='Parentesco', store=True, copied=True, tracking=0)
    phone = fields.Char(string='Teléfono', store=True, copied=True, tracking=0)
    type_id = fields.Char(string='Tipo de Documento', store=True, copied=True, tracking=0)


class HrFiscalSubtype(models.Model):
    _name = 'hr.fiscal.subtype'
    _description = 'Subtipos fiscales de RRHH'

    code = fields.Char(string='Código', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    note = fields.Text(string='Notas', store=True, copied=True, tracking=0)


class HrFiscalType(models.Model):
    _name = 'hr.fiscal.type'
    _description = 'Tipos fiscales de RRHH'

    code = fields.Char(string='Código', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    note = fields.Text(string='Notas', store=True, copied=True, tracking=0)


class HrHoliday(models.Model):
    _name = 'hr.holiday'
    _description = 'Vacaciones de RRHH'

    date = fields.Date(string='Fecha', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)


class HrHolidayBook(models.Model):
    _name = 'hr.holiday.book'
    _description = 'Libro de vacaciones de RRHH'

    auxiliar = fields.Float(string='Auxiliar', store=True, copied=True, tracking=0)
    bold = fields.Boolean(string='Negrita', store=True, copied=True, tracking=0)
    caused_days = fields.Float(string='Días causados', store=True, copied=True, tracking=0)
    date_end_holidays = fields.Date(string='Fecha final vacaciones', store=True, copied=True, tracking=0)
    date_end = fields.Date(string='Fecha final', store=True, copied=True, tracking=0)
    date_paid = fields.Date(string='Fecha de pago', store=True, copied=True, tracking=0)
    date_return = fields.Date(string='Fecha de regreso', store=True, copied=True, tracking=0)
    date_start_holidays = fields.Date(string='Fecha inicio vacaciones', store=True, copied=True, tracking=0)
    date_start = fields.Date(string='Fecha de inicio', store=True, copied=True, tracking=0)
    days_enjoyed = fields.Float(string='Días Disfrutados', store=True, copied=True, tracking=0)
    days_paid = fields.Float(string='Días pagados', store=True, copied=True, tracking=0)
    days_suspension = fields.Float(string='Días Suspendidos', store=True, copied=True, tracking=0)
    manual = fields.Boolean(string='Manual', store=True, copied=True, tracking=0)
    payslip_days = fields.Float(string='Días en Nómina', store=True, copied=True, tracking=0)
    pending_days = fields.Float(string='Días pendientes', store=True, copied=True, tracking=0)
    period_days = fields.Float(string='Días en Periodo', store=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)
    validated_days = fields.Float(string='Días validados', store=True, copied=True, tracking=0)
    worked_days = fields.Float(string='Días Trabajados', store=True, copied=True, tracking=0)


class HrHolidayLines(models.Model):
    _name = 'hr.holiday.lines'
    _description = 'Líneas de vacaciones de RRHH'

    holiday_date = fields.Date(string='Fecha', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Motivo', store=True, copied=True, tracking=0)


class HrHolidayPublic(models.Model):
    _name = 'hr.holiday.public'
    _description = 'Festivos públicos de RRHH'

    name = fields.Char(string='Festivo', store=True, required=True, copied=True, tracking=0)


class HrHolidayYear(models.Model):
    _name = 'hr.holiday.year'
    _description = 'Años de vacaciones de RRHH'

    date_end = fields.Date(string='Fecha de Finalización', store=True, required=True, copied=True, tracking=0)
    date_start = fields.Date(string='Fecha de inicio', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Año', store=True, required=True, copied=True, tracking=0)


class HrInductions(models.Model):
    _name = 'hr.inductions'
    _description = 'Inducciones de RRHH'

    days = fields.Integer(string='Días de inducción', store=True, required=True, copied=True, tracking=0)


class HrMilitaryDegree(models.Model):
    _name = 'hr.military.degree'
    _description = 'Grados militares de RRHH'

    name = fields.Char(string='Grado militar', store=True, copied=True, tracking=0)


class HrNovelty(models.Model):
    _name = 'hr.novelty'
    _description = 'Novedades de RRHH'

    access_token = fields.Char(string='Security Token', store=True, tracking=0)
    access_url = fields.Char(string='Portal Access URL', readonly=True, tracking=0)
    access_warning = fields.Text(string='Access warning', readonly=True, tracking=0)
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    amount_payment_client = fields.Float(string='Valor cobrar cliente', store=True, copied=True, tracking=0)
    amount = fields.Float(string='Valor', store=True, copied=True, tracking=100)
    approve_date = fields.Date(string='Fecha de aprobación', store=True, copied=True, tracking=100)
    close_from_solo_adicionales = fields.Boolean(string='Cerrado desde solo adicionales', store=True, copied=True,
                                                 tracking=0)
    date_end = fields.Date(string='Fecha Final', store=True, copied=True, tracking=100)
    date_start = fields.Date(string='Fecha Inicio', store=True, required=True, copied=True, tracking=100)
    description = fields.Text(string='Descripción', store=True, copied=True, tracking=0)
    inactive_definite = fields.Boolean(string='Inactivación Definitiva', store=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, readonly=True, copied=True, tracking=100)
    payment_client_date = fields.Date(string='Fecha Cobro cliente', store=True, copied=True, tracking=0)
    payment_client = fields.Boolean(string='Cobro Cliente', store=True, copied=True, tracking=0)
    quantity = fields.Float(string='Cantidad', store=True, copied=True, tracking=100)
    replace_concept = fields.Boolean(string='Remplaza Concepto', store=True, copied=True, tracking=100)
    roster = fields.Boolean(string='Origen cierre de turnos', store=True, copied=True, tracking=100)
    unit_amount = fields.Float(string='Valor Unitario', store=True, copied=True, tracking=100)


class HrNoveltyLine(models.Model):
    _name = 'hr.novelty.line'
    _description = 'Líneas de novedades de RRHH'

    amount = fields.Float(string='Valor', store=True, copied=True, tracking=0)
    inactive = fields.Boolean(string='Inactivo', store=True, copied=True, tracking=0)


class HrNoveltyLog(models.Model):
    _name = 'hr.novelty.log'
    _description = 'Registro de novedades de RRHH'

    name = fields.Char(string='Log', store=True, copied=True, tracking=0)


class HrNoveltyType(models.Model):
    _name = 'hr.novelty.type'
    _description = 'Tipos de novedades de RRHH'

    apply_extra_legal = fields.Boolean(string='Aplica Prima Extra Legal', store=True, copied=True, tracking=0)
    apply_social = fields.Boolean(string='Aplica para prestaciones sociales', store=True, copied=True, tracking=0)
    apply_vacation = fields.Boolean(string='Afecta promedio vacaciones disfrutadas', store=True, copied=True,
                                    tracking=0)
    bring_contributions_payroll = fields.Boolean(string='Llevar aportes a planilla', store=True, copied=True,
                                                 tracking=0)
    code = fields.Char(string='Código', store=True, required=True, copied=True, tracking=0)
    dep_days_worked_leaves = fields.Boolean(string='Depende de días Trabajados y Vacaciones', store=True, copied=True,
                                            tracking=0)
    dep_days_worked = fields.Boolean(string='Depende de días trabajados', store=True, copied=True, tracking=0)
    food_aid = fields.Boolean(string='Subsidio de Alimentación', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    prepaid_medicine = fields.Boolean(string='Medicina-Dental Prepagada', store=True, copied=True, tracking=0)
    settlement_agreement = fields.Boolean(string='Acuerdo de Transaccional', store=True, copied=True, tracking=0)


class HrOvertime(models.Model):
    _name = 'hr.overtime'
    _description = 'Horas extras de RRHH'

    access_token = fields.Char(string='Security Token', store=True, tracking=0)
    access_url = fields.Char(string='Portal Access URL', readonly=True, tracking=0)
    access_warning = fields.Text(string='Access warning', readonly=True, tracking=0)
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    amount = fields.Float(string='Valor', store=True, readonly=True, tracking=100)
    approve_date = fields.Date(string='Fecha de aprobación', store=True, copied=True, tracking=100)
    close_from_solo_adicionales = fields.Boolean(string='Cerrado desde solo adicionales', store=True, copied=True,
                                                 tracking=0)
    date_end = fields.Date(string='Fecha Final', store=True, copied=True, tracking=100)
    date_start_original = fields.Date(string='Inicio original', store=True, copied=True, tracking=0)
    date_start = fields.Date(string='Fecha Inicio', store=True, required=True, copied=True, tracking=100)
    from_adicional = fields.Boolean(string='Desde adicional', store=True, copied=True, tracking=100)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, readonly=True, copied=True, tracking=100)
    qty = fields.Float(string='Cantidad', store=True, required=True, copied=True, tracking=100)
    rate = fields.Float(string='Factor', readonly=True, tracking=100)
    roster = fields.Boolean(string='Origen cierre de turnos', store=True, copied=True, tracking=100)
    tipo_pago = fields.Char(string='Tipo de Pago', store=True, copied=True, tracking=100)
    total = fields.Float(string='Total', store=True, readonly=True, copied=True, tracking=100)
    unit = fields.Float(string='Valor Unitario', store=True, readonly=True, copied=True, tracking=100)


class HrOvertimeCategConfig(models.Model):
    _name = 'hr.overtime.categ.config'
    _description = 'Configuración de categorías de horas extras'

    hours_comp_turno = fields.Integer(string='Horas compensadas por turno', store=True, copied=True, tracking=0)
    rate = fields.Float(string='Factor', store=True, copied=True, tracking=0)


class HrOvertimeType(models.Model):
    _name = 'hr.overtime.type'
    _description = 'Tipos de horas extras'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0)
    code = fields.Char(string='Código', store=True, required=True, copied=True, tracking=0)
    eso_to_compensate = fields.Boolean(string='ESO/ESU A compensar', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    rate = fields.Float(string='Factor', store=True, copied=True, tracking=0)


class HrPayrollAdvance(models.Model):
    _name = 'hr.payroll.advance'
    _description = 'Anticipos de nómina'

    accounting_date = fields.Date(string='Fecha de Contabilización', store=True, copied=True, tracking=0)
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    amount_currency = fields.Float(string='Valor', store=True, copied=True, tracking=0)
    approve_date = fields.Date(string='Fecha de Aprobación', store=True, copied=True, tracking=0)
    company_amount_currency = fields.Float(string='Valor Moneda Local', readonly=True, tracking=0)
    description = fields.Text(string='Descripción', store=True, copied=True, tracking=0)
    difference = fields.Float(string='Diferencia', store=True, readonly=True, tracking=0)
    end_date = fields.Date(string='Fecha Final', store=True, copied=True, tracking=0)
    exchange_rate = fields.Float(string='Tasa de Cambio', store=True, copied=True, tracking=0)
    expire_date = fields.Date(string='Fecha de Vencimiento', store=True, readonly=True, tracking=0)
    is_paid = fields.Boolean(string='¿Está pagado?', store=True, readonly=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    partial_reconciled = fields.Boolean(string='Parcialmente Conciliado', readonly=True, tracking=0)
    pay_date = fields.Date(string='Fecha de Pago', store=True, copied=True, tracking=0)
    payment_reference = fields.Char(string='Referencia de Pago', store=True, copied=True, tracking=0)
    remaining = fields.Float(string='Balance', store=True, tracking=0)
    request_date = fields.Date(string='Fecha de Solicitud', store=True, copied=True, tracking=0)
    start_date = fields.Date(string='Fecha de inicio', store=True, copied=True, tracking=0)
    total_expense = fields.Float(string='Total Legalizado', store=True, readonly=True, tracking=0)


class HrPayrollAdvanceWizard(models.Model):
    _name = 'hr.payroll.advance.wizard'
    _description = 'Asistente de anticipos de nómina'

    date_from = fields.Date(string='Fecha inicio', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha fin', store=True, required=True, copied=True, tracking=0)


class HrPayrollEmbargo(models.Model):
    _name = 'hr.payroll.embargo'
    _description = 'Embargos de nómina'

    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    amount_salary_value = fields.Float(string='Valor del monto', store=True, copied=True, tracking=0)
    amount_salary = fields.Boolean(string='Monto o tope', store=True, copied=True, tracking=0)
    court_account_number = fields.Char(string='Número de cuenta del juzgado', store=True, copied=True, tracking=0)
    court_code = fields.Char(string='Código del juzgado old', store=True, copied=True, tracking=0)
    date_start = fields.Date(string='Fecha de inicio', store=True, copied=True, tracking=0)
    date = fields.Date(string='Fecha', store=True, copied=True, tracking=0)
    description = fields.Text(string='Descripción', store=True, copied=True, tracking=0)
    destination_office = fields.Char(string='Oficina de destino', store=True, copied=True, tracking=0)
    due = fields.Float(string='Deuda', store=True, copied=True, tracking=0)
    exceed_salary = fields.Boolean(string='1/5 De lo que exceda el salario mínimo legal mensual vigente', store=True,
                                   copied=True, tracking=0)
    exceed_without_discount_salary = fields.Boolean(
        string='1/5 De lo que exceda el salario mínimo Sin Descuento de Ley', store=True, copied=True, tracking=0)
    file_number = fields.Char(string='Número de expediente', store=True, copied=True, tracking=0)
    fixed_fee_value = fields.Float(string='Valor de la cuota fija', store=True, copied=True, tracking=0)
    fixed_fee = fields.Boolean(string='Cuota Fija', store=True, copied=True, tracking=0)
    located = fields.Char(string='Radicado', store=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    more_smmlv_percentage = fields.Boolean(string='Porcentaje que exceda el salario mínimo', store=True, copied=True,
                                           tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    number_process_court = fields.Char(string='Número del proceso en la corte', store=True, copied=True, tracking=0)
    office = fields.Char(string='Oficio', store=True, copied=True, tracking=0)
    payout_percentage_value = fields.Float(string='Valor del porcentaje', store=True, copied=True, tracking=0)
    payout_percentage = fields.Boolean(string='Porcentaje de pago', store=True, copied=True, tracking=0)
    pending_debt = fields.Float(string='Deuda pendiente', store=True, copied=True, tracking=0)
    savings_account = fields.Char(string='Cuenta de ahorro', store=True, copied=True, tracking=0)
    share = fields.Float(string='Cuota', store=True, copied=True, tracking=0)
    smmlv_percentage = fields.Boolean(string='Porcentaje del salario mínimo', store=True, copied=True, tracking=0)
    without_discount_percentage = fields.Boolean(string='Porcentaje Sin Descuento de Ley', store=True, copied=True,
                                                 tracking=0)


class HrPayrollEmbargoCategory(models.Model):
    _name = 'hr.payroll.embargo.category'
    _description = 'Categorías de embargos de nómina'

    code_emb = fields.Char(string='Código Archivo', store=True, copied=True, tracking=0)
    code = fields.Char(string='Código', store=True, copied=True, tracking=0)
    description = fields.Text(string='Descripción', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)


class HrPayrollEmbargoFileWizard(models.Model):
    _name = 'hr.payroll.embargo.file.wizard'
    _description = 'Asistente de archivo de embargos de nómina'

    consecutive = fields.Char(string='CC', store=True, copied=True, tracking=0)
    date_end = fields.Date(string='Fecha final', store=True, copied=True, tracking=0)
    date_start = fields.Date(string='Fecha Inicial', store=True, copied=True, tracking=0)
    file_name = fields.Text(string='Archivo', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre de archivo', store=True, copied=True, tracking=0)


class HrPayrollEmbargoHistory(models.Model):
    _name = 'hr.payroll.embargo.history'
    _description = 'Historial de embargos de nómina'

    date = fields.Date(string='Fecha', store=True, copied=True, tracking=0)
    reason = fields.Text(string='Motivo de devolución', store=True, copied=True, tracking=0)
    state = fields.Char(string='Estado', store=True, tracking=0)


class HrPayrollEmbargoHistoryWizard(models.Model):
    _name = 'hr.payroll.embargo.history.wizard'
    _description = 'Asistente de historial de embargos de nómina'

    date = fields.Date(string='Fecha', store=True, copied=True, tracking=0)
    reason = fields.Text(string='Motivo de cierre', store=True, copied=True, tracking=0)


class HrPayrollEmbargoLine(models.Model):
    _name = 'hr.payroll.embargo.line'
    _description = 'Líneas de embargos de nómina'

    base_devengado = fields.Float(string='Base de devengo', store=True, copied=True, tracking=0)
    date = fields.Date(string='Fecha', store=True, copied=True, tracking=0)
    description = fields.Char(string='Nombre', readonly=True, tracking=0)
    embargo_due = fields.Float(string='Deuda', readonly=True, tracking=0)
    embargo_share = fields.Float(string='Cuota', readonly=True, tracking=0)
    share_value = fields.Float(string='Valor de la cuota', store=True, copied=True, tracking=0)


class HrPayrollEmbargoLineExtra(models.Model):
    _name = 'hr.payroll.embargo.line.extra'
    _description = 'Líneas extras de embargos de nómina'

    extra_value = fields.Float(string='Valor extra', store=True, copied=True, tracking=0)


class HrPayrollEmbargoPriorityLine(models.Model):
    _name = 'hr.payroll.embargo.priority.line'
    _description = 'Líneas de prioridad de embargos de nómina'

    priority = fields.Integer(string='Prioridad', store=True, copied=True, tracking=0)


class HrPayrollEmbargoType(models.Model):
    _name = 'hr.payroll.embargo.type'
    _description = 'Tipos de embargos de nómina'

    description = fields.Text(string='Descripción', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)


class HrPayrollExtrahours(models.Model):
    _name = 'hr.payroll.extrahours'
    _description = 'Horas extras de nómina'

    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    approve_date = fields.Date(string='Fecha de Aprobación', store=True, readonly=True, copied=True, tracking=0)
    date_end = fields.Datetime(string='Finaliza', store=True, readonly=True, copied=True, tracking=0)
    date_start = fields.Datetime(string='Comienza', store=True, readonly=True, required=True, copied=True, tracking=0)
    description = fields.Text(string='Descripción', store=True, readonly=True, copied=True, tracking=0)
    duracion = fields.Float(string='Duración', store=True, readonly=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Código', store=True, readonly=True, copied=True, tracking=0)
    roster = fields.Boolean(string='Origen cierre de turnos', store=True, copied=True, tracking=0)
    total = fields.Float(string='Total', store=True, readonly=True, copied=True, tracking=0)
    unit = fields.Float(string='Valor Unitario', store=True, readonly=True, copied=True, tracking=0)


class HrPayrollExtrahoursTypeTime(models.Model):
    _name = 'hr.payroll.extrahours.type.time'
    _description = 'Tiempos de tipos de horas extras de nómina'

    hour_from = fields.Float(string='Desde', store=True, required=True, copied=True, tracking=0)


class HrPayrollNovedades(models.Model):
    _name = 'hr.payroll.novedades'
    _description = 'Novedades de nómina'

    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    apply_payroll_novedad = fields.Boolean(string='Aplica a nómina', store=True, copied=True, tracking=0)
    approve_date = fields.Date(string='Fecha de Aprobación', store=True, readonly=True, copied=True, tracking=0)
    cantidad = fields.Float(string='Cantidad', store=True, readonly=True, copied=True, tracking=0)
    date = fields.Date(string='Fecha', store=True, readonly=True, required=True, copied=True, tracking=0)
    description = fields.Text(string='Descripción', store=True, readonly=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Código', store=True, readonly=True, copied=True, tracking=0)
    neto = fields.Boolean(string='Regla del Neto a Pagar', store=True, copied=True, tracking=0)
    roster = fields.Boolean(string='Origen cierre de turnos', store=True, copied=True, tracking=0)
    total = fields.Float(string='Total', store=True, readonly=True, tracking=0)
    valor = fields.Float(string='Valor', store=True, readonly=True, copied=True, tracking=0)


class HrPayrollNovedadesCategory(models.Model):
    _name = 'hr.payroll.novedades.category'
    _description = 'Categorías de novedades de nómina'

    afc = fields.Boolean(string='AFC', store=True, copied=True, tracking=0)
    code = fields.Char(string='Código', store=True, required=True, copied=True, tracking=0)
    ded_rent = fields.Boolean(string='Aporte voluntario', store=True, copied=True, tracking=0)
    descripcion = fields.Text(string='Descripción', store=True, copied=True, tracking=0)
    erent = fields.Boolean(string='Ingreso exento de retención', store=True, copied=True, tracking=0)
    hour_novelty = fields.Boolean(string='Novedad por horas', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)


class HrPayslip(models.Model):
    _name = 'hr.payslip'
    _description = 'Nóminas'

    accepted_rejected_datetime = fields.Datetime(string='Datetime of Accepted/Rejected', store=True, tracking=0)
    access_token = fields.Char(string='Access token', store=True, tracking=0)
    accounting_date = fields.Date(string='Fecha de Contabilización', store=True, copied=True, tracking=0)
    amount_total_words = fields.Char(string='Neto Total en Palabras', readonly=True, tracking=0)
    amount_total = fields.Float(string='Neto Total', readonly=True, tracking=0)
    dbname = fields.Char(string='DB Name', readonly=True, tracking=0)
    error_log = fields.Text(string='Errores', store=True, readonly=True, copied=True, tracking=0)
    is_accepted_rejected = fields.Boolean(string='Is Accepted/Rejected?', store=True, tracking=0)
    liquidation_date = fields.Date(string='Fecha de Liquidación', store=True, copied=True, tracking=0)
    mean_ces = fields.Float(string='Promedio Cesantías', store=True, copied=True, tracking=0)
    mean_ices = fields.Float(string='Promedio Interés Cesantías', store=True, copied=True, tracking=0)
    mean_prima = fields.Float(string='Promedio Prima', store=True, copied=True, tracking=0)
    mean_vac = fields.Float(string='Promedio Vacaciones', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, readonly=True, copied=True, tracking=0)
    portal_exclude = fields.Boolean(string='Excluir del Portal', store=True, copied=True, tracking=0)
    warn_inactive_certificate = fields.Boolean(string='Warn About Inactive Certificate?', readonly=True, tracking=0)
    warn_remaining_certificate = fields.Boolean(string='Warn About Remainings?', readonly=True, tracking=0)


class HrPayslipConceptEpayrollType(models.Model):
    _name = 'hr.payslip.concept.epayroll.type'
    _description = 'Tipos de conceptos de nómina electrónica'

    code = fields.Char(string='Código', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)


class HrPayslipConceptEpayrollTypeCode(models.Model):
    _name = 'hr.payslip.concept.epayroll.type.code'
    _description = 'Códigos de tipos de conceptos de nómina electrónica'

    code = fields.Char(string='Código', store=True, copied=True, tracking=0)
    exclude = fields.Boolean(string='Excluir', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)


class HrPayslipConceptReport(models.Model):
    _name = 'hr.payslip.concept.report'
    _description = 'Reportes de conceptos de nómina'

    company_cost = fields.Boolean(string='Informe general de nómina', store=True, copied=True, tracking=0)
    company_expense = fields.Boolean(string='Informe general de gastos de Compañía', store=True, copied=True,
                                     tracking=0)
    concept_code = fields.Char(string='Código de concepto', store=True, copied=True, tracking=0)
    end_date = fields.Date(string='Fecha hasta', store=True, required=True, copied=True, tracking=0)
    landscape = fields.Boolean(string='Horizontal', store=True, copied=True, tracking=0)
    start_date = fields.Date(string='Fecha desde', store=True, required=True, copied=True, tracking=0)
    workcenter = fields.Char(string='Centro de trabajo', store=True, copied=True, tracking=0)


class HrPayslipConceptsCode(models.Model):
    _name = 'hr.payslip.concepts.code'
    _description = 'Códigos de conceptos de nómina'

    code = fields.Char(string='Código', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)


class HrPayslipDay(models.Model):
    _name = 'hr.payslip.day'
    _description = 'Días de nómina'

    day = fields.Integer(string='Día', store=True, copied=True, tracking=0)
    is_vac = fields.Boolean(string='Vacaciones', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', readonly=True, tracking=0)


class HrPayslipDianDocument(models.Model):
    _name = 'hr.payslip.dian.document'
    _description = 'Documentos DIAN de nómina'

    accepted_rejected_datetime = fields.Datetime(string='Datetime of Accepted/Rejected', store=True, tracking=0)
    access_token = fields.Char(string='Access token', store=True, tracking=0)
    ad_zipped_file = fields.Text(string='AttachedDocument Zipped File', store=True, copied=True, tracking=0)
    ad_zipped_filename = fields.Char(string='AttachedDocument Zipped Filename', store=True, copied=True, tracking=0)
    ar_xml_file = fields.Text(string='ApplicationResponse XML File', store=True, copied=True, tracking=0)
    ar_xml_filename = fields.Char(string='ApplicationResponse XML Filename', store=True, copied=True, tracking=0)
    cune_uncoded = fields.Char(string='CUNE Uncoded', store=True, copied=True, tracking=0)
    cune = fields.Char(string='CUNE', store=True, copied=True, tracking=0)
    date_end = fields.Date(string='End Date', store=True, copied=True, tracking=0)
    date_start = fields.Date(string='Start Date', store=True, copied=True, tracking=0)
    dbname = fields.Char(string='DB Name', readonly=True, tracking=0)
    get_status_zip_response = fields.Text(string='Response', store=True, copied=True, tracking=0)
    invoice_url = fields.Char(string='Invoice Url', store=True, copied=True, tracking=0)
    is_accepted_rejected = fields.Boolean(string='Is Accepted/Rejected?', store=True, tracking=0)
    mail_sent = fields.Boolean(string='Mail Sent?', store=True, copied=True, tracking=0)
    name = fields.Char(string='Name', store=True, tracking=0)
    payslip_datetime = fields.Datetime(string='Payslip Datetime', store=True, tracking=0)
    qr_image = fields.Text(string='QR Code', readonly=True, tracking=0)
    software_security_code_uncoded = fields.Char(string='SoftwareSecurityCode Uncoded', store=True, copied=True,
                                                 tracking=0)
    software_security_code = fields.Char(string='SoftwareSecurityCode', store=True, copied=True, tracking=0)
    validation_datetime = fields.Datetime(string='Validation Datetime', store=True, copied=True, tracking=0)
    warn_inactive_certificate = fields.Boolean(string='Warn About Inactive Certificate?', readonly=True, tracking=0)
    warn_remaining_certificate = fields.Boolean(string='Warn About Remainings?', readonly=True, tracking=0)
    xml_base_file = fields.Text(string='XML Base File', store=True, copied=True, tracking=0)
    xml_base_filename = fields.Char(string='XML Base Filename', store=True, copied=True, tracking=0)
    xml_file = fields.Text(string='Invoice XML File', store=True, copied=True, tracking=0)
    xml_filename = fields.Char(string='Invoice XML Filename', store=True, copied=True, tracking=0)
    zip_key = fields.Char(string='ZipKey', store=True, copied=True, tracking=0)
    zipped_file = fields.Text(string='Zipped File', store=True, copied=True, tracking=0)
    zipped_filename = fields.Char(string='Zipped Filename', store=True, copied=True, tracking=0)


class HrPayslipDianDocumentLine(models.Model):
    _name = 'hr.payslip.dian.document.line'
    _description = 'Líneas de documentos DIAN de nómina'

    send_async_reason = fields.Char(string='Reason', store=True, copied=True, tracking=0)
    send_async_response = fields.Text(string='Response', store=True, copied=True, tracking=0)
    send_async_status_code = fields.Char(string='Status Code', store=True, copied=True, tracking=0)


class HrPayslipEmbargoLine(models.Model):
    _name = 'hr.payslip.embargo.line'
    _description = 'Líneas de embargos de nómina'

    embargo_amount = fields.Float(string='Valor', store=True, copied=True, tracking=0)
    embargo_due = fields.Float(string='Cuota', store=True, copied=True, tracking=0)


class HrPayslipLine(models.Model):
    _name = 'hr.payslip.line'
    _description = 'Líneas de nómina'

    afc = fields.Boolean(string='AFC', store=True, copied=True, tracking=0)
    contract_prod_lec = fields.Float(string='Lectivo', store=True, copied=True, tracking=0)
    contract_prod_prod = fields.Float(string='Productiva', store=True, copied=True, tracking=0)
    erent = fields.Boolean(string='Exento de renta', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    qty = fields.Float(string='Cantidad', store=True, copied=True, tracking=0)
    rate = fields.Float(string='Porcentaje', store=True, copied=True, tracking=0)
    total = fields.Float(string='Total', store=True, copied=True, tracking=0)
    value_overtime = fields.Float(string='Cantidad Hora Extra', store=True, copied=True, tracking=0)
    value = fields.Float(string='Valor', store=True, copied=True, tracking=0)


class HrPayslipLineReport(models.Model):
    _name = 'hr.payslip.line.report'
    _description = 'Reportes de líneas de nómina'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    qty = fields.Float(string='Cantidad', store=True, copied=True, tracking=0)
    rate = fields.Float(string='Porcentaje', store=True, copied=True, tracking=0)
    total = fields.Float(string='Total', store=True, copied=True, tracking=0)
    value = fields.Float(string='Valor', store=True, copied=True, tracking=0)


class HrPayslipProcessing(models.Model):
    _name = 'hr.payslip.processing'
    _description = 'Procesamiento de nóminas'

    accounting_date = fields.Date(string='Fecha de Contabilización', store=True, required=True, copied=True, tracking=0)
    approval_managers = fields.Boolean(string='Gestores de Aprobación', readonly=True, tracking=0)
    correo = fields.Boolean(string='Correo Enviado', store=True, copied=True, tracking=1)
    error_log = fields.Text(string='Errores', store=True, readonly=True, copied=True, tracking=0)
    liquidation_date = fields.Date(string='Fecha de Liquidación', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, tracking=0)


class HrPayslipType(models.Model):
    _name = 'hr.payslip.type'
    _description = 'Tipos de nóminas'

    load_contract_states = fields.Boolean(string='Cargar todos los Contratos', store=True, copied=True, tracking=0)
    load_contract_with_novelty = fields.Boolean(string='Cargar contratos si tiene novedades', store=True, copied=True,
                                                tracking=0)
    load_icesantias_lastyear = fields.Boolean(string='Cargar cesantías, intereses año anterior', store=True,
                                              copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    portal_exclude = fields.Boolean(string='Excluir del Portal', store=True, copied=True, tracking=0)


class HrPeriod(models.Model):
    _name = 'hr.period'
    _description = 'Períodos de RRHH'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0)
    closed = fields.Boolean(string='Cerrado', store=True, copied=True, tracking=0)
    end_date = fields.Date(string='Fin de Corte', store=True, required=True, copied=True, tracking=0)
    end = fields.Date(string='Fin período', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, readonly=True, copied=True, tracking=0)
    start_date = fields.Date(string='Comienzo de Corte', store=True, required=True, copied=True, tracking=0)
    start = fields.Date(string='Inicio período', store=True, required=True, copied=True, tracking=0)


class HrPeriodCreator(models.Model):
    _name = 'hr.period.creator'
    _description = 'Creador de períodos de RRHH'

    notes = fields.Text(string='Notas', store=True, readonly=True, copied=True, tracking=0)


class HrProgramacionLineRun(models.Model):
    _name = 'hr.programacion.line.run'
    _description = 'Ejecución de líneas de programación de RRHH'

    n_times = fields.Integer(string='N Times', store=True, copied=True, tracking=0)


class HrPublicService(models.Model):
    _name = 'hr.public.service'
    _description = 'Servicios públicos de RRHH'

    name = fields.Char(string='Servicio público', store=True, copied=True, tracking=0)


class HrReferencias(models.Model):
    _name = 'hr.referencias'
    _description = 'Referencias de RRHH'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    rela = fields.Char(string='Relación', store=True, required=True, copied=True, tracking=0)
    tele = fields.Char(string='Teléfono', store=True, required=True, copied=True, tracking=0)


class HrRequisicion(models.Model):
    _name = 'hr.requisicion'
    _description = 'Requisiciones de RRHH'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    actividad = fields.Char(string='Actividades', store=True, copied=True, tracking=1)
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    x_and = fields.Char(string='Diligencia Las Líneas', store=True, copied=True, tracking=1)
    auxilio_transporte_grupal = fields.Boolean(string='Auxilio de Transporte', store=True, tracking=1)
    calcula = fields.Char(string='Calculado', copied=True, tracking=1)
    cantidad = fields.Integer(string='Cantidad de Personal', store=True, copied=True, tracking=1)
    cc = fields.Char(string='No Identificación', store=True, tracking=1)
    codigo_kaptus = fields.Char(string='No Requisición Kactus', store=True, copied=True, tracking=1)
    competencias = fields.Text(string='Competencias', store=True, copied=True, tracking=1)
    compuerta_general = fields.Boolean(string='Compuerta General', store=True, copied=True, tracking=1)
    compuerta_verificadora = fields.Boolean(string='Compuerta Verificadora', store=True, readonly=True, tracking=1)
    compuerta_verificar_lineas = fields.Boolean(string='Compuerta Verificar Líneas', store=True, readonly=True,
                                                tracking=1)
    counter_global = fields.Text(string='Vacante cubierta', store=True, tracking=1)
    descripcion_motivo_1 = fields.Char(string='Descripción del Motivo', store=True, copied=True, tracking=1)
    edit_seleccion = fields.Boolean(string='Edición selección', store=True, copied=True, tracking=1)
    es_operativo = fields.Boolean(string='Es Operativo?', store=True, tracking=1)
    es_urgente = fields.Boolean(string='¿Es Urgente?', store=True, copied=True, tracking=1)
    experiencia_requerida = fields.Char(string='Experiencia Requerida', store=True, copied=True, tracking=1)
    fec_ven_con = fields.Datetime(string='Fecha Vencimiento Contrato Comercial', tracking=0)
    fecha_inicio_estimado = fields.Date(string='Fecha de Inicio Estimada', store=True, copied=True, tracking=1)
    gender_value = fields.Char(string='Para mostrar otro', store=True, tracking=1)
    lineas_bloqueadas = fields.Boolean(string='Líneas bloqueadas', store=True, copied=True, tracking=1)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=1)
    nomina_observacion = fields.Char(string='Observación de Nómina', store=True, copied=True, tracking=1)
    observacion_3 = fields.Char(string='Observación Turno/Horario/Jornada', store=True, copied=True, tracking=1)
    observaciones_nomina = fields.Text(string='Observación', store=True, copied=True, tracking=1)
    observaciones = fields.Text(string='Observaciones', store=True, copied=True, tracking=1)
    otro_2 = fields.Char(string='Otro', store=True, copied=True, tracking=1)
    return_reason = fields.Text(string='Motivo Devolución', store=True, copied=True, tracking=1)
    return_response_user_label_1 = fields.Char(string='Att:', store=True, tracking=1)
    return_response_user_label = fields.Char(string='Att:', store=True, tracking=1)
    return_response = fields.Text(string='Respuesta Coordinador', store=True, copied=True, tracking=1)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=1)
    state = fields.Char(string='Estado Técnico', store=True, tracking=1)
    term_value = fields.Char(string='Para mostrar otro', store=True, tracking=1)
    tiempo_fijo = fields.Char(string='¿Cuánto Tiempo?', store=True, copied=True, tracking=1)
    tipo_personal2 = fields.Char(string='Tipo de Personal', store=True, copied=True, tracking=1)
    turno = fields.Char(string='Turno', store=True, copied=True, tracking=1)
    validado = fields.Boolean(string='Validador', store=True, copied=True, tracking=1)


class HrRequisicionDotacion(models.Model):
    _name = 'hr.requisicion.dotacion'
    _description = 'Dotaciones de requisiciones de RRHH'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    description = fields.Text(string='Descripción', store=True, copied=True, tracking=1)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=1)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=1)


class HrRequisicionEstado(models.Model):
    _name = 'hr.requisicion.estado'
    _description = 'Estados de requisiciones de RRHH'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    codigo = fields.Char(string='Código', store=True, copied=True, tracking=1)
    description = fields.Text(string='Descripción', store=True, copied=True, tracking=1)
    name = fields.Char(string='Estado', store=True, copied=True, tracking=1)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=1)


class HrRequisicionEstructuraSalarial(models.Model):
    _name = 'hr.requisicion.estructura.salarial'
    _description = 'Estructuras salariales de requisiciones de RRHH'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    name = fields.Float(string='Valor', store=True, copied=True, tracking=1)
    periodicidad = fields.Boolean(string='X Turno Laborado', store=True, copied=True, tracking=1)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=1)


class HrRequisicionLinea(models.Model):
    _name = 'hr.requisicion.linea'
    _description = 'Líneas de requisiciones de RRHH'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    applied_flag = fields.Boolean(string='Cupo aplicado a HR', store=True, tracking=1)
    auxilio_transporte = fields.Boolean(string='Auxilio de Transporte', store=True, tracking=1)
    codigo_kaptus = fields.Char(string='No Requisición Kaptus', store=True, tracking=1)
    compuerta_linea = fields.Boolean(string='Compuerta Línea', store=True, readonly=True, tracking=1)
    date_start = fields.Date(string='Fecha Inicio Nuevo C', store=True, tracking=1)
    employee_cedula = fields.Char(string='No Identificación', store=True, tracking=1)
    fec_ven_con = fields.Datetime(string='Fecha Vencimiento Contrato Comercial', tracking=0)
    fecha_fin1 = fields.Date(string='Fecha Fin', store=True, tracking=1)
    fecha_inicio1 = fields.Date(string='Fecha Inicio', store=True, tracking=1)
    fecha_novedad = fields.Date(string='Fecha de Novedad', store=True, readonly=True, tracking=1)
    gender_value = fields.Char(string='Para mostrar otro', store=True, tracking=1)
    lineas_bloqueadas = fields.Boolean(string='Líneas bloqueadas', store=True, copied=True, tracking=1)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=1)
    no_reintegro = fields.Boolean(string='No Reintegro', store=True, copied=True, tracking=1)
    nota_retiro = fields.Char(string='Observaciones del Retiro', store=True, readonly=True, tracking=1)
    observacion_lineas_requisicion = fields.Char(string='Observaciones', store=True, copied=True, tracking=1)
    otro_2 = fields.Char(string='Otro', store=True, copied=True, tracking=1)
    requisition_counter = fields.Integer(string='Requisición Cubierta', store=True, tracking=1)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=1)
    settlement_date_id = fields.Date(string='Fecha de Liquidación', store=True, tracking=1)
    state = fields.Char(string='Estado Técnico', store=True, tracking=1)


class HrRequisicionLineaEstado(models.Model):
    _name = 'hr.requisicion.linea.estado'
    _description = 'Estados de líneas de requisiciones de RRHH'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    codigo = fields.Char(string='Código', store=True, copied=True, tracking=1)
    description = fields.Text(string='Descripción', store=True, copied=True, tracking=1)
    name = fields.Char(string='Estado', store=True, copied=True, tracking=1)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=1)


class HrRequisicionLineaTipoVehiculo(models.Model):
    _name = 'hr.requisicion.linea.tipo.vehiculo'
    _description = 'Tipos de vehículos de líneas de requisiciones de RRHH'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    codigo = fields.Char(string='Código', store=True, copied=True, tracking=1)
    description = fields.Text(string='Descripción', store=True, copied=True, tracking=1)
    name = fields.Char(string='Estado', store=True, copied=True, tracking=1)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=1)


class HrRequisicionMotivo(models.Model):
    _name = 'hr.requisicion.motivo'
    _description = 'Motivos de requisiciones de RRHH'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    descripcion = fields.Text(string='Descripción', store=True, copied=True, tracking=1)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=1)


class HrRosterAdicionalDay(models.Model):
    _name = 'hr.roster.adicional.day'
    _description = 'Días adicionales de programación de turnos'

    custom_time = fields.Boolean(string='Horario personalizado', store=True, copied=True, tracking=0)
    date = fields.Date(string='Fecha', store=True, copied=True, tracking=0)
    time_in = fields.Char(string='Entrada', store=True, required=True, copied=True, tracking=0)
    time_out = fields.Char(string='Salida', store=True, required=True, copied=True, tracking=0)


class HrRosterBono(models.Model):
    _name = 'hr.roster.bono'
    _description = 'Bonos de programación de turnos'

    code = fields.Char(string='Código', store=True, copied=True, tracking=0)
    name = fields.Char(string='Descripción', store=True, copied=True, tracking=0)


class HrRosterCambioUpdate(models.Model):
    _name = 'hr.roster.cambio.update'
    _description = 'Actualización de cambios de programación de turnos'

    date = fields.Date(string='Fecha', store=True, required=True, copied=True, tracking=0)


class HrRosterCloseDistribution(models.Model):
    _name = 'hr.roster.close.distribution'
    _description = 'Distribución de cierre de programación de turnos'

    date = fields.Date(string='Fecha de referencia', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', readonly=True, tracking=0)
    rate = fields.Float(string='Distribución', store=True, copied=True, tracking=0)


class HrRosterConceptDistribution(models.Model):
    _name = 'hr.roster.concept.distribution'
    _description = 'Distribución de conceptos de programación de turnos'

    distribution = fields.Float(string='Distribución', store=True, copied=True, tracking=0)


class HrRosterHorario(models.Model):
    _name = 'hr.roster.horario'
    _description = 'Horarios de programación de turnos'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=100)
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    description = fields.Text(string='Descripción', store=True, copied=True, tracking=100)
    diurn_comp = fields.Float(string='Componente Diurno', store=True, copied=True, tracking=100)
    duration = fields.Float(string='Duración', readonly=True, tracking=0)
    editar = fields.Boolean(string='Editar', store=True, copied=True, tracking=1)
    end_break = fields.Char(string='Fin Descanso', store=True, copied=True, tracking=100)
    is_rest = fields.Boolean(string='Turno con Descanso?', store=True, copied=True, tracking=100)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Código', store=True, copied=True, tracking=100)
    nocturn_comp = fields.Float(string='Componente Nocturno', store=True, copied=True, tracking=100)
    start_break = fields.Char(string='Inicio Descanso', store=True, copied=True, tracking=100)
    time_in = fields.Char(string='Entrada', store=True, required=True, copied=True, tracking=100)
    time_out = fields.Char(string='Salida', store=True, required=True, copied=True, tracking=100)


class HrRosterModalidad(models.Model):
    _name = 'hr.roster.modalidad'
    _description = 'Modalidades de programación de turnos'

    basic_salary = fields.Float(string='Salario Básico', store=True, copied=True, tracking=0)
    bearing_value = fields.Float(string='Valor Rodamiento', store=True, copied=True, tracking=0)
    desfase = fields.Integer(string='Desfase', store=True, copied=True, tracking=100)
    festivo = fields.Boolean(string='Festivo', store=True, copied=True, tracking=100)
    is_parent = fields.Boolean(string='Es modalidad padre?', store=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=100)
    numero_personal = fields.Integer(string='Número Personal', store=True, required=True, copied=True, tracking=100)
    numero_personal2 = fields.Float(string='Número Personal (Capacidad Real)', store=True, copied=True, tracking=100)
    supplementary_work_value = fields.Float(string='Valor Trabajo Suplementario', store=True, copied=True, tracking=0)
    transport_assistant = fields.Float(string='Auxilio de transporte', store=True, copied=True, tracking=0)


class HrRosterPrefactura(models.Model):
    _name = 'hr.roster.prefactura'
    _description = 'Prefacturas de programación de turnos'

    amount_tax = fields.Float(string='Total impuestos', store=True, copied=True, tracking=0)
    amount_total = fields.Float(string='Total', store=True, copied=True, tracking=0)
    amount_untaxed = fields.Float(string='Subtotal', store=True, copied=True, tracking=0)
    date_prefactura = fields.Date(string='Fecha prefactura', store=True, copied=True, tracking=0)
    pref_number = fields.Char(string='Prefactura', store=True, readonly=True, copied=True, tracking=0)
    ref1 = fields.Char(string='Referencia', store=True, copied=True, tracking=0)


class HrRosterPrefacturaLine(models.Model):
    _name = 'hr.roster.prefactura.line'
    _description = 'Líneas de prefacturas de programación de turnos'

    adicional = fields.Float(string='Costos adicionales', store=True, copied=True, tracking=0)
    ays = fields.Float(string='A&S', store=True, copied=True, tracking=0)
    dias_mes = fields.Float(string='Días del mes', store=True, copied=True, tracking=0)
    dias_resumen = fields.Char(string='Días resumidos', store=True, copied=True, tracking=0)
    dias = fields.Char(string='Días', store=True, copied=True, tracking=0)
    distribution = fields.Float(string='Distribución', store=True, copied=True, tracking=0)
    dom_diur = fields.Float(string='Hrs dom diurnas', store=True, copied=True, tracking=0)
    dom_noct = fields.Float(string='Hrs dom nocturnas', store=True, copied=True, tracking=0)
    duracion = fields.Integer(string='Duración', store=True, copied=True, tracking=0)
    fes_diur = fields.Float(string='Hrs fes diurnas', store=True, copied=True, tracking=0)
    fes_noct = fields.Float(string='Hrs fes nocturnas', store=True, copied=True, tracking=0)
    horario = fields.Char(string='Horario', store=True, copied=True, tracking=0)
    horas_diurno = fields.Float(string='Horas diurnas', store=True, copied=True, tracking=0)
    horas_nocturno = fields.Float(string='Horas nocturnas', store=True, copied=True, tracking=0)
    name = fields.Char(string='Descripción', store=True, copied=True, tracking=0)
    pref_number = fields.Char(string='Prefactura', store=True, readonly=True, tracking=0)
    puesto_int_code = fields.Char(string='Código interno del cliente', store=True, readonly=True, tracking=0)
    puesto_int_zone = fields.Char(string='Zona interna del cliente', store=True, readonly=True, tracking=0)
    quantity = fields.Float(string='Cantidad', store=True, copied=True, tracking=0)
    service_quantity = fields.Float(string='Cantidad', store=True, copied=True, tracking=0)
    subtotal = fields.Float(string='Subtotal antes de A&S', store=True, copied=True, tracking=0)
    total_ays = fields.Float(string='Total A&S', store=True, copied=True, tracking=0)
    total_validated = fields.Float(string='Total validado', store=True, copied=True, tracking=0)
    total = fields.Float(string='Total general', store=True, copied=True, tracking=0)
    valor_total = fields.Float(string='Valor total', store=True, copied=True, tracking=0)
    valor = fields.Float(string='Valor antes de A&S', store=True, copied=True, tracking=0)


class HrRosterProgramacion(models.Model):
    _name = 'hr.roster.programacion'
    _description = 'Programaciones de turnos'

    billed_diurn_hours = fields.Float(string='Horas Diurnas Facturadas', readonly=True, tracking=0)
    billed_hours = fields.Float(string='Total Horas Facturadas', readonly=True, tracking=0)
    billed_nocturn_hours = fields.Float(string='Horas Nocturnas Facturadas', readonly=True, tracking=0)
    contract_date = fields.Date(string='Fecha Objetivos', store=True, copied=True, tracking=0)
    contratado = fields.Boolean(string='Contrato Vigente', store=True, copied=True, tracking=0)
    d_disponibles = fields.Boolean(string='Disponibles', store=True, copied=True, tracking=0)
    desc_date = fields.Date(string='Fecha objetivo', store=True, copied=True, tracking=0)
    descanso = fields.Boolean(string='Empleados en descanso', store=True, copied=True, tracking=0)
    disp_date = fields.Date(string='Fecha Objetivo', store=True, copied=True, tracking=0)
    disponibles = fields.Char(string='Disponibles', store=True, copied=True, tracking=0)
    dobl_date = fields.Date(string='Fecha objetivo', store=True, copied=True, tracking=0)
    doblaje = fields.Boolean(string='Empleados para doblar', store=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    notification_text = fields.Text(string='Notificación de Ausencias no adjuntas', readonly=True, tracking=0)
    qty_employees = fields.Integer(string='Personal asignado', readonly=True, tracking=0)
    scheduled_diurn_hours = fields.Float(string='Horas Diurnas Programadas', readonly=True, tracking=0)
    scheduled_hours = fields.Float(string='Total Horas Programadas', readonly=True, tracking=0)
    scheduled_nocturn_hours = fields.Float(string='Horas Nocturnas Programadas', readonly=True, tracking=0)
    sin_prog = fields.Boolean(string='Sin programación', store=True, copied=True, tracking=0)
    todos = fields.Boolean(string='Todos los empleados', store=True, copied=True, tracking=0)
    year = fields.Integer(string='Año', store=True, required=True, copied=True, tracking=0)


class HrRosterProgramacionLine(models.Model):
    _name = 'hr.roster.programacion.line'
    _description = 'Líneas de programación de turnos'

    adicional = fields.Boolean(string='Core de programación', store=True, copied=True, tracking=0)
    code_position = fields.Char(string='Puesto', store=True, readonly=True, tracking=0)
    concat_contract = fields.Char(string='Personal', store=True, readonly=True, tracking=0)
    concat_name = fields.Char(string='Info Puesto', store=True, readonly=True, tracking=0)
    days = fields.Integer(string='Días', readonly=True, tracking=0)
    is_select_wizard = fields.Boolean(string='Check', store=True, copied=True, tracking=0)
    line_with_comodin = fields.Boolean(string='Línea con comodín', store=True, copied=True, tracking=0)
    programation_name = fields.Char(string='Nombre de la programación', store=True, readonly=True, tracking=0)
    puesto_corto = fields.Char(string='Puesto Corto', store=True, tracking=1)
    relevante = fields.Boolean(string='R', store=True, copied=True, tracking=0)
    sede = fields.Char(string='Sede', store=True, tracking=1)
    seq_index = fields.Integer(string='Índice de secuencia', store=True, copied=True, tracking=0)
    use_parent_modality = fields.Boolean(string='Usa modalidad padre', readonly=True, tracking=0)
    vencimiento_contracto = fields.Date(string='Vencimiento Contrato', readonly=True, tracking=0)
    year = fields.Integer(string='Año', store=True, readonly=True, tracking=0)


class HrRosterPuesto(models.Model):
    _name = 'hr.roster.puesto'
    _description = 'Puestos de programación de turnos'

    aplica_adicional_nocturno_dom_fes = fields.Boolean(string='Aplica adicional nocturno dominical festivo',
                                                       readonly=True, tracking=0)
    code = fields.Char(string='Código', store=True, copied=True, tracking=0)
    concat_name = fields.Char(string='Info Puesto', store=True, readonly=True, tracking=0)
    devengado = fields.Float(string='Devengado', store=True, copied=True, tracking=0)
    direccion = fields.Char(string='Dirección', store=True, copied=True, tracking=0)
    fecha_inst = fields.Datetime(string='Fecha de instalación', store=True, copied=True, tracking=0)
    heyrec = fields.Float(string='HEYREC', store=True, copied=True, tracking=0)
    induction_days = fields.Integer(string='Días Inducción', store=True, copied=True, tracking=0)
    int_code = fields.Char(string='Código interno del cliente', store=True, copied=True, tracking=0)
    int_zone = fields.Char(string='Código zona del cliente', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, readonly=True, tracking=0)
    sede = fields.Char(string='Sede', store=True, tracking=1)
    valor_mensual_horas = fields.Float(string='Valor mensual de horas', store=True, copied=True, tracking=0)


class HrRosterPuestoBono(models.Model):
    _name = 'hr.roster.puesto.bono'
    _description = 'Bonos de puestos de programación de turnos'

    name = fields.Char(string='Descripción', store=True, copied=True, tracking=0)
    value = fields.Float(string='Valor', store=True, copied=True, tracking=0)


class HrRosterPuestoItemsCliente(models.Model):
    _name = 'hr.roster.puesto.items.cliente'
    _description = 'Ítems de clientes de puestos de programación de turnos'

    name = fields.Char(string='Descripción', store=True, copied=True, tracking=0)
    observaciones = fields.Char(string='Observaciones', store=True, copied=True, tracking=0)


class HrRosterPuestoTarifaAdicional(models.Model):
    _name = 'hr.roster.puesto.tarifa.adicional'
    _description = 'Tarifas adicionales de puestos de programación de turnos'

    end_date = fields.Date(string='Fin', store=True, required=True, copied=True, tracking=0)
    rate_add_df = fields.Float(string='Tarifa Turno Adicional Diurno Dominical y Festivo', store=True, copied=True,
                               tracking=0)
    rate_add_noc = fields.Float(string='Tarifa Turno Adicional Nocturno', store=True, copied=True, tracking=0)
    rate_add_ord = fields.Float(string='Tarifa Turno Adicional Diurno Ordinario', store=True, copied=True, tracking=0)
    rate_adn_df = fields.Float(string='Tarifa Turno Adicional Nocturno Dominical y Festivo', store=True, copied=True,
                               tracking=0)
    start_date = fields.Date(string='Inicio', store=True, required=True, copied=True, tracking=0)


class HrRosterRest(models.Model):
    _name = 'hr.roster.rest'
    _description = 'Descansos de programación de turnos'

    days = fields.Integer(string='Días Descanso', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', readonly=True, required=True, tracking=0)


class HrRosterReverseClose(models.Model):
    _name = 'hr.roster.reverse.close'
    _description = 'Reversión de cierre de programación de turnos'

    reverse_tarifario = fields.Boolean(string='Revertir Tarifarios?', store=True, copied=True, tracking=0)
    revertir_solo_adicionales = fields.Boolean(string='Revertir solo adicionales?', store=True, copied=True, tracking=0)


class HrRosterSaleConcept(models.Model):
    _name = 'hr.roster.sale.concept'
    _description = 'Conceptos de venta de programación de turnos'

    name = fields.Char(string='Concepto', store=True, required=True, copied=True, tracking=0)


class HrRosterSaleDistribution(models.Model):
    _name = 'hr.roster.sale.distribution'
    _description = 'Distribución de ventas de programación de turnos'

    distribution = fields.Float(string='Distribución', store=True, required=True, copied=True, tracking=0)


class HrRosterSchedulingLine(models.Model):
    _name = 'hr.roster.scheduling.line'
    _description = 'Líneas de programación de turnos'

    desfase = fields.Integer(string='Índice de inicio', store=True, copied=True, tracking=0)
    group_index = fields.Integer(string='Índice de grupo', store=True, copied=True, tracking=0)
    index = fields.Integer(string='Índice', store=True, copied=True, tracking=0)
    relevante = fields.Boolean(string='Relevante', store=True, copied=True, tracking=0)
    sequence_ids = fields.Char(string='Sequence', store=True, copied=True, tracking=0)
    use_relevante = fields.Boolean(string='Relevante', readonly=True, tracking=0)


class HrRosterSequence(models.Model):
    _name = 'hr.roster.sequence'
    _description = 'Secuencias de programación de turnos'

    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)


class HrRosterTarifario(models.Model):
    _name = 'hr.roster.tarifario'
    _description = 'Tarifarios de programación de turnos'

    fecha_aprobacion = fields.Date(string='Fecha de aprobación', store=True, copied=True, tracking=0)
    from_close = fields.Boolean(string='Creado desde Cierre', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', readonly=True, tracking=0)
    valor_total = fields.Float(string='Valor Total', readonly=True, tracking=0)


class HrRosterTarifarioLine(models.Model):
    _name = 'hr.roster.tarifario.line'
    _description = 'Líneas de tarifarios de programación de turnos'

    start_date = fields.Date(string='Fecha', store=True, required=True, copied=True, tracking=0)
    valor = fields.Float(string='Valor', store=True, copied=True, tracking=0)


class HrRosterTimesheet(models.Model):
    _name = 'hr.roster.timesheet'
    _description = 'Hojas de tiempo de programación de turnos'

    close_date = fields.Date(string='Fecha de cierre', store=True, copied=True, tracking=0)
    hours = fields.Float(string='Horas', store=True, copied=True, tracking=0)
    name = fields.Char(string='Descripción', store=True, copied=True, tracking=0)
    value = fields.Float(string='Valor', store=True, copied=True, tracking=0)


class HrRosterTipoTurno(models.Model):
    _name = 'hr.roster.tipo.turno'
    _description = 'Tipos de turnos de programación'

    codigo = fields.Char(string='Código', store=True, required=True, copied=True, tracking=0)
    duration = fields.Integer(string='Duración horas', readonly=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    time_break = fields.Char(string='Descanso', store=True, copied=True, tracking=0)
    time_in = fields.Char(string='Entrada', store=True, required=True, copied=True, tracking=0)
    time_out = fields.Char(string='Salida', store=True, required=True, copied=True, tracking=0)


class HrRosterTurno(models.Model):
    _name = 'hr.roster.turno'
    _description = 'Turnos de programación'

    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    additional_per_hour = fields.Boolean(string='Turno adicional (Por horas)', store=True, copied=True, tracking=0)
    adicional_nom = fields.Boolean(string='Turno adicional (NOM)', store=True, copied=True, tracking=0)
    adicional = fields.Boolean(string='Servicio adicional (FAC)', store=True, copied=True, tracking=0)
    categoria_turno = fields.Char(string='Estado', store=True, tracking=0)
    close_from_solo_adicionales = fields.Boolean(string='Cerrado desde solo adicionales', store=True, copied=True,
                                                 tracking=0)
    date_from = fields.Datetime(string='Desde', store=True, copied=True, tracking=0)
    date_to = fields.Datetime(string='Hasta', store=True, copied=True, tracking=0)
    descanso = fields.Boolean(string='Descanso', store=True, copied=True, tracking=0)
    dummy = fields.Boolean(string='Dummy', store=True, copied=True, tracking=0)
    estado_cierre = fields.Boolean(string='Estado cierre', store=True, readonly=True, copied=True, tracking=0)
    estado_tarifario = fields.Boolean(string='Estado tarifario', store=True, readonly=True, copied=True, tracking=0)
    extended = fields.Boolean(string='Extendido', store=True, copied=True, tracking=0)
    extra_hour = fields.Boolean(string='Hora Extra', store=True, copied=True, tracking=0)
    fecha_cierre = fields.Date(string='Fecha de cierre', store=True, readonly=True, copied=True, tracking=0)
    induction = fields.Boolean(string='Inducción', store=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Código', store=True, readonly=True, tracking=0)
    partial_replace = fields.Boolean(string='Reemplazo parcial', store=True, copied=True, tracking=0)
    st_control = fields.Boolean(string='Control de estados', store=True, copied=True, tracking=0)
    use_parent_modality = fields.Boolean(string='Usa modalidad padre', readonly=True, tracking=0)


class HrTarifario(models.Model):
    _name = 'hr.tarifario'
    _description = 'Tarifarios de RRHH'

    name = fields.Char(string='Nombre', readonly=True, tracking=0)
    valor = fields.Float(string='Valor', store=True, required=True, copied=True, tracking=0)


class HrUpdateBookVacation(models.Model):
    _name = 'hr.update.book.vacation'
    _description = 'Actualización de libro de vacaciones'

    date = fields.Date(string='Fecha', store=True, copied=True, tracking=0)


class HrVacationDiferential(models.Model):
    _name = 'hr.vacation.diferential'
    _description = 'Diferenciales de vacaciones'

    days = fields.Integer(string='Días', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', readonly=True, tracking=0)


class HrWizardMassiveRetired(models.Model):
    _name = 'hr.wizard.massive.retired'
    _description = 'Asistente masivo de jubilados'

    date_end = fields.Date(string='Fecha de Finalización', store=True, required=True, copied=True, tracking=0)
    settlement_date = fields.Date(string='Fecha de liquidación', store=True, required=True, copied=True, tracking=0)


class HrWorkOccupation(models.Model):
    _name = 'hr.work.occupation'
    _description = 'Ocupaciones laborales'

    name = fields.Char(string='Ocupación', store=True, copied=True, tracking=0)


class Imei(models.Model):
    _name = 'imei'
    _description = 'IMEI'

    activity_date_deadline = fields.Date(string='Siguiente plazo de actividad', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Resumen de la siguiente actividad', tracking=0)
    activity_type_icon = fields.Char(string='Ícono de tipo de actividad', readonly=True, tracking=0)
    imei1 = fields.Char(string='Imei 1', store=True, copied=True, tracking=0)
    imei2 = fields.Char(string='Imei 2', store=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Nº de archivos adjuntos', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Número de errores', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Error de Envío de Mensaje', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='Error de entrega del SMS', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Es un seguidor', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Acción requerida', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Nº de mensajes sin leer', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Mensajes sin leer', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='Mi fecha límite de actividad', readonly=True, tracking=0)
    serie = fields.Char(string='Serie', store=True, copied=True, tracking=0)


class Imeis(models.Model):
    _name = 'imeis'
    _description = 'IMEIs'

    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    conexion_remoto_num = fields.Char(string='Conexión Remoto', store=True, copied=True, tracking=1)
    conexion_remoto_pass = fields.Char(string='Contraseña Remoto', store=True, copied=True, tracking=1)
    current = fields.Integer(string='Valor Actual', store=True, copied=True, tracking=1)
    email_cell = fields.Char(string='Correo Equipo', store=True, copied=True, tracking=1)
    fecha_compra_dispositivo = fields.Date(string='Fecha De Compra', store=True, copied=True, tracking=1)
    imei1 = fields.Char(string='Imei 1', store=True, tracking=0)
    imei2 = fields.Char(string='Imei 2', store=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Name', store=True, tracking=0)
    numero_serie = fields.Char(string='Serie', store=True, copied=True, tracking=0)
    valor_compra_dispositivo = fields.Integer(string='Valor De Compra Dispositivo', store=True, copied=True, tracking=1)
    vida_util = fields.Integer(string='Vida Útil', store=True, copied=True, tracking=1)


class ImportExcelWizard(models.Model):
    _name = 'import.excel.wizard'
    _description = 'Asistente de importación de Excel'

    file = fields.Text(string='Archivo XLSX', store=True, required=True, copied=True, tracking=0)


class IncomeRecords(models.Model):
    _name = 'income.records'
    _description = 'Registros de ingresos'

    actual_date = fields.Date(string='Fecha:', store=True, copied=True, tracking=0)
    date_from = fields.Date(string='Date From', store=True, copied=True, tracking=0)
    date_to = fields.Date(string='Date To', store=True, copied=True, tracking=0)
    time = fields.Float(string='Registro Hora', store=True, copied=True, tracking=0)


class IncomeRecordsLine(models.Model):
    _name = 'income.records.line'
    _description = 'Líneas de registros de ingresos'

    date_scheduled = fields.Datetime(string='Fecha Prevista', store=True, copied=True, tracking=0)
    horario = fields.Char(string='Horario', store=True, copied=True, tracking=0)
    ot_number = fields.Char(string='Número OT', store=True, copied=True, tracking=0)
    part = fields.Char(string='Parte', store=True, copied=True, tracking=0)
    time_dif = fields.Float(string='Diferencia', readonly=True, tracking=0)
    time = fields.Float(string='Registro Hora', store=True, copied=True, tracking=0)


class InstitucionesEstudiosCapacitaciones(models.Model):
    _name = 'instituciones.estudios.capacitaciones'
    _description = 'Instituciones de estudios y capacitaciones'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    nit = fields.Char(string='NIT', store=True, copied=True, tracking=0)


class IrActionsAccountReportDownload(models.Model):
    _name = 'ir.actions.account.report.download'
    _description = 'Descarga de reportes contables'

    binding_view_types = fields.Char(string='Binding View Types', store=True, copied=True, tracking=0)
    help = fields.Html(string='Action Description', store=True, copied=True, tracking=0)
    name = fields.Char(string='Name', store=True, required=True, copied=True, tracking=0)
    type = fields.Char(string='Action Type', store=True, required=True, copied=True, tracking=0)
    xml_id = fields.Char(string='External ID', readonly=True, tracking=0)


class IrActionsActUrl(models.Model):
    _name = 'ir.actions.act.url'
    _description = 'Acciones de URL'

    binding_view_types = fields.Char(string='Tipos de vista de enlace', store=True, copied=True, tracking=0)
    help = fields.Html(string='Descripción de la acción', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre de acción', store=True, required=True, copied=True, tracking=0)
    type = fields.Char(string='Tipo de acción', store=True, required=True, copied=True, tracking=0)
    url = fields.Text(string='URL de la acción', store=True, required=True, copied=True, tracking=0)
    xml_id = fields.Char(string='ID externo', readonly=True, tracking=0)


class IrActionsActWindow(models.Model):
    _name = 'ir.actions.act.window'
    _description = 'Acciones de ventana'

    binding_view_types = fields.Char(string='Tipos de vista de enlace', store=True, copied=True, tracking=0)
    context = fields.Char(string='Valor de contexto', store=True, required=True, copied=True, tracking=0)
    domain = fields.Char(string='Valor del dominio', store=True, copied=True, tracking=0)
    filter = fields.Boolean(string='Filtro', store=True, copied=True, tracking=0)
    help = fields.Html(string='Descripción de la acción', store=True, copied=True, tracking=0)
    limit = fields.Integer(string='Límite', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre de acción', store=True, required=True, copied=True, tracking=0)
    res_id = fields.Integer(string='ID de registro', store=True, copied=True, tracking=0)
    res_model = fields.Char(string='Modelo destino', store=True, required=True, copied=True, tracking=0)
    search_view = fields.Text(string='Vista de búsqueda', readonly=True, tracking=0)
    type = fields.Char(string='Tipo de acción', store=True, required=True, copied=True, tracking=0)
    usage = fields.Char(string='Uso de la acción', store=True, copied=True, tracking=0)
    view_mode = fields.Char(string='Modo de vista', store=True, required=True, copied=True, tracking=0)
    views = fields.Text(string='Vistas', readonly=True, tracking=0)
    xml_id = fields.Char(string='ID externo', readonly=True, tracking=0)


class IrActionsActWindowClose(models.Model):
    _name = 'ir.actions.act.window.close'
    _description = 'Cierre de acciones de ventana'

    binding_view_types = fields.Char(string='Tipos de vista de enlace', store=True, copied=True, tracking=0)
    help = fields.Html(string='Descripción de la acción', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    type = fields.Char(string='Tipo de acción', store=True, required=True, copied=True, tracking=0)
    xml_id = fields.Char(string='ID externo', readonly=True, tracking=0)


class IrActionsActWindowView(models.Model):
    _name = 'ir.actions.act.window.view'
    _description = 'Vistas de acciones de ventana'

    multi = fields.Boolean(string='En múltiples doc.', store=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)


class IrActionsCenter(models.Model):
    _name = 'ir.actions.center'
    _description = 'Centro de acciones'

    name = fields.Char(string='Name', store=True, copied=True, tracking=0)
    views_order = fields.Char(string='Views Order', store=True, copied=True, tracking=0)


class IrConfigParameter(models.Model):
    _name = 'ir.config.parameter'
    _description = 'Parámetros de configuración'

    google_sheets_credentials = fields.Text(string='Credenciales Google Sheets', store=True, copied=True, tracking=1)
    key = fields.Char(string='Clave', index=True, store=True, required=True, copied=True, tracking=0)
    value = fields.Text(string='Valor', store=True, required=True, copied=True, tracking=0)


class IrDemoFailure(models.Model):
    _name = 'ir.demo.failure'
    _description = 'Fallos de demostración'

    error = fields.Char(string='Error', store=True, copied=True, tracking=0)


class IrDemoFailureWizard(models.Model):
    _name = 'ir.demo.failure.wizard'
    _description = 'Asistente de fallos de demostración'

    failures_count = fields.Integer(string='Nº de fallos', readonly=True, tracking=0)


class IrMailServer(models.Model):
    _name = 'ir.mail.server'
    _description = 'Servidores de correo'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0)
    google_gmail_access_token_expiration = fields.Integer(string='Access Token Expiration Timestamp', store=True,
                                                          tracking=0)
    google_gmail_access_token = fields.Char(string='Access Token', store=True, tracking=0)
    google_gmail_authorization_code = fields.Char(string='Authorization Code', store=True, tracking=0)
    google_gmail_refresh_token = fields.Char(string='Refresh Token', store=True, tracking=0)
    google_gmail_uri = fields.Char(string='URI', readonly=True, tracking=0)
    name = fields.Char(string='Descripción', index=True, store=True, required=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Prioridad', store=True, copied=True, tracking=0)
    smtp_debug = fields.Boolean(string='Depurando', store=True, copied=True, tracking=0)
    smtp_host = fields.Char(string='Servidor SMTP', store=True, required=True, copied=True, tracking=0)
    smtp_pass = fields.Char(string='Contraseña', store=True, copied=True, tracking=0)
    smtp_port = fields.Integer(string='Puerto SMTP', store=True, required=True, copied=True, tracking=0)
    smtp_user = fields.Char(string='Nombre de usuario', store=True, copied=True, tracking=0)
    use_google_gmail_service = fields.Boolean(string='Gmail Authentication', store=True, copied=True, tracking=0)


class JournalEntryImportFast(models.Model):
    _name = 'journal.entry.import.fast'
    _description = 'Importación rápida de asientos contables'

    file = fields.Text(string='File', store=True, copied=True, tracking=0)
    force_validate = fields.Boolean(string='Forzar validación', store=True, copied=True, tracking=0)


class JournalLedgerReportWizard(models.Model):
    _name = 'journal.ledger.report.wizard'
    _description = 'Asistente de reporte de libro mayor'

    date_from = fields.Date(string='Fecha de inicio', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha final', store=True, required=True, copied=True, tracking=0)
    foreign_currency = fields.Boolean(string='Moneda Extranjera', store=True, copied=True, tracking=0)
    with_account_name = fields.Boolean(string='Cuenta con Nombre', store=True, copied=True, tracking=0)
    with_auto_sequence = fields.Boolean(string='Show Auto Sequence', store=True, copied=True, tracking=0)


class Kactus(models.Model):
    _name = 'kactus'
    _description = 'Kactus'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    calcula = fields.Char(string='Calcula', store=True, copied=True, tracking=1)
    fecha_desde = fields.Datetime(string='Desde', store=True, copied=True, tracking=1)
    fecha_hasta = fields.Datetime(string='Hasta', store=True, copied=True, tracking=1)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Solicitud', store=True, copied=True, tracking=1)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=1)


class KactusBiEmple(models.Model):
    _name = 'kactus.bi.emple'
    _description = 'Biografía de empleados en Kactus'

    ape_empl = fields.Char(string='Apellidos', store=True, copied=True, tracking=1)
    bar_resi = fields.Char(string='Barrio de residencia', store=True, copied=True, tracking=1)
    bomail = fields.Char(string='Email', store=True, copied=True, tracking=1)
    cla_lmil = fields.Char(string='Clase libreta militar', store=True, copied=True, tracking=1)
    cod_empl = fields.Char(string='Número de documento', store=True, copied=True, tracking=1)
    cod_inte = fields.Char(string='Número de documento', store=True, copied=True, tracking=1)
    dir_resi = fields.Char(string='Dirección de residencia', store=True, copied=True, tracking=1)
    dis_lmil = fields.Char(string='Distrito libreta militar', store=True, copied=True, tracking=1)
    dto_expe = fields.Char(string='Departamento de expedición', store=True, copied=True, tracking=1)
    dto_naci = fields.Char(string='Departamento de nacimiento', store=True, copied=True, tracking=1)
    dto_resi = fields.Char(string='Departamento de residencia', store=True, copied=True, tracking=1)
    eee_mail = fields.Char(string='Email', store=True, copied=True, tracking=1)
    est_civi = fields.Char(string='Estado civil', store=True, copied=True, tracking=1)
    fec_naci = fields.Char(string='Fecha de nacimiento', store=True, copied=True, tracking=1)
    for_acad = fields.Char(string='Formación académica', store=True, copied=True, tracking=1)
    gra_educ = fields.Char(string='Grado de educación Bachiller', store=True, copied=True, tracking=1)
    loc_naci = fields.Char(string='Localidad de nacimiento', store=True, copied=True, tracking=1)
    loc_resi = fields.Char(string='Localidad de residencia', store=True, copied=True, tracking=1)
    mpi_expe = fields.Char(string='Municipio de expedición', store=True, copied=True, tracking=1)
    mpi_naci = fields.Char(string='Municipio de nacimiento', store=True, copied=True, tracking=1)
    mpi_resi = fields.Char(string='Municipio de residencia', store=True, copied=True, tracking=1)
    nac_iona = fields.Char(string='Nacionalidad', store=True, copied=True, tracking=1)
    name = fields.Char(string='Bi.emple', store=True, copied=True, tracking=1)
    nom_empl = fields.Char(string='Nombres', store=True, copied=True, tracking=1)
    num_lmil = fields.Char(string='Número libreta militar', store=True, copied=True, tracking=1)
    pai_expe = fields.Char(string='País de expedición', store=True, copied=True, tracking=1)
    pai_extr = fields.Char(string='País Extranjero', store=True, copied=True, tracking=1)
    pai_naci = fields.Char(string='País de nacimiento', store=True, copied=True, tracking=1)
    pai_resi = fields.Char(string='País de residencia', store=True, copied=True, tracking=1)
    per_carg = fields.Char(string='Personas a cargo', store=True, copied=True, tracking=1)
    pro_titu = fields.Char(string='Título profesional', store=True, copied=True, tracking=1)
    rel_empl = fields.Char(string='Número de documento', store=True, copied=True, tracking=1)
    seempl = fields.Char(string='Género', store=True, copied=True, tracking=1)
    tel_movi = fields.Char(string='Teléfono móvil', store=True, copied=True, tracking=1)
    tel_resi = fields.Char(string='Teléfono residencia', store=True, copied=True, tracking=1)
    tip_docu = fields.Char(string='Tipo documento', store=True, copied=True, tracking=1)
    tit_obte = fields.Char(string='Título Obtenido', store=True, copied=True, tracking=1)


class KactusNmContr(models.Model):
    _name = 'kactus.nm.contr'
    _description = 'Contratos en Kactus'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    cod_area = fields.Char(string='Área de riesgo', store=True, copied=True, tracking=1)
    cod_carg = fields.Char(string='Código de cargo', store=True, copied=True, tracking=1)
    cod_ccos = fields.Char(string='Centro de costo', store=True, copied=True, tracking=1)
    cod_cenp = fields.Char(string='Nivel de riesgo arl', store=True, copied=True, tracking=1)
    cod_empl = fields.Char(string='Número de documento', store=True, copied=True, tracking=1)
    cod_frep = fields.Char(string='Número de documento jefe inmediato', store=True, copied=True, tracking=1)
    cod_gpro = fields.Char(string='Grupo de prototipo', store=True, copied=True, tracking=1)
    cod_niv1 = fields.Char(string='Sucursal', store=True, copied=True, tracking=1)
    cod_tnom = fields.Char(string='Clase de nómina', store=True, copied=True, tracking=1)
    dia_conf = fields.Char(string='Cantidad de días contrato', store=True, copied=True, tracking=1)
    fec_anti = fields.Char(string='Fecha inicio del contrato', store=True, copied=True, tracking=1)
    fec_cesa = fields.Char(string='Fecha inicio del contrato', store=True, copied=True, tracking=1)
    fec_cont = fields.Char(string='Fecha inicio del contrato', store=True, copied=True, tracking=1)
    fec_deja = fields.Char(string='Fecha inicio del contrato', store=True, copied=True, tracking=1)
    fec_ingr = fields.Char(string='Fecha inicio del contrato', store=True, copied=True, tracking=1)
    fec_nomb = fields.Char(string='Fecha inicio del contrato', store=True, copied=True, tracking=1)
    fec_nove = fields.Char(string='Fecha inicio del contrato', store=True, copied=True, tracking=1)
    fec_pose = fields.Char(string='Fecha inicio del contrato', store=True, copied=True, tracking=1)
    fec_suel = fields.Char(string='Fecha inicio del contrato', store=True, copied=True, tracking=1)
    fec_vaca = fields.Char(string='Fecha inicio del contrato', store=True, copied=True, tracking=1)
    fec_venc = fields.Char(string='Fecha vencimiento del contrato', store=True, copied=True, tracking=1)
    name = fields.Char(string='Nm.contr', store=True, copied=True, tracking=1)
    nro_cont = fields.Char(string='Número de contrato', store=True, copied=True, tracking=1)
    obs_erva = fields.Char(string='Fecha ingreso formato aaaammdd', store=True, copied=True, tracking=1)
    pen_tipo = fields.Char(string='Tipo cotizante / Pensión', store=True, copied=True, tracking=1)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=1)
    sue_basi = fields.Char(string='Sueldo básico', store=True, copied=True, tracking=1)
    tip_cnfj = fields.Char(string='Tipo de contrato', store=True, copied=True, tracking=1)
    tip_cont = fields.Char(string='Tipo de contrato', store=True, copied=True, tracking=1)
    tip_coti = fields.Char(string='Subtipo de cotizante', store=True, copied=True, tracking=1)
    tip_remu = fields.Char(string='Tipo de remuneración', store=True, copied=True, tracking=1)


class KactusNmCuent(models.Model):
    _name = 'kactus.nm.cuent'
    _description = 'Cuentas en Kactus'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    cla_cuen = fields.Char(string='Clase de cuenta', store=True, copied=True, tracking=1)
    cod_empl = fields.Char(string='Número de documento', store=True, copied=True, tracking=1)
    cod_enti = fields.Char(string='Código de entidad', store=True, copied=True, tracking=1)
    cod_sucu = fields.Char(string='Código sucursal', store=True, copied=True, tracking=1)
    fec_inic = fields.Char(string='Fecha inicio del contrato', store=True, copied=True, tracking=1)
    name = fields.Char(string='Kactus Nm.cuent', store=True, copied=True, tracking=1)
    nro_cont = fields.Char(string='Número de documento', store=True, copied=True, tracking=1)
    nro_cuen = fields.Char(string='Número de cuenta', store=True, copied=True, tracking=1)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=1)
    tip_enti = fields.Char(string='Tipo de entidad', store=True, copied=True, tracking=1)


class KactusNmDisrf(models.Model):
    _name = 'kactus.nm.disrf'
    _description = 'Discapacidades en Kactus'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    cod_empl = fields.Char(string='Número de documento', store=True, copied=True, tracking=1)
    fec_inic = fields.Char(string='Fecha inicio del contrato', store=True, copied=True, tracking=1)
    fec_vige = fields.Char(string='Fecha inicio del contrato', store=True, copied=True, tracking=1)
    name = fields.Char(string='Kactus Nm.disrf', store=True, copied=True, tracking=1)
    nro_cont = fields.Char(string='Número de contrato', store=True, copied=True, tracking=1)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=1)
    vig_salu = fields.Char(string='Fecha inicio del contrato', store=True, copied=True, tracking=1)


class L10NLatamIdentificationType(models.Model):
    _name = 'l10n_latam.identification.type'
    _description = 'Tipos de identificación en LATAM'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0)
    description = fields.Char(string='Descripción', store=True, copied=True, tracking=0)
    is_vat = fields.Boolean(string='Es Identificación Fiscal?', store=True, copied=True, tracking=0)
    l10n_co_document_code = fields.Char(string='Document Code', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)


class LineasCelular(models.Model):
    _name = 'lineas.celular'
    _description = 'Líneas celulares'

    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    costo = fields.Float(string='Valor Costo', store=True, copied=True, tracking=1)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Línea Celular', store=True, copied=True, tracking=1)
    validacion = fields.Boolean(string='Validación', store=True, copied=True, tracking=1)


class LoadDataEinvoice(models.Model):
    _name = 'load.data.einvoice'
    _description = 'Carga de datos de factura electrónica'

    e_invoice_xml = fields.Text(string='E-Invoice XML', store=True, tracking=0)


class LoanMoveLine(models.Model):
    _name = 'loan.move.line'
    _description = 'Líneas de movimientos de préstamos'

    bank_charges = fields.Float(string='Gastos bancarios', store=True, readonly=True, copied=True, tracking=0)
    capital_payment = fields.Float(string='Pago a capital', store=True, readonly=True, copied=True, tracking=0)
    core_adjust = fields.Float(string='Ajuste de cuotas', store=True, readonly=True, copied=True, tracking=0)
    cote = fields.Float(string='Cuota', readonly=True, tracking=0)
    date = fields.Date(string='Fecha', store=True, readonly=True, required=True, copied=True, tracking=0)
    final_bal = fields.Float(string='Saldo final', readonly=True, tracking=0)
    initial_value = fields.Float(string='Saldo inicial', store=True, readonly=True, copied=True, tracking=0)
    interest = fields.Float(string='Intereses corrientes', store=True, readonly=True, copied=True, tracking=0)
    move_name = fields.Char(string='Nombre Comprobante', store=True, readonly=True, copied=True, tracking=0)


class OperacionesEstado(models.Model):
    _name = 'operaciones.estado'
    _description = 'Estados de operaciones'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    description = fields.Text(string='Descripción', store=True, copied=True, tracking=1)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=1)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=1)

class OperadorLinea(models.Model):
    _name = 'operador.linea'
    _description = 'Líneas de operadores'

    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Name', store=True, copied=True, tracking=0)

class OrderLineDetail(models.Model):
    _name = 'order.line.detail'
    _description = 'Detalles de líneas de órdenes'

    dummy_days = fields.Char(string='Días calendario', store=True, copied=True, tracking=0)
    hd_exe = fields.Float(string='Horas diurnas prestadas', store=True, copied=True, tracking=0)
    hd = fields.Float(string='Horas diurnas', store=True, copied=True, tracking=0)
    hn_exe = fields.Float(string='Horas nocturnas prestadas', store=True, copied=True, tracking=0)
    hn = fields.Float(string='Horas nocturnas', store=True, copied=True, tracking=0)
    prefestivo = fields.Boolean(string='Prefestivo', store=True, copied=True, tracking=0)
    repetition = fields.Integer(string='Repeticiones', store=True, copied=True, tracking=0)
    rest_in = fields.Char(string='Salida a descanso', store=True, copied=True, tracking=0)
    rest_out = fields.Char(string='Entrada de descanso', store=True, copied=True, tracking=0)
    time_in = fields.Char(string='Hora de entrada', store=True, copied=True, tracking=0)
    time_out = fields.Char(string='Hora de salida', store=True, copied=True, tracking=0)

class OrderQuoterLineDetail(models.Model):
    _name = 'order.quoter.line.detail'
    _description = 'Detalles de líneas de cotizaciones'

    dummy_days = fields.Char(string='Días calendario', store=True, copied=True, tracking=0)
    hd_exe = fields.Float(string='Horas diurnas prestadas', store=True, copied=True, tracking=0)
    hd = fields.Float(string='Horas diurnas', store=True, copied=True, tracking=0)
    hn_exe = fields.Float(string='Horas nocturnas prestadas', store=True, copied=True, tracking=0)
    hn = fields.Float(string='Horas nocturnas', store=True, copied=True, tracking=0)
    prefestivo = fields.Boolean(string='Prefestivo', store=True, copied=True, tracking=0)
    repetition = fields.Integer(string='Repeticiones', store=True, copied=True, tracking=0)
    rest_in = fields.Char(string='Salida a descanso', store=True, copied=True, tracking=0)
    rest_out = fields.Char(string='Entrada de descanso', store=True, copied=True, tracking=0)
    time_in = fields.Char(string='Hora de entrada', store=True, copied=True, tracking=0)
    time_out = fields.Char(string='Hora de salida', store=True, copied=True, tracking=0)

class OvertimeJustification(models.Model):
    _name = 'overtime.justification'
    _description = 'Justificaciones de horas extras'

    name = fields.Char(string='Description', store=True, copied=True, tracking=0)

class PayslipAnalyticDistribution(models.Model):
    _name = 'payslip.analytic.distribution'
    _description = 'Distribución analítica de nóminas'

    rate = fields.Float(string='Distribución', store=True, copied=True, tracking=0)

class PayslipPeriod(models.Model):
    _name = 'payslip.period'
    _description = 'Períodos de nóminas'

    closed = fields.Boolean(string='Cerrado', store=True, copied=True, tracking=0)
    end_date = fields.Date(string='Fin de Corte', store=True, required=True, copied=True, tracking=0)
    end_period = fields.Date(string='Fin del Periodo', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    start_date = fields.Date(string='Comienzo de Corte', store=True, required=True, copied=True, tracking=0)
    start_period = fields.Date(string='Comienzo del Periodo', store=True, required=True, copied=True, tracking=0)

class Pdforientation(models.Model):
    _name = 'pdf.orientation'
    _description = 'Orientación de PDF'

    query_name = fields.Text(string='Query', store=True, copied=True, tracking=0)

class PensionUpdateHistory(models.Model):
    _name = 'pension.update.history'
    _description = 'Historial de actualización de pensiones'

    date = fields.Date(string='Fecha', store=True, required=True, copied=True, tracking=0)

class PermisoEspecialTipo(models.Model):
    _name = 'permiso.especial.tipo'
    _description = 'Tipos de permisos especiales'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)

class PlanesDeCelular(models.Model):
    _name = 'planes.de.celular'
    _description = 'Planes de celular'

    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    costo = fields.Float(string='Valor Costo', store=True, copied=True, tracking=1)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Nombre Plan', store=True, copied=True, tracking=0)

class PrefacturacionWiz(models.Model):
    _name = 'prefacturacion.wiz'
    _description = 'Asistente de prefacturación'

    distribuited = fields.Boolean(string='Con Distribución', store=True, copied=True, tracking=0)
    end_date = fields.Date(string='Hasta', store=True, copied=True, tracking=0)
    invoice_date = fields.Date(string='Fecha de factura', store=True, copied=True, tracking=0)
    start_date = fields.Date(string='Fecha inicio', store=True, copied=True, tracking=0)

class PrefacturacionWizDirect(models.Model):
    _name = 'prefacturacion.wiz.direct'
    _description = 'Asistente directo de prefacturación'

    distribuited = fields.Boolean(string='Con Distribución', store=True, copied=True, tracking=0)
    end_date = fields.Date(string='Hasta', store=True, copied=True, tracking=0)
    invoice_date = fields.Date(string='Fecha de factura', store=True, copied=True, tracking=0)
    start_date = fields.Date(string='Fecha inicio', store=True, copied=True, tracking=0)

class PrintCertificadoRetencion(models.Model):
    _name = 'print.certificado.retencion'
    _description = 'Certificados de retención'

    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    amount_total_text = fields.Char(string='amount.text', readonly=True, tracking=0)
    amount_total = fields.Float(string='amount', readonly=True, tracking=0)
    date_expedition = fields.Date(string='Fecha de Expedición', store=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)

class PrintCertificadoRetencionLine(models.Model):
    _name = 'print.certificado.retencion.line'
    _description = 'Líneas de certificados de retención'

    base_amount = fields.Float(string='Base', store=True, readonly=True, copied=True, tracking=0)
    count = fields.Integer(string='Movimientos', store=True, readonly=True, copied=True, tracking=0)
    invoice_ids = fields.Char(string='Facturas', store=True, readonly=True, copied=True, tracking=0)
    name = fields.Char(string='Name', store=True, readonly=True, copied=True, tracking=0)
    note = fields.Char(string='Descripción', store=True, readonly=True, copied=True, tracking=0)
    porcentaje = fields.Float(string='Porcentaje', store=True, readonly=True, copied=True, tracking=0)
    taamount_parent = fields.Float(string='Base Padre', store=True, readonly=True, copied=True, tracking=0)
    taamount = fields.Float(string='Retenido', store=True, readonly=True, copied=True, tracking=0)

class ProcesosDisciplinarios(models.Model):
    _name = 'procesos.disciplinarios'
    _description = 'Procesos disciplinarios'

    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    cargo = fields.Char(string='Cargo', store=True, readonly=True, tracking=0)
    descripcion_falta = fields.Text(string='Descripción de la Falta', store=True, required=True, copied=True, tracking=0)
    estado_procede = fields.Boolean(string='Estado Procede', store=True, copied=True, tracking=0)
    estado_suspendido = fields.Boolean(string='Estado Suspendido', store=True, copied=True, tracking=0)
    fecha_falta = fields.Date(string='Fecha de la Falta Cometida', store=True, required=True, copied=True, tracking=0)
    fecha_hasta_sancion = fields.Date(string='Fecha Hasta de la Sanción', store=True, copied=True, tracking=0)
    fecha_informe = fields.Date(string='Fecha de Realización del Informe', store=True, required=True, copied=True, tracking=0)
    fecha_reinicio_laboral = fields.Date(string='Fecha de Reinicio de Labores', store=True, copied=True, tracking=0)
    fecha_sancion = fields.Date(string='Fecha de Sanción', store=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    numero_identificacion = fields.Char(string='Número de Identificación', store=True, required=True, copied=True, tracking=0)
    observaciones = fields.Text(string='Observaciones', store=True, copied=True, tracking=0)
    otro_tipo_motivo = fields.Char(string='Otro Tipo de Motivo', store=True, copied=True, tracking=0)
    otro_tipo_sancion = fields.Char(string='Otro Tipo de Sanción', store=True, copied=True, tracking=0)
    reentrenamiento = fields.Boolean(string='Reentrenamiento', store=True, copied=True, tracking=0)
    subzona = fields.Char(string='Subzona', store=True, readonly=True, tracking=0)
    tipo_motivo_nombre = fields.Char(string='Nombre Tipo Motivo', store=True, readonly=True, tracking=0)
    tipo_sancion_nombre = fields.Char(string='Nombre Tipo Sanción', store=True, readonly=True, tracking=0)
    zona = fields.Char(string='Zona', store=True, readonly=True, tracking=0)

class ProductAttributeValue(models.Model):
    _inherit = 'product.attribute.value'
    descripcion_variante = fields.Text(string='Descripción de la Variante', store=True, copied=True, tracking=1)
    marca_variante = fields.Text(string='Marca de la Variante', store=True, copied=True, tracking=1)

class ProductBrand(models.Model):
    _name = 'product.brand'
    _description = 'Marcas de productos'

    description = fields.Text(string='Descripción', store=True, copied=True, tracking=0)
    logo = fields.Text(string='Logotipo', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre de la marca', store=True, required=True, copied=True, tracking=0)
    products_count = fields.Integer(string='Número de productos', readonly=True, tracking=0)

class ProductCategory(models.Model):
    _inherit = 'product.category'
    code = fields.Char(string='Código', store=True, copied=True, tracking=0)

class ProductMargin(models.Model):
    _name = 'product.margin'
    _description = 'Márgenes de productos'

    from_date = fields.Date(string='Desde', store=True, copied=True, tracking=0)
    to_date = fields.Date(string='A', store=True, copied=True, tracking=0)

class ProductPackaging(models.Model):
    _inherit = 'product.packaging'
    height = fields.Integer(string='Altura', store=True, copied=True, tracking=0)
    length_uom_name = fields.Char(string='Etiqueta de la medida de largo', readonly=True, tracking=0)
    maweight = fields.Float(string='Peso máximo', store=True, copied=True, tracking=0)
    packaging_length = fields.Integer(string='Longitud', store=True, copied=True, tracking=0)
    shipper_package_code = fields.Char(string='Código del paquete', store=True, copied=True, tracking=0)
    weight_uom_name = fields.Char(string='Etiqueta de unidad de medida de peso', readonly=True, tracking=0)
    width = fields.Integer(string='Ancho', store=True, copied=True, tracking=0)

class ProductPricelistItem(models.Model):
    _inherit = 'product.pricelist.item'
    price_mamargin = fields.Float(string='Margen precio má', store=True, copied=True, tracking=0)

class ProductProduct(models.Model):
    _inherit = 'product.product'
    alert_time = fields.Integer(string='Hora de alerta', copied=True, tracking=0)
    campo_para_descripcion_juan = fields.Text(string='Descripción del Producto', store=True, readonly=True, tracking=1)
    date_from = fields.Date(string='Fecha Desde del Margen', readonly=True, tracking=0)
    date_to = fields.Date(string='Fecha Hasta del Margen', readonly=True, tracking=0)
    expected_margin_rate = fields.Float(string='Margen Previsto (%)', readonly=True, tracking=0)
    expected_margin = fields.Float(string='Margen Previsto', readonly=True, tracking=0)
    expiration_time = fields.Integer(string='Fecha de caducidad', copied=True, tracking=0)
    hs_code = fields.Char(string='Código HS', copied=True, tracking=0)
    is_peso = fields.Boolean(string='Ajuste al Peso', store=True, copied=True, tracking=0)
    landed_cost_ok = fields.Boolean(string='Es un coste en destino', copied=True, tracking=0)
    manufacturer_pname = fields.Char(string='Nombre de producto del fabricante', store=True, copied=True, tracking=0)
    manufacturer_pref = fields.Char(string='Código de producto del fabricante', store=True, copied=True, tracking=0)
    manufacturer_purl = fields.Char(string='URL de producto del fabricante', store=True, copied=True, tracking=0)
    margin_percentage = fields.Float(string='Porcentaje de Margen', copied=True, tracking=0)
    normal_cost = fields.Float(string='Coste Normal', readonly=True, tracking=0)
    purchase_avg_price = fields.Float(string='Precio Unidad Promedio de Compra', readonly=True, tracking=0)
    purchase_gap = fields.Float(string='Diferencia Compra', readonly=True, tracking=0)
    purchase_num_invoiced = fields.Float(string='# Facturado en Compras', readonly=True, tracking=0)
    reference_price = fields.Float(string='Precio de Referencia', copied=True, tracking=0)
    removal_time = fields.Integer(string='Tiempo de remoción', copied=True, tracking=0)
    reordering_maqty = fields.Float(string='Abasteciendo cant. má', readonly=True, tracking=0)
    sale_avg_price = fields.Float(string='Precio Unidad Promedio de Venta', readonly=True, tracking=0)
    sale_expected = fields.Float(string='Venta Prevista', readonly=True, tracking=0)
    sale_num_invoiced = fields.Float(string='Nº Facturado en Venta', readonly=True, tracking=0)
    sales_gap = fields.Float(string='Diferencia Ventas', readonly=True, tracking=0)
    surveillance_service = fields.Boolean(string='Servicio de vigilancia', store=True, copied=True, tracking=0)
    total_cost = fields.Float(string='Costo Total', readonly=True, tracking=0)
    total_margin_rate = fields.Float(string='Tasa de Margen Total (%)', readonly=True, tracking=0)
    total_margin = fields.Float(string='Margen Total', readonly=True, tracking=0)
    turnover = fields.Float(string='Volumen de negocio', readonly=True, tracking=0)
    use_expiration_date = fields.Boolean(string='Fecha de caducidad', copied=True, tracking=0)
    use_time = fields.Integer(string='Consumir preferentemente antes de', copied=True, tracking=0)

class ProductScheme(models.Model):
    _name = 'product.scheme'
    _description = 'Esquemas de productos'

    code = fields.Char(string='schemeID', store=True, copied=True, tracking=0)
    name = fields.Char(string='schemeName', store=True, copied=True, tracking=0)
    scheme_agency_id = fields.Char(string='schemeAgencyID', store=True, copied=True, tracking=0)

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    alert_time = fields.Integer(string='Hora de alerta', store=True, copied=True, tracking=0)
    expiration_time = fields.Integer(string='Fecha de caducidad', store=True, copied=True, tracking=0)
    hs_code = fields.Char(string='Código HS', store=True, copied=True, tracking=0)
    landed_cost_ok = fields.Boolean(string='Es un coste en destino', store=True, copied=True, tracking=0)
    manufacturer_pname = fields.Char(string='Nombre de producto del fabricante', store=True, tracking=0)
    manufacturer_pref = fields.Char(string='Código de producto del fabricante', store=True, tracking=0)
    manufacturer_purl = fields.Char(string='URL de producto del fabricante', store=True, tracking=0)
    margin_percentage = fields.Float(string='Porcentaje de Margen', store=True, copied=True, tracking=0)
    reference_price = fields.Float(string='Precio de Referencia', store=True, copied=True, tracking=0)
    removal_time = fields.Integer(string='Tiempo de remoción', store=True, copied=True, tracking=0)
    reordering_maqty = fields.Float(string='Abasteciendo cant. má', readonly=True, tracking=0)
    use_expiration_date = fields.Boolean(string='Fecha de caducidad', store=True, copied=True, tracking=0)
    use_time = fields.Integer(string='Consumir preferentemente antes de', store=True, copied=True, tracking=0)

class Programa(models.Model):
    _name = 'programa'
    _description = 'Programas'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)

class ProgramacionModalidadWiz(models.Model):
    _name = 'programacion.modalidad.wiz'
    _description = 'Asistente de modalidades de programación'

    use_parent_modality = fields.Boolean(string='Usa modalidad padre', readonly=True, tracking=0)

class ProgramationLineWiz(models.Model):
    _name = 'programation.line.wiz'
    _description = 'Asistente de líneas de programación'

    year = fields.Integer(string='Año', store=True, copied=True, tracking=0)

class ProjectCreateSaleOrder(models.Model):
    _name = 'project.create.sale.order'
    _description = 'Creación de órdenes de venta de proyectos'

    info_invoice = fields.Char(string='Info Factura', readonly=True, tracking=0)

class ProjectCreateSaleOrderLine(models.Model):
    _name = 'project.create.sale.order.line'
    _description = 'Líneas de creación de órdenes de venta de proyectos'

    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)

class ProjectDistribution(models.Model):
    _name = 'project.distribution'
    _description = 'Distribuciones de proyectos'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)

class ProjectDistributionLine(models.Model):
    _name = 'project.distribution.line'
    _description = 'Líneas de distribuciones de proyectos'

    name = fields.Char(string='Nombre', readonly=True, required=True, tracking=0)
    project_percentage = fields.Float(string='Porcentaje', store=True, required=True, copied=True, tracking=0)

class ProjectLineaNegocio(models.Model):
    _name = 'project.linea.negocio'
    _description = 'Líneas de negocio de proyectos'

    name = fields.Char(string='Línea de negocio', store=True, copied=True, tracking=0)

class ProjectProfitabilityReport(models.Model):
    _name = 'project.profitability.report'
    _description = 'Reportes de rentabilidad de proyectos'

    amount_untaxed_invoiced = fields.Float(string='Base imponible facturada', store=True, readonly=True, copied=True, tracking=0)
    amount_untaxed_to_invoice = fields.Float(string='Importe no gravado a la factura', store=True, readonly=True, copied=True, tracking=0)
    expense_amount_untaxed_invoiced = fields.Float(string='Importe no gravado re-facturado', store=True, readonly=True, copied=True, tracking=0)
    expense_amount_untaxed_to_invoice = fields.Float(string='Importe no gravado para volver a facturar', store=True, readonly=True, copied=True, tracking=0)
    expense_cost = fields.Float(string='Otros costos', store=True, readonly=True, copied=True, tracking=0)
    line_date = fields.Date(string='Fecha', store=True, readonly=True, copied=True, tracking=0)
    margin = fields.Float(string='Margen', store=True, readonly=True, copied=True, tracking=0)
    order_confirmation_date = fields.Datetime(string='Fecha de confirmación del pedido de ventas', store=True, readonly=True, copied=True, tracking=0)
    other_revenues = fields.Float(string='Otros ingresos', store=True, readonly=True, copied=True, tracking=0)
    timesheet_cost = fields.Float(string='Costo del Parte de Horas', store=True, readonly=True, copied=True, tracking=0)
    timesheet_unit_amount = fields.Float(string='Duración del parte de horas', store=True, readonly=True, copied=True, tracking=0)

class ProjectProject(models.Model):
    _inherit = 'project.project'
    allow_billable = fields.Boolean(string='Facturable', store=True, copied=True, tracking=0)
    allow_timesheets = fields.Boolean(string='Partes de horas', store=True, copied=True, tracking=0)
    app_server = fields.Char(string='App Server', store=True, copied=True, tracking=0)
    cliente_operaciones = fields.Boolean(string='Cliente Operaciones', store=True, copied=True, tracking=1)
    customer = fields.Boolean(string='Tipo contacto', tracking=1)
    db_name = fields.Char(string='Nombre de base de datos', store=True, copied=True, tracking=0)
    db_port = fields.Char(string='Puerto de base de datos', store=True, copied=True, tracking=0)
    db_server = fields.Char(string='Servidor de Base de datos', store=True, copied=True, tracking=0)
    display_create_order = fields.Boolean(string='Mostrar Crear pedido', readonly=True, tracking=0)
    email = fields.Char(string='Dirección de Email', tracking=1)
    encode_uom_in_days = fields.Boolean(string='Codificar Uom en días', readonly=True, tracking=0)
    key = fields.Boolean(string='Key', store=True, copied=True, tracking=0)
    ref_num = fields.Char(string='Número de identificación', tracking=1)
    ssh_port = fields.Char(string='Puerto SSH', store=True, copied=True, tracking=0)
    total_timesheet_time = fields.Integer(string='Tiempo total del parte de horas', readonly=True, tracking=0)
    warning_employee_rate = fields.Boolean(string='Tasa de advertencia para los empleados', readonly=True, tracking=0)
    work_phone = fields.Char(string='Teléfono trabajo', tracking=1)

class ProjectSaleLineEmployeeMap(models.Model):
    _name = 'project.sale.line.employee.map'
    _description = 'Mapeo de empleados en líneas de venta de proyectos'

    price_unit = fields.Float(string='Precio unitario', store=True, readonly=True, tracking=0)

class ProjectServiceOrder(models.Model):
    _name = 'project.service.order'
    _description = 'Órdenes de servicio de proyectos'

    cliente_address = fields.Char(string='Dirección', store=True, copied=True, tracking=0)
    cliente_phone = fields.Char(string='Teléfono', store=True, copied=True, tracking=0)
    contact_job = fields.Char(string='Cargo de contacto', store=True, readonly=True, tracking=0)
    count_moves = fields.Integer(string='Movimientos', readonly=True, tracking=0)
    cuotas = fields.Integer(string='Número de cuotas', store=True, copied=True, tracking=0)
    date = fields.Date(string='Fecha de solicitud', store=True, copied=True, tracking=0)
    description = fields.Char(string='Descripción', store=True, copied=True, tracking=0)
    financed = fields.Boolean(string='Financiado', store=True, copied=True, tracking=0)
    horas_ejecutadas = fields.Float(string='Horas ejecutadas', readonly=True, tracking=0)
    horas_facturables = fields.Float(string='Horas facturables', readonly=True, tracking=0)
    initial_cuota = fields.Float(string='Cuota inicial', store=True, copied=True, tracking=0)
    is_manager = fields.Boolean(string='¿Es gerente?', readonly=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    months_cuota = fields.Integer(string='Meses por cuota', store=True, copied=True, tracking=0)
    mora_rate = fields.Float(string='Intereses por mora', store=True, copied=True, tracking=0)
    nit_cliente = fields.Char(string='Nit cliente', store=True, readonly=True, tracking=0)
    notes = fields.Char(string='Observaciones generales', store=True, copied=True, tracking=0)
    pref_number = fields.Char(string='Orden de servicio', store=True, readonly=True, copied=True, tracking=0)
    project_value = fields.Float(string='Valor del proyecto', store=True, copied=True, tracking=0)
    rate = fields.Float(string='Intereses', store=True, copied=True, tracking=0)
    to_finance = fields.Float(string='Valor a Financiar', store=True, copied=True, tracking=0)

class ProjectServiceOrderLine(models.Model):
    _name = 'project.service.order.line'
    _description = 'Líneas de órdenes de servicio de proyectos'

    adicional_valor = fields.Float(string='Valor adicional', store=True, copied=True, tracking=100)
    adicional = fields.Char(string='Concepto adicional', store=True, copied=True, tracking=100)
    cantidad_vigilantes = fields.Float(string='Cantidad de vigilantes', store=True, copied=True, tracking=0)
    code_puesto = fields.Char(string='Código de puesto', store=True, readonly=True, tracking=0)
    dias_facturables = fields.Integer(string='Días mes', store=True, readonly=True, tracking=100)
    duration = fields.Float(string='Total horas', store=True, readonly=True, tracking=100)
    end_date = fields.Datetime(string='Fecha finalización', store=True, copied=True, tracking=100)
    force_value = fields.Boolean(string='Forzar tarifa especial', store=True, copied=True, tracking=100)
    holidays = fields.Boolean(string='Festivos', store=True, copied=True, tracking=100)
    horas_facturables = fields.Integer(string='Horas facturables', store=True, copied=True, tracking=100)
    id_sale_order_line = fields.Integer(string='ID Línea de cotización', store=True, copied=True, tracking=0)
    is_manager = fields.Boolean(string='¿Es gerente?', readonly=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    monitoring_value = fields.Float(string='Valor monitoreo', store=True, copied=True, tracking=0)
    name_sale_order = fields.Char(string='Número de cotización', store=True, copied=True, tracking=0)
    name = fields.Char(string='Ubicación del servicio', store=True, copied=True, tracking=100)
    no_cost = fields.Boolean(string='Sin Costo', store=True, copied=True, tracking=0)
    notes = fields.Char(string='Observaciones', store=True, copied=True, tracking=0)
    observaciones = fields.Text(string='Observaciones', store=True, copied=True, tracking=0)
    puesto_id_code = fields.Char(string='Puesto Asociado Corto', store=True, tracking=0)
    rest_in = fields.Char(string='Salida a descanso', store=True, copied=True, tracking=0)
    rest_out = fields.Char(string='Entrada de descanso', store=True, copied=True, tracking=0)
    seguro_psvv = fields.Float(string='Póliza de seguro de vida', store=True, copied=True, tracking=0)
    service_number = fields.Integer(string='Número de servicio', store=True, copied=True, tracking=0)
    start_date = fields.Datetime(string='Fecha de inicio', store=True, copied=True, tracking=100)
    subtotal = fields.Float(string='Subtotal', store=True, copied=True, tracking=0)
    time_in = fields.Char(string='Hora de entrada', store=True, copied=True, tracking=100)
    time_out = fields.Char(string='Hora de salida', store=True, copied=True, tracking=100)
    use_parent_modality = fields.Boolean(string='Usa modalidad padre', readonly=True, tracking=0)
    valor = fields.Float(string='Valor antes de IVA', store=True, copied=True, tracking=100)

class ProjectServiceOrderLineInvoice(models.Model):
    _name = 'project.service.order.line.invoice'
    _description = 'Facturas de líneas de órdenes de servicio de proyectos'

    amount_total_invoiced = fields.Float(string='Total Facturado', store=True, readonly=True, tracking=0)
    description = fields.Char(string='Description', store=True, copied=True, tracking=0)
    end_date = fields.Datetime(string='Fecha fin servicio', store=True, copied=True, tracking=0)
    fact_end_date = fields.Date(string='Fin Facturación', store=True, copied=True, tracking=0)
    fact_start_date = fields.Date(string='Inicio Facturación', store=True, copied=True, tracking=0)
    fecha_inicio = fields.Date(string='Fecha de programación', store=True, copied=True, tracking=0)
    info = fields.Char(string='Mensaje de cancelación', store=True, copied=True, tracking=100)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    puesto_code = fields.Char(string='Puesto', store=True, readonly=True, tracking=0)
    remaining_value = fields.Float(string='Valor residual', store=True, readonly=True, tracking=0)
    start_date = fields.Datetime(string='Fecha inicio servicio', store=True, copied=True, tracking=0)
    total_value = fields.Float(string='Valor total', store=True, copied=True, tracking=0)
    valor_mensual = fields.Float(string='Valor mensual', store=True, copied=True, tracking=0)

class ProjectServiceOrderLineItemCancel(models.Model):
    _name = 'project.service.order.line.item.cancel'
    _description = 'Cancelación de ítems de líneas de órdenes de servicio de proyectos'

    name = fields.Char(string='Motivo de cancelación', store=True, copied=True, tracking=0)

class ProjectServiceOrderSupport(models.Model):
    _name = 'project.service.order.support'
    _description = 'Soportes de órdenes de servicio de proyectos'

    name = fields.Char(string='Soporte de orden de servicio', store=True, copied=True, tracking=0)

class ProjectServiceOrderTmp(models.Model):
    _name = 'project.service.order.tmp'
    _description = 'Temporales de órdenes de servicio de proyectos'

    balance = fields.Float(string='Saldo anterior', store=True, copied=True, tracking=0)
    capital = fields.Float(string='Abono capital', store=True, copied=True, tracking=0)
    checked = fields.Boolean(string='Facturada', store=True, readonly=True, copied=True, tracking=0)
    cuota_number = fields.Integer(string='Cuota número', store=True, copied=True, tracking=0)
    date = fields.Date(string='Fecha cuota', store=True, copied=True, tracking=0)
    intereses = fields.Float(string='Intereses', store=True, copied=True, tracking=0)
    new_balance = fields.Float(string='Saldo capital', store=True, copied=True, tracking=0)
    value = fields.Float(string='Valor cuota', store=True, copied=True, tracking=0)

class ProjectServiceType(models.Model):
    _name = 'project.service.type'
    _description = 'Tipos de servicio de proyectos'

    ays = fields.Float(string='A&S', store=True, copied=True, tracking=0)
    name = fields.Char(string='Tipo de servicio', store=True, copied=True, tracking=0)

class ProjectTask(models.Model):
    _inherit = 'project.task'
    allow_billable = fields.Boolean(string='Facturable', readonly=True, tracking=0)
    allow_timesheets = fields.Boolean(string='Permitir partes de horas', readonly=True, tracking=0)
    analytic_account_active = fields.Boolean(string='Cuenta analítica activa', readonly=True, tracking=0)
    date_start = fields.Datetime(string='Start Date', store=True, copied=True, tracking=0)
    display_create_order = fields.Boolean(string='Mostrar Crear pedido', readonly=True, tracking=0)
    effective_hours = fields.Float(string='Horas dedicadas', store=True, readonly=True, tracking=0)
    encode_uom_in_days = fields.Boolean(string='Codificar Uom en días', readonly=True, tracking=0)
    has_multi_sol = fields.Boolean(string='Tiene varias soluciones', readonly=True, tracking=0)
    is_project_map_empty = fields.Boolean(string='¿El mapa del proyecto está vacío?', readonly=True, tracking=0)
    non_allow_billable = fields.Boolean(string='No facturable', store=True, copied=True, tracking=0)
    overtime = fields.Float(string='Horas extras', store=True, readonly=True, tracking=0)
    progress = fields.Float(string='En proceso', store=True, readonly=True, tracking=0)
    remaining_hours_available = fields.Boolean(string='Remaining Hours Available', readonly=True, tracking=0)
    remaining_hours_so = fields.Float(string='Remaining Hours on SO', readonly=True, tracking=0)
    remaining_hours = fields.Float(string='Horas restantes', store=True, readonly=True, tracking=0)
    subtask_effective_hours = fields.Float(string='Horas dedicadas en subtareas', store=True, readonly=True, tracking=0)
    ticket_count = fields.Integer(string='Tickets', readonly=True, tracking=0)
    total_hours_spent = fields.Float(string='Horas totales', store=True, readonly=True, tracking=0)

class ProjectTaskCreateSaleOrder(models.Model):
    _name = 'project.task.create.sale.order'
    _description = 'Creación de órdenes de venta de tareas de proyectos'

    info_invoice = fields.Char(string='Info Factura', readonly=True, tracking=0)
    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)

class ProjectTaskCreateTimesheet(models.Model):
    _name = 'project.task.create.timesheet'
    _description = 'Creación de partes de horas de tareas de proyectos'

    description = fields.Char(string='Descripción', store=True, copied=True, tracking=0)
    time_spent = fields.Float(string='Tiempo', store=True, copied=True, tracking=0)

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    purchase_ticket_count = fields.Integer(string='Tickets', readonly=True, tracking=0)

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    recoup = fields.Boolean(string='Recobro', store=True, copied=True, tracking=0)

class PurchaseRequisition(models.Model):
    _name = 'purchase.requisition'
    _description = 'Requisiciones de compra'

    activity_date_deadline = fields.Date(string='Siguiente plazo de actividad', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Resumen de la siguiente actividad', tracking=0)
    activity_type_icon = fields.Char(string='Ícono de tipo de actividad', readonly=True, tracking=0)
    date_end = fields.Datetime(string='Fecha límite', store=True, copied=True, tracking=100)
    description = fields.Text(string='Descripción', store=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Nº de archivos adjuntos', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Número de errores', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Error de Envío de Mensaje', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='Error de entrega del SMS', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Es seguidor', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Acción requerida', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Contador de mensajes no leídos', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Mensajes sin leer', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Referencia', store=True, readonly=True, required=True, tracking=0)
    order_count = fields.Integer(string='Número de órdenes', readonly=True, tracking=0)
    ordering_date = fields.Date(string='Fecha del Pedido', store=True, copied=True, tracking=100)
    origin = fields.Char(string='Documento Origen', store=True, copied=True, tracking=0)
    schedule_date = fields.Date(string='Fecha de entrega', index=True, store=True, copied=True, tracking=100)

class PurchaseRequisitionLine(models.Model):
    _name = 'purchase.requisition.line'
    _description = 'Líneas de requisiciones de compra'

    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)
    product_description_variants = fields.Char(string='Descripción personalizada', store=True, copied=True, tracking=0)
    product_qty = fields.Float(string='Cantidad', store=True, copied=True, tracking=0)
    qty_ordered = fields.Float(string='Cantidades pedidas', readonly=True, tracking=0)
    recoup = fields.Boolean(string='Recobro', store=True, copied=True, tracking=0)
    schedule_date = fields.Date(string='Fecha Programada', store=True, copied=True, tracking=0)

class PurchaseRequisitionType(models.Model):
    _name = 'purchase.requisition.type'
    _description = 'Tipos de requisiciones de compra'

    name = fields.Char(string='Tipo de acuerdo de compra', store=True, required=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=0)

class Querydeluxe(models.Model):
    _name = 'query.deluxe'
    _description = 'Consultas avanzadas'

    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    descripcion = fields.Char(string='Descripción Query', store=True, copied=True, tracking=0)
    html = fields.Html(string='HTML', store=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Text(string='Type a query :', store=True, copied=True, tracking=0)
    raw_output = fields.Text(string='Raw output', store=True, copied=True, tracking=0)
    rowcount = fields.Text(string='Rowcount', store=True, copied=True, tracking=0)
    show_raw_output = fields.Boolean(string='Show the raw output of the query', store=True, copied=True, tracking=0)
    tips_description = fields.Text(string='Description', readonly=True, tracking=0)
    valid_query_name = fields.Text(string='Valid Query Name', store=True, copied=True, tracking=0)

class QuoterAdditionalDotation(models.Model):
    _name = 'quoter.additional.dotation'
    _description = 'Dotaciones adicionales de cotizaciones'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    total_uniform = fields.Float(string='Total Uniformes', store=True, readonly=True, tracking=0)

class QuoterAdditionalDotationLine(models.Model):
    _name = 'quoter.additional.dotation.line'
    _description = 'Líneas de dotaciones adicionales de cotizaciones'

    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)
    qty = fields.Integer(string='Cantidad', store=True, copied=True, tracking=0)
    total_price = fields.Float(string='Total', readonly=True, tracking=0)

class QuoterAdditionalDotationLineAux(models.Model):
    _name = 'quoter.additional.dotation.line.aux'
    _description = 'Líneas auxiliares de dotaciones adicionales de cotizaciones'

    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)
    qty = fields.Integer(string='Cantidad', store=True, copied=True, tracking=0)
    total_price = fields.Float(string='Total', readonly=True, tracking=0)

class QuoterAmountDay(models.Model):
    _name = 'quoter.amount.day'
    _description = 'Cantidad de días de cotizaciones'

    amount_day = fields.Integer(string='Cantidad días', store=True, copied=True, tracking=0)
    holidays = fields.Boolean(string='Festivos', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class QuoterCanine(models.Model):
    _name = 'quoter.canine'
    _description = 'Caninos de cotizaciones'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    total_price_lines = fields.Float(string='Total', readonly=True, tracking=0)

class QuoterCanineLine(models.Model):
    _name = 'quoter.canine.line'
    _description = 'Líneas de caninos de cotizaciones'

    depreciation_value = fields.Integer(string='Valor Depreciación', store=True, copied=True, tracking=0)
    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)
    total_depreciation = fields.Float(string='Total', readonly=True, tracking=0)

class QuoterCanineLineAux(models.Model):
    _name = 'quoter.canine.line.aux'
    _description = 'Líneas auxiliares de caninos de cotizaciones'

    depreciation_value = fields.Integer(string='Valor Depreciación', store=True, copied=True, tracking=0)
    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)
    total_depreciation = fields.Float(string='Total', readonly=True, tracking=0)

class QuoterCommunication(models.Model):
    _name = 'quoter.communication'
    _description = 'Comunicaciones de cotizaciones'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    total_price_lines = fields.Float(string='Total', readonly=True, tracking=0)

class QuoterCommunicationLine(models.Model):
    _name = 'quoter.communication.line'
    _description = 'Líneas de comunicaciones de cotizaciones'

    depreciation_value = fields.Integer(string='Valor Depreciación', store=True, copied=True, tracking=0)
    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)
    quantity = fields.Integer(string='Cantidad', store=True, copied=True, tracking=0)
    total_depreciation = fields.Float(string='Total', readonly=True, tracking=0)

class QuoterCommunicationLineAditionalAux(models.Model):
    _name = 'quoter.communication.line.aditional.aux'
    _description = 'Líneas auxiliares adicionales de comunicaciones de cotizaciones'

    depreciation_value = fields.Integer(string='Valor Depreciación', store=True, copied=True, tracking=0)
    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)
    quantity = fields.Integer(string='Cantidad', store=True, copied=True, tracking=0)
    total_depreciation = fields.Float(string='Total', readonly=True, tracking=0)

class QuoterCommunicationLineAux(models.Model):
    _name = 'quoter.communication.line.aux'
    _description = 'Líneas auxiliares de comunicaciones de cotizaciones'

    depreciation_value = fields.Integer(string='Valor Depreciación', store=True, copied=True, tracking=0)
    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)
    quantity = fields.Integer(string='Cantidad', store=True, copied=True, tracking=0)
    total_depreciation = fields.Float(string='Total', readonly=True, tracking=0)

class QuoterConfAccount(models.Model):
    _name = 'quoter.conf.account'
    _description = 'Cuentas de configuración de cotizaciones'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class QuoterDotation(models.Model):
    _name = 'quoter.dotation'
    _description = 'Dotaciones de cotizaciones'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    total_uniform = fields.Float(string='Total Uniformes', store=True, readonly=True, tracking=0)

class QuoterDotationAdditionalPosition(models.Model):
    _name = 'quoter.dotation.additional.position'
    _description = 'Posiciones adicionales de dotaciones de cotizaciones'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    total_dotation_additional_position = fields.Float(string='Total Dotation Additional Position', store=True, readonly=True, tracking=0)

class QuoterDotationAdditionalPositionLine(models.Model):
    _name = 'quoter.dotation.additional.position.line'
    _description = 'Líneas de posiciones adicionales de dotaciones de cotizaciones'

    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)
    qty = fields.Integer(string='Cantidad', store=True, copied=True, tracking=0)
    total_price = fields.Float(string='Total', readonly=True, tracking=0)

class QuoterDotationAdditionalPositionLineAux(models.Model):
    _name = 'quoter.dotation.additional.position.line.aux'
    _description = 'Líneas auxiliares de posiciones adicionales de dotaciones de cotizaciones'

    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)
    qty = fields.Integer(string='Cantidad', store=True, copied=True, tracking=0)
    total_price = fields.Float(string='Total', readonly=True, tracking=0)

class QuoterDotationLine(models.Model):
    _name = 'quoter.dotation.line'
    _description = 'Líneas de dotaciones de cotizaciones'

    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)
    qty = fields.Integer(string='Cantidad', store=True, copied=True, tracking=0)
    total_price = fields.Float(string='Total', readonly=True, tracking=0)

class QuoterDotationLineAux(models.Model):
    _name = 'quoter.dotation.line.aux'
    _description = 'Líneas auxiliares de dotaciones de cotizaciones'

    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)
    qty = fields.Integer(string='Cantidad', store=True, copied=True, tracking=0)
    total_price = fields.Float(string='Total', readonly=True, tracking=0)

class QuoterDotationPosition(models.Model):
    _name = 'quoter.dotation.position'
    _description = 'Posiciones de dotaciones de cotizaciones'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    total_dotation_position = fields.Float(string='Total Dotation Position', store=True, readonly=True, tracking=0)

class QuoterDotationPositionLine(models.Model):
    _name = 'quoter.dotation.position.line'
    _description = 'Líneas de posiciones de dotaciones de cotizaciones'

    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)
    qty = fields.Integer(string='Cantidad', store=True, copied=True, tracking=0)
    total_price = fields.Float(string='Total', readonly=True, tracking=0)

class QuoterDotationPositionLineAux(models.Model):
    _name = 'quoter.dotation.position.line.aux'
    _description = 'Líneas auxiliares de posiciones de dotaciones de cotizaciones'

    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)
    qty = fields.Integer(string='Cantidad', store=True, copied=True, tracking=0)
    total_price = fields.Float(string='Total', readonly=True, tracking=0)

class QuoterDotationProtection(models.Model):
    _name = 'quoter.dotation.protection'
    _description = 'Protecciones de dotaciones de cotizaciones'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    total_dotation_protection = fields.Float(string='Total Dotation Protection', store=True, readonly=True, tracking=0)

class QuoterDotationProtectionLine(models.Model):
    _name = 'quoter.dotation.protection.line'
    _description = 'Líneas de protecciones de dotaciones de cotizaciones'

    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)
    qty = fields.Integer(string='Cantidad', store=True, copied=True, tracking=0)
    total_price = fields.Float(string='Total', readonly=True, tracking=0)

class QuoterDotationProtectionLineAux(models.Model):
    _name = 'quoter.dotation.protection.line.aux'
    _description = 'Líneas auxiliares de protecciones de dotaciones de cotizaciones'

    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)
    qty = fields.Integer(string='Cantidad', store=True, copied=True, tracking=0)
    total_price = fields.Float(string='Total', readonly=True, tracking=0)

class QuoterFinancing(models.Model):
    _name = 'quoter.financing'
    _description = 'Financiamientos de cotizaciones'

    balance = fields.Float(string='Saldo', store=True, copied=True, tracking=0)
    capital = fields.Float(string='Capital', store=True, copied=True, tracking=0)
    extra = fields.Float(string='Extras', store=True, copied=True, tracking=0)
    interests = fields.Float(string='Intereses', store=True, copied=True, tracking=0)
    quota_number = fields.Float(string='Cuota', store=True, copied=True, tracking=0)
    quota = fields.Float(string='Cuota', store=True, copied=True, tracking=0)

class QuoterFivep(models.Model):
    _name = 'quoter.fivep'
    _description = 'Cinco P de cotizaciones'

    balance = fields.Float(string='Saldo', readonly=True, tracking=0)
    delivery_date = fields.Date(string='Fecha Entrega', store=True, copied=True, tracking=0)
    name = fields.Char(string='Detalle', store=True, copied=True, tracking=0)
    observation = fields.Char(string='Observación', store=True, copied=True, tracking=0)
    quantity = fields.Integer(string='Cantidad', store=True, copied=True, tracking=0)
    total_delivery_value = fields.Float(string='Valor Entregado', store=True, copied=True, tracking=0)
    total_value = fields.Float(string='Valor Total', readonly=True, tracking=0)
    value = fields.Float(string='Valor', readonly=True, tracking=0)



class QuoterPosition(models.Model):
    _name = 'quoter.position'
    _description = 'Posiciones de cotizaciones'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class QuoterPositionService(models.Model):
    _name = 'quoter.position.service'
    _description = 'Servicios de posiciones de cotizaciones'

    service_number = fields.Integer(string='Número de servicio', store=True, copied=True, tracking=0)

class QuoterRateType(models.Model):
    _name = 'quoter.rate.type'
    _description = 'Tipos de tarifas de cotizaciones'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    rate_value = fields.Float(string='Valor de Tarifa', store=True, copied=True, tracking=0)

class QuoterSegment(models.Model):
    _name = 'quoter.segment'
    _description = 'Segmentos de cotizaciones'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class QuoterSelection(models.Model):
    _name = 'quoter.selection'
    _description = 'Selecciones de cotizaciones'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    total_selection = fields.Float(string='Total Selección', readonly=True, tracking=0)

class QuoterSelectionLine(models.Model):
    _name = 'quoter.selection.line'
    _description = 'Líneas de selecciones de cotizaciones'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)

class QuoterSelectionLineAux(models.Model):
    _name = 'quoter.selection.line.aux'
    _description = 'Líneas auxiliares de selecciones de cotizaciones'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)

class QuoterServiceMod(models.Model):
    _name = 'quoter.service.mod'
    _description = 'Modificaciones de servicios de cotizaciones'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    value_percentage = fields.Float(string='Valor porcentaje', store=True, copied=True, tracking=0)

class QuoterSupport(models.Model):
    _name = 'quoter.support'
    _description = 'Soportes de cotizaciones'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    total_support = fields.Float(string='Total Soportes', readonly=True, tracking=0)

class QuoterSupportLine(models.Model):
    _name = 'quoter.support.line'
    _description = 'Líneas de soportes de cotizaciones'

    depreciation_value = fields.Integer(string='Valor Depreciación', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)
    total_depreciation = fields.Float(string='Total', readonly=True, tracking=0)

class QuoterSupportLineAux(models.Model):
    _name = 'quoter.support.line.aux'
    _description = 'Líneas auxiliares de soportes de cotizaciones'

    depreciation_value = fields.Integer(string='Valor Depreciación', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)
    total_depreciation = fields.Float(string='Total', readonly=True, tracking=0)

class QuoterTechnology(models.Model):
    _name = 'quoter.technology'
    _description = 'Tecnologías de cotizaciones'

    name = fields.Char(string='Concepto', store=True, copied=True, tracking=0)
    total_cost = fields.Float(string='Costo Total', store=True, copied=True, tracking=0)
    total_income = fields.Float(string='Ingreso Total', store=True, copied=True, tracking=0)

class QuoterTraining(models.Model):
    _name = 'quoter.training'
    _description = 'Entrenamientos de cotizaciones'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    total_training = fields.Float(string='Total Entrenamientos', readonly=True, tracking=0)

class QuoterTrainingLine(models.Model):
    _name = 'quoter.training.line'
    _description = 'Líneas de entrenamientos de cotizaciones'

    course = fields.Float(string='Curso', readonly=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    people = fields.Integer(string='Personas', store=True, copied=True, tracking=0)
    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)

class QuoterTransport(models.Model):
    _name = 'quoter.transport'
    _description = 'Transportes de cotizaciones'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class QuoterVehicle(models.Model):
    _name = 'quoter.vehicle'
    _description = 'Vehículos de cotizaciones'

    monthly_value = fields.Float(string='Valor Mensual', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class QuoterWeaponType(models.Model):
    _name = 'quoter.weapon.type'
    _description = 'Tipos de armas de cotizaciones'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    total_price_lines = fields.Float(string='Total', readonly=True, tracking=0)

class QuoterWeaponTypeLine(models.Model):
    _name = 'quoter.weapon.type.line'
    _description = 'Líneas de tipos de armas de cotizaciones'

    depreciation_value = fields.Integer(string='Valor Depreciación', store=True, copied=True, tracking=0)
    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)
    total_depreciation = fields.Float(string='Total', readonly=True, tracking=0)

class QuoterWeaponTypeLineAux(models.Model):
    _name = 'quoter.weapon.type.line.aux'
    _description = 'Líneas auxiliares de tipos de armas de cotizaciones'

    depreciation_value = fields.Integer(string='Valor Depreciación', store=True, copied=True, tracking=0)
    price_unit = fields.Float(string='Precio Unitario', store=True, copied=True, tracking=0)
    total_depreciation = fields.Float(string='Total', readonly=True, tracking=0)

class RemplazoNovedadWiz(models.Model):
    _name = 'reemplazo.novedad.wiz'
    _description = 'Asistente de reemplazo de novedades'

    date_end = fields.Date(string='Fecha Fin', store=True, copied=True, tracking=0)
    date_from = fields.Date(string='Fecha Inicio', store=True, copied=True, tracking=0)
    day_from = fields.Integer(string='Día desde', store=True, required=True, copied=True, tracking=0)
    day_to = fields.Integer(string='Día hasta', store=True, required=True, copied=True, tracking=0)
    hour_restriction = fields.Boolean(string='Restricción por horas', store=True, copied=True, tracking=0)
    no_aditional = fields.Boolean(string='No adicional', store=True, copied=True, tracking=0)
    novelty_support_file = fields.Text(string='Soporte de novedad', store=True, copied=True, tracking=0)
    observaciones = fields.Char(string='Observaciones', store=True, copied=True, tracking=0)
    permanent = fields.Boolean(string='Novedad permanente', store=True, copied=True, tracking=0)
    politica_adicional = fields.Boolean(string='Política adicional', readonly=True, tracking=0)
    time_from = fields.Char(string='Hora desde', store=True, copied=True, tracking=0)
    time_to = fields.Char(string='Hora hasta', store=True, copied=True, tracking=0)
    type_name = fields.Char(string='Nombre', readonly=True, tracking=0)
    yes_aditional = fields.Boolean(string='Sí adicional', store=True, copied=True, tracking=0)

class RemplazoNovedadWizMasive(models.Model):
    _name = 'reemplazo.novedad.wiz.masive'
    _description = 'Asistente masivo de reemplazo de novedades'

    date_end = fields.Date(string='Fecha Fin', store=True, copied=True, tracking=0)
    date_from = fields.Date(string='Fecha Inicio', store=True, copied=True, tracking=0)
    day_from = fields.Integer(string='Día desde', store=True, required=True, copied=True, tracking=0)
    day_to = fields.Integer(string='Día hasta', store=True, required=True, copied=True, tracking=0)
    hour_restriction = fields.Boolean(string='Restricción por horas', store=True, copied=True, tracking=0)
    novelty_support_file = fields.Text(string='Soporte de novedad', store=True, copied=True, tracking=0)
    permanent = fields.Boolean(string='Novedad permanente', store=True, copied=True, tracking=0)
    time_from = fields.Char(string='Hora desde', store=True, copied=True, tracking=0)
    time_to = fields.Char(string='Hora hasta', store=True, copied=True, tracking=0)
    type_name = fields.Char(string='Nombre', readonly=True, tracking=0)

class ReplicarProgramacionWiz(models.Model):
    _name = 'replicar.programacion.wiz'
    _description = 'Asistente de replicación de programación'

    repeticiones = fields.Integer(string='Repeticiones', store=True, copied=True, tracking=0)

class ReportAccountBiBudgetLine(models.Model):
    _name = 'report.account.bi.budget.line'
    _description = 'Líneas de reporte de presupuesto BI contable'

    amount = fields.Float(string='Monto Presupuesto', store=True, copied=True, tracking=0)
    date = fields.Date(string='Fecha', store=True, copied=True, tracking=0)
    difference = fields.Float(string='Diferencia', store=True, copied=True, tracking=0)
    place = fields.Char(string='Puesto', store=True, copied=True, tracking=0)
    practical_amount = fields.Float(string='Monto Real', store=True, copied=True, tracking=0)
    sede = fields.Char(string='Sede', store=True, copied=True, tracking=0)
    variation = fields.Float(string='Variación (%)', store=True, copied=True, tracking=0)

class ReportAccountBiBudgetWizard(models.Model):
    _name = 'report.account.bi.budget.wizard'
    _description = 'Asistente de reporte de presupuesto BI contable'

    date_from = fields.Date(string='Fecha Desde', store=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha Hasta', store=True, copied=True, tracking=0)

class ReportCenter(models.Model):
    _name = 'report.center'
    _description = 'Centro de reportes'

    xml = fields.Text(string='Xml', store=True, copied=True, tracking=0)

class ReportProjectTaskUser(models.Model):
    _inherit = 'report.project.task.user'
    hours_effective = fields.Float(string='Horas reales', store=True, readonly=True, copied=True, tracking=0)
    hours_planned = fields.Float(string='Horas planeadas', store=True, readonly=True, copied=True, tracking=0)
    progress = fields.Float(string='En proceso', store=True, readonly=True, copied=True, tracking=0)
    remaining_hours = fields.Float(string='Horas restantes', store=True, readonly=True, copied=True, tracking=0)

class ReportUninvoicedOrderLine(models.Model):
    _name = 'report.uninvoiced.order.line'
    _description = 'Líneas de órdenes no facturadas'

    adicional_valor = fields.Float(string='Valor adicional', store=True, readonly=True, tracking=0)
    date_end = fields.Datetime(string='Fecha finalización', store=True, readonly=True, tracking=0)
    date_from = fields.Datetime(string='Facturar desde', store=True, copied=True, tracking=0)
    date_start = fields.Datetime(string='Fecha de inicio', store=True, readonly=True, tracking=0)
    date_to = fields.Datetime(string='Facturar hasta', store=True, copied=True, tracking=0)
    force_value = fields.Boolean(string='Forzar tarifa especial', store=True, readonly=True, tracking=0)
    no_cost = fields.Boolean(string='Sin Costo', readonly=True, tracking=0)
    valor = fields.Float(string='Valor antes de IVA', store=True, readonly=True, tracking=0)

class ReportUninvoicedOrderLineWizard(models.Model):
    _name = 'report.uninvoiced.order.line.wizard'
    _description = 'Asistente de líneas de órdenes no facturadas'

    date_from = fields.Date(string='Date From', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Date To', store=True, required=True, copied=True, tracking=0)

class RequisicionLine(models.Model):
    _name = 'requisicion.line'
    _description = 'Líneas de requisiciones'

    cedula = fields.Char(string='Cédula', store=True, copied=True, tracking=1)

class ResCiiu(models.Model):
    _name = 'res.ciiu'
    _description = 'CIIU de recursos'

    description = fields.Char(string='Descripción', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Código', store=True, required=True, copied=True, tracking=0)

class ResCity(models.Model):
    _name = 'res.city'
    _description = 'Ciudades'

    code = fields.Char(string='Código de Ciudad', store=True, copied=True, tracking=0)
    kactus = fields.Char(string='Código Kactus', store=True, copied=True, tracking=1)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    zipcode = fields.Char(string='C.P.', store=True, copied=True, tracking=0)

class ResCityZip(models.Model):
    _name = 'res.city.zip'
    _description = 'Códigos postales de ciudades'

    name = fields.Char(string='C.P.', store=True, required=True, copied=True, tracking=0)
    type = fields.Char(string='Tipo', store=True, copied=True, tracking=0)

class ResCompany(models.Model):
    _inherit = 'res.company'
    access_for_everyone = fields.Boolean(string='Acceso para todos', store=True, copied=True, tracking=0)
    account_taoriginal_periodicity_reminder_day = fields.Integer(string='Start from original', store=True, copied=True, tracking=0)
    account_taperiodicity_reminder_day = fields.Integer(string='Start from', store=True, copied=True, tracking=0)
    additional_hours_delivery_datetime = fields.Float(string='Horas Adicionales', store=True, copied=True, tracking=0)
    aditional_option = fields.Boolean(string='Opción de Turnos adicionales', store=True, copied=True, tracking=0)
    analytic_account = fields.Boolean(string='Global Analytic Account', store=True, copied=True, tracking=0)
    aplica_adicional_nocturno_dom_fes = fields.Boolean(string='Aplica adicional nocturno dominical festivo', store=True, copied=True, tracking=0)
    aplica_psvv = fields.Boolean(string='Aplica póliza de seguro de vida?', store=True, copied=True, tracking=0)
    assignment_code = fields.Char(string='Código de Asignación', store=True, copied=True, tracking=0)
    attach_customer_order = fields.Boolean(string='Adjuntar OC Cliente', store=True, copied=True, tracking=0)
    attach_delivery_note = fields.Boolean(string='Adjuntar Remisión', store=True, copied=True, tracking=0)
    attach_invoice_docs = fields.Boolean(string='Enviar Adjuntos de Factura', store=True, copied=True, tracking=0)
    auto_acceptance_email = fields.Boolean(string='Email de Aceptación Automático', store=True, copied=True, tracking=0)
    auto_close_ticket = fields.Boolean(string='Ticket de cierre automático', store=True, copied=True, tracking=0)
    automatic_delivery_datetime = fields.Boolean(string='¿Fecha de Entrega Automática?', store=True, copied=True, tracking=0)
    branch_office = fields.Boolean(string='Active Branch Office Management', store=True, copied=True, tracking=0)
    category = fields.Boolean(string='Categoría', store=True, copied=True, tracking=0)
    certificate_date = fields.Date(string='Fecha de Validez del Certificado', store=True, copied=True, tracking=0)
    certificate_file = fields.Text(string='Archivo del Certificado', store=True, copied=True, tracking=0)
    certificate_filename = fields.Char(string='Nombre de Archivo del Certificado', store=True, copied=True, tracking=0)
    certificate_password = fields.Char(string='Contraseña del Certificado', store=True, copied=True, tracking=0)
    certificate_remaining_days = fields.Integer(string='Días Restantes del Certificado', store=True, copied=True, tracking=0)
    cierre_adicionales_diferente_periodo = fields.Boolean(string='Cierre de adicionales con diferente período', store=True, copied=True, tracking=0)
    close_days = fields.Integer(string='Número de días', store=True, copied=True, tracking=0)
    code_operator_information = fields.Char(string='Código del operador de información', store=True, copied=True, tracking=0)
    commercial_distribution = fields.Boolean(string='Active Business Unit', store=True, copied=True, tracking=0)
    company_signature = fields.Text(string='Firma', store=True, copied=True, tracking=0)
    control_cargo = fields.Boolean(string='Control de cargo', store=True, copied=True, tracking=0)
    control_hours = fields.Boolean(string='Control de horas', store=True, copied=True, tracking=0)
    country_enforce_cities = fields.Boolean(string='Forzar ciudades', readonly=True, tracking=0)
    credit_control_tolerance = fields.Float(string='Tolerancia de control de crédito', store=True, copied=True, tracking=0)
    customer_rating = fields.Boolean(string='Valoración de los clientes', store=True, copied=True, tracking=0)
    cut_off_date_holiday_book = fields.Date(string='Fecha de Corte Libro de Vacaciones', store=True, copied=True, tracking=0)
    descontar_dominical = fields.Boolean(string='Descontar día de descanso', store=True, copied=True, tracking=0)
    draft_novelty = fields.Boolean(string='Novedades en Borrador', store=True, copied=True, tracking=0)
    ei_automatic_generation = fields.Boolean(string='Enviar Factura al Validar', store=True, copied=True, tracking=0)
    ei_database = fields.Char(string='Base de Datos', store=True, required=True, copied=True, tracking=0)
    ei_tmp_path = fields.Char(string='Ruta de Archivos Temporales', store=True, copied=True, tracking=0)
    einvoicing_email = fields.Char(string='Correo Electrónico de Factura Electrónica, De:', store=True, copied=True, tracking=0)
    einvoicing_enabled = fields.Boolean(string='Facturación electrónica Habilitada', store=True, copied=True, tracking=0)
    einvoicing_partner_no_email = fields.Char(string='Correos Electrónicos Fallidos, A:', store=True, copied=True, tracking=0)
    einvoicing_receives_all_emails = fields.Char(string='Correo electrónico que recibe todos los correos electrónicos', store=True, copied=True, tracking=0)
    electronic_invoice = fields.Boolean(string='Activar Facturación Electrónica', store=True, copied=True, tracking=0)
    epayroll_assignment_code = fields.Char(string='Assignment Code', store=True, copied=True, tracking=0)
    epayroll_certificate_date = fields.Date(string='Certificate Date Validity', store=True, copied=True, tracking=0)
    epayroll_certificate_file = fields.Text(string='Certificate File', store=True, copied=True, tracking=0)
    epayroll_certificate_filename = fields.Char(string='Certificate Filename', store=True, copied=True, tracking=0)
    epayroll_certificate_password = fields.Char(string='Certificate Password', store=True, copied=True, tracking=0)
    epayroll_certificate_remaining_days = fields.Integer(string='Certificate Remaining Days', store=True, copied=True, tracking=0)
    epayroll_create_dian_document = fields.Boolean(string='Create DIAN Document When Validate?', store=True, copied=True, tracking=0)
    epayroll_email = fields.Char(string='E-Payroll Email, From:', store=True, copied=True, tracking=0)
    epayroll_employee_no_email = fields.Char(string='Employee Without Email, To:', store=True, copied=True, tracking=0)
    epayroll_enabled = fields.Boolean(string='E-Payroll Enabled', store=True, copied=True, tracking=0)
    epayroll_have_technological_provider = fields.Boolean(string='Do you have a technological provider?', store=True, copied=True, tracking=0)
    epayroll_receives_all_emails = fields.Char(string='Mail That Receives All Emails', store=True, copied=True, tracking=0)
    epayroll_signature_policy_description = fields.Char(string='Signature Policy Description', store=True, copied=True, tracking=0)
    epayroll_signature_policy_file = fields.Text(string='Signature Policy File', store=True, copied=True, tracking=0)
    epayroll_signature_policy_filename = fields.Char(string='Signature Policy Filename', store=True, copied=True, tracking=0)
    epayroll_signature_policy_url = fields.Char(string='Signature Policy URL', store=True, copied=True, tracking=0)
    epayroll_software_id = fields.Char(string='Software ID', store=True, copied=True, tracking=0)
    epayroll_software_pin = fields.Char(string='Software PIN', store=True, copied=True, tracking=0)
    epayroll_test_set_id = fields.Char(string='Test Set ID', store=True, copied=True, tracking=0)
    force_send_mail = fields.Boolean(string='¿Forzar envío de correo?', store=True, copied=True, tracking=0)
    generar_ausencia_dias_no_programados = fields.Boolean(string='Generar ausencia para días no programados', store=True, copied=True, tracking=0)
    get_numbering_range_response = fields.Text(string='Respuesta de GetNumberingRange', store=True, copied=True, tracking=0)
    have_technological_provider = fields.Boolean(string='¿Tienes un proveedor tecnológico?', store=True, copied=True, tracking=0)
    induction = fields.Boolean(string='Control de Inducción', store=True, copied=True, tracking=0)
    invoice_batch_process = fields.Boolean(string='Procesamiento Masivo', store=True, copied=True, tracking=0)
    invoicing_switch_threshold = fields.Date(string='Invoicing Switch Threshold', store=True, copied=True, tracking=0)
    legal_representative = fields.Char(string='Representante Legal', store=True, copied=True, tracking=0)
    liquidar_31 = fields.Boolean(string='Liquidar día 31', store=True, copied=True, tracking=0)
    mahours_14x7 = fields.Integer(string='Máximo de horas para modalidad 14x7', store=True, copied=True, tracking=0)
    pdf_name = fields.Boolean(string='PDF - Usar mismo número de factura?', store=True, copied=True, tracking=0)
    permitir_editar_turnos_cerrados = fields.Boolean(string='Permitir editar turnos cerrados', store=True, copied=True, tracking=0)
    project_distribution = fields.Boolean(string='Active Project Distribution', store=True, copied=True, tracking=0)
    report_icon1 = fields.Text(string='Icono 1', store=True, copied=True, tracking=0)
    report_icon2 = fields.Text(string='Icono 2', store=True, copied=True, tracking=0)
    report_icon3 = fields.Text(string='Icono 3', store=True, copied=True, tracking=0)
    report_icon4 = fields.Text(string='Icono 4', store=True, copied=True, tracking=0)
    report_icon5 = fields.Text(string='Icono 5', store=True, copied=True, tracking=0)
    report_icon6 = fields.Text(string='Icono 6', store=True, copied=True, tracking=0)
    report_icon7 = fields.Text(string='Icono 7', store=True, copied=True, tracking=0)
    report_icon8 = fields.Text(string='Icono 8', store=True, copied=True, tracking=0)
    report_icon9 = fields.Text(string='Icono 9', store=True, copied=True, tracking=0)
    rest_control = fields.Boolean(string='Control de descanso', store=True, copied=True, tracking=0)
    restringir_obra_labor = fields.Boolean(string='Restringir Obra labor', store=True, copied=True, tracking=0)
    send_failure_mail = fields.Boolean(string='¿Enviar Correo de Error?', store=True, copied=True, tracking=0)
    service_url_get = fields.Char(string='URL Respuesta', store=True, copied=True, tracking=0)
    service_url_post = fields.Char(string='URL Petición', store=True, copied=True, tracking=0)
    service_url = fields.Char(string='URL Servicio', store=True, copied=True, tracking=0)
    sh_auto_add_customer_as_follower = fields.Boolean(string='¿Agregar automáticamente al cliente como seguidor cuando crea Ticket?', store=True, copied=True, tracking=0)
    sh_configure_activate = fields.Boolean(string='Administrar productos', store=True, copied=True, tracking=0)
    sh_customer_replied = fields.Boolean(string='¿Cambio en la etapa cuando el cliente respondió?', store=True, copied=True, tracking=0)
    sh_default_description = fields.Boolean(string='Descripción predeterminada en la hoja de tiempo?', store=True, copied=True, tracking=0)
    sh_display_in_chatter = fields.Boolean(string='Mostrar en el mensaje de charla?', store=True, copied=True, tracking=0)
    sh_display_multi_user = fields.Boolean(string='Mostrar múltiples usuarios?', store=True, copied=True, tracking=0)
    sh_display_ticket_reminder = fields.Boolean(string='¿Recordatorio de tickets?', store=True, copied=True, tracking=0)
    sh_file_size = fields.Integer(string='Tamaño del accesorio del portal (KB)', store=True, copied=True, tracking=0)
    sh_multiple_ticket_allowed = fields.Boolean(string='¿Se permiten múltiples tickets?', store=True, copied=True, tracking=0)
    sh_pdf_in_message = fields.Boolean(string='¿Enviar URL de informe en el mensaje?', store=True, copied=True, tracking=0)
    sh_receive_email_seeing_ticket = fields.Boolean(string='¿Recibe correo electrónico cuando el cliente ve el ticket?', store=True, copied=True, tracking=0)
    sh_signature = fields.Boolean(string='¿Firma?', store=True, copied=True, tracking=0)
    sh_staff_replied = fields.Boolean(string='¿Cambio en el escenario cuando respondió el personal?', store=True, copied=True, tracking=0)
    sh_ticket_product_detail = fields.Boolean(string='¿Detalles del producto del ticket en el mensaje?', store=True, copied=True, tracking=0)
    sh_ticket_url_in_message = fields.Boolean(string='¿Enviar URL de tickets en el mensaje?', store=True, copied=True, tracking=0)
    signature_policy_description = fields.Char(string='Descripción de la Política de Firma', store=True, copied=True, tracking=0)
    signature_policy_file = fields.Text(string='Archivo de Política de Firma', store=True, copied=True, tracking=0)
    signature_policy_filename = fields.Char(string='Nombre de Archivo de Política de Firma', store=True, copied=True, tracking=0)
    signature_policy_url = fields.Char(string='URL de Política de Firma', store=True, copied=True, tracking=0)
    software_code_dian = fields.Char(string='Código Software DIAN', store=True, copied=True, tracking=0)
    software_id = fields.Char(string='ID del software', store=True, copied=True, tracking=0)
    software_pin = fields.Char(string='PIN del Software', store=True, copied=True, tracking=0)
    software_token = fields.Char(string='Token', store=True, copied=True, tracking=0)
    sub_category = fields.Boolean(string='Subcategoría', store=True, copied=True, tracking=0)
    taexigibility = fields.Boolean(string='Usar base de efectivo', store=True, copied=True, tracking=0)
    talock_date = fields.Date(string='Fecha de bloqueo de impuestos', store=True, copied=True, tracking=0)
    tarifario_cierre = fields.Boolean(string='Generar Tarifario al cierre', store=True, copied=True, tracking=0)
    test_set_id = fields.Char(string='Test Set ID', store=True, copied=True, tracking=0)
    totals_below_sections = fields.Boolean(string='Add totals below sections', store=True, copied=True, tracking=0)
    tributary_obligations = fields.Char(string='Obligaciones Tributarias', store=True, copied=True, tracking=0)
    use_parent_modality = fields.Boolean(string='Usa modalidad padre', store=True, copied=True, tracking=0)
    validate_einvoicing_email = fields.Boolean(string='¿Validar el Correo Electrónico de Facturación Electrónica?', store=True, copied=True, tracking=0)
    vat_check_vies = fields.Boolean(string='Verificar números de identificación fiscal (NIF)', store=True, copied=True, tracking=0)

#class ResConfigSettings(models.TransientModel):
#    _inherit = 'res.config.settings'
#    access_for_everyone = fields.Boolean(string='Ticket de vista portal con token de acceso', tracking=0)
#    account_taperiodicity_reminder_day = fields.Integer(string='Reminder', required=True, tracking=0)
#    allow_requisition_more_products = fields.Boolean(string='Permitir más requisiciones mismo producto y cantidad', store=True, copied=True, tracking=0)
#   anglo_saxon_accounting = fields.Boolean(string='Use anglo-saxon accounting', tracking=0)
#    approval_managers = fields.Boolean(string='Gestores de Aprobación', store=True, copied=True, tracking=0)
#    auto_close_ticket = fields.Boolean(string='Ticket de cierre automático', tracking=0)
#   average_salary_prima = fields.Boolean(string='Promedio de salarios en prima', store=True, copied=True, tracking=0)
#    average_sub_trans = fields.Boolean(string='Promediar subsidio de transporte en prestaciones sociales', store=True, copied=True, tracking=0)
#    cal_client_id = fields.Char(string='Client.id', store=True, copied=True, tracking=0)
#    cal_client_secret = fields.Char(string='Client.key', store=True, copied=True, tracking=0)
#    category = fields.Boolean(string='Categoría', tracking=0)
#    ciiu_ica = fields.Boolean(string='Ciiu en ICA', store=True, copied=True, tracking=0)
#    city_cc = fields.Boolean(string='Ciudades en cuentas analíticas', store=True, copied=True, tracking=0)
#    client_name_dotation_stock = fields.Boolean(string='Asiento de dotación a nombre del empleado', store=True, copied=True, tracking=0)
#    close_days = fields.Integer(string='Número de días', tracking=0)
#    create_payslip_prov = fields.Boolean(string='Cálculo automático de provisiones', store=True, copied=True, tracking=0)
#    credit_control_tolerance = fields.Float(string='Tolerancia de control de crédito', tracking=0)
#    customer_rating = fields.Boolean(string='Valoración de los clientes', tracking=0)
#    days_advance = fields.Float(string='Días vencimiento anticipo', store=True, copied=True, tracking=0)
#    days_suspensions_libraryvac = fields.Boolean(string='Días de suspensiones en libro de vacaciones', store=True, copied=True, tracking=0)
#    ded_round = fields.Boolean(string='Redondeo de deducciones EPS,PEN,FSO', store=True, copied=True, tracking=0)
#    discount_first_rest_day = fields.Boolean(string='Descontar día de descanso real', store=True, copied=True, tracking=0)
#    discount_interes_cesantias = fields.Boolean(string='Descuenta días de suspensión en Intereses Cesantías', store=True, copied=True, tracking=0)
#    discount_oneday_suspension = fields.Boolean(string='Descuento de 1 día en Auxilio para Suspensiones', store=True, copied=True, tracking=0)
#    discount_suspensions = fields.Boolean(string='Descuenta días de suspensión en prima', store=True, copied=True, tracking=0)
#    discount_transport_minimum = fields.Boolean(string='Descuento Auxilio de Transporte por Base Mínima', store=True, copied=True, tracking=0)
#    documents_forbidden_extensions = fields.Char(string='Extensiones', store=True, copied=True, tracking=0)
#    documents_Texto_masize = fields.Integer(string='Tamaño', store=True, copied=True, tracking=0)
#    eps_rate_employee = fields.Float(string='EPS para empleado', store=True, copied=True, tracking=0)
#    eps_rate_employer = fields.Float(string='EPS para empleador', store=True, copied=True, tracking=0)
#    exclude_transport_4060 = fields.Boolean(string='Excluir Subsidio Transporte Tope 40/60', store=True, copied=True, tracking=0)
#    fiscalyear_last_day = fields.Integer(string='Último día año fiscal', required=True, tracking=0)
#    fiscalyear_lock_date = fields.Date(string='Fecha de bloqueo para todos los usuarios', tracking=0)
#    fragmented_holidays = fields.Boolean(string='Vacaciones Fragmentadas', store=True, copied=True, tracking=0)
#    geoloc_provider_googlemap_key = fields.Char(string='Clave de la API de Google Map', store=True, copied=True, tracking=0)
#    geoloc_provider_techname = fields.Char(string='Nombre Técnico', readonly=True, tracking=0)
#    google_drive_authorization_code = fields.Char(string='Código de autorización', store=True, copied=True, tracking=0)
#    google_drive_uri_copy = fields.Char(string='Copia URI', tracking=0)
#    google_drive_uri = fields.Char(string='URI', readonly=True, tracking=0)
#    google_gmail_client_identifier = fields.Char(string='Gmail Client Id', store=True, copied=True, tracking=0)
#    google_gmail_client_secret = fields.Char(string='Gmail Client Secret', store=True, copied=True, tracking=0)
#    group_expiry_date_on_delivery_slip = fields.Boolean(
#        string='Mostrar fecha de caducidad en las notas de remisión',
#        implied_group='product_expiry.group_expiry_date_on_delivery_slip',
#        tracking=0,
#    )
    #group_fiscal_year = fields.Boolean(
    #    string='Ejercicio fiscal',
    #    implied_group='account.group_fiscal_year',
    #    tracking=0,
    #)
#    group_ir_attachment_user = fields.Boolean(
#        string='Acceso central a Documentos',
#        implied_group='base.group_ir_attachment_user',
#        tracking=0,
#    )
#    group_show_line_subtotals_taexcluded = fields.Boolean(
#        string='Mostrar subtotales de línea sin impuestos (B2B)',
#        implied_group='account.group_show_line_subtotals_tax_excluded',
#        tracking=0,
#    )
#    group_show_line_subtotals_taincluded = fields.Boolean(
#        string='Mostrar subtotales de línea con impuestos (B2C)',
#        implied_group='account.group_show_line_subtotals_tax_included',
#        tracking=0,
#    )
#    grouped_name_concept_a = fields.Boolean(string='Agrupación de nombres de conceptos aprendices y salario integral', store=True, copied=True, tracking=0)
#    invoicing_switch_threshold = fields.Date(string='Invoicing Switch Threshold', tracking=0)
#    is_encode_uom_days = fields.Boolean(string='Está codificado en días Uom', readonly=True, tracking=0)
#    is_google_drive_token_generated = fields.Boolean(string='Token de actualización generado', store=True, copied=True, tracking=0)
#    limit_uvt = fields.Boolean(string='Límite de 790uvt Mensuales', store=True, copied=True, tracking=0)
#    mean_salary_cesantia = fields.Boolean(string='Promedio de Salarios en Cesantía', store=True, copied=True, tracking=0)
#    module_account_predictive_bills = fields.Boolean(string='Facturas Predictivas de Cuenta', store=True, copied=True, tracking=0)
#    module_attachment_indexation = fields.Boolean(string='Attachments List and Document Indexation', store=True, copied=True, tracking=0)
#    module_cmis_read = fields.Boolean(string='Attach files from an external DMS into Odoo', store=True, copied=True, tracking=0)
#    module_cmis_write = fields.Boolean(string='Store attachments in an external DMS instead of the Odoo Filestore', store=True, copied=True, tracking=0)
#    module_document_page_approval = fields.Boolean(string='Gestionar aprobación de documentos', store=True, copied=True, tracking=0)
#    module_document_page = fields.Boolean(string='Gestionar páginas de documento (Wiki)', store=True, copied=True, tracking=0)
#    module_project_timesheet_holidays = fields.Boolean(string='Registrar tiempo libre', store=True, copied=True, tracking=0)
#    module_project_timesheet_synchro = fields.Boolean(string='Increíbles partes de horas', store=True, copied=True, tracking=0)
#    nonprofit = fields.Boolean(string='Empresa sin ánimo de lucro', store=True, copied=True, tracking=0)
#    pay_absent_avg_lyear = fields.Boolean(string='Pagar ausentismo con el promedio del último año', store=True, copied=True, tracking=0)
#    pay_ccf_mat_pat = fields.Boolean(string='Cotiza CCF en licencias de MAT o PAT', store=True, copied=True, tracking=0)
#    pay_inability_benefit = fields.Boolean(string='Pago 33.33% incapacidades como beneficio', store=True, copied=True, tracking=0)
#    pay_salary_to_end_holidays = fields.Boolean(string='Paga salario hasta el día final de las vacaciones', store=True, copied=True, tracking=0)
#    pay_volunter_pila = fields.Boolean(string='Pagar Aportes Voluntaria en PILA', store=True, copied=True, tracking=0)
#    payroll_filter_analityc_account = fields.Boolean(string='Filtrar cuentas analíticas por ciudad al causar nómina', store=True, copied=True, tracking=0)
#    pays_atep_b1_with_wage = fields.Boolean(string='Paga 1 día de accidente de trabajo - enfermedad profesional con salario', store=True, copied=True, tracking=0)
#    pays_eg_b2_with_wage = fields.Boolean(string='Paga 1-2 días de incapacidad de enfermedad general con salario', store=True, copied=True, tracking=0)
#    pays_sub_trans_train_prod = fields.Boolean(string='Paga subsidio de transporte a aprendices en etapa productiva', store=True, copied=True, tracking=0)
#    pen_rate_employee = fields.Float(string='Pensión para empleado', store=True, copied=True, tracking=0)
#    pen_rate_employer = fields.Float(string='Pensión para empleador', store=True, copied=True, tracking=0)
#    percentage_advance_payment = fields.Float(string='Porcentaje Pago Anticipado', store=True, copied=True, tracking=0)
#    period_lock_date = fields.Date(string='Fecha establecida para no asesores', tracking=0)
#    projected_withholding_tax = fields.Boolean(string='Retención en la fuente proyectada', store=True, copied=True, tracking=0)
#    provision_payslip_electronic = fields.Boolean(string='Provisión de Prestaciones en Nómina Electrónica', store=True, copied=True, tracking=0)
#    rest_paid_same_biweekly = fields.Boolean(string='Descanso remunerado en la misma quincena', store=True, copied=True, tracking=0)
#    restringir_programaciones = fields.Boolean(string='Saltar restricciones en programación?', store=True, copied=True, tracking=0)
#    rtf_projection = fields.Boolean(string='Cálculo de retención en la fuente proyectada en primera quincena', store=True, copied=True, tracking=0)
#    rtf_round = fields.Boolean(string='Redondeo de retención en la fuente', store=True, copied=True, tracking=0)
#    separate_concept = fields.Boolean(string='Separar concepto en porcentaje', store=True, copied=True, tracking=0)
#    sh_auto_add_customer_as_follower = fields.Boolean(string='¿Agregar automáticamente al cliente como seguidor cuando crea Ticket?', tracking=0)
#    sh_configure_activate = fields.Boolean(string='Administrar productos', tracking=0)
#    sh_customer_replied = fields.Boolean(string='¿Cambio en la etapa cuando el cliente respondió?', tracking=0)
#    sh_default_description = fields.Boolean(string='Descripción predeterminada en la hoja de tiempo?', tracking=0)
#    sh_display_in_chatter = fields.Boolean(string='Mostrar en el mensaje de charla?', tracking=0)
#    sh_display_multi_user = fields.Boolean(string='Mostrar múltiples usuarios?', tracking=0)
#    sh_display_ticket_reminder = fields.Boolean(string='¿Recordatorio de tickets?', tracking=0)
#    sh_file_size = fields.Integer(string='Tamaño del accesorio del portal (KB)', tracking=0)
#    sh_multiple_ticket_allowed = fields.Boolean(string='¿Se permiten múltiples tickets?', tracking=0)
#    sh_pdf_in_message = fields.Boolean(string='¿Enviar URL de informe en el mensaje?', tracking=0)
#    sh_receive_email_seeing_ticket = fields.Boolean(string='¿Recibe correo electrónico cuando el cliente ve el ticket?', tracking=0)
#    sh_signature = fields.Boolean(string='¿Firma?', tracking=0)
#    sh_staff_replied = fields.Boolean(string='¿Cambio en el escenario cuando respondió el personal?', tracking=0)
#    sh_ticket_product_detail = fields.Boolean(string='¿Detalles del producto del ticket en el mensaje?', tracking=0)
#    sh_ticket_url_in_message = fields.Boolean(string='¿Enviar URL de tickets en el mensaje?', tracking=0)
#    simple_provisions = fields.Boolean(string='Cálculo de provisiones simple', store=True, copied=True, tracking=0)
#    sub_category = fields.Boolean(string='Subcategoría', tracking=0)
#    taexigibility = fields.Boolean(string='Base del Efectivo', tracking=0)
#    talock_date = fields.Date(string='Fecha de bloqueo de impuestos', tracking=0)
#    timesheet_min_duration = fields.Integer(string='Duración mínima', store=True, copied=True, tracking=0)
#    timesheet_rounding = fields.Integer(string='Redondear', store=True, copied=True, tracking=0)
#    totals_below_sections = fields.Boolean(string='Add totals below sections', tracking=0)
#    unique_payslip_period = fields.Boolean(string='Única nómina por período', store=True, copied=True, tracking=0)
#    use_anglo_saxon = fields.Boolean(string='Contabilidad anglo-sajona', tracking=0)
#    vacation_differential = fields.Boolean(string='Vacaciones Diferenciales', store=True, copied=True, tracking=0)
#    vacation_money = fields.Boolean(string='Pago de dinero por vacaciones', store=True, copied=True, tracking=0)
#    vacation_without_ingress = fields.Boolean(string='Provisión de Vacación sin Ingreso Complementario', store=True, copied=True, tracking=0)
#    vat_check_vies = fields.Boolean(string='Verificar números de identificación fiscal (NIF)', tracking=0)

class ResCountry(models.Model):
    _inherit = 'res.country'
    enforce_cities = fields.Boolean(string='Forzar ciudades', store=True, copied=True, tracking=0)
    kactus = fields.Char(string='Código Kactus', store=True, copied=True, tracking=1)

class ResCountryState(models.Model):
    _inherit = 'res.country.state'
    kactus = fields.Char(string='Código Kactus', store=True, copied=True, tracking=1)
    numeric_code = fields.Char(string='Código Numérico', store=True, copied=True, tracking=0)

class ResCurrencyRate(models.Model):
    _inherit = 'res.currency.rate'
    rate_inv = fields.Float(string='Tasa Inversa', tracking=0)

class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'
    cupo_endeudamiento = fields.Float(string='Cupo de endeudamiento', store=True, copied=True, tracking=0)
    date_renovacion = fields.Date(string='Fecha de renovación de cupo', store=True, copied=True, tracking=0)
    oficina_nombre = fields.Char(string='Nombre de la oficina', store=True, copied=True, tracking=0)

class ResPartnerDocumentType(models.Model):
    _name = 'res.partner.document.type'
    _description = 'Tipos de documentos de socios'

    code_dian = fields.Char(string='Código DIAN', store=True, copied=True, tracking=0)
    code = fields.Char(string='Código', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    no_validar_nit = fields.Boolean(string='No validar NIT', store=True, copied=True, tracking=0)

class ResPartnerDriver(models.Model):
    _name = 'res.partner.driver'
    _description = 'Conductores de socios'

    comment = fields.Text(string='Comentario', store=True, copied=True, tracking=0)
    mobile = fields.Char(string='Celular', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    plate = fields.Char(string='Placa', store=True, copied=True, tracking=0)
    vat = fields.Char(string='NIT', store=True, copied=True, tracking=0)

class ResPartnerIdCategory(models.Model):
    _name = 'res.partner.id.category'
    _description = 'Categorías de identificación de socios'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0)
    code = fields.Char(string='Código', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre ID', store=True, required=True, copied=True, tracking=0)
    validation_code = fields.Text(string='Código de validación Python', store=True, copied=True, tracking=0)

class ResPartnerIdNumber(models.Model):
    _name = 'res.partner.id.number'
    _description = 'Números de identificación de socios'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0)
    activo = fields.Boolean(string='Cliente Activo', store=True, readonly=True, tracking=0)
    adjunto_bin = fields.Text(string='Soporte', store=True, copied=True, tracking=0)
    adjunto_id = fields.Char(string='Id Soporte', readonly=True, tracking=0)
    auxiliar_file_url = fields.Char(string='Url Soporte', store=True, readonly=True, tracking=0)
    comment = fields.Text(string='Notas', store=True, copied=True, tracking=0)
    customer = fields.Boolean(string='Es Cliente', readonly=True, tracking=0)
    date_issued = fields.Date(string='Emitido en', store=True, copied=True, tracking=0)
    name = fields.Char(string='Número ID', store=True, required=True, copied=True, tracking=0)
    PD473416478822277 = fields.Text(string='Adjunto', store=True, copied=True, tracking=0)
    place_issuance = fields.Char(string='Lugar de emisión', store=True, copied=True, tracking=0)
    supplier = fields.Boolean(string='Es Proveedor', tracking=0)
    valid_from = fields.Date(string='Válido desde', store=True, copied=True, tracking=0)
    valid_until = fields.Date(string='Válido hasta', store=True, copied=True, tracking=0)

class ResPartnerPaymentActionType(models.Model):
    _name = 'res.partner.payment.action.type'
    _description = 'Tipos de acciones de pago de socios'

    active = fields.Boolean(string='Activa', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)
    sequence = fields.Integer(string='Sequence', store=True, copied=True, tracking=0)

class ResRegional(models.Model):
    _name = 'res.regional'
    _description = 'Regionales'

    kactus = fields.Char(string='Código Kactus', store=True, copied=True, tracking=1)
    name = fields.Char(string='Regional', store=True, copied=True, tracking=0)

class ResUsers(models.Model):
    _inherit = 'res.users'
    google_calendar_cal_id = fields.Char(string='ID del calendario', store=True, tracking=0)
    google_calendar_rtoken = fields.Char(string='Token de actualización', store=True, tracking=0)
    google_calendar_sync_token = fields.Char(string='Siguiente sincronización de token', store=True, tracking=0)
    google_calendar_token_validity = fields.Datetime(string='Validez del token', store=True, tracking=0)
    google_calendar_token = fields.Char(string='Token de usuario', store=True, tracking=0)
    grant_portal = fields.Boolean(string='Grant Portal', store=True, copied=True, tracking=0)
    sh_portal_user = fields.Boolean(string='Portal', readonly=True, tracking=0)
    sign = fields.Text(string='Firma', store=True, copied=True, tracking=0)
    user_signature = fields.Text(string='Firma Usuario', store=True, copied=True, tracking=0)

class ResUsersApikeys(models.Model):
    _inherit = 'res.users.apikeys'
    sign = fields.Text(string='Firma', store=True, copied=True, tracking=0)

class ResWeekday(models.Model):
    _name = 'res.weekday'
    _description = 'Días de la semana'

    day_index = fields.Integer(string='Índice de día', readonly=True, tracking=0)
    habil = fields.Boolean(string='Día hábil', store=True, copied=True, tracking=0)
    name = fields.Char(string='Día de la semana', store=True, copied=True, tracking=0)

class ReturnChangeDifference(models.Model):
    _name = 'return.change.difference'
    _description = 'Diferencias de devolución y cambio'

    date = fields.Date(string='Fecha de Contabilización', store=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'
    date_end_invoice_timesheet = fields.Date(string='Fecha final', store=True, copied=True, tracking=0)
    date_start_invoice_timesheet = fields.Date(string='Fecha de inicio', store=True, copied=True, tracking=0)
    invoicing_timesheet_enabled = fields.Boolean(string='Habilitada facturación hojas de horas', store=True, copied=True, tracking=0)

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    customer_po_file = fields.Text(string='Orden de Compra Cliente', store=True, tracking=0)
    customer_po_name = fields.Char(string='Nombre OC Cliente', store=True, tracking=0)
    customer_po_policy = fields.Boolean(string='Política Envío OC', readonly=True, tracking=0)
    delivery_message = fields.Char(string='Mensaje de entrega', store=True, readonly=True, tracking=0)
    delivery_rating_success = fields.Boolean(string='Promedio de éxito en entregas', store=True, tracking=0)
    delivery_set = fields.Boolean(string='Entrega establecida', readonly=True, tracking=0)
    eq_utilidades = fields.Float(string='Utilidad EQ', store=True, copied=True, tracking=0)
    imp_utilidades = fields.Float(string='Utilidad IMP', store=True, copied=True, tracking=0)
    is_all_service = fields.Boolean(string='Producto: servicio', readonly=True, tracking=0)
    mo_utilidades = fields.Float(string='Utilidad M.O', store=True, copied=True, tracking=0)
    recompute_delivery_price = fields.Boolean(string='El coste de envío debería ser recalculado', store=True, copied=True, tracking=0)
    rentabilidad_de_venta_porcentaje = fields.Float(string='%', store=True, readonly=True, tracking=1)
    rentabilidad_de_venta = fields.Float(string='Rentabilidad de Venta', store=True, readonly=True, tracking=1)
    sale_ticket_count = fields.Integer(string='Tickets', readonly=True, tracking=0)
    service_order = fields.Boolean(string='Ver orden de servicio', readonly=True, tracking=0)
    timesheet_count = fields.Float(string='Actividades del parte de horas', readonly=True, tracking=0)
    timesheet_total_duration = fields.Integer(string='Duración total del parte de horas', readonly=True, tracking=0)

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    authorized_transaction_ids = fields.Char(string='Transacciones autorizadas', store=True, copied=True, tracking=0)
    compute_val = fields.Float(string='Valor calculado', store=True, copied=True, tracking=0)
    is_delivery = fields.Boolean(string='Es un envío', store=True, copied=True, tracking=0)
    location = fields.Char(string='Ubicación', store=True, copied=True, tracking=0)
    marca_variante_sale_order = fields.Text(string='Marca', store=True, copied=True, tracking=1)
    no_cost = fields.Boolean(string='Sin Costo', store=True, copied=True, tracking=0)
    precio_original = fields.Float(string='necesario.para.mo.utilidades.no.visible', store=True, copied=True, tracking=0)
    product_qty = fields.Float(string='Cant. producto', readonly=True, tracking=0)
    recompute_delivery_price = fields.Boolean(string='El coste de envío debería ser recalculado', readonly=True, tracking=0)
    remaining_hours_available = fields.Boolean(string='Remaining Hours Available', readonly=True, tracking=0)
    remaining_hours = fields.Float(string='Remaining Hours on SO', readonly=True, tracking=0)
    use_parent_modality = fields.Boolean(string='Usa modalidad padre', readonly=True, tracking=0)

class SaleOrderTemplate(models.Model):
    _inherit = 'sale.order.template'
    condiciones_comerciales = fields.Text(string='Condiciones Comerciales', store=True, copied=True, tracking=1)
    descripcion_de_la_propuesta = fields.Text(string='Descripción de la Propuesta', store=True, copied=True, tracking=1)
    precio_total_acumulado = fields.Float(string='Total Valor Cotización', store=True, copied=True, tracking=1)
    trm = fields.Float(string='TRM', store=True, copied=True, tracking=1)

class SaleOrderTemplateLine(models.Model):
    _inherit = 'sale.order.template.line'
    item = fields.Integer(string='ITEM', store=True, readonly=True, copied=True, tracking=1)
    marca_variante_enlace_1 = fields.Text(string='Marca de la Variante', store=True, copied=True, tracking=1)
    precio_v = fields.Float(string='Precio de Venta', store=True, copied=True, tracking=1)
    valor_imp = fields.Float(string='Valor Importación', store=True, copied=True, tracking=1)

class SaleQuoterStage(models.Model):
    _name = 'sale.quoter.stage'
    _description = 'Etapas de cotizaciones de ventas'

    bool_generate_quoter = fields.Boolean(string='Generar cotización', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class SearchAvailableEmployee(models.Model):
    _name = 'search.available.employee'
    _description = 'Búsqueda de empleados disponibles'

    end_date = fields.Datetime(string='Fecha fin', store=True, required=True, copied=True, tracking=0)
    start_date = fields.Datetime(string='Fecha inicio', store=True, required=True, copied=True, tracking=0)

class SecurityCourseType(models.Model):
    _name = 'security.course.type'
    _description = 'Tipos de cursos de seguridad'

    code = fields.Char(string='Código', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, readonly=True, tracking=0)
    type = fields.Char(string='Curso', store=True, required=True, copied=True, tracking=0)

class Sedes(models.Model):
    _name = 'sedes'
    _description = 'Sedes'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    calcula = fields.Char(string='fila', tracking=1)
    direccion = fields.Char(string='Dirección', store=True, copied=True, tracking=1)
    fecha_fin = fields.Date(string='Fecha Fin', store=True, copied=True, tracking=1)
    fecha_inicio = fields.Date(string='Fecha de Inicio', store=True, copied=True, tracking=1)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Id Sede', store=True, tracking=1)
    nombre_sede = fields.Char(string='Nombre Sede', store=True, copied=True, tracking=1)
    sequence = fields.Integer(string='Secuencia', store=True, tracking=1)

class ServiceOrderLineSecuence(models.Model):
    _name = 'service.order.line.secuence'
    _description = 'Secuencias de líneas de órdenes de servicio'

    secuence = fields.Integer(string='secuencia', store=True, copied=True, tracking=0)

class Servicios(models.Model):
    _name = 'servicios'
    _description = 'Servicios'

    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)

class ServiciosAdicionalesTurnos(models.Model):
    _name = 'servicios.adicionales.turnos'
    _description = 'Servicios adicionales de turnos'

    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)

class SeveranceUpdateHistory(models.Model):
    _name = 'severance.update.history'
    _description = 'Historial de actualización de cesantías'

    date = fields.Date(string='Fecha', store=True, required=True, copied=True, tracking=0)

class ShHelpdeskSla(models.Model):
    _name = 'sh.helpdesk.sla'
    _description = 'SLA de helpdesk'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)
    sh_days = fields.Integer(string='Días', store=True, required=True, copied=True, tracking=0)
    sh_hours = fields.Integer(string='Horas', store=True, required=True, copied=True, tracking=0)
    sh_minutes = fields.Integer(string='Minutos', store=True, required=True, copied=True, tracking=0)
    sla_ticket_count = fields.Integer(string='Recuento de tickets de SLA', readonly=True, tracking=0)

class ShHelpdeskSlaStatus(models.Model):
    _name = 'sh.helpdesk.sla.status'
    _description = 'Estados de SLA de helpdesk'

    color = fields.Integer(string='Índice de color', readonly=True, tracking=0)
    sh_deadline = fields.Datetime(string='Fecha límite de SLA', store=True, readonly=True, tracking=0)
    sh_done_sla_date = fields.Datetime(string='Sla Fecha de hecho', store=True, copied=True, tracking=0)

class ShHelpdeskTicketMassUpdateWizard(models.Model):
    _name = 'sh.helpdesk.ticket.mass.update.wizard'
    _description = 'Asistente de actualización masiva de tickets de helpdesk'

    check_add_remove = fields.Boolean(string='Agregar eliminar', store=True, copied=True, tracking=0)
    check_assign_to_multiuser = fields.Boolean(string='Asignar múltiples usuarios', store=True, copied=True, tracking=0)
    check_assign_to = fields.Boolean(string='Avisar a', store=True, copied=True, tracking=0)
    check_helpdesks_state = fields.Boolean(string='Escenario', store=True, copied=True, tracking=0)
    check_sh_display_multi_user = fields.Boolean(string='Verifique SH Display Multi User', store=True, copied=True, tracking=0)

class ShHelpdeskTicketMergeTicketWizard(models.Model):
    _name = 'sh.helpdesk.ticket.merge.ticket.wizard'
    _description = 'Asistente de fusión de tickets de helpdesk'

    sh_check_multi_user = fields.Boolean(string='sh.check.multi.user', store=True, copied=True, tracking=0)
    sh_merge_history = fields.Boolean(string='Historia de fusiones', store=True, copied=True, tracking=0)

class ShHelpdeskTicketStageInfo(models.Model):
    _name = 'sh.helpdesk.ticket.stage.info'
    _description = 'Información de etapas de tickets de helpdesk'

    date_in = fields.Datetime(string='Date In', store=True, copied=True, tracking=0)
    date_out = fields.Datetime(string='Date Out', store=True, copied=True, tracking=0)
    day_diff = fields.Integer(string='Day Diff', store=True, copied=True, tracking=0)
    stage_name = fields.Char(string='Stage Name', store=True, copied=True, tracking=0)
    time_diff = fields.Float(string='Time Diff', store=True, copied=True, tracking=0)
    total_time_diff = fields.Float(string='Total Time Diff', store=True, copied=True, tracking=0)

class ShQuickReply(models.Model):
    _name = 'sh.quick.reply'
    _description = 'Respuestas rápidas'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=0)
    commom_for_all = fields.Boolean(string='Común para todos', store=True, copied=True, tracking=0)
    name = fields.Char(string='Título', store=True, required=True, copied=True, tracking=0)
    sh_description = fields.Html(string='Cuerpo', store=True, copied=True, tracking=0)

class ShTicketAlarm(models.Model):
    _name = 'sh.ticket.alarm'
    _description = 'Alarmas de tickets'

    name = fields.Char(string='Nombre', store=True, readonly=True, copied=True, tracking=0)
    sh_remind_before = fields.Integer(string='Recordatorio antes', store=True, copied=True, tracking=0)

class StockLandedCost(models.Model):
    _name = 'stock.landed.cost'
    _description = 'Costos de aterrizaje de inventario'

    activity_date_deadline = fields.Date(string='Siguiente plazo de actividad', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Resumen de la siguiente actividad', tracking=0)
    activity_type_icon = fields.Char(string='Ícono de tipo de actividad', readonly=True, tracking=0)
    date = fields.Date(string='Fecha', store=True, required=True, tracking=100)
    description = fields.Text(string='Descripción del Elemento', store=True, copied=True, tracking=0)
    message_attachment_count = fields.Integer(string='Nº de archivos adjuntos', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Número de errores', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Error de Envío de Mensaje', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='Error de entrega del SMS', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Es un seguidor', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Acción requerida', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Nº de mensajes sin leer', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Mensajes sin leer', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='Mi fecha límite de actividad', readonly=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, readonly=True, tracking=100)

class StockLandedCostLines(models.Model):
    _name = 'stock.landed.cost.lines'
    _description = 'Líneas de costos de aterrizaje de inventario'

    name = fields.Char(string='Descripción', store=True, copied=True, tracking=0)

class StockMove(models.Model):
    _inherit = 'stock.move'
    create_asset = fields.Boolean(string='Activo Creado', store=True, copied=True, tracking=0)
    price_total = fields.Float(string='Precio Total', store=True, readonly=True, tracking=0)
    qty_done = fields.Float(string='Cantidad hecha', tracking=0)
    use_expiration_date = fields.Boolean(string='Usar fecha de caducidad', readonly=True, tracking=0)
    weight = fields.Float(string='Peso', store=True, readonly=True, tracking=0)

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'
    expiration_date = fields.Datetime(string='Fecha de caducidad', store=True, readonly=True, tracking=0)
    sale_price = fields.Float(string='Precio de venta', readonly=True, tracking=0)

class StockPackageLevel(models.Model):
    _inherit = 'stock.package_level'
    is_done = fields.Boolean(string='Terminado', tracking=0)
    is_fresh_package = fields.Boolean(string='Es un paquete fresco', readonly=True, tracking=0)
    show_lots_m2o = fields.Boolean(string='Mostrar Lotes M2O', readonly=True, tracking=0)
    show_lots_text = fields.Boolean(string='Mostrar texto de lotes', readonly=True, tracking=0)

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    carrier_price = fields.Float(string='Coste de envío', store=True, copied=True, tracking=0)
    carrier_tracking_ref = fields.Char(string='Número de seguimiento', store=True, tracking=0)
    carrier_tracking_url = fields.Char(string='URL para seguimiento', readonly=True, tracking=0)
    dotacion_end_date = fields.Date(string='Fecha final', store=True, copied=True, tracking=0)
    dotacion_start_date = fields.Date(string='Fecha de inicio', store=True, copied=True, tracking=0)
    driver_plate = fields.Char(string='Placa', store=True, copied=True, tracking=0)
    is_dotation = fields.Boolean(string='Dotación', store=True, copied=True, tracking=0)
    is_refund = fields.Boolean(string='Reintegro', store=True, copied=True, tracking=0)
    is_return_picking = fields.Boolean(string='Devolución para recolección', readonly=True, tracking=0)
    print_date = fields.Date(string='Fecha de Impresión', store=True, tracking=0)
    print_remission = fields.Char(string='Número Remisión', store=True, copied=True, tracking=0)
    ref_num = fields.Char(string='Número de identificación', readonly=True, tracking=0)
    shipping_weight = fields.Float(string='Peso para envío', readonly=True, tracking=0)
    to_puesto = fields.Boolean(string='Asignación puesto', store=True, copied=True, tracking=0)
    user_signature = fields.Text(string='Firma Usuario', store=True, tracking=0)
    weight_bulk = fields.Float(string='Peso a granel', readonly=True, tracking=0)
    weight_uom_name = fields.Char(string='Etiqueta de unidad de medida de peso', readonly=True, tracking=0)
    weight = fields.Float(string='Peso', store=True, readonly=True, tracking=0)

class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'
    alert_date = fields.Datetime(string='Fecha de Alerta', store=True, copied=True, tracking=0)
    expiration_date = fields.Datetime(string='Fecha de caducidad', store=True, copied=True, tracking=0)
    product_expiry_alert = fields.Boolean(string='Alerta de caducidad del producto', readonly=True, tracking=0)
    product_expiry_reminded = fields.Boolean(string='Se ha recordado el vencimiento', store=True, copied=True, tracking=0)
    removal_date = fields.Datetime(string='Fecha de Eliminación', store=True, copied=True, tracking=0)
    use_date = fields.Datetime(string='Consumir preferentemente antes de', store=True, copied=True, tracking=0)
    use_expiration_date = fields.Boolean(string='Usar fecha de caducidad', readonly=True, tracking=0)

class StockQuant(models.Model):
    _inherit = 'stock.quant'
    price_total = fields.Float(string='Precio Total', store=True, readonly=True, tracking=0)
    price_unit = fields.Float(string='Precio unitario', store=True, readonly=True, tracking=0)
    removal_date = fields.Datetime(string='Fecha de Eliminación', store=True, tracking=0)
    use_expiration_date = fields.Boolean(string='Fecha de caducidad', readonly=True, tracking=0)

class StockQuantPackage(models.Model):
    _inherit = 'stock.quant.package'
    shipping_weight = fields.Float(string='Peso del envío', store=True, copied=True, tracking=0)
    weight_uom_name = fields.Char(string='Etiqueta de unidad de medida de peso', readonly=True, tracking=0)
    weight = fields.Float(string='Peso', readonly=True, tracking=0)

class StockReportKardedotLine(models.Model):
    _name = 'stock.report.kardedot.line'
    _description = 'Líneas de reporte de kardex de dotaciones'

    date_dot_f = fields.Datetime(string='Fecha Dotación Final', store=True, copied=True, tracking=0)
    date_dot_i = fields.Datetime(string='Fecha Dotación Inicial', store=True, copied=True, tracking=0)
    date = fields.Datetime(string='Fecha', store=True, copied=True, tracking=0)
    doc_orig = fields.Char(string='Documento Origen', store=True, copied=True, tracking=0)
    dot_ret = fields.Char(string='DOT/RET', store=True, copied=True, tracking=0)
    num_ced = fields.Char(string='Cédula', store=True, copied=True, tracking=0)
    qty = fields.Float(string='Cantidad', store=True, copied=True, tracking=0)
    type_move = fields.Char(string='Tipo de movimiento', store=True, copied=True, tracking=0)

class StockReportKardedotWizard(models.Model):
    _name = 'stock.report.kardedot.wizard'
    _description = 'Asistente de reporte de kardex de dotaciones'

    date_end = fields.Datetime(string='Fecha Final', store=True, required=True, copied=True, tracking=0)
    date_start = fields.Datetime(string='Fecha Inicial', store=True, required=True, copied=True, tracking=0)
    employees = fields.Boolean(string='Varios Empleados', store=True, copied=True, tracking=0)

class StockReportKardeline(models.Model):
    _name = 'stock.report.kardeline'
    _description = 'Líneas de reporte de kardex'

    cost_move = fields.Float(string='Costo Unitario Movimiento', store=True, copied=True, tracking=0)
    cost_promedio_total = fields.Float(string='Costo Valorizado', store=True, copied=True, tracking=0)
    cost_promedio = fields.Float(string='Costo Promedio', store=True, copied=True, tracking=0)
    cost_total_move = fields.Float(string='Costo Total Movimiento', store=True, copied=True, tracking=0)
    date = fields.Datetime(string='Fecha', store=True, copied=True, tracking=0)
    default_code = fields.Char(string='Referencia Interna', store=True, copied=True, tracking=0)
    location_dest_id = fields.Char(string='Ubicación Destino', store=True, copied=True, tracking=0)
    location_id = fields.Char(string='Ubicación Origen', store=True, copied=True, tracking=0)
    name = fields.Char(string='Documento Referencia', store=True, copied=True, tracking=0)
    origin = fields.Char(string='Documento Origen', store=True, copied=True, tracking=0)
    product_name = fields.Char(string='Descripción', store=True, copied=True, tracking=0)
    qty_end = fields.Float(string='Saldo Final', store=True, copied=True, tracking=0)
    qty_in = fields.Float(string='Entrada', store=True, copied=True, tracking=0)
    qty_out = fields.Float(string='Salida', store=True, copied=True, tracking=0)
    qty_start = fields.Float(string='Saldo Inicial', store=True, copied=True, tracking=0)
    qty = fields.Float(string='Interno', store=True, copied=True, tracking=0)
    type_move = fields.Char(string='Tipo de movimiento', store=True, copied=True, tracking=0)

class StockReportKardewizard(models.Model):
    _name = 'stock.report.kardewizard'
    _description = 'Asistente de reporte de kardex'

    date_end = fields.Datetime(string='Fecha Final', store=True, required=True, copied=True, tracking=0)
    date_start = fields.Datetime(string='Fecha Inicial', store=True, required=True, copied=True, tracking=0)
    title = fields.Char(string='títulos', store=True, copied=True, tracking=0)

class StockReportSqlGroupLocation(models.Model):
    _name = 'stock.report.sql.group.location'
    _description = 'Grupos de ubicación de reporte de stock'

    name = fields.Char(string='Name', store=True, required=True, copied=True, tracking=0)

class StockValuationAdjustmentLines(models.Model):
    _name = 'stock.valuation.adjustment.lines'
    _description = 'Líneas de ajuste de valoración de stock'

    name = fields.Char(string='Descripción', store=True, readonly=True, tracking=0)
    quantity = fields.Float(string='Cantidad', store=True, required=True, copied=True, tracking=0)
    volume = fields.Float(string='Volumen', store=True, copied=True, tracking=0)
    weight = fields.Float(string='Peso', store=True, copied=True, tracking=0)

class StockWarehouseOrderpoint(models.Model):
    _inherit = 'stock.warehouse.orderpoint'
    product_maqty = fields.Float(string='Cantidad máxima', store=True, required=True, copied=True, tracking=0)

class StudioApprovalDetails(models.Model):
    _name = 'studio.approval.details'
    _description = 'Detalles de aprobación de Studio'

    date_accepted = fields.Datetime(string='Date Accepted', store=True, copied=True, tracking=0)
    res_id = fields.Integer(string='Record Id', store=True, copied=True, tracking=0)

class StudioApprovalRule(models.Model):
    _name = 'studio.approval.rule'
    _description = 'Reglas de aprobación de Studio'

    description = fields.Char(string='Description', store=True, copied=True, tracking=0)

class StudioButton(models.Model):
    _name = 'studio.button'
    _description = 'Botones de Studio'

    name = fields.Char(string='Button Id', store=True, copied=True, tracking=0)

class StudioViewCenter(models.Model):
    _name = 'studio.view.center'
    _description = 'Centro de vistas de Studio'

    arch = fields.Text(string='Arch', store=True, copied=True, tracking=0)
    field_name = fields.Char(string='Field Name', store=True, copied=True, tracking=0)
    view_key = fields.Char(string='View Key', store=True, copied=True, tracking=0)
    views_order = fields.Char(string='Views Order', store=True, copied=True, tracking=0)

class SubcategoriaFlujoCajaVise(models.Model):
    _name = 'subcategoria.flujo.caja.vise'
    _description = 'Subcategorías de flujo de caja'

    activity_date_deadline = fields.Date(string='Siguiente plazo de actividad', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Resumen de la siguiente actividad', tracking=0)
    activity_type_icon = fields.Char(string='Ícono de tipo de actividad', readonly=True, tracking=0)
    message_attachment_count = fields.Integer(string='Nº de archivos adjuntos', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Número de errores', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Error de Envío de Mensaje', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='Error de entrega del SMS', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Es un seguidor', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Acción requerida', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Nº de mensajes sin leer', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Mensajes sin leer', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='Mi fecha límite de actividad', readonly=True, tracking=0)
    name = fields.Char(string='Subcategoría', store=True, copied=True, tracking=0)
    PD4381219024334353 = fields.Integer(string='Código', store=True, copied=True, tracking=0)

class SubMotivoProcesosDisciplinarios(models.Model):
    _name = 'sub.motivo.procesos.disciplinarios'
    _description = 'Submotivos de procesos disciplinarios'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    name = fields.Char(string='Sub Motivo', store=True, required=True, copied=True, tracking=1)

class SurveyQuestion(models.Model):
    _inherit = 'survey.question'
    validation_madate = fields.Date(string='Fecha Máxima', store=True, copied=True, tracking=0)
    validation_madatetime = fields.Datetime(string='Fecha y hora máxima', store=True, copied=True, tracking=0)
    validation_mafloat_value = fields.Float(string='Valor máximo', store=True, copied=True, tracking=0)

class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'
    access_token = fields.Char(string='Token de identificación', store=True, readonly=True, required=True, tracking=0)
    attempts_limit = fields.Integer(string='Número de intentos', readonly=True, tracking=0)
    attempts_number = fields.Integer(string='Intento n°', readonly=True, tracking=0)
    deadline = fields.Datetime(string='Fecha límite', store=True, copied=True, tracking=0)
    email = fields.Char(string='Correo', store=True, readonly=True, copied=True, tracking=0)
    invite_token = fields.Char(string='Token de acceso', store=True, readonly=True, tracking=0)
    is_attempts_limited = fields.Boolean(string='Número limitado de intentos', readonly=True, tracking=0)
    is_session_answer = fields.Boolean(string='Está en una sesión', store=True, copied=True, tracking=0)
    nickname = fields.Char(string='Apodo', store=True, copied=True, tracking=0)
    question_time_limit_reached = fields.Boolean(string='Límite de tiempo de preguntas alcanzado', readonly=True, tracking=0)
    scoring_percentage = fields.Float(string='Calificación (%)', store=True, readonly=True, tracking=0)
    scoring_success = fields.Boolean(string='Prueba aprobada', store=True, readonly=True, tracking=0)
    scoring_total = fields.Float(string='Puntuación Total', store=True, readonly=True, tracking=0)
    start_datetime = fields.Datetime(string='Fecha y hora de inicio', store=True, readonly=True, copied=True, tracking=0)
    survey_time_limit_reached = fields.Boolean(string='Se alcanzó el límite de tiempo de la encuesta', readonly=True, tracking=0)
    test_entry = fields.Boolean(string='Entrada de prueba', store=True, readonly=True, copied=True, tracking=0)


class SurveyUserInputLine(models.Model):
    _inherit = 'survey.user_input.line'
    answer_is_correct = fields.Boolean(string='Correcto', store=True, copied=True, tracking=0)
    answer_score = fields.Float(string='Puntuación', store=True, copied=True, tracking=0)
    question_sequence = fields.Integer(string='Secuencia', store=True, readonly=True, tracking=0)
    skipped = fields.Boolean(string='Omitida', store=True, copied=True, tracking=0)
    value_char_box = fields.Char(string='Respuesta de texto', store=True, copied=True, tracking=0)
    value_date = fields.Date(string='Fecha de respuesta', store=True, copied=True, tracking=0)
    value_datetime = fields.Datetime(string='Respuesta de fecha y hora', store=True, copied=True, tracking=0)
    value_numerical_box = fields.Float(string='Respuesta numérica', store=True, copied=True, tracking=0)
    value_text_box = fields.Text(string='Respuesta de Text Libre', store=True, copied=True, tracking=0)

class TaadjustmentsWizard(models.Model):
    _name = 'ta.adjustments.wizard'
    _description = 'Asistente de ajustes de impuestos'

    date = fields.Date(string='Fecha', store=True, required=True, copied=True, tracking=0)
    reason = fields.Char(string='Justificación', store=True, required=True, copied=True, tracking=0)

class Tags(models.Model):
    _name = 'tags'
    _description = 'Etiquetas'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    calcula = fields.Char(string='Calcula', store=True, copied=True, tracking=1)
    name = fields.Char(string='Solicitud', store=True, copied=True, tracking=1)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=1)

class TarifarioWiz(models.Model):
    _name = 'tarifario.wiz'
    _description = 'Asistente de tarifario'

    fecha_cierre = fields.Date(string='Fecha de cierre', store=True, required=True, copied=True, tracking=0)
    from_close = fields.Boolean(string='Creado desde Cierre', store=True, copied=True, tracking=0)

class TemplateReportContract(models.Model):
    _name = 'template.report.contract'
    _description = 'Plantillas de reportes de contratos'

    codes_print = fields.Text(string='Campos usables', readonly=True, tracking=0)
    description = fields.Html(string='Descripción', store=True, copied=True, tracking=0)
    footer_section = fields.Html(string='Pie de Página', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class Tesoreria(models.Model):
    _name = 'tesoreria'
    _description = 'Tesorería'

    activity_date_deadline = fields.Date(string='Siguiente plazo de actividad', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icono', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Resumen de la siguiente actividad', tracking=0)
    activity_type_icon = fields.Char(string='Ícono de tipo de actividad', readonly=True, tracking=0)
    message_attachment_count = fields.Integer(string='Nº de archivos adjuntos', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Número de errores', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Error de Envío de Mensaje', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='Error de entrega del SMS', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Es un seguidor', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Número de acciones', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Acción requerida', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Nº de mensajes sin leer', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Mensajes sin leer', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='Mi fecha límite de actividad', readonly=True, tracking=0)
    name = fields.Char(string='Name', store=True, copied=True, tracking=0)

class TicketDashboard(models.Model):
    _name = 'ticket.dashboard'
    _description = 'Tablero de tickets'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class TicketTimeAccountLine(models.Model):
    _name = 'ticket.time.account.line'
    _description = 'Líneas de tiempo de tickets'

    duration = fields.Float(string='Duración (HH: MM)', store=True, readonly=True, copied=True, tracking=0)
    end_date = fields.Datetime(string='Fecha final', store=True, readonly=True, copied=True, tracking=0)
    name = fields.Text(string='Descripción', store=True, required=True, copied=True, tracking=0)
    start_date = fields.Datetime(string='Fecha de inicio', store=True, readonly=True, copied=True, tracking=0)

class TipoDuracionEstudiosCapacitaciones(models.Model):
    _name = 'tipo.duracion.estudios.capacitaciones'
    _description = 'Tipos de duración de estudios y capacitaciones'

    name = fields.Char(string='Tipo de Duración', store=True, required=True, copied=True, tracking=0)

class TipoEstudiosCapacitaciones(models.Model):
    _name = 'tipo.estudios.capacitaciones'
    _description = 'Tipos de estudios y capacitaciones'

    name = fields.Char(string='Tipo', store=True, required=True, copied=True, tracking=0)

class TipoLicitaciones(models.Model):
    _name = 'tipo.licitaciones'
    _description = 'Tipos de licitaciones'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)

class TipoMotivoProcesosDisciplinarios(models.Model):
    _name = 'tipo.motivo.procesos.disciplinarios'
    _description = 'Tipos de motivos de procesos disciplinarios'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)

class TipoSancionProcesosDisciplinarios(models.Model):
    _name = 'tipo.sancion.procesos.disciplinarios'
    _description = 'Tipos de sanciones de procesos disciplinarios'

    name = fields.Char(string='Nombre', store=True, required=True, copied=True, tracking=0)

class Tipsqueries(models.Model):
    _name = 'tips.queries'
    _description = 'Consultas de consejos'

    description = fields.Text(string='Description', store=True, copied=True, tracking=0)
    name = fields.Text(string='Query', store=True, required=True, copied=True, tracking=0)

class TitulosEducativosEstudiosCapacitaciones(models.Model):
    _name = 'titulos.educativos.estudios.capacitaciones'
    _description = 'Títulos educativos de estudios y capacitaciones'

    name = fields.Char(string='Nombre del Título', store=True, required=True, copied=True, tracking=0)

class TrialBalanceReportWizard(models.Model):
    _name = 'trial.balance.report.wizard'
    _description = 'Asistente de reporte de balance de prueba'

    date_from = fields.Date(string='Fecha de inicio', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha final', store=True, required=True, copied=True, tracking=0)
    foreign_currency = fields.Boolean(string='Mostrar Moneda Extranjera', store=True, copied=True, tracking=0)
    fy_start_date = fields.Date(string='Fecha Inicio', readonly=True, tracking=0)
    hide_account_at_0 = fields.Boolean(string='Ocultar cuentas a 0', store=True, copied=True, tracking=0)
    hide_parent_hierarchy_level = fields.Boolean(string='No mostrar niveles padre', store=True, copied=True, tracking=0)
    limit_hierarchy_level = fields.Boolean(string='Limitar niveles de jerarquía', store=True, copied=True, tracking=0)
    not_only_one_unaffected_earnings_account = fields.Boolean(string='No solo una cuenta de ganancias no afectadas', store=True, readonly=True, copied=True, tracking=0)
    payable_accounts_only = fields.Boolean(string='Sólo cuentas a pagar', store=True, copied=True, tracking=0)
    receivable_accounts_only = fields.Boolean(string='Sólo cuentas a cobrar', store=True, copied=True, tracking=0)
    show_hierarchy_level = fields.Integer(string='Niveles de Jerarquía a mostrar', store=True, copied=True, tracking=0)
    show_hierarchy = fields.Boolean(string='Show hierarchy', store=True, copied=True, tracking=0)
    show_partner_details = fields.Boolean(string='Mostrar detalles de empresa', store=True, copied=True, tracking=0)

class UiSolicitud(models.Model):
    _name = 'ui.solicitud'
    _description = 'Solicitudes de UI'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    calcula = fields.Char(string='fila', tracking=1)
    costo_externo = fields.Boolean(string='Costo Externo', store=True, copied=True, tracking=1)
    descripcion = fields.Text(string='Notas', store=True, copied=True, tracking=1)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Solicitud', store=True, copied=True, tracking=1)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=1)
    url_autorizacion_datos = fields.Char(string='Autorizacion Datos', store=True, copied=True, tracking=1)

class UiSolicitudEstado(models.Model):
    _name = 'ui.solicitud.estado'
    _description = 'Estados de solicitudes de UI'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    descripcion = fields.Text(string='Descripción', store=True, copied=True, tracking=1)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Estado', store=True, copied=True, tracking=1)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=1)

class UiSolicitudServicio(models.Model):
    _name = 'ui.solicitud.servicio'
    _description = 'Servicios de solicitudes de UI'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    calcula = fields.Char(string='Calculado', tracking=1)
    costo_externo = fields.Boolean(string='Costo Externo', tracking=1)
    descripcion = fields.Text(string='Descripción', store=True, copied=True, tracking=1)
    fecha_realizacion = fields.Datetime(string='Fecha y Hora Realizacion', store=True, copied=True, tracking=1)
    function = fields.Char(string='Cargo', tracking=1)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Servicio', store=True, copied=True, tracking=1)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=1)

class UiSolicitudServicioConcepto(models.Model):
    _name = 'ui.solicitud.servicio.concepto'
    _description = 'Conceptos de servicios de solicitudes de UI'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    codigo1 = fields.Char(string='Codigo 1', store=True, copied=True, tracking=1)
    codigo2 = fields.Char(string='Codigo 2', store=True, copied=True, tracking=1)
    descripcion = fields.Text(string='Descripción', store=True, copied=True, tracking=1)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Concepto', store=True, copied=True, tracking=1)

class UiSolicitudServicioDeteccionEngano(models.Model):
    _name = 'ui.solicitud.servicio.deteccion.engano'
    _description = 'Detección de engaño de servicios de solicitudes de UI'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    descripcion = fields.Text(string='Descripción', store=True, copied=True, tracking=1)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Prueba Detección', store=True, copied=True, tracking=1)

class UiSolicitudServicioEstado(models.Model):
    _name = 'ui.solicitud.servicio.estado'
    _description = 'Estados de servicios de solicitudes de UI'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    descripcion = fields.Text(string='Descripción', store=True, copied=True, tracking=1)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Estado', store=True, copied=True, tracking=1)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=1)

class UiSolicitudServicioModalidad(models.Model):
    _name = 'ui.solicitud.servicio.modalidad'
    _description = 'Modalidades de servicios de solicitudes de UI'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    descripcion = fields.Text(string='Descripción', store=True, copied=True, tracking=1)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Modalidad', store=True, copied=True, tracking=1)

class UiSolicitudServicioTipoEstudio(models.Model):
    _name = 'ui.solicitud.servicio.tipo.estudio'
    _description = 'Tipos de estudio de servicios de solicitudes de UI'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    autorizacion_id_url = fields.Char(string='Url', store=True, readonly=True, tracking=1)
    descripcion = fields.Text(string='Descripción', store=True, copied=True, tracking=1)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Tipo Servicio', store=True, copied=True, tracking=1)

class UiSolicitudServicioTipoPrueba(models.Model):
    _name = 'ui.solicitud.servicio.tipo.prueba'
    _description = 'Tipos de prueba de servicios de solicitudes de UI'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    descripcion = fields.Text(string='Descripción', store=True, copied=True, tracking=1)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Modalidad', store=True, copied=True, tracking=1)

class UndefinedEstado(models.Model):
    _name = 'undefined.estado'
    _description = 'Estados indefinidos'

    active = fields.Boolean(string='Activo', store=True, copied=True, tracking=1)
    activity_date_deadline = fields.Date(string='Next Activity Deadline', readonly=True, tracking=0)
    activity_exception_icon = fields.Char(string='Icon', readonly=True, tracking=0)
    activity_summary = fields.Char(string='Next Activity Summary', tracking=0)
    activity_type_icon = fields.Char(string='Activity Type Icon', readonly=True, tracking=0)
    descripcion = fields.Text(string='Descripción', store=True, copied=True, tracking=1)
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True, tracking=0)
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, tracking=0)
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, tracking=0)
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, tracking=0)
    message_is_follower = fields.Boolean(string='Is Follower', readonly=True, tracking=0)
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, tracking=0)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, tracking=0)
    message_unread_counter = fields.Integer(string='Unread Messages Counter', readonly=True, tracking=0)
    message_unread = fields.Boolean(string='Unread Messages', readonly=True, tracking=0)
    my_activity_date_deadline = fields.Date(string='My Activity Deadline', readonly=True, tracking=0)
    name = fields.Char(string='Estado', store=True, copied=True, tracking=1)
    sequence = fields.Integer(string='Secuencia', store=True, copied=True, tracking=1)

class UomCode(models.Model):
    _name = 'uom.code'
    _description = 'Códigos de unidades de medida'

    code = fields.Char(string='Código', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class UomUom(models.Model):
    _inherit = 'uom.uom'
    code_dian = fields.Char(string='Código DIAN', store=True, copied=True, tracking=0)
    timesheet_widget = fields.Char(string='Widget', store=True, copied=True, tracking=0)

class VariablesEconomicas(models.Model):
    _name = 'variables.economicas'
    _description = 'Variables económicas'

    code = fields.Char(string='Codigo', store=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class VariablesEconomicasLine(models.Model):
    _name = 'variables.economicas.line'
    _description = 'Líneas de variables económicas'

    date_from = fields.Datetime(string='Fecha desde', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Datetime(string='Fecha hasta', store=True, required=True, copied=True, tracking=0)
    valor = fields.Float(string='Valor', store=True, required=True, copied=True, tracking=0)

class VariablesEconomicasRetefuente(models.Model):
    _name = 'variables.economicas.retefuente'
    _description = 'Variables económicas de retención en la fuente'

    date_from = fields.Datetime(string='Fecha desde', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Datetime(string='Fecha hasta', store=True, required=True, copied=True, tracking=0)
    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class VariablesEconomicasRetefuenteLine(models.Model):
    _name = 'variables.economicas.retefuente.line'
    _description = 'Líneas de variables económicas de retención en la fuente'

    valor_desde = fields.Float(string='Valor desde (UVT)', store=True, required=True, copied=True, tracking=0)
    valor_hasta = fields.Float(string='Valor hasta (UVT)', store=True, required=True, copied=True, tracking=0)
    valor_impuesto = fields.Float(string='Impuesto (UVT)', store=True, required=True, copied=True, tracking=0)

class VariablesEconomicasRetefuenteMarginalLine(models.Model):
    _name = 'variables.economicas.retefuente.marginal.line'
    _description = 'Líneas marginales de variables económicas de retención en la fuente'

    ajuste = fields.Float(string='Ajuste (UVT)', store=True, required=True, copied=True, tracking=0)
    tarifa = fields.Float(string='Tarifa (%)', store=True, required=True, copied=True, tracking=0)
    valor_desde = fields.Float(string='Valor desde(UVT)', store=True, required=True, copied=True, tracking=0)
    valor_hasta = fields.Float(string='Valor hasta (UVT)', store=True, required=True, copied=True, tracking=0)

class VatReportWizard(models.Model):
    _name = 'vat.report.wizard'
    _description = 'Asistente de reporte de IVA'

    date_from = fields.Date(string='Fecha de comienzo', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='Fecha final', store=True, required=True, copied=True, tracking=0)
    tadetail = fields.Boolean(string='Detalle de impuestos', store=True, copied=True, tracking=0)

class ViewCenterButton(models.Model):
    _name = 'view.center.button'
    _description = 'Botones de centro de vistas'

    button_key = fields.Char(string='Button Key', store=True, required=True, copied=True, tracking=0)

class WageUpdateHistory(models.Model):
    _name = 'wage.update.history'
    _description = 'Historial de actualización de salarios'

    date = fields.Datetime(string='Fecha', store=True, required=True, copied=True, tracking=0)
    wage = fields.Float(string='Salario', store=True, required=True, copied=True, tracking=0)

class WebEditorConverterTest(models.Model):
    _name = 'web.editor.converter.test'
    _description = 'Pruebas de conversor de editor web'

    char = fields.Char(string='Char', store=True, copied=True, tracking=0)
    date = fields.Date(string='Date', store=True, copied=True, tracking=0)
    datetime = fields.Datetime(string='Datetime', store=True, copied=True, tracking=0)
    float = fields.Float(string='Float', store=True, copied=True, tracking=0)
    html = fields.Html(string='HTML', store=True, copied=True, tracking=0)
    integer = fields.Integer(string='Integer', store=True, copied=True, tracking=0)
    numeric = fields.Float(string='Numeric', store=True, copied=True, tracking=0)
    Text = fields.Text(string='Text', store=True, copied=True, tracking=0)

class WebEditorConverterTestSub(models.Model):
    _name = 'web.editor.converter.test.sub'
    _description = 'Subpruebas de conversor de editor web'

    name = fields.Char(string='Nombre', store=True, copied=True, tracking=0)

class WebsiteCoverPropertiesMixin(models.Model):
    _name = 'website.cover.properties.mixin'
    _description = 'Mezcla de propiedades de portada de sitio web'

    cover_properties = fields.Text(string='Propiedades de la portada', store=True, copied=True, tracking=0)

class WebTourTour(models.Model):
    _name = 'web.tour.tour'
    _description = 'Recorridos de tour web'

    name = fields.Char(string='Nombre del recorrido', store=True, required=True, copied=True, tracking=0)

class WizAccountAssetReport(models.Model):
    _name = 'wiz.account.asset.report'
    _description = 'Asistente de reporte de activos contables'

    date_from = fields.Date(string='Start Date', store=True, required=True, copied=True, tracking=0)
    date_to = fields.Date(string='End Date', store=True, required=True, copied=True, tracking=0)
    draft = fields.Boolean(string='Include draft assets', store=True, copied=True, tracking=0)

class WizardCertificadoRetencion(models.Model):
    _name = 'wizard.certificado.retencion'
    _description = 'Asistente de certificados de retención'

    date_expedition = fields.Date(string='Fecha de Expedicion', store=True, copied=True, tracking=0)

class WizardContractProrroga(models.Model):
    _name = 'wizard.contract.prorroga'
    _description = 'Asistente de prórroga de contratos'

    specific_date = fields.Date(string='Fecha', store=True, copied=True, tracking=0)

class WizardDocumentPageHistoryShowDiff(models.Model):
    _name = 'wizard.document.page.history.show.diff'
    _description = 'Asistente de visualización de diferencias de historial de páginas de documentos'

    diff = fields.Text(string='Diff', store=True, readonly=True, copied=True, tracking=0)

class WizardNoveltyAdvance(models.Model):
    _name = 'wizard.novelty.advance'
    _description = 'Asistente de anticipo de novedades'

    date = fields.Date(string='Fecha Referencia', store=True, copied=True, tracking=0)

class WizardServiceOrderLine(models.Model):
    _name = 'wizard.service.order.line'
    _description = 'Asistente de líneas de órdenes de servicio'

    date_start = fields.Date(string='Fecha de Cálculo', store=True, copied=True, tracking=0)




