from odoo import api, fields, models


class HelpdeskTicketAction(models.Model):
    _name = 'helpdesk.ticket.action'
    _description = 'Helpdesk ticket action'

    name = fields.Char()
    date = fields.Date()
    ticket_id = fields.Many2one(comodel_name='helpdesk.ticket')


class HelpdeskTag(models.Model):
    _name = 'helpdesk.tag'
    _description = 'Helpdesk Tags'
    name = fields.Char()
    ticket_ids = fields.Many2many(comodel_name='helpdesk.ticket',
                                  relation='rel_helpdesk_ticket_tag',
                                  column1='tag_id',
                                  column2='ticket_id',
                                  string='Tickets')


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
    assigned = fields.Boolean(string='Assigned',
                              readonly=True,
                              compute='_compute_assigned',
                              store=True)
    date_due = fields.Date(string='Date Due')
    action_id = fields.One2many(comodel_name='helpdesk.ticket.action',
                                inverse_name='ticket_id',
                                string='Actions')
    corrective_action = fields.Html(
        help='Detail of corrective action after this issue')
    preventive_action = fields.Html(
        help='Detail of preventive action after this issue')
    user_id = fields.Many2one(comodel_name='res.users', string='Assigned to')
    tag_ids = fields.Many2many(comodel_name='helpdesk.tag',
                               relation='rel_helpdesk_ticket_tag',
                               column1='ticket_id',
                               column2='tag_id',
                               string='Tags')
    ticket_qty = fields.Integer(compute='_compute_tickets_qty')
    related_tag_ids = fields.Many2many(comodel_name='helpdesk.tag',
                                       string='Related tags',
                                       compute='_compute_related_tags')
    new_tag_name = fields.Char("New tag")
    color = fields.Char("Color")

    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            record.assigned = record.user_id and True

    @api.depends('user_id')
    def _compute_tickets_qty(self):
        for record in self:
            user = record.user_id
            other_tickets = self.env['helpdesk.ticket'].search([
                ('user_id', '=', user.id)
            ])
            record.ticket_qty = len(other_tickets)

    @api.depends('user_id')
    def _compute_related_tags(self):
        for record in self:
            user = record.user_id
            other_tickets = self.env['helpdesk.ticket'].search([
                ('user_id', '=', user.id)
            ])
            all_tags = other_tickets.mapped('tag_ids')
            self.related_tag_ids = all_tags

    def set_assigned(self):
        self.ensure_one()
        self.write({
            'assigned': True,
            'state': 'assigned',
            'user_id': self.env.uid
        })

    def create_new_tag(self):
        self.ensure_one()
        tag = self.env['helpdesk.tag'].create({
            'name': self.new_tag_name,
        })
        self.tag_ids = self.tag_ids + tag

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
