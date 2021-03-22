from django.shortcuts import get_object_or_404
from users.models import Profile
from django.contrib.auth.models import User
from movies.models import MovieRating
from django.core.paginator import Paginator

def get_movies(request, username):
    """Returns the movies under user's profile"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    movies_star_count = profile.star.filter(Type='movie').count()
    series_star_count = profile.star.filter(Type='series').count()
    watchlist_count = profile.watchlist.all().count()
    watchedlist_count = profile.watchedlist.all().count()
    opinions_count = MovieRating.objects.filter(user=user).count()
    following = []
    for p in Profile.objects.all():
        if user in p.followers.all():
            following.append(p.user)

    movies = profile.star.filter(Type='movie')

    data = Paginator(movies, 9).get_page(request.GET.get('page'))

    context = {
        'profile': profile,
        'movies_star_count': movies_star_count,
        'series_star_count': series_star_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'movie_data': data,
        'list_title': 'Favourite movies',
        'following': len(following),
    }

    return context


def get_series(request, username):
    """Returns the series under user's profile"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    movies_star_count = profile.star.filter(Type='movie').count()
    series_star_count = profile.star.filter(Type='series').count()
    watchlist_count = profile.watchlist.all().count()
    watchedlist_count = profile.watchedlist.all().count()
    opinions_count = MovieRating.objects.filter(user=user).count()
    following = []
    for p in Profile.objects.all():
        if user in p.followers.all():
            following.append(p.user)

    series = profile.star.filter(Type='series')

    data = Paginator(series, 9).get_page(request.GET.get('page'))

    context = {
        'profile': profile,
        'movies_star_count': movies_star_count,
        'series_star_count': series_star_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'movie_data': data,
        'list_title': 'Favourite series',
        'following': len(following),
    }

    return context

def get_watchlist(request, username):
    """Returns the watchlist under user's profile"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    movies_star_count = profile.star.filter(Type='movie').count()
    series_star_count = profile.star.filter(Type='series').count()
    watchlist_count = profile.watchlist.all().count()
    watchedlist_count = profile.watchedlist.all().count()
    opinions_count = MovieRating.objects.filter(user=user).count()
    following = []
    for p in Profile.objects.all():
        if user in p.followers.all():
            following.append(p.user)

    watchlist = profile.watchlist.all()

    data = Paginator(watchlist, 9).get_page(request.GET.get('page'))

    context = {
        'profile': profile,
        'movies_star_count': movies_star_count,
        'series_star_count': series_star_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'movie_data': data,
        'list_title': 'Watchlist',
        'following': len(following),
    }

    return context

def get_watchedlist(request, username):
    """Returns the watched list under user's profile"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    movies_star_count = profile.star.filter(Type='movie').count()
    series_star_count = profile.star.filter(Type='series').count()
    watchlist_count = profile.watchlist.all().count()
    watchedlist_count = profile.watchedlist.all().count()
    opinions_count = MovieRating.objects.filter(user=user).count()
    following = []
    for p in Profile.objects.all():
        if user in p.followers.all():
            following.append(p.user)

    watchedlist = profile.watchedlist.all()

    data = Paginator(watchedlist, 9).get_page(request.GET.get('page'))

    context = {
        'profile': profile,
        'movies_star_count': movies_star_count,
        'series_star_count': series_star_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'movie_data': data,
        'list_title': 'Watchedlist',
        'following': len(following),
    }

    return context

def get_reviews(request, username):
    """Returns the movies user has revied under his profile"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    movies_star_count = profile.star.filter(Type='movie').count()
    series_star_count = profile.star.filter(Type='series').count()
    watchlist_count = profile.watchlist.all().count()
    watchedlist_count = profile.watchedlist.all().count()
    opinions_count = MovieRating.objects.filter(user=user).count()
    following = []
    for p in Profile.objects.all():
        if user in p.followers.all():
            following.append(p.user)

    opinions = MovieRating.objects.filter(user=user)

    data = Paginator(opinions, 9).get_page(request.GET.get('page'))

    context = {
        'profile': profile,
        'movies_star_count': movies_star_count,
        'series_star_count': series_star_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'movie_data': data,
        'list_title': 'Reviewed',
        'following': len(following),
    }

    return context