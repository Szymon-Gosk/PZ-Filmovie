"""Test cases for comments app"""
from django.test import TestCase
from users.forms import SignupForm, ChangePasswordForm, EditProfileForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupFormTestCase(TestCase):
    def test_signup_form_username_label(self):
        form = SignupForm()
        self.assertEqual(form.fields['username'].label, None)
        
    def test_signup_form_username_required(self):
        form = SignupForm()
        self.assertEqual(form.fields['username'].required, True)
        
    def test_signup_form_username_max_length(self):
        form = SignupForm()
        self.assertEqual(form.fields['username'].max_length, 25)
        
    def test_signup_form_first_name_label(self):
        form = SignupForm()
        self.assertEqual(form.fields['first_name'].label, None)
        
    def test_signup_form_first_name_required(self):
        form = SignupForm()
        self.assertEqual(form.fields['first_name'].required, True)
        
    def test_signup_form_first_name_max_length(self):
        form = SignupForm()
        self.assertEqual(form.fields['first_name'].max_length, 25)
        
    def test_signup_form_last_name_label(self):
        form = SignupForm()
        self.assertEqual(form.fields['last_name'].label, None)
        
    def test_signup_form_last_name_required(self):
        form = SignupForm()
        self.assertEqual(form.fields['last_name'].required, True)
        
    def test_signup_form_last_name_max_length(self):
        form = SignupForm()
        self.assertEqual(form.fields['last_name'].max_length, 25)
        
    def test_signup_form_email_label(self):
        form = SignupForm()
        self.assertEqual(form.fields['email'].label, None)
        
    def test_signup_form_email_required(self):
        form = SignupForm()
        self.assertEqual(form.fields['email'].required, True)
        
    def test_signup_form_email_max_length(self):
        form = SignupForm()
        self.assertEqual(form.fields['email'].max_length, 50)
        
    def test_signup_form_password_label(self):
        form = SignupForm()
        self.assertEqual(form.fields['password'].label, None)
        
    def test_signup_form_password_required(self):
        form = SignupForm()
        self.assertEqual(form.fields['password'].required, True)
        
    def test_signup_form_confirm_password_label(self):
        form = SignupForm()
        self.assertEqual(form.fields['confirm_password'].label, 'Confirm your password')
        
    def test_signup_form_confirm_password_required(self):
        form = SignupForm()
        self.assertEqual(form.fields['confirm_password'].required, True)
        
    def test_signup_form_username_too_long(self):
        data = {
            'username': 'halohalotssdkasdlkdalsdkasldkasfskdfhsdfs', 
            'first_name': 'Firstname',
            'last_name': 'Lastname',
            'email': 'test@emailk.com',
            'password': 'Password123!',
            'confirm_password': 'Password123!'
        }
        form = SignupForm(data = data)
        self.assertFalse(form.is_valid())
        
    def test_signup_form_username_is_restricted(self):
        data = {
            'username': 'test', 
            'first_name': 'Firstname',
            'last_name': 'Lastname',
            'email': 'test@emailk.com',
            'password': 'Password123!',
            'confirm_password': 'Password123!'
        }
        form = SignupForm(data = data)
        self.assertFalse(form.is_valid())
        
    def test_signup_form_username_has_special_character(self):
        data = {
            'username': 'johnny!', 
            'first_name': 'Firstname',
            'last_name': 'Lastname',
            'email': 'test@emailk.com',
            'password': 'Password123!',
            'confirm_password': 'Password123!'
        }
        form = SignupForm(data = data)
        self.assertFalse(form.is_valid())
        
    def test_signup_form_username_is_taken(self):
        User.objects.create_user(username='johnny', email='johnny@wp.pl', password='Password123!')
        data = {
            'username': 'johnny', 
            'first_name': 'Firstname',
            'last_name': 'Lastname',
            'email': 'test@emailk.com',
            'password': 'Password123!',
            'confirm_password': 'Password123!'
        }
        form = SignupForm(data = data)
        self.assertFalse(form.is_valid())
        
    def test_signup_form_username_is_ok(self):
        data = {
            'username': 'johnny', 
            'first_name': 'Firstname',
            'last_name': 'Lastname',
            'email': 'test@emailk.com',
            'password': 'Password123!',
            'confirm_password': 'Password123!'
        }
        form = SignupForm(data = data)
        self.assertTrue(form.is_valid())
        
    def test_signup_form_first_name_is_too_long(self):
        data = {
            'username': 'johnny', 
            'first_name': 'Firstnamefirstnamefirstnamefirstnamefirstname',
            'last_name': 'Lastname',
            'email': 'test@emailk.com',
            'password': 'Password123!',
            'confirm_password': 'Password123!'
        }
        form = SignupForm(data = data)
        self.assertFalse(form.is_valid())
        
    def test_signup_form_first_name_is_ok(self):
        data = {
            'username': 'johnny', 
            'first_name': 'Firstname',
            'last_name': 'Lastname',
            'email': 'test@emailk.com',
            'password': 'Password123!',
            'confirm_password': 'Password123!'
        }
        form = SignupForm(data = data)
        self.assertTrue(form.is_valid())
        
    def test_signup_form_last_name_is_too_long(self):
        data = {
            'username': 'johnny', 
            'first_name': 'Firstname',
            'last_name': 'Lastnamelastnamelastnamelastnamelastnamelastnamelastnamelastname',
            'email': 'test@emailk.com',
            'password': 'Password123!',
            'confirm_password': 'Password123!'
        }
        form = SignupForm(data = data)
        self.assertFalse(form.is_valid())
        
    def test_signup_form_last_name_is_ok(self):
        data = {
            'username': 'johnny', 
            'first_name': 'Firstname',
            'last_name': 'Lastname',
            'email': 'test@emailk.com',
            'password': 'Password123!',
            'confirm_password': 'Password123!'
        }
        form = SignupForm(data = data)
        self.assertTrue(form.is_valid())
        
    def test_signup_form_email_is_invalid(self):
        data = {
            'username': 'johnny', 
            'first_name': 'Firstname',
            'last_name': 'Lastname',
            'email': 'testemailk.com',
            'password': 'Password123!',
            'confirm_password': 'Password123!'
        }
        form = SignupForm(data = data)
        self.assertFalse(form.is_valid())
        
    def test_signup_form_email_is_taken(self):
        User.objects.create_user(username='johnny123', email='johnny@wp.pl', password='Password123!')
        data = {
            'username': 'johnny', 
            'first_name': 'Firstname',
            'last_name': 'Lastname',
            'email': 'johnny@wp.pl',
            'password': 'Password123!',
            'confirm_password': 'Password123!'
        }
        form = SignupForm(data = data)
        self.assertFalse(form.is_valid())
        
    def test_signup_form_email_is_ok(self):
        data = {
            'username': 'johnny', 
            'first_name': 'Firstname',
            'last_name': 'Lastname',
            'email': 'test@emailk.com',
            'password': 'Password123!',
            'confirm_password': 'Password123!'
        }
        form = SignupForm(data = data)
        self.assertTrue(form.is_valid())
        
    def test_signup_form_password_do_not_match(self):
        data = {
            'username': 'johnny', 
            'first_name': 'Firstname',
            'last_name': 'Lastname',
            'email': 'test@emailk.com',
            'password': 'Password123!',
            'confirm_password': 'Password123'
        }
        form = SignupForm(data = data)
        self.assertFalse(form.is_valid())
        
    def test_signup_form_password_do_match(self):
        data = {
            'username': 'johnny', 
            'first_name': 'Firstname',
            'last_name': 'Lastname',
            'email': 'test@emailk.com',
            'password': 'Password123!',
            'confirm_password': 'Password123!'
        }
        form = SignupForm(data = data)
        self.assertTrue(form.is_valid())
        
