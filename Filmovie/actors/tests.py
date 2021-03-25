"""Test cases for actors app"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Actor
from django.urls import reverse
from django.test import Client

User = get_user_model()

class EndpointTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test_user', password='test_user')
        self.actor = Actor.objects.create(name='Gal Gadot', slug='gal-gadot')
        
    def test_actor_url(self):
        slug = 'gal-gadot'
        res = self.client.get(reverse('actors', args=[slug]), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="profiles/actor.html")
