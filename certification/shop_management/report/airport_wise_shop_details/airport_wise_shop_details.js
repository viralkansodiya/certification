// Copyright (c) 2024, viral and contributors
// For license information, please see license.txt

frappe.query_reports["Airport Wise Shop Details"] = {
	"filters": [
		{
			"fieldname" : "airport",
			"fieldtype" : "Link",
			"label" : "Airport",
			"options" : "Airport"
		}
	]
};
