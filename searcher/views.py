from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
import requests
import cgi
import datetime
import time
import xml.etree.ElementTree as ET
from datetime import date
from searcher.models import CampgroundQuery
#import pdb; pdb.set_trace()

# display the list of eligible queries
def index(request):
	latest_campgroundquery_list = CampgroundQuery.objects.filter(active=True).order_by('-start_date')[:5]
	template = loader.get_template('searcher/index.html')
	context = RequestContext(request, {
		'latest_campgroundquery_list': latest_campgroundquery_list,
	})
	return HttpResponse(template.render(context))

def detail(request, campgroundquery_id):
	try:
		campgroundquery = CampgroundQuery.objects.get(pk=campgroundquery_id)
	except CampgroundQuery.DoesNotExist:
		raise Http404
	return render(request, 'searcher/detail.html', {'campgroundquery': campgroundquery})

def results(request, campgroundquery_id):
	return HttpResponse("You are looking at the results of CampgroundQuery %s" % campgroundquery_id)

def execute(request, campgroundquery_id):
	c = get_object_or_404(CampgroundQuery, pk=campgroundquery_id)
	date_delta = datetime.timedelta(days=1)
	query_date = c.start_date
	eligible_days = c.eligible_days.values_list('date_code', flat=True)
	response = HttpResponse()
	response.write("<h1>Executing CampgroundQuery {0}</1>".format(campgroundquery_id))
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
				req = requests.get("http://api.amp.active.com/camping/campsites/", params=params)
				if req.status_code == requests.codes.ok:
					break
				else:
					time.sleep(1)	# delay to avoid hitting rate limit 
			response.write("<h2><a href='{0}' target='_blank'>{1}</a></h2> <!-- Return Status: {2}-->".format(req.url, query_date.strftime("%x (%a)"), req.status_code))
			response.write("<pre>{0}</pre>".format(cgi.escape(req.text))) 
			response.write("<h3>Parsed</h3>")
			response.write("<table>")
			response.write("<tr><td>site</td><td>site_id</td><td>status</td></tr>")
			for result in parse_xml(req.text):
				response.write("<tr><td>{0}</td><td>{1}</td><td>{2}</td></tr>".format(
					result['site'],
					result['site_id'],
					result['availability_status']))
			response.write("</table>")
		query_date += date_delta
	return response;

def parse_xml(xml_response):
	resultset = ET.fromstring(xml_response)
	result_list = []
	for result in resultset.findall('result'):
		result_list.append({
			'site': result.get('Site'),
			'site_id': result.get('SiteId'),
			'availability_status': result.get('availabilityStatus')})
	return result_list

