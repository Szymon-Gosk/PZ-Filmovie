from django.shortcuts import get_object_or_404
from users.models import Profile
from django.contrib.auth.models import User
from movies.models import MovieRating

def user_profile(request, username):
    """Returns the user's profile"""
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

    context = {
        'profile': profile,
        'movies_star_count': movies_star_count,
        'series_star_count': series_star_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'following': len(following),
    }

    return context