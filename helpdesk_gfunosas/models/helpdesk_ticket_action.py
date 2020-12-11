from odoo import models, fields


class HelpdeskTicketAction(models.Model):
    _name = 'helpdesk.ticket.action'
    _description= 'Helpdesk Action'

    name = fields.Char()
    date = fields.Date()
    ticket_id = fields.Many2one(
        'helpdesk.ticket'
    )