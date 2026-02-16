{
    'name': 'Certificado de Seguridad',
    'version': '14.0.1.0',
    'summary': 'Extrae datos de certificados de seguridad usando Gemini AI',
    'author': 'VISE - jarodriguez',
    'category': 'Tools',
    'depends': ['base', 'transcriptores_gemini'],
    'data': [
        'security/ir.model.access.csv',
        #'data/ir_config_parameter.xml',
        'views/certificado_seguridad_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}