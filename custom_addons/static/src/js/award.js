/** @odoo-module */

import { Component, useState, xml } from "@odoo/owl";
import { registry } from "@web/core/registry";


export class AwardDashboard extends Component{

    static template = xml`
        <div>
            <h3>Award Dashboard</h3>
            <p>This is working!</p>
        </div>
    `;

    async setup(){
        this.state=useState({
            awardStatusCount:{},
            awardDetail:[]
        });
        this.loadAwardDashboard();
    }

    async loadAwardDashboard(){
        try{
            const response = await fetch("/award/dashboard/data",{
                method:"POST",
                headers:{
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({})
            })

            const data = await response.json();
            const result =data.result;
            this.state.awardStatusCount= result.award_status_count || {};
            this.state.awardDetail= result.award_detail || [];

        }
        catch(error){
            console.error(error)
        }
    }
}

registry.category("actions").add('fibi.award_action',AwardDashboard);