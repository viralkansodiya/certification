import frappe


@frappe.whitelist()
def get_flight_details(date):
    data = frappe.db.sql(f"""
            Select *  
            From `tabAirplane Flight`
            Where status = "Scheduled" and date_of_departure = '{date}'
    """, as_dict=1)
    for row in data:
        row.update({"date_of_departure" : frappe.utils.format_date(row.date_of_departure, "d MMMM, YYYY")})
    return data

@frappe.whitelist()
def update_get_no(name, gate_no):
    frappe.db.set_value("Airplane Flight", name, "gate_no", gate_no)
    return "Gate No is successfully updated"
