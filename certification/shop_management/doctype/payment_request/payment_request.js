// Copyright (c) 2024, viral and contributors
// For license information, please see license.txt

frappe.ui.form.on("Payment Request", {
	refresh(frm) {
        if(frm.doc.status == 'Unpaid'){
            frm.add_custom_button('Payment Receipt', function() {
                    frappe.model.open_mapped_doc({
                        method: "certification.shop_management.doctype.payment_request.payment_request.create_payment_receipt",
                        frm: cur_frm,
                    });
            }, 'Create');
        }
	},
});
