from django import forms
from movies.models import MovieRating, RATE

class MovieRateForm(forms.ModelForm):
    opinion = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), required=True, min_length=2)
    rate = forms.ChoiceField(choices=RATE, widget=forms.Select(), required=True)

    class Meta:
        model = MovieRating
        fields = ('opinion', 'rate')
