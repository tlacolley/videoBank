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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect

# from userena.views import signup

from userena import settings as userena_settings
from userena import views as userena_views

from video_bank.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view(), name="login_user"),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page="/"), name="logout_user"),

    url(r'^$', IndexView.as_view(), name="index"),

    url(r'^movie/create/$', MovieCreateView.as_view(), name="movie_create"),
    url(r'^movie/(?P<slug>[\w-]+)/$', MovieDetailView.as_view(), name="movie_detail"),
    url(r'^movie/(?P<slug>[\w-]+)/edit/$', MovieUpdate.as_view(), name="movie_update"),
    url(r'^movie/(?P<slug>[\w-]+)/remove/$', MovieRemoveView.as_view(), name="movie_remove"),
    url(r'^movie/(?P<slug>[\w-]+)/rent/$', MovieRentView.as_view(), name="rent_movie"),


# -----------------Userena--------------------

    # Signup
    url(r'^customer/create/$', userena_views.signup,{'template_name':'userena/signup.html','success_url':'/'}, name="customer_create"),

    # Profil Detail
    url(r'^customer/(?P<username>(?!(signout|signup|signin)/)[\@\.\+\w-]+)/$',
    userena_views.profile_detail,{'template_name':'userena/customer_detail.html'},
    name='userena_profile_detail'),

    # Change Password
    url(r'^customer/(?P<username>[\@\.\+\w-]+)/password/$',
       userena_views.password_change,
       name='userena_password_change'),

    url(r'^customer/(?P<username>[\@\.\+\w-]+)/password/complete/$',
    userena_views.direct_to_user_template,
    {'template_name': 'userena/password_complete.html'},
    name='userena_password_change_complete'),

    # Edit Profil
    url(r'^(?P<username>[\@\.\+\w-]+)/edit/$',
    userena_views.profile_edit,
    name='userena_profile_edit'),


    # Change email and confirm it
    url(r'^(?P<username>[\@\.\+\w-]+)/email/$',
        userena_views.email_change,
        name='userena_email_change'),
    url(r'^(?P<username>[\@\.\+\w-]+)/email/complete/$',
        userena_views.direct_to_user_template,
        {'template_name': 'userena/email_change_complete.html'},
        name='userena_email_change_complete'),
    url(r'^(?P<username>[\@\.\+\w-]+)/confirm-email/complete/$',
        userena_views.direct_to_user_template,
        {'template_name': 'userena/email_confirm_complete.html'},
        name='userena_email_confirm_complete'),
    url(r'^confirm-email/(?P<confirmation_key>\w+)/$',
        userena_views.email_confirm,
        name='userena_email_confirm'),

    # View profiles
    url(r'^page/(?P<page>[0-9]+)/$',
        userena_views.ProfileListView.as_view(),
        name='userena_profile_list_paginated'),
    url(r'^$',
        userena_views.ProfileListView.as_view(),
        name='userena_profile_list'),

# -------------------------Customer Historic-----------------

    url(r'^customer/(?P<username>[\@\.\+\w-]+)/historic/$', CustomerHistoricView.as_view(), name="customer_historic"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
