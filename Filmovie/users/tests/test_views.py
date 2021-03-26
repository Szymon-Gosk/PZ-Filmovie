"""Test cases for users app"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse
from users.models import Profile
from django.test import Client

User = get_user_model()

class EndpointsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test_user', password='test_user')
        
    def test_login_url(self):
        res = self.client.get(reverse('login'), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="auth/login.html")
        
    def test_logout_url(self):
        res = self.client.get(reverse('logout'), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="auth/login.html")
        
    def test_signup_url(self):
        res = self.client.get(reverse('signup'), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="auth/register.html")
        
    def test_edit_profile_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('profile-edit'), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="profiles/edit_profile.html")
        
    def test_profile_settings_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('profile-settings'), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="profiles/settings.html")
        
    def test_change_password_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('change-password'), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="auth/change_password.html")
        
    def test_change_password_done_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('change-password-done'), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="auth/change_password_done.html")
        
    def test_reset_password_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('password_reset'), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="registration/password_reset_form.html")
        
    def test_reset_password_done_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('password_reset_done'), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="registration/password_reset_done.html")
        
    def test_reset_password_confirm_url(self):
        token = 'soemtoken23123'
        uidb64 = 'someuidb64'
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('password_reset_confirm', args=[uidb64, token]), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="registration/password_reset_confirm.html")
        
    def test_reset_password_complete_url(self):
        self.client.login(username='test_user', password='test_user')
        res = self.client.get(reverse('password_reset_complete'), follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name="registration/password_reset_complete.html")