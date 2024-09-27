<p>Hello {{ frappe.db.get_value("Lessee - Shop Owner" , doc.lessee_shop_owner, "owner_name") }},</p>

<br>
<p>This Email we are sending you to remind about this month of rent payment.</p>
<br>
<p>If you have already paid then ignore this email</p>
<br>
<p><b>Rent Amount : </b>{{ doc.rent_amount }}</p>

<br>
<p>Last day of payment is 6th day of this month.</p>
<br>
<br>


Thanks