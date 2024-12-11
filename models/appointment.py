from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'appointment_date'
    _rec_name="name"

    name = fields.Char(string='Appointment',required=True )
    # readonly=True, copy=False
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    appointment_date = fields.Datetime(string='Appointment Date', required=True)
    duration = fields.Float(string='Duration (Hours)', default=1.0)
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='Status', default='draft', tracking=True)
    
    prescription_ids = fields.One2many('hospital.prescription', 'appointment_id', string='Prescriptions')
    
    _sql_constraints = [
        ('name_unique','UNIQUE (name)', 'The name must be unique.'), 
    ]
    # treatment_plan_ids = fields.One2many('hospital.treatment.plan', 'appointment_id', string='Treatment Plans')
    
    # @api.model_create_multi
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
    #     return super(HospitalAppointment, self).create(vals_list)
    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        if self.patient_id:
            self.doctor_id = self.patient_id.primary_doctor_id

    @api.constrains('appointment_date')
    def _check_appointment_date(self):
        for record in self:
            if record.appointment_date  < fields.Datetime.now():
                raise ValidationError("Appointment date cannot be in the past!")
            
    def action_confirm(self):
        self.state = 'confirmed'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancelled'

    def action_draft(self):
        self.state = 'draft'