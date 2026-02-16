# -*- coding:utf-8 -*-
{
    'name': 'Modulo Gestión Documentos',
    'version': '1.0',
    'category': 'Gestion Documentos',
    'summary': 'Modulo para la gestión de documentos',
    'description': """
        Módulo para la gestión de documentos en Odoo.
    """,
    'author': 'Freddy Alexander Urrego Beltran',
    'website': 'https://vise.avancyserp.com/web?db=dev-vise#id=1088&action=35&model=ir.module.module&view_type=form&cids=1&menu_id=5',
    'depends': ['base', 'mail', 'avancys'],
    'license': 'AGPL-3',
    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',

        'views_model/view_gestion_serie.xml',
        'views_model/view_gestion_subserie.xml',
        'views_model/views_gestion_iss.xml',
        'views_model/views_gestion_ccd.xml',
        'views_model/view_gestion_trd.xml',
        'views_model/views_relacion_trd.xml',

        'views_model/menu_gestion.xml',
        'views_model/templates.xml',

        'data/gestion.serie.csv',
        'data/gestion.subserie.csv',
        'data/gestion.dependencia.csv',
        'data/gestion.soporte.csv',
        'data/gestion.disposicion.final.csv',
        'data/gestion.iss.csv',
        'data/file.extension.csv',
        'data/gestion.trd.csv'

        ],
}