from django import forms
from django.urls import reverse, reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from parler.views import TranslatableSlugMixin

from .models import Movie , Customer


class MovieCreateView(CreateView):
    model = Movie
    fields = "__all__"

    def get_success_url(self):
        return reverse('movie_detail', args=[self.object.slug])


class MovieUpdate(TranslatableSlugMixin, UpdateView):
    model = Movie
    fields = "__all__"

    def get_success_url(self):
        return reverse('movie_detail', args=[self.object.slug])


class MovieRemoveView(DeleteView):
    model = Movie
    success_url = reverse_lazy('index')


class CustomerCreateView(CreateView):
    model = Customer
    fields = "__all__"

    # def get_success_url(self):
    #     return reverse('customer_detail', args=[self.object.slug])
