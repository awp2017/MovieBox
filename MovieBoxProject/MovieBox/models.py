# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class MBUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length = 100)


class Actor(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    picture =  models.CharField(max_length=200, default='actor-defaul.jpg')

    def __str__(self):
        return self.last_name + " " + self.first_name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.DateField()
    genre = models.IntegerField(choices=[
        (1, "Comedy"),
        (2, "Action"),
        (3, "Thriller"),
        (4, "Drama"),
        (5, "Horror"),
        (6, "Romance"),
        (7, "Fantasy"),
        (8, "Sci-Fi"),
    ])
    score = models.FloatField(default=0.0)
    cover =  models.CharField(max_length=200, default='')

    actors = models.ManyToManyField(Actor, related_name='Movies')

    # verifica daca un user a votat pentru filmul respectiv
    votes = models.ManyToManyField(User, blank=True, related_name='UserMovie')


    def __str__(self):
        return self.name


class MBUserProfile(models.Model):
    user = models.OneToOneField(MBUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date =  models.DateTimeField(null=True, blank=True)
    profile_pic =  models.CharField(max_length=200)
    favourites = models.ManyToManyField(Movie, related_name='Favourites')

    def __str__(self):
        return self.first_name + " " + self.last_name
