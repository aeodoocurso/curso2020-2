# Copyright 2020 Rafael Doña Martinez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Helpdesk Tickets Rafael Doña',
    'summary': 'Module to manage the helpdesk tickets',
    'category': 'Helpdesk',
    'version': '13.0.1.0.0',
    'author': 'Rafael Doña Martinez',
    'website': 'https://www.github.com/OCA/helpdesk',
    'maintainers': ["rafadm98"],
    'description': 'Helpdesk -- Module to manage the helpdesk tickets',
    'license': 'AGPL-3',
    'application': True,
    'installable': True,
    'depends': [
        'base',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/helpdesk_ticket_views.xml',
    ],
    'demo': [
    ],
}
