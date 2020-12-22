{
	"name" : "Helpdesk",
	"summary" : "Helpdesk tickets",
	"description" : """
Helpdesk
========

Helpdesk module that enables the feature of creating support tickets.

	""",
    "version": "13.0.1.0.0",
    "development_status": "Alpha",
    "category": "Helpdesk",
    "author": "AEOdoo, Odoo Community Association (OCA)",
    "maintainers": ["jesusjmclue"],
    "license": "AGPL-3",
    "application": True,
    "installable": True,
	"depends" : [ "base", "mail"],
	"data" : [
		'security/helpdesk_security.xml',
		'security/ir.model.access.csv',
		'views/helpdesk_ticket_views.xml',
		'views/helpdesk_tag_views.xml',
		'views/helpdesk_action_views.xml',
		'report/helpdesk_ticket_templates.xml',
	],
	"demo" : [
		'data/helpdesk_demo.xml',
	]
}