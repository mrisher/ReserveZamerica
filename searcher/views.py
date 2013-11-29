from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("You are in the Searcher index")

def detail(request, campgroundquery_id):
	return HttpResponse("You are looking at CampgroundQuery %s" % campgroundquery_id)

def results(request, campgroundquery_id):
	return HttpResponse("You are looking at the results of CampgroundQuery %s" % campgroundquery_id)

def execute(request, campgroundquery_id):
	return HttpResponse("You have executed CampgroundQuery %s" % campgroundquery_id)
