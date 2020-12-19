# Copyright 2020 Hergar
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "helpdesk.ticket",
    "summary": "Helpdesk Ticket",
    "version": "13.0.1.0.0",
    "category": "Helpdesk",
    "website": "https://github.com/OCA/helpdesk",
    "author": "Hergar, Odoo Community Association (OCA)",
    # see https://odoo-community.org/page/maintainer-role for a description of the maintainer role and responsibilities
    "maintainers": ["luismiguelarpon"],
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_ticket_views.xml",
    ],
    "demo": [
    ]
}
