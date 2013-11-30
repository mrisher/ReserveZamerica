from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
import requests
import cgi
from searcher.models import CampgroundQuery

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
	params = {
		'parkId': c.campground.park_id,
		'arvdate': c.start_date.strftime("%x"),
		'lengthOfStay': c.stay_length,
		'contractCode': 'CA',
		'siteType': 10001,
		'api_key': '3vtcjh2jfsnh78z7bjbfkdmj'}
	req = requests.get("http://api.amp.active.com/camping/campsites/", params=params)
	return HttpResponse("You have executed CampgroundQuery %s with URL %s<br><pre>%s</pre>" % 
		(campgroundquery_id, req.url, cgi.escape(req.text)))
