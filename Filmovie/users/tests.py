"""Test cases for users app"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class ProfileTestCase(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(username="test1", password="test1")
        self.user2 = User.objects.create(username="test2", password="test2")
        
    def test_profile_created_via_signal(self):
        qs = Profile.objects.all()
        self.assertEqual(qs.count(), 2)
        
    def test_following(self):
        first = self.user1
        second = self.user2
        # first_profile = first.profile.followers.add(second)
        second_user_following_whom = second.following.all()
        qs = second_user_following_whom.filter(user=first)
        first_user_following_no_one = first.following.all()
        self.assertTrue(qs.exists())
        self.assertFalse(first_user_following_no_one.exists())