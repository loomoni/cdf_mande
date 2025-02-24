# -*- coding: utf-8 -*-
{
    'name': "M and E",

    'description': """
        M and E solution to monitor site project
    """,

    'author': "Loomoni Morwo",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'project',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project', 'point_of_sale', 'report_xlsx'],

    # always loaded
    'data': [
        # 'security/security.xml',
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/configurations.xml',
        # 'views/outcomes.xml',
        # 'views/output.xml',
        # 'views/event_reporting.xml',
        # 'views/dashboard_action.xml',
        # 'views/projects_view.xml',
        # 'views/activities_views.xml',
        # 'views/success_story.xml',
        # 'reports/report.xml',
        # 'views/brand_remove.xml',
        # 'views/sp.xml',
        # 'views/national_strategy.xml',
        # 'reports/report_template.xml',
        # 'views/menu.xml',

    ],
    # only loaded in demonstration mode

    # 'demo': [
    #     'demo/demo.xml',
    # ],

    # 'qweb': ['static/src/xml/dashboard.xml'],

    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}