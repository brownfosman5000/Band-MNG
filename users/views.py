# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def homesigned(request):
	return render(request,"registration/home.html")
def register(request):

	if request.method != "POST":
		registerform = UserCreationForm()


	else:
		print request.POST
		registerform = UserCreationForm(request.POST)

		if registerform.is_valid():
			new_user = registerform.save()

			new_user = authenticate(username=new_user.username,password=request.POST['password2'])
			login(request,new_user)
			return render(request,"manager/home.html")

	context = {"registerform" : registerform}

	return render(request,"registration/register.html",context)


