"""Forms definitions for comments app"""
from django import forms
from comments.models import Comment


class CommentForm(forms.ModelForm):
    """Form for comments"""
    text = forms.CharField(required=True, min_length=2)

    class Meta:
        model = Comment
        fields = ('text',)