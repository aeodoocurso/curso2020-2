# -*- coding: utf-8 -*-

from odoo import fields, models


class HelpdeskTicket(models.Model):

    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'

    # Nombre de la tarea
    name = fields.Char(string='Name', required=True)
    # Descrición de la tarea
    description = fields.Text(string='Description')
    # Fecha de alta de la tarea
    date = fields.Date(string='Date')

    # Estado [Nuevo, Asignado, En proceso, Pendiente, Resuelto, Cancelado], que por defecto sea Nuevo
    state = fields.Selection([
        ('new', 'New'),
        ('assigned','Assigned'),
        ('progress','Progress'),
        ('remaining', 'Remaining'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ], string='State', default='new')
    # Tiempo dedicado (en horas)
    dedicated_time = fields.Float(string='Time in hours')
    # Asignado (tipo check)
    assigned = fields.Boolean(string='Assigned', readonly=True)
    # Fecha límite
    deadline = fields.Date(string='Deadline date')
    # Acción correctiva (html)
    corrective_action = fields.Html(string='Corrective action', help="Actions to be taken to correct this task")
    # Acción preventiva (html)
    preventive_action = fields.Html(string='Preventive action', help="Actions to be taken to prevent errors")

    user_id = fields.Many2one(comodel_name='res.users', string='Assigned to')
    
    def set_assigned_multi(self):
        for ticket in self:
            ticket.set_assigned()

    def set_assigned(self):
        self.ensure_one()
        self.write(
            {'assigned' : True,
            'state' : 'assigned',
            'user_id':self.env.uid})
        
    def set_progress(self):
        self.ensure_one()
        self.state = 'progress'

    def set_remaining(self):    
        self.ensure_one()
        self.state = 'remaining'

    def set_done(self):    
        self.ensure_one()
        self.state = 'done'

    def set_cancel(self):    
        self.ensure_one()
        self.state = 'cancel'
    



