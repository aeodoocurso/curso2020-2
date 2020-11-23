# Copyright 2020 MAREA ONLINE SL
#   César Sahagún
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Help Desk Cesar Sahagun",
    "summary": "HelpDesk Aeodoo",
    "version": "13.0.1.0.0",
    "development_status": "Alpha",
    "category": "Help Desk",
    "website": "https://github.com/OCA/helpdesk",
    "author": "Cesar Sahagún, Odoo Community Association (OCA)",
    "maintainers": ["cesaraeodoo"],
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
}
