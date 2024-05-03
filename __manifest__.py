{
    'name': 'Real Estate X',
    'summary': """
        This module helps to tenants can register complaints from website 
    """,
    'description': """
        This module helps to tenants can register complaints about (question, electrical issue, heating issue,
            etc) for their rented flats. 
    """,
    'license': 'OPL-1',
    'category': 'sale',
    'sequence': '10',
    'version': '17.0',
    'depends': ['base', 'website', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/website_data.xml',
        'data/ir_sequence_data.xml',
        'data/mail_template_data.xml',
        'wizards/question_complaint_answer.xml',
        'wizards/drop_complaint.xml',
        'views/tenants_complaints_view.xml',
        'views/complaint_type_view.xml',
        'reports/ir_actions_report.xml',
        'reports/work_order_report_template.xml'
    ],
    'assets': {
        'web.assets_backend': [
        ],
    },
}
