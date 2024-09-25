
frappe.pages['Update Gate No of Flights'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Update Gate No of Flights',
		single_column: true
	});
	frappe.UpdateFlight.init(wrapper, page);
}


frappe.UpdateFlight = {
	init: function(wrapper, page){
		console.log("constructor")
		this.setup_field(wrapper, page)
		this.wrapper = $(wrapper).find('.layout-main-section');
		this.page = wrapper.page;
		this.wrapper.append(`<style>
				
					.flight-card {
						border: 1px solid #ddd;
						padding: 10px;
						border-radius: 8px;
						display:inlign;
						background-color: #f9f9f9;
						box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
						margin: 10px;
					}
					.flight-card h4 {
						margin: 0;
						font-size: 18px;
					}
					.flight-card p {
						margin: 5px 0;
						font-size: 14px;
					}
					.update {
						margin-top:5px;
					}
					</style>
			<div class="cards"></div>`)
		

		this.get_flight_update_on_page(wrapper, page)
	},

	setup_field:function(wrapper, page){
		this.posting_date_field = page.add_field({
			fieldname: 'posting_date',
			label: __('Required Execution Date'),
			fieldtype:'Date',
			default:"Today",
			change: function () {
				frappe.UpdateFlight.get_flight_update_on_page(wrapper, page)
			}
		});
	}, 


	get_flight_update_on_page:function(wrapper, page){
		$(wrapper).find(".cards").empty();
		this.wrapper = $(wrapper).find('.cards');
		this.wrapper.append(
			`<div class="row"><div>`
		)
		frappe.call({
			method:"certification.certification.page.update_gate_no_of_flights.api.get_flight_details",
			args:{
				'date': this.posting_date_field.get_value(),
			},
			callback:r=>{
				$(wrapper).find(".cards").empty();
				this.wrapper = $(wrapper).find('.cards');
				this.wrapper.append(
					`<div class="row"><div>`
				)
				r.message.forEach( e => {
					this.add_small_cards(wrapper, e)
					$("."+ e.name).on('click', ()=> {
						this.update_gate_no(e.name)	
					})
				});
			}
		})
	},


	add_small_cards:function(wrapper, e){
		this.wrapper = $(wrapper).find(".cards").find(".row")
		this.wrapper.append(
			`
			<div class="flight-card col-3" style="border : 2px;">
				<h4>${e.name}</h4>
				<p><b>Airline:</b> ${e.airplane} </p>
				<p><b>Date of Departure:</b> ${e.date_of_departure}</p>
				<p><b>Time of Departure:</b> ${e.time_of_departure}</p>
				<label for=${e.name}>Gate No:</label>
   				<input type="text" id=${e.name} class=${e.name} name=${e.name} value=${e.gate_no || ''}>
				<button class="btn btn-primary ${e.name}" >Update Gate Number</button>
			</div>
			`
		)
		
	},

	update_gate_no:function(name){
		console.log("update_gate_no")
		var inputValue = $('.' + name).val();
		frappe.call({
			method : "certification.certification.page.update_gate_no_of_flights.api.update_get_no",
			args : {
				"name" : name,
				"gate_no" : inputValue
			}
		})
	},

	change_detail_on_change_of_date:function (wrapper, page){
		$(wrapper).find(".cards").empty();
		frappe.call({
			method:"certification.certification.page.update_gate_no_of_flights.api.get_flight_details",
			args:{
				'date': page.posting_date_field.get_value(),
			},
			callback:r=>{
				r.message.forEach( e => {
					add_small_cards(wrapper, e)
					$("."+ e.name).on('click', ()=> {
						this.update_gate_no(e.name)	
					})
				});
			}
		})
	}
}
