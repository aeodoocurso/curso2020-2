{
	"name" : "CRM Helpdesk",
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
	"depends" : [ "crm"],
	"data" : [
		'security/crm_helpdesk_security.xml',
		'security/ir.model.access.csv',
		'views/crm_helpdesk_ticket_views.xml',
	],
	"demo" : [
	]
}