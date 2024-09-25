frappe.pages['crew-member-status'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Crew Member Status',
		single_column: true
	});
	frappe.CrewMemberStatus.init(wrapper, page)
}


frappe.CrewMemberStatus = {
	init:function(wrapper, page){
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
	},
	setup_field:function(wrapper, page){
		this.flights_field = page.add_field({
			fieldname: 'flights',
			label: __('Flights'),
			fieldtype:'Link',
			options : "Airplane Flight",
			change: function () {
				frappe.CrewMemberStatus.get_flights_crew_member(wrapper, page)
			}
		})
	},
	get_flights_crew_member:function(wrapper, page){
		frappe.call({
			method:"certification.certification.page.crew_member_status.api.get_flights_crew_member",
			args:{
				"flight" : this.flights_field.get_value()
			},
			callback:(r)=>{
					$(wrapper).find(".cards").empty();
					this.wrapper = $(wrapper).find('.cards');
					this.wrapper.append(
						`<div class="row"><div>`
					)
					r.message.forEach( e => {
						this.add_small_cards(wrapper, e)
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
				<p><b>Airline:</b> ${e.full_name} </p>
				<p><b>Date of Birth:</b> ${e.date_of_birth}</p>
				<p><b>Seat No:</b> ${e.seat}</p>
				<p><b>Date of Departure:</b> ${e.departure_date}</p>
				<p><b>Time of Departure:</b> ${e.departure_time}</p>
				<p><b>Status: </b> ${e.status}</p>
			</div>
			`
		)
		
	},
		
}