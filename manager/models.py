# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

#Keeps track of dates times and names of shows
class ShowTracker(models.Model):
        datetime = models.DateTimeField()
        venue = models.CharField(max_length=50,null=True)

        def __unicode__(self):
                return self.venue or u''

#For each show I want a setlist
##Key to ShowTracker
class Setlist(models.Model):
        show = models.ForeignKey(ShowTracker)
	nameofsetlist = models.CharField(max_length=50,null=True)

        def __unicode__(self):
                return self.nameofsetlist or u''

#For each setlist I want a song 
class Song(models.Model):
	setlist = models.ForeignKey(Setlist)
        song = models.CharField(max_length=50,null=True)
	
	def __unicode__(self):
		return self.song 
		

#For each show I want a group of bandmemebers
##Key to ShowTracker
class Band(models.Model):
	show = models.ForeignKey(ShowTracker)
	nameofband = models.CharField(max_length=50,null=True)	
	
	def __unicode__(self):	
		return self.nameofband or u''
	
class BandMembers(models.Model):
	band = models.ForeignKey(Band)
	nameofbandmember = models.CharField(max_length=50,null=True)
	instrument = models.CharField(max_length=50,null=True)	
	
	def __unicode__(self):
		return self.nameofbandmember or u''
	
#class CashOrCheck(models.Model):
	#bandmember = models.ForeignKey(BandMembers)
	



	





