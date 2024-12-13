from odoo import models, fields, api

class inherit_hospital(models.Model):
    _inherit='hospital.appointment'
    
    place=fields.Char(string='مكان العيادة')
    # def action_confirm(self):
    #     rec=super(inherit_hospital, self).action_confirm()
    #     print('good inherit')
    #     return rec