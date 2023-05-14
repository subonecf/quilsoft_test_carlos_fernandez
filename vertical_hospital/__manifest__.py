{
    'name': 'Gestión de hospitales',
    'version': '1.0',
    'summary': 'Gestión de hospitales',
    'sequence': 10,
    'author': 'Carlos Fernández',
    'contribuitors': "Carlos Fernández <cfernandez.wx@gmail.com>",
    'category': 'Extra Tools',
    'depends': ['base', 'mail'],
    'data': [
        # security access model 
        'security/ir.model.access.csv',
        #data view
        'data/patient_for_request_api_rest.xml',
        'data/sequence_hospital_patient.xml',
        'data/state_date_hospital_patient.xml',
       
        #view models
        'views/hospital_patient_view.xml',
        'views/hospital_treatment_view.xml',
        'views/state_patient_view.xml',
        #view report
        'report/report_hospital_patient_pdf.xml',
        'views/action_report_server_hospital_patient_pdf.xml',
        #view menu
        'views/menuitem.xml',
    
        #inherit view models
        'views/res_config_setting_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/icon.png'], 
}