# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from MovieBox.models import Movie, Actor, MBUserProfile
from MovieBox.forms import MovieForm, LoginForm, ActorForm, SignUpForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseForbidden

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

class UserProfileDetailView(DetailView):
    template_name = 'profile.html'
    model = MBUserProfile
    context_object_name = 'mbuserprofile'

class ActorCreateView(CreateView):
    template_name = 'add_actor.html'
    form_class = ActorForm
    model = Actor

    def get_success_url(self, *args, **kwargs):
        return reverse('actor_detail', kwargs={'pk': self.object.pk})

class UserCreateView(CreateView):
    template_name = "signup.html"
    form_class = SignUpForm
    model = MBUserProfile

    def get_success_url(self, *args, **kwargs):
        return reverse('home')

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

class AddedScoreView(View):
     def get(self, request, *args, **kwargs):
        obj = Movie.objects.get(pk=kwargs['pk'])
        votedScore = float(kwargs['value'])
        if request.user not in obj.votes.all():
            nr = int(obj.votes.count())
            obj.score = str(format((float(obj.score) * nr + votedScore) / (nr + 1), '.2f'))
            obj.votes.add(request.user)
            obj.save()
            return render( request, 'voted.html', {'response': 'Thank you for your vote!'})
        else:
            return render( request, 'voted.html', {'response': 'You gave already voted for this movie'})

def upload_pic(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            m = Movie.objects.get(pk=request.Movie.pk)
            m.cover = form.cleaned_data['cover']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')