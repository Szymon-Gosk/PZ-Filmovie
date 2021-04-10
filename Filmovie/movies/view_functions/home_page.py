from movies.models import Movie
from django.conf import settings
import requests


def main(request, page_number):
    """Returns the home or movies if there was query"""
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
    
    movies = Movie.objects.all().order_by("-Year")[:9]
    
    context = {'data': movies}
    
    return context