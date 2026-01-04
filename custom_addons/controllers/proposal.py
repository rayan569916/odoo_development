from odoo import http
from odoo.http import request

class ProposalDashboard(http.Controller):
    @http.route("/proposal/dashboard/data", auth="user", type="json")
    def proposal_dashboard(self, **kw):
        Proposal=request.env["research.proposal"].sudo()

        proposal_count = {
            "total_count": Proposal.search_count([]),
            "total_draft": Proposal.search_count([("status","=","draft")]),
            "total_submitted": Proposal.search_count([("status","=","submitted")]),
            "total_under_review": Proposal.search_count([("status","=","under_review")]),
            "total_approved": Proposal.search_count([("status","=","approved")]),
            "total_declined": Proposal.search_count([("status","=","declined")]),
        }

        proposal_detail = [
            {
                "name":p.name,
                "pi_id":p.pi_id.name,
                "department":p.department,
                "status":p.status,
                "start_date":p.start_date,
                "end_date":p.end_date,
                "budget_total":p.budget_total,
                "currency_id":p.currency_id,
                "award_ids":p.award_ids,
                "is_upcoming":p.is_upcoming,
            }
            for p in Proposal.search([])
        ]

        proposal_status= Proposal.read_group([],["id"],["status"])

        proposal = {
            "proposal_count": proposal_count,
            "proposal_detail": proposal_detail,
            "proposal_status": proposal_status
        }

        return proposal