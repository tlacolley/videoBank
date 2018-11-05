# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import MovieGenre, Movie, Customer, MovieRent
# Register your models here.


class MovieGenreAdmin(admin.ModelAdmin):
    list_display = ( 'label', 'slug',)
    list_filter = ( 'label',)


class MovieAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'slug', 'synopsis', 'actors', 'director', 'picture', 'release_date', 'rented', 'trailer_url' )

    fieldsets = (
        ('General', {
            'fields': (('title', 'rented'),
                             ('actors','director', 'country')
                             ),
        }),
        ('Content', {
            'fields': (('synopsis',),
                        ('release_date','genre','length'),
                        ('picture','trailer_url')
                             ),
        }),
    )



class MovieRentAdmin(admin.ModelAdmin):
    list_display = (  'movie', 'checkout_date', 'return_date' )

    list_filter = ( 'movie', 'checkout_date', 'return_date' )


admin.site.register(MovieGenre, MovieGenreAdmin)
admin.site.register(Movie)
admin.site.register(MovieRent, MovieRentAdmin)
