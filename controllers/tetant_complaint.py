# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.http import request
from odoo import http, SUPERUSER_ID, _, _lt
from odoo.exceptions import ValidationError


class TenantComplaint(http.Controller):
    @http.route('/website/complaint', methods=['POST'], auth="public",
                website=True, csrf=False)
    def tenant_complaint(self, **kw):
        ''' This controller save the data comes from the tenant register form \
        and redirect to thank you page '''
        try:
            values = {}
            thank_you_data = {}
            data = request.params
            values.update({'name': data.get('tenant_name'),
                           'email': data.get('email'),
                           'address': data.get('address'),
                           'type': data.get('type_id'),
                           'description': data.get('description')})
            record = (request.env['tenants.complaints']
                      .with_user(SUPERUSER_ID).with_context(
            ).create(values))
            thank_you_data.update({'number': record.complaint_number})
            return request.render('RealEstateX.complaint_thanks', thank_you_data)

        except Exception as error:
            raise ValidationError(error)

    @http.route('/tetant', type='http', auth="public", website=True)
    def tenant_complaint_data(self, **kwargs):
        ''' This controller Redirect to the tenant register web form with data '''
        data = {}
        complaint_type = request.env['complaint.type'].sudo().search([])
        data.update({'complaint_type_ids': complaint_type})
        return request.render("RealEstateX.tenant_complaint", data)
