{
    'name': 'Extractor Universal de Diplomas',
    'version': '14.0.1.0',
    'summary': 'Extracción de datos académicos con Gemini 2.5 Flash',
    'author': 'VISE - jarodriguez',
    'category': 'Tools',
    'depends': ['base', 'transcriptores_gemini'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/diploma_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}