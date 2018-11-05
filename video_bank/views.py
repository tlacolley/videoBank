# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from django.db.models import Q

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import ListView, DetailView, CreateView


from .models import MovieGenre, Movie, Customer, MovieRent
from .forms import *
# Create your views here.


class IndexView(ListView):
    model = Movie


class MovieDetailView(DetailView):
    model = Movie
