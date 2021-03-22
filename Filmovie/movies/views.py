"""Views definitions for movies app"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from movies.view_functions import (
    detail_movie, 
    home_page, 
    user_activity, 
    paginate, 
    movie_genre, 
    type_of_movie, 
    movie_action, 
    rate_a_movie)


def redirect_to_home(request, *args, **kwargs):
    """Redirects to 'index' template (home)"""
    return render(request, 'index.html')

def home(request, page_number=1):
    context = home_page.main(request, page_number)
    
    if context.get('query') is not None:
        return HttpResponse(loader.get_template('movies/search_result.html').render(context, request))
    
    return render(request, 'home.html', context)

@login_required
def user_activities_view(request, page_number=1):
    """Receives the user last activities context. Renders 'search_result' template if the
    function gets the query from a user"""
    context = user_activity.user_last_activities(request, page_number)

    if context.get('query') is not None:
        return HttpResponse(loader.get_template('movies/search_result.html').render(context, request))

    return render(request, 'users/user_activities.html', context)

def pagination(request, query, page_number):
    """Returns movies at the specified page from the API"""
    context = paginate.paginate(request, query, page_number)
    return HttpResponse(loader.get_template('movies/search_result.html').render(context, request))

def movie_detail_view(request, imdb_id):
    context = detail_movie.movie_detail(request, imdb_id)
    
    return HttpResponse(loader.get_template('movies/movie_detail.html').render(context, request))

def genres_view(request, genre_slug, page_number=1):
    """Returns the 'genres_view' which renders the 'genre' template."""
    context = movie_genre.genre(request, genre_slug, page_number)
    
    if context.get('query') is not None:
        return HttpResponse(loader.get_template('movies/search_result.html').render(context, request))
    
    return HttpResponse(loader.get_template('movies/genre.html').render(context, request))

def type_view(request, movie_type, page_number=1):
    """Returns the 'genres_view' which renders the 'genre' template."""
    context = type_of_movie.type_of_movie(request, movie_type, page_number)
    
    if context.get('query') is not None:
        return HttpResponse(loader.get_template('movies/search_result.html').render(context, request))

    return HttpResponse(loader.get_template('movies/genre.html').render(context, request))

def star_movie_view(request, imdb_id):
    """Returns the reverse template 'movie-details' to refresh the page and save
    a movie user has added to favourites"""
    movie_action.star_a_movie(request, imdb_id)
    return HttpResponseRedirect(reverse('movie-details', args=[imdb_id]))

def add_to_watchlist_view(request, imdb_id):
    """Returns the reverse template 'movie-details' to refresh the page and save
    a movie user has added to watchlist"""
    movie_action.add_movie_to_watchlist(request, imdb_id)
    return HttpResponseRedirect(reverse('movie-details', args=[imdb_id]))

def add_to_watchedlist_view(request, imdb_id):
    """Returns the reverse template 'movie-details' to refresh the page and save
    a movie user has added to watched movies"""
    movie_action.add_movie_to_watchedlist(request, imdb_id)
    return HttpResponseRedirect(reverse('movie-details', args=[imdb_id]))

def movie_rate_view(request, imdb_id):
    """Returns the the 'rate' view"""
    context = rate_a_movie.rate(request, imdb_id)
    
    if context.get('redirect'):
        return HttpResponseRedirect(reverse('movie-details', args=[imdb_id]))
    return HttpResponse(loader.get_template('movies/rate.html').render(context, request))