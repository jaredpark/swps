import os

os.environ.get('FACEBOOK')

def site_settings_processor(request):
	context_dictionary = {
		'root_url': '.yourwebsiteprogress.com',
		'admin_name': 'admin',
		'company_name': 'Shimmering Waters Pool Services',
		'company_short': 'SWPS',
		'logo_file_name': 'images/logo.jpg',
		'site_email': 'shimmeringwaterspoolservices@gmail.com',
		# if email changes, update misc_pages/email.html
		'company_phone_text': '602-363-8267',
		'company_phone_link': '16023638267',
		'company_fax': '',
		'company_address': '',
		'yelp_id': '',
		'meta_title': 'Shimmering Waters Pool Services',
		'meta_content': 'West Phoenix Area Pool Care Specialists.',
		'navbar_link1_name': 'home',
		'navbar_link1_text': 'Home',
		'navbar_link2_name': 'about',
		'navbar_link2_text': 'About',
		'navbar_link3_name': 'services',
		'navbar_link3_text': 'Services',
		'sublink1_name': 'weekly_service',
		'sublink1_text': 'Weekly Service',
		'sublink2_name': 'repair',
		'sublink2_text': 'Repairs',
		'sublink3_name': 'remodels',
		'sublink3_text': 'Remodels',
		'sublink4_name': 'tile_cleaning',
		'sublink4_text': 'Tile Cleaning',
		'sublink5_name': 'commercial',
		'sublink5_text': 'Commercial',
		'sublink6_name': 'services',
		'sublink6_text': 'All Services',
		'navbar_link4_name': 'contact',
		'navbar_link4_text': 'Contact',
	}
	return(context_dictionary)