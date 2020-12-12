from odoo import models, fields


class HelpdeskTag(models.Model):
    _name = 'helpdesk.tag'
    _description = 'Helpdesk Tag'

    name = fields.Char()
    ticket_ids = fields.Many2many(
        'helpdesk.ticket',
        string ='Tickets',
        relation ='helpdesk_ticket_tag_rel',
        column1 ='tag_id',
        column2 ='ticket_id',
    )