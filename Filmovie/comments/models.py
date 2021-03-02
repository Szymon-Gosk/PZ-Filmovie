from django.db import models
from movies.models import MovieRating
from django.contrib.auth.models import User


class Comment(models.Model):
    rating = models.ForeignKey(MovieRating, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
