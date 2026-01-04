/** @odoo-module */

import { Component, useState} from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class ProposalDashboard extends Component {

    static template = "fibi.ProposalDashboardTemplate";

    async setup(){

        this.action= useService("action");
        this.state = useState({
            proposal_count: {},
            proposal_detail: [],
            proposal_status: []
        });

        await this.loadDashboardData();

    }


    async loadDashboardData() {
        try {
            const response = await fetch("/proposal/dashboard/data", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({})
            });
            const data = await response.json();
            const result = data.result;

            this.state.proposal_count = result.proposal_count || {};
            this.state.proposal_detail = result.proposal_detail || [];
            this.state.proposal_status = result.proposal_status || [];

            // Data updated → redraw chart
            this.renderChart();

        }
        catch (error){
            console.error("Dashboard Load Error:", error);
        }
    }

    renderChart(){

        // Make sure Chart.js is available
        if (typeof Chart === "undefined") {
            console.error("Chart.js missing");
            return;
        }

        const labels = this.state.proposal_status.map(p => p.status || "Undefined");
        const counts = this.state.proposal_status.map(p => p.status_count || 0);

        const chart1 = document.getElementById("proposal_status_chart_pd");

        if (chart1) {
            new Chart(chart1, {
                type: "radar",
                data: {
                    labels: labels,
                    datasets: [{
                        label: "Proposals",
                        data: counts,
                    }],
                },
            });
        }

        const chart2 = document.getElementById("proposal_status_");

        if (chart2){
            new Chart(chart2,{
                type:"polarArea",
                data:{
                    labels:labels,
                    datasets:[{
                        label:"Proposal",
                        data: counts
                    }]
                }
            })
        }
    }

    createProposal() {
        this.action.doAction({
            type: "ir.actions.act_window",
            res_model: "research.proposal",
            views: [[false, "form"]],
            target:"new"
        });
    }
}

registry.category("actions").add("fibi.proposal_action", ProposalDashboard);