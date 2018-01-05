# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class FrontPageMovieListView(ListView):
	template_name = 'homeMovieList.html'
	model = Movie
	context_object_name = 'movies'

class MovieDetailView(DetailView):
	template_name = 'movie.html'
	model = Movie
	context_object_name = 'movie'
