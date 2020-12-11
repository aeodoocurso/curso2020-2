# -*- coding: utf-8 -*-

from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'

    name = fields.Char(
        string='Name',
        required=True,)

    description = fields.Text(
        string='Description',)

    date = fields.Date(
        string='Date',)

    dedicated_time = fields.Float(
        string='Time',)

    assigned = fields.Boolean(
        string='Assigned',
        compute='_compute_assigned',
        store=True,)

    assigned_qty = fields.Integer(
        string='Assigned qty',
        compute='_compute_assigned_qty',)

    date_due = fields.Date(
        string="Date Due",)

    new_tag_name = fields.Char(
        string = "New tag",)

    corrective_action = fields.Html(
        help='Detail of corrective action after this issue',)

    preventive_action = fields.Html(
        help='Detail of preventive action after this issue',)

    user_id = fields.Many2one(
        "res.users",
        string="Assigned to",)

    state_id = fields.Many2one(
        'helpdesk.ticket.state',
        string='State')

    action_ids = fields.One2many(
        'helpdesk.ticket.action',
        inverse_name='ticket_id',
        string='Actions')

    tag_ids = fields.Many2many(
        'helpdesk.tag',
        string="Tags",
        relation = 'helpdesk_ticket_tag_rel',
        column1 = 'ticket_id',
        column2 = 'tag_id',
    )

    related_tag_ids = fields.Many2many(
        'helpdesk.tag',
        string='Related Tags',
        compute='_compute_related_tag_ids')


    def create_new_tag(self):
        self.ensure_one()
        tag = self.env['helpdesk.tag'].create({
            'name': self.new_tag_name
        })
        self.tag_ids += tag


    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            record.assigned = record.user_id and True

    @api.depends('user_id')
    def _compute_assigned_qty(self):
        for record in self:
            user_id = record.user_id
            same_user_id_tickets = self.env['helpdesk.ticket'].search([
                ('user_id', '=', user_id.id)
            ])
            record.assigned_qty = len(same_user_id_tickets)


    @api.depends('user_id')
    def _compute_related_tag_ids(self):
        for record in self:
            user = record.user_id
            other_tickets = self.env['helpdesk.ticket'].search([
                ('user_id', '=', user.id)
            ])
            all_tags = other_tickets.mapped('tag_ids')

            self.update({
                'related_tag_ids': [(6, 0, all_tags.ids)]
            })



