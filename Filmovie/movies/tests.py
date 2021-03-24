"""Test cases for movies app"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import MovieRating, Movie, Likes

User = get_user_model()


class LikesTestCase(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(username="test1", password="test1")
        self.user2 = User.objects.create(username="test2", password="test2")
        self.user3 = User.objects.create(username="test3", password="test3")
        self.movie = Movie.objects.create(Title="test", Poster='', Poster_url='')
        self.rating = MovieRating.objects.create(user=self.user1, movie = self.movie, rate=2)
        
    def test_liking(self):
        first = self.user1
        second = self.user2
        third = self.user3
        rating = self.rating
        Likes.objects.create(user=second, rating=rating, like_type=1)
        Likes.objects.create(user=third, rating=rating, like_type=1)
        self.assertEqual(Likes.objects.filter(rating=rating, like_type=1).count(), 2)
        
    def test_disliking(self):
        first = self.user1
        second = self.user2
        third = self.user3
        rating = self.rating
        Likes.objects.create(user=second, rating=rating, like_type=2)
        Likes.objects.create(user=third, rating=rating, like_type=2)
        self.assertEqual(Likes.objects.filter(rating=rating, like_type=2).count(), 2)
