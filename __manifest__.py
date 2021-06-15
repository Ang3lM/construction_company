# -*- coding: utf-8 -*-
{
    'name': "construction_company",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','portal','website','om_account_accountant'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu_top.xml',
        'views/client.xml',
        'views/home.xml',
        'views/assign_materials.xml',
        'views/templates/client_templates.xml',
        'views/templates/client_tree_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}