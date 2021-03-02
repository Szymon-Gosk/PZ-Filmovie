"""
Registering Movie model in admin panel
"""
from django.contrib import admin
from movies.models import Movie, MovieRating

admin.site.register(Movie)
admin.site.register(MovieRating)
