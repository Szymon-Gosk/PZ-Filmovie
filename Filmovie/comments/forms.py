from django import forms
from comments.models import Comment


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), required=True, min_length=2)

    class Meta:
        model = Comment
        fields = ('text',)
