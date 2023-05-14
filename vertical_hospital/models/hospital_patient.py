from odoo import models, fields, api

class HospitalPatientState(models.Model):
    _name = 'hospital.patient.state'
    _description = 'Estado del paciente'

    name = fields.Char(string='Nombre', required=True, translate=True)

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # para habilitar el chatter

    # Fields Char
    name = fields.Char(string='Number', required=True, copy=False, default=lambda self: self.env['ir.sequence'].next_by_code('hospital.patient.sequence'))
    full_name = fields.Char(string='Full Name', required=True)
    
    dni = fields.Char(string='DNI', required=True, track_visibility="always")
    # Fields Datetime
    registration_date = fields.Datetime(string='Fecha de Alta', readonly=True, default=fields.Datetime.now)
    update_date = fields.Datetime(string='Fecha de Actualización', readonly=True, default=fields.Datetime.now)
    # Fields Selection
  
    # Fields Many2many
    treatment_ids = fields.Many2many('hospital.treatment', string='Tratamientos')

    state_id = fields.Many2one('hospital.patient.state', string='Estado',  default=lambda self: self.env.ref('vertical_hospital.state_draft').id)

  

    
    






