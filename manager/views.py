# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import forms
import models
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
	
	return render(request,"manager/home.html")

def addBand(request):
	if request.method == "POST":
		#send info from post to forms
		showform = forms.ShowTrackerForm(request.POST)
		setlistform = forms.SetlistForm(request.POST)
		songformset = forms.SongForm.SongFormSet(request.POST)
		bandform = forms.BandForm(request.POST)
		bandmembersformset = forms.BandMembersForm.BandMembersFormSet(request.POST)		

		#check each form for validity				
		if showform.is_valid() and setlistform.is_valid() and songformset.is_valid() and bandform.is_valid() and bandmembersformset.is_valid():
			#save the shows info		
			show = showform.save()
			
			#need to process the null fields
			setlist = setlistform.save(commit=False)
			band = bandform.save(commit=False)
			
			songs = songformset.save(commit=False)
			bandmembers = bandmembersformset.save(commit=False)
				
			#connect them together	
			setlist.show = show
			setlist.save()
				


			band.show = show
			band.save()
			for bandmember in bandmembers:
				bandmember.band = band
				bandmember.save()

			for song in songs:	
				song.setlist = setlist
				song.save()
	


			return render(request,"manager/success.html")





		#return a bandform with content with incomplete fields
		else:
			return render(request,"manager/addband.html",
				{"showform" : showform,
				"setlistform" : setlistform,	
				"songformset" : songformset,
				"bandform" : bandform,
				"bandmembersformset" : bandmembersformset}
			)


	else:	
		#make empty forms
		showform = forms.ShowTrackerForm()		
		setlistform = forms.SetlistForm()
		songformset = forms.SongForm.SongFormSet()
		bandform = forms.BandForm()
		bandmembersformset = forms.BandMembersForm.BandMembersFormSet()		
		
		#render those empty forms
		return render(request,"manager/addband.html",
				{"showform" : showform,
				"setlistform" : setlistform,	
				"songformset" : songformset,
				"bandform" : bandform,
				"bandmembersformset" : bandmembersformset}
			)


def success(request):
	return render(request,"manager/success.html")



def deleteBand(request):
	bands = models.Band.objects.all()
	context = {'bands': bands}
	return render(request,"manager/deleteband.html",context)

def displayBand(request):
	
	bands = models.Band.objects.all();
	context = {'bands': bands}
	return render(request,"manager/displayband.html",context)






