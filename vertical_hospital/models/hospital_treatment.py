from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class HospitalTreatment(models.Model):
    _name = 'hospital.treatment'
    _description = 'Hospital Treatment'

    #fields Char
    code = fields.Char(string='Código de tratamiento', required=True)
    name = fields.Char(string='Nombre del tratamiento', required=True)
    doctor = fields.Char(string='Medico tratante')

    @api.constrains('code')
    def _check_code(self):
        for record in self:
            if '026' in record.code:
                raise ValidationError(_('El código no puede contener la secuencia "026".'))