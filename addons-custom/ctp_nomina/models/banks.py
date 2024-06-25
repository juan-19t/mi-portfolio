# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime



class Banks(models.Model):
    _name = 'banks'
    _description = 'Banks'
    _inherit =  ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, size=120,tracking=True)
    active = fields.Boolean(string='Active',default=True,tracking=True)

    _sql_constraints= [('name_unique','unique(name)','The bank name already exists in the records')]









