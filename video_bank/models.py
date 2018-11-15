# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

from django.contrib.auth.models import User
from userena.models import UserenaBaseProfile\

from django.utils.translation import ugettext_lazy as _

from autoslug import AutoSlugField

from parler.models import TranslatableModel, TranslatedFields

# Create your models here.

class MovieGenre(models.Model):
    label = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="label", unique=True, always_update=True)

    def __unicode__(self):
        return "%s" % (self.label)


class Movie(TranslatableModel):
    translation = TranslatedFields(
        title = models.CharField(verbose_name=_("title"), max_length=500),
        slug = AutoSlugField(populate_from="title",verbose_name=_("slug"), unique=True, always_update=True),
        country = models.CharField(verbose_name=_("country"),max_length=100),
        synopsis = models.TextField(verbose_name=_("synopsis"),),
        trailer_url = models.URLField(verbose_name=_("trailer_url"),blank=True)

        )
    actors = models.CharField(verbose_name=_("actors"),max_length=500)
    director = models.CharField(verbose_name=_("director"),max_length=100)
    length = models.CharField(verbose_name=_("length"),max_length=50)
    picture = models.ImageField(upload_to='movie_picture', verbose_name=_("picture"),default="/no-image-icon-4.png")
    release_date = models.DateField(verbose_name=_("release_date"),)
    rented = models.BooleanField(verbose_name=_("rented"),default=False)
    genre = models.ManyToManyField("MovieGenre",verbose_name=_("genre"), blank=True)

    def __unicode__(self):
        return "%s release %s " %(self.title, self.release_date)

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


