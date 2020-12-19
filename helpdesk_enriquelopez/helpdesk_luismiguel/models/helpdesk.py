# -*- coding: utf-8 -*-
from odoo import models, fields

class HelpdeskTicket(models.Model):
    _name = "helpdesk.ticket"
    _description = "Helpdesk Ticket"

    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripción")
    date = fields.Date(string="Fecha")

    state = fields.Selection(
        [('nuevo', 'Nuevo'),
         ('asignado', 'Asignado'),
         ('enproceso', 'En proceso'),
         ('pendiente', 'Pendiente'),
         ('resuelto', 'Resuelto'),
         ('cancelado', 'Cancelado')],
         string="Estado",
         default="nuevo")

    horas_dedicadas = fields.Float(string="Tiempo")
    asignado = fields.Boolean(string="Asignado", readonly=True)
    fecha_limite = fields.Date(string="Fecha límite")
    accion_correctiva = fields.Html(help="Detalles de la acción correctiva")
    accion_preventiva = fields.Html(help="Detalles de la acción preventiva")

    def set_asignado_multi(self):
        for ticket in self:
            ticket.set_asignado()
    
    def set_asignado(self):
        self.ensure_one()
        self.write({
            "asignado": True,
            "state": "asignado"
        })

    def set_enproceso(self):
        self.ensure_one()
        self.state = "enproceso"

    def set_pendiente(self):
        self.ensure_one()
        self.state = "pendiente"
    
    def set_resuelto(self):
        self.ensure_one()
        self.state = "resuelto"
    
    def set_cancelado(self):
        self.ensure_one()
        self.state = "cancelado"