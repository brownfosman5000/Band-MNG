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

		bandform = forms.BandForm(request.POST)

		#check each form for validity				
		if bandform.is_valid():	
			bandform.save()
			return render(request,"manager/success.html")
		else:
			return render(request,"manager/addband.html",{"bandform" : bandform})
	else:	
		#make empty forms	
		bandform = forms.BandForm()
		#render those empty forms
		return render(request,"manager/addband.html",{"bandform" : bandform})

	
def addshow(request):
	if request.method == "POST":
			showform = forms.ShowTrackerForm(request.POST)
			if showform.is_valid():
				showform.save()
				return render(request, "manager/success.html")
			else:
				return render(request, "manager/addshow.html",{"showform":showform})

	else:
		showform = forms.ShowTrackerForm()
		return render(request, "manager/addshow.html",{"showform":showform})


def success(request):
	return render(request,"manager/success.html")



def deleteBand(request):
	bands = models.Band.objects.all()
	context = {'bands': bands}
	return render(request,"manager/deleteband.html",context)

def displayBand(request):
	
	shows = models.ShowTracker.objects.all();

	context = {'shows':shows}
	return render(request,"manager/displayband.html",context)

def deletesuccessful(request):
	return render(request,"manager/deletesuccessful.html")









