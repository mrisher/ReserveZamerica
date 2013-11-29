from django.db import models
from django.core.exceptions import ValidationError

class DayOfWeek(models.Model):
	name = models.CharField(max_length=10)
	def __unicode__(self):
		return self.name

class Campground(models.Model):
	campground_name = models.CharField(max_length=100)
	park_id = models.SmallIntegerField()
	def __unicode__(self):
		return self.campground_name

class CampgroundQuery(models.Model):
	# loads choices from defined list
	eligible_days = models.ManyToManyField('DayOfWeek')
	campground = models.ForeignKey('Campground')
	stay_length = models.SmallIntegerField()
	start_date = models.DateField()
	end_date = models.DateField()
	last_query = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return (self.campground.campground_name + '-' + 
			self.end_date.strftime('%x'))


class Result(models.Model):
	data = models.TextField('response data')

