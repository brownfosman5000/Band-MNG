from django import forms
from django.forms import DateTimeField,CharField


#Form for ShowTracker
class ShowTrackerForm(forms.Form):
	datetime = forms.DateTimeField()
	venue = forms.CharField(max_length=50)
	
	
		

