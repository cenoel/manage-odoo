# -*- coding: utf-8 -*-
{
    'name': "Manage",
    'sequence': -10,
    'icon': '/manage/static/description/icon.png',
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
        'stock',
        'maintenance',
        'hr',
        'contacts',
        'project',
        'purchase',
        'hr_attendance'
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'data/res_config_setting_data.xml',
        'views/maintenance_equipment_views.xml',
        'views/product_template_views.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
