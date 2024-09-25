// Copyright (c) 2024, viral and contributors
// For license information, please see license.txt

frappe.ui.form.on("Lessee - Shop Owner", {
	refresh(frm) {
        if (frm.doc.website_link){
            frm.add_web_link(frm.doc.website_link, "View Website")
        }
	},
    person_address(frm){
        let _address_field = "person_address";
		let _display_field = "address_display";

		if (!frm.doc[_address_field]) {
			frm.set_value(_display_field, "");
			return;
		}

		frappe
			.xcall("frappe.contacts.doctype.address.address.get_address_display", {
				address_dict: frm.doc[_address_field],
			})
			.then((address_display) => frm.set_value(_display_field, address_display));
	},
    
});
