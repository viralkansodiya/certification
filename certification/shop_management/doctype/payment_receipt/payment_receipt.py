# Copyright (c) 2024, viral and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from frappe.utils import getdate, get_link_to_form

class PaymentReceipt(Document):
	def validate(self):
		receipts = frappe.db.sql(f"""Select name, rent_agreement, posting_date
						   			From `tabPayment Receipt`
						   			Where rent_agreement = '{self.rent_agreement}' and name != '{self.name}' and is_advance = 0
						   		""", as_dict=1)

		for row in receipts:
			if not self.can_create_receipt(row):
				frappe.throw(f"Payment Receipt is allready available for this month. <b>{get_link_to_form('Payment Receipt',row.name)}</b>")

	def can_create_receipt(self, receipt):
		month = getdate(self.posting_date).month
		year = getdate(self.posting_date).year

		if receipt["rent_agreement"] == self.rent_agreement and receipt["posting_date"].month == month and receipt["posting_date"].year == year:
			return False  
		
		return True
	
	def on_submit(self):
		if not self.is_advance:
			frappe.db.set_value("Payment Request", self.payment_request, "status", "Paid")

	def on_cancel(self):
		if not self.is_advance:
			frappe.db.set_value("Payment Request", self.payment_request, "status", "Unpaid")