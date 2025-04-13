# -*- coding: utf-8 -*-
{
    'name': "M_and_E",
    'author': "Loomoni Morwo",
    'version': '15.0.1.0.0',
    'description': 'Module for Monitoring and Evaluation.',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/project.xml',
        'views/configurations.xml',
        'views/case_study.xml',
        'views/events_reporting.xml',
        'views/dashboard.xml',
        'views/output_dashboard.xml',
        'views/outcome_dashboard.xml',
        'views/monitoring_visit.xml',
        'views/success_story.xml',
        'views/brand_remove.xml',
        'views/sp.xml',
        'views/activities.xml',
        'views/project_beneficiary_views.xml',
        'views/menu.xml',


    ],

    'installable': True,
    'application': True

}
