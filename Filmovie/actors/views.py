from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.template import loader
from movies.models import Movie
from actors.models import Actor


def actor_view(request, actor_slug):
    actor = get_object_or_404(Actor, slug=actor_slug)
    movie = Movie.objects.filter(Actors=actor)

    paginator = Paginator(movie, 3)

    page_number = request.GET.get('page')
    movie_data = paginator.get_page(page_number)

    context = {
        'movie_data': movie_data,
        'actor': actor,
    }

    template = loader.get_template('profiles/actor.html')

    return HttpResponse(template.render(context, request))
