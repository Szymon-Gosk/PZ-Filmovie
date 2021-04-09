"""Url patterns for actors app"""
from django.urls import path
from actors.views import actor_view


urlpatterns = [
    path('<slug:actor_slug>', actor_view, name='actors')
]