"""Models definitions for comments app"""
from django.db import models
from movies.models import MovieRating
from django.contrib.auth.models import User


class Comment(models.Model):
    """Model for comments"""
    rating = models.ForeignKey(MovieRating, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username