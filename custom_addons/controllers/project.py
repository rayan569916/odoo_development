from odoo import http
from odoo.http import request

class ProjectDashboard(http.Controller):
    @http.route("/project/dashboard/data",auth="user",type="json")
    def projectDashboard(self, **kw):
        Project = request.env["research.project"].sudo()

        project_count= {
            "total_projects": Project.search_count([]),
            "ongoing_projects": Project.search_count([("state","=","ongoing")]),
            "completed_projects": Project.search_count([("state","=","completed")])
        }

        project_data_json= [{
            "name":p.name,
            "award_id":p.award_id,
            "pi_id":p.pi_id,
            "start_date":p.start_date,
            "end_date":p.end_date,
            "state":p.end_date,
            "is_upcoming":p.end_date,
        }
        for p in Project.search([])
        ]

        project = {
            "project_count":project_count,
            "project_data":project_data_json
        }

        return project