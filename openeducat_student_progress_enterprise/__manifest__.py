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
    'name': 'OpenEduCat Student Progress Enterprise',
    'version': '13.0',
    'category': 'Education',
    "sequence": 4,
    'summary': 'Manage Student progress',
    'complexity': "easy",
    'description': """
        This module provide feature of student progress.

    """,
    'author': 'Tech Receptives',
    'website': 'http://www.openeducat.org',
    'depends': [
        'openeducat_core_enterprise',

    ],
    'data': [
        'data/ir_sequence.xml',
        'security/ir.model.access.csv',
        'report/student_progression_report.xml',
        'report/report_menu.xml',
        'views/op_student_progress_portal.xml',
        'views/op_student_progress_data.xml',
        'menu/progress_menu.xml',
    ],
    'demo': ['demo/student_progression_demo.xml'],
    'css': [],
    'qweb': [],
    'js': [],
    'images': [

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 50,
    'currency': 'EUR',
    'license': 'OPL-1',
    'live_test_url': 'https://www.openeducat.org/plans'
}
