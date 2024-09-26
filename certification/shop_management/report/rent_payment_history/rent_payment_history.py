# Copyright (c) 2024, viral and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []
	columns , data = get_data(filters)
	return columns, data


def get_data(filters):
	condition = ''
	if filters.get("rent_agreement"):
		condition += f" and p.rent_agreement = '{filters.get('rent_agreement')}'"
	if filters.get("company_name"):
		condition += f" and ra.company_name like '%{filters.get('company_name')}%'"
	if filters.get("shop_owner"):
		condition += f" and  r.lessee_shop_owner = '{filters.get('shop_owner')}'"
	if filters.get("from_date"):
		condition += f"p.posting_date >= '{filters.get('from_date')}'"
	if filters.get("to_date"):
		condition += f"p.posting_date <= '{filters.get('to_date')}'"




	data = frappe.db.sql(f"""
			Select p.name , p.rent_agreement, p.lessee_shop_owner, p.shop, p.rent_amount, p.payment_day_of_month, p.status, ra.company_name
			From `tabPayment Request` as p
			join `tabPayment Receipt` as r ON p.name = r.payment_request
			join `tabRent Agreement` as ra ON p.rent_agreement = ra.name
			where r.docstatus = 1 {condition}
	""", as_dict=1)

	columns = [
		{
			"fieldname" : "name",
			"fieldtype" : "Link",
			"options" : "Payment Request",
			"label" : "Payment Request",
		},
		{
			"fieldname" : "lessee_shop_owner",
			"fieldtype" : "Link",
			"options" : "Lessee - Shop Owner",
			"label" : "Shop Owner"	
		},
		{
			"fieldname" : "company_name",
			"fieldtype" : "Data",
			"label" : "Brand Name"
		}
	]

	return columns , data

	