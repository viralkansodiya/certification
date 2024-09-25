// Copyright (c) 2024, viral and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh:function(frm){
        if(!frm.doc.__islocal){
            frm.add_custom_button(__("Assign Seat"), () => {
                var d = new frappe.ui.Dialog({
                    'fields': [
                        {'label': 'Seat Number','fieldname': 'seat_number', 'fieldtype': 'Data'}
                    ],
                    primary_action: function(){
                        let data = d.get_values()
                        frm.set_value("seat", data.seat_number)
                        frm.save()
                        console.log(data)

                        d.hide();
                    }
                });
                d.show();
                
            },__("Actions"));
        }
    }
});
