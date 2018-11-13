# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import MovieGenre, Movie, Customer, MovieRent
# Register your models here.


class MovieGenreAdmin(admin.ModelAdmin):
    list_display = ( 'label', 'slug',)
    list_filter = ( 'label',)


class MovieAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'slug', 'actors', 'director', 'picture', 'release_date', 'rented' )

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
    list_display = (  'movie', 'customer', 'checkout_date', 'return_date' )

    list_filter = ( 'movie', 'checkout_date', 'return_date' )


admin.site.register(MovieGenre, MovieGenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieRent, MovieRentAdmin)

# PARLER_LANGUAGES = {
#     ID: (
#         {'code': 'en',},
#         {'code': 'en-us',},
#         {'code': 'it',},
#         {'code': 'nl',},
#     ),
#     'default': {
#         'fallback': 'en',             # defaults to PARLER_DEFAULT_LANGUAGE_CODE
#         'hide_untranslated': False,   # the default; let .active_translations() return fallbacks too.
#     }
# }
