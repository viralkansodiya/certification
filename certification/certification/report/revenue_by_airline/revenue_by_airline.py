# Copyright (c) 2024, viral and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []
	data , chart_data , report_summary = get_data(filters)
	columns = get_columns(filters)
	return columns, data, None, chart_data, report_summary


def get_data(filters):
	data = frappe.db.sql(f"""
		Select ar.name as airline, IF(at.total_amount, sum(at.total_amount), 0) as revenue
		From `tabAirline` as ar
		Left Join `tabAirplane` as ap ON ap.airline = ar.name
		Left Join `tabAirplane Flight`  as af ON af.airplane = ap.name
		Left Join `tabAirplane Ticket` as at ON at.flight = af.name
		Group By ar.name 
		Order By at.total_amount DESC
		""", as_dict=1)
	
	chart = prepare_chart_data(data)
	report_summary = get_report_summary(data)
	return data, chart, report_summary


def get_report_summary(data):
	total_revenue = 0
	for row in data:
		total_revenue += row.get('revenue')
	return [{"value": total_revenue, "label": "Total Ravenue", "datatype": "Currency"},]

def get_columns(filters):
	columns = [
		{
			"fieldname":"airline",
			"label":"Airline",
			"fieldtype":"Link",
			"options":"Airline",
			"width":200
		},
		{
			"fieldname":"revenue",
			"label":"Revenue",
			"fieldtype":"Currency",
			"default":0,
			"width":200
		}
	]
	return columns
	

def prepare_chart_data(data):
	labels = [row.airline for row in data]
	values = [row.revenue for row in data]

	return {
		"data": {"labels": labels, "datasets": [{"values": values}]},
		"type": "donut",
		"height": 300,
	}