from odoo import models, fields


class HelpdeskTicketState(models.Model):
    _name = 'helpdesk.ticket.state'
    _description = 'Helpdesk State'

    name = fields.Char()