# Copyright (c) 2024, viral and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator


class ShopDetail(WebsiteGenerator):
	def validate(self):
		super().validate()
