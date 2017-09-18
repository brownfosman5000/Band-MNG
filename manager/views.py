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
		songform = forms.SongForm(request.POST)
		bandform = forms.BandForm(request.POST)
		bandmembersform = forms.BandMembersForm(request.POST)		

		#check each form for validity				
		if showform.is_valid() and setlistform.is_valid() and songform.is_valid() and bandform.is_valid() and bandmembersform.is_valid():
			#save the shows info		
			show = showform.save()
			
			#need to process the null fields
			setlist = setlistform.save(commit=False)
			band = bandform.save(commit=False)
			
			song = songform.save(commit=False)
			bandmembers = bandmembersform.save(commit=False)
				
			#connect them together	
			setlist.show = show
			setlist.save()
			
			song.setlist = setlist


			band.show = show
			band.save()
		
			bandmembers.band = band

			song.save()
			bandmembers.save()

			return render(request,"manager/success.html")





		#return a bandform with content with incomplete fields
		else:
			return render(request,"manager/addband.html",
				{"showform" : showform,
				"setlistform" : setlistform,	
				"songform" : songform,
				"bandform" : bandform,
				"bandmembersform" : bandmembersform}
			)


	else:	
		#make empty forms
		showform = forms.ShowTrackerForm()		
		setlistform = forms.SetlistForm()
		songform = forms.SongForm()
		bandform = forms.BandForm()
		bandmembersform = forms.BandMembersForm()		
		
		#render those empty forms
		return render(request,"manager/addband.html",
				{"showform" : showform,
				"setlistform" : setlistform,	
				"songform" : songform,
				"bandform" : bandform,
				"bandmembersform" : bandmembersform}
			)


def success(request):
	return render(request,"manager/success.html")



def deleteBand(request):
	return render(request,"manager/deleteband.html")

def displayBand(request,showtracker_id):
	showtracker = models.ShowTracker.objects.get(id=showtracker_id)
	
	context = {'showtracker' : showtracker}
	return render(request,"manager/displayband.html",context)






