# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from MovieBox.models import Movie, MBUser, Actor, MBUserProfile
from MovieBox.forms import MovieForm

# Create your views here.

class FrontPageMovieListView(ListView):
    template_name = 'homeMovieList.html'
    model = Movie
    context_object_name = 'movies'

class MovieDetailView(DetailView):
    template_name = 'movie.html'
    model = Movie
    context_object_name = 'movie'

class ActorDetailView(DetailView):
    template_name = 'actor.html'
    model = Actor
    context_object_name = 'actor'

class MovieDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Movie

class MovieCreateView(CreateView):
    template_name = 'form.html'
    form_class = MovieForm
    model = Movie

    def get_success_url(self, *args, **kwargs):
        return reverse('movie_detail', kwargs={'pk': self.object.pk})


class MovieUpdateView(UpdateView):
    template_name = 'form.html'
    form_class = MovieForm
    model = Movie

    def get_success_url(self, *args, **kwargs):
        return reverse('movie_detail', kwargs={'pk': self.object.pk})