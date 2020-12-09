###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import api, fields, models


class HelpdeskTicketState(models.Model):
    _name = 'helpdesk.ticket.state'
    _description = 'Helpdesk Ticket State'

    name = fields.Char(
        string='Name',
    )


class HelpdeskTag(models.Model):
    _name = 'helpdesk.tag'
    _description = 'Helpdesk Tag'

    name = fields.Char(
        string='Name',
    )
    ticket_ids = fields.Many2many(
        comodel_name='helpdesk.ticket',
        relation='helpdesk_ticket_tag_rel',
        column1='tag_id',
        column2='ticket_id',
        string='Tickets',
    )


class HelpdeskTicketAction(models.Model):
    _name = 'helpdesk.ticket.action'
    _description = 'Helpdesk Action'

    name = fields.Char(
        string='Name',
    )
    date = fields.Date(
        string='Date',
    )
    ticket_id = fields.Many2one(
        comodel_name='helpdesk.ticket',
    )


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'

    name = fields.Char(
        string='Name',
        required=True,
    )
    description = fields.Text(
        string='Description',
    )
    date = fields.Date(
        string='Date',
    )
    state_id = fields.Many2one(
        comodel_name='helpdesk.ticket.state',
        string='State',
    )
    dedicated_time = fields.Float(
        string='Time dedicated',
    )
    assigned = fields.Boolean(
        string='Assigned',
        compute='_compute_assigned',
        store=True,
    )
    assigned_qty = fields.Integer(
        string='Assigned Quantity',
        ccompute='_compute_assigned_qty',
    )
    date_due = fields.Date(
        string='Date Due',
    )
    corrective_action = fields.Html(
        help='Detail of corrective action after this issue',
    )
    preventive_action = fields.Html(
        help='Detail of preventive action after this issue',
    )
    action_ids = fields.One2many(
        comodel_name='helpdesk.ticket.action',
        inverse_name='ticket_id',
        string='Actions',
    )
    tag_ids = fields.Many2many(
        comodel_name='helpdesk.tag',
        relation='helpdesk_ticket_tag_rel',
        column1='ticket_id',
        column2='tag_id',
        string='Tags',
    )
    related_tag_is = fields.Many2many(
        comodel_name='helpdesk.tag',
        compute='_compute_related_tag_ids',
        string='Related Tags',
    )
    new_tag_name = fields.Char(
        string='New Tag',
    )
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Assigned to',
    )

    def set_assigned(self):
        self.ensure_one()
        self.write({
            'assigned': True,
            'state': 'assigned',
            'user_id': self.env.user.id,
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

    def create_new_tag(self):
        self.ensure_one()
        tag = self.env['helpdesk.tag'].create({
            'name': self.new_tag_name,
        })
        self.tag_ids += tag

    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            if not record.user_id:
                record.assigned = False
            else:
                record.assigned = True

    @api.depends('user_id')
    def _compute_assigned_qty(self):
        for record in self:
            user = self.user_id
            quantity = self.env['helpdesk.ticket'].search([
                ('user_id', '=', user.id)
            ])
            record.assigned_qty = len(quantity)
            # quantity = self.env['helpdesk.ticket'].search_count(
            #     [('user_id', '=', user.id)]
            # )
            # record.assigned_qty = quantity

    @api.depends('user_id')
    def _compute_related_tag_ids(self):
        for record in self:
            user = record.user_id
            tickets = self.env['helpdesk.ticket'].search(
                [('user_id', '=', user.id)]
            )
            tags = tickets.mapped('tag_ids')
            self.update({
                'related_tag_is': [(6, 0, tags.ids)]
            })
