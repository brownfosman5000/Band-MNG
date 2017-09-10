from django import forms
import models

#Form for ShowTracker
class ShowTrackerForm(forms.ModelForm):
	class Meta:
		model = models.ShowTracker	
		fields ="__all__"	
		
class SetlistForm(forms.ModelForm):
	class Meta:
		model = models.Setlist	
		fields ="__all__"

class SongForm(forms.ModelForm):
	class Meta:
		model = models.Song
		fields ="__all__"

class BandForm(forms.ModelForm):
	class Meta:
		model = models.Band
		fields = "__all__"

class BandMembersForm(forms.ModelForm):
	class Meta:
		model = models.BandMembers
		fields = "__all__"
	
