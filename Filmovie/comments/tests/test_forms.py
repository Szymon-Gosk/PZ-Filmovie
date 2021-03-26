"""Test cases for comments app"""
from django.test import TestCase
from comments.forms import CommentForm


class CommentFormTestCase(TestCase):
    def test_comment_form_text_label(self):
        form = CommentForm()
        self.assertEqual(form.fields['text'].label, None)
        
    def test_comment_form_text_required(self):
        form = CommentForm()
        self.assertEqual(form.fields['text'].required, True)
        
    def test_comment_form_text_min_length(self):
        form = CommentForm()
        self.assertEqual(form.fields['text'].min_length, 2)
        
    def test_comment_form_text_too_shor_text(self):
        data = {'text': 'k'}
        form = CommentForm(data = data)
        self.assertFalse(form.is_valid())
        
    def test_comment_form_text_ok(self):
        data = {'text': 'test comment'}
        form = CommentForm(data = data)
        self.assertTrue(form.is_valid())
        
    def test_comment_form_text_not_be_null(self):
        data = {'text': ''}
        form = CommentForm(data = data)
        self.assertFalse(form.is_valid())
    