from odoo import fields, models

class HelpdeskTicket (models.Model):
    _name = 'helpdesk.ticket'
    _description = 'HelpDesk Ticket'

    name = fields.Char(
        string='Name',
    )
    description = fields.Text(
        string='Description',
    )
    date = fields.Date(
        string='Date',
    )

