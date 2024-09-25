// Copyright (c) 2024, viral and contributors
// For license information, please see license.txt

frappe.ui.form.on("Rent Agreement", {
	year:function(frm) {
        if(!frm.doc.start_date){
            frappe.throw("First add start date of rent agreement")
        }
        if(frm.doc.year){
            frm.set_value("end_date", frappe.datetime.add_days(frappe.datetime.add_months(frm.doc.start_date, 12 * frm.doc.year)))
        }
	},
    refresh:function(frm){
        frm.add_custom_button(__('Payment Receipt'), () => {
            frappe.model.open_mapped_doc({
                method: "certification.shop_management.doctype.rent_agreement.rent_agreement.make_payment_receipt",
                frm: cur_frm,
            });
        },__("Create"))
    }
});
