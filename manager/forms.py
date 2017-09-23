from django import forms
from .models import ShowTracker,Setlist,Song,Band,BandMembers

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
	# Max num of songs is 2 subject to change to variable
	SongFormSet = forms.modelformset_factory(Song,fields=('song',),max_num=2,extra=10)


class BandForm(forms.ModelForm):
	class Meta:
		model = Band
		exclude = ("show",)

class BandMembersForm(forms.ModelForm):
	class Meta:
		model = BandMembers
		exclude = ("band",)
	
	# Max num of songs is 2 subject to change to variable
	BandMembersFormSet = forms.modelformset_factory(BandMembers,fields=('nameofbandmember','instrument',),max_num=2,extra=10)

