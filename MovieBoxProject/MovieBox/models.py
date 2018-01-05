# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class MBUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.CharField(max_length = 100)

class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.DateTimeField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Actor(models.Model):
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length=100)
	birth_date = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.last_name + " " + self.first_name
