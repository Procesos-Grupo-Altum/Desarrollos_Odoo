#-*- coding:utf-8 -*-

{
    'name':'Modulo de Altum Forms',
    'version':'1.0',
    'depends':['base',
               'product_expiry',],
    'author':'Freddy Alexander Urrego',
    'category':'AltumForms',
    'website':'http://localhost:8071/web#action=84&model=user&view_type=list&cids=&menu_id=69',
    'description':'''
        Modulo de Pruebas para Altun Forms
    ''',
    'data':[
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/question_type_views.xml',
        'views/sector.xml',
        'views/source.xml',
        'data/question_type.csv',
        'data/source.csv',
        'data/sector.csv',



    ],

}