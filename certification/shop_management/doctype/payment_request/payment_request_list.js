frappe.listview_settings["Payment Request"] = {
	add_fields: ["status"],
	get_indicator: function (doc) {
		var colors = {
			Paid: "green",
			Unpaid: "red",
		};
		let status = doc.status;
		return [__(status), colors[status], "status,=," + status];
	},
};