from django import forms
from movies.models import MovieRating, RATE


class MovieRateForm(forms.ModelForm):
    """Form for rating of a movie"""
    opinion = forms.CharField(required=True, min_length=2)
    rate = forms.ChoiceField(choices=RATE, required=True)

    class Meta:
        model = MovieRating
        fields = ('opinion', 'rate')