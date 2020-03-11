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
    'name': 'OpenEduCat Skills Enterprise',
    'version': '13.0',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Skills Management',
    'complexity': "easy",
    'description': """
        This module provide skills of students.
    """,
    'author': 'Tech Receptives',
    'website': 'http://www.openeducat.org',
    'depends': ['base',
                'openeducat_core_enterprise',
                'openeducat_job_enterprise'],
    'demo': ['demo/skill_category_demo.xml',
             'demo/skilll_demo.xml',
             'demo/skill_line_demo.xml',
             'demo/job_post_demo.xml'],
    'data': ['security/ir.model.access.csv',
             'views/skill_category_view.xml',
             'views/skill_view.xml',
             'views/student_view.xml',
             'views/job_post_view_inherit.xml',
             'views/openeducat_student_skill_portal.xml',
             'views/openeducat_add_skill_portal.xml',
             'menus/op_menu.xml',
             ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 100,
    'currency': 'EUR',
    'license': 'OPL-1',
    'live_test_url': 'https://www.openeducat.org/plans'
}
