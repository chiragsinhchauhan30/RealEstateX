from odoo.tests import TransactionCase, tagged
from odoo import SUPERUSER_ID, Command


@tagged('-at_install', 'tenant', 'post_install')
class TestTenantComplaint(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_create_tenant_complaint(self):
        print("\n ====== TESTING TENANT COMPLAINT =======")

        # Create Partner Marc Demo
        partner_demo = self.env['res.partner'].create({
            'name': 'Marc Demo',
        })
        check_partner = self.env['res.partner'].search([('id', '=', partner_demo.id)])
        self.assertEqual(check_partner.id, check_partner.id)
        print("\n ====== Partner Created =======", check_partner)

        # Create User Demo2
        user2 = self.env['res.users'].create({
            'login': 'demo2',
            'password': 'demo2',
            'partner_id': partner_demo.id,
            'groups_id': [
                Command.set([self.env.ref('base.group_user').id])],
        })
        check_user = self.env['res.users'].search([('id', '=', user2.id)])
        self.assertEqual(check_user.id, check_user.id)
        print("\n ====== User Created =======", check_user)

        # Create Complaint Type
        complaint_type = self.env['complaint.type'].create({'name': 'TEST', 'user_id': user2.id})
        check_type = self.env['complaint.type'].search([('id', '=', complaint_type.id)])
        self.assertEqual(check_type.id, check_type.id)
        print("\n ====== Complaint TYPE Created =======", complaint_type)

        # Creating Tenant Complaint
        tenant_complaint = self.env['tenants.complaints'].with_context(force_true=False, mail_create_nolog=True).create(
            {
                'name': "TEST",
                'email': "test@gmail.com",
                'address': "TEST Address",
                'description': 'TEST Problem',
                'type': complaint_type.id,
            })
        check_complaint = self.env['tenants.complaints'].search([('id', '=', tenant_complaint.id)])
        self.assertEqual(check_complaint.id, check_complaint.id)
        print("\n ======Tenant Complaint Created =======", tenant_complaint)
