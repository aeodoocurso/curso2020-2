from odoo import api, fields, models


class HelpdeskTicketState(models.Model):
    _name = 'helpdesk.ticket.state'
    _description = 'Helpdesk State'

    name = fields.Char()


class HelpdeskTag(models.Model):
    _name = 'helpdesk.tag'
    _description = 'Helpdesk Tag'

    name = fields.Char()
    ticket_ids = fields.Many2many(
        comodel_name='helpdesk.ticket',
        relation='helpdesk_ticket_tag_rel',
        column1='tag_id',
        column2='ticket_id',
        string='Tickets')


class HelpdeskTicketAction(models.Model):
    _name = 'helpdesk.ticket.action'
    _description = 'Helpdesk Action'

    name = fields.Char()
    date = fields.Date()
    ticket_id = fields.Many2one(
        comodel_name='helpdesk.ticket')


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
    state_id = fields.Many2one(
        comodel_name='helpdesk.ticket.state',
        string='State')
    # state = fields.Selection(
    #     [('new', 'New'),
    #      ('assigned', 'Assigned'),
    #      ('progress', 'Progress'),
    #      ('waiting', 'Waiting'),
    #      ('done', 'Done'),
    #      ('cancel', 'Cancel')],
    #     string='State',
    #     default='new')
    dedicated_time = fields.Float(
        string='Time')

    assigned = fields.Boolean(
        string='Assigned',
        compute='_compute_assinged',
        store=True)

    assigned_qty = fields.Integer(
        string='Assigned Qty',
        compute='_compute_assigned_qty')

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Assigned to')

    date_due = fields.Date(
        string='Date Due')

    corrective_action = fields.Html(
        help='Detail of corrective action after this issue'
    )
    preventive_action = fields.Html(
        help='Detail of preventive action after this issue')

    action_ids = fields.One2many(
        comodel_name='helpdesk.ticket.action',
        inverse_name='ticket_id',
        string='Actions')

    tag_ids = fields.Many2many(
        comodel_name='helpdesk.tag',
        relation='helpdesk_ticket_tag_rel',
        column1='ticket_id',
        column2='tag_id',
        string='Tags')

    related_tag_is = fields.Many2many(
        comodel_name='helpdesk.tag',
        string='Related Tags',
        compute='_compute_related_tag_ids')

    new_tag_name = fields.Char(
        string='New tag')

    color = fields.Integer(string='Color')

    def create_new_tag(self):
        self.ensure_one()
        tag = self.env['helpdesk.tag'].create({
            'name': self.new_tag_name,
            # 'ticket_ids': [(4, self.id, 0)]
        })
        # self.write({
        #     'tag_ids': [(4, tag.id, 0)]
        # })
        self.tag_ids = self.tag_ids + tag

    @api.depends('user_id')
    def _compute_assinged(self):
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

    @api.depends('user_id')
    def _compute_related_tag_ids(self):
        for record in self:
            user = record.user_id
            other_tickers = self.env['helpdesk.ticket'].search([
                ('user_id', '=', user.id)
            ])
            all_tag = other_tickers.mapped('tag_ids')
            # self.related_tag_is = all_tag
            self.update({
                'related_tag_is': [(6, 0, all_tag.ids)]
            })
