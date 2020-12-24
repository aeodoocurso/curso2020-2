from odoo import fields, models


class TicketsFromTag(models.TransientModel):
    """  """
    _name = 'tickets.from.tag'
    _description = 'Wizard to create tickets from tag.'

    # Defaults
    def _default_get_tag(self):
        """  """
        return self._context.get('active_id')

    name = fields.Char(
            'Name',
            required=True)

    date = fields.Date(
            'Date')

    user_id = fields.Many2one(
            comodel_name='res.users',
            string='User')

    tag_id = fields.Many2one(
            comodel_name='helpdesk.tag',
            string='Tag',
            default=_default_get_tag)

    # Methods
    def create_ticket(self):
        """  """
        # self.env.context == self._context
        # tag_id = self._context.get('active_id')

        values = {
                'name': self.name,
                'date': self.date,
                'user_id': self.user_id.id,
                'tag_ids': [(6, 0, self.tag_id.ids)]
                }
        ticket = self.env['helpdesk.ticket'].create(values)

        action = self.env.ref(
                'helpdesk_osirisgtz.helpdesk_ticket_action').read()[0]
        # action['context'] = {
        #        'res_id': ticket.id,}
        action['views'] = [(self.env.ref(
            'helpdesk_osirisgtz.helpdesk_ticket_view_form').id, 'form')
            ]
        action['res_id'] = ticket.id
        return action
