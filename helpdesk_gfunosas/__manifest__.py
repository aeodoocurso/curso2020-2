# -*- coding: utf-8 -*-
# Copyright 2020 Gerard Funosas
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "helpdesk_gfunosas",
    "summary": "Helpesk and tickets",
    "description": "Test odoo module for learnig purposes",
    "version": "13.0.1.0.0",
    "category": "Help Desk",
    "website": "https://github.com/OCA/helpdesk",
    "author": "AEODOO, Odoo Community Association (OCA)",
    "maintainers": ["gfunosas"],
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": ["base"],
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "data/helpdesk_data.xml",
        "wizards/new_ticket_from_tag.xml",
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_tag_views.xml",
        "views/helpdesk_actions_views.xml",
    ],
    "demo": [
    ],
}
