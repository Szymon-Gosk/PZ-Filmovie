"""Views definitions for actors app"""
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.template import loader
from movies.models import Movie
from actors.models import Actor
from django.conf import settings
import requests


def actor_view(request, actor_slug, page_number=1):
    """View for a specified actor"""
    actor = get_object_or_404(Actor, slug=actor_slug)
    movie = Movie.objects.filter(Actors=actor)
    data = Paginator(movie, 6).get_page(request.GET.get('page'))
    
    query = request.GET.get('q')

    if query:
        url = "http://www.omdbapi.com/?apikey=" + settings.OMDB_API_KEY + "&s=" + query + '&page=' + str(page_number)
        response = requests.get(url)
        data = response.json()
        page_number = int(page_number)+1

        context = {
            'query': query,
            'movie_data': data,
            'page_number': page_number,
            'previous_page': page_number,
            'next_page': page_number,
        }
        return HttpResponse(loader.get_template('movies/search_result.html').render(context, request))

    return HttpResponse(loader.get_template('profiles/actor.html').render({'movie_data': data,'actor': actor}, request))
