# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime





class EmployeeTypes(models.Model):
    _name = 'employee.types'
    _description = 'Employee Types'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    
    name = fields.Char(string='Name', required=True, size=50, unique=True,tracking=True)
    active = fields.Boolean(string='Active',default=True,tracking=True)

    _sql_constraints= [('name_unique','unique(name)','The type of employee already exists in the records')]