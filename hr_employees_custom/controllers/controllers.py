# -*- coding: utf-8 -*-
# from odoo import http


# class HrEmployeesCustom(http.Controller):
#     @http.route('/hr_employees_custom/hr_employees_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_employees_custom/hr_employees_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_employees_custom.listing', {
#             'root': '/hr_employees_custom/hr_employees_custom',
#             'objects': http.request.env['hr_employees_custom.hr_employees_custom'].search([]),
#         })

#     @http.route('/hr_employees_custom/hr_employees_custom/objects/<model("hr_employees_custom.hr_employees_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_employees_custom.object', {
#             'object': obj
#         })

