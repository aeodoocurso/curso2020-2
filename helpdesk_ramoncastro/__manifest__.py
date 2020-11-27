

{
    "name": "Helpdesk Ramón Castro",
    "summary": "Helpdesk and ticket",
    "version": "13.0.1.0.0",
    "author": "Ramón Castro, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        "security/helpdesk_ticket_security.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_ticket_views.xml",
    ],
    
}