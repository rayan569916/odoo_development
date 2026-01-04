from odoo import models, fields

class EthicsReview(models.Model):
    _name = "research.ethics.review"
    _description = "Ethics Review"

    name = fields.Char("Reference", required=True)
    project_id = fields.Many2one("research.project", required=True)
    status = fields.Selection([
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ], default="pending")
    committee_date = fields.Date()
