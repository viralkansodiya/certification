# Copyright (c) 2024, viral and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import flt
from frappe.model.document import Document
import random


class AirplaneTicket(Document):
    def before_save(self):
        total_amount = 0
        for row in self.add_ons:
            total_amount += row.amount

        self.total_amount = flt(total_amount) + flt(self.flight_price)
        self.remove_duplicate_add_ons()
        if self.is_new():
            self.validate_flight_capacity()
    
    def remove_duplicate_add_ons(self):
        add_ons = []
        item = []
        for row in self.add_ons:
            if row.item not in item:
                item.append(row.item)
                add_ons.append(row)
        self.add_ons = []
        self.add_ons = add_ons
    def on_submit(self):
        if self.status != "Boarded":
            frappe.throw("Status should be Boarded")
        
    def before_insert(self):
        self.set_random_seat()

    def set_random_seat(self):
        random_integer = random.randint(1, 99)  # Generates a random integer between 1 and 99
        random_letter = chr(random.randint(65, 69))  # Generates a random letter between A and E (ASCII 65 to 69)
        self.seat = f"{random_integer}{random_letter}"

    def validate_flight_capacity(self):
        airplane = frappe.db.get_value("Airplane Flight", self.flight, "airplane")
        capacity = frappe.db.get_value("Airplane", airplane, "capacity")
        if frappe.db.count("Airplane Ticket", {"flight": self.flight}) >= capacity:
            frappe.throw("No seats available")
