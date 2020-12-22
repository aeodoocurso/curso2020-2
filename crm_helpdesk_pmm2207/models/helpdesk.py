from odoo import api, fields, models




class CrmLeadTicket(models.Model):
    _name = 'crm.lead.ticket'
    _description = "Helpdesk Ticket"
    _inherits = {'crm.lead': 'lead_id'}

    lead_id = fields.Many2one(
        comodel_name="crm.lead",
        string="lead")

    corrective_action = fields.Html(
        help='Detail of corrective action after this issue'
    )

    preventive_action = fields.Html(
        help='Detail of preventive action after this issue'
    )
