from odoo import api, fields, models, _


class HelpdeskTicketAction(models.Model):
    _inherit = 'helpdesk.ticket'

    ticket_id = fields.Many2one(comodel_name='sale.order',
                                string='Sale order  ')
