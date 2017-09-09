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
		showform = forms.ShowTrackerForm(request.POST)
		
		if showform.is_valid():
			showform.save()
	        	return HttpResponseRedirect("infostored")		
	else:
		showform = forms.ShowTrackerForm()		
		return render(request,"manager/addband.html" ,{"form" : showform})
