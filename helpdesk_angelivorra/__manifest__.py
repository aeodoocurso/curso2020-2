# Copyright 2020 Ticomsa
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Helpdesk Angel Ivorra",
    "summary": "Helpdesk and tickets",
    "version": "13.0.0.0.0",
    "category": "Uncategorized",
    "website": "https://github.com/OCA/heldesk",
    "author": "Ticomsa",
    "maintainers": ["aivorraticomsa"],
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        'security/security.xml',
        'security/ir.model.access.csv',
        'view/helpdesk_ticket_views.xml',
        'view/helpdesk_tag_views.xml',
    ],
    "demo": [

    ],
    "qweb": [

    ]
}