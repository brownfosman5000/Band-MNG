# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import forms
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
		if showform.is_valid():
			showform.save()

		if setlistform.is_valid():   			
			setlistform.save()

		if songform.is_valid():
			songform.save()

		if bandform.is_valid():
			bandform.save()

		if bandmembersform.is_valid():	
			bandmembersform.save()
			return HttpResponseRedirect("/success")		
		
		#return a bandform with content with incomplete fields
		else:
			return render(request,"manager/addband.html" ,{"showform" : showform,"setlistform" : setlistform,"setlistform" : setlistform ,"songform" : songform,"bandform" : bandform,"bandmembersform" : bandmembersform})

	else:	
		#make empty forms
		showform = forms.ShowTrackerForm()		
		setlistform = forms.SetlistForm()
		songform = forms.SongForm()
		bandform = forms.BandForm()
		bandmembersform = forms.BandMembersForm()		
		
		#render those empty forms
		return render(request,"manager/addband.html" ,{"showform" : showform,"setlistform" : setlistform,"setlistform" : setlistform ,"songform" : songform,"bandform" : bandform,"bandmembersform" : bandmembersform})



def success(request):
	return render(request,"manager/success.html")
