# -*- coding: utf-8 -*-
{
    'name': 'MFH Herencia',
    'author': 'Marlon Falcón Hernández',
    'category': 'Sales',
    'description': """
Ejemplo de módulo
=====================================================
        """,
    'version': '10.0.0.1',
    'depends': ['base','mail','report','account'],
    'data': [
         'views/res_partner_view.xml',
         'views/account_account_view.xml'
            ],
    'demo': [],
    'auto_install': False,
    'installable': True,
}
