from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError
from datetime import datetime, timedelta


class CrmLeadTicket(models.Model):
    _name = 'crm.lead.ticket'
    _description = "Helpdesk Ticket"
    _inherits = {'crm.lead': 'lead_id'}

    lead_id = fields.Many2one(
        comodel_name='crm.lead',
        string='Lead'
        )

    # Acción correctiva (html)
    corrective_action = fields.Html(
        help='Detail of corrective action after this issue')
    # Acción preventiva (html)
    preventive_action = fields.Html(
        help='Detail of preventive action after this issue')