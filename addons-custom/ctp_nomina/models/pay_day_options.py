# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime



class PayDayOptions(models.Model):
    _name = 'pay.day.options'
    _description = 'Pay Day Options'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, size=50, unique=True,tracking=True)
    active = fields.Boolean(string='Active',default=True,tracking=True)

    _sql_constraints= [('name_unique','unique(name)','The pay day option already exists in the records')]
