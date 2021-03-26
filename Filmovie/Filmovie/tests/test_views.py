"""Test cases for users app"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse
from movies.models import Movie, MovieRating
from django.core.paginator import Paginator
from users.models import Profile
from django.test import Client

User = get_user_model()

class EndpointsTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="test1", password="test1")
        self.client = Client()
        self.user = User.objects.create_user('test_user', password='test_user')
        self.movie = Movie.objects.create(
            imdbID="tt0451279",
            Title='test', 
            Poster='movies/MV5BMTYzODQzYjQtNTczNC00MzZhLTg1ZWYtZDUxYmQ3ZTY4NzA1XkEyXkFqcGdeQXVyODE5NzE3OTE._V1_SX300.jpg', 
            Poster_url='https://m.media-amazon.com/images/M/MV5BMTYzODQzYjQtNTczNC00MzZhLTg1ZWYtZDUxYmQ3ZTY4NzA1XkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_SX300.jpg')
        self.movie_rating = MovieRating.objects.create(user=self.user1, movie=self.movie, rate=8)
        self.imdb_id = self.movie.imdbID
        
    def test_home_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('home-page'), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="index.html")
        
    def test_search_users_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('search-users'), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="users/search_users.html")
        
    def test_user_activities_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('user-activities'), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="users/user_activities.html")

    def test_profile_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('profile', args=[self.user1.username]), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="profiles/profile.html")
        
    def test_follow_profile_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('follow', args=[self.user1.username]), follow=True)
        followers = Profile.objects.get(user=self.user1).followers.all().count()
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="profiles/profile.html")
        self.assertTrue(followers == 1)
        
    def test_followers_profile_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('followers', args=[self.user1.username]), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['list_title'], 'Followers')
        self.assertEqual(type(res.context['movie_data']), type([]))
        self.assertTemplateUsed(res, template_name="profiles/profile.html")
        
    def test_following_profile_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('following', args=[self.user1.username]), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['list_title'], 'Following')
        self.assertEqual(type(res.context['movie_data']), type([]))
        self.assertTemplateUsed(res, template_name="profiles/profile.html")
        
    def test_star_movies_profile_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('user-star-movies', args=[self.user1.username]), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['list_title'], 'Favourite movies')
        self.assertEqual(type(res.context['movie_data']), type(Paginator([],1).get_page(1)))
        self.assertTemplateUsed(res, template_name="profiles/profile.html")
        
    def test_star_series_profile_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('user-star-series', args=[self.user1.username]), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['list_title'], 'Favourite series')
        self.assertEqual(type(res.context['movie_data']), type(Paginator([],1).get_page(1)))
        self.assertTemplateUsed(res, template_name="profiles/profile.html")
        
    def test_watchlist_profile_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('user-watchlist', args=[self.user1.username]), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['list_title'], 'Watchlist')
        self.assertEqual(type(res.context['movie_data']), type(Paginator([],1).get_page(1)))
        self.assertTemplateUsed(res, template_name="profiles/profile.html")
        
    def test_watchedlist_profile_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('user-watchedlist', args=[self.user1.username]), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['list_title'], 'Watchedlist')
        self.assertEqual(type(res.context['movie_data']), type(Paginator([],1).get_page(1)))
        self.assertTemplateUsed(res, template_name="profiles/profile.html")
        
    def test_reviews_profile_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('user-reviews', args=[self.user1.username]), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['list_title'], 'Reviewed')
        self.assertEqual(type(res.context['movie_data']), type(Paginator([],1).get_page(1)))
        self.assertTemplateUsed(res, template_name="profiles/profile.html")
        
    def test_user_rating_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('user-rating', args=[self.user1.username, self.imdb_id]), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="movies/movie_rating.html")