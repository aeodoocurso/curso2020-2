from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError


class HelpdeskTicketAction(models.Model):
    """  """
    _name = 'helpdesk.ticket.action'
    _description = " Model to define all Actions in tickets"

    name = fields.Char(
            'Name')
    date = fields.Date(
            'Date')
    ticket_id = fields.Many2one(
            comodel_name='helpdesk.ticket')

    dedicated_time = fields.Float(
            'Time')


class HelpdeskTags(models.Model):
    """   """
    _name = 'helpdesk.tag'
    _description = " Model to define tags to helpdesk tickets"

    name = fields.Char('Name')
    ticket_ids = fields.Many2many(
            comodel_name='helpdesk.ticket',
            relation='helpdesk_ticket_tag_rel',
            column1='tag_id',
            column2='ticket_id',
            string="Tickets")

    # Methods
    @api.model
    def _clean_not_relateds(self):
        """ """
        tags = self.search([('ticket_ids', '=', False)])
        tags.unlink()


class HelpdeskTicket (models.Model):
    """   """
    _name = 'helpdesk.ticket'
    _description = "Helpdesk Ticket"

    # Defaults
    def _default_ticket_assign(self):
        """  """
        return self.env.user

    # Fields
    name = fields.Char(
            'Name',
            required=True)
    description = fields.Text(
            'Description')
    date = fields.Date('Date')

    state = fields.Selection(
            [('new', 'New'),
             ('assigned', 'Assigned'),
             ('in_progress', 'In Progress'),
             ('pending', 'Pending'),
             ('done', 'Done'),
             ('cancel', 'Cancel')],
            default='new')

    dedicated_time = fields.Float(
            'Time',
            compute='_computed_dedicated_time',
            inverse='_set_dedicated_time',
            search='_search_dedicated_time')

    assigned = fields.Boolean(
            compute="_compute_assigned")

    due_date = fields.Date('Due Date')

    corrective_action = fields.Html(
            help='To add all actions taken to fix the issue'
            )
    preventive_action = fields.Html(
            help='To add actions to prevent the issue to happen')

    user_id = fields.Many2one(
            comodel_name='res.users',
            string='Assigned to',
            default=_default_ticket_assign)

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

    tickets_for_user = fields.Integer(
            string='Tickets for user assigned',
            compute="_compute_tickets_for_user")

    tag_generator = fields.Char(
            string='Add new Tag')

    color = fields.Integer('Color')

    # Methods
    def _search_dedicated_time(self, operator, value):
        """  """
        query_str = """select ticket_id from helpdesk_ticket_action
                    group by ticket_id
                    having sum(dedicated_time) %s %s""" % (operator, value)
        self._cr.execute(query_str)
        res = self._cr.fetchall()
        return [('id', 'in', [r[0] for r in res])]

    def _set_dedicated_time(self):
        """  """
        for ticket in self:
            computed_time = sum(ticket.action_ids.mapped('dedicated_time'))
            if self.dedicated_time != computed_time:
                values = {
                        'name': "auto time",
                        'date': fields.Date.today(),
                        'ticket_id': ticket.id,
                        'dedicated_time': self.dedicated_time - computed_time
                        }
                ticket.update({
                    'action_ids': [(0, 0, values)]
                    })

    @api.depends('action_ids.dedicated_time')
    def _computed_dedicated_time(self):
        """  """
        # for ticket in self.filtered(lambda x: x.action_ids):
        for ticket in self:
            ticket.dedicated_time = ticket.action_ids and sum(
                    ticket.action_ids.mapped('dedicated_time')) or 0

    @api.onchange('date')
    def _onchange_date(self):
        """  """
        if self.date:
            if self.date >= fields.Date.today() and self.due_date:
                import datetime
                self.due_date = self.date + datetime.timedelta(days=1)
            else:
                raise UserError(
                        _("Date has to be grater or equal than %s "
                            % fields.Date.today()))

    @api.constrains('dedicated_time')
    def _check_dedicated_time(self):
        """  """
        for ticket in self:
            if ticket.dedicated_time < 0:
                raise ValidationError(_("Dedicated time must be positive"))

    def create_new_tag(self):
        """   """
        self.ensure_one()
        # import pdb; pdb.set_trace()
        action = self.env.ref(
                "helpdesk_osirisgtz.helpdesk_tag_quick_action").read()[0]
        action['context'] = {
               'default_name': self.tag_generator,
               'default_ticket_ids': [(6, 0, self.ids)]
               }
        action['views'] = [(self.env.ref(
            "helpdesk_osirisgtz.helpdesk_tag_view_form_related").id,
            'form')]
        return action

        # if self.tag_generator:
        #     new_tag = self.env['helpdesk.tag'].create({
        #         'name': self.tag_generator,
        #        # 'ticket_ids':[(4,self.id,0)]
        #         })
        #    # self.write({'tag_ids': [(4,new_tag.id,0)]})
        #     self.tag_ids += new_tag  # This works in this odoo version

    @api.depends('user_id')
    def _compute_tickets_for_user(self):
        """  """
        for ticket in self:
            user = ticket.user_id
            all_tickets = self.env['helpdesk.ticket'].search([
                ('user_id', '=', user.id)
                ])
            ticket.tickets_for_user = len(all_tickets)

    @api.depends('user_id')
    def _compute_assigned(self):
        """  """
        for ticket in self:
            ticket.assigned = ticket.user_id and True

    def btn_assigned(self):
        """"""
        self.ensure_one()
        self.write({
            'state': 'assigned',
            # 'assigned': True,
            'user_id': self.env.user.id
            })

    def btn_progress(self):
        """  """
        self.ensure_one()
        self.state = 'in_progress'

    def btn_pending(self):
        """  """
        self.ensure_one()
        self.state = 'pending'

    def btn_done(self):
        """  """
        self.ensure_one()
        self.state = 'done'

    def btn_cancel(self):
        """  """
        self.ensure_one()
        self.state = 'cancel'
