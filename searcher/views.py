from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext, loader
import requests
import cgi
import datetime
import time
import xml.etree.ElementTree as ET
from datetime import date
from searcher.models import CampgroundQuery
#import pdb; pdb.set_trace()

class IndexView(generic.ListView):
	template_name = 'searcher/index.html'
	context_object_name = 'latest_campgroundquery_list'

	def get_queryset(self):
		"""Return the last five active campground_query objects."""
		return CampgroundQuery.objects.filter(active=True).order_by('-start_date')[:5]

class DetailView(generic.DetailView):
	model = CampgroundQuery
	template_name = 'searcher/detail.html'

class ResultsView(generic.DetailView):
	model = CampgroundQuery
	template_name = 'searcher/detail.html'


def execute(request, campgroundquery_id):
	c = get_object_or_404(CampgroundQuery, pk=campgroundquery_id)
	date_delta = datetime.timedelta(days=1)
	query_date = c.start_date
	eligible_days = c.eligible_days.values_list('date_code', flat=True)
	query_list = []
	while query_date <= c.end_date:
		#isoweekday: Monday=1, Sunday=7
		if query_date > date.today() and query_date.isoweekday() in eligible_days:
			# run the query for this day
			params = {
				'parkId': c.campground.park_id,
				'arvdate': query_date.strftime("%x"),
				'lengthOfStay': c.stay_length,
				'contractCode': 'CA',
				'siteType': 10001,
				'api_key': '3vtcjh2jfsnh78z7bjbfkdmj'}
			for i in range(3):
				# Active.com returns 403 (Forbidden) if we exceed rate limit
				# So attempt up to 3 tries
				req = requests.get("http://api.amp.active.com/camping/campsites/", params=params)
				if req.status_code == requests.codes.ok:
					break
				else:
					time.sleep(1)	# delay to avoid hitting rate limit 
			query_list.append({
				'query_url': req.url,
				'query_results': parse_xml(req.text),
				'query_date': query_date,
			})		
		query_date += date_delta

	template = loader.get_template('searcher/results.html')
	context = RequestContext(request, {
		'query_desc': "{0} from {1} to {2}".format(c.campground, c.start_date, c.end_date),
		'query_set': query_list,
	})
	return HttpResponse(template.render(context))

def parse_xml(xml_response):
	resultset = ET.fromstring(xml_response)
	result_list = []
	for result in resultset.findall('result'):
		result_list.append({
			'site': result.get('Site'),
			'site_id': result.get('SiteId'),
			'availability_status': result.get('availabilityStatus')})
	return result_list

