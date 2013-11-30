from django.conf.urls import patterns, url
from searcher import views

urlpatterns = patterns('', 
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<campgroundquery_id>\d+)/execute/$', views.execute, name='execute'),
)
