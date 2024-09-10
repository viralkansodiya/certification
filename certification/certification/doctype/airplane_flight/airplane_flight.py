# Copyright (c) 2024, viral and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document


class AirplaneFlight(Document):
	def on_submit(self):
		self.status = "Completed"
