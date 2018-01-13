# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from MovieBox.models import Movie, Actor, MBUserProfile

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(MBUserProfile)
