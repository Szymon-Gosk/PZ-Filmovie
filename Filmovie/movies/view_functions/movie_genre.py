from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from movies.models import Movie, Genre
from django.conf import settings
import requests

def genre(request, genre_slug, page_number):
    """Returns the movies based on their genre.
    Uses paginator for data from the database"""
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

        return context
        
    genre = get_object_or_404(Genre, slug=genre_slug)
    movies_for_pagination = Movie.objects.filter(Genre=genre)
    movie_data = Paginator(movies_for_pagination, 9).get_page(request.GET.get('page'))
    
    context = {'movie_data': movie_data,'genre': genre}

    return context