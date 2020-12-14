from odoo import fields, models


class NewTicketFromTag(models.TransientModel):
    _name = 'new.ticket.from.tag'
    _description = 'New ticket from tag'

    def _get_default_tag(self):
        return self._context.get('active_id')

    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Date')
    user_id = fields.Many2one(comodel_name='res.users', string='User')
    tag_id = fields.Many2one(
        comodel_name='helpdesk.tag',
        string='Tag',
        default=_get_default_tag
    )

    def create_ticket(self):
        tag_id = self.tag_id.id
        values = {
            'name': self.name,
            'date': self.date,
            'user_id': self.user_id.id,
            'tag_ids':[(6, 0, [tag_id])]
        }
        ticket = self.env['helpdesk.ticket'].create(values)

        action = self.env.ref('helpdesk_salvamad.helpdesk_ticket_action').read()[0]
        action['views']=[(
            self.env.ref('helpdesk_salvamad.view_helpdesk_ticket_form').id,
            'form'
        )]

        action['res_id'] = ticket.id
        return action
