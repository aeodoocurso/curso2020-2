from odoo import models, fields


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = "Helpesk Ticket"

    name = fields.Char(
        string='Name',
        required=True)
    description = fields.Text(
        string='Description')
    date = fields.Date(
        string='Date')
    state = fields.Selection(
        [('new', 'New'),
         ('assigned', 'Assigned'),
         ('progress', 'Progress'),
         ('waiting', 'Waiting'),
         ('done', 'Done'),
         ('cancel', 'Cancel')],
        string='State',
        default='new')
    dedicated_time = fields.Float(
        string='Time')

    assigned = fields.Boolean(
        string='Assigned',
        readonly=False)

    date_due = fields.Date(
        string='Date Due')

    corrective_action = fields.Html(
        help='Detail of corrective action after this issue'
    )
    preventive_action = fields.Html(
        help='Detail of preventive action after this issue')
