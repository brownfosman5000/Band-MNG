# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.

#Keeps track of dates times and names of shows
class ShowTracker(models.Model):
        datetime = models.DateTimeField()
        venue = models.CharField(max_length=50,null=True)

        def __unicode__(self):
                return self.venue or u''

class Setlist(models.Model):
        show = models.ForeignKey(ShowTracker)
        song = models.CharField(max_length=50,null=True)

        def __unicode__(self):
                return self.song or u''

class BandMembers(models.Model):
	show = models.ForeignKey(ShowTracker)
	member = models.CharField(max_length=50,null=True)	
	
	
class CashOrCheck(models.Model):
	bandmember = models.ForeignKey(BandMembers)
	



	