class ChangePasswordFormTestCase(TestCase):
    def test_change_password_form_id_label(self):
        form = ChangePasswordForm()
        self.assertEqual(form.fields['id'].label, None)
        
    def test_change_password_form_old_password_label(self):
        form = ChangePasswordForm()
        self.assertEqual(form.fields['old_password'].label, 'Old password')
        
    def test_change_password_form_old_password_required(self):
        form = ChangePasswordForm()
        self.assertEqual(form.fields['old_password'].required, True)
        
    def test_change_password_form_new_password_label(self):
        form = ChangePasswordForm()
        self.assertEqual(form.fields['new_password'].label, 'New password')
        
    def test_change_password_form_new_password_required(self):
        form = ChangePasswordForm()
        self.assertEqual(form.fields['new_password'].required, True)
        
    def test_change_password_form_confirm_new_password_label(self):
        form = ChangePasswordForm()
        self.assertEqual(form.fields['confirm_new_password'].label, 'Confirm new password')
        
    def test_change_password_form_confirm_new_password_required(self):
        form = ChangePasswordForm()
        self.assertEqual(form.fields['confirm_new_password'].required, True)
        
    def test_change_password_form_old_password_do_match(self):
        user = User.objects.create_user(username='johnny', email='johnny@wp.pl', password='Password123!')
        data = {
            'id': user.id, 
            'old_password': 'Password',
            'new_password': 'Password123',
            'confirm_new_password': 'Password123'
        }
        form = ChangePasswordForm(data = data)
        self.assertFalse(form.is_valid())
        
    def test_change_password_form_old_password_ok(self):
        user = User.objects.create_user(username='johnny', email='johnny@wp.pl', password='Password123!')
        data = {
            'id': user.id, 
            'old_password': 'Password123!',
            'new_password': 'Password123',
            'confirm_new_password': 'Password123'
        }
        form = ChangePasswordForm(data = data)
        self.assertTrue(form.is_valid())
        
    def test_change_password_form_new_password_do_not_match(self):
        user = User.objects.create_user(username='johnny', email='johnny@wp.pl', password='Password123!')
        data = {
            'id': user.id, 
            'old_password': 'Password123!',
            'new_password': 'Password12345',
            'confirm_new_password': 'Password1234'
        }
        form = ChangePasswordForm(data = data)
        self.assertFalse(form.is_valid())
        
    def test_change_password_form_new_password_do_match(self):
        user = User.objects.create_user(username='johnny', email='johnny@wp.pl', password='Password123!')
        data = {
            'id': user.id, 
            'old_password': 'Password123!',
            'new_password': 'Password12345',
            'confirm_new_password': 'Password12345'
        }
        form = ChangePasswordForm(data = data)
        self.assertTrue(form.is_valid())
        
