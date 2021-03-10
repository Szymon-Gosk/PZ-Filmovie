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

def home(request, page_number=1):
    """Returns the 'home' view. Renders 'search_result' template if the
    function gets the query from a user (if home template has not been rendered)"""
    query = request.GET.get('q')

    if query:
        url = "http://www.omdbapi.com/?apikey=7d7fa8d6&s=" + query + '&page=' + str(page_number)
        response = requests.get(url)
        data = response.json()
        page_number = int(page_number)+1

        context = {
            'query': query,
            'movie_data': data,
            'page_number': page_number,
            'previous_page': page_number,
            'next_page': page_number,
        }

        return HttpResponse(loader.get_template('movies/search_result.html').render(context, request))
    
    movies = Movie.objects.all().order_by("-timestamp")[:9]
    
    return render(request, 'home.html', {"movie_data": movies})

@login_required
def user_activities_view(request, page_number=1):
    """Returns the 'user last activities' view. Renders 'search_result' template if the
    function gets the query from a user (if home template has not been rendered)"""
    query = request.GET.get('q')

    if query:
        url = "http://www.omdbapi.com/?apikey=7d7fa8d6&s=" + query + '&page=' + str(page_number)
        response = requests.get(url)
        data = response.json()
        page_number = int(page_number)+1

        context = {
            'query': query,
            'movie_data': data,
            'page_number': page_number,
            'previous_page': page_number,
            'next_page': page_number,
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
        
    last_activities = sorted(last_activities, key=lambda x: x.timestamp, reverse=True)[:10]
    
    context = {
        "has_rated": has_rated, 
        "has_liked": has_liked, 
        "activities": last_activities
    }

    return render(request, 'users/user_activities.html', context)

def pagination(request, query, page_number):
    """Returns movies at the specified page from the API"""
    query2 = request.GET.get('q')

    if query2:
        url = "http://www.omdbapi.com/?apikey=7d7fa8d6&s=" + query2 + '&page=1'
        response = requests.get(url)
        data = response.json()
        page_number = int(page_number)
        next_page = int(page_number) + 1
        previous_page = int(page_number)

        context = {
            'query': query2,
            'movie_data': data,
            'page_number': 1,
            'previous_page': 1,
            'next_page': 2,
        }

        return HttpResponse(loader.get_template('movies/search_result.html').render(context, request))

    url = "http://www.omdbapi.com/?apikey=7d7fa8d6&s=" + query + '&page=' + str(page_number)
    response = requests.get(url)
    data = response.json()
    next_page = int(page_number) + 1
    previous_page = int(page_number) - 1

    context = {
        'query': query,
        'movie_data': data,
        'previous_page': previous_page,
        'next_page': next_page,
        'page_number': page_number
    }

    return HttpResponse(loader.get_template('movies/search_result.html').render(context, request))

def movie_detail_view(request, imdb_id):
    """Returns 'movieDetail' view which renders 'movie_detail' template.
    If a movie exists in the database it renders it using the database.
    Otherwise it is rendered from the API"""

    if Movie.objects.filter(imdbID=imdb_id).exists():
        data = Movie.objects.get(imdbID=imdb_id)
        opinions = MovieRating.objects.filter(movie=data)
        url = "http://www.omdbapi.com/?apikey=7d7fa8d6&i=" + imdb_id
        response = requests.get(url)
        api_data = response.json()
        
        if data.Type == 'movie':
            if not (data.Title == api_data['Title'] and
                data.Year == api_data['Year'] and
                data.Rated == api_data['Rated'] and
                data.Released == api_data['Released'] and
                data.Runtime == api_data['Runtime'] and
                data.Director == api_data['Director'] and
                data.Writer == api_data['Writer'] and
                data.Language == api_data['Language'] and
                data.Country == api_data['Country'] and
                data.Plot == api_data['Plot'] and
                data.Poster_url == api_data['Poster'] and
                data.Awards == api_data['Awards'] and
                data.Metascore == api_data['Metascore'] and
                data.imdbRating == api_data['imdbRating'] and
                data.imdbVotes == api_data['imdbVotes'] and
                data.imdbID == api_data['imdbID'] and
                data.Type == api_data['Type'] and
                data.DVD == api_data['DVD'] and
                data.BoxOffice == api_data['BoxOffice'] and
                data.Production == api_data['Production'] and
                data.Website == api_data['Website']):

                    data.Title = api_data['Title']
                    data.Year = api_data['Year']
                    data.Rated = api_data['Rated']
                    data.Released = api_data['Released']
                    data.Runtime = api_data['Runtime']
                    data.Director = api_data['Director']
                    data.Writer = api_data['Writer']
                    data.Plot = api_data['Plot']
                    data.Language = api_data['Language']
                    data.Country = api_data['Country']
                    data.Awards = api_data['Awards']
                    data.Poster_url = api_data['Poster']
                    data.Metascore = api_data['Metascore']
                    data.imdbRating = api_data['imdbRating']
                    data.imdbVotes = api_data['imdbVotes']
                    data.imdbID = api_data['imdbID']
                    data.Type = api_data['Type']
                    data.DVD = api_data['DVD']
                    data.BoxOffice = api_data['BoxOffice']
                    data.Production = api_data['Production']
                    data.Website = api_data['Website']
                    
                    data.save()
                    
            rating_objs = []
            genre_objs = []
            actors_obj = []

            actor_list = [x.strip() for x in api_data['Actors'].split(',')]

            for actor in actor_list:
                a, updated = Actor.objects.update_or_create(name=actor)
                actors_obj.append(a)
                
            genre_list = list(api_data['Genre'].replace(" ", "").split(','))

            for genre in genre_list:
                genre_slug = slugify(genre)
                g, updated = Genre.objects.update_or_create(title=genre, slug=genre_slug)
                genre_objs.append(g)

            for rate in api_data['Ratings']:
                r, updated = Rating.objects.update_or_create(source=rate['Source'], rating=rate['Value'])
                rating_objs.append(r)
                
            isDiffs = False
            for genre in genre:
                if genre not in data.Genre.all():
                    isDiffs = True
                
            if isDiffs:
                data.Genre.set(genre_objs)
                
            isDiffs = False
            for actor in actors_obj:
                if actor not in data.Actors.all():
                    isDiffs = True
            
            if isDiffs:
                data.Actors.set(actors_obj)
                for actor in actors_obj:
                    actor.movies.add(data)
                    actor.save()
                
            isDiffs = False
            for rating in rating_objs:
                if rating not in data.Ratings.all():
                    isDiffs = True
            
            if isDiffs:
                data.Ratings.set(rating_objs)
                        
            data.save()
            
        else:
            
            if not (data.Title == api_data['Title'] and
                data.Year == api_data['Year'] and
                data.Rated == api_data['Rated'] and
                data.Released == api_data['Released'] and
                data.Runtime == api_data['Runtime'] and
                data.Director == api_data['Director'] and
                data.Writer == api_data['Writer'] and
                data.Plot == api_data['Plot'] and
                data.Language == api_data['Language'] and
                data.Country == api_data['Country'] and
                data.Awards == api_data['Awards'] and
                data.Poster_url == api_data['Poster'] and
                data.Metascore == api_data['Metascore'] and
                data.imdbRating == api_data['imdbRating'] and
                data.imdbVotes == api_data['imdbVotes'] and
                data.imdbID == api_data['imdbID'] and
                data.Type == api_data['Type'] and
                data.totalSeasons == api_data['totalSeasons']):

                data.Title = api_data['Title']
                data.Year = api_data['Year']
                data.Rated = api_data['Rated']
                data.Released = api_data['Released']
                data.Runtime = api_data['Runtime']
                data.Director = api_data['Director']
                data.Writer = api_data['Writer']
                data.Plot = api_data['Plot']
                data.Language = api_data['Language']
                data.Country = api_data['Country']
                data.Awards = api_data['Awards']
                data.Poster_url = api_data['Poster']
                data.Metascore = api_data['Metascore']
                data.imdbRating = api_data['imdbRating']
                data.imdbVotes = api_data['imdbVotes']
                data.imdbID = api_data['imdbID']
                data.Type = api_data['Type']
                data.totalSeasons = api_data['totalSeasons']

                data.save()
                
            rating_objs = []
            genre_objs = []
            actors_obj = []

            actor_list = [x.strip() for x in api_data['Actors'].split(',')]

            for actor in actor_list:
                a, updated = Actor.objects.update_or_create(name=actor)
                actors_obj.append(a)
                
            genre_list = list(api_data['Genre'].replace(" ", "").split(','))

            for genre in genre_list:
                genre_slug = slugify(genre)
                g, updated = Genre.objects.update_or_create(title=genre, slug=genre_slug)
                genre_objs.append(g)

            for rate in api_data['Ratings']:
                r, updated = Rating.objects.update_or_create(source=rate['Source'], rating=rate['Value'])
                rating_objs.append(r)
                
            isDiffs = False
            for genre in genre:
                if genre not in data.Genre.all():
                    isDiffs = True
                
            if isDiffs:
                data.Genre.set(genre_objs)
                
            isDiffs = False
            for actor in actors_obj:
                if actor not in data.Actors.all():
                    isDiffs = True
            
            if isDiffs:
                data.Actors.set(actors_obj)
                for actor in actors_obj:
                    actor.movies.add(data)
                    actor.save()
                
            isDiffs = False
            for rating in rating_objs:
                if rating not in data.Ratings.all():
                    isDiffs = True
            
            if isDiffs:
                data.Ratings.set(rating_objs)
                        
            data.save()
        
        if not request.user.is_authenticated:
            if not opinions:
                rating_avg = 0
                rating_count = 0
            else:
                rating_avg = round(opinions.aggregate(Avg('rate'))['rate__avg'], 2)
                rating_count = opinions.count()

            data = Movie.objects.get(imdbID=imdb_id)
            our_db = True

            context = {
                'movie_data': data,
                'our_db': our_db,
                'opinions': opinions,
                'rating_avg': rating_avg,
                'rating_count': rating_count,
            }
            
        else:
            data = Movie.objects.get(imdbID=imdb_id)
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

def genres_view(request, genre_slug, page_number=1):
    """Returns the 'genres_view' which renders the 'genre' template.
    Uses paginator for data from the database"""
    query = request.GET.get('q')

    if query:
        url = "http://www.omdbapi.com/?apikey=7d7fa8d6&s=" + query + '&page=' + str(page_number)
        response = requests.get(url)
        data = response.json()
        page_number = int(page_number)+1

        context = {
            'query': query,
            'movie_data': data,
            'page_number': page_number,
            'previous_page': page_number,
            'next_page': page_number,
        }

        return HttpResponse(loader.get_template('movies/search_result.html').render(context, request))
        
    genre = get_object_or_404(Genre, slug=genre_slug)
    movies_for_pagination = Movie.objects.filter(Genre=genre)
    movie_data = Paginator(movies_for_pagination, 9).get_page(request.GET.get('page'))

    return HttpResponse(loader.get_template('movies/genre.html').render({'movie_data': movie_data,'genre': genre}, request))

def type_view(request, type, page_number=1):
    """Returns the 'genres_view' which renders the 'genre' template.
    Uses paginator for data from the database"""
    query = request.GET.get('q')

    if query:
        url = "http://www.omdbapi.com/?apikey=7d7fa8d6&s=" + query + '&page=' + str(page_number)
        response = requests.get(url)
        data = response.json()
        page_number = int(page_number)+1

        context = {
            'query': query,
            'movie_data': data,
            'page_number': page_number,
            'previous_page': page_number,
            'next_page': page_number,
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