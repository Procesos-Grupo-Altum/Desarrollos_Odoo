from Api_conexion import db, uid, password, models

# --- Función para crear permisos ---
def crear_permisos(group_id, model_id, permiso_name, permiso_read, permiso_write, permiso_create, permiso_unlink):
    # Crear el permiso sin verificar si ya existe
    access_id = models.execute_kw(
        db, uid, password,
        'ir.model.access', 'create',
        [{
            'name': permiso_name,
            'group_id': group_id,
            'model_id': model_id,
            'perm_read': permiso_read,
            'perm_write': permiso_write,
            'perm_create': permiso_create,
            'perm_unlink': permiso_unlink,
        }]
    )
    print(f"✅ Permiso creado para el grupo {group_id} y modelo {model_id} con ID: {access_id}")
    return access_id

# --- Función para modificar permisos ---
def modificar_permisos(group_id, model_id, access_id, permiso_name, permiso_read, permiso_write, permiso_create, permiso_unlink):
    access_exists = models.execute_kw(
        db, uid, password,
        'ir.model.access', 'search',
        [[('id', '=', access_id), ('group_id', '=', group_id), ('model_id', '=', model_id)]]
    )
    if not access_exists:
        print(f"❌ No se encontró el permiso con ID {access_id} para el grupo {group_id} y modelo {model_id}")
        return None

    models.execute_kw(
        db, uid, password,
        'ir.model.access', 'write',
        [access_exists, {
            'name': permiso_name,
            'perm_read': permiso_read,
            'perm_write': permiso_write,
            'perm_create': permiso_create,
            'perm_unlink': permiso_unlink,
        }]
    )
    print(f"✅ Permiso modificado con ID {access_id}")
    return access_id

# --- Función para eliminar permisos ---
def eliminar_permisos(group_id, model_id, access_id):
    access_exists = models.execute_kw(
        db, uid, password,
        'ir.model.access', 'search',
        [[('id', '=', access_id), ('group_id', '=', group_id), ('model_id', '=', model_id)]]
    )
    if not access_exists:
        print(f"❌ No se encontró el permiso con ID {access_id} para el grupo {group_id} y modelo {model_id}")
        return None

    models.execute_kw(
        db, uid, password,
        'ir.model.access', 'unlink',
        [access_exists]
    )
    print(f"✅ Permiso eliminado con ID {access_id}")
    return True

