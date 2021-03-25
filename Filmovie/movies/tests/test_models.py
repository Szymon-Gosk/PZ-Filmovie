"""Test cases for comments app"""
from django.test import TestCase
from movies.models import Genre, Movie, Rating, MovieRating, Likes
from actors.models import Actor
from django.contrib.auth import get_user_model

User = get_user_model()


RATE = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
]


class MovieModelTestCase(TestCase):
    @classmethod
    def setUp(cls):
        genre = Genre.objects.create(title='Test', slug='test')
        rating = Rating.objects.create(source='test', rating='test')
        actor = Actor.objects.create(name='Test Test', slug='test-test')
        movie = Movie.objects.create(
            Title='Test', 
            Year='1999',
            Rated='Test Rated',
            Released='Test Released',
            Runtime='Test Runtime',
            Director='Test Director',
            Writer='Test Writer',
            Plot='Test Plot',
            Language='Test Language',
            Country='Test Country',
            Awards='Test Awards',
            Poster='Test Poster', 
            Poster_url='Test Poster URL',
            Metascore='1',
            imdbRating='1',
            imdbVotes='Test id',
            imdbID='Test IMDBID',
            Type='Test Type',
            DVD='Test DVD',
            BoxOffice='Test BoxOffice',
            Production='Test Production',
            Website='Test Website',
            totalSeasons='1')
        movie.Genre.add(genre)
        movie.Ratings.add(rating)
        movie.Actors.add(actor)
        
    def test_title_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Title').verbose_name
        self.assertEqual(name, 'Title')
    
    def test_title_field_max_length(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Title').max_length
        self.assertEqual(name, 150)
        
    def test_title_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Title').null
        self.assertEqual(name, True)
        
    def test_year_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Year').verbose_name
        self.assertEqual(name, 'Year')
    
    def test_year_field_max_length(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Year').max_length
        self.assertEqual(name, 25)
        
    def test_year_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Year').null
        self.assertEqual(name, True)
        
    def test_year_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Year').blank
        self.assertEqual(name, True)
        
    def test_rated_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Rated').verbose_name
        self.assertEqual(name, 'Rated')
    
    def test_rated_field_max_length(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Rated').max_length
        self.assertEqual(name, 10)
        
    def test_rated_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Rated').blank
        self.assertEqual(name, True)
        
    def test_rated_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Rated').null
        self.assertEqual(name, True)
        
    def test_released_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Released').verbose_name
        self.assertEqual(name, 'Released')
    
    def test_released_field_max_length(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Released').max_length
        self.assertEqual(name, 25)
        
    def test_released_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Released').null
        self.assertEqual(name, True)
        
    def test_released_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Released').blank
        self.assertEqual(name, True)
        
    def test_runtime_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Runtime').verbose_name
        self.assertEqual(name, 'Runtime')
    
    def test_runtime_field_max_length(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Runtime').max_length
        self.assertEqual(name, 25)
        
    def test_runtime_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Runtime').null
        self.assertEqual(name, True)
        
    def test_runtime_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Runtime').blank
        self.assertEqual(name, True)
        
    def test_genre_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Genre').verbose_name
        self.assertEqual(name, 'Genre')
        
    def test_genre_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Genre').blank
        self.assertEqual(name, True)
        
    def test_director_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Director').verbose_name
        self.assertEqual(name, 'Director')
    
    def test_director_field_max_length(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Director').max_length
        self.assertEqual(name, 100)
        
    def test_director_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Director').null
        self.assertEqual(name, True)
        
    def test_director_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Director').blank
        self.assertEqual(name, True)
        
    def test_writer_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Writer').verbose_name
        self.assertEqual(name, 'Writer')
    
    def test_writer_field_max_length(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Writer').max_length
        self.assertEqual(name, 300)
        
    def test_writer_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Writer').blank
        self.assertEqual(name, True)
        
    def test_writer_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Writer').null
        self.assertEqual(name, True)
        
    def test_actors_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Actors').verbose_name
        self.assertEqual(name, 'Actors')
        
    def test_actors_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Actors').blank
        self.assertEqual(name, True)
        
    def test_plot_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Plot').verbose_name
        self.assertEqual(name, 'Plot')
    
    def test_plot_field_max_length(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Plot').max_length
        self.assertEqual(name, 900)
        
    def test_plot_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Plot').blank
        self.assertEqual(name, True)
        
    def test_plot_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Plot').null
        self.assertEqual(name, True)
        
    def test_language_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Language').verbose_name
        self.assertEqual(name, 'Language')
    
    def test_language_field_max_length(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Language').max_length
        self.assertEqual(name, 300)
        
    def test_language_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Language').blank
        self.assertEqual(name, True)
        
    def test_language_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Language').null
        self.assertEqual(name, True)
        
    def test_country_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Country').verbose_name
        self.assertEqual(name, 'Country')
    
    def test_country_field_max_length(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Country').max_length
        self.assertEqual(name, 150)
        
    def test_country_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Country').blank
        self.assertEqual(name, True)
        
    def test_country_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Country').null
        self.assertEqual(name, True)
        
    def test_awards_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Awards').verbose_name
        self.assertEqual(name, 'Awards')
    
    def test_awards_field_max_length(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Awards').max_length
        self.assertEqual(name, 500)
        
    def test_awards_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Awards').blank
        self.assertEqual(name, True)
        
    def test_awards_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Awards').null
        self.assertEqual(name, True)
        
    def test_poster_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Poster').verbose_name
        self.assertEqual(name, 'Poster')
        
    def test_poster_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Poster').blank
        self.assertEqual(name, True)
        
    def test_poster_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Poster').null
        self.assertEqual(name, True)
    
    def test_poster_url_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Poster_url').verbose_name
        self.assertEqual(name, 'Poster url')
        
    def test_poster_url_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Poster_url').blank
        self.assertEqual(name, True)
        
    def test_poster_url_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Poster_url').null
        self.assertEqual(name, True)
        
    def test_ratings_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Ratings').verbose_name
        self.assertEqual(name, 'Ratings')
        
    def test_ratings_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Ratings').blank
        self.assertEqual(name, True)
        
    def test_metascore_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Metascore').verbose_name
        self.assertEqual(name, 'Metascore')
    
    def test_metascore_field_max_length(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Metascore').max_length
        self.assertEqual(name, 5)
        
    def test_metascore_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Metascore').blank
        self.assertEqual(name, True)
        
    def test_metascore_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Metascore').null
        self.assertEqual(name, True)
        
    def test_imdbrating_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('imdbRating').verbose_name
        self.assertEqual(name, 'imdbRating')
    
    def test_imdbrating_field_max_length(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('imdbRating').max_length
        self.assertEqual(name, 5)
        
    def test_imdbrating_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('imdbRating').blank
        self.assertEqual(name, True)
        
    def test_imdbrating_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('imdbRating').null
        self.assertEqual(name, True)
        
    def test_imdbvotes_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('imdbVotes').verbose_name
        self.assertEqual(name, 'imdbVotes')
    
    def test_imdbvotes_field_max_length(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('imdbVotes').max_length
        self.assertEqual(name, 100)
        
    def test_imdbvotes_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('imdbVotes').blank
        self.assertEqual(name, True)
        
    def test_imdbvotes_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('imdbVotes').null
        self.assertEqual(name, True)
        
    def test_imdbid_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('imdbID').verbose_name
        self.assertEqual(name, 'imdbID')
    
    def test_imdbid_field_max_length(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('imdbID').max_length
        self.assertEqual(name, 100)
        
    def test_imdbid_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('imdbID').blank
        self.assertEqual(name, True)
        
    def test_imdbid_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('imdbID').null
        self.assertEqual(name, True)
        
    def test_type_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Type').verbose_name
        self.assertEqual(name, 'Type')
    
    def test_type_field_max_length(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Type').max_length
        self.assertEqual(name, 10)
        
    def test_type_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Type').blank
        self.assertEqual(name, True)
        
    def test_type_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Type').null
        self.assertEqual(name, True)
        
    def test_dvd_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('DVD').verbose_name
        self.assertEqual(name, 'DVD')
    
    def test_dvd_field_max_length(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('DVD').max_length
        self.assertEqual(name, 25)
        
    def test_dvd_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('DVD').blank
        self.assertEqual(name, True)
        
    def test_dvd_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('DVD').null
        self.assertEqual(name, True)
        
    def test_boxoffice_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('BoxOffice').verbose_name
        self.assertEqual(name, 'BoxOffice')
    
    def test_boxoffice_field_max_length(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('BoxOffice').max_length
        self.assertEqual(name, 25)
        
    def test_boxoffice_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('BoxOffice').blank
        self.assertEqual(name, True)
        
    def test_boxoffice_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('BoxOffice').null
        self.assertEqual(name, True)
        
    def test_production_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Production').verbose_name
        self.assertEqual(name, 'Production')
    
    def test_production_field_max_length(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Production').max_length
        self.assertEqual(name, 25)
        
    def test_production_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Production').blank
        self.assertEqual(name, True)
        
    def test_production_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Production').null
        self.assertEqual(name, True)
        
    def test_website_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Website').verbose_name
        self.assertEqual(name, 'Website')
    
    def test_website_field_max_length(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Website').max_length
        self.assertEqual(name, 150)
        
    def test_website_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Website').blank
        self.assertEqual(name, True)
        
    def test_website_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('Website').null
        self.assertEqual(name, True)
        
    def test_totalseasons_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('totalSeasons').verbose_name
        self.assertEqual(name, 'totalSeasons')
    
    def test_totalseasons_field_max_length(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('totalSeasons').max_length
        self.assertEqual(name, 3)
        
    def test_totalseasons_field_blank(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('totalSeasons').blank
        self.assertEqual(name, True)
        
    def test_totalseasons_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('totalSeasons').null
        self.assertEqual(name, True)
        
    def test_timestamp_name_field(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('timestamp').verbose_name
        self.assertEqual(name, 'timestamp')
        
    def test_timestamp_field_auto_now_add(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('timestamp').auto_now_add
        self.assertEqual(name, True)
        
    def test_timestamp_field_null(self):
        movie = Movie.objects.get(id=1)
        name = movie._meta.get_field('timestamp').null
        self.assertEqual(name, True)
        
    def test_object_name(self):
        movie = Movie.objects.get(id=1)
        object_name = f'{movie.Title}'
        self.assertEqual(object_name, str(movie))
        
class GenreModelTestCase(TestCase):
    @classmethod
    def setUp(cls):
        genre = Genre.objects.create(title='Test', slug='test')
        
    def test_title_name_field(self):
        genre = Genre.objects.get(id=1)
        name = genre._meta.get_field('title').verbose_name
        self.assertEqual(name, 'title')
        
    def test_title_field_max_length(self):
        genre = Genre.objects.get(id=1)
        name = genre._meta.get_field('title').max_length
        self.assertEqual(name, 20)
        
    def test_slug_name_field(self):
        genre = Genre.objects.get(id=1)
        name = genre._meta.get_field('slug').verbose_name
        self.assertEqual(name, 'slug')
        
    def test_slug_field_null(self):
        genre = Genre.objects.get(id=1)
        name = genre._meta.get_field('slug').null
        self.assertEqual(name, False)
        
    def test_slug_field_unique(self):
        genre = Genre.objects.get(id=1)
        name = genre._meta.get_field('slug').unique
        self.assertEqual(name, True)
        
    def test_object_name(self):
        genre = Genre.objects.get(id=1)
        object_name = f'{genre.title}'
        self.assertEqual(object_name, str(genre))
        
    def test_get_absolute_url(self):
        genre = Genre.objects.get(id=1)
        self.assertEqual(genre.get_absolute_url(), '/movie/genre/test/')
        
class RatingModelTestCase(TestCase):
    @classmethod
    def setUp(cls):
        rating = Rating.objects.create(source='Test portal', rating='50%')
        
    def test_source_name_field(self):
        rating = Rating.objects.get(id=1)
        name = rating._meta.get_field('source').verbose_name
        self.assertEqual(name, 'source')
        
    def test_source_field_max_length(self):
        rating = Rating.objects.get(id=1)
        name = rating._meta.get_field('source').max_length
        self.assertEqual(name, 25)
        
    def test_rating_name_field(self):
        rating = Rating.objects.get(id=1)
        name = rating._meta.get_field('rating').verbose_name
        self.assertEqual(name, 'rating')
        
    def test_rating_field_max_length(self):
        rating = Rating.objects.get(id=1)
        name = rating._meta.get_field('rating').max_length
        self.assertEqual(name, 20)
        
    def test_object_name(self):
        rating = Rating.objects.get(id=1)
        object_name = f'{rating.source}'
        self.assertEqual(object_name, str(rating))
        
class MovieRatingModelTestCase(TestCase):
    @classmethod
    def setUp(cls):
        movie = Movie.objects.create(Title='Test', Poster='', Poster_url='')
        user = User.objects.create_user('test_user', password='test_user')
        movie_rating = MovieRating.objects.create(
            user=user, 
            movie=movie,
            opinion='test opinion',
            rate=8,
            likes=0,
            dislikes=0)
        
    def test_user_name_field(self):
        movie_rating = MovieRating.objects.get(id=1)
        name = movie_rating._meta.get_field('user').verbose_name
        self.assertEqual(name, 'user')
        
    def test_movie_name_field(self):
        movie_rating = MovieRating.objects.get(id=1)
        name = movie_rating._meta.get_field('movie').verbose_name
        self.assertEqual(name, 'movie')
        
    def test_date_name_field(self):
        movie_rating = MovieRating.objects.get(id=1)
        name = movie_rating._meta.get_field('date').verbose_name
        self.assertEqual(name, 'date')
        
    def test_date_field_auto_now_add(self):
        movie_rating = MovieRating.objects.get(id=1)
        name = movie_rating._meta.get_field('date').auto_now_add
        self.assertEqual(name, True)
        
    def test_opinion_name_field(self):
        movie_rating = MovieRating.objects.get(id=1)
        name = movie_rating._meta.get_field('opinion').verbose_name
        self.assertEqual(name, 'opinion')
        
    def test_opinion_field_max_length(self):
        movie_rating = MovieRating.objects.get(id=1)
        name = movie_rating._meta.get_field('opinion').max_length
        self.assertEqual(name, 300)
        
    def test_opinion_field_blank(self):
        movie_rating = MovieRating.objects.get(id=1)
        name = movie_rating._meta.get_field('opinion').blank
        self.assertEqual(name, True)
        
    def test_rate_name_field(self):
        movie_rating = MovieRating.objects.get(id=1)
        name = movie_rating._meta.get_field('rate').verbose_name
        self.assertEqual(name, 'rate')
        
    def test_rate_field_choices(self):
        movie_rating = MovieRating.objects.get(id=1)
        name = movie_rating._meta.get_field('rate').choices
        self.assertEqual(name, RATE)
        
    def test_likes_name_field(self):
        movie_rating = MovieRating.objects.get(id=1)
        name = movie_rating._meta.get_field('likes').verbose_name
        self.assertEqual(name, 'likes')
        
    def test_likes_field_default(self):
        movie_rating = MovieRating.objects.get(id=1)
        name = movie_rating._meta.get_field('likes').default
        self.assertEqual(name, 0)
        
    def test_dislikes_name_field(self):
        movie_rating = MovieRating.objects.get(id=1)
        name = movie_rating._meta.get_field('dislikes').verbose_name
        self.assertEqual(name, 'dislikes')
        
    def test_dislikes_field_default(self):
        movie_rating = MovieRating.objects.get(id=1)
        name = movie_rating._meta.get_field('dislikes').default
        self.assertEqual(name, 0)
        
    def test_timestamp_name_field(self):
        movie_rating = MovieRating.objects.get(id=1)
        name = movie_rating._meta.get_field('timestamp').verbose_name
        self.assertEqual(name, 'timestamp')
        
    def test_timestamp_field_auto_now_add(self):
        movie_rating = MovieRating.objects.get(id=1)
        name = movie_rating._meta.get_field('timestamp').auto_now_add
        self.assertEqual(name, True)
        
    def test_object_name(self):
        movie_rating = MovieRating.objects.get(id=1)
        object_name = f'{movie_rating.user.username}'
        self.assertEqual(object_name, str(movie_rating))
        
class LikeModelTestCase(TestCase):
    @classmethod
    def setUp(cls):
        movie = Movie.objects.create(Title='Test', Poster='', Poster_url='')
        user = User.objects.create_user('test_user', password='test_user')
        movie_rating = MovieRating.objects.create(
            user=user, 
            movie=movie,
            opinion='test opinion',
            rate=8,
            likes=0,
            dislikes=0)
        likes = Likes.objects.create(
            user=user,
            like_type=1,
            rating=movie_rating)
        
    def test_user_name_field(self):
        like = Likes.objects.get(id=1)
        name = like._meta.get_field('user').verbose_name
        self.assertEqual(name, 'user')
        
    def test_like_type_name_field(self):
        like = Likes.objects.get(id=1)
        name = like._meta.get_field('like_type').verbose_name
        self.assertEqual(name, 'like type')
        
    def test_rating_name_field(self):
        like = Likes.objects.get(id=1)
        name = like._meta.get_field('rating').verbose_name
        self.assertEqual(name, 'rating')
        
    def test_timestamp_name_field(self):
        like = Likes.objects.get(id=1)
        name = like._meta.get_field('timestamp').verbose_name
        self.assertEqual(name, 'timestamp')
        
    def test_timestamp_field_auto_now_add(self):
        like = Likes.objects.get(id=1)
        name = like._meta.get_field('timestamp').auto_now_add
        self.assertEqual(name, True)