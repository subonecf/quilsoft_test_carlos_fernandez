# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request, route
import requests

class HospitalPatientAPI(http.Controller):
   
    @http.route(['/pacientes/consulta/<string:seq>'], type='http', auth='public', methods=['GET'], csrf=False)
    def get_patient(self, seq, **kwargs):
        patient = request.env['hospital.patient'].sudo().search([('name', '=', seq)], limit=1)
        if patient:
            data = json.dumps(patient.read(fields=['name', 'full_name', 'dni', 'state_id'])[0])
            return request.make_response(data,headers=[('Content-Type', 'application/json')])
        
            # no me quedo claro que hacer con el endpoint que se va a configurar en los ajuste.
            # supuse que era una url donde se enviaria el formato json


            # hospital_webservice_endpoint = request.env['ir.config_parameter'].sudo().get_param('vertical_hospital.enable_hospital_webservice_endpoint')
            # if hospital_webservice_endpoint:
            #     response = requests.request("POST", hospital_webservice_endpoint, headers={'Content-Type', 'application/json'}, json=data)


        else:
            patient_data = {'Paciente no encontrado en el sistema'}
            return request.make_response((patient_data),
                                            headers=[('Content-Type', 'application/json')])