# --- Ejemplo de uso ---
# modificar_permisos(1, 3, 14, 'ir_model_all', True, False, False, False
# modificar_permisos(1, 4, 16, 'ir_model_fields_all', True, False, False, False
# modificar_permisos(1, 5, 17, 'ir_model_fields_selection_all', True, False, False, False
# modificar_permisos(1, 9, 15, 'ir_model_data_user', True, False, True, False
# modificar_permisos(1, 11, 25, 'ir_sequence_group_user', True, True, True, False
# modificar_permisos(1, 12, 27, 'ir_sequence_date_range_group_user', True, True, False, False
# modificar_permisos(1, 13, 31, 'ir_ui_menu_group_user', True, False, False, False
# modificar_permisos(1, 18, 2736, 'ir.actions.act_window', True, False, False, False
# modificar_permisos(1, 26, 226, 'ir.actions.report.access.user', True, False, False, False
# modificar_permisos(1, 27, 2444, 'ir.attachment.usuario.interno', True, True, True, False
# modificar_permisos(1, 29, 93, 'ir_filters_all', True, True, True, True
# modificar_permisos(1, 30, 38, 'ir_default_group_user', True, True, True, True
# modificar_permisos(1, 31, 29, 'ir_translation_all', True, True, True, True
# modificar_permisos(1, 33, 6, 'ir_exports_line_group_system', True, True, True, True
# modificar_permisos(1, 63, 2371, 'ir.module.module.all', True, False, False, False
# modificar_permisos(1, 77, 63, 'res_partner_category_group_user', True, False, False, False
# modificar_permisos(1, 79, 60, 'res_partner_group_user', True, False, False, False
# modificar_permisos(1, 80, 65, 'res_partner_industry_group_user', True, False, False, False
# modificar_permisos(1, 81, 91, 'res_bank_user', True, False, False, False
# modificar_permisos(1, 82, 61, 'res_partner_bank_group_user', True, False, False, False
# modificar_permisos(1, 85, 2065, 'res.config.settings.usuario_interno', True, False, False, False
# modificar_permisos(1, 89, 54, 'res_groups_group_user', True, False, False, False
# modificar_permisos(1, 91, 69, 'res_users_all', True, False, False, False
# modificar_permisos(1, 95, 74, 'API_keys_access_employees', True, False, False, False
# modificar_permisos(1, 96, 76, 'API_key_wizard_employees', True, False, True, False
# modificar_permisos(1, 97, 78, 'API_key_result_employees', True, False, True, False
# modificar_permisos(1, 105, 117, 'access.base.language.export', True, True, True, False
# modificar_permisos(1, 111, 122, 'auth_totp wizard access rules', True, True, True, True
# modificar_permisos(1, 112, 137, 'base.import.mapping', True, True, True, True
# modificar_permisos(1, 113, 139, 'access.base_import.import', True, True, True, False
# modificar_permisos(1, 114, 123, 'base.import.tests.models.char', True, True, True, True
# modificar_permisos(1, 115, 124, 'base.import.tests.models.char.required', True, True, True, True
# modificar_permisos(1, 116, 125, 'base.import.tests.models.char.readonly', True, True, True, True
# modificar_permisos(1, 117, 126, 'base.import.tests.models.char.states', True, True, True, True
# modificar_permisos(1, 118, 127, 'base.import.tests.models.char.noreadonly', True, True, True, True
# modificar_permisos(1, 119, 128, 'base.import.tests.models.char.stillreadonly', True, True, True, True
# modificar_permisos(1, 120, 129, 'base.import.tests.models.m2o', True, True, True, True
# modificar_permisos(1, 121, 130, 'base.import.tests.models.m2o.related', True, True, True, True
# modificar_permisos(1, 122, 131, 'base.import.tests.models.m2o.required', True, True, True, True
# modificar_permisos(1, 123, 132, 'base.import.tests.models.m2o.required.related', True, True, True, True
# modificar_permisos(1, 124, 133, 'base.import.tests.models.o2m', True, True, True, True
# modificar_permisos(1, 125, 134, 'base.import.tests.models.o2m.child', True, True, True, True
# modificar_permisos(1, 126, 136, 'base.import.tests.models.preview', True, True, True, True
# modificar_permisos(1, 127, 135, 'base.import.tests.models.float', True, True, True, True
# modificar_permisos(1, 128, 138, 'access_base_import_tests_models_complex', True, False, False, False
# modificar_permisos(1, 134, 2655, 'interno', True, False, False, False
# modificar_permisos(1, 136, 149, 'uom.uom.user', True, False, False, False
# modificar_permisos(1, 141, 155, 'bus.presence', True, True, True, True
# modificar_permisos(1, 143, 157, 'resource.calendar.user', True, False, False, False
# modificar_permisos(1, 144, 159, 'resource.calendar.attendance.user', True, False, False, False
# modificar_permisos(1, 145, 162, 'resource.resource all', True, False, False, False
# modificar_permisos(1, 146, 163, 'resource.calendar.leaves', True, True, True, True
# modificar_permisos(1, 147, 165, 'resource.test.all', True, True, True, True
# modificar_permisos(1, 148, 170, 'mail.utm.stage', True, False, False, False
# modificar_permisos(1, 149, 168, 'access_utm_medium_user', True, True, True, False
# modificar_permisos(1, 150, 166, 'access_utm_campaign_user', True, True, True, False
# modificar_permisos(1, 151, 169, 'access_utm_source_user', True, True, True, False
# modificar_permisos(1, 152, 175, 'utm.tag', True, False, False, False
# modificar_permisos(1, 154, 178, 'iap.account.user', True, False, True, False
# modificar_permisos(1, 155, 202, 'mail.message.subtype.user', True, True, True, True
# modificar_permisos(1, 156, 205, 'mail.tracking.value.user', False, False, False, False
# modificar_permisos(1, 157, 199, 'mail.alias.user', True, False, False, False
# modificar_permisos(1, 159, 187, 'mail.followers.user', True, False, False, False
# modificar_permisos(1, 160, 190, 'mail.notification.user', True, True, True, False
# modificar_permisos(1, 162, 181, 'mail.message.user', True, True, True, True
# modificar_permisos(1, 163, 215, 'mail.activity.type.user', True, False, False, False
# modificar_permisos(1, 164, 213, 'mail.activity.user', True, True, True, True
# modificar_permisos(1, 166, 184, 'mail.mail.user', True, True, True, False
# modificar_permisos(1, 171, 196, 'mail.channel.partner.user', True, True, True, True
# modificar_permisos(1, 172, 197, 'mail.moderation.user', True, True, True, True
# modificar_permisos(1, 173, 193, 'mail.group.user', True, True, True, True
# modificar_permisos(1, 174, 208, 'mail.template', True, True, True, False
# modificar_permisos(1, 175, 210, 'mail.shortcode', True, True, True, True
# modificar_permisos(1, 191, 218, 'access.mail.wizard.invite', True, True, True, False
# modificar_permisos(1, 193, 219, 'access.mail.compose.message', True, True, True, False
# modificar_permisos(1, 194, 221, 'access.mail.resend.cancel', True, True, True, False
# modificar_permisos(1, 195, 222, 'access.mail.resend.message', True, True, True, False
# modificar_permisos(1, 196, 223, 'access.mail.resend.partner', True, True, True, False
# modificar_permisos(1, 197, 224, 'access.mail.template.preview', True, True, True, False
# modificar_permisos(1, 339, 2012, 'account.analytic.account', True, False, False, False
# modificar_permisos(1, 339, 2753, 'account.analytic.account', True, False, False, False
# modificar_permisos(1, 341, 233, 'calendar.attendee_employee', True, True, True, True
# modificar_permisos(1, 342, 243, 'access_calendar_recurrence', True, True, True, True
# modificar_permisos(1, 343, 236, 'calendar.event_all_employee', True, True, True, True
# modificar_permisos(1, 344, 234, 'calendar.alarm', True, True, True, True
# modificar_permisos(1, 345, 240, 'access_calendar_alarm_manager', True, True, True, True
# modificar_permisos(1, 346, 241, 'access_calendar_contacts_all', True, True, True, True
# modificar_permisos(1, 347, 238, 'calendar.event.type.all', True, False, False, False
# modificar_permisos(1, 347, 1028, 'calendar.event.type.user', True, False, False, False
# modificar_permisos(1, 357, 269, 'access.gamification.goal.wizard', True, True, True, False
# modificar_permisos(1, 358, 270, 'access.gamification.badge.user.wizard', True, True, True, False
# modificar_permisos(1, 362, 275, 'hr.employee_public', True, False, False, False
# modificar_permisos(1, 363, 278, 'hr.department.employee', True, False, False, False
# modificar_permisos(1, 365, 280, 'access_hr_plan_activity_type', True, False, False, False
# modificar_permisos(1, 366, 281, 'access_hr_plan_employee', True, False, False, False
# modificar_permisos(1, 374, 290, 'product.template.user', True, False, False, False
# modificar_permisos(1, 375, 289, 'product.category.user', True, False, False, False
# modificar_permisos(1, 376, 296, 'product.product employee', True, False, False, False
# modificar_permisos(1, 378, 292, 'product.supplierinfo.user', True, False, False, False
# modificar_permisos(1, 379, 297, 'product.attribute', True, False, False, False
# modificar_permisos(1, 381, 302, 'product.template.attribute line', True, False, False, False
# modificar_permisos(1, 382, 300, 'product.template.attribute value', True, False, False, False
# modificar_permisos(1, 386, 294, 'product.pricelist.item.user', True, False, False, False
# modificar_permisos(1, 391, 2311, 'hr.contract.all', True, False, False, False
# modificar_permisos(1, 399, 343, 'res.partner.autocomplete.sync.user', True, True, True, False
# modificar_permisos(1, 408, 351, 'access.sms.template.user', True, False, False, False
# modificar_permisos(1, 409, 353, 'access.sms.cancel', True, True, True, False
# modificar_permisos(1, 410, 354, 'access.sms.composer', True, True, True, False
# modificar_permisos(1, 411, 355, 'access.sms.resend.recipient', True, True, True, False
# modificar_permisos(1, 412, 356, 'access.sms.resend', True, True, True, False
# modificar_permisos(1, 413, 357, 'access.sms.template.preview', True, True, True, False
# modificar_permisos(1, 414, 358, 'snailmail.letter.user', True, True, True, False
# modificar_permisos(1, 416, 360, 'access.snailmail.letter.cancel', True, True, True, False
# modificar_permisos(1, 417, 361, 'access.snailmail.letter.format.error', True, True, True, False
# modificar_permisos(1, 418, 362, 'access.snailmail.letter.missing.required.fields', True, True, True, False
# modificar_permisos(1, 428, 414, 'account.fiscal.position all', True, False, False, False
# modificar_permisos(1, 429, 415, 'account.fiscal.position.tax all', True, False, False, False
# modificar_permisos(1, 430, 416, 'account.fiscal.position all', True, False, False, False
# modificar_permisos(1, 433, 451, 'account.account user', True, False, False, False
# modificar_permisos(1, 437, 652, 'account.journal.employee', True, False, False, False
# modificar_permisos(1, 438, 472, 'account.tax.group internal user', True, False, False, False
# modificar_permisos(1, 439, 457, 'account.tax internal user', True, False, False, False
# modificar_permisos(1, 440, 464, 'account.tax repartition.line.user', True, False, False, False
# modificar_permisos(1, 446, 491, 'account.payment.term partner manager', True, False, False, False
# modificar_permisos(1, 447, 493, 'account.payment.term.line partner manager', True, False, False, False
# modificar_permisos(1, 448, 2300, 'account.move', True, True, True, False
# modificar_permisos(1, 449, 2302, 'account.move.line.all', True, True, True, False
# modificar_permisos(1, 449, 2366, 'account.move.line.vise.grupo.usuario', True, False, False, False
# modificar_permisos(1, 453, 495, 'account.payment.method', True, False, False, False
# modificar_permisos(1, 496, 3105, 'hr.applicant.vise_requisicion', True, False, False, False
# modificar_permisos(1, 502, 583, 'product.removal all users', True, False, False, False
# modificar_permisos(1, 503, 581, 'stock.putaway.rule all users', True, False, False, False
# modificar_permisos(1, 506, 537, 'stock.location.user', True, False, False, False
# modificar_permisos(1, 507, 576, 'stock.location.route', True, False, False, False
# modificar_permisos(1, 509, 580, 'stock.move.line all users', True, True, True, True
# modificar_permisos(1, 510, 577, 'stock.rule.flow internal', True, False, False, False
# modificar_permisos(1, 511, 532, 'procurement.group', True, True, True, False
# modificar_permisos(1, 514, 540, 'stock.picking.type all users', True, False, False, False
# modificar_permisos(1, 516, 566, 'stock.quant all users', True, False, False, False
# modificar_permisos(1, 517, 567, 'stock.quant.package all users', True, False, False, False
# modificar_permisos(1, 518, 534, 'stock.warehouse.user', True, False, False, False
# modificar_permisos(1, 519, 2296, 'stock.scrap.all', True, False, False, False
# modificar_permisos(1, 520, 570, 'stock.package_level all users', True, False, False, False
# modificar_permisos(1, 523, 595, 'access_report_stock_quantity', True, False, False, False
# modificar_permisos(1, 557, 2303, 'theme.ir.attachment.usuario.interno', True, True, True, False
# modificar_permisos(1, 567, 642, 'hr.expense.employee', True, True, True, True
# modificar_permisos(1, 568, 643, 'hr.expense.sheet.employee', True, True, True, True
# modificar_permisos(1, 571, 668, 'payment.icon.user', True, True, True, False
# modificar_permisos(1, 572, 661, 'payment.transaction.user', True, True, True, False
# modificar_permisos(1, 573, 664, 'payment.token.user', True, True, True, True
# modificar_permisos(1, 640, 766, 'crm.team', True, False, False, False
# modificar_permisos(1, 641, 769, 'crm_tag', False, False, False, False
# modificar_permisos(1, 642, 772, 'Read access on account.payment.mode to Employees', True, False, False, False
# modificar_permisos(1, 652, 2310, 'account.move.tax.all', True, False, False, False
# modificar_permisos(1, 653, 2974, 'res.ciiu.interno', True, False, False, False
# modificar_permisos(1, 665, 2373, 'hr.expense.expense.all', True, True, True, False
# modificar_permisos(1, 684, 949, 'date_range.date_range', True, False, False, False
# modificar_permisos(1, 702, 954, 'access_aged_partner_balance_report_wizard', True, True, True, True
# modificar_permisos(1, 703, 955, 'access_general_ledger_report_wizard', True, True, True, True
# modificar_permisos(1, 704, 956, 'access_journal_ledger_report_wizard', True, True, True, True
# modificar_permisos(1, 705, 957, 'access_open_items_report_wizard', True, True, True, True
# modificar_permisos(1, 706, 958, 'access_trial_balance_report_wizard', True, True, True, True
# modificar_permisos(1, 707, 959, 'access_vat_report_wizard', True, True, True, True
# modificar_permisos(1, 716, 1023, 'crm.lost.reason.user', True, False, False, False
# modificar_permisos(1, 721, 1024, 'crm.activity.report.user', True, False, False, False
# modificar_permisos(1, 760, 2380, 'res.partner.document.type.all', True, False, False, False
# modificar_permisos(1, 812, 1260, 'access_account_financial_report_assistant_line', True, True, True, True
# modificar_permisos(1, 813, 1261, 'access_account_financial_report_state_income', True, True, True, True
# modificar_permisos(1, 814, 1262, 'access_account_financial_report_state_income_line', True, True, True, True
# modificar_permisos(1, 815, 1263, 'access_account_financial_report_balance_general', True, True, True, True
# modificar_permisos(1, 816, 1264, 'access_account_financial_report_balance_general_line', True, True, True, True
# modificar_permisos(1, 884, 1168, 'hr_ed_institution_user', True, True, True, True
# modificar_permisos(1, 885, 1169, 'hr_work_occupation_user', True, True, True, True
# modificar_permisos(1, 886, 1170, 'hr_military_degree_user', True, True, True, True
# modificar_permisos(1, 887, 1166, 'hr_employee_disciplinary_action_user', True, True, True, True
# modificar_permisos(1, 888, 1167, 'hr_employee_disciplinary_action_line_user', True, True, True, True
# modificar_permisos(1, 889, 1165, 'hr_disability_user', True, True, True, True
# modificar_permisos(1, 890, 1164, 'hr_public_service_user', True, True, True, True
# modificar_permisos(1, 891, 1160, 'hr_employee_capacitaciones_user', True, True, True, True
# modificar_permisos(1, 892, 1161, 'hr_employee_referencias_user', True, True, True, True
# modificar_permisos(1, 893, 1162, 'hr_employee_familiar_user', True, True, True, True
# modificar_permisos(1, 894, 1163, 'hr_employee_dotacion_user', True, True, True, True
# modificar_permisos(1, 896, 3293, 'grupo interno', True, True, True, False
# modificar_permisos(1, 925, 1182, 'project.project on partners', True, False, True, False
# modificar_permisos(1, 926, 1180, 'project.task on partners', True, False, False, False
# modificar_permisos(1, 1026, 1266, 'access_hr_concept_log', True, True, True, True
# modificar_permisos(1, 1048, 1304, 'access_account_consignment_wizard', True, True, True, True
# modificar_permisos(1, 1143, 3034, 'access_hr_payroll_novedades_category', True, True, True, True
# modificar_permisos(1, 1149, 1362, 'account_account_bank_statement_avancys', True, True, True, True
# modificar_permisos(1, 1150, 1363, 'account_account_bank_statement_line_avancys', True, True, True, True
# modificar_permisos(1, 1151, 1364, 'account_account_bank_multi_transaction', True, True, True, True
# modificar_permisos(1, 1152, 1365, 'account_account_bank_multi_move', True, True, True, True
# modificar_permisos(1, 1153, 1360, 'account_account_banking_parser', True, True, True, True
# modificar_permisos(1, 1154, 1361, 'account_banking_bank_import', True, True, True, True
# modificar_permisos(1, 1155, 1366, 'bank_transaction_wiz', True, True, True, True
# modificar_permisos(1, 1160, 1374, 'account_dimensions_avancys.res_regional', True, False, False, False
# modificar_permisos(1, 1160, 1422, 'hr_roster_avancys.res_regional', True, False, False, False
# modificar_permisos(1, 1161, 1377, 'account_dimensions_avancys.account_commercial', True, True, True, True
# modificar_permisos(1, 1162, 2794, 'account.commercial.distribution.usuario_interno', True, False, False, False
# modificar_permisos(1, 1163, 1379, 'account_dimensions_avancys.account_commercial_distribution_line', True, True, True, True
# modificar_permisos(1, 1164, 1375, 'account_dimensions_avancys.project_distribution', True, True, True, True
# modificar_permisos(1, 1165, 1376, 'account_dimensions_avancys.project_distribution_line', True, True, True, True
# modificar_permisos(1, 1170, 1384, 'access.account.suppier.payment.wizard', True, True, True, True
# modificar_permisos(1, 1171, 1385, 'access.account.payment.file.config', True, True, True, True
# modificar_permisos(1, 1172, 1386, 'access.account.payment.config.line', True, True, True, True
# modificar_permisos(1, 1178, 2734, 'res.city.zip.interno', True, False, False, False
# modificar_permisos(1, 1180, 1397, 'res.partner.id_number', True, False, False, False
# modificar_permisos(1, 1181, 1399, 'res.partner.id_category', True, False, False, False
# modificar_permisos(1, 1191, 2379, 'account.move.dian.document.vise.grupo.usuario', True, False, False, False
# modificar_permisos(1, 1228, 1259, 'access_journal_entry_import_fast', True, True, True, True
# modificar_permisos(1, 1234, 1457, 'hr_roster_avancys.remplazo_novedad_wiz', True, True, True, True
# modificar_permisos(1, 1235, 1455, 'hr_roster_avancys.massive_shift_scheduling', True, True, True, True
# modificar_permisos(1, 1236, 1456, 'hr_roster_avancys.massive_shift_scheduling_wizard', True, True, True, True
# modificar_permisos(1, 1237, 1460, 'hr_roster_avancys.manual_entry', True, True, True, True
# modificar_permisos(1, 1238, 1461, 'hr_roster_avancys.activos_puesto_wiz', True, True, True, True
# modificar_permisos(1, 1239, 1463, 'hr_roster_avancys.order_puesto_wiz', True, True, True, True
# modificar_permisos(1, 1241, 1464, 'hr_roster_avancys.cierre_programacion_wiz', True, True, True, True
# modificar_permisos(1, 1242, 1449, 'hr_roster_avancys.cierre_nomina_wiz', True, True, True, True
# modificar_permisos(1, 1243, 1465, 'hr_roster_avancys.programacion_modalidad_wiz', True, True, True, True
# modificar_permisos(1, 1244, 1466, 'hr_roster_avancys.hr_roster_adicionales', True, True, True, True
# modificar_permisos(1, 1245, 1467, 'hr_roster_avancys.hr_roster_adicional_day', True, True, True, True
# modificar_permisos(1, 1247, 1469, 'access_hr_roster_cambio_turno', True, True, True, True
# modificar_permisos(1, 1248, 1470, 'access_hr_roster_cambio_update', True, True, True, True
# modificar_permisos(1, 1249, 1462, 'hr_roster_avancys.hr_roster_reverse_close', True, True, True, True
# modificar_permisos(1, 1252, 1438, 'hr_roster_avancys.hr_roster_disponibles', True, True, True, True
# modificar_permisos(1, 1253, 1439, 'hr_roster_avancys.hr_roster_puesto_tarifa_adicional', True, True, True, True
# modificar_permisos(1, 1254, 1440, 'hr_roster_avancys.hr_roster_puesto', True, True, True, True
# modificar_permisos(1, 1255, 1441, 'hr_roster_avancys.hr_roster_puesto_bono', True, True, True, True
# modificar_permisos(1, 1256, 1442, 'hr_roster_avancys.hr_roster_bono', True, True, True, True
# modificar_permisos(1, 1257, 1443, 'hr_roster_avancys.hr_roster_puesto_items_cliente', True, True, True, True
# modificar_permisos(1, 1259, 1445, 'hr_roster_avancys.hr_roster_horario', True, True, True, True
# modificar_permisos(1, 1260, 1446, 'hr_roster_avancys.hr_roster_tipo_turno', True, True, True, True
# modificar_permisos(1, 1261, 1447, 'hr_roster_avancys.hr_roster_turno', True, True, True, True
# modificar_permisos(1, 1262, 1448, 'hr_roster_avancys.hr_roster_sequence', True, True, True, True
# modificar_permisos(1, 1263, 1450, 'hr_roster_avancys.hr_roster_programacion', True, True, True, True
# modificar_permisos(1, 1264, 1451, 'hr_roster_avancys.hr_roster_programacion_line', True, True, True, True
# modificar_permisos(1, 1265, 1452, 'hr_roster_avancys.hr_roster_timesheet', True, True, True, True
# modificar_permisos(1, 1266, 1453, 'hr_roster_avancys.account_move_line_print', True, True, True, True
# modificar_permisos(1, 1267, 1431, 'hr_roster_avancys.hr_roster_prefactura', True, True, True, True
# modificar_permisos(1, 1268, 1432, 'hr_roster_avancys.hr_roster_prefactura_line', True, True, True, True
# modificar_permisos(1, 1269, 1433, 'hr_roster_avancys.account_move_profile', True, True, True, True
# modificar_permisos(1, 1270, 1434, 'hr_roster_avancys.hr_roster_concept_distribution', True, True, True, True
# modificar_permisos(1, 1271, 1435, 'hr_roster_avancys.hr_roster_sale_concept', True, True, True, True
# modificar_permisos(1, 1272, 1436, 'hr_roster_avancys.hr_roster_sale_distribution', True, True, True, True
# modificar_permisos(1, 1273, 2972, 'hr_roster_avancys.sale_order_rate', True, True, True, True
# modificar_permisos(1, 1274, 1458, 'hr_roster_avancys.hr_holiday_public', True, True, True, True
# modificar_permisos(1, 1275, 1459, 'hr_roster_avancys.hr_holiday_lines', True, True, True, True
# modificar_permisos(1, 1276, 1423, 'hr_roster_avancys.res_weekday', True, True, True, True
# modificar_permisos(1, 1276, 2629, 'res.weekday.usuario.interno', True, False, False, False
# modificar_permisos(1, 1277, 1428, 'hr_roster_avancys.project_service_order', True, True, True, True
# modificar_permisos(1, 1278, 1429, 'hr_roster_avancys.project_linea_negocio', True, True, True, True
# modificar_permisos(1, 1279, 1430, 'hr_roster_avancys.project_service_type', True, True, True, True
# modificar_permisos(1, 1280, 1425, 'hr_roster_avancys.project_service_order_support', True, True, True, True
# modificar_permisos(1, 1281, 1424, 'hr_roster_avancys.project_service_order_tmp', True, True, True, True
# modificar_permisos(1, 1282, 1454, 'hr_roster_avancys.service_order_line_secuence', True, True, True, True
# modificar_permisos(1, 1283, 1427, 'hr_roster_avancys.project_service_order_line', True, True, True, True
# modificar_permisos(1, 1284, 1426, 'hr_roster_avancys.order_line_detail', True, True, True, True
# modificar_permisos(1, 1285, 1468, 'hr_roster_avancys.payslip_period', True, True, True, True
# modificar_permisos(1, 1291, 1480, 'fr.fpa_financial_reports_concepts', True, True, True, True
# modificar_permisos(1, 1292, 1479, 'fr.fpa_niveles', True, True, True, True
# modificar_permisos(1, 1295, 1481, 'fr.fpa_financial_reports_concepts_columns', True, True, True, True
# modificar_permisos(1, 1296, 1484, 'fr.hr_payslip_concepts_code', True, True, True, True
# modificar_permisos(1, 1297, 1482, 'fr.fpa_financial_reports_concepts_columns_lines', True, True, True, True
# modificar_permisos(1, 1298, 1596, 'fr.fpa_financial_reports_period_range', True, True, True, True
# modificar_permisos(1, 1299, 1478, 'fr.fpa_financial_reports', True, True, True, True
# modificar_permisos(1, 1300, 1483, 'fr.fpa_export_wizard_ept', True, True, True, True
# modificar_permisos(1, 1301, 1485, 'fr.account_account_estructure', True, True, True, True
# modificar_permisos(1, 1302, 1486, 'fr.fpa_auxiliar_analitico', True, True, True, True
# modificar_permisos(1, 1303, 1487, 'fr.fpa_auxiliar_analitico_line', True, True, True, True
# modificar_permisos(1, 1304, 1488, 'fr.fpa_auxiliar_analitico_wizard', True, True, True, True
# modificar_permisos(1, 1305, 1489, 'fr.fpa_balance_pruebas', True, True, True, True
# modificar_permisos(1, 1306, 1490, 'fr.fpa_balance_pruebas_line', True, True, True, True
# modificar_permisos(1, 1307, 1491, 'fr.fpa_balance_pruebas_wizard', True, True, True, True
# modificar_permisos(1, 1308, 1492, 'fr.fpa_auxiliar', True, True, True, True
# modificar_permisos(1, 1309, 1493, 'fr.fpa_auxiliar_line', True, True, True, True
# modificar_permisos(1, 1310, 1494, 'fr.fpa_auxiliar_wizard', True, True, True, True
# modificar_permisos(1, 1311, 1495, 'fr.fpa_auxiliar_equivalente', True, True, True, True
# modificar_permisos(1, 1312, 1496, 'fr.fpa_auxiliar_equivalente_line', True, True, True, True
# modificar_permisos(1, 1313, 1497, 'fr.fpa_auxiliar_equivalente_wizard', True, True, True, True
# modificar_permisos(1, 1314, 1498, 'fr.fpa_mayor_balance', True, True, True, True
# modificar_permisos(1, 1315, 1499, 'fr.fpa_mayor_balance_line', True, True, True, True
# modificar_permisos(1, 1316, 1500, 'fr.fpa_mayor_balance_wizard', True, True, True, True
# modificar_permisos(1, 1317, 1501, 'fr.fpa_diario', True, True, True, True
# modificar_permisos(1, 1318, 1502, 'fr.fpa_diario_line', True, True, True, True
# modificar_permisos(1, 1319, 1503, 'fr.fpa_diario_wizard', True, True, True, True
# modificar_permisos(1, 1320, 1504, 'fr.fpa_inventario_balance', True, True, True, True
# modificar_permisos(1, 1321, 1505, 'fr.fpa_inventario_balance_line', True, True, True, True
# modificar_permisos(1, 1322, 1506, 'fr.fpa_inventario_balance_wizard', True, True, True, True
# modificar_permisos(1, 1323, 1507, 'fr.fpa_auxiliar_fc', True, True, True, True
# modificar_permisos(1, 1324, 1508, 'fr.fpa_auxiliar_fc_line', True, True, True, True
# modificar_permisos(1, 1325, 1509, 'fr.fpa_auxiliar_fc_wizard', True, True, True, True
# modificar_permisos(1, 1351, 1559, 'access.res.partner.driver', True, False, False, False
# modificar_permisos(1, 1355, 1570, 'spd_stock_report_sql_group_location', True, True, True, True
# modificar_permisos(1, 1356, 1569, 'spd_stock_report_kardex_dot_line', True, True, True, True
# modificar_permisos(1, 1357, 1568, 'spd_stock_report_kardex_dot_wizard', True, True, True, True
# modificar_permisos(1, 1359, 1576, 'crm_claim_category', True, False, False, False
# modificar_permisos(1, 1368, 1590, 'access_project_sale_line_employee_map', True, False, False, False
# modificar_permisos(1, 1381, 1606, 'fr.fpa_pyg_c', True, True, True, True
# modificar_permisos(1, 1382, 1607, 'fr.fpa_pyg_c_line', True, True, True, True
# modificar_permisos(1, 1383, 1608, 'fr.fpa_pyg_c_wizard', True, True, True, True
# modificar_permisos(1, 1384, 1603, 'fr.fpa_pyg_cc', True, True, True, True
# modificar_permisos(1, 1385, 1604, 'fr.fpa_pyg_cc_line', True, True, True, True
# modificar_permisos(1, 1386, 1605, 'fr.fpa_pyg_cc_wizard', True, True, True, True
# modificar_permisos(1, 1387, 1600, 'fr.fpa_pyg_cc_analytic', True, True, True, True
# modificar_permisos(1, 1388, 1601, 'fr.fpa_pyg_cc_analytic_line', True, True, True, True
# modificar_permisos(1, 1389, 1602, 'fr.fpa_pyg_cc_analytic_wizard', True, True, True, True
# modificar_permisos(1, 1390, 1612, 'fr.fpa_flujocaja', True, True, True, True
# modificar_permisos(1, 1391, 1613, 'fr.fpa_flujocaja_line', True, True, True, True
# modificar_permisos(1, 1392, 1614, 'fr.fpa_flujocaja_wizard', True, True, True, True
# modificar_permisos(1, 1393, 1597, 'fr.fpa_equity_changes', True, True, True, True
# modificar_permisos(1, 1394, 1598, 'fr.fpa_equity_changes_line', True, True, True, True
# modificar_permisos(1, 1395, 1599, 'fr.fpa_equity_changes_wizard', True, True, True, True
# modificar_permisos(1, 1396, 1609, 'fr.fpa_pyg', True, True, True, True
# modificar_permisos(1, 1397, 1610, 'fr.fpa_pyg_line', True, True, True, True
# modificar_permisos(1, 1398, 1611, 'fr.fpa_pyg_wizard', True, True, True, True
# modificar_permisos(1, 1520, 1679, 'equipment.category.user', True, False, False, False
# modificar_permisos(1, 1521, 1676, 'equipment.user', True, False, False, False
# modificar_permisos(1, 1525, 3252, 'audit.audit.empleados.rrhh', True, True, True, False
# modificar_permisos(1, 1538, 3250, 'audit.process.empleados.rrhh', True, True, True, False
# modificar_permisos(1, 1539, 3249, 'audit.system.empleados.rrhh', True, True, True, False
# modificar_permisos(1, 1545, 1719, 'account.asset.close.wizard', True, True, True, True
# modificar_permisos(1, 1548, 1736, 'access_security_access_groups_user', True, True, True, True
# modificar_permisos(1, 1565, 1772, 'access_sh_helpdesk_sla_policy', True, True, True, True
# modificar_permisos(1, 1567, 1773, 'access_sh_helpdesk_sla_status', True, True, True, True
# modificar_permisos(1, 1569, 1774, 'access_sh_ticket_alarm', True, True, True, True
# modificar_permisos(1, 1571, 1770, 'access_sh_quick_reply', True, True, True, True
# modificar_permisos(1, 1572, 1775, 'access_sh_helpdesk_ticket_mass_update_wizard', True, True, True, True
# modificar_permisos(1, 1573, 1776, 'access_sh_helpdesk_ticket_merge_ticket_wizard', True, True, True, True
# modificar_permisos(1, 1574, 1777, 'access_sh_helpdesk_ticket_stage_info', True, True, True, True
# modificar_permisos(1, 1575, 1778, 'access_ticket_time_account_line', True, True, True, True
# modificar_permisos(1, 1580, 1807, 'report.print.certificado.retencion.line', True, True, True, True
# modificar_permisos(1, 1581, 1805, 'report.print.certificado.retencion', True, True, True, True
# modificar_permisos(1, 1582, 1803, 'report.certificado.report.retencion', True, True, True, True
# modificar_permisos(1, 1583, 1806, 'report.certificado.report.retencion.line', True, True, True, True
# modificar_permisos(1, 1584, 1802, 'report.certificado.report.retencion.periodicidad', True, True, True, True
# modificar_permisos(1, 1585, 1804, 'report.wizard.certificado.retencion', True, True, True, True
# modificar_permisos(1, 1630, 1836, 'ir.actions.center', True, True, True, True
# modificar_permisos(1, 1632, 1832, 'studio.view.center', True, True, True, True
# modificar_permisos(1, 1634, 1835, 'studio.button', True, True, True, True
# modificar_permisos(1, 1636, 1838, 'studio.approval.details', True, True, True, True
# modificar_permisos(1, 1640, 1839, 'access_base_geo_provider', True, False, False, False
# modificar_permisos(1, 1646, 2039, 'Vise_Proveedor', True, False, False, False
# modificar_permisos(1, 1657, 2038, 'Vise.contabilidad', True, False, False, False
# modificar_permisos(1, 1808, 2319, 'account.asset.process.wizard', True, True, True, True
# modificar_permisos(1, 1844, 2351, 'base_user_move_recoup_line', True, True, True, True
# modificar_permisos(1, 1845, 2352, 'base_user_account_move_recoup', True, True, True, True
# modificar_permisos(1, 1846, 2353, 'base_user_hr_expense_line_recoup', True, True, True, True
# modificar_permisos(1, 1942, 2435, 'access_account_aged_receivable', True, False, False, False
# modificar_permisos(1, 1943, 2436, 'access_account_aged_payable', True, False, False, False
# modificar_permisos(1, 2042, 2609, 'access_hr_payroll_advance_wizard', True, True, True, True
# modificar_permisos(1, 2174, 2639, 'note.stage', True, True, True, True
# modificar_permisos(1, 2175, 2641, 'note.tag', True, True, True, True
# modificar_permisos(1, 2176, 2640, 'note.note', True, True, True, True
# modificar_permisos(1, 2641, 2797, 'x_imeis.usuario_interno', True, True, True, True
# modificar_permisos(1, 2647, 2801, 'x_lineas_celular.usuario_interno', True, True, True, True
# modificar_permisos(1, 2660, 2812, 'hr_roster_avancys.remplazo_novedad_wiz_masive', True, True, True, True
# modificar_permisos(1, 2676, 2888, 'hr_roster_avancys.tarifario_wiz', True, True, True, True
# modificar_permisos(1, 2677, 2891, 'hr_roster_avancys.validate_tarifario', True, True, True, True
# modificar_permisos(1, 2680, 2889, 'hr_roster_avancys.hr_roster_tarifario', True, True, True, True
# modificar_permisos(1, 2681, 2890, 'hr_roster_avancys.hr_roster_tarifario_line', True, True, True, True
# modificar_permisos(1, 2700, 2899, 'access_hr_novelty_log', True, False, False, True
# modificar_permisos(1, 2728, 2929, 'access_auditlog_autovacuum', True, True, True, True
# modificar_permisos(1, 2742, 2943, 'x_asignacion_celular_usuario_interno', True, True, True, False
# modificar_permisos(1, 2787, 2989, 'mail_tracking_email group_user', True, False, False, False
# modificar_permisos(1, 2788, 2990, 'mail_tracking_event group_user', True, False, False, False
# modificar_permisos(1, 2789, 2993, 'access_cartera_avancys_line', True, True, True, True
# modificar_permisos(1, 2790, 2994, 'access_cartera_avancys_extended', True, True, True, True
# modificar_permisos(1, 2851, 3026, 'access.instituciones.estudios.capacitaciones', True, True, True, True
# modificar_permisos(1, 2852, 3027, 'access.titulos.educativos.estudios.capacitaciones', True, True, True, True
# modificar_permisos(1, 2853, 3028, 'access.tipo.estudios.capacitaciones', True, True, True, True
# modificar_permisos(1, 2854, 3029, 'access.estado.estudios.capacitaciones', True, True, True, True
# modificar_permisos(1, 2855, 3030, 'access.tipo.duracion.estudios.capacitaciones', True, True, True, True
# modificar_permisos(1, 2856, 3025, 'access.estudios.capacitaciones', True, True, True, True
# modificar_permisos(1, 2878, 3093, 'access_quoter_position_service', True, True, True, True
# modificar_permisos(1, 2879, 3041, 'access_sale_quoter_line', True, True, True, True
# modificar_permisos(1, 2880, 3040, 'access_sale_quoter', True, True, True, True
# modificar_permisos(1, 2881, 3042, 'access_quoter_amount_day', True, True, True, True
# modificar_permisos(1, 2882, 3043, 'access_quoter_rate_type', True, True, True, True
# modificar_permisos(1, 2883, 3044, 'access_quoter_dotation', True, True, True, True
# modificar_permisos(1, 2884, 3045, 'access_quoter_dotation_line', True, True, True, True
# modificar_permisos(1, 2885, 3046, 'access_quoter_dotation_line_aux', True, True, True, True
# modificar_permisos(1, 2886, 3047, 'access_quoter_additional_dotation', True, True, True, True
# modificar_permisos(1, 2887, 3048, 'access_quoter_additional_dotation_line', True, True, True, True
# modificar_permisos(1, 2888, 3049, 'access_quoter_additional_dotation_line_aux', True, True, True, True
# modificar_permisos(1, 2889, 3050, 'access_quoter_dotation_protection', True, True, True, True
# modificar_permisos(1, 2890, 3051, 'access_quoter_dotation_protection_line', True, True, True, True
# modificar_permisos(1, 2891, 3052, 'access_quoter_dotation_protection_line_aux', True, True, True, True
# modificar_permisos(1, 2892, 3053, 'access_quoter_dotation_position', True, True, True, True
# modificar_permisos(1, 2893, 3054, 'access_quoter_dotation_position_line', True, True, True, True
# modificar_permisos(1, 2894, 3055, 'access_quoter_dotation_position_line_aux', True, True, True, True
# modificar_permisos(1, 2895, 3056, 'access_quoter_dotation_additional_position', True, True, True, True
# modificar_permisos(1, 2896, 3057, 'access_quoter_dotation_additional_position_line', True, True, True, True
# modificar_permisos(1, 2897, 3058, 'access_quoter_dotation_additional_position_line_aux', True, True, True, True
# modificar_permisos(1, 2898, 3059, 'access_quoter_service_mod', True, True, True, True
# modificar_permisos(1, 2899, 3060, 'access_quoter_weapon_type', True, True, True, True
# modificar_permisos(1, 2900, 3061, 'access_quoter_weapon_type_line', True, True, True, True
# modificar_permisos(1, 2901, 3062, 'access_quoter_weapon_type_line_aux', True, True, True, True
# modificar_permisos(1, 2902, 3063, 'access_quoter_communication', True, True, True, True
# modificar_permisos(1, 2903, 3064, 'access_quoter_communication_line', True, True, True, True
# modificar_permisos(1, 2904, 3065, 'access_quoter_communication_line_aux', True, True, True, True
# modificar_permisos(1, 2905, 3066, 'access_quoter_communication_line_aditional_aux', True, True, True, True
# modificar_permisos(1, 2907, 3068, 'access_quoter_canine', True, True, True, True
# modificar_permisos(1, 2908, 3069, 'access_quoter_canine_line', True, True, True, True
# modificar_permisos(1, 2909, 3070, 'access_quoter_canine_line_aux', True, True, True, True
# modificar_permisos(1, 2910, 3071, 'access_quoter_support', True, True, True, True
# modificar_permisos(1, 2911, 3072, 'access_quoter_support_line', True, True, True, True
# modificar_permisos(1, 2912, 3073, 'access_quoter_support_line_aux', True, True, True, True
# modificar_permisos(1, 2913, 3074, 'access_quoter_selection', True, True, True, True
# modificar_permisos(1, 2914, 3075, 'access_quoter_selection_line', True, True, True, True
# modificar_permisos(1, 2915, 3076, 'access_quoter_selection_line_aux', True, True, True, True
# modificar_permisos(1, 2916, 3077, 'access_quoter_training', True, True, True, True
# modificar_permisos(1, 2917, 3078, 'access_quoter_training_line', True, True, True, True
# modificar_permisos(1, 2918, 3079, 'access_quoter_policy_line', True, True, True, True
# modificar_permisos(1, 2919, 3080, 'access_quoter_fivep', True, True, True, True
# modificar_permisos(1, 2920, 3081, 'access_fivep_state', True, True, True, True
# modificar_permisos(1, 2921, 3082, 'access_quoter_technology', True, True, True, True
# modificar_permisos(1, 2922, 3083, 'access_quoter_financing', True, True, True, True
# modificar_permisos(1, 2924, 3084, 'access_quoter_conf_account', True, True, True, True
# modificar_permisos(1, 2926, 3089, 'access_quoter_segment', True, True, True, True
# modificar_permisos(1, 2927, 3085, 'access_quoter_transport', True, True, True, True
# modificar_permisos(1, 2928, 3086, 'access_quoter_vehicle', True, True, True, True
# modificar_permisos(1, 2929, 3090, 'access_sale_quoter_stage', True, True, True, True
# modificar_permisos(1, 2930, 3087, 'access_quoter_position', True, True, True, True
# modificar_permisos(1, 2931, 3088, 'access_quoter_freelance', True, True, True, True
# modificar_permisos(1, 2932, 3091, 'access_order_quoter_line_detail', True, True, True, True
# modificar_permisos(1, 2933, 3092, 'access_wizard_project_service_order_line', True, True, True, True
# modificar_permisos(1, 2934, 3094, 'x_hr.requisicion.usuario_interno', True, True, False, False
# modificar_permisos(1, 2937, 3095, 'x_hr.requisicion.estado.usuario_interno', True, True, True, True
# modificar_permisos(1, 2939, 3096, 'x_hr.requisicion.motivo.usuario_interno', True, False, False, True
# modificar_permisos(1, 2941, 3099, 'x_hr.requisicion.linea.usuario_interno', True, True, False, False
# modificar_permisos(1, 2943, 3097, 'x_hr.requisicion.linea.estado.usuario_interno', True, True, True, True
# modificar_permisos(1, 2945, 3098, 'x_hr.requisicion.linea.tipo.vehiculo.usuario_interno', True, True, True, True
# modificar_permisos(1, 2947, 3100, 'x_hr.requisicion.dotacion.usuario_interno', True, True, True, True
# modificar_permisos(1, 2949, 3101, 'x_hr.requisicion.estructura.salarial.usuario_interno', True, False, False, False
# modificar_permisos(1, 2965, 3272, 'x_tags.usuario_interno', True, True, True, True
# modificar_permisos(1, 2995, 3241, 'programa.usuario_interno', True, True, True, True
# modificar_permisos(1, 2998, 3181, 'procesos_disciplinarios.procesos_disciplinarios', True, True, True, False
# modificar_permisos(1, 3120, 3239, 'x_sedes.usuario_interno', True, True, True, True
# modificar_permisos(1, 3122, 3238, 'x_operaciones.estado.usuario_interno', True, False, False, False
# modificar_permisos(1, 3124, 3240, 'x_coordinador.de.apoyo.usuario_interno', True, True, True, True
# modificar_permisos(1, 3143, 3243, 'access_x_sub_motivo_user', True, True, True, False
# modificar_permisos(1, 3145, 3244, 'access_x_estado_medida_user', True, True, True, False
# modificar_permisos(1, 3161, 3254, 'access_x_estado_proceso_user', True, True, True, False
# modificar_permisos(1, 3165, 3256, 'x_modelo.prueba.usuario_interno', True, True, True, True
# modificar_permisos(1, 3167, 3257, 'x_modelo.prueba.estado.usuario_interno', True, False, False, False
# modificar_permisos(1, 3188, 3259, 'access_x_employee_bank_line_user', True, True, True, False
# modificar_permisos(1, 3205, 3271, 'x_mos.usuario_interno', True, True, True, True
# modificar_permisos(1, 3214, 3294, 'x_visita.cliente.usuario_interno', True, True, True, True
# modificar_permisos(2, 3, 7, 'ir_model_group_erp_manager', True, True, True, True
# modificar_permisos(2, 4, 12, 'ir_model_fields_group_erp_manager', True, True, True, True
# modificar_permisos(2, 5, 13, 'ir_model_fields_selection_group_erp_manager', True, True, True, True
# modificar_permisos(2, 6, 8, 'ir_model_constraint_group_erp_manager', True, True, True, True
# modificar_permisos(2, 7, 9, 'ir_model_relation_group_erp_manager', True, True, True, True
# modificar_permisos(2, 8, 10, 'ir_model_access_group_erp_manager', True, True, True, True
# modificar_permisos(2, 9, 11, 'ir_model_data_group_erp_manager', True, True, True, True
# modificar_permisos(2, 16, 103, 'access.reset.view.arch.wizard', True, True, True, False
# modificar_permisos(2, 29, 92, 'ir_filters_all', True, True, True, True
# modificar_permisos(2, 34, 24, 'ir_rule_group_erp_manager', True, True, True, True
# modificar_permisos(2, 60, 98, 'ir_logging_admin', True, True, True, True
# modificar_permisos(2, 62, 18, 'ir_module_category_group_user', True, False, False, False
# modificar_permisos(2, 88, 40, 'res_company_group_erp_manager', True, True, True, True
# modificar_permisos(2, 89, 53, 'res_groups_group_erp_manager', True, True, True, False
# modificar_permisos(2, 91, 70, 'res_users_group_erp_manager', True, True, True, True
# modificar_permisos(2, 93, 110, 'access.change.password.wizard', True, True, True, False
# modificar_permisos(2, 94, 111, 'access.change.password.user', True, True, True, False
# modificar_permisos(2, 137, 151, 'barcode.nomenclature.manager', True, True, True, True
# modificar_permisos(2, 138, 153, 'barcode.rule.manager', True, True, True, True
# modificar_permisos(2, 349, 249, 'Goal Definition Manager', True, True, True, True
# modificar_permisos(2, 350, 246, 'Goal Manager', True, True, True, True
# modificar_permisos(2, 351, 252, 'Goal Challenge Manager', True, True, True, True
# modificar_permisos(2, 352, 255, 'Challenge Line Manager', True, True, True, True
# modificar_permisos(2, 353, 262, 'Badge-user Manager', True, True, True, True
# modificar_permisos(2, 354, 258, 'Badge Manager', True, True, True, True
# modificar_permisos(2, 425, 386, 'digest.digest.administration', True, True, True, True
# modificar_permisos(2, 426, 388, 'digest.tip.administration', True, True, True, True
# modificar_permisos(2, 2722, 2923, 'auditlog_rule_manager', True, True, True, True
# modificar_permisos(2, 2723, 2927, 'auditlog_http_session_manager', True, True, True, True
# modificar_permisos(2, 2724, 2928, 'auditlog_http_request_manager', True, True, True, True
# modificar_permisos(2, 2725, 2924, 'auditlog_log_manager', True, True, True, True
# modificar_permisos(2, 2726, 2925, 'auditlog_log_line_manager', True, True, True, True
# modificar_permisos(2, 2727, 2926, 'auditlog_log_line_view', True, False, False, False
# modificar_permisos(3, 10, 2200, 'access.wizard.ir.model.menu.create', True, True, True, False
# modificar_permisos(3, 11, 2269, 'ir_sequence_group_system', True, True, True, True
# modificar_permisos(3, 12, 2262, 'ir_sequence_date_range_group_system', True, True, True, True
# modificar_permisos(3, 13, 2245, 'ir_ui_menu_group_system', True, True, True, True
# modificar_permisos(3, 15, 2292, 'ir_ui_view_group_system', True, True, True, True
# modificar_permisos(3, 16, 2199, 'reset_view_arch_wizard_group_system', True, True, True, False
# modificar_permisos(3, 17, 2185, 'ir_actions_group_system', True, True, True, True
# modificar_permisos(3, 18, 2191, 'ir_actions_act_window_system', True, True, True, True
# modificar_permisos(3, 19, 2294, 'ir_actions_act_window_view_group_system', True, True, True, True
# modificar_permisos(3, 20, 2212, 'ir_actions_act_window_close_group_system', True, True, True, True
# modificar_permisos(3, 21, 2285, 'ir_actions_act_url_group_system', True, True, True, True
# modificar_permisos(3, 22, 2190, 'ir_actions_server_group_system', True, True, True, True
# modificar_permisos(3, 23, 2244, 'ir_server_object_lines_group_system', True, True, True, True
# modificar_permisos(3, 24, 2203, 'ir_actions_todo_group_system', True, True, True, True
# modificar_permisos(3, 25, 2188, 'ir_actions_client_all', True, True, True, True
# modificar_permisos(3, 26, 2189, 'ir_actions_report_group_system', True, True, True, True
# modificar_permisos(3, 28, 2186, 'ir_cron_group_cron', True, True, True, True
# modificar_permisos(3, 30, 2291, 'ir_default_group_system', True, True, True, True
# modificar_permisos(3, 31, 2283, 'ir_translation_group_system', True, True, True, True
# modificar_permisos(3, 35, 2251, 'ir_config_parameter_system', True, True, True, True
# modificar_permisos(3, 37, 2272, 'ir_mail_server', True, True, True, True
# modificar_permisos(3, 61, 2257, 'ir_property_group_system', True, True, True, False
# modificar_permisos(3, 63, 2248, 'ir_module_module_group_user', True, True, True, True
# modificar_permisos(3, 64, 2220, 'ir_module_module_dependency_group_system', True, True, True, True
# modificar_permisos(3, 65, 2231, 'ir_module_module_exclusion_group_system', True, True, True, True
# modificar_permisos(3, 66, 2219, 'access.ir.demo', True, True, True, False
# modificar_permisos(3, 67, 2232, 'access.ir.demo_failure', True, True, True, False
# modificar_permisos(3, 68, 2202, 'access.ir.demo_failure.wizard', True, True, True, False
# modificar_permisos(3, 70, 2215, 'ir_actions_report_paperformat_group_system', True, True, True, True
# modificar_permisos(3, 72, 2252, 'res_country_group_system', True, True, True, True
# modificar_permisos(3, 75, 2237, 'res_lang_group_user', True, True, True, True
# modificar_permisos(3, 80, 2268, 'res_partner_industry_group_system', True, True, True, True
# modificar_permisos(3, 81, 2205, 'res_bank_group_system', True, True, True, True
# modificar_permisos(3, 83, 2213, 'access.res.config', True, True, True, False
# modificar_permisos(3, 84, 2239, 'access.res.config.installer', True, True, True, False
# modificar_permisos(3, 85, 2250, 'access.res.config.settings', True, True, True, False
# modificar_permisos(3, 86, 2247, 'res_currency_group_system', True, True, True, True
# modificar_permisos(3, 87, 2276, 'res_currency_rate_group_system', True, True, True, True
# modificar_permisos(3, 98, 2256, 'decimal.precision_configuration', True, True, True, True
# modificar_permisos(3, 100, 2193, 'access.base.module.update', True, True, True, False
# modificar_permisos(3, 101, 2240, 'access.base.language.install', True, True, True, False
# modificar_permisos(3, 102, 2238, 'access.base.language.import', True, True, True, False
# modificar_permisos(3, 103, 2194, 'access.base.module.upgrade', True, True, True, False
# modificar_permisos(3, 104, 2221, 'access.base.module.uninstall', True, True, True, False
# modificar_permisos(3, 106, 2192, 'access.base.update.translations', True, True, True, False
# modificar_permisos(3, 110, 2224, 'access.base.document.layout', True, True, True, False
# modificar_permisos(3, 133, 2263, 'access_web_tour_tour_admin', True, False, True, False
# modificar_permisos(3, 135, 2210, 'uom.category.manager', True, True, True, True
# modificar_permisos(3, 136, 2286, 'uom.uom.manager', True, True, True, True
# modificar_permisos(3, 143, 2277, 'resource.calendar.system', True, True, True, True
# modificar_permisos(3, 144, 2223, 'resource.calendar.attendance.system', True, True, True, True
# modificar_permisos(3, 145, 2264, 'resource.resource', True, False, False, False
# modificar_permisos(3, 146, 2616, 'resource.calendar.leaves', True, True, True, True
# modificar_permisos(3, 148, 2227, 'mail.utm.stage', True, True, True, True
# modificar_permisos(3, 150, 2207, 'utm.campaign.system', True, True, True, True
# modificar_permisos(3, 152, 2229, 'utm.tag', True, True, True, True
# modificar_permisos(3, 154, 2218, 'iap.account.manager', True, True, True, True
# modificar_permisos(3, 156, 2288, 'mail.tracking.value.system', True, True, True, True
# modificar_permisos(3, 157, 2274, 'mail.alias.system', True, True, True, True
# modificar_permisos(3, 159, 2270, 'mail.followers.system', True, True, True, True
# modificar_permisos(3, 160, 2249, ' mail.notification.system', True, True, True, True
# modificar_permisos(3, 163, 2738, 'mail.activity.type.system', True, True, True, True
# modificar_permisos(3, 166, 2217, 'mail.mail.system', True, True, True, True
# modificar_permisos(3, 170, 2181, 'access_mail_blacklist_system', True, True, True, True
# modificar_permisos(3, 174, 2255, 'mail.template_system', True, True, True, True
# modificar_permisos(3, 192, 2201, 'acesss.mail.blacklist.remove.system', True, True, True, True
# modificar_permisos(3, 346, 2216, 'access_calendar_contacts', True, True, True, True
# modificar_permisos(3, 347, 2278, 'calendar.event.type.manager', True, True, True, True
# modificar_permisos(3, 348, 2273, 'fetchmail.server', True, True, True, True
# modificar_permisos(3, 355, 2260, 'gamification.karma.rank.access.user.manager', True, True, True, True
# modificar_permisos(3, 356, 2271, 'gamification.karma.tracking.access.user.manager', True, True, True, True
# modificar_permisos(3, 370, 2182, 'access.phone.blacklist.system', True, True, True, True
# modificar_permisos(3, 373, 2225, 'acesss.phone.blacklist.remove.system', True, True, True, True
# modificar_permisos(3, 374, 2743, 'product.template.manager', True, True, True, True
# modificar_permisos(3, 375, 2211, 'product.category.manager', True, True, True, True
# modificar_permisos(3, 376, 2184, 'product.product manager', True, True, True, True
# modificar_permisos(3, 377, 2226, 'product.packaging.manager', True, True, True, True
# modificar_permisos(3, 378, 2241, 'product.supplierinfo.manager', True, True, True, True
# modificar_permisos(3, 379, 2204, 'product.attribute manager', True, True, True, True
# modificar_permisos(3, 380, 2289, 'product.attribute value manager', True, True, True, True
# modificar_permisos(3, 381, 2242, 'product.template.attribute line manager', True, True, True, True
# modificar_permisos(3, 382, 2287, 'product.template.attribute value manager', True, True, True, True
# modificar_permisos(3, 383, 2230, 'product.template.attribute exclusion manager', True, True, True, True
# modificar_permisos(3, 384, 2290, 'product.attribute.custom value manager', True, True, True, True
# modificar_permisos(3, 385, 2243, 'product.pricelist.manager', True, True, True, True
# modificar_permisos(3, 386, 2265, 'product.pricelist.item.manager', True, True, True, True
# modificar_permisos(3, 388, 2206, 'rating.rating.access.system', True, True, True, True
# modificar_permisos(3, 399, 2275, 'res.partner.autocomplete.sync.system', True, True, True, True
# modificar_permisos(3, 407, 2267, 'access.sms.sms.system', True, True, True, True
# modificar_permisos(3, 408, 2254, 'access.sms.template.system', True, True, True, True
# modificar_permisos(3, 414, 2209, 'snailmail.letter.system', True, True, True, True
# modificar_permisos(3, 556, 2295, 'access_theme_ir_ui_view', True, True, True, True
# modificar_permisos(3, 557, 2195, 'access_theme_ir_attachment', True, True, True, True
# modificar_permisos(3, 558, 2246, 'access_theme_website_menu', True, True, True, True
# modificar_permisos(3, 559, 2258, 'access_theme_website_page', True, True, True, True
# modificar_permisos(3, 561, 2259, 'access_website_track_system', True, True, True, True
# modificar_permisos(3, 562, 2293, 'access_website_visitor_system', True, True, False, True
# modificar_permisos(3, 563, 2233, 'access_website_dynamic_filter', True, True, True, True
# modificar_permisos(3, 570, 2196, 'payment.acquirer.system', True, True, True, True
# modificar_permisos(3, 571, 2236, 'payment.icon.system', True, True, True, True
# modificar_permisos(3, 572, 2284, 'payment.transaction.system', True, True, True, True
# modificar_permisos(3, 573, 2282, 'payment.token.system', True, True, True, True
# modificar_permisos(3, 574, 2197, 'access.payment.acquirer.onboarding.wizard', True, True, True, False
# modificar_permisos(3, 648, 2198, 'access.sale.payment.acquirer.onboarding.wizard', True, True, True, False
# modificar_permisos(3, 680, 2253, 'sale.order.template', True, False, False, False
# modificar_permisos(3, 683, 2280, 'date_range.date_range_type.config', True, True, True, True
# modificar_permisos(3, 684, 2261, 'date_range.date_range.config', True, True, True, True
# modificar_permisos(3, 685, 2235, 'access_date_range_generator', True, True, True, True
# modificar_permisos(3, 718, 2234, 'access_crm_lead_scoring_frequency_system', True, False, False, False
# modificar_permisos(3, 719, 2208, 'access_crm_lead_scoring_frequency_field_system', True, False, False, False
# modificar_permisos(3, 1175, 2281, 'access_account_tax_group_type_manager', True, True, True, True
# modificar_permisos(3, 1364, 2214, 'google.drive.config', True, True, True, True
# modificar_permisos(3, 1561, 2228, 'access_helpdesk_stages_manager', True, True, True, True
# modificar_permisos(3, 1628, 2266, 'google_calendar_account_reset_access_right', True, True, True, False
# modificar_permisos(3, 1629, 2187, 'base.automation config', True, True, True, True
# modificar_permisos(3, 1945, 2437, 'ir_actions_account_report_download_group_system', True, True, True, True
# modificar_permisos(3, 2787, 2991, 'mail_tracking_email group_system', True, True, True, True
# modificar_permisos(3, 2788, 2992, 'mail_tracking_event group_system', True, True, True, True
# modificar_permisos(6, 1351, 1561, 'access.res.partner.driver.admin', True, True, True, True
# modificar_permisos(7, 32, 5, 'ir_exports_group_system', True, True, True, True
# modificar_permisos(8, 72, 45, 'res_country_group_user', True, False, False, False
# modificar_permisos(8, 73, 48, 'res_country_group_group_user', True, True, True, True
# modificar_permisos(8, 74, 47, 'res_country_state_group_user', True, True, True, True
# modificar_permisos(8, 77, 64, 'res_partner_category_group_partner_manager', True, True, True, True
# modificar_permisos(8, 78, 67, 'res_partner_title_group_partner_manager', True, True, True, True
# modificar_permisos(8, 79, 59, 'res_partner_group_partner_manager', True, True, True, True
# modificar_permisos(8, 107, 119, 'access.base.partner.merge.line', True, True, True, True
# modificar_permisos(8, 108, 120, 'access.base.partner.merge.automatic.wizard', True, True, True, False
# modificar_permisos(8, 134, 144, 'res_city_group_user', True, False, False, False
# modificar_permisos(8, 343, 2740, 'calendar.event.partner.manager', True, True, True, True
# modificar_permisos(8, 385, 295, 'product.pricelist partner manager', True, False, False, False
# modificar_permisos(8, 401, 345, 'access.portal.share', True, True, True, False
# modificar_permisos(8, 402, 346, 'access.portal.wizard', True, True, True, False
# modificar_permisos(8, 403, 347, 'access.portal.wizard.user', True, True, True, False
# modificar_permisos(8, 433, 2759, 'account.account partner manager', True, False, False, False
# modificar_permisos(8, 506, 535, 'stock.location.partner.manager', True, False, False, False
# modificar_permisos(8, 581, 684, 'latam id type manager', True, True, False, False
# modificar_permisos(8, 715, 1020, 'crm.lead.partner.manager', True, False, False, False
# modificar_permisos(8, 760, 1154, 'access.res.partner.document.type.partner.manager', True, True, True, True
# modificar_permisos(8, 915, 1156, 'access_hr_payslip_line_report_manager_payslip', True, True, True, True
# modificar_permisos(8, 1178, 1395, 'res_city_zip group_user', True, True, True, True
# modificar_permisos(8, 1180, 1398, 'res.partner.id_number', True, True, True, True
# modificar_permisos(8, 1181, 1400, 'res.partner.id_category', True, True, True, True
# modificar_permisos(8, 1185, 1407, 'product.brand', True, True, True, True
# modificar_permisos(8, 1340, 1531, 'delivery.carrier partner_manager', True, False, False, False
# modificar_permisos(8, 1351, 1560, 'access.res.partner.driver.manager', True, True, True, False
# modificar_permisos(8, 1358, 1575, 'crm.claim.partner.manager', True, False, False, False
# modificar_permisos(9, 29, 94, 'ir_filters_all', True, True, True, True
# modificar_permisos(9, 79, 2386, 'access_res_partner_portal', True, False, False, False
# modificar_permisos(9, 79, 58, 'res_partner_group_portal', True, False, False, False
# modificar_permisos(9, 91, 2973, 'user_porta.', True, False, False, False
# modificar_permisos(9, 92, 73, 'id_check_portal', True, True, True, False
# modificar_permisos(9, 95, 75, 'API_keys_access_portal', True, False, False, False
# modificar_permisos(9, 96, 77, 'API_key_wizard', True, False, True, False
# modificar_permisos(9, 111, 385, 'auth_totp_portal wizard access rules', True, True, True, True
# modificar_permisos(9, 141, 156, 'bus.presence', True, True, True, True
# modificar_permisos(9, 156, 204, 'mail.tracking.value.portal', False, False, False, False
# modificar_permisos(9, 160, 189, 'mail.notification.portal', True, False, False, False
# modificar_permisos(9, 162, 180, 'mail.message.portal', True, True, True, True
# modificar_permisos(9, 166, 183, 'mail.mail.portal', False, False, False, False
# modificar_permisos(9, 171, 195, 'mail.channel.partner.portal', True, True, True, True
# modificar_permisos(9, 175, 211, 'mail.shortcode.portal', True, False, False, False
# modificar_permisos(9, 193, 220, 'access.mail.compose.message.portal', True, True, True, False
# modificar_permisos(9, 341, 232, 'calendar.attendee_portal', False, False, False, False
# modificar_permisos(9, 343, 235, 'calendar.event_all_user', True, False, False, False
# modificar_permisos(9, 349, 250, 'Goal Definition Portal', True, False, False, False
# modificar_permisos(9, 350, 247, 'Goal Portal', True, True, False, False
# modificar_permisos(9, 351, 253, 'Goal Challenge Portal', True, False, False, False
# modificar_permisos(9, 352, 256, 'Challenge Line Portal', True, False, False, False
# modificar_permisos(9, 353, 263, 'Badge-user Portal', True, True, True, False
# modificar_permisos(9, 354, 259, 'Badge Portal', True, False, False, False
# modificar_permisos(9, 360, 1514, 'access_hr_employee_portal', True, False, False, False
# modificar_permisos(9, 364, 1512, 'access_hr_job_portal', True, False, False, False
# modificar_permisos(9, 388, 318, 'rating.rating.portal', False, False, False, False
# modificar_permisos(9, 391, 1511, 'access_hr_contract_portal', True, False, False, False
# modificar_permisos(9, 399, 342, 'res.partner.autocomplete.sync.portal', True, False, True, False
# modificar_permisos(9, 448, 2604, 'account.move', True, False, False, False
# modificar_permisos(9, 448, 2750, 'account.move.portal', True, False, False, False
# modificar_permisos(9, 449, 2751, 'account.move.line.portal', True, False, False, False
# modificar_permisos(9, 515, 919, 'stock.picking', True, False, False, False
# modificar_permisos(9, 573, 665, 'payment.token.portal', True, True, True, True
# modificar_permisos(9, 643, 778, 'sale.order.portal', True, False, False, False
# modificar_permisos(9, 644, 779, 'sale.order.line.portal', True, False, False, False
# modificar_permisos(9, 709, 964, 'purchase.order.portal', True, False, False, False
# modificar_permisos(9, 710, 969, 'purchase.order.line.portal', True, False, False, False
# modificar_permisos(9, 881, 1510, 'access_hr_period_portal_payslip', True, False, False, False
# modificar_permisos(9, 924, 1176, 'task_type_portal', True, False, False, False
# modificar_permisos(9, 925, 1183, 'project_portal', True, False, False, False
# modificar_permisos(9, 926, 1181, 'task_portal', True, False, False, False
# modificar_permisos(9, 927, 1189, 'project_tags_portal', True, False, False, False
# modificar_permisos(9, 1548, 1735, 'access_dms_access_group_portal', True, False, False, False
# modificar_permisos(9, 1552, 1723, 'dms_storage_portal', True, False, False, False
# modificar_permisos(9, 1553, 1727, 'dms_directory_portal', True, False, False, False
# modificar_permisos(9, 1554, 1731, 'dms_file_portal', True, False, False, False
# modificar_permisos(9, 2787, 2988, 'mail_tracking_email group_portal', True, False, False, False
# modificar_permisos(10, 29, 95, 'ir_filters_all', True, True, True, True
# modificar_permisos(10, 79, 57, 'res_partner_group_public', True, False, False, False
# modificar_permisos(10, 171, 194, 'mail.channel.partner.public', True, False, False, False
# modificar_permisos(10, 353, 264, 'Badge-user Public', True, False, False, False
# modificar_permisos(10, 354, 260, 'Badge Public', True, False, False, False
# modificar_permisos(10, 363, 686, 'hr.department.public', True, False, False, False
# modificar_permisos(10, 388, 317, 'rating.rating.public', False, False, False, False
# modificar_permisos(10, 1548, 1734, 'access_dms_access_group_public', True, False, False, False
# modificar_permisos(10, 1553, 1726, 'dms_directory_public', True, False, False, False
# modificar_permisos(10, 1554, 1730, 'dms_file_public', True, False, False, False
# modificar_permisos(10, 2787, 2987, 'mail_tracking_email group_public', True, False, False, False
# modificar_permisos(13, 336, 231, 'access_account_analytic_distribution', True, True, True, True
# modificar_permisos(13, 337, 229, 'access_account_analytic_tag', True, True, True, True
# modificar_permisos(13, 338, 230, 'access_account_analytic_group', True, True, True, True
# modificar_permisos(13, 339, 2739, 'access_account_analytic_account', True, False, False, False
# modificar_permisos(13, 340, 228, 'access_account_analytic_line', True, True, True, True
# modificar_permisos(13, 450, 515, 'account.analytic.default analytic', True, False, False, False
# modificar_permisos(15, 143, 321, 'hr.employee.resource.calendar.user', True, True, True, True
# modificar_permisos(15, 144, 322, 'hr.employee.resource.calendar.attendance.user', True, True, True, True
# modificar_permisos(15, 145, 276, 'resource.resource.user', True, True, True, True
# modificar_permisos(15, 351, 325, 'Challenge Officer', True, True, True, True
# modificar_permisos(15, 352, 326, 'Challenge Line Officer', True, True, True, True
# modificar_permisos(15, 353, 328, 'Badge-user Officer', True, True, True, True
# modificar_permisos(15, 354, 327, 'Badge Officer', True, True, True, True
# modificar_permisos(15, 360, 273, 'hr.employee user', True, True, True, True
# modificar_permisos(15, 361, 271, 'hr.employee.category.user', True, True, True, True
# modificar_permisos(15, 363, 277, 'hr.department.user', True, True, True, True
# modificar_permisos(15, 364, 279, 'hr.job', True, True, True, False
# modificar_permisos(15, 365, 282, 'access_hr_plan_activity_type', True, True, True, True
# modificar_permisos(15, 366, 283, 'access_hr_plan_hr_user', True, True, True, True
# modificar_permisos(15, 368, 285, 'access.hr.departure.wizard', True, True, True, False
# modificar_permisos(15, 393, 329, 'hr.resume.line', True, True, True, True
# modificar_permisos(15, 394, 331, 'hr.resume.line.type', True, True, True, True
# modificar_permisos(15, 395, 337, 'hr.skill', True, True, True, True
# modificar_permisos(15, 396, 339, 'hr.employee.skill', True, True, True, True
# modificar_permisos(15, 397, 335, 'hr.skill.level', True, True, True, True
# modificar_permisos(15, 398, 333, 'hr.skill.type', True, True, True, True
# modificar_permisos(15, 1032, 1270, 'hr.branch.user', True, False, False, False
# modificar_permisos(16, 145, 320, 'hr.employee.resource.manager', True, True, True, True
# modificar_permisos(16, 367, 284, 'access.hr.plan.wizard', True, True, True, False
# modificar_permisos(22, 391, 323, 'hr.contract.manager', True, True, True, True
# modificar_permisos(22, 392, 324, 'hr.payroll.structure.type.contract.manager', True, True, True, True
# modificar_permisos(23, 354, 383, 'gamification.badge.survey.user', True, True, True, True
# modificar_permisos(23, 419, 365, 'survey.survey.survey.user', True, True, True, True
# modificar_permisos(23, 420, 369, 'survey.question.survey.user', True, True, True, True
# modificar_permisos(23, 421, 373, 'survey.question.answer.survey.user', True, True, True, True
# modificar_permisos(23, 422, 377, 'survey.user_input.survey.user', True, True, True, True
# modificar_permisos(23, 423, 381, 'survey.user_input.line.survey.user', True, True, True, True
# modificar_permisos(23, 424, 384, 'access.survey.invite', True, True, True, False
# modificar_permisos(24, 419, 366, 'survey.survey.survey.manager', True, True, True, True
# modificar_permisos(24, 420, 370, 'survey.question.survey.manager', True, True, True, True
# modificar_permisos(24, 421, 374, 'survey.question.answer.survey.manager', True, True, True, True
# modificar_permisos(24, 422, 378, 'survey.user_input.survey.manager', True, True, True, True
# modificar_permisos(24, 423, 382, 'survey.user_input.line.survey.manager', True, True, True, True
# modificar_permisos(27, 340, 2754, 'account.analytic.line invoice', True, False, False, False
# modificar_permisos(27, 376, 417, 'product.product.account.user', True, False, False, False
# modificar_permisos(27, 431, 462, 'account.account.tag', True, False, False, False
# modificar_permisos(27, 432, 455, 'account.account.type readonly', True, False, False, False
# modificar_permisos(27, 433, 2758, 'account.account.readonly', True, False, False, False
# modificar_permisos(27, 434, 446, 'account.group', True, False, False, False
# modificar_permisos(27, 435, 448, 'account.root', True, False, False, False
# modificar_permisos(27, 437, 2756, 'account.journal', True, False, False, False
# modificar_permisos(27, 438, 2763, 'account.tax.group', True, False, False, False
# modificar_permisos(27, 439, 2761, 'account.tax', True, False, False, False
# modificar_permisos(27, 440, 465, 'account.tax repartition.line.invoice', True, False, False, False
# modificar_permisos(27, 441, 470, 'account.tax.report.invoice', True, False, False, False
# modificar_permisos(27, 442, 468, 'account.tax.report.line.invoice', True, False, False, False
# modificar_permisos(27, 443, 482, 'account.reconcile.model.partner.mapping.readonly', True, False, False, False
# modificar_permisos(27, 444, 479, 'account.reconcile.model.line.readonly', True, False, False, False
# modificar_permisos(27, 445, 476, 'account.reconcile.model.readonly', True, False, False, False
# modificar_permisos(27, 448, 2748, 'account.move readonly', True, False, False, False
# modificar_permisos(27, 449, 2749, 'account.move.line readonly', True, False, False, False
# modificar_permisos(27, 450, 514, 'account.analytic.default', True, False, False, False
# modificar_permisos(27, 451, 2765, 'account.partial.reconcile.readonly', True, False, False, False
# modificar_permisos(27, 452, 488, 'account.full.reconcile.group.invoice', True, False, False, False
# modificar_permisos(27, 454, 497, 'account.payment', True, False, False, False
# modificar_permisos(27, 458, 421, 'account.bank.statement.group.invoice', True, False, False, False
# modificar_permisos(27, 459, 423, 'account.bank.statement.line.group.invoice', True, False, False, False
# modificar_permisos(27, 470, 390, 'account.cash.rounding', True, False, False, False
# modificar_permisos(27, 488, 406, 'account.invoice.report_user', True, False, False, False
# modificar_permisos(27, 508, 677, 'stock.move', True, False, False, False
# modificar_permisos(27, 515, 675, 'stock.picking', True, False, False, False
# modificar_permisos(27, 643, 791, 'sale.order.accountant', True, False, False, False
# modificar_permisos(27, 644, 776, 'sale.order.line accountant', True, False, False, False
# modificar_permisos(27, 676, 939, 'account.fiscal.year.user', True, False, False, False
# modificar_permisos(27, 709, 962, 'purchase.order', True, False, False, False
# modificar_permisos(27, 710, 967, 'purchase.order.line', True, False, False, False
# modificar_permisos(27, 940, 1213, 'wiz.account.asset.report', True, True, True, False
# modificar_permisos(27, 1927, 2426, 'account.report_manager', True, True, True, False
# modificar_permisos(27, 1928, 2428, 'account.report_footnote_readonly', True, False, False, False
# modificar_permisos(27, 1932, 2422, 'account.financial.html.report readonly', True, False, False, False
# modificar_permisos(27, 1933, 2425, 'account.financial.html.report.line readonly', True, False, False, False
# modificar_permisos(27, 1949, 2438, 'avancys_account_followup.followup.line', True, False, False, False
# modificar_permisos(28, 340, 438, 'account.analytic.line invoice', True, True, True, True
# modificar_permisos(28, 431, 463, 'account.account.tag', True, False, False, False
# modificar_permisos(28, 432, 893, 'account.account.type.account.invoice', True, True, True, False
# modificar_permisos(28, 432, 456, 'account.account.type invoice', True, False, False, False
# modificar_permisos(28, 433, 2760, 'account.account invoice', True, False, False, False
# modificar_permisos(28, 437, 2757, 'account.journal invoice', True, False, False, False
# modificar_permisos(28, 438, 2764, 'account.tax.group', True, False, False, False
# modificar_permisos(28, 439, 2762, 'account.tax', True, False, False, False
# modificar_permisos(28, 440, 466, 'account.tax repartition.line.invoice', True, False, False, False
# modificar_permisos(28, 443, 483, 'account.reconcile.model.partner.mapping.billing', True, False, True, False
# modificar_permisos(28, 444, 480, 'account.reconcile.model.line.billing', True, False, True, False
# modificar_permisos(28, 445, 477, 'account.reconcile.model.billing', True, False, True, False
# modificar_permisos(28, 448, 430, 'account.move', True, True, True, False
# modificar_permisos(28, 449, 432, 'account.move.line invoice', True, True, True, True
# modificar_permisos(28, 450, 516, 'account.analytic.default invoice', True, True, True, True
# modificar_permisos(28, 451, 486, 'account.partial.reconcile.group.invoice', True, True, True, True
# modificar_permisos(28, 452, 489, 'account.full.reconcile.group.invoice', True, True, True, True
# modificar_permisos(28, 454, 498, 'account.payment', True, True, True, True
# modificar_permisos(28, 458, 422, 'account.bank.statement.group.invoice', True, False, False, False
# modificar_permisos(28, 459, 424, 'account.bank.statement.line.group.invoice', True, False, False, False
# modificar_permisos(28, 470, 391, 'account.cash.rounding', True, True, True, True
# modificar_permisos(28, 474, 504, 'access.validate.account.move', True, True, True, False
# modificar_permisos(28, 476, 506, 'access.account.move.reversal', True, True, True, False
# modificar_permisos(28, 484, 513, 'access.account.invoice.send', True, True, True, False
# modificar_permisos(28, 485, 499, 'access.account.payment.register', True, True, True, False
# modificar_permisos(28, 488, 407, 'account.invoice.report_billing', True, False, False, False
# modificar_permisos(28, 508, 678, 'stock.move', True, True, True, False
# modificar_permisos(28, 515, 676, 'stock.picking', True, True, True, False
# modificar_permisos(28, 565, 639, 'account.edi.format', True, True, True, True
# modificar_permisos(28, 566, 641, 'account.edi.document', True, True, True, True
# modificar_permisos(28, 576, 672, 'access_snailmail_confirm_invoice', True, True, True, False
# modificar_permisos(28, 639, 765, 'account_debit_note_group_invoice', True, True, True, False
# modificar_permisos(28, 643, 811, 'sale.order', True, True, False, False
# modificar_permisos(28, 644, 812, 'sale.order.line', True, True, False, False
# modificar_permisos(28, 652, 876, 'account.move.account.invoice', True, True, True, False
# modificar_permisos(28, 653, 874, 'res.ciiu.account.invoice', True, True, True, False
# modificar_permisos(28, 654, 883, 'account.financial.report.balance.account.invoice', True, True, True, False
# modificar_permisos(28, 655, 885, 'account.financial.report.balance.line.account.invoice', True, True, True, False
# modificar_permisos(28, 656, 910, 'account.financial.report.balance.account.invoice', True, True, True, True
# modificar_permisos(28, 657, 912, 'account.financial.report.balance.line.account.invoice', True, True, True, True
# modificar_permisos(28, 658, 895, 'account.financial.report.taxes.account.invoice', True, True, True, False
# modificar_permisos(28, 659, 898, 'account.financial.report.taxes.line.account.invoice', True, True, True, False
# modificar_permisos(28, 661, 878, 'account.financial.structure.line.account.invoice', True, True, True, False
# modificar_permisos(28, 662, 881, 'account.financial.levels.account.invoice', True, True, True, False
# modificar_permisos(28, 663, 891, 'excel.report.avancys.account.invoice', True, True, True, False
# modificar_permisos(28, 664, 900, 'hr.payroll.advance.account.invoice', True, True, True, False
# modificar_permisos(28, 665, 2349, 'hr.expense.expense.account.invoice', True, True, True, False
# modificar_permisos(28, 666, 904, 'hr.expense.line.account.invoice', True, True, True, False
# modificar_permisos(28, 667, 906, 'hr.expense.tax.account.invoice', True, True, True, False
# modificar_permisos(28, 668, 908, 'account.financial.report.trial.wizard.account.invoice', True, True, True, False
# modificar_permisos(28, 669, 887, 'account.financial.report.balance.wizard.account.invoice', True, True, True, False
# modificar_permisos(28, 670, 889, 'account.financial.report.assistant.wizard.account.invoice', True, True, True, False
# modificar_permisos(28, 672, 931, 'access.account.advance.supplier.account.invoice', True, True, True, False
# modificar_permisos(28, 673, 933, 'account.advance.customer.account.invoice', True, True, True, False
# modificar_permisos(28, 674, 2418, 'account.voucher.account.invoice', True, True, True, False
# modificar_permisos(28, 674, 1295, 'account.voucher.user', True, True, True, False
# modificar_permisos(28, 675, 937, 'account.voucher.line.account.invoice', True, True, True, True
# modificar_permisos(28, 675, 1298, 'account.voucher.line.user', True, True, True, True
# modificar_permisos(28, 709, 963, 'purchase.order', True, True, False, False
# modificar_permisos(28, 710, 968, 'purchase.order.line', True, True, False, False
# modificar_permisos(28, 810, 1103, 'account.container.group.account.invoice', True, True, True, True
# modificar_permisos(28, 817, 1097, 'account.financial.report.balance.inventory.wizard.account_invoice', True, True, True, True
# modificar_permisos(28, 818, 1099, 'account.financial.report.major.balance.wizard.account_invoice', True, True, True, True
# modificar_permisos(28, 819, 1101, 'account.financial.report.state.income.wizard.account.invoice', True, True, True, True
# modificar_permisos(28, 820, 1093, 'account.financial.report.balance.general.wizard.account.invoice', True, True, True, False
# modificar_permisos(28, 821, 1095, 'account.financial.report.diario.wizard.account.invoice', True, True, True, False
# modificar_permisos(28, 932, 1200, 'account.asset', True, True, True, True
# modificar_permisos(28, 933, 1208, 'account.asset.group', True, False, False, False
# modificar_permisos(28, 934, 1197, 'account.asset.profile', True, False, False, False
# modificar_permisos(28, 935, 1203, 'account.asset.line', True, True, True, True
# modificar_permisos(28, 1033, 1279, 'access.account.move.group', True, True, True, True
# modificar_permisos(28, 1034, 1278, 'access.account.move.line.recocnile', True, True, True, True
# modificar_permisos(28, 1045, 1302, 'acces.account.consignment.invoice', True, True, True, False
# modificar_permisos(28, 1049, 1300, 'account.voucher.wizard.user', True, True, True, True
# modificar_permisos(28, 1112, 1313, 'account.change.difference', True, True, True, True
# modificar_permisos(28, 1113, 1314, 'account.return.change.difference', True, True, True, True
# modificar_permisos(28, 1176, 1391, 'account.asset.line.niff', True, True, True, True
# modificar_permisos(28, 1287, 2897, 'hr.roster.close.distribution', True, True, True, True
# modificar_permisos(28, 1648, 1858, 'credit_control_fin_invoice_line', True, False, False, False
# modificar_permisos(28, 1927, 2427, 'account.report_manager', True, True, True, True
# modificar_permisos(28, 1928, 2430, 'account.report_footnote', True, False, False, False
# modificar_permisos(28, 1932, 2421, 'account.financial.html.report invoice', True, False, False, False
# modificar_permisos(28, 1933, 2424, 'account.financial.html.report.line invoice', True, False, False, False
# modificar_permisos(28, 1949, 2439, 'avancys_account_followup.followup.line', True, False, False, False
# modificar_permisos(28, 2777, 2978, 'access_electronic_invoice_resolution_user', True, True, False, False
# modificar_permisos(28, 2778, 2981, 'access_ei_transaction_log_user', True, True, False, False
# modificar_permisos(28, 2779, 2984, 'access_ei_multi_process_user', True, True, True, False
# modificar_permisos(29, 339, 2755, 'account.analytic.account accountant', True, True, True, True
# modificar_permisos(29, 431, 461, 'account.account.tag', True, True, True, True
# modificar_permisos(29, 443, 484, 'account.reconcile.model.partner.mapping', True, True, True, True
# modificar_permisos(29, 444, 481, 'account.reconcile.model.line', True, True, True, True
# modificar_permisos(29, 445, 478, 'account.reconcile.model', True, True, True, True
# modificar_permisos(29, 451, 487, 'account.partial.reconcile', True, True, True, True
# modificar_permisos(29, 452, 490, 'account.full.reconcile', True, True, True, True
# modificar_permisos(29, 455, 420, 'account.bank.statement.cashbox.line', True, True, True, True
# modificar_permisos(29, 456, 419, 'account.bank.statement.cashbox', True, True, True, True
# modificar_permisos(29, 457, 500, 'access.account.bank.statement.closebalance', True, True, True, False
# modificar_permisos(29, 458, 425, 'account.bank.statement', True, True, True, True
# modificar_permisos(29, 459, 426, 'account.bank.statement.line', True, True, True, True
# modificar_permisos(29, 472, 501, 'access.account.automatic.entry.wizard', True, True, True, False
# modificar_permisos(29, 473, 502, 'access.account.unreconcile', True, True, True, False
# modificar_permisos(29, 475, 505, 'access.cash.box.out', True, True, True, False
# modificar_permisos(29, 477, 507, 'access.account.common.report', True, True, True, False
# modificar_permisos(29, 478, 508, 'access.account.common.journal.report', True, True, True, False
# modificar_permisos(29, 479, 509, 'access.account.print.journal', True, True, True, False
# modificar_permisos(29, 483, 512, 'access.tax.adjustments.wizard', True, True, True, False
# modificar_permisos(29, 575, 671, 'access.payment.link.wizard', True, True, True, False
# modificar_permisos(29, 643, 792, 'sale.order.accountant', True, True, False, False
# modificar_permisos(29, 644, 777, 'sale.order.line accountant', True, True, False, False
# modificar_permisos(29, 676, 1272, 'account.fiscal.year.user', True, False, False, False
# modificar_permisos(29, 932, 1201, 'account.asset', True, True, True, True
# modificar_permisos(29, 933, 1209, 'account.asset.group', True, False, False, False
# modificar_permisos(29, 934, 1198, 'account.asset.profile', True, False, False, False
# modificar_permisos(29, 935, 1204, 'account.asset.line', True, True, True, True
# modificar_permisos(29, 936, 1206, 'account.asset.recompute.trigger', True, True, True, True
# modificar_permisos(29, 938, 1212, 'account.asset.compute', True, True, True, True
# modificar_permisos(29, 939, 1211, 'account.asset.remove', True, True, True, True
# modificar_permisos(29, 1156, 1369, 'account.budget.post accountant', True, True, True, True
# modificar_permisos(29, 1157, 1370, 'crossovered.budget accountant', True, True, True, True
# modificar_permisos(29, 1158, 1371, 'crossovered.budget.lines accountant', True, True, True, True
# modificar_permisos(29, 1166, 1380, 'account.loan', True, True, True, True
# modificar_permisos(29, 1167, 1381, 'loan.move.line', True, True, True, True
# modificar_permisos(29, 1168, 1382, 'account.loan.prepaid', True, True, True, True
# modificar_permisos(29, 1169, 1383, 'account.loan.distribution', True, True, True, True
# modificar_permisos(29, 1176, 1392, 'account.asset.line.niff', True, True, True, True
# modificar_permisos(29, 1362, 1579, 'access.product.margin', True, True, True, False
# modificar_permisos(29, 1648, 1857, 'credit_control_fin_user_line', True, False, False, False
# modificar_permisos(29, 1928, 2429, 'account.report_footnote', True, True, True, True
# modificar_permisos(29, 1939, 2434, 'access_account_multicurrency_revaluation', True, False, False, False
# modificar_permisos(29, 1946, 2431, 'access.account_financial_reports.export.wizard', True, True, True, False
# modificar_permisos(29, 1947, 2432, 'access.account_financial_reports.export.wizard.format', True, True, True, False
# modificar_permisos(29, 1948, 2433, 'access.account.multicurrency.revaluation.wizard', True, True, True, False
# modificar_permisos(30, 79, 2744, 'res_partner group_account_manager', True, False, False, False
# modificar_permisos(30, 86, 404, 'res.currency account manager', True, True, True, True
# modificar_permisos(30, 87, 405, 'res.currency.rate account manager', True, True, True, True
# modificar_permisos(30, 340, 2752, 'account.analytic.line manager', True, False, False, False
# modificar_permisos(30, 374, 2745, 'product.template.account.manager', True, True, True, True
# modificar_permisos(30, 376, 418, 'product.product.account.manager', True, True, True, True
# modificar_permisos(30, 408, 2441, 'access.sms.template.account.manager', True, True, True, True
# modificar_permisos(30, 428, 411, 'account.fiscal.position account.manager', True, True, True, True
# modificar_permisos(30, 429, 412, 'account.fiscal.position.tax account.manager', True, True, True, True
# modificar_permisos(30, 430, 413, 'account.fiscal.position account.manager', True, True, True, True
# modificar_permisos(30, 432, 454, 'account.account.type', True, True, True, True
# modificar_permisos(30, 432, 892, 'account.account.type.manager', True, True, True, True
# modificar_permisos(30, 433, 449, 'account.account', True, True, True, True
# modificar_permisos(30, 434, 445, 'account.group', True, True, True, True
# modificar_permisos(30, 435, 447, 'account.root', True, False, False, False
# modificar_permisos(30, 436, 444, 'account.journal.group manager', True, True, True, True
# modificar_permisos(30, 437, 441, 'account.journal', True, True, True, True
# modificar_permisos(30, 438, 475, 'account.tax.group', True, True, True, True
# modificar_permisos(30, 439, 460, 'account.tax', True, True, True, True
# modificar_permisos(30, 440, 467, 'account.tax repartition.line.manager', True, True, True, True
# modificar_permisos(30, 441, 471, 'account.tax.report.ac.user', True, True, True, True
# modificar_permisos(30, 442, 469, 'account.tax.report.line.ac.user', True, True, True, True
# modificar_permisos(30, 446, 492, 'account.payment.term', True, True, True, True
# modificar_permisos(30, 447, 494, 'account.payment.term.line', True, True, True, True
# modificar_permisos(30, 448, 2747, 'account.move manager', True, False, False, False
# modificar_permisos(30, 449, 2746, 'account.move.line manager', True, False, False, False
# modificar_permisos(30, 453, 496, 'Full access on account.payment.method to Financial Manager', True, True, True, True
# modificar_permisos(30, 460, 403, 'account.group.template', True, True, True, True
# modificar_permisos(30, 461, 398, 'account.account.template', True, True, True, True
# modificar_permisos(30, 462, 393, 'account.chart.template', True, True, True, True
# modificar_permisos(30, 463, 399, 'account.tax.template', True, True, True, True
# modificar_permisos(30, 464, 400, 'account.tax repartition.line.template.manager', True, True, True, True
# modificar_permisos(30, 465, 394, 'account.fiscal.position.template', True, True, True, True
# modificar_permisos(30, 466, 395, 'account.fiscal.position.tax.template', True, True, True, True
# modificar_permisos(30, 467, 396, 'account.fiscal.position.account.template', True, True, True, True
# modificar_permisos(30, 468, 401, 'account.reconcile.model.template', True, True, True, True
# modificar_permisos(30, 469, 402, 'account.reconcile.model.line.template', True, True, True, True
# modificar_permisos(30, 471, 410, 'account.incoterms manager', True, True, True, True
# modificar_permisos(30, 480, 503, 'access.account.resequence.wizard', True, True, True, False
# modificar_permisos(30, 481, 510, 'access.account.financial.year.op', True, True, True, False
# modificar_permisos(30, 482, 511, 'access.account.setup.bank.manual.config', True, True, True, False
# modificar_permisos(30, 486, 517, 'account.tour.upload.bill', True, True, True, False
# modificar_permisos(30, 487, 518, 'account.tour.upload.bill.email.confirm', True, True, True, False
# modificar_permisos(30, 488, 408, 'account.invoice.report', True, True, True, True
# modificar_permisos(30, 642, 773, 'Full access on account.payment.mode to Financial Manager', True, True, True, True
# modificar_permisos(30, 652, 875, 'account.move.tax.manager', True, True, True, True
# modificar_permisos(30, 653, 873, 'res.ciiu.manager', True, True, True, True
# modificar_permisos(30, 654, 882, 'account.financial.report.balance.manager', True, True, True, True
# modificar_permisos(30, 655, 884, 'account.financial.report.balance.line.manager', True, True, True, True
# modificar_permisos(30, 656, 909, 'account.financial.report.balance.manager', True, True, True, True
# modificar_permisos(30, 657, 911, 'account.financial.report.balance.line.manager', True, True, True, True
# modificar_permisos(30, 658, 896, 'account.financial.report.taxes.manager', True, True, True, True
# modificar_permisos(30, 659, 897, 'account.financial.report.taxes.line.manager', True, True, True, True
# modificar_permisos(30, 660, 877, 'account.financial.structure.manager', True, True, True, True
# modificar_permisos(30, 661, 879, 'account.financial.structure.line.manager', True, True, True, True
# modificar_permisos(30, 662, 880, 'account.financial.levels.manager', True, True, True, True
# modificar_permisos(30, 663, 890, 'excel.report.avancys.manager', True, True, True, True
# modificar_permisos(30, 664, 899, 'hr.payroll.advance.manager', True, True, True, True
# modificar_permisos(30, 665, 2348, 'hr.expense.expense.manager', True, True, True, True
# modificar_permisos(30, 666, 903, 'hr.expense.line.manager', True, True, True, True
# modificar_permisos(30, 667, 905, 'hr.expense.tax.manager', True, True, True, True
# modificar_permisos(30, 668, 907, 'account.financial.report.trial.wizard.manager', True, True, True, True
# modificar_permisos(30, 669, 886, 'account.financial.report.balance.wizard.manager', True, True, True, True
# modificar_permisos(30, 670, 888, 'account.financial.report.assistant.wizard.manager', True, True, True, True
# modificar_permisos(30, 671, 894, 'account.financial.report.taxes.wizard.manager', True, True, True, True
# modificar_permisos(30, 672, 930, 'account.advance.supplier.manager', True, True, True, True
# modificar_permisos(30, 673, 932, 'account.advance.customer.manager', True, True, True, True
# modificar_permisos(30, 674, 934, 'account.voucher.manager', True, True, True, True
# modificar_permisos(30, 674, 2793, 'account.voucher.manager', True, True, True, True
# modificar_permisos(30, 675, 936, 'account.voucher.line.manager', True, True, True, True
# modificar_permisos(30, 675, 1297, 'account.voucher.line.manager', True, True, True, True
# modificar_permisos(30, 676, 1273, 'account.fiscal.year.manager', True, True, True, True
# modificar_permisos(30, 676, 2770, 'account.fiscal.year.manager', True, True, True, True
# modificar_permisos(30, 678, 938, 'access.account.change.lock.date', True, True, True, False
# modificar_permisos(30, 684, 1280, 'access.date.range.manager', True, True, True, True
# modificar_permisos(30, 810, 1102, 'account.container.group.manager', True, True, True, True
# modificar_permisos(30, 817, 1096, 'account.financial.report.balance.inventory.wizard.manager', True, True, True, True
# modificar_permisos(30, 818, 1098, 'account.financial.report.major.balance.wizard.manager', True, True, True, True
# modificar_permisos(30, 819, 1100, 'account.financial.report.state.income.wizard.manager', True, True, True, True
# modificar_permisos(30, 820, 1092, 'account.financial.report.balance.general.wizard.manager', True, True, True, True
# modificar_permisos(30, 821, 1094, 'account.financial.report.diario.wizard.manager', True, True, True, True
# modificar_permisos(30, 932, 1202, 'account.asset', True, True, True, True
# modificar_permisos(30, 933, 1210, 'account.asset.group', True, True, True, True
# modificar_permisos(30, 934, 1199, 'account.asset.profile', True, True, True, True
# modificar_permisos(30, 935, 1205, 'account.asset.line', True, True, True, True
# modificar_permisos(30, 936, 1207, 'account.asset.recompute.trigger', True, True, True, True
# modificar_permisos(30, 1045, 1303, 'acces.account.consignment.manager', True, True, True, True
# modificar_permisos(30, 1156, 1368, 'account.budget.post', True, False, False, False
# modificar_permisos(30, 1157, 1367, 'crossovered.budget', True, False, False, False
# modificar_permisos(30, 1173, 1387, 'name_open_petty_cash', True, True, True, True
# modificar_permisos(30, 1174, 1388, 'name_move_petty_cash', True, True, True, True
# modificar_permisos(30, 1176, 1393, 'account.asset.line.niff', True, True, True, True
# modificar_permisos(30, 1182, 1401, 'account_payment_mean_manager', True, True, True, True
# modificar_permisos(30, 1183, 1403, 'account_payment_mean_code_manager', True, True, True, True
# modificar_permisos(30, 1184, 1405, 'account.move.discrepancy.response.code.manager', True, True, True, True
# modificar_permisos(30, 1187, 1409, 'account_fiscal_position_party_tax_scheme_manager', True, True, True, True
# modificar_permisos(30, 1188, 1411, 'account_fiscal_position_tax_level_code_manager', True, True, True, True
# modificar_permisos(30, 1648, 1859, 'credit_control_fin_manager_line', True, True, True, True
# modificar_permisos(30, 1932, 2420, 'account.financial.html.report', True, True, True, True
# modificar_permisos(30, 1933, 2423, 'account.financial.html.report.line', True, True, True, True
# modificar_permisos(30, 1949, 2440, 'avancys_account_followup.followup.line.manager', True, True, True, True
# modificar_permisos(35, 79, 524, 'res.partner.user', True, True, True, True
# modificar_permisos(35, 343, 2766, 'calendar.event.hruser', True, True, True, True
# modificar_permisos(35, 347, 530, 'calendar.event.type.officer', True, True, True, False
# modificar_permisos(35, 493, 526, 'hr.recruitment.source', True, True, True, True
# modificar_permisos(35, 494, 520, 'hr.recruitment.stage.user', True, False, False, False
# modificar_permisos(35, 495, 522, 'hr.recruitment.degree', True, True, True, True
# modificar_permisos(35, 496, 519, 'hr.applicant.user', True, False, False, False
# modificar_permisos(35, 497, 529, 'hr.applicant_category', True, True, True, True
# modificar_permisos(35, 498, 523, 'hr.applicant.refuse.reason', True, True, True, True
# modificar_permisos(35, 501, 531, 'access.applicant.get.refuse.reason', True, True, True, False
# modificar_permisos(36, 494, 521, 'hr.recruitment.stage.manager', True, True, True, True
# modificar_permisos(39, 137, 584, 'barcode.nomenclature.stock.user', True, False, False, False
# modificar_permisos(39, 138, 586, 'barcode.rule.stock.user', True, False, False, False
# modificar_permisos(39, 374, 2618, 'product.template stock user', True, False, False, False
# modificar_permisos(39, 374, 2622, 'product.template.stock.user', True, True, False, False
# modificar_permisos(39, 376, 1551, 'product.product.stock.user', True, True, False, False
# modificar_permisos(39, 376, 550, 'product_product_stock_user', True, False, False, False
# modificar_permisos(39, 504, 546, 'stock.inventory user', True, True, True, False
# modificar_permisos(39, 505, 548, 'stock.inventory.line user', True, True, True, False
# modificar_permisos(39, 508, 545, 'stock.move user', True, True, True, False
# modificar_permisos(39, 509, 579, 'stock.move.line user', True, True, True, True
# modificar_permisos(39, 510, 573, 'stock_rule user', True, False, False, False
# modificar_permisos(39, 512, 562, 'stock.warehouse.orderpoint', True, False, False, False
# modificar_permisos(39, 513, 543, 'stock.production.lot user', True, True, True, True
# modificar_permisos(39, 514, 541, 'stock.picking.type user', True, False, False, False
# modificar_permisos(39, 515, 538, 'stock.picking user', True, True, True, True
# modificar_permisos(39, 516, 565, 'stock.quant user', True, False, False, False
# modificar_permisos(39, 517, 569, 'stock.quant.package stock user', True, True, True, True
# modificar_permisos(39, 519, 588, 'stock.scrap.user', True, True, True, False
# modificar_permisos(39, 520, 572, 'stock.package_level stock user', True, True, True, True
# modificar_permisos(39, 525, 596, 'access.stock.traceability.report', True, True, True, False
# modificar_permisos(39, 526, 597, 'access.stock.assign.serial', True, True, True, False
# modificar_permisos(39, 527, 598, 'access.stock.return.picking.line', True, True, True, True
# modificar_permisos(39, 528, 599, 'access.stock.return.picking', True, True, True, False
# modificar_permisos(39, 529, 600, 'access.stock.change.product.qty', True, True, True, False
# modificar_permisos(39, 530, 601, 'access.stock.scheduler.compute', True, True, True, False
# modificar_permisos(39, 531, 602, 'access.stock.immediate.transfer.line', True, True, True, False
# modificar_permisos(39, 532, 603, 'access.stock.immediate.transfer', True, True, True, False
# modificar_permisos(39, 533, 604, 'access.stock.backorder.confirmation.line', True, True, True, False
# modificar_permisos(39, 534, 605, 'access.stock.backorder.confirmation', True, True, True, False
# modificar_permisos(39, 535, 606, 'access.stock.quantity.history', True, True, True, False
# modificar_permisos(39, 536, 607, 'access.stock.rules.report', True, True, True, False
# modificar_permisos(39, 538, 608, 'access.stock.warn.insufficient.qty.scrap', True, True, True, False
# modificar_permisos(39, 539, 609, 'access.product.replenish', True, True, True, False
# modificar_permisos(39, 540, 610, 'access.stock.track.confirmation', True, True, True, False
# modificar_permisos(39, 541, 611, 'access.stock.track.line', True, True, True, False
# modificar_permisos(39, 542, 612, 'access.stock.package.destination', True, True, True, False
# modificar_permisos(39, 543, 613, 'access_stock_orderpoint_snooze', True, True, True, True
# modificar_permisos(39, 579, 682, 'access.confirm.stock.sms', True, True, True, False
# modificar_permisos(39, 643, 916, 'sale.order stock worker', True, True, False, False
# modificar_permisos(39, 644, 917, 'sale.order.line stock worker', True, True, False, False
# modificar_permisos(39, 709, 998, 'purchase.order', True, False, False, False
# modificar_permisos(39, 710, 999, 'purchase.order.line', True, False, False, False
# modificar_permisos(39, 1336, 1523, 'access.expiry.picking.confirmation', True, True, True, False
# modificar_permisos(39, 1340, 1532, 'delivery.carrier stock_user', True, False, False, False
# modificar_permisos(39, 1342, 1535, 'access.choose.delivery.package', True, True, True, False
# modificar_permisos(39, 1343, 1536, 'access.choose.delivery.carrier', True, True, True, False
# modificar_permisos(39, 1344, 1537, 'delivery.guide.user', True, True, True, False
# modificar_permisos(39, 1345, 1553, 'delivery.guide.line.user', True, True, True, True
# modificar_permisos(39, 1346, 1540, 'access.delivery.invoice.stock', True, True, True, False
# modificar_permisos(39, 1347, 1544, 'delivery.rate.user', True, True, False, False
# modificar_permisos(39, 1348, 1547, 'delivery.rate.line.user', True, True, False, False
# modificar_permisos(39, 1349, 1563, 'access.delivery.vehicle.user', True, True, False, False
# modificar_permisos(39, 1350, 1566, 'access.delivery.vehicle.condition.user', True, True, False, False
# modificar_permisos(39, 1352, 1558, 'access.picking.guide.wizard', True, True, True, True
# modificar_permisos(39, 1354, 1556, 'payment.delivery.guide.user', True, True, True, False
# modificar_permisos(40, 79, 560, 'res_partner group_stock_manager', True, True, True, False
# modificar_permisos(40, 135, 552, 'uom.category stock_manager', True, True, True, True
# modificar_permisos(40, 136, 553, 'uom.uom stock_manager', True, True, True, True
# modificar_permisos(40, 137, 585, 'barcode.nomenclature.stock.manager', True, True, True, True
# modificar_permisos(40, 138, 587, 'barcode.rule.stock.manager', True, True, True, True
# modificar_permisos(40, 374, 2619, 'product.template stock_manager', True, True, True, True
# modificar_permisos(40, 375, 554, 'product.category stock_manager', True, True, True, True
# modificar_permisos(40, 376, 556, 'product.product stock_manager', True, True, True, True
# modificar_permisos(40, 377, 557, 'product.packaging stock_manager', True, True, True, True
# modificar_permisos(40, 378, 558, 'product.supplierinfo stock_manager', True, True, True, True
# modificar_permisos(40, 379, 590, 'product.attribute manager', True, True, True, True
# modificar_permisos(40, 380, 591, 'product.attribute manager value', True, True, True, True
# modificar_permisos(40, 381, 594, 'product.attribute manager line', True, True, True, True
# modificar_permisos(40, 382, 592, 'product.product.attribute manager value', True, True, True, True
# modificar_permisos(40, 383, 593, 'product.attribute manager filter line', True, True, True, True
# modificar_permisos(40, 385, 559, 'product.pricelist stock_manager', True, True, True, True
# modificar_permisos(40, 386, 561, 'product.pricelist.item stock_manager', True, True, True, True
# modificar_permisos(40, 408, 681, 'access.sms.template.stock.manager', True, True, True, True
# modificar_permisos(40, 433, 2620, 'account.account stock manager', True, False, False, False
# modificar_permisos(40, 437, 926, 'account.journal', True, True, False, False
# modificar_permisos(40, 437, 2621, 'account.journal stock manager', True, False, False, False
# modificar_permisos(40, 451, 925, 'account.partial.reconcile', True, True, True, True
# modificar_permisos(40, 503, 582, 'stock.putaway.rule all managers', True, True, True, True
# modificar_permisos(40, 504, 547, 'stock.inventory manager', True, True, True, True
# modificar_permisos(40, 505, 549, 'stock.inventory.line manager', True, True, True, True
# modificar_permisos(40, 506, 536, 'stock.location.manager', True, True, True, True
# modificar_permisos(40, 507, 575, 'stock.location.route', True, True, True, True
# modificar_permisos(40, 508, 544, 'stock.move manager', True, True, True, True
# modificar_permisos(40, 509, 578, 'stock.move.line manager', True, True, True, True
# modificar_permisos(40, 510, 574, 'stock_rule stock manager', True, True, True, True
# modificar_permisos(40, 512, 563, 'stock.warehouse.orderpoint system', True, True, True, True
# modificar_permisos(40, 514, 542, 'stock.picking.type manager', True, True, True, True
# modificar_permisos(40, 515, 539, 'stock.picking manager', True, True, True, True
# modificar_permisos(40, 516, 564, 'stock.quant manager', True, False, False, False
# modificar_permisos(40, 517, 568, 'stock.quant.package stock manager', True, True, True, True
# modificar_permisos(40, 518, 533, 'stock.warehouse.manager', True, True, True, True
# modificar_permisos(40, 519, 589, 'stock.scrap.manager', True, True, True, True
# modificar_permisos(40, 520, 571, 'stock.package_level stock manager', True, True, True, True
# modificar_permisos(40, 577, 679, 'access_stock_valuation_layer', True, True, True, False
# modificar_permisos(40, 578, 680, 'access_stock_valuation_layer_revaluation', True, True, True, False
# modificar_permisos(40, 1036, 1292, 'purchase.requisition', True, False, True, False
# modificar_permisos(40, 1037, 1293, 'purchase.requisition.line', True, False, True, False
# modificar_permisos(40, 1337, 1524, 'stock.landed.cost', True, True, True, True
# modificar_permisos(40, 1338, 1525, 'stock.landed.cost.lines', True, True, True, True
# modificar_permisos(40, 1339, 1526, 'stock.valuation.adjustment.lines', True, True, True, True
# modificar_permisos(40, 1340, 1533, 'delivery.carrier', True, True, True, True
# modificar_permisos(40, 1341, 1534, 'delivery.price.rule', True, True, True, True
# modificar_permisos(40, 1344, 1538, 'delivery.guide.manager', True, True, True, True
# modificar_permisos(40, 1345, 1554, 'delivery.guide.line.manager', True, True, True, True
# modificar_permisos(40, 1347, 1543, 'delivery.rate.manager', True, True, True, True
# modificar_permisos(40, 1348, 1546, 'delivery.rate.line.manager', True, True, True, True
# modificar_permisos(40, 1349, 1562, 'access.delivery.vehicle.manager', True, True, True, False
# modificar_permisos(40, 1350, 1565, 'access.delivery.vehicle.condition.manager', True, True, True, False
# modificar_permisos(40, 1354, 1557, 'payment.delivery.guide.manager', True, True, True, True
# modificar_permisos(49, 15, 622, 'access_website_ir_ui_view_publisher', True, False, False, False
# modificar_permisos(49, 355, 687, 'gamification.karma.rank.access.website.publisher', True, True, True, True
# modificar_permisos(50, 15, 623, 'access_website_ir_ui_view_designer', True, True, True, True
# modificar_permisos(50, 546, 625, 'access_seo_designer', True, True, True, True
# modificar_permisos(50, 551, 615, 'website.website.designer', True, True, True, True
# modificar_permisos(50, 552, 617, 'Web Menu Manager', True, True, True, True
# modificar_permisos(50, 553, 621, 'Web Page Manager', True, True, True, True
# modificar_permisos(50, 554, 630, 'access_website_designer_route', True, True, True, True
# modificar_permisos(50, 555, 619, 'Web Rewrite Manager', True, True, True, True
# modificar_permisos(50, 561, 628, 'access_website_track_designer', True, True, True, True
# modificar_permisos(50, 562, 626, 'access_website_visitor_designer', True, True, False, True
# modificar_permisos(50, 564, 635, 'access.website.robots', True, True, True, False
# modificar_permisos(51, 136, 650, 'uom.uom.hr.expense.user', True, True, True, True
# modificar_permisos(51, 340, 655, 'account.analytic.line.user', True, True, True, True
# modificar_permisos(51, 437, 651, 'account.journal.user', True, True, True, True
# modificar_permisos(51, 448, 2772, 'account.move.hr.expense.approver', True, False, False, False
# modificar_permisos(51, 449, 2773, 'account.move.line.hr.expense.approver', True, False, False, False
# modificar_permisos(51, 567, 644, 'hr.expense.user', True, True, True, True
# modificar_permisos(51, 568, 645, 'hr.expense.sheet.user', True, True, True, True
# modificar_permisos(51, 569, 657, 'access.hr.expense.refuse.wizard', True, True, True, False
# modificar_permisos(53, 163, 2774, 'mail.activity.type.expense.user', True, True, True, True
# modificar_permisos(53, 374, 2771, 'product.template.hr.expense.user', True, True, True, True
# modificar_permisos(53, 376, 648, 'product.product.hr.expense.user', True, True, True, True
# modificar_permisos(53, 567, 646, 'hr.expense.manager', True, True, True, True
# modificar_permisos(53, 568, 647, 'hr.expense.sheet.manager', True, True, True, True
# modificar_permisos(58, 77, 1019, 'res.partner.category.crm.user', True, True, True, False
# modificar_permisos(58, 79, 1018, 'res.partner.crm.user', True, True, True, False
# modificar_permisos(58, 79, 2784, 'res.partner.sale.user', True, False, False, False
# modificar_permisos(58, 136, 801, 'uom.uom.user', True, False, False, False
# modificar_permisos(58, 337, 787, 'account.analytic.tag.sale.salesman', True, False, False, False
# modificar_permisos(58, 339, 2782, 'account_analytic_account salesman', True, True, True, False
# modificar_permisos(58, 343, 2731, 'calendar.event', True, True, True, False
# modificar_permisos(58, 347, 1029, 'calendar.event.type.salesman', True, False, False, False
# modificar_permisos(58, 374, 2785, 'product.template sale use', True, False, False, False
# modificar_permisos(58, 376, 799, 'product.product sale use', True, False, False, False
# modificar_permisos(58, 377, 920, 'product.packaging.user', True, True, True, False
# modificar_permisos(58, 378, 2787, 'product.supplierinfo.user', True, False, False, False
# modificar_permisos(58, 384, 819, 'product.attribute.custom value manager', True, True, True, True
# modificar_permisos(58, 385, 802, 'product.pricelist.sale.user', True, False, False, False
# modificar_permisos(58, 431, 785, 'account.account.tag.sale.salesman', True, False, False, False
# modificar_permisos(58, 432, 786, 'account.account.type.sale.salesman', True, False, False, False
# modificar_permisos(58, 433, 2786, 'account_account salesman', True, False, False, False
# modificar_permisos(58, 437, 2783, 'account.journal sale order.user', True, False, False, False
# modificar_permisos(58, 438, 2790, 'account.tax.group sale manager', True, False, False, False
# modificar_permisos(58, 439, 2789, 'account.tax sale manager', True, False, False, False
# modificar_permisos(58, 439, 800, 'account.tax.user', True, False, False, False
# modificar_permisos(58, 446, 784, 'account_payment_term salesman', True, False, False, False
# modificar_permisos(58, 448, 2779, 'account_move salesman', True, False, False, False
# modificar_permisos(58, 449, 2780, 'account_move_line salesman', True, False, False, False
# modificar_permisos(58, 451, 2781, 'account_partial_reconcile salesman', True, False, False, False
# modificar_permisos(58, 484, 789, 'access.account.invoice.send.salesman', True, True, True, False
# modificar_permisos(58, 506, 922, 'stock.location.user', True, False, False, False
# modificar_permisos(58, 508, 914, 'stock_move salesman', True, True, True, False
# modificar_permisos(58, 510, 929, 'stock.rule.flow', True, False, False, False
# modificar_permisos(58, 512, 924, 'stock.warehouse.orderpoint', True, False, False, False
# modificar_permisos(58, 515, 913, 'stock_picking salesman', True, True, True, False
# modificar_permisos(58, 518, 921, 'stock.warehouse.user', True, False, False, False
# modificar_permisos(58, 561, 1046, 'access_website_track_salesman', True, False, False, False
# modificar_permisos(58, 562, 1045, 'access_website_visitor_salesman', True, False, False, False
# modificar_permisos(58, 575, 830, 'access.payment.link.wizard.sale', True, True, True, False
# modificar_permisos(58, 640, 767, 'crm.team.user', True, False, False, False
# modificar_permisos(58, 641, 770, 'crm_tag salesman', True, True, True, False
# modificar_permisos(58, 643, 774, 'sale.order', True, True, True, False
# modificar_permisos(58, 644, 775, 'sale.order.line', True, True, True, True
# modificar_permisos(58, 645, 793, 'sale.report', True, True, True, False
# modificar_permisos(58, 649, 828, 'access.sale.advance.payment.inv', True, True, True, False
# modificar_permisos(58, 650, 829, 'access.sale.order.cancel', True, True, True, False
# modificar_permisos(58, 679, 947, 'sale.order.option', True, True, True, True
# modificar_permisos(58, 680, 941, 'sale.order.template', True, False, False, False
# modificar_permisos(58, 681, 943, 'sale.order.template.line', True, False, False, False
# modificar_permisos(58, 682, 945, 'sale.order.template.option', True, False, False, False
# modificar_permisos(58, 715, 1013, 'crm.lead', True, True, True, False
# modificar_permisos(58, 716, 1022, 'crm.lost.reason.salesman', True, False, False, False
# modificar_permisos(58, 718, 1031, 'access_crm_lead_scoring_frequency', True, False, False, False
# modificar_permisos(58, 719, 1032, 'access_crm_lead_scoring_frequency_field', True, False, False, False
# modificar_permisos(58, 720, 1038, 'crm.recurring.plan.access.salesman', True, False, False, False
# modificar_permisos(58, 722, 1033, 'access.crm.lead.lost', True, True, True, False
# modificar_permisos(58, 723, 1034, 'access.crm.lead2opportunity.partner', True, True, True, False
# modificar_permisos(58, 724, 1035, 'access.crm.lead2opportunity.partner.mass', True, True, True, False
# modificar_permisos(58, 725, 1036, 'access.crm.merge.opportunity', True, True, True, False
# modificar_permisos(58, 732, 1047, 'access.crm.quotation.partner', True, True, True, False
# modificar_permisos(58, 1340, 1527, 'delivery.carrier', True, False, False, False
# modificar_permisos(58, 1341, 1528, 'delivery.price.rule', True, False, False, False
# modificar_permisos(58, 1358, 1572, 'crm.claim.user', True, True, True, False
# modificar_permisos(58, 1359, 1577, 'crm_claim_category salesman', True, True, True, False
# modificar_permisos(58, 1360, 1573, 'crm.claim.stage.user', True, True, True, True
# modificar_permisos(58, 1369, 1592, 'access.project.create.sale.order', True, True, True, False
# modificar_permisos(58, 1370, 1593, 'access.project.create.sale.order.line', True, True, True, True
# modificar_permisos(58, 1372, 1595, 'access.project.task.create.sale.order', True, True, True, False
# modificar_permisos(59, 1371, 1594, 'access.project.create.invoice', True, True, True, False
# modificar_permisos(60, 77, 1017, 'res.partner.category.crm.manager', True, False, False, False
# modificar_permisos(60, 79, 2719, 'res.partner.crm.manager', True, False, False, False
# modificar_permisos(60, 79, 810, 'res_partner group_sale_manager', True, True, True, False
# modificar_permisos(60, 79, 797, 'res.partner.sale.manager', True, True, True, False
# modificar_permisos(60, 135, 804, 'uom.category salemanager', True, True, True, True
# modificar_permisos(60, 136, 805, 'uom.uom salemanager', True, True, True, True
# modificar_permisos(60, 163, 2720, 'mail.activity.type.sale.manager', True, True, True, True
# modificar_permisos(60, 163, 2792, 'mail.activity.type.sale.manager', True, True, True, True
# modificar_permisos(60, 343, 2718, 'calendar.event.manager', True, True, True, True
# modificar_permisos(60, 347, 1027, 'calendar.event.type.manager', True, True, True, False
# modificar_permisos(60, 374, 2788, 'product.template salemanager', True, True, True, True
# modificar_permisos(60, 375, 806, 'product.category salemanager', True, True, True, True
# modificar_permisos(60, 376, 815, 'product.product salemanager', True, True, True, True
# modificar_permisos(60, 377, 923, 'product.packaging salemanager', True, True, True, True
# modificar_permisos(60, 378, 808, 'product.supplierinfo salemanager', True, True, True, True
# modificar_permisos(60, 379, 816, 'product.attribute manager', True, True, True, True
# modificar_permisos(60, 380, 817, 'product.attribute manager value', True, True, True, True
# modificar_permisos(60, 381, 821, 'product.attribute manager line', True, True, True, True
# modificar_permisos(60, 382, 818, 'product.template.attribute manager value', True, True, True, True
# modificar_permisos(60, 383, 820, 'product.attribute manager filter line', True, True, True, True
# modificar_permisos(60, 385, 809, 'product.pricelist salemanager', True, True, True, True
# modificar_permisos(60, 386, 813, 'product.pricelist.item salemanager', True, True, True, True
# modificar_permisos(60, 433, 2791, 'account.account sale manager', True, False, False, False
# modificar_permisos(60, 448, 2778, 'account_move manager', True, False, False, False
# modificar_permisos(60, 506, 927, 'stock.location sale manager', True, False, False, False
# modificar_permisos(60, 508, 915, 'stock_move manager', True, True, True, True
# modificar_permisos(60, 510, 928, 'stock_rule salemanager', True, True, True, True
# modificar_permisos(60, 515, 918, 'stock.picking.sales', True, True, True, True
# modificar_permisos(60, 640, 768, 'crm.team.manager', True, True, True, True
# modificar_permisos(60, 641, 771, 'crm_tag manager', True, True, True, True
# modificar_permisos(60, 643, 790, 'sale.order.manager', True, True, True, True
# modificar_permisos(60, 645, 794, 'sale.report', True, True, True, True
# modificar_permisos(60, 647, 826, 'access_report_all_channels_sales', True, False, False, False
# modificar_permisos(60, 680, 942, 'sale.order.template', True, True, True, True
# modificar_permisos(60, 681, 944, 'sale.order.template.line', True, True, True, True
# modificar_permisos(60, 682, 946, 'sale.order.template.option', True, True, True, True
# modificar_permisos(60, 714, 1015, 'crm.stage', True, True, True, True
# modificar_permisos(60, 715, 1012, 'crm.lead.manager', True, True, True, True
# modificar_permisos(60, 716, 1021, 'crm.lost.reason.manager', True, False, False, False
# modificar_permisos(60, 720, 1037, 'crm.recurring.plan.access.manager', True, True, True, True
# modificar_permisos(60, 1340, 1529, 'delivery.carrier', True, True, True, True
# modificar_permisos(60, 1341, 1530, 'delivery.price.rule', True, True, True, True
# modificar_permisos(60, 1358, 1571, 'crm.claim.manager', True, True, True, True
# modificar_permisos(60, 1359, 1578, 'crm_claim_category manager', True, True, True, True
# modificar_permisos(60, 1361, 1574, 'crm.claim.report.manager', True, True, True, True
# modificar_permisos(69, 79, 2726, 'res.partner purchase', True, False, False, False
# modificar_permisos(69, 340, 983, 'account.analytic.line', True, False, False, False
# modificar_permisos(69, 374, 2728, 'product.template purchase_user', True, False, False, False
# modificar_permisos(69, 376, 973, 'product.product.purchase.user', True, False, False, False
# modificar_permisos(69, 428, 976, 'account.fiscal.position purchase', True, False, False, False
# modificar_permisos(69, 431, 971, 'account.account.tag', True, False, False, False
# modificar_permisos(69, 432, 984, 'account.acount.type.purchase.user', True, False, False, False
# modificar_permisos(69, 437, 2727, 'account.journal', True, False, False, False
# modificar_permisos(69, 439, 2729, 'account.tax', True, False, False, False
# modificar_permisos(69, 448, 2725, 'account.move', True, True, True, False
# modificar_permisos(69, 449, 982, 'account.move.line', True, True, True, False
# modificar_permisos(69, 451, 985, 'account.partial.reconcile.purchase.user', True, False, False, False
# modificar_permisos(69, 506, 1000, 'stock.location', True, False, False, False
# modificar_permisos(69, 508, 1003, 'stock.move', True, True, True, False
# modificar_permisos(69, 512, 1009, 'stock.warehouse.orderpoint', True, False, False, False
# modificar_permisos(69, 515, 1002, 'stock.picking', True, True, True, True
# modificar_permisos(69, 518, 1001, 'stock.warehouse', True, False, False, False
# modificar_permisos(69, 709, 960, 'purchase.order', True, True, True, True
# modificar_permisos(69, 710, 965, 'purchase.order.line user', True, True, True, True
# modificar_permisos(69, 711, 997, 'purchase.stock.report user', True, False, False, False
# modificar_permisos(69, 712, 995, 'access_purchase_bill_union', True, False, False, False
# modificar_permisos(69, 713, 1011, 'vendor.delay.report user', True, False, False, False
# modificar_permisos(69, 1035, 1281, 'purchase.requisition.type', True, False, False, False
# modificar_permisos(69, 1036, 1283, 'purchase.requisition', True, True, True, True
# modificar_permisos(69, 1037, 1284, 'purchase.requisition.line', True, True, True, True
# modificar_permisos(70, 79, 986, 'res.partner.purchase.manager', True, True, True, False
# modificar_permisos(70, 135, 987, 'uom.category purchase_manager', True, True, True, True
# modificar_permisos(70, 136, 988, 'uom.uom purchase_manager', True, True, True, True
# modificar_permisos(70, 374, 2722, 'product.template purchase_manager', True, True, True, True
# modificar_permisos(70, 375, 989, 'product.category purchase_manager', True, True, True, True
# modificar_permisos(70, 376, 974, 'product.product purchase_manager', True, True, True, True
# modificar_permisos(70, 377, 991, 'product.packaging purchase_manager', True, True, True, True
# modificar_permisos(70, 378, 992, 'product.supplierinfo purchase_manager', True, True, True, True
# modificar_permisos(70, 386, 993, 'product.pricelist.item purchase_manager', True, True, True, True
# modificar_permisos(70, 433, 2723, 'account.account purchase manager', True, False, False, False
# modificar_permisos(70, 437, 2721, 'account.journal', True, False, False, False
# modificar_permisos(70, 439, 2724, 'account.tax', True, False, False, False
# modificar_permisos(70, 449, 981, 'account.move.line', True, True, True, True
# modificar_permisos(70, 506, 1004, 'stock.location', True, False, False, False
# modificar_permisos(70, 508, 1007, 'stock.move', True, True, True, True
# modificar_permisos(70, 512, 1008, 'stock.warehouse.orderpoint', True, False, False, False
# modificar_permisos(70, 515, 1006, 'stock.picking', True, True, True, True
# modificar_permisos(70, 518, 1005, 'stock.warehouse', True, False, False, False
# modificar_permisos(70, 709, 961, 'purchase.order', True, True, True, True
# modificar_permisos(70, 710, 966, 'purchase.order.line', True, True, True, True
# modificar_permisos(70, 711, 996, 'purchase.stock.report', True, False, False, False
# modificar_permisos(70, 713, 1010, 'vendor.delay.report', True, False, False, False
# modificar_permisos(70, 1035, 1282, 'purchase.requisition.type', True, True, True, True
# modificar_permisos(70, 1036, 1285, 'purchase.requisition manager', True, False, False, False
# modificar_permisos(70, 1037, 1286, 'purchase.requisition.line manager', True, False, False, False
# modificar_permisos(77, 79, 1116, 'access_res_partner_manager_payslip', True, True, True, True
# modificar_permisos(77, 760, 1117, 'access_res_partner_document_type_group_partner_manager', True, True, True, True
# modificar_permisos(77, 870, 1118, 'access_hr_novelty_type_manager_payslip', True, True, True, True
# modificar_permisos(77, 871, 1122, 'access_hr_novelty_manager_payslip', True, True, True, True
# modificar_permisos(77, 872, 1123, 'access_hr_novelty_line_manager_payslip', True, True, True, True
# modificar_permisos(77, 873, 1119, 'access_hr_leave_type_manager_payslip', True, True, True, True
# modificar_permisos(77, 874, 1124, 'access_hr_leave_manager_payslip', True, True, True, True
# modificar_permisos(77, 875, 1125, 'access_hr_leave_line_manager_payslip', True, True, True, True
# modificar_permisos(77, 876, 1150, 'access_hr_leave_cause_manager_payslip', True, True, True, True
# modificar_permisos(77, 877, 1126, 'access_hr_overtime_type_manager_payslip', True, True, True, True
# modificar_permisos(77, 878, 1127, 'access_hr_overtime_manager_payslip', True, True, True, True
# modificar_permisos(77, 879, 1158, 'access_hr_holiday_year_manager_payslip', True, True, True, True
# modificar_permisos(77, 880, 1159, 'access_hr_holiday_manager_payslip', True, True, True, True
# modificar_permisos(77, 881, 1121, 'access_hr_period_manager_payslip', True, True, True, True
# modificar_permisos(77, 882, 1120, 'access_hr_period_creator_manager_payslip', True, True, True, True
# modificar_permisos(77, 883, 1155, 'access_hr_employee_rh_manager_payslip', True, True, True, True
# modificar_permisos(77, 895, 1135, 'access_hr_contract_group_manager', True, True, True, True
# modificar_permisos(77, 896, 1134, 'access_hr_contract_type_manager', True, True, True, True
# modificar_permisos(77, 897, 1136, 'access_hr_contract_risk_manager', True, True, True, True
# modificar_permisos(77, 898, 1130, 'access_eps_update_history_manager', True, True, True, True
# modificar_permisos(77, 899, 1131, 'access_pension_update_history_manager', True, True, True, True
# modificar_permisos(77, 900, 1132, 'access_severance_update_history_manager', True, True, True, True
# modificar_permisos(77, 901, 1133, 'access_wage_update_history_manager', True, True, True, True
# modificar_permisos(77, 902, 1141, 'access_hr_fiscal_type_manager', True, True, True, True
# modificar_permisos(77, 903, 1142, 'access_hr_fiscal_subtype_manager', True, True, True, True
# modificar_permisos(77, 904, 1140, 'access_hr_equipment_manager', True, True, True, True
# modificar_permisos(77, 905, 1137, 'access_hr_contract_analytic_distribution_manager', True, True, True, True
# modificar_permisos(77, 906, 1138, 'access_hr_contract_withholding_log_manager', True, True, True, True
# modificar_permisos(77, 907, 1139, 'access_hr_contract_extension_manager', True, True, True, True
# modificar_permisos(77, 908, 1151, 'access_hr_holiday_book_manager_payslip', True, True, True, True
# modificar_permisos(77, 909, 1144, 'access_hr_concept_manager_payslip', True, True, True, True
# modificar_permisos(77, 910, 1129, 'access_hr_payslip_type_manager_payslip', True, True, True, True
# modificar_permisos(77, 911, 1128, 'access_hr_payslip_manager_payslip', True, True, True, True
# modificar_permisos(77, 912, 1143, 'access_hr_payslip_line_manager_payslip', True, True, True, True
# modificar_permisos(77, 913, 1145, 'access_hr_payslip_day_manager_payslip', True, True, True, True
# modificar_permisos(77, 914, 1146, 'access_hr_payslip_processing_manager_payslip', True, True, True, True
# modificar_permisos(77, 916, 1157, 'access_hr_payslip_line_report_manager_payslip_wizard', True, True, True, True
# modificar_permisos(77, 917, 1147, 'access_economic_variable_manager_payslip', True, True, True, True
# modificar_permisos(77, 918, 1148, 'access_economic_variable_line_manager_payslip', True, True, True, True
# modificar_permisos(77, 919, 1149, 'access_economic_variable_line_detail_manager_payslip', True, True, True, True
# modificar_permisos(77, 920, 1152, 'access_hr_contribution_form_manager_payslip', True, True, True, True
# modificar_permisos(77, 921, 1153, 'access_hr_contribution_form_line_manager_payslip', True, True, True, True
# modificar_permisos(77, 1547, 1720, 'access_group_update_history_manager', True, True, True, True
# modificar_permisos(79, 79, 2411, 'base.res.partner user', True, False, False, False
# modificar_permisos(79, 143, 1184, 'project.resource_calendar user', True, False, False, False
# modificar_permisos(79, 144, 1185, 'project.resource_calendar_attendance user', True, False, False, False
# modificar_permisos(79, 146, 2767, 'resource.calendar.leaves user', True, True, True, True
# modificar_permisos(79, 339, 2768, 'account.analytic.account', True, False, False, False
# modificar_permisos(79, 923, 1196, 'project.task.recurrence', True, True, True, True
# modificar_permisos(79, 924, 1174, 'project.task.type.project.user', True, False, False, False
# modificar_permisos(79, 925, 1171, 'project.project', True, False, False, False
# modificar_permisos(79, 926, 1177, 'project.task', True, True, True, True
# modificar_permisos(80, 163, 2412, 'mail.activity.type.project.manager', True, True, True, True
# modificar_permisos(80, 339, 2769, 'account.analytic.account', True, False, False, False
# modificar_permisos(80, 340, 1193, 'account.analytic.line project', True, True, True, True
# modificar_permisos(80, 643, 1256, 'sale.order.project.manager', True, False, False, False
# modificar_permisos(80, 644, 1255, 'sale.order.line.project.manager', True, False, False, False
# modificar_permisos(80, 924, 1175, 'project.task.type manager', True, True, True, True
# modificar_permisos(80, 925, 1172, 'project.project', True, True, True, True
# modificar_permisos(80, 927, 1188, 'project.project_tags_manager', True, True, True, True
# modificar_permisos(80, 929, 1178, 'report.project.task.user', True, True, True, True
# modificar_permisos(80, 930, 1194, 'access_project_delete_wizard', True, True, True, True
# modificar_permisos(80, 931, 1195, 'project.task.type.delete.wizard', True, True, True, True
# modificar_permisos(80, 1368, 1591, 'access_project_sale_line_employee_map_project_manager', True, True, True, True
# modificar_permisos(80, 1373, 1589, 'project.profitability.report.analysis', True, True, True, True
# modificar_permisos(84, 448, 2776, 'acces.account.move.info', True, False, False, False
# modificar_permisos(84, 449, 2777, 'acces.account.move.line.info', True, False, False, False
# modificar_permisos(84, 453, 1275, 'acces.account.payment.method.info', True, False, False, False
# modificar_permisos(84, 454, 1274, 'acces.account.payment.info', True, True, True, False
# modificar_permisos(85, 674, 1296, 'account.voucher.info', True, True, False, False
# modificar_permisos(85, 675, 1299, 'account.voucher.line.info', True, True, True, True
# modificar_permisos(85, 1045, 1301, 'acces.account.consignment.manager', True, True, True, False
# modificar_permisos(85, 1344, 1539, 'delivery.guide.account', True, False, False, False
# modificar_permisos(85, 1345, 1555, 'delivery.guide.line.account', True, False, False, False
# modificar_permisos(85, 1346, 1541, 'access.delivery.invoice.account', True, True, True, False
# modificar_permisos(88, 81, 90, 'Full access on res.bank to Account Payment group', True, True, True, True
# modificar_permisos(88, 82, 62, 'Full access on res.partner.bank to Account Payment group', True, True, True, True
# modificar_permisos(88, 1039, 1287, 'Full access on account.payment.order to Payment Manager', True, True, True, True
# modificar_permisos(88, 1040, 1288, 'Full access on account.payment.line to Payment Manager', True, True, True, True
# modificar_permisos(88, 1041, 1289, 'Full access on bank.payment.line to Payment Manager', True, True, True, True
# modificar_permisos(88, 1043, 1290, 'access_account_payment_line_create', True, True, True, True
# modificar_permisos(88, 1044, 1291, 'access_account_invoice_payment_line_multi', True, True, True, True
# modificar_permisos(96, 1144, 1350, 'access_variables_economicas', True, False, False, False
# modificar_permisos(96, 1145, 1352, 'variables.economicas.line', True, False, False, False
# modificar_permisos(96, 1146, 1354, 'variables.economicas.retefuente', True, False, False, False
# modificar_permisos(96, 1147, 1356, 'variables.economicas.retefuente.line', True, False, False, False
# modificar_permisos(96, 1148, 1358, 'variables.economicas.retefuente.marginal.line', True, False, False, False
# modificar_permisos(97, 1144, 1351, 'variables.economicas.user', True, True, True, True
# modificar_permisos(97, 1145, 1353, 'variables.economicas.line', True, True, True, True
# modificar_permisos(97, 1146, 1355, 'variables.economicas.retefuente', True, True, True, True
# modificar_permisos(97, 1147, 1357, 'variables.economicas.retefuente.line', True, True, True, True
# modificar_permisos(97, 1148, 1359, 'variables.economicas.retefuente.marginal.line', True, True, True, True
# modificar_permisos(100, 1162, 1378, 'account_dimensions_avancys.account_commercial_distribution', True, True, True, True
# modificar_permisos(121, 508, 1542, 'access.stock.move.user', True, False, False, False
# modificar_permisos(121, 1347, 1545, 'delivery.rate.info', True, False, False, False
# modificar_permisos(121, 1348, 1548, 'delivery.rate.line.info', True, False, False, False
# modificar_permisos(121, 1349, 1564, 'access.delivery.vehicle.info', True, True, False, False
# modificar_permisos(121, 1350, 1567, 'access.delivery.vehicle.condition.info', True, True, False, False
# modificar_permisos(128, 136, 1585, 'uom.uom.timesheet.user', True, False, False, False
# modificar_permisos(128, 339, 2775, 'analytic.account.analytic.timesheet.user', True, False, False, False
# modificar_permisos(128, 340, 1583, 'analytic.account.analytic.line.timesheet.user', True, True, True, True
# modificar_permisos(128, 925, 1586, 'project.project.timesheet.user', True, False, False, False
# modificar_permisos(128, 926, 1587, 'project.task.timesheet.user', True, True, False, False
# modificar_permisos(128, 1367, 1588, 'access.project.task.create.timesheet', True, True, True, False
# modificar_permisos(132, 27, 2, 'ir_attachment_group_user', True, True, True, True
# modificar_permisos(132, 85, 2413, 'res.config.settings.vise.administracion', True, True, True, True
# modificar_permisos(132, 134, 2410, 'res.city_vise_adminstrador', True, True, True, True
# modificar_permisos(132, 514, 3185, 'consulta', True, True, True, True
# modificar_permisos(132, 534, 2867, 'access.stock.backorder.confirmation', True, True, True, False
# modificar_permisos(132, 1157, 2605, 'crossovered.budget', True, True, True, True
# modificar_permisos(132, 1160, 2601, 'res.regional.vise.administrador', True, True, True, True
# modificar_permisos(132, 1274, 2628, 'hr.holiday.public.vise.administrador', True, True, True, True
# modificar_permisos(132, 1410, 2802, 'document.page.usuario_interno', True, True, True, True
# modificar_permisos(132, 1568, 1876, 'access_helpdesk_ticket_user.vise.administrador', True, True, True, True
# modificar_permisos(132, 1657, 2016, 'Vise_Administrador', True, True, True, True
# modificar_permisos(132, 2934, 3176, 'manejan todos los parametros', True, True, True, True
# modificar_permisos(132, 2941, 3177, 'manejan todos los parametros', True, True, True, True
# modificar_permisos(132, 2998, 3258, 'mi grupo_2', True, True, True, True
# modificar_permisos(132, 3163, 3255, 'mi grupo', True, True, True, True
# modificar_permisos(133, 1399, 1619, 'fleet_vehicle_access_right', True, True, False, False
# modificar_permisos(133, 1400, 1626, 'fleet_vehicle_odometer_access_right', True, True, True, True
# modificar_permisos(133, 1401, 1617, 'fleet_vehicle_state_access_right', True, False, False, False
# modificar_permisos(133, 1402, 1616, 'fleet_vehicle_tag_access_right', True, False, False, False
# modificar_permisos(133, 1403, 1622, 'fleet_service_type_access_right', True, False, False, False
# modificar_permisos(133, 1404, 1633, 'fleet_vehicle_assignation_log fleet_group_user', True, True, True, True
# modificar_permisos(133, 1405, 1621, 'fleet_vehicle_log_contract_access_right', True, False, False, False
# modificar_permisos(133, 1406, 1620, 'fleet_vehicle_log_services_access_right', True, False, False, False
# modificar_permisos(133, 1407, 1615, 'fleet_vehicle_model_access_right', True, False, False, False
# modificar_permisos(133, 1408, 1618, 'fleet_vehicle_model_brand_access_right', True, False, False, False
# modificar_permisos(134, 163, 2741, 'mail.activity.type.fleet.manager', True, True, True, True
# modificar_permisos(134, 1399, 1628, 'fleet_vehicle_access_right', True, True, True, True
# modificar_permisos(134, 1401, 1625, 'fleet_vehicle_state_access_right', True, True, True, True
# modificar_permisos(134, 1402, 1624, 'fleet_vehicle_tag_access_right', True, True, True, True
# modificar_permisos(134, 1403, 1631, 'fleet_service_type_access_right', True, True, True, True
# modificar_permisos(134, 1405, 1630, 'fleet_vehicle_log_contract_access_right', True, True, True, True
# modificar_permisos(134, 1406, 1629, 'fleet_vehicle_log_services_access_right', True, True, True, True
# modificar_permisos(134, 1407, 1623, 'fleet_vehicle_model_access_right', True, True, True, True
# modificar_permisos(134, 1408, 1627, 'fleet_vehicle_model_brand_access_right', True, True, True, True
# modificar_permisos(134, 1409, 1634, 'fleet_vehicle_cost_report_access_right', True, True, True, True
# modificar_permisos(135, 1410, 1635, 'document.page user', True, False, False, False
# modificar_permisos(135, 1411, 1636, 'document.page.history user', True, False, False, False
# modificar_permisos(135, 1412, 1641, 'document.page.create.menu wizard', True, True, True, False
# modificar_permisos(135, 1413, 1642, 'document.page.history.show_diff wizard', True, True, True, False
# modificar_permisos(137, 1410, 1637, 'document.page editor', True, False, False, False
# modificar_permisos(137, 1411, 1638, 'document.page.history editor', True, True, True, False
# modificar_permisos(138, 1410, 1639, 'document.page manager', True, False, False, True
# modificar_permisos(138, 1411, 1640, 'document.page.history manager', True, True, True, False
# modificar_permisos(145, 163, 2742, 'mail.activity.type.equipment.manager', True, True, True, True
# modificar_permisos(145, 1519, 1682, 'equipment.request.stage system user', True, True, True, True
# modificar_permisos(145, 1520, 1680, 'equipment.category system user', True, True, True, True
# modificar_permisos(145, 1521, 1677, 'equipment.admin.user', True, True, True, True
# modificar_permisos(145, 1523, 1684, 'maintenance.team.admin.user', True, True, True, True
# modificar_permisos(146, 1410, 1708, 'document.pages.hseq.user', True, False, False, False
# modificar_permisos(146, 1524, 1704, 'audit.action.hseq.user', True, True, True, False
# modificar_permisos(146, 1525, 1694, 'audit.audit.hseq.user', True, True, True, False
# modificar_permisos(146, 1527, 1702, 'audit.cause.hseq.user', True, True, True, False
# modificar_permisos(146, 1528, 1706, 'audit.evaluation.hseq.user', True, True, True, False
# modificar_permisos(146, 1529, 1714, 'audit.indicator.rango.hseq.user', True, True, True, False
# modificar_permisos(146, 1530, 1716, 'audit.indicator.result.hseq.user', True, True, True, False
# modificar_permisos(146, 1531, 1712, 'audit.indicator.type.hseq.user', True, True, True, False
# modificar_permisos(146, 1532, 1710, 'audit.indicator.hseq.user', True, True, True, False
# modificar_permisos(146, 1533, 1696, 'audit.list.hseq.user', True, True, True, False
# modificar_permisos(146, 1534, 1700, 'audit.nonconformity.origin.hseq.user', True, True, True, False
# modificar_permisos(146, 1535, 1698, 'audit.nonconformity.hseq.user', True, True, True, False
# modificar_permisos(146, 1536, 1688, 'audit.objectives.hseq.user', True, True, True, False
# modificar_permisos(146, 1537, 1686, 'audit.plannning.hseq.user', True, False, False, False
# modificar_permisos(146, 1538, 1692, 'audit.process.hseq.user', True, True, True, False
# modificar_permisos(146, 1539, 1690, 'audit.system.hseq.user', True, True, True, False
# modificar_permisos(147, 1410, 1709, 'document.pages.hseq.manager', True, False, False, True
# modificar_permisos(147, 1524, 1705, 'audit.action.hseq.manager', True, True, True, True
# modificar_permisos(147, 1525, 1695, 'audit.audit.hseq.manager', True, True, True, True
# modificar_permisos(147, 1527, 1703, 'audit.cause.hseq.manager', True, True, True, True
# modificar_permisos(147, 1528, 1707, 'audit.evaluation.hseq.manager', True, True, True, True
# modificar_permisos(147, 1529, 1715, 'audit.indicator.rango.hseq.manager', True, True, True, True
# modificar_permisos(147, 1530, 1717, 'audit.indicator.result.hseq.manager', True, True, True, True
# modificar_permisos(147, 1531, 1713, 'audit.indicator.type.hseq.manager', True, True, True, True
# modificar_permisos(147, 1532, 1711, 'audit.indicator.hseq.manager', True, True, True, True
# modificar_permisos(147, 1533, 1697, 'audit.list.hseq.manager', True, True, True, True
# modificar_permisos(147, 1534, 1701, 'audit.nonconformity.origin.hseq.manager', True, True, True, True
# modificar_permisos(147, 1535, 1699, 'audit.nonconformity.hseq.manager', True, True, True, True
# modificar_permisos(147, 1536, 1689, 'audit.objectives.hseq.manager', True, True, True, True
# modificar_permisos(147, 1537, 1687, 'audit.plannning.hseq.manager', True, True, True, True
# modificar_permisos(147, 1538, 1693, 'audit.process.hseq.manager', True, True, True, True
# modificar_permisos(147, 1539, 1691, 'audit.system.hseq.manager', True, True, True, True
# modificar_permisos(150, 1411, 3273, 'document.page.history user', True, False, False, False
# modificar_permisos(150, 1552, 1724, 'dms_storage_user', True, False, False, False
# modificar_permisos(150, 1553, 1729, 'dms_directory_user', True, True, True, True
# modificar_permisos(150, 1554, 1733, 'dms_file_user', True, True, True, True
# modificar_permisos(150, 1555, 1722, 'dms_category_user', True, True, True, True
# modificar_permisos(150, 1556, 1721, 'dms_tag_user', True, True, True, True
# modificar_permisos(151, 1552, 1725, 'dms_storage_manager', True, True, True, True
# modificar_permisos(152, 1557, 1739, 'access_helpdesk_team_user', True, False, False, False
# modificar_permisos(152, 1558, 1742, 'access_helpdesk_ticket_type_user', True, False, False, False
# modificar_permisos(152, 1559, 1745, 'access_helpdesk_sub_type_user', True, False, False, False
# modificar_permisos(152, 1560, 1748, 'access_helpdesk_tags_user', True, False, False, False
# modificar_permisos(152, 1561, 1752, 'access_helpdesk_stages_user', True, True, True, False
# modificar_permisos(152, 1562, 1755, 'access_helpdesk_category_user', True, False, False, False
# modificar_permisos(152, 1563, 1760, 'access_helpdesk_subcategory_user', True, False, False, False
# modificar_permisos(152, 1564, 1763, 'access_helpdesk_priority_user', True, False, False, False
# modificar_permisos(152, 1566, 1756, 'access_helpdesk_release', True, False, False, False
# modificar_permisos(152, 1568, 1766, 'access_helpdesk_ticket_user', True, True, True, False
# modificar_permisos(152, 1570, 1769, 'access_helpdesk_dashboard_user', True, True, True, True
# modificar_permisos(153, 1557, 1738, 'access_helpdesk_team_leader', True, False, False, False
# modificar_permisos(153, 1558, 1741, 'access_helpdesk_ticket_type_leader', True, False, False, False
# modificar_permisos(153, 1559, 1744, 'access_helpdesk_sub_type_leader', True, False, False, False
# modificar_permisos(153, 1560, 1747, 'access_helpdesk_tags_leader', True, False, False, False
# modificar_permisos(153, 1561, 1751, 'access_helpdesk_stages_leader', True, True, True, False
# modificar_permisos(153, 1562, 1754, 'access_helpdesk_category_leader', True, False, False, False
# modificar_permisos(153, 1563, 1759, 'access_helpdesk_subcategory_leader', True, False, False, False
# modificar_permisos(153, 1564, 1762, 'access_helpdesk_priority_leader', True, False, False, False
# modificar_permisos(153, 1566, 1757, 'access_helpdesk_release', True, True, True, True
# modificar_permisos(153, 1568, 1765, 'access_helpdesk_ticket_leader', True, True, True, False
# modificar_permisos(153, 1570, 1768, 'access_helpdesk_dashboard_leader', True, True, True, True
# modificar_permisos(154, 1557, 1737, 'access_helpdesk_team_manager', True, True, True, True
# modificar_permisos(154, 1558, 1740, 'access_helpdesk_ticket_type_manager', True, True, True, True
# modificar_permisos(154, 1559, 1743, 'access_helpdesk_sub_type_manager', True, True, True, True
# modificar_permisos(154, 1560, 1746, 'access_helpdesk_tags_manager', True, True, True, True
# modificar_permisos(154, 1561, 1749, 'access_helpdesk_stages_manager', True, True, True, True
# modificar_permisos(154, 1562, 1753, 'access_helpdesk_category_manager', True, True, True, True
# modificar_permisos(154, 1563, 1758, 'access_helpdesk_subcategory_manager', True, True, True, True
# modificar_permisos(154, 1564, 1761, 'access_helpdesk_priority_manager', True, True, True, True
# modificar_permisos(154, 1568, 1764, 'access_helpdesk_ticket_manager', True, True, True, True
# modificar_permisos(154, 1570, 1767, 'access_helpdesk_dashboard_manager', True, True, True, True
# modificar_permisos(159, 1571, 1771, 'access_sh_quick_reply_user', True, True, True, True
# modificar_permisos(166, 15, 2451, 'usario', True, True, True, False
# modificar_permisos(166, 35, 2305, 'Parámetro_del_sistema', True, True, True, False
# modificar_permisos(166, 91, 1909, 'usuarios', True, True, True, False
# modificar_permisos(166, 159, 2306, 'Seguidores_del_documento', True, True, True, False
# modificar_permisos(166, 360, 1908, 'empleado', True, True, True, False
# modificar_permisos(166, 1525, 1780, 'audit.audit.vise.capacitacion.credenciales', True, True, False, False
# modificar_permisos(166, 1538, 1781, 'audit.process.vise.capacitacion.credenciales', True, False, False, False
# modificar_permisos(166, 1539, 1779, 'audit.system.vise.capacitacion.credenciales', True, False, False, False
# modificar_permisos(166, 1576, 2308, 'hr.employee.accreditation_vise.capacitacion.credenciales', True, True, True, False
# modificar_permisos(166, 1577, 2307, 'hr.employee.accreditation.line_vise.capacitacion.credenciales', True, False, False, False
# modificar_permisos(166, 1578, 2654, 'cursos', True, True, True, True
# modificar_permisos(172, 85, 2735, 'res.config.settings.', True, True, True, False
# modificar_permisos(172, 339, 2414, 'account.analytic.account.vise.contabilidad.administrador', True, False, False, False
# modificar_permisos(172, 375, 1877, 'Vise_Contabilildad_Administrador', True, True, True, True
# modificar_permisos(172, 433, 1941, 'account.account', True, True, True, True
# modificar_permisos(172, 437, 1937, 'account.journal', True, True, True, True
# modificar_permisos(172, 439, 2449, 'account.tax.vise.contabilidad.administrador', True, True, True, True
# modificar_permisos(172, 683, 950, 'date_range.date_range_type', True, False, False, False
# modificar_permisos(172, 684, 2387, 'date.range.vise.contabilidad.administrador', True, True, True, False
# modificar_permisos(172, 932, 2940, 'account.asset', True, True, True, False
# modificar_permisos(172, 1191, 2397, 'account.move.dian.document.vise.contabilidad.administrador', False, False, False, True
# modificar_permisos(172, 1287, 2896, 'hr.roster.close.distribution', True, True, True, True
# modificar_permisos(172, 1584, 2450, 'certificado.report.retencion.periodicidad.vise.contabilidad.administrador', True, True, True, True
# modificar_permisos(173, 82, 2362, 'res.partner.bank.vise.compras.administrador', True, True, True, False
# modificar_permisos(173, 91, 2361, 'usuarios.vise.compras.administrador', False, True, False, False
# modificar_permisos(173, 449, 2341, 'acount.move.line', True, True, True, True
# modificar_permisos(173, 653, 2343, 'res.ciiu.manager.vise.compras', True, False, False, False
# modificar_permisos(173, 672, 2347, 'account.advance.supplier.vise.compras', True, False, False, False
# modificar_permisos(173, 709, 1913, 'purchase.order.vise.compras', True, True, True, False
# modificar_permisos(173, 710, 2297, 'Vise_Compras', True, True, True, True
# modificar_permisos(173, 1157, 2332, 'Vise.compras', True, True, True, True
# modificar_permisos(173, 1166, 2344, 'account.loan.vise.compras', True, True, True, False
# modificar_permisos(173, 1337, 2346, 'stock.landed.cost.vise.compras', True, False, False, False
# modificar_permisos(175, 2934, 3118, 'Talento_humano.vise_nomina_175', True, True, False, False
# modificar_permisos(175, 2941, 3121, 'x_hr.requisicion.linea.vise_nomina', True, True, False, False
# modificar_permisos(175, 2949, 3175, 'Talento_humano.vise_nomina_175', True, True, True, True
# modificar_permisos(179, 79, 3204, 'Contactos', True, True, True, True
# modificar_permisos(179, 2969, 3203, 'x_vise.unidad.integrtidad', True, True, True, True
# modificar_permisos(179, 2971, 3196, 'x_vise.unidad.integrtidad', True, True, True, True
# modificar_permisos(179, 2973, 3197, 'x_vise.unidad.integrtidad', True, True, True, True
# modificar_permisos(179, 2975, 3195, 'x_vise.unidad.integrtidad', True, True, True, True
# modificar_permisos(179, 2977, 3199, 'x_vise.unidad.integrtidad', True, True, True, True
# modificar_permisos(179, 2981, 3200, 'x_vise.unidad.integrtidad', True, True, True, True
# modificar_permisos(179, 2983, 3198, 'x_vise.unidad.integrtidad', True, True, True, True
# modificar_permisos(179, 2985, 3201, 'x_vise.unidad.integrtidad', True, True, True, True
# modificar_permisos(179, 2987, 3202, 'x_vise.unidad.integrtidad', True, True, True, True
# modificar_permisos(180, 63, 2321, 'Vise_Contabilidad_Viaticcos', True, True, True, False
# modificar_permisos(180, 664, 1826, 'hr.payroll.advance.vise.viaticos.usuarios', True, True, True, False
# modificar_permisos(180, 666, 2320, 'Contabilidad_Viaticos', True, True, True, True
# modificar_permisos(180, 667, 2323, 'Viaticos', True, True, True, True
# modificar_permisos(181, 391, 2315, 'Vise', True, False, False, False
# modificar_permisos(181, 872, 2014, 'hr.novelty.line', True, True, True, True
# modificar_permisos(181, 874, 2015, 'Vise_Eficiencia_Usuarios', True, True, True, False
# modificar_permisos(181, 1142, 2013, 'hr.novelty', True, True, True, True
# modificar_permisos(181, 1258, 2316, 'Vise_efcincia', True, False, False, False
# modificar_permisos(181, 2679, 2939, 'hr.tarifario_vise_eficiencia_usuario', True, False, False, False
# modificar_permisos(181, 2688, 2903, 'hr.roster.rest_modalidad', True, False, False, False
# modificar_permisos(181, 2734, 2938, 'hr.inductions_vise_grupo_eficiencia_usuarios', True, False, False, False
# modificar_permisos(182, 63, 1840, 'Vise_Contabilidad_Facturación_Clientes', True, True, True, False
# modificar_permisos(183, 1258, 1912, 'hr_roster_avancys.hr_roster_modalidad', True, True, True, False
# modificar_permisos(183, 1259, 1911, 'hr_roster_avancys.hr_roster_horario', True, True, True, False
# modificar_permisos(183, 1277, 2630, 'project.service.order.administrador.eficiencia', True, True, True, True
# modificar_permisos(185, 496, 3032, 'hr.applicant.vise_selección', True, True, True, True
# modificar_permisos(185, 905, 3295, 'hr.contract.analytic.distribution.vise_selección', True, False, False, False
# modificar_permisos(185, 1949, 3017, 'avancys_account_followup.followup.line.vise_selección', True, True, True, False
# modificar_permisos(185, 2850, 3031, 'contacto.emergencia.vise_selección', True, True, True, True
# modificar_permisos(186, 672, 2359, 'account.advance.supplier.vise.requisicion2', True, False, False, False
# modificar_permisos(186, 1036, 2357, 'purchase.requisition.vise.requisicion', True, True, True, False
# modificar_permisos(186, 1337, 2358, 'stock.landed.cost.vise.requisicion', True, False, False, False
# modificar_permisos(188, 448, 2395, 'account.move.vise_financiera auditoria usuario', True, True, True, True
# modificar_permisos(188, 449, 2396, 'account.move.line.auditoria.usuario', True, True, True, True
# modificar_permisos(188, 674, 2388, 'account.voucher.auditoria.usuario', True, True, False, False
# modificar_permisos(188, 911, 2314, 'Vise_Financiera_usuario', True, True, True, False
# modificar_permisos(188, 1039, 2389, 'account.payment.order.auditoria.usuario', True, True, True, False
# modificar_permisos(188, 1040, 2390, 'account.payment.order.line.auditoria.usuario', True, True, True, False
# modificar_permisos(188, 1041, 2391, 'bank.payment.line.auditoria.usuario', True, True, True, False
# modificar_permisos(188, 1043, 2392, 'account.payment.line.create.auditoria.usuario', True, True, True, True
# modificar_permisos(188, 1157, 2393, 'crossovered.budget.auditoria.usuario', True, True, True, False
# modificar_permisos(188, 1158, 2394, 'crossovered.budget.line.auditoria.usuario', True, True, True, True
# modificar_permisos(188, 1337, 2026, 'Inventario', True, True, True, True
# modificar_permisos(188, 1822, 2338, 'x_categoria_flujo_caja_vise.usuario_interno', True, True, True, True
# modificar_permisos(188, 1826, 2340, 'x_subcategoria_flujo_caja_vise.', True, True, True, False
# modificar_permisos(189, 12, 2448, 'ir.sequence.date_range.vise.contabilidad.general', True, True, True, False
# modificar_permisos(189, 63, 2031, 'ir.module.module', True, True, True, True
# modificar_permisos(189, 79, 2419, 'res.partner.vise.contabilidad.general', True, True, True, False
# modificar_permisos(189, 88, 2415, 'res.company.contabilidad.general', True, True, True, True
# modificar_permisos(189, 433, 3184, 'account.account.vise_contabilidad general', True, False, False, False
# modificar_permisos(189, 436, 443, 'account.journal.group all', True, False, False, False
# modificar_permisos(189, 437, 3242, 'account.journal', True, True, False, False
# modificar_permisos(189, 482, 2416, 'account.setup.bank.manual.config.vise.contabildad.general', True, True, True, False
# modificar_permisos(189, 652, 2447, 'account.move.tax.vise.contabilidad.general', True, True, True, True
# modificar_permisos(189, 676, 2398, 'account.fiscal.year.vise.contabilidad.general', True, True, True, True
# modificar_permisos(189, 911, 2603, 'hr.payslip', True, False, False, False
# modificar_permisos(189, 932, 2941, 'account.asset', True, True, False, False
# modificar_permisos(189, 1040, 2445, 'account.payment.line.vise.contabilidad.general', True, True, True, False
# modificar_permisos(189, 1157, 2446, 'crossovered.budget.vise.contabilidad.general', True, True, True, False
# modificar_permisos(189, 1166, 2417, 'account.loan.vise.contabilidad.general', True, True, True, False
# modificar_permisos(189, 1174, 2643, 'move.petty.cash_vise_contabilidad_general', True, True, True, False
# modificar_permisos(189, 1250, 2915, 'facturacion.wiz_vise_contabilidad_general', True, True, True, True
# modificar_permisos(189, 1337, 2032, 'stock.landed.cost', True, True, True, True
# modificar_permisos(189, 1946, 2443, 'account_financial_reports.export.wizard.vise.contabilidad', True, True, True, False
# modificar_permisos(189, 1947, 2442, 'account_financial_reports.export.wizard.format.vise.contabilidad.general', True, True, True, False
# modificar_permisos(189, 2641, 2798, 'x_imeis.vise_contabilidad_general', True, True, True, False
# modificar_permisos(190, 79, 3014, 'res.partner.vise_contactos contabilidad configuracion', True, True, True, False
# modificar_permisos(190, 82, 3012, 'res.partner.bank.vise_contactos contabilidad configuracion', True, False, True, False
# modificar_permisos(191, 360, 3291, 'hr.employee.vise_grupo almacen', True, False, False, False
# modificar_permisos(193, 91, 3004, 'res.users_vise.grupo.usuario.lector', True, True, False, False
# modificar_permisos(193, 451, 3007, 'account.partial.reconcile.vise_grupo usuario lector', True, False, False, False
# modificar_permisos(193, 494, 3253, 'hr.recruitment.stage.vise_grupo usuario lector', True, False, False, False
# modificar_permisos(193, 508, 2369, 'stock.move.contabilidad.vise.grupo.usuario', True, False, False, False
# modificar_permisos(193, 515, 3245, 'stock.picking.vise_grupo usuario lector', True, True, True, False
# modificar_permisos(193, 660, 2378, 'account.financial.structure.vise.grupo.usuario', True, False, False, False
# modificar_permisos(193, 662, 2377, 'account.financial.levels.manager.vise.grupo.usuario', True, False, False, False
# modificar_permisos(193, 670, 2376, 'account.financial.report.assistant.wizard.manager.vise.grupo.usuario', True, False, False, False
# modificar_permisos(193, 672, 2365, 'account.advance.supplier.contabilidad.vise.grupo.usuario', True, False, False, False
# modificar_permisos(193, 709, 2367, 'purchase.order.contabilidad.vise.grupo.usuario', True, False, False, False
# modificar_permisos(193, 710, 2368, 'purchase.order.line.contabilidad.vise.grupo.usuariol', True, False, False, False
# modificar_permisos(193, 712, 3011, 'purchase.bill.union.vise_grupo usuario lector', True, False, False, False
# modificar_permisos(193, 932, 2942, 'account.asset', True, False, False, False
# modificar_permisos(193, 940, 2375, 'wiz.account.asset.report', True, True, True, False
# modificar_permisos(193, 1036, 2381, 'purchase.requisition.vise.grupo.usuario.lector', True, False, False, False
# modificar_permisos(193, 1037, 2382, 'purchase.requisition.line.vise.grupo.usuario.lector', True, False, False, False
# modificar_permisos(193, 1648, 2975, 'credit.control.line_vise.grupo.usuario.lector', True, False, False, False
# modificar_permisos(193, 1949, 3018, 'avancys_account_followup.followup.line.vise_grupo usuario lector', True, False, False, False
# modificar_permisos(193, 2850, 3033, 'contacto.emergencia.vise_grupo usuario lector', True, False, False, False
# modificar_permisos(193, 2965, 3103, 'x_tags.usuario_interno', True, True, True, True
# modificar_permisos(197, 374, 3002, 'product.template_vise.directores.techzone', True, True, False, False
# modificar_permisos(197, 376, 3001, 'product.product_vise.directores.techzone', True, True, False, False
# modificar_permisos(197, 380, 3003, 'product.attribute.value_vise.directores.techzone', True, True, True, False
# modificar_permisos(197, 512, 2997, 'stock.warehouse.orderpoint_vise.directores.techzone', True, False, False, False
# modificar_permisos(197, 641, 2998, 'crm.tag_vise.directores.techzone', True, False, False, False
# modificar_permisos(197, 643, 2952, 'sale.order_vise.directores.techzone', True, True, True, True
# modificar_permisos(197, 644, 2954, 'sale.order.line_vise.directores.techzone', True, True, True, True
# modificar_permisos(197, 650, 2953, 'sale.order.cancel_vise.directores.techzone', True, True, True, True
# modificar_permisos(197, 679, 2955, 'sale.order.option_vise.directores.techzone', True, True, True, False
# modificar_permisos(197, 680, 2957, 'sale.order.template_vise.directores.techzone', True, True, True, True
# modificar_permisos(197, 681, 2958, 'sale.order.template.line_vise.directores.techzone', True, True, True, True
# modificar_permisos(197, 682, 2959, 'sale.order.template.option_vise.directores.techzone', True, True, True, True
# modificar_permisos(197, 1273, 2956, 'sale.order.rate_vise.directores.techzone', True, True, True, True
# modificar_permisos(197, 1369, 2949, 'project.create.sale.order_vise.directores.techzone', True, True, True, False
# modificar_permisos(197, 1370, 2950, 'project.create.sale.order.line_vise.directores.techzone', True, True, True, True
# modificar_permisos(197, 1372, 2951, 'project.task.create.sale.order_vise.directores.techzone', True, True, True, True
# modificar_permisos(198, 2993, 3179, 'examenes.medicos', True, True, True, False
# modificar_permisos(199, 1411, 2037, 'document.page.history_manager', True, True, True, False
# modificar_permisos(200, 5, 3193, 'ir.model.fields.selection.vise_requisiciones', True, True, True, False
# modificar_permisos(200, 360, 3161, 'hr.employee.vise_requisiciones', True, True, False, False
# modificar_permisos(200, 363, 2027, 'hr.department.vise_requisiciones', True, True, False, False
# modificar_permisos(200, 364, 3151, 'hr.job.vise_requisicion', True, True, False, False
# modificar_permisos(200, 391, 3172, 'hr.contract.vise_requisiciones', True, True, False, False
# modificar_permisos(200, 664, 3194, 'hr.payroll.advance.vise.tecnicos.techzone', True, True, True, False
# modificar_permisos(200, 672, 2364, 'account.advance.supplier.vise.requisiciones', True, False, False, False
# modificar_permisos(200, 709, 1875, 'purchase.order.vise.requisiciones', True, False, False, False
# modificar_permisos(200, 1035, 3009, 'purchase.requisition.type.vise_requisiciones', True, False, False, False
# modificar_permisos(200, 1036, 3008, 'purchase.requisition.vise_requisiciones', True, True, True, False
# modificar_permisos(200, 1037, 3010, 'purchase.requisition.line.vise_requisiciones', True, True, True, True
# modificar_permisos(200, 1337, 3178, 'stock.landed.cost.vise_requisiciones', True, False, False, False
# modificar_permisos(200, 2934, 3116, 'Vise_Requisiciones_01.res_groups_200', True, True, True, False
# modificar_permisos(200, 2941, 3119, 'Vise_Requisiciones_01.res_groups_200', True, True, True, False
# modificar_permisos(200, 2949, 3173, 'Vise_Requisiciones_01.res_groups_200', True, False, False, False
# modificar_permisos(204, 162, 1847, 'credit_control_info_mail_message', True, False, False, False
# modificar_permisos(204, 1645, 1860, 'credit.control.communication info', True, False, False, False
# modificar_permisos(204, 1646, 1853, 'credit_control_info_policy', True, False, False, False
# modificar_permisos(204, 1647, 1856, 'credit_control_info_level', True, False, False, False
# modificar_permisos(204, 1648, 1843, 'credit_control_info_line', True, False, False, False
# modificar_permisos(204, 1649, 1850, 'credit_control_info_run', True, False, False, False
# modificar_permisos(204, 1651, 1872, 'res.partner.payment.action.type info access', True, False, False, False
# modificar_permisos(204, 1657, 1871, 'credit.control.analysis access', True, False, False, False
# modificar_permisos(205, 162, 1846, 'credit_control_user_mail_message', True, True, True, False
# modificar_permisos(205, 1645, 1861, 'credit.control.communication user', True, True, True, False
# modificar_permisos(205, 1646, 1852, 'credit_control_user_policy', True, False, False, False
# modificar_permisos(205, 1647, 1855, 'credit_control_user_level', True, False, False, False
# modificar_permisos(205, 1648, 1842, 'credit_control_user_line', True, True, True, True
# modificar_permisos(205, 1649, 1849, 'credit_control_user_run', True, True, True, True
# modificar_permisos(205, 1653, 1863, 'credit_control_emailer_credit_control_user', True, True, True, False
# modificar_permisos(205, 1654, 1865, 'credit_control_marker_credit_control_user', True, True, True, False
# modificar_permisos(205, 1655, 1867, 'credit_control_printer_credit_control_user', True, True, True, False
# modificar_permisos(205, 1656, 1869, 'credit_control_policy_changer_credit_control_user', True, True, True, False
# modificar_permisos(206, 162, 1845, 'credit_control_manager_mail_message', True, True, True, True
# modificar_permisos(206, 174, 1844, 'credit_control_manager_mail_template', True, True, True, True
# modificar_permisos(206, 1645, 1862, 'credit.control.communication manager', True, True, True, True
# modificar_permisos(206, 1646, 1851, 'credit_control_manager_policy', True, True, True, True
# modificar_permisos(206, 1647, 1854, 'credit_control_manager_level', True, True, True, True
# modificar_permisos(206, 1648, 1841, 'credit_control_manager_line', True, True, True, True
# modificar_permisos(206, 1649, 1848, 'credit_control_mananger_run', True, True, True, True
# modificar_permisos(206, 1651, 1873, 'res.partner.payment.action.type manager access', True, True, True, True
# modificar_permisos(206, 1653, 1864, 'credit_control_emailer_credit_control_manager', True, True, True, False
# modificar_permisos(206, 1654, 1866, 'credit_control_marker_credit_control_manager', True, True, True, False
# modificar_permisos(206, 1655, 1868, 'credit_control_printer_credit_control_manager', True, True, True, False
# modificar_permisos(206, 1656, 1870, 'credit_control_policy_changer_credit_control_manager', True, True, True, False
# modificar_permisos(207, 365, 2021, 'Planear_tipo_de_actividad', True, True, True, True
# modificar_permisos(207, 2934, 3117, 'Vise_Aprobadores.res_groups_207', True, True, False, False
# modificar_permisos(207, 2941, 3120, 'Vise_Aprobadores.res_groups_207', True, True, False, False
# modificar_permisos(207, 2949, 3174, 'Vise_Aprobadores.res_groups_207', True, False, False, False
# modificar_permisos(208, 643, 2999, 'sale.order_vise.pqrs.usuario', True, False, False, False
# modificar_permisos(208, 715, 3000, 'crm.lead_vise.pqrs.usuario', True, False, False, False
# modificar_permisos(208, 1557, 2409, 'helpdesk.team.vise.pqrs.usuario', True, False, False, False
# modificar_permisos(208, 1558, 2403, 'helpdesk.ticket.type.vise.pqrs.usuario', True, False, False, False
# modificar_permisos(208, 1559, 2404, 'helpdesk.sub.type.vise.pqrs.usuario', True, False, True, False
# modificar_permisos(208, 1560, 2401, 'helpdesk.tags.vise.pqrs.usuario', True, False, False, False
# modificar_permisos(208, 1561, 2402, 'helpdesk.stages.vise.pqrs.usuario', True, False, False, False
# modificar_permisos(208, 1562, 2406, 'helpdesk.category.vise.pqrs.usuario', True, False, False, False
# modificar_permisos(208, 1563, 2407, 'helpdesk.subcategory.vise.pqrs.usuario', True, False, False, False
# modificar_permisos(208, 1564, 2408, 'helpdesk.priority.vise.pqrs.usuario', True, False, False, False
# modificar_permisos(208, 1566, 2405, 'helpdesk.release.vise.pqrs.usuario', True, False, False, False
# modificar_permisos(208, 1568, 2400, 'helpdesk.ticket.vise.pqrs.usuario', True, True, True, False
# modificar_permisos(210, 92, 72, 'id_check_employees', True, True, True, False
# modificar_permisos(210, 135, 147, 'uom.category.user', True, False, False, False
# modificar_permisos(210, 137, 150, 'barcode.nomenclature.user', True, False, False, False
# modificar_permisos(210, 138, 152, 'barcode.rule.user', True, False, False, False
# modificar_permisos(210, 349, 248, 'Goal Definition Employee', True, False, False, False
# modificar_permisos(210, 350, 245, 'Goal Employee', True, True, False, False
# modificar_permisos(210, 351, 251, 'Goal Challenge Employee', True, False, False, False
# modificar_permisos(210, 352, 254, 'Challenge Line Employee', True, False, False, False
# modificar_permisos(210, 353, 261, 'Badge-user Employee', True, True, True, False
# modificar_permisos(210, 354, 257, 'Badge Employee', True, False, False, False
# modificar_permisos(210, 360, 274, 'hr.employee system user', False, False, False, False
# modificar_permisos(210, 361, 272, 'hr.employee.category.emp', True, False, False, False
# modificar_permisos(210, 377, 291, 'product.packaging.user', True, False, False, False
# modificar_permisos(210, 380, 298, 'product.attribute value', True, False, False, False
# modificar_permisos(210, 383, 301, 'product..template.attribute exclusion', True, False, False, False
# modificar_permisos(210, 384, 299, 'product.attribute.custom value manager', True, False, False, False
# modificar_permisos(210, 385, 293, 'product.pricelist.user', True, False, False, False
# modificar_permisos(210, 388, 316, 'rating.rating.user', True, True, True, False
# modificar_permisos(210, 393, 330, 'hr.resume.line.employee', True, True, True, True
# modificar_permisos(210, 394, 332, 'hr.resume.line.type.employee', True, False, False, False
# modificar_permisos(210, 395, 338, 'hr.skill.employee', True, False, False, False
# modificar_permisos(210, 396, 340, 'hr.employee.skill', True, True, True, True
# modificar_permisos(210, 397, 336, 'hr.skill.level.employee', True, False, False, False
# modificar_permisos(210, 398, 334, 'hr.skill.type.employee', True, False, False, False
# modificar_permisos(210, 419, 364, 'survey.survey.user', False, False, False, False
# modificar_permisos(210, 420, 368, 'survey.question.user', False, False, False, False
# modificar_permisos(210, 421, 372, 'survey.question.answer.user', False, False, False, False
# modificar_permisos(210, 422, 376, 'survey.user_input.user', False, False, False, False
# modificar_permisos(210, 423, 380, 'survey.user_input.line.user', False, False, False, False
# modificar_permisos(210, 425, 387, 'digest.digest.user', True, False, False, False
# modificar_permisos(210, 426, 389, 'digest.tip.user', True, False, False, False
# modificar_permisos(210, 494, 3106, 'hr.recruitment.stage.vise_requisicion', True, False, False, False
# modificar_permisos(210, 515, 1550, 'stock.picking.manager', True, True, True, False
# modificar_permisos(210, 664, 2372, 'hr.payroll.advance.contabilidad.vise.grupo.usuario', True, False, False, False
# modificar_permisos(210, 666, 2374, 'hr.expense.line,all', True, False, False, False
# modificar_permisos(210, 1032, 1271, 'hr.branch.employee', True, False, False, False
# modificar_permisos(210, 1158, 1372, 'crossovered.budget.lines manager', True, True, True, False
# modificar_permisos(210, 1353, 1549, 'update.delivery.guide.manager', True, True, True, True
# modificar_permisos(210, 1519, 1681, 'maintenance.stage.user', True, False, False, False
# modificar_permisos(210, 1522, 1678, 'equipment.request system user', True, True, True, True
# modificar_permisos(210, 1523, 1683, 'maintenance.team.user', True, False, False, False
# modificar_permisos(210, 1553, 1728, 'dms_directory_base_user', True, False, False, False
# modificar_permisos(210, 1554, 1732, 'dms_file_base_user', True, False, False, False
# modificar_permisos(210, 1579, 2638, 'hr.employee.credentials.line.usuario_interno', True, False, False, False
# modificar_permisos(210, 1631, 1834, 'report.center', True, True, True, True
# modificar_permisos(210, 1633, 1833, 'view.center.button', True, True, True, True
# modificar_permisos(210, 1635, 1837, 'studio.approval.rule', True, True, True, True
# modificar_permisos(210, 2000, 2602, 'x_epidemiological_surveillance_program_interno', True, True, True, True
# modificar_permisos(210, 2170, 2634, 'x_cargos_svsp.usuario_interno', True, True, True, False
# modificar_permisos(210, 2170, 2636, 'x_cargos_svsp.usuario_interno', True, False, False, False
# modificar_permisos(210, 2172, 2635, 'x_cursos_peis.usuario_interno', True, True, True, False
# modificar_permisos(210, 2182, 2642, 'x_paz_y_salvo.usuario_interno', True, True, True, False
# modificar_permisos(210, 2424, 2795, 'x_tesoreria.usuario_interno', True, True, True, False
# modificar_permisos(210, 2643, 2799, 'x_operador_linea.usuario_interno', True, True, True, True
# modificar_permisos(210, 2645, 2800, 'x_planes_de_celular.usuario_interno', True, True, True, True
# modificar_permisos(210, 2649, 2803, 'x_email_celulares.usuario_interno', True, True, True, True
# modificar_permisos(210, 2651, 2804, 'x_modelo_disposivo.usuario_interno', True, True, True, True
# modificar_permisos(210, 2653, 2805, 'x_estado_dispositivo.usuario_interno', True, True, True, False
# modificar_permisos(210, 2655, 2806, 'x_estado_de_linea.usuario_interno', True, True, True, True
# modificar_permisos(210, 2722, 2918, 'auditlog_rule_user', False, False, False, False
# modificar_permisos(210, 2723, 2921, 'auditlog_http_session_user', False, False, False, False
# modificar_permisos(210, 2724, 2922, 'auditlog_http_request_user', False, False, False, False
# modificar_permisos(210, 2725, 2919, 'auditlog_log_user', False, False, False, False
# modificar_permisos(210, 2726, 2920, 'auditlog_log_line_user', False, False, False, False
# modificar_permisos(210, 2744, 2944, 'x_decision', True, True, True, True
# modificar_permisos(210, 2746, 2945, 'x_comunicaciones_configuracion', True, True, True, True
# modificar_permisos(210, 2802, 3016, 'x_paz_y_salvo', True, True, True, True
# modificar_permisos(210, 2804, 3013, 'x_paz_y_salvo', True, True, True, True
# modificar_permisos(210, 2806, 3015, 'x_paz_y_salvo', True, True, True, True
# modificar_permisos(210, 2809, 3005, 'x_requisicion.line_empleado', True, True, True, True
# modificar_permisos(210, 2969, 3107, 'x_ui.solicitud.usuario_interno', True, True, True, True
# modificar_permisos(210, 2971, 3108, 'x_ui.solicitud.servicio.tipo.estudio.usuario_interno', True, False, False, False
# modificar_permisos(210, 2973, 3109, 'x_ui.solicitud.servicio.modalidad.usuario_interno', True, False, False, False
# modificar_permisos(210, 2975, 3110, 'x_ui.solicitud.servicio.tipo.prueba.usuario_interno', True, False, False, False
# modificar_permisos(210, 2977, 3111, 'x_ui.solicitud.servicio.deteccion.engano.usuario_interno', True, False, False, False
# modificar_permisos(210, 2981, 3112, 'x_ui.solicitud.servicio.concepto.usuario_interno', True, False, False, False
# modificar_permisos(210, 2983, 3113, 'x_ui.solicitud.servicio.estado.usuario_interno', True, False, False, False
# modificar_permisos(210, 2985, 3114, 'x_ui.solicitud.servicio.usuario_interno', True, True, True, True
# modificar_permisos(210, 2987, 3115, 'x_ui.solicitud.estado.usuario_interno', True, True, True, True
# modificar_permisos(210, 2996, 3182, 'tipo_sancion_procesos_disciplinarios.tipo_sancion_procesos_disciplinarios', True, True, True, True
# modificar_permisos(210, 2997, 3183, 'tipo_motivo_procesos_disciplinarios.tipo_motivo_procesos_disciplinarios', True, True, True, True
# modificar_permisos(210, 3002, 3186, 'x_kactus.usuario_interno', True, True, True, True
# modificar_permisos(210, 3004, 3187, 'x_kactus.bi_emple.usuario_interno', True, True, True, True
# modificar_permisos(210, 3036, 3188, 'x_kactus.nm_contr.usuario_interno', True, True, True, True
# modificar_permisos(210, 3038, 3189, 'x_kactus.nm_disrf.usuario_interno', True, True, True, True
# modificar_permisos(210, 3040, 3191, 'x_kactus.nm_cuent.usuario_interno', True, True, True, True
# modificar_permisos(212, 79, 1884, 'res.partner.purchase.manager', True, True, True, False
# modificar_permisos(212, 135, 1885, 'uom.category_purchase_manager', True, True, True, True
# modificar_permisos(212, 136, 1886, 'uom.uom_purchase_manager', True, True, True, True
# modificar_permisos(212, 375, 1887, 'product.category_purchase_manager', True, False, False, False
# modificar_permisos(212, 376, 1881, 'product.product_purchase_manager', True, True, True, True
# modificar_permisos(212, 377, 1889, 'product.packaging_purchase_manager', True, True, True, True
# modificar_permisos(212, 378, 1890, 'product.supplierinfo_purchase_manager', True, True, True, True
# modificar_permisos(212, 386, 1891, 'product.pricelist.item_purchase_manager', True, True, True, True
# modificar_permisos(212, 449, 1883, 'account.move.line', True, True, True, True
# modificar_permisos(212, 506, 1894, 'stock.location', True, False, False, False
# modificar_permisos(212, 508, 1897, 'stock.move', True, True, True, True
# modificar_permisos(212, 512, 1898, 'stock.warehouse.orderpoint', True, False, False, False
# modificar_permisos(212, 515, 1896, 'stock.picking', True, True, True, False
# modificar_permisos(212, 518, 1895, 'stock.warehouse', True, False, False, False
# modificar_permisos(212, 709, 1878, 'purchase.order', True, False, False, False
# modificar_permisos(212, 710, 1879, 'purchase.order.line', True, False, False, False
# modificar_permisos(212, 711, 1893, 'purchase.stock.report', True, False, False, False
# modificar_permisos(212, 713, 1899, 'vendor.delay.report', True, False, False, False
# modificar_permisos(212, 1035, 1900, 'purchase.requisition.type', True, True, True, True
# modificar_permisos(212, 1036, 1901, 'purchase.requisition_manager', True, False, False, False
# modificar_permisos(212, 1037, 1902, 'purchase.requisition.line_manager', True, False, False, False
# modificar_permisos(214, 339, 2025, 'account.analytic.account.vise.eficiencia', True, True, True, True
# modificar_permisos(214, 340, 2024, 'Vise.eficiencia.Analistas', True, True, True, True
# modificar_permisos(214, 715, 2399, 'crm.lead.vise.eficiencia', True, False, False, False
# modificar_permisos(214, 1277, 2631, 'project.service.order.analistas.eficiencia', True, True, True, False
# modificar_permisos(217, 86, 1926, 'res.currency_account_manager', True, True, True, True
# modificar_permisos(217, 87, 1927, 'res.currency.rate_account_manager', True, True, True, True
# modificar_permisos(217, 376, 1933, 'product.product.account.manager', True, True, True, True
# modificar_permisos(217, 428, 1930, 'account.fiscal.position_account.manager', True, True, True, True
# modificar_permisos(217, 429, 1931, 'account.fiscal.position.tax_account.manager', True, True, True, True
# modificar_permisos(217, 430, 1932, 'account.fiscal.position_account.manager', True, True, True, True
# modificar_permisos(217, 432, 1942, 'account.account.type', True, True, True, True
# modificar_permisos(217, 432, 1967, 'account.account.type.manager', True, True, True, True
# modificar_permisos(217, 434, 1939, 'account.group', True, True, True, True
# modificar_permisos(217, 435, 1940, 'account.root', True, False, False, False
# modificar_permisos(217, 436, 1938, 'account.journal.group_manager', True, True, True, True
# modificar_permisos(217, 438, 1947, 'account.tax.group', True, True, True, True
# modificar_permisos(217, 439, 1943, 'account.tax', True, True, True, True
# modificar_permisos(217, 440, 1944, 'account.tax_repartition.line.manager', True, True, True, True
# modificar_permisos(217, 441, 1946, 'account.tax.report.ac.user', True, True, True, True
# modificar_permisos(217, 442, 1945, 'account.tax.report.line.ac.user', True, True, True, True
# modificar_permisos(217, 446, 1948, 'account.payment.term', True, True, True, True
# modificar_permisos(217, 447, 1949, 'account.payment.term.line', True, True, True, True
# modificar_permisos(217, 453, 1950, 'Full_access_on_account.payment.method_to_Financial_Manager', True, True, True, True
# modificar_permisos(217, 460, 1925, 'account.group.template', True, True, True, True
# modificar_permisos(217, 461, 1920, 'account.account.template', True, True, True, True
# modificar_permisos(217, 462, 1915, 'account.chart.template', True, True, True, True
# modificar_permisos(217, 463, 1921, 'account.tax.template', True, True, True, True
# modificar_permisos(217, 464, 1922, 'account.tax_repartition.line.template.manager', True, True, True, True
# modificar_permisos(217, 465, 1916, 'account.fiscal.position.template', True, True, True, True
# modificar_permisos(217, 466, 1917, 'account.fiscal.position.tax.template', True, True, True, True
# modificar_permisos(217, 467, 1918, 'account.fiscal.position.account.template', True, True, True, True
# modificar_permisos(217, 468, 1923, 'account.reconcile.model.template', True, True, True, True
# modificar_permisos(217, 469, 1924, 'account.reconcile.model.line.template', True, True, True, True
# modificar_permisos(217, 471, 1929, 'account.incoterms_manager', True, True, True, True
# modificar_permisos(217, 480, 1951, 'access.account.resequence.wizard', True, True, True, False
# modificar_permisos(217, 481, 1952, 'access.account.financial.year.op', True, True, True, False
# modificar_permisos(217, 482, 1953, 'access.account.setup.bank.manual.config', True, True, True, False
# modificar_permisos(217, 486, 1954, 'account.tour.upload.bill', True, True, True, False
# modificar_permisos(217, 487, 1955, 'account.tour.upload.bill.email.confirm', True, True, True, False
# modificar_permisos(217, 488, 1928, 'account.invoice.report', True, True, True, True
# modificar_permisos(217, 642, 1956, 'Full_access_on_account.payment.mode_to_Financial_Manager', True, True, True, True
# modificar_permisos(217, 652, 1958, 'account.move.tax.manager', True, True, True, True
# modificar_permisos(217, 653, 1957, 'res.ciiu.manager', True, True, True, True
# modificar_permisos(217, 654, 1962, 'account.financial.report.balance.manager', True, True, True, True
# modificar_permisos(217, 655, 1963, 'account.financial.report.balance.line.manager', True, True, True, True
# modificar_permisos(217, 656, 1976, 'account.financial.report.balance.manager', True, True, True, True
# modificar_permisos(217, 657, 1977, 'account.financial.report.balance.line.manager', True, True, True, True
# modificar_permisos(217, 658, 1969, 'account.financial.report.taxes.manager', True, True, True, True
# modificar_permisos(217, 659, 1970, 'account.financial.report.taxes.line.manager', True, True, True, True
# modificar_permisos(217, 660, 1959, 'account.financial.structure.manager', True, True, True, True
# modificar_permisos(217, 661, 1960, 'account.financial.structure.line.manager', True, True, True, True
# modificar_permisos(217, 662, 1961, 'account.financial.levels.manager', True, True, True, True
# modificar_permisos(217, 663, 1966, 'excel.report.avancys.manager', True, True, True, True
# modificar_permisos(217, 664, 1971, 'hr.payroll.advance.manager', True, False, True, True
# modificar_permisos(217, 666, 1973, 'hr.expense.line.manager', True, True, True, True
# modificar_permisos(217, 667, 1974, 'hr.expense.tax.manager', True, True, True, True
# modificar_permisos(217, 668, 1975, 'account.financial.report.trial.wizard.manager', True, True, True, True
# modificar_permisos(217, 669, 1964, 'account.financial.report.balance.wizard.manager', True, True, True, True
# modificar_permisos(217, 670, 1965, 'account.financial.report.assistant.wizard.manager', True, True, True, True
# modificar_permisos(217, 671, 1968, 'account.financial.report.taxes.wizard.manager', True, True, True, True
# modificar_permisos(217, 672, 1978, 'account.advance.supplier.manager', True, False, False, False
# modificar_permisos(217, 673, 1979, 'account.advance.customer.manager', True, True, True, True
# modificar_permisos(217, 674, 1980, 'account.voucher.manager', True, True, True, True
# modificar_permisos(217, 675, 1981, 'account.voucher.line.manager', True, True, True, True
# modificar_permisos(217, 675, 1998, 'account.voucher.line.manager', True, True, True, True
# modificar_permisos(217, 676, 1995, 'account.fiscal.year.manager', True, True, True, True
# modificar_permisos(217, 678, 1982, 'access.account.change.lock.date', True, True, True, False
# modificar_permisos(217, 684, 1996, 'access.date.range.manager', True, False, False, False
# modificar_permisos(217, 810, 1989, 'account.container.group.manager', True, True, True, True
# modificar_permisos(217, 817, 1986, 'account.financial.report.balance.inventory.wizard.manager', True, True, True, True
# modificar_permisos(217, 818, 1987, 'account.financial.report.major.balance.wizard.manager', True, True, True, True
# modificar_permisos(217, 819, 1988, 'account.financial.report.state.income.wizard.manager', True, True, True, True
# modificar_permisos(217, 820, 1984, 'account.financial.report.balance.general.wizard.manager', True, True, True, True
# modificar_permisos(217, 821, 1985, 'account.financial.report.diario.wizard.manager', True, True, True, True
# modificar_permisos(217, 932, 1991, 'account.asset', True, False, False, False
# modificar_permisos(217, 933, 1994, 'account.asset.group', True, True, True, True
# modificar_permisos(217, 934, 1990, 'account.asset.profile', True, True, True, True
# modificar_permisos(217, 935, 1992, 'account.asset.line', True, True, True, True
# modificar_permisos(217, 936, 1993, 'account.asset.recompute.trigger', True, True, True, True
# modificar_permisos(217, 1045, 1999, 'acces.account.consignment.manager', True, True, True, True
# modificar_permisos(217, 1156, 2001, 'account.budget.post', True, False, False, False
# modificar_permisos(217, 1157, 2000, 'crossovered.budget', True, False, False, False
# modificar_permisos(217, 1173, 2002, 'name_open_petty_cash', True, True, True, True
# modificar_permisos(217, 1174, 2003, 'name_move_petty_cash', True, True, True, True
# modificar_permisos(217, 1176, 2004, 'account.asset.line.niff', True, True, True, True
# modificar_permisos(217, 1182, 2005, 'account_payment_mean_manager', True, True, True, True
# modificar_permisos(217, 1183, 2006, 'account_payment_mean_code_manager', True, True, True, True
# modificar_permisos(217, 1184, 2007, 'account.move.discrepancy.response.code.manager', True, True, True, True
# modificar_permisos(217, 1187, 2008, 'account_fiscal_position_party_tax_scheme_manager', True, True, True, True
# modificar_permisos(217, 1188, 2009, 'account_fiscal_position_tax_level_code_manager', True, True, True, True
# modificar_permisos(217, 1287, 2898, 'hr.roster.close.distribution', True, True, True, True
# modificar_permisos(217, 1648, 2010, 'credit_control_fin_manager_line', True, True, True, True
# modificar_permisos(218, 672, 2030, 'account.advance.supplier', True, True, True, True
# modificar_permisos(223, 664, 2018, 'hr.payroll.advance', True, True, True, True
# modificar_permisos(224, 360, 3292, 'hr.employee.vise_inventarios usuarios', True, False, False, False
# modificar_permisos(225, 374, 2028, 'Vise.Inventarios.Administrador', True, True, True, True
# modificar_permisos(227, 83, 2304, 'Configuración', True, True, True, False
# modificar_permisos(227, 360, 2059, 'Vise_cursos_seguridad', True, True, True, False
# modificar_permisos(227, 1525, 2058, 'vise_cursos_seguridad', True, True, True, False
# modificar_permisos(227, 1538, 2061, 'Vise_cursos_seguridad', True, True, True, False
# modificar_permisos(227, 1539, 2062, 'Vise_cursos_seguridad', True, True, True, False
# modificar_permisos(227, 1576, 2063, 'hr.employee.accreditation_vise.cursos.seguridad', True, True, True, False
# modificar_permisos(227, 1577, 2064, 'hr.employee.accreditation.line_vise.cursos.seguridad', True, False, False, False
# modificar_permisos(228, 63, 2324, 'Vise_tecnicos', True, True, True, False
# modificar_permisos(228, 567, 2331, 'Vise_Tecnicos', True, True, True, True
# modificar_permisos(228, 664, 2298, 'hr.payroll.advance.vise.tecnicos.techzone', True, True, True, False
# modificar_permisos(228, 666, 2301, 'Vise_Tecnicos', True, True, True, True
# modificar_permisos(228, 667, 2322, 'tecnicos', True, True, True, True
# modificar_permisos(239, 27, 3036, 'Vise Botón Confirmar Factura', True, True, True, True
# modificar_permisos(239, 557, 3035, 'Vise Botón Confirmar Factura', True, True, True, True
# modificar_permisos(243, 27, 2733, 'ir.attachment.vise_cursos_acredityaciones_formacion_otros', True, True, True, False
# modificar_permisos(243, 353, 2598, 'gamification.badge.vise_cursos_acredityaciones_formacion_otros', True, False, False, False
# modificar_permisos(243, 557, 2600, 'access_theme_ir_attachment.vise_cursos_acredityaciones_formacion_otros', True, True, True, False
# modificar_permisos(243, 1525, 2597, 'audit.audit.vise_cursos_acredityaciones_formacion_otros', True, False, False, False
# modificar_permisos(243, 1538, 2595, 'audit.process.vise_cursos_acredityaciones_formacion_otros', True, False, False, False
# modificar_permisos(243, 1539, 2596, 'audit.system.vise_cursos_acredityaciones_formacion_otros', True, False, False, False
# modificar_permisos(243, 1576, 2565, 'hr.employee.accreditation.vise_cursos_acredityaciones_formacion_otros', True, True, True, False
# modificar_permisos(243, 1577, 2566, 'hr.employee.accreditation.line_vise_cursos_acredityaciones_formacion_otros', True, False, False, False
# modificar_permisos(243, 1578, 2653, 'hr.employee.credentials.vise_cursos_acredityaciones_formacion_otros', True, True, True, False
# modificar_permisos(243, 1579, 2732, 'hr.employee.credentials.vise_cursos_acredityaciones_formacion_otros', True, False, False, False
# modificar_permisos(243, 2172, 2637, 'x_cursos_peis.usuario_interno', True, False, False, False
# modificar_permisos(246, 926, 2617, 'project.task.vise_proyectos_usuarios', True, True, True, False
# modificar_permisos(247, 2158, 2626, 'pdforientation access', True, True, True, True
# modificar_permisos(247, 2159, 2625, 'querydeluxe access', True, True, True, True
# modificar_permisos(247, 2160, 2627, 'tipsqueries access', True, True, True, True
# modificar_permisos(254, 1258, 1444, 'hr_roster_avancys.hr_roster_modalidad', True, False, False, False
# modificar_permisos(254, 2679, 2892, 'hr_roster_avancys.hr_tarifario', True, True, True, True
# modificar_permisos(254, 2734, 2935, 'hr_roster_avancys.hr_inductions', True, True, True, True
# modificar_permisos(255, 1160, 2816, 'hr_roster_avancys.res_regional', True, False, False, False
# modificar_permisos(255, 1234, 2851, 'hr_roster_avancys.remplazo_novedad_wiz', True, True, True, True
# modificar_permisos(255, 1235, 2849, 'hr_roster_avancys.massive_shift_scheduling', True, True, True, True
# modificar_permisos(255, 1236, 2850, 'hr_roster_avancys.massive_shift_scheduling_wizard', True, True, True, True
# modificar_permisos(255, 1237, 2855, 'hr_roster_avancys.manual_entry', True, True, True, True
# modificar_permisos(255, 1238, 2856, 'hr_roster_avancys.activos_puesto_wiz', True, True, True, True
# modificar_permisos(255, 1239, 2858, 'hr_roster_avancys.order_puesto_wiz', True, True, True, True
# modificar_permisos(255, 1241, 2859, 'hr_roster_avancys.cierre_programacion_wiz', True, True, True, True
# modificar_permisos(255, 1242, 2843, 'hr_roster_avancys.cierre_nomina_wiz', True, True, True, True
# modificar_permisos(255, 1243, 2860, 'hr_roster_avancys.programacion_modalidad_wiz', True, True, True, True
# modificar_permisos(255, 1244, 2861, 'hr_roster_avancys.hr_roster_adicionales', True, True, True, True
# modificar_permisos(255, 1245, 2862, 'hr_roster_avancys.hr_roster_adicional_day', True, True, True, True
# modificar_permisos(255, 1247, 2864, 'access_hr_roster_cambio_turno', True, True, True, True
# modificar_permisos(255, 1248, 2865, 'access_hr_roster_cambio_update', True, True, True, True
# modificar_permisos(255, 1249, 2857, 'hr_roster_avancys.hr_roster_reverse_close', True, True, True, True
# modificar_permisos(255, 1252, 2832, 'hr_roster_avancys.hr_roster_disponibles', True, True, True, True
# modificar_permisos(255, 1253, 2833, 'hr_roster_avancys.hr_roster_puesto_tarifa_adicional', True, True, True, True
# modificar_permisos(255, 1254, 2834, 'hr_roster_avancys.hr_roster_puesto', True, True, True, True
# modificar_permisos(255, 1255, 2835, 'hr_roster_avancys.hr_roster_puesto_bono', True, True, True, True
# modificar_permisos(255, 1256, 2836, 'hr_roster_avancys.hr_roster_bono', True, True, True, True
# modificar_permisos(255, 1257, 2837, 'hr_roster_avancys.hr_roster_puesto_items_cliente', True, True, True, True
# modificar_permisos(255, 1258, 2838, 'hr_roster_avancys.hr_roster_modalidad', True, True, True, True
# modificar_permisos(255, 1259, 2839, 'hr_roster_avancys.hr_roster_horario', True, True, True, True
# modificar_permisos(255, 1260, 2840, 'hr_roster_avancys.hr_roster_tipo_turno', True, True, True, True
# modificar_permisos(255, 1261, 2841, 'hr_roster_avancys.hr_roster_turno', True, True, True, True
# modificar_permisos(255, 1262, 2842, 'hr_roster_avancys.hr_roster_sequence', True, True, True, True
# modificar_permisos(255, 1263, 2844, 'hr_roster_avancys.hr_roster_programacion', True, True, True, True
# modificar_permisos(255, 1264, 2845, 'hr_roster_avancys.hr_roster_programacion_line', True, True, True, True
# modificar_permisos(255, 1265, 2846, 'hr_roster_avancys.hr_roster_timesheet', True, True, True, True
# modificar_permisos(255, 1266, 2847, 'hr_roster_avancys.account_move_line_print', True, True, True, True
# modificar_permisos(255, 1267, 2825, 'hr_roster_avancys.hr_roster_prefactura', True, True, True, True
# modificar_permisos(255, 1268, 2826, 'hr_roster_avancys.hr_roster_prefactura_line', True, True, True, True
# modificar_permisos(255, 1269, 2827, 'hr_roster_avancys.account_move_profile', True, True, True, True
# modificar_permisos(255, 1270, 2828, 'hr_roster_avancys.hr_roster_concept_distribution', True, True, True, True
# modificar_permisos(255, 1271, 2829, 'hr_roster_avancys.hr_roster_sale_concept', True, True, True, True
# modificar_permisos(255, 1272, 2830, 'hr_roster_avancys.hr_roster_sale_distribution', True, True, True, True
# modificar_permisos(255, 1273, 2831, 'hr_roster_avancys.sale_order_rate', True, True, True, True
# modificar_permisos(255, 1274, 2853, 'hr_roster_avancys.hr_holiday_public', True, True, True, True
# modificar_permisos(255, 1275, 2854, 'hr_roster_avancys.hr_holiday_lines', True, True, True, True
# modificar_permisos(255, 1276, 2817, 'hr_roster_avancys.res_weekday', True, True, True, True
# modificar_permisos(255, 1277, 2822, 'hr_roster_avancys.project_service_order', True, True, True, True
# modificar_permisos(255, 1278, 2823, 'hr_roster_avancys.project_linea_negocio', True, True, True, True
# modificar_permisos(255, 1279, 2824, 'hr_roster_avancys.project_service_type', True, True, True, True
# modificar_permisos(255, 1280, 2819, 'hr_roster_avancys.project_service_order_support', True, True, True, True
# modificar_permisos(255, 1281, 2818, 'hr_roster_avancys.project_service_order_tmp', True, True, True, True
# modificar_permisos(255, 1282, 2848, 'hr_roster_avancys.service_order_line_secuence', True, True, True, True
# modificar_permisos(255, 1283, 2821, 'hr_roster_avancys.project_service_order_line', True, True, True, True
# modificar_permisos(255, 1284, 2820, 'hr_roster_avancys.order_line_detail', True, True, True, True
# modificar_permisos(255, 1285, 2863, 'hr_roster_avancys.payslip_period', True, True, True, True
# modificar_permisos(255, 2660, 2852, 'hr_roster_avancys.remplazo_novedad_wiz_masive', True, True, True, True
# modificar_permisos(255, 2676, 2883, 'hr_roster_avancys.tarifario_wiz', True, True, True, True
# modificar_permisos(255, 2677, 2886, 'hr_roster_avancys.validate_tarifario', True, True, True, True
# modificar_permisos(255, 2679, 2887, 'hr_roster_avancys.hr_tarifario', True, True, True, True
# modificar_permisos(255, 2680, 2884, 'hr_roster_avancys.hr_roster_tarifario', True, True, True, True
# modificar_permisos(255, 2681, 2885, 'hr_roster_avancys.hr_roster_tarifario_line', True, True, True, True
# modificar_permisos(255, 2702, 2902, 'hr_roster_avancys.hr_programacion_line_run', True, True, True, True
# modificar_permisos(255, 2734, 2934, 'hr_roster_avancys.hr_inductions', True, True, True, True
# modificar_permisos(257, 515, 2866, 'Restricción para crear transferencias', True, False, False, False
# modificar_permisos(258, 1261, 2893, 'hr_roster_avancys.hr_roster_turno', True, True, True, True
# modificar_permisos(260, 1557, 2904, 'access_helpdesk_team_user', True, False, False, False
# modificar_permisos(260, 1558, 2905, 'access_helpdesk_ticket_type_user', True, False, False, False
# modificar_permisos(260, 1559, 2906, 'access_helpdesk_sub_type_user', True, False, False, False
# modificar_permisos(260, 1560, 2907, 'access_helpdesk_tags_user', True, False, False, False
# modificar_permisos(260, 1561, 2908, 'access_helpdesk_stages_user', True, True, True, False
# modificar_permisos(260, 1562, 2909, 'access_helpdesk_category_user', True, False, False, False
# modificar_permisos(260, 1563, 2911, 'access_helpdesk_subcategory_user', True, False, False, False
# modificar_permisos(260, 1564, 2912, 'access_helpdesk_priority_user', True, False, False, False
# modificar_permisos(260, 1566, 2910, 'access_helpdesk_release', True, False, False, False
# modificar_permisos(260, 1568, 2913, 'access_helpdesk_ticket_user', True, True, True, False
# modificar_permisos(260, 1570, 2914, 'access_helpdesk_dashboard_user', True, True, True, True
# modificar_permisos(269, 2777, 2976, 'access_electronic_invoice_resolution_manager', True, True, True, True
# modificar_permisos(269, 2778, 2979, 'access_ei_transaction_log_manager', True, True, True, True
# modificar_permisos(269, 2779, 2982, 'access_ei_multi_process_manager', True, True, True, True
# modificar_permisos(269, 2780, 2985, 'access_ei_state_Reset_manager', True, True, True, True
# modificar_permisos(270, 2777, 2977, 'access_electronic_invoice_resolution_user', True, True, False, False
# modificar_permisos(270, 2778, 2980, 'access_ei_transaction_log_user', True, True, False, False
# modificar_permisos(270, 2779, 2983, 'access_ei_multi_process_user', True, True, True, False
# modificar_permisos(271, 27, 2995, 'ir.attachment_vise.eliminar.adjuntos', True, True, True, True
# modificar_permisos(271, 2787, 2996, 'mail.tracking.email_vise.eliminar.adjuntos', True, False, False, False
# modificar_permisos(273, 924, 3301, 'project.task.type.user', True, False, False, False
# modificar_permisos(273, 925, 3300, 'project.project', True, True, True, False
# modificar_permisos(273, 2679, 3289, 'hr_roster_avancys.hr_tarifario', True, False, False, False
# modificar_permisos(273, 2967, 3104, 'x_operaciones.vise_operaciones analistas', True, True, True, True
# modificar_permisos(274, 27, 3122, 'ir_attachment group_analistas', True, True, True, True
# modificar_permisos(274, 2969, 3131, 'x_ui.solicitud.analistas', True, True, True, False
# modificar_permisos(274, 2971, 3124, 'x_ui.solicitud.analistas', True, False, False, False
# modificar_permisos(274, 2973, 3125, 'x_ui.solicitud.analistas', True, False, False, False
# modificar_permisos(274, 2975, 3123, 'x_ui.solicitud.analistas', True, False, False, False
# modificar_permisos(274, 2977, 3127, 'x_ui.solicitud.analistas', True, False, False, False
# modificar_permisos(274, 2981, 3128, 'x_ui.solicitud.analistas', True, False, False, False
# modificar_permisos(274, 2983, 3126, 'x_ui.solicitud.analistas', True, False, False, False
# modificar_permisos(274, 2985, 3129, 'x_ui.solicitud.analistas', True, True, True, False
# modificar_permisos(274, 2987, 3130, 'x_ui.solicitud.analistas', True, True, True, False
# modificar_permisos(275, 79, 3141, 'Crear Contacto', True, True, True, False
# modificar_permisos(275, 2969, 3140, 'x_ui.solicitud.clientes', True, True, True, False
# modificar_permisos(275, 2971, 3133, 'x_ui.solicitud.clientes', True, False, False, False
# modificar_permisos(275, 2973, 3134, 'x_ui.solicitud.clientes', True, False, False, False
# modificar_permisos(275, 2975, 3132, 'x_ui.solicitud.clientes', True, False, False, False
# modificar_permisos(275, 2977, 3136, 'x_ui.solicitud.clientes', True, False, False, False
# modificar_permisos(275, 2981, 3137, 'x_ui.solicitud.clientes', True, False, False, False
# modificar_permisos(275, 2983, 3135, 'x_ui.solicitud.clientes', True, False, False, False
# modificar_permisos(275, 2985, 3138, 'x_ui.solicitud.clientes', True, True, True, False
# modificar_permisos(275, 2987, 3139, 'x_ui.solicitud.clientes', True, False, False, False
# modificar_permisos(277, 2969, 3160, 'x_ui.solicitud.profecionales', True, True, False, False
# modificar_permisos(277, 2971, 3153, 'x_ui.solicitud.profesionales', True, False, False, False
# modificar_permisos(277, 2973, 3154, 'x_ui.solicitud.profesionales', True, False, False, False
# modificar_permisos(277, 2975, 3152, 'x_ui.solicitud.profesionales', True, False, False, False
# modificar_permisos(277, 2977, 3156, 'x_ui.solicitud.profesionales', True, False, False, False
# modificar_permisos(277, 2981, 3157, 'x_ui.solicitud.profesionales', True, False, False, False
# modificar_permisos(277, 2983, 3155, 'x_ui.solicitud.profesionales', True, False, False, False
# modificar_permisos(277, 2985, 3158, 'x_ui.solicitud.profesionales', True, True, False, False
# modificar_permisos(277, 2987, 3159, 'x_ui.solicitud.profesionales', True, False, False, False
# modificar_permisos(278, 79, 3171, 'Crear Contacto', True, True, True, False
# modificar_permisos(278, 2969, 3170, 'x_ui.solicitud.sucursales', True, True, True, False
# modificar_permisos(278, 2971, 3163, 'x_ui.solicitud.sucursales', True, False, False, False
# modificar_permisos(278, 2973, 3164, 'x_ui.solicitud.sucursales', True, False, False, False
# modificar_permisos(278, 2975, 3162, 'x_ui.solicitud.sucursales', True, False, False, False
# modificar_permisos(278, 2977, 3166, 'x_ui.solicitud.sucursales', True, False, False, False
# modificar_permisos(278, 2981, 3167, 'x_ui.solicitud.sucursales', True, False, False, False
# modificar_permisos(278, 2983, 3165, 'x_ui.solicitud.sucursales', True, False, False, False
# modificar_permisos(278, 2985, 3168, 'x_ui.solicitud.sucursales', True, True, True, False
# modificar_permisos(278, 2987, 3169, 'x_ui.solicitud.sucursales', True, False, False, False
# modificar_permisos(279, 924, 1173, 'project.task.type.user', True, False, False, False
# modificar_permisos(279, 925, 3299, 'project.project.vise_operaciones coordinadores', True, True, False, False
# modificar_permisos(279, 2679, 3297, 'hr.tarifario_vise_eficiencia_usuario', True, False, False, False
# modificar_permisos(279, 2734, 3298, 'hr.inductions_vise_grupo_eficiencia_usuarios', True, False, False, False
# modificar_permisos(279, 2967, 3247, 'x_operaciones_puestos', True, False, False, False
# modificar_permisos(279, 3122, 3248, 'x_operaciones_estado', True, False, False, False
# modificar_permisos(280, 3169, 3260, 'Acceso a Usuarios', True, False, False, False
# modificar_permisos(280, 3172, 3262, 'Acceso a Clientes', True, False, False, False
# modificar_permisos(280, 3174, 3268, 'Acceso a Grupo de Sector', True, False, False, False
# modificar_permisos(280, 3175, 3261, 'Acceso a Tipos de Usuario', True, False, False, False
# modificar_permisos(280, 3176, 3263, 'Acceso a Preguntas', True, False, False, False
# modificar_permisos(280, 3177, 3264, 'Acceso a Tipos de Pregunta', True, False, False, False
# modificar_permisos(280, 3178, 3265, 'Acceso a Opciones de Pregunta', True, False, False, False
# modificar_permisos(280, 3179, 3266, 'Acceso a Grupo de Pregunta', True, False, False, False
# modificar_permisos(280, 3181, 3269, 'Acceso a Respuestas', True, False, False, False
# modificar_permisos(280, 3182, 3270, 'Acceso a Formulario de Respuestas', True, False, False, False
# modificar_permisos(280, 3199, 3267, 'Acceso a Grupo de Fuente', True, False, False, False
# modificar_permisos(281, 5, 3287, 'ir.model.fields.selection.vise_requisiciones', True, True, True, False
# modificar_permisos(281, 360, 3283, 'hr.employee.vise_requisiciones', True, True, False, False
# modificar_permisos(281, 363, 3275, 'hr.department.vise_requisiciones', True, True, False, False
# modificar_permisos(281, 364, 3282, 'hr.job.vise_requisicion', True, True, False, False
# modificar_permisos(281, 391, 3284, 'hr.contract.vise_requisiciones', True, True, False, False
# modificar_permisos(281, 664, 3288, 'hr.payroll.advance.vise.tecnicos.techzone', True, True, True, False
# modificar_permisos(281, 672, 3276, 'account.advance.supplier.vise.requisiciones', True, False, False, False
# modificar_permisos(281, 709, 3274, 'purchase.order.vise.requisiciones', True, False, False, False
# modificar_permisos(281, 1035, 3278, 'purchase.requisition.type.vise_requisiciones', True, False, False, False
# modificar_permisos(281, 1036, 3277, 'purchase.requisition.vise_requisiciones', True, True, True, False
# modificar_permisos(281, 1037, 3279, 'purchase.requisition.line.vise_requisiciones', True, True, True, True
# modificar_permisos(281, 1337, 3286, 'stock.landed.cost.vise_requisiciones', True, False, False, False
# modificar_permisos(281, 2934, 3280, 'Vise_Requisiciones_01.res_groups_200', True, True, True, False
# modificar_permisos(281, 2941, 3281, 'Vise_Requisiciones_01.res_groups_200', True, True, True, False
# modificar_permisos(281, 2949, 3285, 'Vise_Requisiciones_01.res_groups_200', True, False, False, False
# modificar_permisos(, 14, 36, 'ir_ui_view_custom_group_user', True, True, True, True
# modificar_permisos(, 15, 2615, 'ir_ui_view group_user', False, False, False, False
# modificar_permisos(, 27, 2614, 'ir_attachment group_portal_public', False, False, False, False
# modificar_permisos(, 30, 37, 'ir_default all', True, False, False, False
# modificar_permisos(, 61, 22, 'ir_property group_user', False, False, False, False
# modificar_permisos(, 69, 101, 'access_report_layout', True, True, True, True
# modificar_permisos(, 70, 99, 'ir_actions_report_paperformat group_portal', True, False, False, False
# modificar_permisos(, 72, 42, 'res_country group_user_all', True, False, False, False
# modificar_permisos(, 73, 44, 'res_country_group group_user_all', True, False, False, False
# modificar_permisos(, 74, 43, 'res_country_state group_user_all', True, False, False, False
# modificar_permisos(, 75, 55, 'res_lang group_all', True, False, False, False
# modificar_permisos(, 78, 68, 'res_partner_title group_user', True, False, False, False
# modificar_permisos(, 79, 3020, 'res.partner custom access', True, True, True, False
# modificar_permisos(, 86, 49, 'res_currency group_all', True, False, False, False
# modificar_permisos(, 87, 50, 'res_currency_rate group_all', True, False, False, False
# modificar_permisos(, 88, 41, 'res_company group_user', True, False, False, False
# modificar_permisos(, 90, 71, 'res_users_log_all', True, False, True, False
# modificar_permisos(, 131, 140, 'access_web_editor_converter_test', True, True, True, True
# modificar_permisos(, 132, 141, 'access_web_editor_converter_test_sub', True, True, True, True
# modificar_permisos(, 133, 143, 'access_web_tour_tour', True, False, False, False
# modificar_permisos(, 134, 145, 'res_city group_user_all', True, False, False, False
# modificar_permisos(, 140, 154, 'bus.bus public', False, False, False, False
# modificar_permisos(, 149, 173, 'access_utm_medium', True, False, True, False
# modificar_permisos(, 150, 172, 'access_utm_campaign', True, False, True, False
# modificar_permisos(, 151, 174, 'access_utm_source', True, False, True, False
# modificar_permisos(, 155, 201, 'mail.message.subtype.all', True, False, False, False
# modificar_permisos(, 156, 203, 'mail.tracking.value.all', False, False, False, False
# modificar_permisos(, 157, 198, 'mail.alias.all', True, False, False, False
# modificar_permisos(, 159, 186, 'mail.followers.all', False, False, False, False
# modificar_permisos(, 162, 179, 'mail.message.all', True, False, False, False
# modificar_permisos(, 163, 2737, 'mail.activity.type.all', False, False, False, False
# modificar_permisos(, 164, 212, 'mail.activity.all', False, False, False, False
# modificar_permisos(, 166, 182, 'mail.mail.all', False, False, False, False
# modificar_permisos(, 173, 192, 'mail.group.all', True, False, False, False
# modificar_permisos(, 182, 207, 'publisher.warranty.contract.all', True, True, True, True
# modificar_permisos(, 355, 265, 'gamification.karma.rank.access.all', True, False, False, False
# modificar_permisos(, 356, 267, 'gamification.karma.tracking.access.all', False, False, False, False
# modificar_permisos(, 364, 685, 'hr.job.public', True, False, False, False
# modificar_permisos(, 370, 286, 'access.phone.blacklist.all', False, False, False, False
# modificar_permisos(, 399, 341, 'res.partner.autocomplete.sync.all', True, False, False, False
# modificar_permisos(, 407, 348, 'access.sms.sms.all', False, False, False, False
# modificar_permisos(, 408, 350, 'access.sms.template.all', False, False, False, False
# modificar_permisos(, 419, 363, 'survey.survey.all', False, False, False, False
# modificar_permisos(, 420, 367, 'survey.question.all', False, False, False, False
# modificar_permisos(, 421, 371, 'survey.question.answer.all', False, False, False, False
# modificar_permisos(, 422, 375, 'survey.user_input.all', False, False, False, False
# modificar_permisos(, 423, 379, 'survey.user_input.line.all', False, False, False, False
# modificar_permisos(, 471, 409, 'account.incoterms all', True, False, False, False
# modificar_permisos(, 493, 527, 'hr.recruitment.source', True, False, False, False
# modificar_permisos(, 497, 528, 'hr.applicant_category', True, True, True, False
# modificar_permisos(, 546, 624, 'access_seo_public', True, False, False, False
# modificar_permisos(, 551, 614, 'website.public', True, False, False, False
# modificar_permisos(, 552, 616, 'access_website_menu', True, False, False, False
# modificar_permisos(, 553, 620, 'access_website_page', False, False, False, False
# modificar_permisos(, 555, 618, 'access_website_rewrite', False, False, False, False
# modificar_permisos(, 563, 636, 'access_website_dynamic_filter', False, False, False, False
# modificar_permisos(, 565, 638, 'account.edi.format', True, False, False, False
# modificar_permisos(, 566, 640, 'account.edi.document', True, False, False, False
# modificar_permisos(, 570, 658, 'payment.acquirer.all', True, False, False, False
# modificar_permisos(, 571, 667, 'payment.icon.all', True, False, False, False
# modificar_permisos(, 572, 660, 'payment.transaction.all', True, False, False, False
# modificar_permisos(, 573, 663, 'payment.token.all', True, False, False, False
# modificar_permisos(, 581, 683, 'latam id type all', True, False, False, False
# modificar_permisos(, 679, 948, 'sale.order.option', True, False, False, False
# modificar_permisos(, 714, 1014, 'crm.stage', True, False, False, False
# modificar_permisos(, 877, 2932, 'access_hr_overtime_type_manager_payslip', True, True, True, True
# modificar_permisos(, 927, 1187, 'project.project_tags_all', True, False, False, False
# modificar_permisos(, 1027, 1267, 'access_hr_employee_job_log', True, True, True, True
# modificar_permisos(, 1028, 1269, 'access_hr_vacation_diferential', True, True, True, True
# modificar_permisos(, 1029, 1265, 'hr_payslip_concept_report_user', True, True, True, True
# modificar_permisos(, 1030, 1268, 'access_process_hr_payslip', True, True, True, True
# modificar_permisos(, 1158, 2608, 'Access to Crossovered Budget Lines', True, True, True, True
# modificar_permisos(, 1159, 1373, 'account_fiscalyear_close_account', True, True, True, True
# modificar_permisos(, 1175, 1389, 'access_account_tax_group_type_user', True, False, False, False
# modificar_permisos(, 1179, 1396, 'uom_code_users', True, False, False, False
# modificar_permisos(, 1182, 1402, 'account_payment_mean_users', True, False, False, False
# modificar_permisos(, 1183, 1404, 'account_payment_mean_code_users', True, False, False, False
# modificar_permisos(, 1184, 1406, 'account.move.discrepancy.response.code.users', True, False, False, False
# modificar_permisos(, 1185, 1408, 'product.brand.public', True, False, False, False
# modificar_permisos(, 1186, 1417, 'product_scheme_user', True, False, False, False
# modificar_permisos(, 1187, 1410, 'account_fiscal_position_party_tax_scheme_users', True, False, False, False
# modificar_permisos(, 1188, 1412, 'account_fiscal_position_tax_level_code_users', True, False, False, False
# modificar_permisos(, 1189, 1415, 'account_move_summary_line_user', True, True, True, False
# modificar_permisos(, 1190, 1413, 'account_move_dian_document_line_user', True, True, True, False
# modificar_permisos(, 1191, 1414, 'account_move_dian_document_user', True, True, True, False
# modificar_permisos(, 1192, 1416, 'einvoice_notification_group_user', True, True, True, True
# modificar_permisos(, 1194, 1418, 'load_data_einvoice', True, True, True, True
# modificar_permisos(, 1195, 1419, 'process_dian_document', True, True, True, True
# modificar_permisos(, 1225, 1420, 'access_hr_update_book_vacation', True, True, True, True
# modificar_permisos(, 1226, 1421, 'access_update_concept_account', True, True, True, True
# modificar_permisos(, 1240, 1473, 'access_prefacturacion_wiz', True, True, True, False
# modificar_permisos(, 1242, 1472, 'access_cierre_nomina_wiz', True, True, True, True
# modificar_permisos(, 1246, 1471, 'hr_roster_avancys.replicar_programacion_wiz', True, True, True, True
# modificar_permisos(, 1286, 2936, 'access_payslip_analytic_distribution', True, True, True, True
# modificar_permisos(, 1287, 2933, 'access_hr_roster_close_distribution', True, True, True, True
# modificar_permisos(, 1326, 1516, 'hr_employee_epayroll_subtype_user', True, True, True, False
# modificar_permisos(, 1327, 1517, 'hr_employee_epayroll_type_user', True, True, True, False
# modificar_permisos(, 1328, 1518, 'hr_payslip_concept_epayroll_type_code_user', True, True, True, False
# modificar_permisos(, 1329, 1519, 'hr_payslip_concept_epayroll_type_user', True, True, True, False
# modificar_permisos(, 1330, 1520, 'hr_payslip_dian_document_user', True, True, True, False
# modificar_permisos(, 1331, 1521, 'hr_payslip_dian_document_line_user', True, True, True, False
# modificar_permisos(, 1332, 1515, 'create_hr_payslip_dian_document_user', True, True, True, False
# modificar_permisos(, 1334, 1522, 'process_hr_dian_document', True, True, True, True
# modificar_permisos(, 1364, 1580, 'google.drive.config', True, False, False, False
# modificar_permisos(, 1526, 1718, 'audit_cause_clasification_user', True, True, True, False
# modificar_permisos(, 1576, 1785, 'access_hr_employee_accreditation', True, True, True, True
# modificar_permisos(, 1577, 1786, 'access_hr_employee_accreditation_line', True, True, True, True
# modificar_permisos(, 1578, 1787, 'access_hr_employee_credentials', True, True, True, True
# modificar_permisos(, 1579, 1788, 'access_hr_employee_credentials_line', True, True, True, True
# modificar_permisos(, 1586, 1808, 'access_certificado_report_ingresos', True, True, True, True
# modificar_permisos(, 1587, 1809, 'access_certificado_report_ingresos_line', True, True, True, True
# modificar_permisos(, 1588, 1813, 'access_certificado_ingresos', True, True, True, True
# modificar_permisos(, 1589, 1812, 'access_certificado_ingresos_line', True, True, True, True
# modificar_permisos(, 1590, 1810, 'access_certificado_ingresos_line_item', True, True, True, True
# modificar_permisos(, 1591, 1811, 'access_wizard_certificado_ingresos', True, True, True, True
# modificar_permisos(, 1603, 1815, 'access_hr_payroll_embargo', True, True, True, True
# modificar_permisos(, 1604, 1816, 'access_hr_payroll_embargo_line_extra', True, True, True, True
# modificar_permisos(, 1605, 1817, 'access_hr_payroll_embargo_extra', True, True, True, True
# modificar_permisos(, 1606, 1818, 'access_hr_payroll_embargo_history', True, True, True, True
# modificar_permisos(, 1607, 1819, 'access_hr_payroll_embargo_line', True, True, True, True
# modificar_permisos(, 1608, 1820, 'access_hr_payroll_embargo_category', True, True, True, True
# modificar_permisos(, 1609, 1821, 'access_hr_payroll_embargo_type', True, True, True, True
# modificar_permisos(, 1610, 1822, 'access_hr_payroll_embargo_priority', True, True, True, True
# modificar_permisos(, 1611, 1823, 'access_hr_payroll_embargo_priority_line', True, True, True, True
# modificar_permisos(, 1612, 1814, 'access_hr_payroll_embargo_history_wizard', True, True, True, True
# modificar_permisos(, 1613, 1824, 'access_hr_payslip_embargo_line', True, True, True, True
# modificar_permisos(, 1614, 1825, 'access_hr_payroll_embargo_file_wizard', True, True, True, True
# modificar_permisos(, 1690, 2023, 'board.board', True, False, False, False
# modificar_permisos(, 1856, 2363, 'access_template_report_contract', True, True, True, True
# modificar_permisos(, 2035, 2607, 'Access to Budget Wizard Report', True, True, True, True
# modificar_permisos(, 2036, 2606, 'Access to Budget Line Report', True, True, True, True
# modificar_permisos(, 2047, 2610, 'access_hr_wizard_massive_retired', True, True, True, True
# modificar_permisos(, 2060, 2611, 'access_hr_court_embargoes', True, True, True, True
# modificar_permisos(, 2061, 2612, 'access_hr_court_embargoes_code', True, True, True, True
# modificar_permisos(, 2062, 2613, 'access_hr_court_embargoes_destination', True, True, True, True
# modificar_permisos(, 2156, 2916, 'access_validate_service_order', True, True, True, True
# modificar_permisos(, 2157, 2917, 'access_validate_service_order_line', True, True, True, True
# modificar_permisos(, 2168, 2632, 'stock.report.kardex.line', True, True, True, True
# modificar_permisos(, 2169, 2633, 'access_stock_report_kardex_wizard', True, True, True, True
# modificar_permisos(, 2187, 2652, 'access_hr_eps_code', True, True, True, True
# modificar_permisos(, 2668, 2815, 'access_wizard_novelty_advance', True, True, True, True
# modificar_permisos(, 2685, 2894, 'access_compute_hr_payslip', True, True, True, True
# modificar_permisos(, 2686, 2895, 'access_draft_hr_payslip', True, True, True, True
# modificar_permisos(, 2729, 2930, 'access_hr_contract_hour_limit', True, True, True, True
# modificar_permisos(, 2730, 2931, 'access_hr_overtime_categ_config', True, True, True, True
# modificar_permisos(, 2733, 2937, 'hr_roster_avancys.hr_roster_puesto_cargo', True, True, True, True
# modificar_permisos(, 2749, 2946, 'access_contract_hours_job', True, True, True, True
# modificar_permisos(, 2750, 2947, 'access_hr_contract_job_do', True, True, True, True
# modificar_permisos(, 2760, 2948, 'hr_roster_avancys.hr_roster_scheduling_line', True, True, True, True
# modificar_permisos(, 2784, 2986, 'security.course.type', True, True, True, True
# modificar_permisos(, 2839, 3019, 'cursosvigilancia_vs_acreditacion', True, True, True, True
# modificar_permisos(, 2845, 3021, 'tipo.licitaciones access', True, True, True, True
# modificar_permisos(, 2846, 3022, 'access_hr_contract_zone', True, True, True, True
# modificar_permisos(, 2847, 3023, 'access_hr_contract_subzone', True, True, True, True
# modificar_permisos(, 2848, 3024, 'access_wizard_contract_prorroga', True, True, True, True
# modificar_permisos(, 2906, 3067, 'access_communication_quoter', True, True, True, True
# modificar_permisos(, 2954, 3102, 'hr_roster_avancys.hr_programation_leaves', True, True, True, True
# modificar_permisos(, 2994, 3180, 'access_examen_seguimiento', True, True, True, True
# modificar_permisos(, 3101, 3228, 'hr_roster_avancys.account_move_project_order_line', True, True, True, True
# modificar_permisos(, 3102, 3232, 'hr_roster_avancys.project_service_order_line_invoice', True, True, True, True
# modificar_permisos(, 3103, 3236, 'hr_roster_avancys.project_service_order_line_item_cancel', True, True, True, True
# modificar_permisos(, 3104, 3227, 'hr_roster_avancys.search_available_employee', True, True, True, True
# modificar_permisos(, 3105, 3229, 'hr_roster_avancys.prefacturacion_wiz_direct', True, True, True, True
# modificar_permisos(, 3106, 3230, 'hr_roster_avancys.report_uninvoiced_order_line', True, True, True, True
# modificar_permisos(, 3107, 3231, 'hr_roster_avancys.report_uninvoiced_order_line_wizard', True, True, True, True
# modificar_permisos(, 3108, 3234, 'hr_roster_avancys.add_from_invoice_items', True, True, True, True
# modificar_permisos(, 3109, 3233, 'hr_roster_avancys.add_invoice_items', True, True, True, True
# modificar_permisos(, 3110, 3235, 'hr_roster_avancys.compute_invoice_items', True, True, True, True
# modificar_permisos(, 3111, 3237, 'wizard.service.order.line', True, True, True, True
# modificar_permisos(, 3212, 3290, 'access_programacion_summary_hours', True, True, True, True



