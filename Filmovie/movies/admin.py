"""Admin configuration for movies app"""
from django.contrib import admin
from movies.models import Movie, MovieRating

admin.site.register(Movie)
admin.site.register(MovieRating)
