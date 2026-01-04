from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResearchProject(models.Model):
    _name = "research.project"
    _description = "Research Project"

    name = fields.Char(required=True)
    award_id = fields.Many2one("research.award", required=True)
    pi_id = fields.Many2one(related="award_id.proposal_id.pi_id", store=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date()
    state = fields.Selection([
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
    ], default="ongoing")
    is_upcoming= fields.Boolean(string="Up Coming",compute="_is_upcoming")


    @api.depends("start_date")
    def _is_upcoming(self):
        date = fields.Date.today()
        for p in self:
            if p.start_date:
                p.is_upcoming= True if p.start_date and p.start_date >= date else False


    @api.constrains("start_date","end_date")
    def _validate_error(self):
        for p in self:
            if p.end_date and p.start_date:
                if p.end_date<=p.start_date:
                    raise ValidationError("The end date should be greater than start date")