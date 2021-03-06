"""Views definitions for movies app"""
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from movies.models import Movie, Genre, Rating, MovieRating, Likes
from actors.models import Actor
from users.models import Profile, FollowerRelation
from movies.forms import MovieRateForm
from django.db.models import Avg
import requests


def redirect_to_home(request, *args, **kwargs):
    """Redirects to 'index' template (home)"""
    return render(request, 'index.html')

def home(request):
    """Returns the 'home' view. Renders 'search_result' template if the
    function gets the query from a user (if home template has not been rendered)"""
    query = request.GET.get('q')

    if query:
        url = "http://www.omdbapi.com/?apikey=7d7fa8d6&s=" + query
        response = requests.get(url)
        data = response.json()

        context = {
            'query': query,
            'movie_data': data,
            'page_number': 1,
        }

        return HttpResponse(loader.get_template('movies/search_result.html').render(context, request))
    
    movies = Movie.objects.all().order_by("-timestamp")[:9]
    
    return render(request, 'home.html', {"movie_data": movies})

@login_required
def user_activities_view(request):
    """Returns the 'user last activities' view. Renders 'search_result' template if the
    function gets the query from a user (if home template has not been rendered)"""
    query = request.GET.get('q')

    if query:
        url = "http://www.omdbapi.com/?apikey=7d7fa8d6&s=" + query
        response = requests.get(url)
        data = response.json()

        context = {
            'query': query,
            'movie_data': data,
            'page_number': 1,
        }

        return HttpResponse(loader.get_template('movies/search_result.html').render(context, request))
    
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
        
    last_activities = sorted(last_activities, key=lambda x: x.timestamp, reverse=True)
    
    print(last_activities)

    return render(request, 'users/user_activities.html', {"has_rated": has_rated,"has_liked": has_liked, "last_activities": last_activities})

def pagination(request, query, page_number):
    """Returns movies at the specified page from the API"""

    url = "http://www.omdbapi.com/?apikey=7d7fa8d6&s=" + query + '&page=' + str(page_number)
    response = requests.get(url)
    data = response.json()
    page_number = int(page_number)+1

    context = {
        'query': query,
        'movie_data': data,
        'page_number': page_number,
    }

    return HttpResponse(loader.get_template('movies/search_result.html').render(context, request))

def movie_detail_view(request, imdb_id):
    """Returns 'movieDetail' view which renders 'movie_detail' template.
    If a movie exists in the database it renders it using the database.
    Otherwise it is rendered from the API"""

    if Movie.objects.filter(imdbID=imdb_id).exists():
        data = Movie.objects.get(imdbID=imdb_id)
        opinions = MovieRating.objects.filter(movie=data)
        
        if not request.user.is_authenticated:
            if not opinions:
                rating_avg = 0
                rating_count = 0
            else:
                rating_avg = round(opinions.aggregate(Avg('rate'))['rate__avg'], 2)
                rating_count = opinions.count()

            our_db = True

            context = {
                'movie_data': data,
                'our_db': our_db,
                'opinions': opinions,
                'rating_avg': rating_avg,
                'rating_count': rating_count,
            }
            
        else:
            user = request.user
            if data in user.profile.watchedlist.all():
                watchedlist = True
            else:
                watchedlist = False

            if data in user.profile.watchlist.all():
                watchlist = True
            else:
                watchlist = False

            if data in user.profile.star.all():
                star = True
            else:
                star = False

            if not opinions:
                rating_avg = 0
                rating_count = 0
            else:
                rating_avg = round(opinions.aggregate(Avg('rate'))['rate__avg'], 2)
                rating_count = opinions.count()

            our_db = True

            context = {
            'movie_data': data,
            'our_db': our_db,
            'opinions': opinions,
            'rating_avg': rating_avg,
            'rating_count': rating_count,
            "star": star,
            "watchlist": watchlist,
            "watchedlist": watchedlist,
            }

    else:
        url = "http://www.omdbapi.com/?apikey=7d7fa8d6&i=" + imdb_id
        response = requests.get(url)
        data = response.json()

        rating_objs = []
        genre_objs = []
        actors_obj = []

        actor_list = [x.strip() for x in data['Actors'].split(',')]

        for actor in actor_list:
            a, created = Actor.objects.get_or_create(name=actor)
            actors_obj.append(a)
            
        genre_list = list(data['Genre'].replace(" ", "").split(','))

        for genre in genre_list:
            genre_slug = slugify(genre)
            g, created = Genre.objects.get_or_create(title=genre, slug=genre_slug)
            genre_objs.append(g)

        for rate in data['Ratings']:
            r, created = Rating.objects.get_or_create(source=rate['Source'], rating=rate['Value'])
            rating_objs.append(r)

        if data['Type'] == 'movie':
            m, created = Movie.objects.get_or_create(
                Title = data['Title'],
                Year = data['Year'],
                Rated = data['Rated'],
                Released = data['Released'],
                Runtime = data['Runtime'],
                Director = data['Director'],
                Writer = data['Writer'],
                Plot = data['Plot'],
                Language = data['Language'],
                Country = data['Country'],
                Awards = data['Awards'],
                Poster_url = data['Poster'],
                Metascore = data['Metascore'],
                imdbRating = data['imdbRating'],
                imdbVotes = data['imdbVotes'],
                imdbID = data['imdbID'],
                Type = data['Type'],
                DVD = data['DVD'],
                BoxOffice = data['BoxOffice'],
                Production = data['Production'],
                Website = data['Website'],
            )
            m.Genre.set(genre_objs)
            m.Actors.set(actors_obj)
            m.Ratings.set(rating_objs)

        else:
            m, created = Movie.objects.get_or_create(
                Title = data['Title'],
                Year = data['Year'],
                Rated = data['Rated'],
                Released = data['Released'],
                Runtime = data['Runtime'],
                Director = data['Director'],
                Writer = data['Writer'],
                Plot = data['Plot'],
                Language = data['Language'],
                Country = data['Country'],
                Awards = data['Awards'],
                Poster_url = data['Poster'],
                Metascore = data['Metascore'],
                imdbRating = data['imdbRating'],
                imdbVotes = data['imdbVotes'],
                imdbID = data['imdbID'],
                Type = data['Type'],
                totalSeasons = data['totalSeasons'],
            )
            m.Genre.set(genre_objs)
            m.Actors.set(actors_obj)
            m.Ratings.set(rating_objs)

        for actor in actors_obj:
            actor.movies.add(m)
            actor.save()

        m.save()
        our_db = False
        
        context = {
            'movie_data': data,
            'our_db': our_db
        }

    return HttpResponse(loader.get_template('movies/movie_detail.html').render(context, request))

