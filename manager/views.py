# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import forms
# Create your views here.

def home(request):
	return render(request,"manager/home.html")

def addBand(request):
	#if request.method == "POST":
	
	showform = forms.ShowTrackerForm(request.POST)
		
		#if showform.isValid():
	        	#HttpResponseRedirect("infostored")		
	
	return render(request,"manager/addband.html" ,{"form" : showform})
