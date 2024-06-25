# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime




class Benefits(models.Model):
    _name = 'benefits'
    _description = 'Benefits'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Name', required=True, size=120, unique=True,tracking=True)
    active = fields.Boolean(string='Active',default=True,tracking=True)