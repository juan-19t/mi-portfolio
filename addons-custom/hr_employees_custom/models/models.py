# -*- coding: utf-8 -*-

from odoo import models, fields, api
from lxml import etree
from odoo.exceptions import ValidationError
from datetime import datetime


class HrEmployeesCustom(models.Model):
    _inherit = 'hr.employee'


    status = fields.Boolean(string='Status')
    departure_reason_id = fields.Many2one('hr.departure.reason',string='Departure reason')
    private_state_name = fields.Char(compute='_compute_private_state_name')
    #Personal information
    routing_number = fields.Char(string='Routing number', size=12)
    #Relacion con tabla de incapacidades medicas
    medical_incapacity_ids = fields.One2many('hr.employee.medical.incapacity', 'employee_id', string='Medical Incapacities')


    ###### FUNCION QUE VALIDA QUE ROUTING_NUMBER SEA NÚMERICO Y NO TENGA MÁS DE 12 DIGITOS#####
    @api.constrains('routing_number')
    def _check_routing_number(self):
        for employee in self:
            if not employee.routing_number.isdigit():
                raise ValidationError("The Routing Number must contain only numeric characters.")
            if len(employee.routing_number) > 12:
                raise ValidationError("The Routing Number must not exceed 12 digits.")
    ########################################################################     
     
      
     
       

    ############# PRIVATE MASK STARTS ################
    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(HrEmployeesCustom, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        if view_type == 'form':
            doc = etree.XML(res['arch'])
            for field_name in ['routing_number','bank_account_id', 'visa_no', 'permit_no', 'identification_id', 'ssnid','passport_id']:
                for node in doc.xpath(f"//field[@name='{field_name}']"):
                    node.set('widget', 'char_mask')
            res['arch'] = etree.tostring(doc, encoding='unicode')
        return res

    def _mask_char_field(self, value):
        if value:
            value_str = str(value)
            if len(value_str) > 4:
                return '*' * (len(value_str) - 4) + value_str[-4:]
        return value

    @api.model
    def fields_get(self, allfields=None, attributes=None):
        res = super(HrEmployeesCustom, self).fields_get(allfields, attributes)
        for field_name in ['routing_number','bank_account_id', 'visa_no', 'permit_no', 'identification_id', 'ssnid','passport_id']:
            if field_name in res:
                res[field_name]['mask'] = True
        return res

    def read(self, fields=None, load='_classic_read'):
        result = super(HrEmployeesCustom, self).read(fields=fields, load=load)
        for record in result:
            for field_name in ['routing_number','bank_account_id', 'visa_no', 'permit_no', 'identification_id', 'ssnid','passport_id']:
                if field_name in record and record[field_name]:
                    if isinstance(record[field_name], tuple) and len(record[field_name]) > 1:
                        record[field_name] = self._mask_char_field(record[field_name][1])
                    else:
                        record[field_name] = self._mask_char_field(record[field_name])
        return result
    
    ############# PRIVATE MASK ENDS ################



    
    ######## FUNCION PARA UN MEJOR MANEJO DE PRIVATE_STATE_ID EN VISTA LISTA#######
    @api.depends('private_state_id')
    def _compute_private_state_name(self):
        for employee in self:
            employee.private_state_name = employee.private_state_id.name if employee.private_state_id else 'Incomplete "State"'
    ###############################################################



    ######## SE SOOBREESCRIBEN FUNCIONES PARA VALIDAR QUE PRIVATE_STATE_ID ESTE COMPLETO ANTES DE GUARDAR#######
    @api.model
    def create(self, vals):
        if vals.get('status') and not vals.get('private_state_id'):
            raise ValidationError("The state where the employee lives has not been specified, please specify it.")
        return super(HrEmployeesCustom, self).create(vals)

    def write(self, vals):
        for employee in self:
            if ('status' in vals and vals.get('status')) or (employee.status and 'private_state_id' in vals and not vals.get('private_state_id')):
                if not (vals.get('private_state_id') or employee.private_state_id):
                    raise ValidationError("The state where the employee lives has not been specified, please specify it.")
        return super(HrEmployeesCustom, self).write(vals)
    
   #################################################################################


class MedicalReasons(models.Model):
    _name ='medical.reasons'
    _description = 'Medical Reasons'


    name = fields.Char(string='Name', required=True, size=120)
    active = fields.Boolean(string='Active',default=True)


class HrEmployeeMedicalIncapacity(models.Model):
    _name = 'hr.employee.medical.incapacity'
    _description = 'Medical Incapacity'
    _order = 'initial_date desc'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, ondelete='cascade')
    medical_reason_id = fields.Many2one('medical.reasons', string='Medical Reason', required=True)
    initial_date = fields.Date(string='Initial Date', required=True)
    final_date = fields.Date(string='Final Date', required=True)
    days = fields.Integer(string='Days', compute='_compute_days', store=True)

    @api.depends('initial_date', 'final_date')
    def _compute_days(self):
        for record in self:
            if record.initial_date and record.final_date:
                start_date = fields.Date.from_string(record.initial_date)
                end_date = fields.Date.from_string(record.final_date)
                record.days = (end_date - start_date).days + 1
            else:
                record.days = 0