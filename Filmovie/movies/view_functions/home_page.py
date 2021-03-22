from movies.models import Movie
import requests

def main(request, page_number):
    """Returns the home or movies if there was query"""
    query = request.GET.get('q')

    if query:
        url = "http://www.omdbapi.com/?apikey=7d7fa8d6&s=" + query + '&page=' + str(page_number)
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
    
    movies = Movie.objects.all().order_by("-timestamp")[:9]
    
    context = {'movie_data': movies}
    
    return context