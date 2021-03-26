"""Test cases for MovieRateForm"""
from django.test import TestCase
from movies.forms import MovieRateForm
from movies.models import RATE


class MovieRateFormTestCase(TestCase):
    def test_movie_rate_form_opinion_label(self):
        form = MovieRateForm()
        self.assertEqual(form.fields['opinion'].label, None)
        
    def test_movie_rate_form_opinion_required(self):
        form = MovieRateForm()
        self.assertEqual(form.fields['opinion'].required, True)
        
    def test_movie_rate_form_opinion_min_length(self):
        form = MovieRateForm()
        self.assertEqual(form.fields['opinion'].min_length, 2)
        
    def test_movie_rate_form_rate_label(self):
        form = MovieRateForm()
        self.assertEqual(form.fields['rate'].label, None)
        
    def test_movie_rate_form_rate_required(self):
        form = MovieRateForm()
        self.assertEqual(form.fields['rate'].required, True)
        
    def test_movie_rate_form_rate_choices(self):
        form = MovieRateForm()
        self.assertEqual(form.fields['rate'].choices, RATE)
        
    def test_movie_rate_form_opinion_is_required(self):
        data = {'rate': RATE[5][1]}
        form = MovieRateForm(data = data)
        self.assertFalse(form.is_valid())
        
    def test_movie_rate_form_opinion_too_short(self):
        data = {'opinion': 'k', 'rate': RATE[5][1]}
        form = MovieRateForm(data = data)
        self.assertFalse(form.is_valid())
        
    def test_movie_rate_form_opinion_ok(self):
        data = {'opinion': 'test opinion', 'rate': RATE[5][1]}
        form = MovieRateForm(data = data)
        self.assertTrue(form.is_valid())
    
    def test_movie_rate_form_rate_is_required(self):
        data = {'opinion': 'test opinion'}
        form = MovieRateForm(data = data)
        self.assertFalse(form.is_valid())
        
    def test_movie_rate_form_rate_is_ok(self):
        data = {'opinion': 'test opinion', 'rate': RATE[5][1]}
        form = MovieRateForm(data = data)
        self.assertTrue(form.is_valid())