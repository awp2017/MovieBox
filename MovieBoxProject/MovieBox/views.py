# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView

# Create your views here.

class FrontPageMovieListView(ListView):
	template_name = 'homeMovieList.html'
	model = Movie
	context_object_name = 'movies'