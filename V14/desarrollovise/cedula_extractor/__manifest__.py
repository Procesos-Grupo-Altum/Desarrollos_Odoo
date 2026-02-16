{
    'name': 'Extractor de Cédulas Colombianas',
    'version': '14.0.1.0',
    'summary': 'Extrae datos de cédulas colombianas usando Gemini AI',
    'author': 'VISE - jarodriguez',
    'category': 'Tools',
    'depends': ['base', 'transcriptores_gemini'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        #'data/ir_config_parameter.xml',
        'views/cedula_extractor_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}