# Copyright (c) 2024, viral and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate, get_link_to_form
from frappe.model.mapper import get_mapped_doc


class RentAgreement(Document):
	def on_submit(self):
		docname = self.name
		data = frappe.db.sql(f"""
						Select name, start_date, end_date
					   From `tabRent Agreement`
					   Where start_date <= '{self.end_date}' AND end_date >= '{self.start_date}' and name != '{docname}' and shop_detail = '{self.shop_detail}'
				""", as_dict=1)
		if(len(data)):
			frappe.throw("Rent Agreement Already booked for {1} to {2}, <b>{0}</b>".format(get_link_to_form("Rent Agreement", data[0].get('name')), data[0].get('start_date'), data[0].get('end_date')))
	def on_cancel(self):
		self.status = "Cancelled"


@frappe.whitelist()
def make_payment_receipt(source_name, target_doc=None):
	doclist = get_mapped_doc(
		"Rent Agreement",
		source_name,
		{
			"Rent Agreement": {
				"doctype": "Payment Receipt",
				"field_map": {"shop_owner": "lessee", "shop_detail": "shop_details"},
			},

		},
		target_doc,
	)

	return doclist


def update_agreement_status():
	current_date = str(getdate())
	frappe.db.sql(f"""
				Update `tabRent Agreement` SET status = 'Expired'
				Where status = 'Active' and docstatus=1 and end_date < '{current_date}'
			""", as_dict = 1)
	


def create_payment_request():
	current_date = str(getdate())
	rent_agreement = frappe.db.sql(f"""
			Select name , shop_owner, company_name, shop_no, standard_rate, monthly_rent,monthly_rent_payment_date, end_date, shop_detail
			From `tabRent Agreement`
			where docstatus = 1 and status = 'Active'
	""", as_dict=1)

	for row in rent_agreement:
		new_doc = frappe.new_doc("Payment Request")
		new_doc.posting_date = current_date
		new_doc.rent_agreement = row.name
		new_doc.lessee_shop_owner = row.shop_owner
		new_doc.shop = row.shop_detail
		new_doc.mobile_no = frappe.db.get_value("Lessee - Shop Owner", row.shop_detail, "mobile_no")
		new_doc.monthly_rent = row.monthly_rent
		new_doc.email_id = frappe.db.get_value("Lessee - Shop Owner", row.shop_detail, "email_id")
		new_doc.payment_day_of_month = row.monthly_rent_payment_date
		try:
			new_doc.save()
			new_doc.submit()
		except Exception as e:
			frappe.log_error(e)


	
