

from odoo import models, fields


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = "Helpdesk Ticket"

    name = fields.Char(
        string='Name',
        required=True)

    description = fields.Text(
        string='Description')
    date = fields.Date(
        string='Date')
    # Estado [Nuevo, Asignado, En proceso, Pendiente, Resuelto, Cancelado], que por defecto sea Nuevo
    state = fields.Selection(
        [('new', 'New'),
         ('assigned', 'Assigned'),
         ('progress', 'Progress'),
         ('waiting', 'Waiting'),
         ('done', 'Done'),
         ('cancel', 'Cancel')],
        string='State',
        default='new')

    # Tiempo dedicado (en horas)
    dedicated_time = fields.Float(
        string='Time')

    # Asignado (tipo check)
    assigned = fields.Boolean(
        string='Assigned',
        readonly=False)

    # Fecha límite
    date_due = fields.Date(
        string='Date Due')

    # Acción correctiva (html)
    corrective_action = fields.Html(
        help='Detail of corrective action after this issue')
    # Acción preventiva (html)
    preventive_action = fields.Html(
        help='Detail of preventive action after this issue')
    # Ticket asociado a una persona (una persona puede tener muchos tickets, )
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Assigned to')

    # Asignar, cambia estado a asignado y pone a true el campo asignado, visible solo con estado = nuevo
    def set_assigned(self):
        self.ensure_one()  # para un solo registro
        self.write({
            'assigned': True,
            'state': 'assigned',
            'user_id': self.env.user.id # ID (int)
        })

    def set_assigned_multi(self):
        for ticket in self:
            ticket.set_assigned()

    # En proceso, visible sólo con estado = asignado
    def set_progress(self):
        self.ensure_one()
        self.state = 'progress'

    # Pendiente, visible en cualquier estado = en proceso o asignado
    def set_waiting(self):
        self.ensure_one()
        self.state = 'waiting'

    # Finalizar, visible en cualquier estado, menos cancelado y finalizado
    def set_done(self):
        self.ensure_one()
        self.state = 'done'

    # Cancelar, visible si no está cancelado
    def set_cancel(self):
        self.ensure_one()
        self.state = 'cancel'
