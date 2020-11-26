from odoo import models, fields

class Helpdesk(models.Model):
    _name = 'helpdesk.ticket'
    _description = "Helpdesk ticket"

    name = fields.Char(
        string = 'Name')
    description = fields.Text(
        string = 'Description')
    date = fields.Date(
        string = 'Date')

    state = fields.Selection(
        [ ('new', 'New'),
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
        reSadonly=True)

    date_due = fields.Date(
        string='Date due')

    corrective_action = fields.Html(
        string='Corrective Action',
        help='Detail of corrective action')

    preventive_action = fields.Html(
        string='Preventive Action',
        help='Detail of preventive action')

