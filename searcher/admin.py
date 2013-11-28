from django.contrib import admin
from searcher.models import Query
from forms import QueryAdminForm

class QueryAdmin(admin.ModelAdmin):
	#list_display = ('campground_id', 'stay_length', 'days', 'start_date', 'end_date')
	form = QueryAdminForm

admin.site.register(Query, QueryAdmin)
