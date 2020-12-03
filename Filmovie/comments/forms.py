from django import forms
from comments.models import Comment

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), required=False)

    class Meta:
        model = Comment
        fields = ('text',)