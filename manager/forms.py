from django import forms
from django.forms import inlineformset_factory
from .models import ShowTracker,Setlist,Song,Band,BandMembers
#Form for ShowTracker
class ShowTrackerForm(forms.ModelForm):
	class Meta:
		model = ShowTracker	
		fields ="__all__"	
class SetlistForm(forms.ModelForm):
	class Meta:
		model = Setlist	
		exclude = ("show",)		
	

class SongForm(forms.ModelForm):
	class Meta:
		model = Song
		exclude = ("setlist",)

class BandForm(forms.ModelForm):
	class Meta:
		model = Band
		exclude = ("show",)

class BandMembersForm(forms.ModelForm):
	class Meta:
		model = BandMembers
		exclude = ("band",)


