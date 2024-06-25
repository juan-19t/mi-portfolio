# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class Deductions(models.Model):
    _name = 'deductions'
    _description = 'Deductions'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Name', required=True, size=120, unique=True,tracking=True)
    active = fields.Boolean(string='Active',default=True,tracking=True)