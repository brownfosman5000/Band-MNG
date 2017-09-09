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

		#showform = forms.ShowTrackerForm(request.POST)
		#setlistform = forms.SetlistForm(request.POST)
		#song = forms.SongForm(request.POST)
		#band = forms.BandForm(request.POST)
		#bandmembers = forms.BandMembersForm(request.POST)		
		Band =forms.Band(request.POST)

				
		if Band.is_valid():
			showform.save()
	        	return HttpResponseRedirect("/success")		
	else:
		band = forms.Band()		
		return render(request,"manager/addband.html" ,{"form" : Band})


def success(request):
	return render(request,"manager/success.html")
