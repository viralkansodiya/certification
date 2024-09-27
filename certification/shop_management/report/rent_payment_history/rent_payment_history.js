// Copyright (c) 2024, viral and contributors
// For license information, please see license.txt

frappe.query_reports["Rent Payment History"] = {
	"filters": [
		{
			"fieldname" : "rent_agreement",
			"fieldtype" : "Link",
			"options" : "Rent Agreement",
			"label" : "Rent Agreement"			
		},
		{
			"fieldname" : "company_name",
			"fieldtype" : "Data",
			"label" : "Brand Name"			
		},
		{
			"fieldname" : "shop_owner",
			"fieldtype" : "Link",
			"options" : "Lessee - Shop Owner",
			"label" : "Shop Owner"
		},
		{
			"fieldname" : "status",
			"fieldtype" : "Select",
			"options" : ['', "Paid", "Unpaid"],
			"label" : "Payment Status"
		},
		{
			"fieldname" : "from_date",
			"fieldtype" : "Date",
			"label" : "From Date"
		},
		{
			"fieldname" : "to_date",
			"fieldtype" : "Date",
			"label" : "To Date"
		},

	]
};
