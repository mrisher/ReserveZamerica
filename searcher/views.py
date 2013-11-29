from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from searcher.models import CampgroundQuery

def index(request):
	latest_campgroundquery_list = CampgroundQuery.objects.order_by('-start_date')[:5]
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
	return HttpResponse("You have executed CampgroundQuery %s" % campgroundquery_id)
