# -*- coding: utf-8 -*-
{
    "name": "Helpdesk",
    "summary": "Helpdesk Ticket Luis Miguel",
    "description": """
    Descripción larga del Helpdesk
    """,
    "version": "10.0.1.0.0",
    "category": "Helpdesk",
    "author": "Luis Miguel",
    "application": True,
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_tag_views.xml",
    ],
    "demo": [
    ]
}