"""Test cases for movies app"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import MovieRating, Movie, Likes

User = get_user_model()


from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse
from movies.models import Movie, MovieRating, Genre
from django.test import Client

User = get_user_model()

class EndpointsTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="test1", password="test1")
        self.user2 = User.objects.create(username="test2", password="test2")
        self.client = Client()
        self.user = User.objects.create_user('test_user', password='test_user')
        self.movie = Movie.objects.create(
            imdbID="tt10813940",
            Title='test', 
            Poster='movies/MV5BMTQ2ZWFlNmEtNWYyYy00Yjk1LWIxMTEtMWVkM2NlMTEzOGI2XkEyXkFqcGdeQXVyMTEyMjM2NDc2._QB6Lem0.jpg', 
            Poster_url='https://m.media-amazon.com/images/M/MV5BMTQ2ZWFlNmEtNWYyYy00Yjk1LWIxMTEtMWVkM2NlMTEzOGI2XkEyXkFqcGdeQXVyMTEyMjM2NDc2._V1_SX300.jpg')
        self.genre = Genre.objects.create(title='Adventure', slug='adventure')
        self.movie_rating = MovieRating.objects.create(user=self.user1, movie=self.movie, rate=8)
        self.imdb_id = self.movie.imdbID
        self.genre_slug = self.genre.slug
        
    def test_home_movie_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('home'), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="home.html")
        
    def test_pagination_url(self):
        query = 'movie'
        page_number = 1
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('pagination', args=[query, page_number]), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="movies/search_result.html")
        
    def test_movie_details_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('movie-details', args=[self.imdb_id]), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="movies/movie_detail.html")
        
    def test_star_movie_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('star', args=[self.imdb_id]), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="movies/movie_detail.html")
        
    def test_watchlist_movie_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('watchlist', args=[self.imdb_id]), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="movies/movie_detail.html")
        
    def test_watchedlist_movie_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('watchedlist', args=[self.imdb_id]), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="movies/movie_detail.html")
        
    def test_genres_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('genres', args=[self.genre_slug]), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="movies/genre.html")
        
    def test_type_url(self):
        movie_type = 'movie'
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('type', args=[movie_type]), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="movies/genre.html")
        
    def test_rate_movie_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('rate-movie', args=[self.imdb_id]), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="movies/rate.html")