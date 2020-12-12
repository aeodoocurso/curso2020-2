from odoo import _, api, fields, models

class HelpdeskTicketState(models.Model):
    _name = 'helpdesk.ticket.state'
    _description= 'Helpdesk State'

    name = fields.Char(
        string='name',
    )


class HelpdeskTag(models.Model):
    _name = 'helpdesk.tag'
    _description= 'Helpdesk Tag'

    name = fields.Char(
        string='Name'
    )
    ticket_ids = fields.Many2many(
        comodel_name='helpdesk.ticket',
        relation='helpdesk_ticket_tag_rel',
        column1='tag_id',
        column2='ticket_id',
        string='Tickets')

class HelpdeskTickectAction(models.Model):
    _name = 'helpdesk.ticket.action'
    _description = 'HelpDesk Action'

    name = fields.Char(
        string='Name',
        required=True,
    )
    date = fields.Date(
        string='date',
    )
    ticket_id = fields.Many2one(
        comodel_name = 'helpdesk.ticket',
    )



class HelpdeskTicket (models.Model):
    _name = 'helpdesk.ticket'
    _description = 'HelpDesk Ticket'

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
        string='State'
    )
    dedicated_time = fields.Float(
        string='Time',
    )
    assigned = fields.Boolean(
        string='Assigned',
        compute='_compute_assigned',
        store=True,
    )
    assigned_qty = fields.Integer(
        string='Assigned Qty',
        compute='_compute_assigned_qty',
    )
    due_date = fields.Date(
        string='Due Date',
    )
    corrective_action =fields.Html(
        help='Default of corrective action after this issue',
    )
    preventive_action =fields.Html(
        help='Default of preventive action after this issue',
    )
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Assigned to',
    )
    action_ids = fields.One2many(
        comodel_name='helpdesk.ticket.action',
        inverse_name='ticket_id',
        string='Action',
    )
    tag_ids = fields.Many2many(
        comodel_name='helpdesk.tag',
        relation='helpdesk_ticket_tag_rel',
        column2='tag_id',
        column1='ticket_id',
        string='Tickets'
    )
    new_tag_name = fields.Char(
        string='New tag',
    )
    related_tag_ids = fields.Many2many(
        comodel_name='helpdesk.tag',
        string='Related Tags',
        compute='_compute_related_tag_ids'
    )

    def create_new_tag(self):
        self.ensure_one()
        tag = self.env['helpdesk.tag'].create(
            {
            'name': self.new_tag_name,
            }
        )
        self.tag_ids += tag\

    @api.depends('user_id')
    def _compute_related_tag_ids(self):
        for record in self:
            user = record.user_id
            other_tickers = self.env['helpdesk.ticket'].search(
                [
                ('user_id', '=', user.id),
                ]
            )
            all_tag = other_tickers.mapped('tag_ids')
            self.update({
                'related_tag_ids': [(6,0,all_tag.ids)]
            })


    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            record.assigned = record.user_id and True

    @api.depends('user_id')
    def _compute_assigned_qty(self):
        for record in self:
            user = record.user_id
            other_tickers = self.env['helpdesk.ticket'].search([
                ('user_id', '=', user.id)
            ])
            record.assigned_qty = len(other_tickers)


    def set_assigned_multi(self):
        for ticket in self:
            ticket.set_assigned()

    def set_assigned(self):
        self.ensure_one()
        self.write(
            {
                'assigned': True,
                'state': 'assigned',
                'user_id': self.env.user.id,
            }

        )

    def set_progress(self):
        self.ensure_one()
        self.state = 'progress'

    def set_waiting(self):
        self.ensure_one()
        self.state = 'waiting'

    def set_cancel(self):
        self.ensure_one()
        self.state = 'cancel'

    def set_done(self):
        self.ensure_one()
        self.state = 'done'