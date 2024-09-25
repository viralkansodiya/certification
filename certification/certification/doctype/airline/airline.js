// Copyright (c) 2024, viral and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
	refresh(frm) {
        if (frm.doc.website_link){
            frm.add_web_link(frm.doc.website_link, "View Website")
        }
	},
});
