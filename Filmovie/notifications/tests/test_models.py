"""Test cases for comments app"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from notifications.models import Notification

User = get_user_model()


class NotificationModelTestCase(TestCase):
    @classmethod
    def setUp(cls):
        user = User.objects.create_user('test_user', password='test_user')
        user2 = User.objects.create_user('test_user2', password='test_user2')
        notification = Notification.objects.create(
            executor=user2,
            receiver=user,
            text='test',
            url_name='test url',
            imdb_id='test imdbID'
        )
        
    def test_executor_name_field(self):
        notification = Notification.objects.get(id=1)
        name = notification._meta.get_field('executor').verbose_name
        self.assertEqual(name, 'executor')
        
    def test_receiver_name_field(self):
        notification = Notification.objects.get(id=1)
        name = notification._meta.get_field('receiver').verbose_name
        self.assertEqual(name, 'receiver')
        
    def test_text_name_field(self):
        notification = Notification.objects.get(id=1)
        name = notification._meta.get_field('text').verbose_name
        self.assertEqual(name, 'text')
        
    def test_text_field_max_length(self):
        notification = Notification.objects.get(id=1)
        name = notification._meta.get_field('text').max_length
        self.assertEqual(name, 300)
        
    def test_text_field_null(self):
        notification = Notification.objects.get(id=1)
        name = notification._meta.get_field('text').null
        self.assertEqual(name, True)
        
    def test_text_field_blank(self):
        notification = Notification.objects.get(id=1)
        name = notification._meta.get_field('text').blank
        self.assertEqual(name, True)
        
    def test_url_name_name_field(self):
        notification = Notification.objects.get(id=1)
        name = notification._meta.get_field('url_name').verbose_name
        self.assertEqual(name, 'url name')
        
    def test_url_name_field_max_length(self):
        notification = Notification.objects.get(id=1)
        name = notification._meta.get_field('url_name').max_length
        self.assertEqual(name, 50)
        
    def test_url_name_field_null(self):
        notification = Notification.objects.get(id=1)
        name = notification._meta.get_field('url_name').null
        self.assertEqual(name, True)
        
    def test_url_name_field_blank(self):
        notification = Notification.objects.get(id=1)
        name = notification._meta.get_field('url_name').blank
        self.assertEqual(name, True)
        
    def test_imdb_id_name_field(self):
        notification = Notification.objects.get(id=1)
        name = notification._meta.get_field('imdb_id').verbose_name
        self.assertEqual(name, 'imdb id')
        
    def test_imdb_id_field_max_length(self):
        notification = Notification.objects.get(id=1)
        name = notification._meta.get_field('imdb_id').max_length
        self.assertEqual(name, 50)
        
    def test_imdb_id_field_null(self):
        notification = Notification.objects.get(id=1)
        name = notification._meta.get_field('imdb_id').null
        self.assertEqual(name, True)
        
    def test_imdb_id_field_blank(self):
        notification = Notification.objects.get(id=1)
        name = notification._meta.get_field('imdb_id').blank
        self.assertEqual(name, True)
        
    def test_timestamp_name_field(self):
        notification = Notification.objects.get(id=1)
        name = notification._meta.get_field('timestamp').verbose_name
        self.assertEqual(name, 'timestamp')
        
    def test_timestamp_field_auto_now_add(self):
        notification = Notification.objects.get(id=1)
        name = notification._meta.get_field('timestamp').auto_now_add
        self.assertEqual(name, True)
        
    def test_timestamp_field_null(self):
        notification = Notification.objects.get(id=1)
        name = notification._meta.get_field('timestamp').null
        self.assertEqual(name, True)
        
    def test_object_name(self):
        notification = Notification.objects.get(id=1)
        object_name = f'{notification.receiver.username}'
        self.assertEqual(object_name, str(notification))