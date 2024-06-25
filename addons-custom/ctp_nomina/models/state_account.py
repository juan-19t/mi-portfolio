# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class StateAccount(models.Model):
    _name = 'state.account'
    _description = 'State Account'
    _rec_name = 'state'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    

    country = fields.Many2one('res.country',string="Country" ,default=lambda self: self.env.ref('base.us').id, required=True,tracking=True)
    state = fields.Many2one('res.country.state',string="State" ,required=True, domain="[('country_id', '=', country)]",tracking=True)
    account = fields.Many2one('account.account',string="Account",required=True,tracking=True,company_dependent=True)
    status = fields.Boolean(string='Status',default=True,tracking=True)

    _sql_constraints = [('unique_country_state', 'unique(country, state)', 'The combination of country and state must be unique.')]



