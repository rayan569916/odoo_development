from odoo import http
from odoo.http import request

class ResearchDashboard(http.Controller):
    @http.route("/research/dashboard/data", auth="user", type="json")
    def research_dashboard(self, **kw):
        Proposal=request.env["research.proposal"].sudo()
        Award=request.env["research.award"].sudo()
        Project=request.env["research.project"].sudo()
        Ethics=request.env["research.ethics.review"].sudo()

        card_data = {
            "proposal_count": Proposal.search_count([]),
            "approved_awards": Award.search_count([("state","=","approved")]),
            "ongoing_award" : Project.search_count([("state","=","ongoing")]),
            "pending_award" : Ethics.search_count([("status","=","pending")])
        }

        status_data = Proposal.read_group([],["id"],["status"])

        dept_data = Award.read_group([],["amount:sum"],["department"])

        upcoming_projects= Proposal.search([("is_upcoming", "=", True)],order="start_date asc",limit=5)

        upcoming_projects_list = [    
        {
            "id": p.id,
            "name": p.name,
            "pi": p.pi_id.name,
            "start_date": str(p.start_date),
        }
        for p in upcoming_projects
        ]

        values = {
            "card_data": card_data,
            "status_data": status_data,
            "dept_data": dept_data,
            "upcoming_projects": upcoming_projects_list,
        }

        return values
    
