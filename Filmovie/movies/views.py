"""Movie views"""
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from movies.models import Movie, Genre, Rating, MovieRating, Likes
from actors.models import Actor
from users.models import Profile
from movies.forms import MovieRateForm
from django.db.models import Avg
import requests

def redirect_to_home(request, *args, **kwargs):
    return render(request, 'index.html')

def home(request):
    """Returning the home view. Rendering search_result template if the
    function gets the query from a user (if not rendering home template)"""
    query = request.GET.get('q')

    if query:
        url = "http://www.omdbapi.com/?apikey=7d7fa8d6&s=" + query
        response = requests.get(url)
        movie_data = response.json()

        context = {
            'query': query,
            'movie_data': movie_data,
            'page_number': 1,
        }

        template = loader.get_template('movies/search_result.html')

        return HttpResponse(template.render(context, request))
    
    movies = Movie.objects.all().order_by("-timestamp")
    movies = movies[:9]
    
    context = {
        "movie_data": movies,
    }
    
    
    return render(request, 'home.html', context)


@login_required
def user_activities_view(request):
    """Returning the user last activities view. Rendering search_result template if the
    function gets the query from a user (if not rendering home template)"""
    query = request.GET.get('q')

    if query:
        url = "http://www.omdbapi.com/?apikey=7d7fa8d6&s=" + query
        response = requests.get(url)
        movie_data = response.json()

        context = {
            'query': query,
            'movie_data': movie_data,
            'page_number': 1,
        }

        template = loader.get_template('movies/search_result.html')

        return HttpResponse(template.render(context, request))
    
    user = request.user
    profiles = user.following.all()
    followed_users_id = []
    for x in profiles:
        followed_users_id.append(x.user.id)
        
    has_rated = MovieRating.objects.filter(user__id__in=followed_users_id).order_by("-timestamp")
    has_rated = has_rated[:10]
    has_liked = Likes.objects.filter(user__id__in=followed_users_id).order_by("-timestamp")
    has_liked = has_liked[:10]
    print(has_liked)
    
    context = {
        "has_rated": has_rated,
        "has_liked": has_liked,
    }
    
    
    return render(request, 'users/user_activities.html', context)


def pagination(request, query, page_number):
    """Returning the movies at the specific page from an external API"""

    url = "http://www.omdbapi.com/?apikey=7d7fa8d6&s=" + query + '&page=' + str(page_number)
    response = requests.get(url)
    movie_data = response.json()
    page_number = int(page_number)+1

    context = {
        'query': query,
        'movie_data': movie_data,
        'page_number': page_number,
    }

    template = loader.get_template('movies/search_result.html')

    return HttpResponse(template.render(context, request))

