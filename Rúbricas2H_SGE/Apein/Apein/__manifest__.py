# -*- coding: utf-8 -*-
{
    'name': "Apein",
    'summary': """Apein""",
    'description': """
        Module to manage component's supply
    """,
    'author': "Borja",
    'website': "http://www.salesianos.edu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Repaso',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views.xml',
    ],
}