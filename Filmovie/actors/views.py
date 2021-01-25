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

    paginator = Paginator(movie, 6)

    page = request.GET.get('page')
    data = paginator.get_page(page)

    context = {
        'movie_data': data,
        'actor': actor,
    }

    return HttpResponse(loader.get_template('profiles/actor.html').render(context, request))
