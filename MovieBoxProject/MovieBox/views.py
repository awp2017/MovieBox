# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from MovieBox.models import Movie, MBUser, Actor, MBUserProfile
from MovieBox.forms import MovieForm, LoginForm
from django.contrib.auth import authenticate, login, logout

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
    template_name = 'add_movie.html'
    form_class = MovieForm
    model = Movie

    def get_success_url(self, *args, **kwargs):
        return reverse('movie_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(MovieCreateView, self).get_context_data(**kwargs)
        context['actors'] = Actor.objects.all()
        return context

class MovieUpdateView(UpdateView):
    template_name = 'edit_movie.html'
    form_class = MovieForm
    model = Movie

    def get_success_url(self, *args, **kwargs):
        return reverse('movie_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(MovieUpdateView, self).get_context_data(**kwargs)
        actors = Actor.objects.all()
        for actor in actors:
            actor.movies_pk = [pk for pk in actor.Movies.values_list('pk', flat=True)]
        context['actors'] = actors
        context['movie_pk'] = self.object.pk
        return context


#afisare mesaj de eroare daca username-ul sau parola nu sunt valide
def login_view(request):
    context = {}
    if request.method == 'GET':
        form = LoginForm()
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                login(request=request,
                      user=user)
                return redirect('home')
            else:
                context['error_message'] = 'Wrong username or password!'
    context['form'] = form
    return render(request, 'login.html', context)


def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')

class SearchPageListView(ListView):
    template_name = 'search.html'
    model = Movie
    context_object_name = 'items'
    def get_queryset(self):
        searchInput = self.kwargs['input']
        queryset = Movie.objects.filter(name__contains=searchInput).all()
        return queryset

