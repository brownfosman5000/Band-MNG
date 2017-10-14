# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import pdb

import forms
import models
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
	return render(request,"manager/index.html")

def home(request):
	
	return render(request,"manager/home.html")

#Adds a new band object
def addBand(request):
	if request.method == "POST":
		#send info from post to forms
		bandform = forms.BandForm(request.POST)

		#check each form for validity				
		if bandform.is_valid():	
			bandform.save()
			return render(request,"manager/home.html")
		else:
			return render(request,"manager/addband.html",{"bandform" : bandform})
	else:	
		#make empty forms	
		bandform = forms.BandForm()
		#render those empty forms
		return render(request,"manager/addband.html",{"bandform" : bandform})

#Adds a new show object that connects to a band object
def addshow(request):
	if request.method == "POST":
			showform = forms.ShowTrackerForm(request.POST)
			if showform.is_valid():
				showform.save()
				return render(request, "manager/home.html")
			else:
				return render(request, "manager/addshow.html",{"showform":showform})

	else:
		showform = forms.ShowTrackerForm()
		return render(request, "manager/addshow.html",{"showform":showform})




def success(request):
	return render(request,"manager/success.html")




def displayband(request):
	bands = models.Band.objects.all()
	context = {'bands': bands}
	return render(request,"manager/displayband.html",context)



def displayshows(request,pk):

	#Based off of band we chose it has the val of pk and we set that band_id equal to that
	#So we display the right shows associated with that particular band
	shows = models.ShowTracker.objects.filter(band_id=pk)
	#Take the pk of the band selected and set it equal to our id
	band = models.Band.objects.get(id=pk)

	context = {'shows': shows,'band' : band,'bandid' : pk}

	return render(request,"manager/displayshows.html",context)


#Called as a part of the displayshow template if delete button was clicked
def deleteshow(request,pk):
	show = models.ShowTracker.objects.get(pk=pk)

	#Must use this button because we have to get info related to that specific band
	#Best way to do it as of right now
	print request.POST
	bandid = request.POST.get(pk)
	shows = models.ShowTracker.objects.filter(band_id=bandid)
	band = models.Band.objects.get(id=bandid)

	print "DELTETED"
	#show.delete()

	return render(request,"manager/displayshows.html",{"shows":shows,"band":band})



#Called as a part of the displayshow template if edit button was clicked
def editshow(request,pk):
	show = models.ShowTracker.objects.get(pk=pk)
	bandid = request.POST.get(pk)


	shows = models.ShowTracker.objects.filter(band_id=bandid)
	band = models.Band.objects.get(id=bandid)
	showform = forms.ShowTrackerForm(request.POST)


	context = {"shows":shows,"band":band, "showform":showform,"showid" : pk}

	if showform.is_valid():
		print "was valid"
		showform.save()
		return render(request,"manager/displayshows.html",context)
	
	return render(request,"manager/displayshows.html",context)







#Called as a part of the displayband template if delete button was clicked
def deleteband(request,pk):
	bands = models.Band.objects.all()
	context = {'bands': bands}
	deleteid = request.POST.get("DeleteButton")


	if deleteid:
		models.Band.objects.get(pk=pk).delete()

	return render(request,"manager/displayband.html",context)


#Called as a part of the displayband template if edit button was clicked
def editband(request,pk):
	bands = models.Band.objects.all()
	editid = request.POST.get("EditButton")
	bandedit = models.Band.objects.get(pk=pk)
	data = {"bandname" : models.Band.objects.get(id=pk).nameofband}
	print data
	context = {'bands': bands}
	bandform = forms.BandForm(request.POST,instance = bandedit)
	contextwithform = {"bands" : bands, "editid" : editid,"bandform" : bandform}

	if bandform.is_valid():
		print "Was Valid"
		bandform.save()
		return render(request,"manager/displayband.html",context)
	else:
		print "wasn't valid"
		return render(request,"manager/displayband.html",contextwithform)






def calandar(request):
	shows = models.ShowTracker.objects.all();
	context = {'shows':shows}
	return render(request,"manager/calandar.html",context)





def deletesuccessful(request):
	return render(request,"manager/deletesuccessful.html")











