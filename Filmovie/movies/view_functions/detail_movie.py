"""Movie detail functions for Movie detail view"""
from django.utils.text import slugify
from movies.models import Movie, Genre, Rating, MovieRating
from actors.models import Actor
from django.db.models import Avg
import requests

def movie_detail(request, imdb_id):
    """Returns detail information about the requested movie.
    If a movie exists in the database it checks if the content 
    from API is same as in database, if not, updating it 
    and then renders it using the database.
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
        
    return context