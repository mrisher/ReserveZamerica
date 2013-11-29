from django import forms
from django.contrib import admin
from searcher.models import CampgroundQuery

class CampgroundQueryAdminForm(forms.ModelForm):
	class Meta:
		model = CampgroundQuery
		widgets = {
			'eligible_days': forms.widgets.CheckboxSelectMultiple
		}

