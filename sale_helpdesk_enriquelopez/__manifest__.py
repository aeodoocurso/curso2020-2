# Copyright 2020 Analistas Cooffee
#   Enrique López de Roda López - e.lrl@hotmail.com
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sale Helpdesk Enrique Lopez",
    "summary": "Sale Helpdesk and Tickets",
    "description":"""
Sale Helpdesk
=============
Módulo de prueba de Sale Helpdesk curso Aeodoo
    """,
    "version": "13.0.1.0.0",
    "category": "Helpdesk",
    "website": "https://github.com/OCA/Helpdesk",
    "author": "Analistas Cooffee, Odoo Community Association (OCA)",
    "maintainers": ["e-lrl"],
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": [
        "sale_management", "helpdesk_enriquelopez",
    ],
    "data": [
        "views/sale_views.xml",
        "views/product_views.xml",
        "views/helpdesk_ticket_views.xml",
    ],
    "demo": [],
}
