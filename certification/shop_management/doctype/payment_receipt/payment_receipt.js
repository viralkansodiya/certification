// Copyright (c) 2024, viral and contributors
// For license information, please see license.txt

frappe.ui.form.on("Payment Receipt", {
	is_advance(frm) {
        if(frm.doc.is_advance){
            frappe.model.get_value("Rent Agreement", frm.doc.rent_agreement, "advance_amount", r=>{
                frm.set_value("rent_amount", r.advance_amount)
            })
        }
        else{
            frappe.model.get_value("Rent Agreement", frm.doc.rent_agreement, "monthly_rent", r=>{
                frm.set_value("rent_amount", r.monthly_rent)
            })
        }
	},
    
});
