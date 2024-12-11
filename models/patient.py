from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'patient_id'

    name = fields.Char(string='Patient Name', required=True, tracking=True)
    patient_id = fields.Char(string='Patient ID', )
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], required=True, tracking=True)
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    date_of_birth = fields.Date(string='Date of Birth', required=True)
    blood_group = fields.Selection([
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
    ], string='Blood Group')
    
    # Relations
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string='Appointments')
    prescription_ids = fields.One2many('hospital.prescription', 'patient_id', string='Prescriptions')
    doctor_ids = fields.Many2many('hospital.doctor', string='Consulting Doctors')
    primary_doctor_id = fields.Many2one('hospital.doctor', string='Primary Doctor')
    
    # Status and other fields
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], default='draft', string='Status', tracking=True)
    active = fields.Boolean(default=True)
    note = fields.Text(string='Internal Notes')
    _sql_constraints = [
        ('patient_id_unique','UNIQUE (patient_id)', 'The patient_id must be unique.'), 
    ]

    # @api.model_create_multi
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         vals['patient_id'] = self.env['ir.sequence'].next_by_code('hospital.patient')
    #     return super(HospitalPatient, self).create(vals_list)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                today = date.today()
                record.age = today.year - record.date_of_birth.year - (
                    (today.month, today.day) < (record.date_of_birth.month, record.date_of_birth.day)
                )
            else:
                record.age = 0

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for record in self:
            if record.date_of_birth > fields.Date.today():
                raise ValidationError("Date of Birth cannot be in the future!")

    def action_confirm(self):
        self.state = 'confirmed'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancelled'

    def action_draft(self):
        self.state = 'draft'