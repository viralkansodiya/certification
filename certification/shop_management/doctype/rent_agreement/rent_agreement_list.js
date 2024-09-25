frappe.listview_settings["Rent Agreement"] = {
	add_fields: ["status"],
	get_indicator: function (doc) {
		var colors = {
			Active: "green",
			Expried: "red",
		};
		let status = doc.status;
		return [__(status), colors[status], "status,=," + status];
	},
};