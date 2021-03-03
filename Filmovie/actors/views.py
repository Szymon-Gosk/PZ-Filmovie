"""Views definitions for actors app"""
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.template import loader
from movies.models import Movie
from actors.models import Actor


def actor_view(request, actor_slug):
    """View for a specified actor"""
    actor = get_object_or_404(Actor, slug=actor_slug)
    movie = Movie.objects.filter(Actors=actor)
    data = Paginator(movie, 6).get_page(request.GET.get('page'))

    return HttpResponse(loader.get_template('profiles/actor.html').render({'movie_data': data,'actor': actor}, request))
