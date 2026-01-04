/** @odoo-module */

import { Component, useState} from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class ResearchDashboard extends Component {
    static template = "fibi.DashboardTemplate";

    async setup(){

        this.action= useService("action")

        this.state = useState ({
            cardData:{},
            statusData:[],
            deptData:[],
            upcomingProjects:[]
        })

        await this.loadDashboardData();
    }

    async loadDashboardData(){
        try
        {const response = await fetch('/research/dashboard/data',{
            method: "POST",
            headers: {
                    "Content-Type": "application/json",
                },
            body: JSON.stringify({})
        });

        const data = await response.json();
        const result = data.result;
        this.state.cardData= result.card_data || {};
        this.state.statusData= result.status_data || [];
        this.state.deptData= result.dept_data || [];     
        this.state.upcomingProjects = result.upcoming_projects || [];
        this.renderChart();
        }
        catch(error){
            console.error("Dashboard Load Error:", error);
        }
    }

    renderChart() {
        if (typeof Chart === "undefined") {
            console.log("Chart Error")
            return;
        }


        const Labels= this.state.statusData.map(p => p.status || 'undefined');
        const Count = this.state.statusData.map(p => p.status_count || 0);

        const dashboardChart1 = document.getElementById("proposal_status_chart");
        
        if (dashboardChart1) {
            new Chart(dashboardChart1, {
                type:"bar",
                data: {
                    labels: Labels,
                    datasets: [{
                        label: "Proposals",
                        data: Count
                    }],
                },
            });
        }

        const dashboardChart2 = document.getElementById("award_dept_chart");

        if (dashboardChart2) {
            new Chart (dashboardChart2,{
                type: "doughnut",
                data:{
                    labels:Labels,
                    datasets:[{
                        label:"Proposal",
                        data: Count
                    }],
                },
            })
        }

    }
    createAward() {
        this.action.doAction({
            type: "ir.actions.act_window",
            res_model: "research.award",
            views:[[false,"form"]],
            target: "new",
        });
    }
}

registry.category("actions").add("fibi.dashboard_action", ResearchDashboard);