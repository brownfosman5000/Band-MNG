from django import forms
from models import ShowTracker


#Form for ShowTracker
class ShowTrackerForm(forms.ModelForm):
	class Meta:
		model = ShowTracker	
		fields ="__all__"	
		

