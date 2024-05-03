# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ComplaintsType(models.Model):
    _name = 'complaint.type'
    _description = "This Model provide about compliant types"

    name = fields.Char("Name", required=True)
    user_id = fields.Many2one('res.users', string="Service Representative",
                              required=True)
