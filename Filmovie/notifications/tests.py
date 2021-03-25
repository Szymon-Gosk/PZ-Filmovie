from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse
from movies.models import Movie, MovieRating
from notifications.models import Notification
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
        self.movie_rating = MovieRating.objects.create(user=self.user, movie=self.movie, rate=8)
        self.notification = Notification.objects.create(executor=self.user1, receiver=self.user, text='test', url_name='')
        self.notification2 = Notification.objects.create(executor=self.user1, receiver=self.user, text='test', url_name='', imdb_id=self.movie.imdbID)
        self.imdb_id = self.movie.imdbID
        
    def test_notification_follow_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('notifications', args=[self.notification.id, self.user1.username, self.notification.imdb_id]), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="profiles/profile.html")
        
    def test_notification_rating_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('notifications', args=[self.notification2.id, self.user1.username, self.notification2.imdb_id]), follow=True)
        print(res)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="movies/movie_rating.html")