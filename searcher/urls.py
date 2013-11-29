from django.conf.urls import patterns, url
from django.contrib import admin
from searcher import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^(?P<campgroundquery_id>\d+)/$', views.detail, name='detail'),
	url(r'^(?P<campgroundquery_id>\d+)/results/$', views.results, name='results'),
	url(r'^(?P<campgroundquery_id>\d+)/execute/$', views.execute, name='execute'),
)
