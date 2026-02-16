# -*- coding:utf-8 -*-
{
    'name': 'Modulo de Peliculas',
    'version': '1.0',
    'depends': [
        'base',
        'contacts',
        'mail',
        'product',
        'purchase',
        'account',
        'sale_management',
        'crm',
        'account',
        'hr',
        'hr_recruitment',
        'fleet',
        'hr_contract',
        'website_hr_recruitment',
        'board',
        'note',
        'lunch',
        'hr_skills',
        'hr_holidays',
        'hr_attendance',
        'survey',
        'website_event',
        'mass_mailing',
        'website_sale',
        'website_slides',
        'im_livechat',
        'maintenance',
        'point_of_sale',
        'website_blog',
        'repair',
        'website_forum',











    ],
    'author': 'Alexander Giraldo Cardozo',
    'category': 'Peliculas',
    'website': 'www.google.com',
    'summary': 'Modulo de presupuestos para peliculas',
    'description': '''
    Modulo para hacer presupuestos de peliculas
    ''',
    'data': [
        'security/securyty.xml',
        'security/ir.model.access.csv',
        'data/secuencia.xml',
        'data/categoria.xml',
        'wizard/update_wizard_views.xml',
        'report/reporte_pelicula.xml',
        'views/presupuesto_views.xml',
        'views/menu.xml',
    ],
}
