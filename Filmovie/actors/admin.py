"""Admin configuration for actors app"""
from django.contrib import admin
from .models import Actor

admin.site.register(Actor)
