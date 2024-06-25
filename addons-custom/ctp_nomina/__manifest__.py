# -*- coding: utf-8 -*-
{
    'name': "ctp_nomina",

    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'sequence': -100,
    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'license': "LGPL-3",
    'category': 'Accounting',
    'version': '0.1',
    

    # any module necessary for this one to work correctly
    'depends': ['base','mail','account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/banks_views.xml',
        'views/state_account_views.xml',
        'views/employee_types_views.xml',
        'views/pay_day_options_views.xml',
        'views/benefits_views.xml',
        'views/deductions_views.xml',
        'views/nomina_menu.xml',
        'views/payment_methods_views.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

