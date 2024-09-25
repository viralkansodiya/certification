# Copyright (c) 2024, viral and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import getdate


def execute(filters=None):
	columns, data = [], []
	columns, data = get_data(filters)
	return columns, data

def get_data(filters):
	condition = ""
	if filters.get('airport'):
		condition += f" and sd.airport = '{filters.get('airport')}'"
	data = frappe.db.sql(f"""
    SELECT sd.name, sd.shop_no, sd.airport, sd.terminal, sd.shop_size, sd.standard_rent, ra.name AS rent_agreement, 
           ra.shop_owner, ra.company_name, ra.start_date, ra.end_date, ra.standard_rate AS monthly_rent, 
           ra.advance_amount, ra.status
		FROM `tabShop Detail` AS sd
		LEFT JOIN `tabRent Agreement` AS ra ON sd.name = ra.shop_detail AND ra.status = 'Active' AND ra.docstatus = 1
		WHERE 1=1 {condition}
	""", as_dict=1)


	for row in data:
		if row.rent_agreement:
			row.update({"remaining_date" : (row.end_date - getdate()).days})

	columns = [
		
		{
			"fieldname" : "airport",
			"fieldtype" : "Link",
			"label" : "Airport",
			"options" : "Airport",
		},
		{
			"fieldname" : "shop_no",
			"fieldtype" : "Data",
			"label" : "Shop No",
		},
		{
			"fieldname" : "terminal",
			"fieldtype" : "Data",
			"label" : "Terminal",
		},
		{
			"fieldname" : "shop_size",
			"fieldtype" : "data",
			"label" : "Shop Size(In Square Feet)",
			"options" : "Airport",
		},
		{
			"fieldname" : "standard_rent",
			"fieldtype" : "data",
			"label" : "Shop Size(In Square Feet)",
			"options" : "Airport",
		},
		{
			"fieldname" : "rent_agreement",
			"fieldtype" : "Link",
			"label" : "Rent Agreement",
			"options" : "Rent Agreement",
		},
		{
			"fieldname" : "rent_agreement",
			"fieldtype" : "Link",
			"label" : "Rent Agreement",
			"options" : "Rent Agreement",
		},
		{
			
			"fieldname" : "shop_owner",
			"fieldtype" : "Link",
			"label" : "Lessee - Shop Owner",
			"options" : "Lessee - Shop Owner",
		},
		{
			"fieldname" : "company_name",
			"fieldtype" : "Data",
			"label" : "Company Name",
		},
		{
			"fieldname" : "start_date",
			"fieldtype" : "Date",
			"label" : "Start date",
		},
		{
			"fieldname" : "end_date",
			"fieldtype" : "Date",
			"label" : "End Date",
		},
		{
			"fieldname" : "monthly_rent",
			"fieldtype" : "Currency",
			"label" : "Monthly Rent",
		},
		{
			"fieldname" : "advance_amount",
			"fieldtype" : "Currency",
			"label" : "Advance Amount",
		},
		{
			"fieldname" : "status",
			"fieldtype" : "Data",
			"label" : "Status",	
		},
		{
			"fieldname" : "remaining_date",
			"fieldtype" : "Data",
			"label" : "Remaining Date",	
		}

	]

	return columns,data 

	
