# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import pdb

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
		bandform = forms.BandForm(request.POST)

		#check each form for validity				
		if showform.is_valid() and bandform.is_valid():	
			show = showform.save()
			band = bandform.save(commit=False)
			band.show = show
			band.save()


			return render(request,"manager/success.html")





		#return a bandform with content with incomplete fields
		else:
			return render(request,"manager/addband.html",
				{
				"showform" : showform,
				"bandform" : bandform,
				}
			)


	else:	
		#make empty forms
		showform = forms.ShowTrackerForm()		
		bandform = forms.BandForm()
		
		
		#render those empty forms
		return render(request,"manager/addband.html",
				{
				"showform" : showform,
				"bandform" : bandform,
				}
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

def deletesuccessful(request):
	return render(request,"manager/deletesuccessful.html")








