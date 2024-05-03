# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models
from datetime import datetime


class TenantsComplaints(models.Model):
    _name = 'tenants.complaints'
    _description = "This Module is provide information about tenants complaints"
    _inherit = 'mail.thread'
    _order = 'complaint_number desc'

    AVAILABLE_PRIORITIES = [
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
        ('3', 'Very High'),
    ]

    name = fields.Char("Tenant Name", required=True)
    complaint_number = fields.Char("Complaint Number", readonly=True,
                                   default=lambda self: _('New'), copy=False)
    email = fields.Char("Email", required=True)
    address = fields.Char("Address", required=True)
    priority = fields.Selection(AVAILABLE_PRIORITIES, string='Priority',
                                default=AVAILABLE_PRIORITIES[0][0])
    type = fields.Many2one('complaint.type', "Type",
                           required=True)
    type_name = fields.Char(related='type.name', string="Type Name")
    user_id = fields.Many2one(related='type.user_id', string="Assigned To")
    description = fields.Char("Problem Description", required=True)
    action_plan = fields.Html("Action Plan")
    resolve_date = fields.Datetime("Resolve / Drop Date")
    resolve_reason = fields.Html("Resolve / Drop Reason")
    state = fields.Selection([
        ('new', 'New'),
        ('review', 'In Review'),
        ('progress', 'In Progress'),
        ('solved', 'Solved'),
        ('dropped', 'Dropped')], 'State', default='new', tracking=True)

    def action_set_to_draft(self):
        ''' Set State to new '''
        self.write({'state': 'new', 'resolve_date': "", "resolve_reason": ""})

    def action_action_plan(self):
        ''' Set State to In Progrss '''
        self.write({'state': 'progress'})

    def action_classify_complaint(self):
        ''' Set State to In Review '''
        self.write({'state': 'review'})

    def action_resolve_complaint(self):
        ''' Resolve the complaint and inform about the complaint '''
        self.write({'state': 'solved', 'resolve_date': datetime.now()})
        template_id = self.env.ref('RealEstateX.solved_tenant_complaint_email_template')
        email_values = {'action_plan': self.action_plan}
        (self.env['mail.template'].browse(template_id.id)
         .with_context(email_values).send_mail(self.id, force_send=True))

    def create(self, vals_list):
        ''' Create Complaint And Generate Sequence Number '''
        if not vals_list.get('complaint_number') or vals_list['complaint_number'] == _('New'):
            vals_list['complaint_number'] = (self.env['ir.sequence']
                                             .next_by_code('tenants.complaints') or _('New'))
        res = super().create(vals_list)
        template_id = self.env.ref('RealEstateX.new_tenant_complaint_request_email_template')
        (self.env['mail.template'].browse(template_id.id)
         .send_mail(res.id, force_send=False))
        return res