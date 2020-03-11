# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, fields


class OpBatch(models.Model):
    _inherit = "op.batch"

    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.user.company_id)
    color = fields.Integer(string='Color Index', default=0)

    def action_onboarding_batch_layout(self):
        self.env.user.company_id.onboarding_batch_layout_state = 'done'