def genres_view(request, genre_slug):
    """Returns the 'genres_view' which renders the 'genre' template.
    Uses paginator for data from the database"""
    query = request.GET.get('q')

    if query:
        url = "http://www.omdbapi.com/?apikey=7d7fa8d6&s=" + query
        response = requests.get(url)
        data = response.json()

        context = {
            'query': query,
            'movie_data': data,
            'page_number': 1,
        }

        return HttpResponse(loader.get_template('movies/search_result.html').render(context, request))
        
    genre = get_object_or_404(Genre, slug=genre_slug)
    movies_for_pagination = Movie.objects.filter(Genre=genre)
    movie_data = Paginator(movies_for_pagination, 9).get_page(request.GET.get('page'))

    return HttpResponse(loader.get_template('movies/genre.html').render({'movie_data': movie_data,'genre': genre}, request))

def type_view(request, type):
    """Returns the 'genres_view' which renders the 'genre' template.
    Uses paginator for data from the database"""
    query = request.GET.get('q')

    if query:
        url = "http://www.omdbapi.com/?apikey=7d7fa8d6&s=" + query
        response = requests.get(url)
        data = response.json()

        context = {
            'query': query,
            'movie_data': data,
            'page_number': 1,
        }

        return HttpResponse(loader.get_template('movies/search_result.html').render(context, request))

    movies_for_pagination = Movie.objects.filter(Type=type)
    data = Paginator(movies_for_pagination, 9).get_page(request.GET.get('page'))

    return HttpResponse(loader.get_template('movies/genre.html').render({'movie_data': data,'genre': type}, request))

def star_movie_view(request, imdb_id):
    """Returns the reverse template 'movie-details' to refresh the page and save
    a movie user has added to favourites"""
    movie = Movie.objects.get(imdbID=imdb_id)
    profile = Profile.objects.get(user=request.user)

    if movie in profile.star.all():
        profile.star.remove(movie)
    else:
        profile.star.add(movie)

    return HttpResponseRedirect(reverse('movie-details', args=[imdb_id]))

def add_to_watchlist_view(request, imdb_id):
    """Returns the reverse template 'movie-details' to refresh the page and save
    a movie user has added to watchlist"""
    movie = Movie.objects.get(imdbID=imdb_id)
    profile = Profile.objects.get(user=request.user)

    if movie in profile.watchlist.all():
        profile.watchlist.remove(movie)
    else:
        profile.watchlist.add(movie)

    return HttpResponseRedirect(reverse('movie-details', args=[imdb_id]))

def add_to_watchedlist_view(request, imdb_id):
    """Returns the reverse template 'movie-details' to refresh the page and save
    a movie user has added to watched movies"""
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

    return HttpResponseRedirect(reverse('movie-details', args=[imdb_id]))

def movie_rate_view(request, imdb_id):
    """Returns the the 'rate' view"""
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
            return HttpResponseRedirect(reverse('movie-details', args=[imdb_id]))
    else:
        form = MovieRateForm()

    return HttpResponse(loader.get_template('movies/rate.html').render({'form': form,'movie': movie}, request)) 