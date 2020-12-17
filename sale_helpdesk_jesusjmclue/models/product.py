from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError
from datetime import timedelta

class ProductProduct(models.Model):
	_inherit = 'product.product'

	helpdesk_tag_id = fields.Many2one(
		comodel_name = 'helpdesk.ticket.tag',
		string = 'Helpdesk Tag')
	