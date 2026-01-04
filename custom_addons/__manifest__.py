{
    "name": "fibi",
    "author": "Development Team",
    "license": "LGPL-3",
    "category": "Research Administration",
    "version": "1.0",
    "summary": "Manage research proposals, awards and projects",
    "depends": ["base", "web"],
    "data": [
        "security/ir.model.access.csv",
        "views/proposal_views.xml",
        "views/menu.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "fibi/static/src/css/dashboard.css",
            "fibi/static/src/js/dashboard.js",
            "fibi/static/src/js/proposal.js",
            "fibi/static/src/js/award.js",
            "fibi/static/lib/chartjs/chart.umd.js",
            "fibi/static/src/xml/proposal_dashboard_template.xml",
            "fibi/static/src/xml/dashboard_template.xml",
        ],
    },
    "application": True,
}
