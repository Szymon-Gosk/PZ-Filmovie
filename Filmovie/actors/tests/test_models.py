"""Test cases for actors app"""
from django.test import TestCase
from actors.models import Actor
from movies.models import Movie


class ActorModelTestCase(TestCase):
    @classmethod
    def setUp(cls):
        movie = Movie.objects.create(Title='Test', Poster='', Poster_url='')
        actor = Actor.objects.create(
            name='Test Test',
            slug='test-test',
        )
        actor.movies.add(movie)
        
    def test_name_name_field(self):
        actor = Actor.objects.get(id=1)
        name = actor._meta.get_field('name').verbose_name
        self.assertEqual(name, 'name')
        
    def test_name_field_max_legnth(self):
        actor = Actor.objects.get(id=1)
        name = actor._meta.get_field('name').max_length
        self.assertEqual(name, 80)
        
    def test_name_field_unique(self):
        actor = Actor.objects.get(id=1)
        name = actor._meta.get_field('name').unique
        self.assertEqual(name, True)
        
    def test_slug_name_field(self):
        actor = Actor.objects.get(id=1)
        slug = actor._meta.get_field('slug').verbose_name
        self.assertEqual(slug, 'slug')
        
    def test_slug_field_null(self):
        actor = Actor.objects.get(id=1)
        slug = actor._meta.get_field('slug').null
        self.assertEqual(slug, True)
        
    def test_slug_field_blank(self):
        actor = Actor.objects.get(id=1)
        slug = actor._meta.get_field('slug').blank
        self.assertEqual(slug, True)
        
    def test_slug_field_unique(self):
        actor = Actor.objects.get(id=1)
        slug = actor._meta.get_field('slug').unique
        self.assertEqual(slug, True)
        
    def test_movies_name_field(self):
        actor = Actor.objects.get(id=1)
        movies = actor._meta.get_field('movies').verbose_name
        self.assertEqual(movies, 'movies')
        
    def test_object_name(self):
        actor = Actor.objects.get(id=1)
        object_name = f'{actor.name}'
        self.assertEqual(object_name, str(actor))
        
    def test_get_absolute_url(self):
        actor = Actor.objects.get(id=1)
        self.assertEqual(actor.get_absolute_url(), '/actors/test-test')