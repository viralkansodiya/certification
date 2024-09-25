import frappe

@frappe.whitelist()
def get_flights_crew_member(flight):
    data  = frappe.db.sql(f"""
                        Select at.name, fp.full_name, fp.date_of_birth, at.seat, at.status, at.departure_date, at.departure_time
                        From `tabAirplane Ticket` as at
                        Left Join `tabFlight Passenger` as fp ON fp.name = at.passenger
                        Where flight = '{flight}'
                        """, as_dict=1)
    
    for row in data:
        row.update({"date_of_birth":frappe.utils.format_date(row.date_of_birth, "d MMMM, YYYY")})
    
    return data
    
