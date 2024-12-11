{
    'name': 'Hospital Management',
    'version': '17.0.1.0.0',
    'category': '',
    'summary': 'Complete Hospital Management System',
    'description': """
        Hospital Management System with complete Patient lifecycle:
        - Patient Registration
        - Appointment Management
        - Medical Records
        - Treatment Plans
        - Prescription Management
    """,
    'author': 'Abdulrahman Elsharef',
    'website': 'https://github.com/AbdulrahmanElsharef',
    'depends': ['base', 'mail'],
    # 'product'
    'data': [
        # 'security/hospital_security.xml',
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        'views/appointment_view.xml',
        'views/doctor_view.xml',
        'views/prescription_view.xml',
        'views/hospital_menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'hospital_management/static/src/css/hospital_style.css',
        ],
    },
    'application': True,
    'installable': True,
    'auto_install': False,
    'sequence': 1,
    'license': 'LGPL-3',
    'icon': '/hospital_management/static/description/icon.png',
}