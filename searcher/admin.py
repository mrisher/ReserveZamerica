from django.contrib import admin
from searcher.models import CampgroundQuery
from searcher.models import Campground
from searcher.models import DayOfWeek
from forms import CampgroundQueryAdminForm

class CampgroundQueryAdmin(admin.ModelAdmin):
	form = CampgroundQueryAdminForm

admin.site.register(Campground)

admin.site.register(CampgroundQuery, CampgroundQueryAdmin)

admin.site.register(DayOfWeek)
