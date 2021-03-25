"""Test cases for comments app"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from users.models import Profile
from movies.models import Movie

User = get_user_model()


class ProfileModelTestCase(TestCase):
    @classmethod
    def setUp(cls):
        user = User.objects.create_user('test_user', password='test_user')
        user2 = User.objects.create_user('test_user2', password='test_user2')
        movie = Movie.objects.create(Title='Test', Poster='', Poster_url='')
        profile = Profile.objects.filter(user=user).get()
        profile.star.add(movie)
        profile.watchlist.add(movie)
        profile.watchedlist.add(movie)
        profile.followers.add(user2)
        
    def test_user_name_field(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('user').verbose_name
        self.assertEqual(name, 'user')
        
    def test_first_name_name_field(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('first_name').verbose_name
        self.assertEqual(name, 'first name')
        
    def test_first_name_field_max_length(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('first_name').max_length
        self.assertEqual(name, 25)
        
    def test_first_name_field_blank(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('first_name').blank
        self.assertEqual(name, True)
        
    def test_first_name_field_null(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('first_name').null
        self.assertEqual(name, True)
        
    def test_last_name_name_field(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('last_name').verbose_name
        self.assertEqual(name, 'last name')
        
    def test_last_name_field_max_length(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('last_name').max_length
        self.assertEqual(name, 25)
        
    def test_last_name_field_blank(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('last_name').blank
        self.assertEqual(name, True)
        
    def test_last_name_field_null(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('last_name').null
        self.assertEqual(name, True)
        
    def test_bio_name_field(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('bio').verbose_name
        self.assertEqual(name, 'bio')
        
    def test_bio_field_max_length(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('bio').max_length
        self.assertEqual(name, 200)
        
    def test_bio_field_blank(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('bio').blank
        self.assertEqual(name, True)
        
    def test_bio_field_null(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('bio').null
        self.assertEqual(name, True)
        
    def test_created_name_field(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('created').verbose_name
        self.assertEqual(name, 'created')
        
    def test_created_field_auto_now_add(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('created').auto_now_add
        self.assertEqual(name, True)
        
    def test_star_name_field(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('star').verbose_name
        self.assertEqual(name, 'star')
        
    def test_watchlist_name_field(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('watchlist').verbose_name
        self.assertEqual(name, 'watchlist')
        
    def test_watchedlist_name_field(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('watchedlist').verbose_name
        self.assertEqual(name, 'watchedlist')
        
    def test_picture_name_field(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('picture').verbose_name
        self.assertEqual(name, 'picture')
        
    def test_picture_field_blank(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('picture').blank
        self.assertEqual(name, True)
        
    def test_picture_field_null(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('picture').null
        self.assertEqual(name, True)
        
    def test_background_name_field(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('background').verbose_name
        self.assertEqual(name, 'background')
        
    def test_background_field_blank(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('background').blank
        self.assertEqual(name, True)
        
    def test_background_field_null(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('background').null
        self.assertEqual(name, True)
        
    def test_followers_name_field(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('followers').verbose_name
        self.assertEqual(name, 'followers')
        
    def test_timestamp_name_field(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('timestamp').verbose_name
        self.assertEqual(name, 'timestamp')
        
    def test_timestamp_field_auto_now_add(self):
        profile = Profile.objects.get(id=1)
        name = profile._meta.get_field('timestamp').auto_now_add
        self.assertEqual(name, True)
        
    def test_object_name(self):
        profile = Profile.objects.get(id=1)
        object_name = f'{profile.user.username}'
        self.assertEqual(object_name, str(profile))