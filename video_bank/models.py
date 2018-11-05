# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

from django.contrib.auth.models import User
from userena.models import UserenaBaseProfile

from autoslug import AutoSlugField

# Create your models here.

class MovieGenre(models.Model):
    label = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="label", unique=True, always_update=True)

    def __unicode__(self):
        return "%s" % (self.label)


class Movie(models.Model):
    title = models.CharField(max_length=500)
    slug = AutoSlugField(populate_from="title", unique=True, always_update=True)
    synopsis = models.TextField()
    actors = models.CharField(max_length=500)
    country = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    length = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='movie_picture',blank=True)
    release_date = models.DateField()
    rented = models.BooleanField(default=False)
    genre = models.ManyToManyField("MovieGenre", blank=True)
    trailer_url = models.URLField()

    def __unicode__(self):
        return "%s release %s" %(self.title, self.release_date)

class Customer(UserenaBaseProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return "%s" %(self.user)


class MovieRent(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True)
    movie = models.ForeignKey(Movie, null=True, blank=True)
    checkout_date = models.DateTimeField()
    return_date = models.DateTimeField()
