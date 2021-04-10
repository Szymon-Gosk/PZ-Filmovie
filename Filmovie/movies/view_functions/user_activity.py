from django.template import loader
from django.http import HttpResponse
from movies.models import MovieRating, Likes
from django.conf import settings
import requests


def user_last_activities(request, page_number):
    """Returns the context of user last activities."""
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
    
    user = request.user
    profiles = user.following.all()
    followed_users_id = []
    for x in profiles:
        followed_users_id.append(x.user.id)
    
    has_rated = MovieRating.objects.filter(user__id__in=followed_users_id).order_by("-timestamp")
    has_liked = Likes.objects.filter(user__id__in=followed_users_id).order_by("-timestamp")
    
    last_activities = []
    for x in has_rated:
        last_activities.append(x)
        
    for x in has_liked:
        last_activities.append(x)
        
    last_activities = sorted(last_activities, key=lambda x: x.timestamp, reverse=True)[:10]
    
    context = {
        "has_rated": has_rated, 
        "has_liked": has_liked, 
        "activities": last_activities
    }

    return context