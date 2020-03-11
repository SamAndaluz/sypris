# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request


class OnboardingController(http.Controller):

    @http.route('/openeducat_core_enterprise/'
                'openeducat_core_enterprise_onboarding_panel',
                auth='user', type='json')
    def openeducat_core_enterprise_onboarding_panel(self):
        """ Returns the `banner` for the sale onboarding panel.
            It can be empty if the user has closed it or if he doesn't have
            the permission to see it. """

        company = request.env.user.company_id
        if not request.env.user._is_admin() or \
           company.openeducat_core_onboard_panel == 'closed':
            return {}
        return {
            'html': request.env.ref(
                'openeducat_core_enterprise.'
                'openeducat_core_enterprise_onboarding_panel').render({
                    'company': company,
                    'state': company.update_core_onboarding_state()
                })

        }
