# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class PaymentMethods(models.Model):
    _name = 'payment.methods'
    _description = 'Payment Methods'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    
    state = fields.Many2one('res.country.state',string="State" , domain="[('country_id', '=', 'United States')]",tracking=True,unique=True)
    weekly = fields.Boolean(string='(1)Weekly', tracking=True)
    bi_weekly = fields.Boolean(string='(2)Bi-Weekly', tracking=True)
    semi_monthly = fields.Boolean(string='(3)Semi-Monthly', tracking=True)
    monthly = fields.Boolean(string='(4)Monthly', tracking=True)
    comments = fields.Text(string="Comments", tracking=True)
    _sql_constraints= [('state_unique','unique(state)','The state you have selected is already in the list')]


    def action_view_comments(self):
        self.ensure_one()
        return {
            'name': 'Comments',
            'type': 'ir.actions.act_window',
            'res_model': 'payment.methods',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
        }