class EditProfileFormTestCase(TestCase):
    def test_edit_profile_form_picture_label(self):
        form = EditProfileForm()
        self.assertEqual(form.fields['picture'].label, None)
        
    def test_edit_profile_form_picture_required(self):
        form = EditProfileForm()
        self.assertEqual(form.fields['picture'].required, False)
        
    def test_edit_profile_form_background_label(self):
        form = EditProfileForm()
        self.assertEqual(form.fields['background'].label, None)
        
    def test_edit_profile_form_background_required(self):
        form = EditProfileForm()
        self.assertEqual(form.fields['background'].required, False)
        
    def test_edit_profile_form_first_name_label(self):
        form = EditProfileForm()
        self.assertEqual(form.fields['first_name'].label, None)
        
    def test_edit_profile_form_first_name_required(self):
        form = EditProfileForm()
        self.assertEqual(form.fields['first_name'].required, False)
        
    def test_edit_profile_form_first_name_max_length(self):
        form = EditProfileForm()
        self.assertEqual(form.fields['first_name'].max_length, 25)
        
    def test_edit_profile_form_last_name_label(self):
        form = EditProfileForm()
        self.assertEqual(form.fields['last_name'].label, None)
        
    def test_edit_profile_form_last_name_required(self):
        form = EditProfileForm()
        self.assertEqual(form.fields['last_name'].required, False)
        
    def test_edit_profile_form_last_name_max_length(self):
        form = EditProfileForm()
        self.assertEqual(form.fields['last_name'].max_length, 25)
        
    def test_edit_profile_form_bio_label(self):
        form = EditProfileForm()
        self.assertEqual(form.fields['bio'].label, None)
        
    def test_edit_profile_form_bio_required(self):
        form = EditProfileForm()
        self.assertEqual(form.fields['bio'].required, False)
        
    def test_edit_profile_form_bio_max_length(self):
        form = EditProfileForm()
        self.assertEqual(form.fields['bio'].max_length, 200)
        
    def test_edit_profile_form_first_name_is_too_long(self):
        data = {
            'first_name': 'Johnnyjohnnyjohnnyjohnnyjohnny',
            'last_name': 'Nowak',
            'bio': 'mybiobiobio'
        }
        form = EditProfileForm(data = data)
        self.assertFalse(form.is_valid())
        
    def test_edit_profile_form_first_name_ok(self):
        data = {
            'first_name': 'Johnny',
            'last_name': 'Nowak',
            'bio': 'mybiobiobio'
        }
        form = EditProfileForm(data = data)
        self.assertTrue(form.is_valid())
        
    def test_edit_profile_form_last_name_is_too_long(self):
        data = {
            'first_name': 'Johnny',
            'last_name': 'NowakNowakNowakNowakNowakNowak',
            'bio': 'mybiobiobio'
        }
        form = EditProfileForm(data = data)
        self.assertFalse(form.is_valid())
        
    def test_edit_profile_form_last_name_ok(self):
        data = {
            'first_name': 'Johnny',
            'last_name': 'Nowak',
            'bio': 'mybiobiobio'
        }
        form = EditProfileForm(data = data)
        self.assertTrue(form.is_valid())
        
    def test_edit_profile_form_bio_is_too_long(self):
        data = {
            'first_name': 'Johnny',
            'last_name': 'Nowak',
            'bio': 'mybiobiobiomybiobiomybiobiobiomybiobiobiomybiobiobiomybiob' +
            'iobiomybiobiobiobiomybiobiobiomybiobiobiomybiobiobiomybiobiobiomy' +
            'biobiobiomybiobiobiomybiobiobiomybiobiobiomybiobiobiomybiobiobiom' +
            'ybiobiobiomybiobiobiomybiobiobiomybiobiobiomybiobiobio'
        }
        form = EditProfileForm(data = data)
        self.assertFalse(form.is_valid())
        
    def test_edit_profile_form_bio_ok(self):
        data = {
            'first_name': 'Johnny',
            'last_name': 'Nowak',
            'bio': 'mybiobiobiomybiobiomybiobiobiomybiobiobiomybiobiobiomybiob'
        }
        form = EditProfileForm(data = data)
        self.assertTrue(form.is_valid())