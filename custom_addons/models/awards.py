from odoo import models, fields

class ResearchAward(models.Model):
    _name = "research.award"
    _description = "Research Award"

    name = fields.Char("Award Reference", required=True)
    pi_id = fields.Many2one("res.partner", string="Principal Investigator", required=True)
    proposal_id = fields.Many2one("research.proposal", required=True)
    budget_total = fields.Monetary("Total Budget")
    currency_id = fields.Many2one("res.currency", default=lambda self: self.env.company.currency_id.id)
    department = fields.Selection(related="proposal_id.department", store=True)
    state = fields.Selection([
        ("approved", "Approved"),
        ("ongoing", "Ongoing"),
        ("closed", "Closed"),
    ], default="approved")
