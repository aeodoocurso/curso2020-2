from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    date = fields.Date(string='Date')
    state = fields.Selection(selection=[
        ('new', 'New'),
        ('assigned', 'Assigned'),
        ('progress', 'Progress'),
        ('waiting', 'Waiting'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ],
                             string='State',
                             default='new')
    dedicated_time = fields.Float(string='Time')
    assigned = fields.Boolean(string='Assigned', readonly=True)
    date_due = fields.Date(string='Date Due')
    corrective_action = fields.Html(
        help='Detail of corrective action after this issue')
    preventive_action = fields.Html(
        help='Detail of preventive action after this issue')
    user_id = fields.Many2one(comodel_name='res.users', string='Assigned to')

    def set_assigned(self):
        self.ensure_one()
        self.write({
            'assigned': True,
            'state': 'assigned',
            'user_id': self.env.uid
        })

    def set_progress(self):
        self.ensure_one()
        self.state = 'progress'

    def set_waiting(self):
        self.ensure_one()
        self.state = 'waiting'

    def set_done(self):
        self.ensure_one()
        self.state = 'done'

    def set_cancel(self):
        self.ensure_one()
        self.state = 'cancel'
