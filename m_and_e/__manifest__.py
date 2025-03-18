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
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/project.xml',
        'views/configurations.xml',
        'views/case_study.xml',
        # 'views/output.xml',
        'views/events_reporting.xml',
        'views/dashboard.xml',
        'views/output_dashboard.xml',
        'views/outcome_dashboard.xml',
        # 'views/projects_view.xml',
        'views/monitoring_visit.xml',
        'views/success_story.xml',
        # 'reports/report.xml',
        'views/brand_remove.xml',
        'views/sp.xml',
        'views/activities.xml',
        'views/menu.xml',


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