from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from movies.models import Movie, Genre
from django.conf import settings
import requests


def genre(request, genre_slug, page_number):
    """Returns the movies based on their genre.
    Uses paginator for data from the database"""
    q = request.GET.get('q')

    if q:
        url = "http://www.omdbapi.com/?apikey=" + settings.OMDB_API_KEY + "&s=" + q + '&page=' + str(page_number)
        response = requests.get(url)
        data = response.json()
        page_number = int(page_number)+1

        context = {
            'q': q,
            'data': data,
            'page_number': page_number,
            'previous_page': page_number,
            'next_page': page_number,
        }

        return context
        
    genre = get_object_or_404(Genre, slug=genre_slug)
    movies_for_pagination = Movie.objects.filter(Genre=genre)
    data = Paginator(movies_for_pagination, 9).get_page(request.GET.get('page'))
    
    context = {'data': data, 'genre': genre}

    return context