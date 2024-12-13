from odoo import models, fields, api

class HospitalFemaleDoctor(models.Model):
    _name='hospital.female'
    _inherit='hospital.doctor'