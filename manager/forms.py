from django import forms
from django.forms import inlineformset_factory
import models

#Form for ShowTracker
class ShowTrackerForm(forms.ModelForm):
	class Meta:
		model = models.ShowTracker	
		fields ="__all__"	
class SetlistForm(forms.ModelForm):
	class Meta:
		model = models.Setlist	
		
	

class SongForm(forms.ModelForm):
	class Meta:
		model = models.Song
		fields = ('song',)

class BandForm(forms.ModelForm):
	class Meta:
		model = models.Band
		fields = ('nameofband',)

class BandMembersForm(forms.ModelForm):
	class Meta:
		model = models.BandMembers
		fields = ('nameofbandmember',)

	
