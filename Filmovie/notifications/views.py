from django.shortcuts import render
from .models import Notification
from movies.models import Movie
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader


def delete_notification_and_redirect_view(request, notification_id,  username, imdb_id):
    Notification.objects.filter(id=notification_id).delete()
    if  Movie.objects.filter(imdbID=imdb_id).count() > 0:
        return HttpResponseRedirect(reverse('user-rating', args=[request.user.username, imdb_id]))
    else:
        return HttpResponseRedirect(reverse('profile', args=[username]))
