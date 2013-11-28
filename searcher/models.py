from django.db import models

class DaysOfWeek(models.Model):
	SUN = 0
	MON = 1
	TUE = 2
	WED = 3
	THU = 4
	FRI = 5
	SAT = 6

	DAYS_OF_WEEK_CHOICES = (
		(SUN, 'Sunday'),
		(MON, 'Monday'),
		(TUE, 'Tuesday'),
		(WED, 'Wednesday'),
		(THU, 'Thursday'),
		(FRI, 'Friday'),
		(SAT, 'Saturday'),
	)

class Query(models.Model):
	start_date = models.DateField()
	end_date = models.DateField()
	SUN = 0
	MON = 1
	TUE = 2
	WED = 3
	THU = 4
	FRI = 5
	SAT = 6

	DAYS_OF_WEEK_CHOICES = (
		(SUN, 'Sunday'),
		(MON, 'Monday'),
		(TUE, 'Tuesday'),
		(WED, 'Wednesday'),
		(THU, 'Thursday'),
		(FRI, 'Friday'),
		(SAT, 'Saturday'),
	)

	# loads choices from defined constant, but won't allow saving
	eligible_days = models.CharField(max_length=14,choices=DAYS_OF_WEEK_CHOICES,
		blank=False, default='Saturday')
	campground_id = models.SmallIntegerField()
	stay_length = models.SmallIntegerField()

class Result(models.Model):
	data = models.TextField('response data')

