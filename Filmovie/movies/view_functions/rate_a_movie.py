from movies.models import Movie, MovieRating
from movies.forms import MovieRateForm
from django.urls import reverse
from django.http import HttpResponseRedirect


def rate(request, imdb_id):
    """Saves the rating in database"""
    movie = Movie.objects.get(imdbID=imdb_id)
    user = request.user

    if request.method == 'POST':
        user_rated_this_movie = MovieRating.objects.filter(user=user, movie=movie)
        if user_rated_this_movie.count() >= 1:
            for u in user_rated_this_movie:
                u.delete()
        form = MovieRateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.movie = movie
            rate.save()
            context = {'redirect': 'redirect'}
            return context
    else:
        form = MovieRateForm()

    context = {'form': form,'movie': movie}
    
    return context