# Copyright (c) 2024, viral and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import calendar
from frappe.utils import getdate


class PaymentRequest(Document):
	pass



def notification_payment_reminder():
	rent_agreements = frappe.db.sql(f"""
						Select name, shop_owner, monthly_rent_payment_date, enable_payment_reminder
						From `tabRent Agreement`
						Where status = 'Active'
					""", as_dict = 1)
					
	for row in rent_agreements:
		if getdate().month == (row.monthly_rent_payment_date - 2) and row.enable_payment_reminder:
			content = ''
			due_payment = frappe.db.sql(f"""
								Select name, posting_date, rent_amount, lessee_shop_owner
								From `tabPayment Request`
								Where rent_agreement = '{row.name}' and status = 'Unpaid'
						""", as_dict = 1)
			
			content += """
						<h2>Gental Reminder of Rent Payment</h2>

						<p> Hello, {0} </p>

						<p>Bellow is the detail about your due payment of rent</p>
						""".format(frappe.db.get_value("Lessee - Shop Owner", row.shop_owner, "owner_name"))

			content += """
						<table width='60%' border=1>
							<tr>
								<th>Month</th>
								<th>Rent Amount</th>
							</tr>
						"""
			for d in due_payment:
				content += """
						<tr>
							<td align='center'>
								{0}
							</td>
							<td align='center'>
								{1}
							</td>
						</tr>
					""".format(calendar.month_name[d.posting_date.month], d.rent_amount)
				
			content += "</table>"
			email_id = frappe.db.get_value("Lessee - Shop Owner", row.shop_owner, "email_id")
			
			frappe.sendmail(
					recipients=email_id,
					subject="Rent Payment Reminder",
					message=content
				)
		



