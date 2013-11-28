from django import forms
from django.contrib import admin
from searcher.models import Query

class QueryAdminForm(forms.ModelForm):
	class Meta:
		model = Query
		widgets = {
			'eligible_days': forms.widgets.CheckboxSelectMultiple
		}

