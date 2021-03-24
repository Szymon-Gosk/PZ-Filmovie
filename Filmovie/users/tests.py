"""Test cases for users app"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse
from .models import Profile
from django.test import Client

User = get_user_model()


class ProfileTestCase(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(username="test1", password="test1")
        self.user2 = User.objects.create(username="test2", password="test2")
        self.client = Client()
        self.user = User.objects.create_user('test_user', password='test_user')
        
    def test_profile_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get('/user/%s' % (self.user1.username), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="profiles/profile.html")
        
    def test_follow_profile_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get('/user/%s/follow' % (self.user1.username), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="profiles/profile.html")
        
    def test_followers_profile_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get('/user/%s/followers' % (self.user1.username), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="profiles/profile.html")
        
    def test_following_profile_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get('/user/%s/following' % (self.user1.username), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="profiles/profile.html")
        
    def test_star_movies_profile_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get('/user/%s/star-movies' % (self.user1.username), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="profiles/profile.html")
        
    def test_star_series_profile_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get('/user/%s/star-series' % (self.user1.username), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="profiles/profile.html")
        
    def test_watchlist_profile_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get('/user/%s/watchlist' % (self.user1.username), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="profiles/profile.html")
        
    def test_watchedlist_profile_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get('/user/%s/watchedlist' % (self.user1.username), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="profiles/profile.html")
        
    def test_profile_created_via_signal(self):
        qs = Profile.objects.all()
        self.assertEqual(qs.count(), 3)
        
    def test_following(self):
        first = self.user1
        second = self.user2
        first_profile = first.profile.followers.add(second)
        second_user_following_whom = second.following.all()
        qs = second_user_following_whom.filter(user=first)
        first_user_following_no_one = first.following.all()
        self.assertTrue(qs.exists())
        self.assertFalse(first_user_following_no_one.exists())
        

class SignUpTest(TestCase):
    def setUp(self) -> None:
        self.username = 'test'
        self.first_name = 'test'
        self.last_name = 'test'
        self.email = 'test@test.pl'
        self.password = 'Password123!@#'
        self.confirm_password = 'Password123!@#'
        
    def test_login_url(self):
        res = self.client.get(reverse('login'), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="auth/login.html")
        
    def test_signup_url(self):
        res = self.client.get(reverse('signup'), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="auth/register.html")
        