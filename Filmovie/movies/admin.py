"""
Registering Movie model in admin panel
"""
from django.contrib import admin
from movies.models import Movie



admin.site.register(Movie)