# Lista de permisos a crear
permisos_a_crear = [
    {
        'group_id': 286,
        'model_id': 439,
        'permiso_name': 'account.tax',
        'permiso_read': True,
        'permiso_write': True,
        'permiso_create': True,
        'permiso_unlink': False
    },
{
        'group_id': 288,
        'model_id': 439,
        'permiso_name': 'account.tax',
        'permiso_read': True,
        'permiso_write': True,
        'permiso_create': True,
        'permiso_unlink': False
    },
{
        'group_id': 285,
        'model_id': 439,
        'permiso_name': 'account.tax',
        'permiso_read': True,
        'permiso_write': True,
        'permiso_create': True,
        'permiso_unlink': False
    },
{
        'group_id': 292,
        'model_id': 439,
        'permiso_name': 'account.tax',
        'permiso_read': True,
        'permiso_write': True,
        'permiso_create': True,
        'permiso_unlink': False
    },
{
        'group_id': 289,
        'model_id': 439,
        'permiso_name': 'account.tax',
        'permiso_read': True,
        'permiso_write': True,
        'permiso_create': True,
        'permiso_unlink': False
    },
{
        'group_id': 287,
        'model_id': 439,
        'permiso_name': 'account.tax',
        'permiso_read': True,
        'permiso_write': True,
        'permiso_create': True,
        'permiso_unlink': False
    },
{
        'group_id': 284,
        'model_id': 439,
        'permiso_name': 'account.tax',
        'permiso_read': True,
        'permiso_write': True,
        'permiso_create': True,
        'permiso_unlink': False
    },
{
        'group_id': 290,
        'model_id': 439,
        'permiso_name': 'account.tax',
        'permiso_read': True,
        'permiso_write': True,
        'permiso_create': True,
        'permiso_unlink': False
    },
{
        'group_id': 291,
        'model_id': 439,
        'permiso_name': 'account.tax',
        'permiso_read': True,
        'permiso_write': True,
        'permiso_create': True,
        'permiso_unlink': False
    },

]

# Crear todos los permisos en la lista
for permiso in permisos_a_crear:
    access_id = crear_permisos(
        group_id=permiso['group_id'],
        model_id=permiso['model_id'],
        permiso_name=permiso['permiso_name'],
        permiso_read=permiso['permiso_read'],
        permiso_write=permiso['permiso_write'],
        permiso_create=permiso['permiso_create'],
        permiso_unlink=permiso['permiso_unlink']
    )
    print(f"Permiso creado con ID: {access_id}")


# IDs de ir.model.access que quieres eliminar
#ids_a_eliminar = [3327, 3328, 3329]

# Grupo y modelo a los que pertenecen esos accesos
#group_id = 288        # ejemplo
#model_id = 2182       # ejemplo (ir.model.id del modelo objetivo)

# Ejecutar eliminación uno por uno (reutilizando tu función)
#for access_id in ids_a_eliminar:
#    try:
#        eliminar_permisos(group_id, model_id, access_id)
#    except Exception as e:
#        print(f"⚠️ Error eliminando ID {access_id}: {e}")
