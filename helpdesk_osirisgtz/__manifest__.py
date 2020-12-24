# Copyright 2020 AEODOO
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Helpdesk Osiris Gutierrez",
    "summary": "Helpdesk module created for the AEODOO course 2020-2",
    "description": """
    HELPDESK
    ===
    Detail description for the module developed in the __AEODOO course 2020-2__
    """,
    "version": "13.0.1.0.0",
    "category": "Helpdesk",
    "website": "https://github.com/OCA/helpdesk",
    "author": "AEODOO, Odoo Community Association (OCA)",
    "maintainers": ["osiris"],
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": ["base", ],
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_ticket_views.xml",
        "wizards/tickets_from_tag.xml",
        "views/helpdesk_tag_views.xml",
        "views/helpdesk_action_views.xml",
        "data/helpdesk_data.xml",
    ],
    "demo": [
    ]
}
