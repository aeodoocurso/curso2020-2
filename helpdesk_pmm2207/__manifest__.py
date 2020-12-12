# Copyright 2020 AEODOO
# Pablo Moreno - pmoreno@ticomsa.com
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Helpdesk Pablo Moreno",
    "summary": "Helpdesk and tickets",
    'description': """
Helpdesk and tickets
====================
This helpdesk system enables the creation of tickets for technical support 
    """,
    "version": "13.0.1.0.0",
    "category": "Helpdesk",
    "website": "https://github.com/OCA/helpdesk",
    "author": "AEODOO, Odoo Community Association (OCA)",
    # see https://odoo-community.org/page/maintainer-role for a description of the maintainer role and responsibilities
    "maintainers": ["pmm2207"],
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": [
        "base",
    ],

    "data": [
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        'views/helpdesk_ticket_views.xml'
    ],
    "demo": [

    ]
}