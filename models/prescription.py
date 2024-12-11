from odoo import models, fields, api


class HospitalPrescriptionLine(models.Model):
    _name = 'hospital.prescription.line'
    _description = 'Prescription Line'

    prescription_id = fields.Many2one('hospital.prescription', string='Prescription')
    medicine = fields.Char(string='Medicine')
    dosage = fields.Char(string='Dosage')
    quantity = fields.Integer(string='Quantity')
    instructions = fields.Text(string='Instructions')

class HospitalPrescription(models.Model):
    _name = 'hospital.prescription'
    _description = 'Hospital Prescription'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Reference', readonly=True, copy=False)
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    date = fields.Date(string='Date', default=fields.Date.context_today)
    
    prescription_line_ids = fields.One2many('hospital.prescription.line', 'prescription_id', string='Prescription Lines')
    notes = fields.Text(string='Notes')
    
    # @api.model_create_multi
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         vals['name'] = self.env['ir.sequence'].next_by_code('hospital.prescription')
    #     return super(HospitalPrescription, self).create(vals_list)

