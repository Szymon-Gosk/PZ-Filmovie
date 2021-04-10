from django.http import HttpResponse
from django.conf import settings
import requests


def paginate(request, q, page_number):
    """Returns movies at the specified page from the API"""
    q2 = request.GET.get('q')

    if q2:
        url = "http://www.omdbapi.com/?apikey=" + settings.OMDB_API_KEY + "&s=" + q2 + '&page=1'
        response = requests.get(url)
        data = response.json()
        page_number = int(page_number)
        next_page = int(page_number) + 1
        previous_page = int(page_number)

        context = {
            'q': q2,
            'data': data,
            'page_number': 1,
            'previous_page': 1,
            'next_page': 2,
        }

        return context

    url = "http://www.omdbapi.com/?apikey=" + settings.OMDB_API_KEY + "&s=" + q + '&page=' + str(page_number)
    response = requests.get(url)
    data = response.json()
    next_page = int(page_number) + 1
    previous_page = int(page_number) - 1

    context = {
        'q': q,
        'data': data,
        'previous_page': previous_page,
        'next_page': next_page,
        'page_number': page_number
    }

    return context