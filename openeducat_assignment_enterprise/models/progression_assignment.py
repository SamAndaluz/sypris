# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, fields, api


class StudentProgression(models.Model):
    _inherit = ["op.student.progression"]

    @api.depends("assignment_lines")
    def _calculate_total_assignment(self):
        self.total_assignment = len(self.assignment_lines)

    assignment_lines = fields.One2many('op.assignment.sub.line',
                                       'progression_id',
                                       string='Progression Assignment')
    total_assignment = fields.Integer('Total Assignment',
                                      compute="_calculate_total_assignment",
                                      store=True)
