"""videoBank URL Configuration

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
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect

from video_bank.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', IndexView.as_view(), name="index"),

    url(r'^movie/create/$', MovieCreateView.as_view(), name="movie_create"),
    url(r'^movie/(?P<slug>[\w-]+)/$', MovieDetailView.as_view(), name="movie_detail"),
    url(r'^movie/(?P<slug>[\w-]+)/edit/$', MovieUpdate.as_view(), name="movie_update"),
    url(r'^movie/(?P<slug>[\w-]+)/remove/$', MovieRemoveView.as_view(), name="movie_remove"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
