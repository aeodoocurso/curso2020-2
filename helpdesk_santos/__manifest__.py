# Copyright 2020 Santos
#   José Ramón Santos - josesantosinsua@gmail.com
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Helpdesk Santos",
    "summary": "Helpesk and tickets",
    'description': """
Helpdesk
=======
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.
You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    "version": "13.0.1.0.0",
    "category": "Helpdesk",
    "website": "https://github.com/OCA/helpdesk",
    "author": "AEODOO, Odoo Community Association (OCA)",
    "maintainers": ["santos-dev"],
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        'views/helpdesk_ticket_views.xml',
        'views/helpdesk_tag_views.xml',
        'views/helpdesk_action_views.xml',
        'data/helpdesk_data.xml',
    ],
    "demo": [
    ]
}
