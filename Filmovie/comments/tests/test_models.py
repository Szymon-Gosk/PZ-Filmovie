"""Test cases for comments app"""
from django.test import TestCase
from comments.models import Comment
from django.contrib.auth import get_user_model
from movies.models import MovieRating, Movie

User = get_user_model()


class CommentModelTestCase(TestCase):
    @classmethod
    def setUp(cls):
        movie = Movie.objects.create(Title='Test', Poster='', Poster_url='')
        user = User.objects.create_user('test_user', password='test_user')
        movie_rating = MovieRating.objects.create(user=user, movie=movie, rate=8)
        comment = Comment.objects.create(rating=movie_rating, user=user, text='test')
        
    def test_rating_name_field(self):
        comment = Comment.objects.get(id=1)
        name = comment._meta.get_field('rating').verbose_name
        self.assertEqual(name, 'rating')
        
    def test_user_name_field(self):
        comment = Comment.objects.get(id=1)
        name = comment._meta.get_field('user').verbose_name
        self.assertEqual(name, 'user')
        
    def test_text_name_field(self):
        comment = Comment.objects.get(id=1)
        name = comment._meta.get_field('text').verbose_name
        self.assertEqual(name, 'text')
        
    def test_text_field_max_length(self):
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field('text').max_length
        self.assertEqual(max_length, 200)
        
    def test_text_field_null(self):
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field('text').null
        self.assertEqual(max_length, True)
        
    def test_text_field_blank(self):
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field('text').blank
        self.assertEqual(max_length, True)
        
    def test_date_name_field(self):
        comment = Comment.objects.get(id=1)
        name = comment._meta.get_field('date').verbose_name
        self.assertEqual(name, 'date')
        
    def test_date_field_auto_add(self):
        comment = Comment.objects.get(id=1)
        name = comment._meta.get_field('date').auto_now_add
        self.assertEqual(name, True)
        
    def test_object_name(self):
        comment = Comment.objects.get(id=1)
        object_name = f'{comment.user.username}'
        self.assertEqual(object_name, str(comment))