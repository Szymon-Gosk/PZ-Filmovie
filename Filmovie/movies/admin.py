"""Admin configuration for movies app"""
from django.contrib import admin
from movies.models import Movie, MovieRating, Likes, Genre, Rating


admin.site.register(Movie)
admin.site.register(MovieRating)
admin.site.register(Likes)
admin.site.register(Genre)
admin.site.register(Rating)