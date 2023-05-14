from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    hospital_webservice_endpoint = fields.Char(string='Hospital Web Service Endpoint', config_parameter='vertical_hospital.enable_hospital_webservice_endpoint')


    
    
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        hospital_webservice_endpoint = self.env.ref('vertical_hospital.enable_hospital_webservice_endpoint', False)
        if hospital_webservice_endpoint:
            res.update(
                    hospital_webservice_endpoint=hospital_webservice_endpoint.hospital_webservice_endpoint,
             )
        return res

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        hospital_webservice_endpoint = self.env.ref('vertical_hospital.enable_hospital_webservice_endpoint', False)
        if hospital_webservice_endpoint:
            res.update(
                    hospital_webservice_endpoint=hospital_webservice_endpoint.hospital_webservice_endpoint,
             )
        return res

