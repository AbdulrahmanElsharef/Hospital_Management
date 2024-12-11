from odoo import models, fields, api

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Doctor Name', required=True)
    specialization = fields.Char(string='Specialization')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    
    patient_ids = fields.Many2many('hospital.patient', string='Patients')
    appointment_ids = fields.One2many('hospital.appointment', 'doctor_id', string='Appointments')
    
    active = fields.Boolean(default=True)
    # user_id = fields.Many2one('res.users', string='Related User')
    _sql_constraints = [('Phone_unique','UNIQUE (Phone)', 'The Phone must be unique.')
    ]