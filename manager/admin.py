# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from manager.models import ShowTracker,Setlist,BandMembers

# Register your models here.

admin.site.register(ShowTracker)
admin.site.register(Setlist)
admin.site.register(BandMembers)
