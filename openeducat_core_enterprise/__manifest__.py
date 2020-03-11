# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.
#
##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

{
    'name': 'OpenEduCat Core Enterprise',
    'version': '13.0',
    'category': 'Education',
    "sequence": 1,
    'summary': 'Manage Students, Faculties and Education Institute',
    'complexity': "easy",
    'description': """
        This module provide core education management system.
        Features includes managing
            * Student
            * Faculty
            * Course
            * Batch
    """,
    'author': 'Tech Receptives',
    'website': 'http://www.openeducat.org',
    'depends': [
        'gamification',
        'openeducat_core',
        'openeducat_web',
    ],
    'data': [
        'security/op_security.xml',
        'security/ir.model.access.csv',
        'wizard/op_grant_badge_wizard_view.xml',
        'views/batch_view.xml',
        'views/student_view.xml',
        'views/subject_view.xml',
        'views/student_badge_view.xml',
        'views/openeducat_personal_info_portal.xml',
        'views/openeducat_educational_info_portal.xml',
        'views/board_affiliation_view.xml',
        'views/onboard.xml',
        'views/openeducat_subject_registration_portal.xml',
        'views/assets.xml',
        'dashboard/openeducat_dashboard_view.xml',
        'menu/course_menu.xml'
    ],
    'demo': [
        'demo/student_badge_demo.xml',
        'demo/course_subject_demo.xml',
    ],
    'css': [],
    'qweb': [
        'static/src/xml/custom.xml'
    ],
    'js': [],
    'images': [
        'static/description/openeducat_core_enterprise_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 300,
    'currency': 'EUR',
    'license': 'OPL-1',
    'live_test_url': 'https://www.openeducat.org/plans'
}
