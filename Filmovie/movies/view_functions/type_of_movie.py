from django.core.paginator import Paginator
from movies.models import Movie
from django.conf import settings
import requests


def type_of_movie(request, movie_type, page_number):
    """Returns the movies based on thier type.
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

    movies_for_pagination = Movie.objects.filter(Type=movie_type).order_by("-imdbRating")
    data = Paginator(movies_for_pagination, 9).get_page(request.GET.get('page'))
    
    context = {'data': data,'genre': movie_type}

    return context