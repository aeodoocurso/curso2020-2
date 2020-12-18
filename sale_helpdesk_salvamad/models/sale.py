from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    ticket_ids = fields.One2many(
        comodel_name='helpdesk.ticket',
        inverse_name='sale_id',
        string='Tickets'
    )

    def action_cancel(self):
        # Extender antes de la llamada
        res = super(SaleOrder, self).action_cancel()
        # Extender después de la llamada
        self.mapped('ticket_ids').write({'state':'cancel'})
        return res
       

