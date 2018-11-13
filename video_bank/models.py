# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

from django.contrib.auth.models import User
from userena.models import UserenaBaseProfile\

from django.utils.translation import ugettext_lazy as _

from autoslug import AutoSlugField

# Create your models here.

class MovieGenre(models.Model):
    label = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="label", unique=True, always_update=True)

    def __unicode__(self):
        return "%s" % (self.label)


class Movie(models.Model):
    title = models.CharField(verbose_name=_('titre'), max_length=500)
    slug = AutoSlugField(populate_from="title",verbose_name=_('slug'), unique=True, always_update=True)
    synopsis = models.TextField(verbose_name=_('synopsis'),)
    actors = models.CharField(verbose_name=_('acteurs'),max_length=500)
    country = models.CharField(verbose_name=_('pays'),max_length=100)
    director = models.CharField(verbose_name=_('realisateur'),max_length=100)
    length = models.CharField(verbose_name=_('duree'),max_length=50)
    picture = models.ImageField(upload_to='movie_picture', verbose_name=_('image'),default="/no-image-icon-4.png")
    release_date = models.DateField(verbose_name=_('date de sortie'),)
    rented = models.BooleanField(verbose_name=_('louer'),default=False)
    genre = models.ManyToManyField("MovieGenre",verbose_name=_('genre'), blank=True)
    trailer_url = models.URLField(verbose_name=_('bande annonce'),blank=True)

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

MovieRent.objects.order_by("-date")
