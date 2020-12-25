# Copyright 2020 AEODOO
# Juanma Beltrán Osa - jmbo@wvbs.eu
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name":
    "Helpdesk Juanma Beltran",
    "summary":
    "Helpdesk and tickets",
    "version":
    "13.0.1.0.0",
    "category":
    "Helpdesk",
    "website":
    "https://github.com/OCA/helpdesk",
    "author":
    "AEODOO, Odoo Community Association (OCA)",
    """ see https://odoo-community.org/page/maintainer-role for a 
    description of the maintainer role and responsibilities """
    "maintainers": ["tyrantbit"],
    "license":
    "AGPL-3",
    "application":
    True,
    "installable":
    True,
    "depends": [
        "base",
    ],
    "data": [
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        'wizards/new_ticket_from_tag.xml',
        'views/helpdesk_ticket_views.xml',
        'views/helpdesk_tag_views.xml',
        'views/helpdesk_ticket_action_views.xml',
        'data/helpdesk_data.xml',
    ],
    "demo": []
}
