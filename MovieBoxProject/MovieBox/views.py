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
