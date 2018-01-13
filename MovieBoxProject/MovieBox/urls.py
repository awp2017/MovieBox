"""courseproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from MovieBox import views

urlpatterns = [
	url(r'^$', views.FrontPageMovieListView.as_view(), name = 'home'),
    url(r'^actor/add/$', views.ActorCreateView.as_view(), name='actor_create'),
    url(r'^actor/(?P<pk>[0-9]+)/$', views.ActorDetailView.as_view(), name='actor_detail'),
    url(r'^movie/(?P<pk>[0-9]+)/$', views.MovieDetailView.as_view(), name = 'movie_detail'),
    url(r'^movie/(?P<pk>[0-9]+)/delete$',  views.MovieDeleteView.as_view(), name='movie_delete'),
    url(r'^movie/add/$', views.MovieCreateView.as_view(), name='movie_create'),
    url(r'^movie/(?P<pk>[0-9]+)/update$', views.MovieUpdateView.as_view(), name='movie_update'),
    url(r'^movie/(?P<pk>[0-9]+)/voted/(?P<value>[0-5])/$', views.AddedScoreView.as_view(), name='voted'),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^search/(?P<input>[A-Za-z]+)/$', views.SearchPageListView.as_view(), name="search"),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.UserProfileDetailView.as_view(), name='profile'),
    url(r'^register/$', views.UserCreateView.as_view(), name="register"),
]
