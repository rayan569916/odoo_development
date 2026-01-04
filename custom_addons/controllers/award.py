from odoo import http
from odoo.http import request

class AwardDashboard(http.Controller):
    @http.route("/award/dashboard/data", auth="user", type="json")
    def award_dashboard_data(self, **kw):
        Award = request.env["research.award"].sudo()

        award_status_count={
            "total_award": Award.search_count([]),
            "approved_award": Award.search_count([("state","=","approved")]),
            "ongoing_awaard": Award.search_count([("state","=","ongoing")]),
            "closed_award": Award.search_count([("state","=","closed")])
        }

        award_details_json = [
            {
                "name":p.name,
                "pi_id":p.pi_id,
                "proposal_id":p.proposal_id,
                "budget_total":p.budget_total,
                "currency_id":p.currency_id,
                "department":p.department,
                "state":p.state,
            }
            for p in Award.search([])
        ]

        award_data={
            "award_status_count":award_status_count,
            "award_details":award_details_json
        }

        return award_data