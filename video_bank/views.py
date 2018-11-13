# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import datetime
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import View
from django.views.generic import ListView, DetailView, CreateView


from .models import MovieGenre, Movie, Customer, MovieRent
from .forms import *
# Create your views here.


class IndexView(ListView):
    model = Movie


class MovieDetailView(DetailView):
    model = Movie


class CustomerHistoricView(ListView):
    model = MovieRent

    def get_queryset(self, **kwargs):
        currentCustomer = Customer.objects.get(id=self.request.user.id)
        return MovieRent.objects.filter(customer=currentCustomer)


class MovieRentView(View):

     def post(self, request, **kwargs):
        customer_id =  request.POST.get('customer_id')
        movie_id =  request.POST.get('movie_id')
        rent_status =  request.POST.get('status_rent')
        now = datetime.datetime.now()
        end_rent = now + datetime.timedelta(days=7)

        customer = Customer.objects.get(id=customer_id)
        movie = Movie.objects.get(id=movie_id)
        movie_rent = movie.movierent_set.create(customer=customer,movie=movie,checkout_date=now,return_date=end_rent)

        print repr(rent_status)
        movie.rented = True
        movie.save()

        return JsonResponse({"rentStatus" : "html"})
