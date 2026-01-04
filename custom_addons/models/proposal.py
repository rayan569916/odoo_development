from odoo import fields, models, api

class ResearchProposal(models.Model):
    _name="research.proposal"
    _description="Research Proposal"

    name = fields.Char("Title", required=True)
    pi_id = fields.Many2one("res.partner", string="Principal Investigator", required=True)
    department = fields.Selection([
        ("science", "Science"),
        ("engineering", "Engineering"),
        ("humanities", "Humanities"),
        ("medicine", "Medicine"),
        ("other", "Other"),
    ], required=True)
    status = fields.Selection([
        ("draft", "Draft"),
        ("submitted", "Submitted"),
        ("under_review", "Under Review"),
        ("approved", "Approved"),
        ("declined", "Declined"),
    ], default="draft", tracking=True)
    start_date = fields.Date()
    end_date = fields.Date()
    budget_total=fields.Monetary("Total Budget")
    currency_id=fields.Many2one("res.currency", default = lambda self: self.env.company.currency_id.id)
    award_ids = fields.One2many("research.award", "proposal_id", string="Awards")
    is_upcoming= fields.Boolean(string="Up Coming",compute="_is_upcoming",store=True)

    @api.depends('start_date')
    def _is_upcoming(self):
        today=fields.Date.today()
        for rec in self:
            rec.is_upcoming = True if rec.start_date and rec.start_date >= today else False