def movie_detail_view(request, imdb_id):
    """Returning movieDetail view which renders movie_detail template.
    If the movie exists in database it renders it using the database.
    If not it will render it from and external API"""

    if Movie.objects.filter(imdbID=imdb_id).exists():
        movie_data = Movie.objects.get(imdbID=imdb_id)
        opinions = MovieRating.objects.filter(movie=movie_data)
        
        if not request.user.is_authenticated:
            if not opinions:
                rating_avg = 0
                rating_count = 0
            else:
                rating_avg = round(opinions.aggregate(Avg('rate'))['rate__avg'],2)
                rating_count = opinions.count()

            our_db = True

            context = {
                'movie_data': movie_data,
                'our_db': our_db,
                'opinions': opinions,
                'rating_avg': rating_avg,
                'rating_count': rating_count,
            }
        else:
            user = request.user
            if movie_data in user.profile.watchedlist.all():
                watchedlist = True
            else:
                watchedlist = False

            if movie_data in user.profile.watchlist.all():
                watchlist = True
            else:
                watchlist = False

            if movie_data in user.profile.star.all():
                star = True
            else:
                star = False
            
            if not opinions:
                rating_avg = 0
                rating_count = 0
            else:
                rating_avg = round(opinions.aggregate(Avg('rate'))['rate__avg'],2)
                rating_count = opinions.count()

            our_db = True
            
            context = {
            'movie_data': movie_data,
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
        print(url)
        response = requests.get(url)
        print(response)
        movie_data = response.json()
        print(movie_data)

        #inject to our db

        rating_objs = []
        genre_objs = []
        actors_obj = []

        #Actors
        actor_list = [x.strip() for x in movie_data['Actors'].split(',')]

        for actor in actor_list:
            a, created = Actor.objects.get_or_create(name=actor)
            actors_obj.append(a)

        #Ganre
        genre_list = list(movie_data['Genre'].replace(" ", "").split(','))


        for genre in genre_list:
            genre_slug = slugify(genre)
            g, created = Genre.objects.get_or_create(title=genre, slug=genre_slug)
            genre_objs.append(g)

        #Rate

        for rate in movie_data['Ratings']:
            r, created = Rating.objects.get_or_create(source=rate['Source'], rating=rate['Value'])
            rating_objs.append(r)

        if movie_data['Type'] == 'movie':
            m, created = Movie.objects.get_or_create(
                Title = movie_data['Title'],
                Year = movie_data['Year'],
                Rated = movie_data['Rated'],
                Released = movie_data['Released'],
                Runtime = movie_data['Runtime'],
                Director = movie_data['Director'],
                Writer = movie_data['Writer'],
                Plot = movie_data['Plot'],
                Language = movie_data['Language'],
                Country = movie_data['Country'],
                Awards = movie_data['Awards'],
                Poster_url = movie_data['Poster'],
                Metascore = movie_data['Metascore'],
                imdbRating = movie_data['imdbRating'],
                imdbVotes = movie_data['imdbVotes'],
                imdbID = movie_data['imdbID'],
                Type = movie_data['Type'],
                DVD = movie_data['DVD'],
                BoxOffice = movie_data['BoxOffice'],
                Production = movie_data['Production'],
                Website = movie_data['Website'],
            )
            m.Genre.set(genre_objs)
            m.Actors.set(actors_obj)
            m.Ratings.set(rating_objs)

        else:
            m, created = Movie.objects.get_or_create(
                Title = movie_data['Title'],
                Year = movie_data['Year'],
                Rated = movie_data['Rated'],
                Released = movie_data['Released'],
                Runtime = movie_data['Runtime'],
                Director = movie_data['Director'],
                Writer = movie_data['Writer'],
                Plot = movie_data['Plot'],
                Language = movie_data['Language'],
                Country = movie_data['Country'],
                Awards = movie_data['Awards'],
                Poster_url = movie_data['Poster'],
                Metascore = movie_data['Metascore'],
                imdbRating = movie_data['imdbRating'],
                imdbVotes = movie_data['imdbVotes'],
                imdbID = movie_data['imdbID'],
                Type = movie_data['Type'],
                totalSeasons = movie_data['totalSeasons'],
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
            'movie_data': movie_data,
            'our_db': our_db,
        }

    template = loader.get_template('movies/movie_detail.html')

    return HttpResponse(template.render(context, request))


def genres_view(request, genre_slug):
    """Returning the genres_view which renders the genre template.
    Using paginator for the data from database"""
    query = request.GET.get('q')

    if query:
        url = "http://www.omdbapi.com/?apikey=7d7fa8d6&s=" + query
        response = requests.get(url)
        movie_data = response.json()

        context = {
            'query': query,
            'movie_data': movie_data,
            'page_number': 1,
        }

        template = loader.get_template('movies/search_result.html')

        return HttpResponse(template.render(context, request))
        
    genre = get_object_or_404(Genre, slug=genre_slug)

    movies_for_pagination = Movie.objects.filter(Genre=genre)

    paginator = Paginator(movies_for_pagination, 9)

    page_number = request.GET.get('page')
    movie_data = paginator.get_page(page_number)

    context = {
        'movie_data': movie_data,
        'genre': genre,
    }

    template = loader.get_template('movies/genre.html')

    return HttpResponse(template.render(context, request))

def type_view(request, type):
    """Returning the genres_view which renders the genre template.
    Using paginator for the data from database"""
    query = request.GET.get('q')

    if query:
        url = "http://www.omdbapi.com/?apikey=7d7fa8d6&s=" + query
        response = requests.get(url)
        movie_data = response.json()

        context = {
            'query': query,
            'movie_data': movie_data,
            'page_number': 1,
        }

        template = loader.get_template('movies/search_result.html')

        return HttpResponse(template.render(context, request))

    movies_for_pagination = Movie.objects.filter(Type=type)

    paginator = Paginator(movies_for_pagination, 9)

    page_number = request.GET.get('page')
    movie_data = paginator.get_page(page_number)

    context = {
        'movie_data': movie_data,
        'genre': type,
    }

    template = loader.get_template('movies/genre.html')

    return HttpResponse(template.render(context, request))


def star_movie_view(request, imdb_id):
    """Returning the reverse template movie-details to refresh the page and save
    the movie user had added to faveourites"""
    movie = Movie.objects.get(imdbID=imdb_id)
    user = request.user
    profile = Profile.objects.get(user=user)

    if (movie in profile.star.all()):
        profile.star.remove(movie)
    else:
        profile.star.add(movie)


    return HttpResponseRedirect(reverse('movie-details', args=[imdb_id]))



def add_to_watchlist_view(request, imdb_id):
    """Returning the the reverse template movie-details to refresh the page and save
    the movie user had added to watchlist"""
    movie = Movie.objects.get(imdbID=imdb_id)
    user = request.user
    profile = Profile.objects.get(user=user)

    if (movie in profile.watchlist.all()):
        profile.watchlist.remove(movie)
    else:
        profile.watchlist.add(movie)

    return HttpResponseRedirect(reverse('movie-details', args=[imdb_id]))


def add_to_watchedlist_view(request, imdb_id):
    """Returning the the reverse template movie-details to refresh the page and save
    the movie user had added to watched movies"""
    movie = Movie.objects.get(imdbID=imdb_id)
    user = request.user
    profile = Profile.objects.get(user=user)

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
    movie = Movie.objects.get(imdbID=imdb_id)
    user = request.user
    

    if request.method == 'POST':
        user_rated_this_movie = MovieRating.objects.filter(user=user, movie=movie)
        if user_rated_this_movie.count()>=1:
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

    template = loader.get_template('movies/rate.html')

    context = {
        'form': form,
        'movie': movie,
    }

    return HttpResponse(template.render(context, request)) 
