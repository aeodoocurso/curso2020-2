# -*- coding: utf-8 -*-
"""
    Modulo para la gestion de incidencias
"""
from odoo import api, fields, models


class HelpdeskTicketState(models.Model):
    """
        Modelo de los estados de los tickets
    """
    _name = "helpdesk.ticket.state"
    _description = "Helpdesk Ticket State"

    name = fields.Char()


class HelpdeskTag(models.Model):
    """
        Modelo de las etiqutas de los tickets
    """
    _name = "helpdesk.tag"
    _description = "Helpdesk Tag"

    name = fields.Char()
    ticket = fields.Boolean()
    action = fields.Boolean()
    ticket_ids = fields.Many2many(
        comodel_name="helpdesk.ticket",
        relation="helpdesk_ticket_tag_rel",
        column1="tag_id",
        column2="ticket_id",
        string="Tickets")


class HelpdeskTicketAction(models.Model):
    """
        Modelo de las acciones de los tickets
    """
    _name = "helpdesk.ticket.action"
    _description = "Helpdesk Ticket Action"

    name = fields.Char()
    date = fields.Date()
    ticket_id = fields.Many2one(
        comodel_name="helpdesk.ticket")


class HelpdeskTicket(models.Model):
    """
        Modelo de los tickets
    """
    _name = "helpdesk.ticket"
    _description = "Helpdesk Ticket"

    name = fields.Char(string="Nombre")
    description = fields.Text(string=u"Descripción")
    date = fields.Date(string="Fecha")

    # state = fields.Selection(
    #     [('nuevo', 'Nuevo'),
    #      ('asignado', 'Asignado'),
    #      ('enproceso', 'En proceso'),
    #      ('pendiente', 'Pendiente'),
    #      ('resuelto', 'Resuelto'),
    #      ('cancelado', 'Cancelado')],
    #      string="Estado",
    #      default="nuevo", track_visibility='onchange')

    state_id = fields.Many2one(
        comodel_name="helpdesk.ticket.state",
        string="Estado")

    horas_dedicadas = fields.Float(string="Tiempo")

    asignado = fields.Boolean(
        string="Asignado",
        compute="_compute_asignado",
        store=True)

    num_asignados = fields.Integer(
        string=u"Número de asignados",
        compute="_compute_num_asignados")

    fecha_limite = fields.Date(string=u"Fecha límite")
    accion_correctiva = fields.Html(help=u"Detalles de la acción correctiva")
    accion_preventiva = fields.Html(help=u"Detalles de la acción preventiva")

    user_id = fields.Many2one(
        comodel_name="res.users",
        string="Asignado a")

    action_ids = fields.One2many(
        comodel_name="helpdesk.ticket.action",
        inverse_name="ticket_id",
        string="Acciones")

    tag_ids = fields.Many2many(
        comodel_name="helpdesk.tag",
        relation="helpdesk_ticket_tag_rel",
        column1="ticket_id",
        column2="tag_id",
        string="Etiquetas")

    tag_relacionado_ids = fields.Many2many(
        comodel_name="helpdesk.tag",
        string="Etiquetas relacionadas",
        compute="_compute_tag_relacionado_ids")

    nombre_nuevo_tag = fields.Char(
        string="Nueva etiqueta")

    def crear_nuevo_tag(self):
        """
            Funcion para crear una nueva etiqueta
        """
        self.ensure_one()
        # tag = self.env["helpdesk.tag"].create({
        #     "name": self.nombre_nuevo_tag,
        #     # "ticket_ids": [(4, self.id, 0)]
        # })
        # # self.write({
        # #     "tag_ids": [(4, tag.id, 0)]
        # # })
        # self.tag_ids += tag

        action = self.env.ref(
            'helpdesk_luismiguel.helpdesk_tag_new_action').read()[0]
        action['context'] = {
            'default_name': self.nombre_nuevo_tag,
            'default_ticket_ids': [(6, 0, self.ids)]
        }
        return action

    def _compute_tag_relacionado_ids(self):
        for record in self:
            user = record.user_id
            tickets = self.env["helpdesk.ticket"].search([
                ("user_id", "=", user.id), ("id", "!=", record.id)
            ])
            all_tag = tickets.mapped("tag_ids")
            self.tag_relacionado_ids = all_tag

    # def set_asignado_multi(self):
    #     for ticket in self:
    #         ticket.set_asignado()

    # def set_asignado(self):
    #     self.ensure_one()
    #     self.write({
    #         "state": "asignado",
    #         "asignado": True
    #     })

    # def set_enproceso(self):
    #     self.ensure_one()
    #     self.state = "enproceso"

    # def set_pendiente(self):
    #     self.ensure_one()
    #     self.state = "pendiente"

    # def set_resuelto(self):
    #     self.ensure_one()
    #     self.state = "resuelto"

    # def set_cancelado(self):
    #     self.ensure_one()
    #     self.state = "cancelado"

    @api.depends("user_id")
    def _compute_asignado(self):
        for record in self:
            record.asignado = record.user_id and True

    def _compute_num_asignados(self):
        for record in self:
            user = record.user_id
            tickets = self.env["helpdesk.ticket"].search([
                ("user_id", "=", user.id)
            ])
            record.num_asignados = len(tickets)
