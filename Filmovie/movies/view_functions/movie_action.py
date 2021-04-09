from movies.models import Movie
from users.models import Profile


def star_a_movie(request, imdb_id):
    """Adding a movie to star movies list, if movie 
    already exists in list it removes it"""
    movie = Movie.objects.get(imdbID=imdb_id)
    profile = Profile.objects.get(user=request.user)

    if movie in profile.star.all():
        profile.star.remove(movie)
    else:
        profile.star.add(movie)
        
def add_movie_to_watchlist(request, imdb_id):
    """Adding a movie to watchlist, if movie 
    already exists in list it removes it"""
    movie = Movie.objects.get(imdbID=imdb_id)
    profile = Profile.objects.get(user=request.user)

    if movie in profile.watchlist.all():
        profile.watchlist.remove(movie)
    else:
        profile.watchlist.add(movie)
        
def add_movie_to_watchedlist(request, imdb_id):
    """Adding a movie to watchedlist, if movie 
    already exists in list it removes it"""
    movie = Movie.objects.get(imdbID=imdb_id)
    profile = Profile.objects.get(user=request.user)

    if movie in profile.watchedlist.all():
        profile.watchedlist.remove(movie)
    else:
        if profile.watchlist.filter(imdbID=imdb_id).exists():
            profile.watchlist.remove(movie)
            profile.watchedlist.add(movie)
        else:
            profile.watchedlist.add(movie)