from django import forms
from .models import ShowTracker,Band

class BandForm(forms.ModelForm):
	class Meta:
		model = Band
		exclude = ["user"]


class ShowTrackerForm(forms.ModelForm):
	class Meta:
		model = ShowTracker	
		exclude =["user"]	

	def __init__(self,*args,**kwargs):
		print kwargs
		#Get the user
		self.user = kwargs.pop('user')
		#Call base init
		super(ShowTrackerForm,self).__init__(*args,**kwargs)
		#filter for bands of a specific user
		self.fields['band'].queryset = Band.objects.filter(user=self.user)
		# print  Band.objects.filter(user=self.user)

	def save(self, commit=True):
		inst = super(ShowTrackerForm, self).save(commit=False)
		inst.user = self.user
		print self.user
		if commit:
			inst.save()
			self.save_m2m()
		return inst
        #  = self._user
        # if commit:
        #     inst.save()
        #     self.save_m2m()
        # return inst
# class SetlistForm(forms.ModelForm):
# 	class Meta:
# 		model = Setlist	
# 		exclude = ("show",)		
	

# class SongForm(forms.ModelForm):
# 	class Meta:
# 		model = Song
# 		exclude = ("setlist",)
# 	# Max num of songs is 2 subject to change to variable
# 	#SongFormSet = forms.modelformset_factory(Song,fields=('song',),extra=4)



# class BandMembersForm(forms.ModelForm):
# 	class Meta:
# 		model = BandMembers
# 		exclude = ("band",)
	
	# Max num of songs is 2 subject to change to variable
	#BandMembersFormSet = forms.modelformset_factory(BandMembers,fields=('nameofbandmember','instrument',),max_num=2,extra=10)
