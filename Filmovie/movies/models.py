"""Models definitions for movies app"""
from io import BytesIO
from django.db import models
from django.utils.text import slugify
from django.core import files
from django.urls import reverse
from actors.models import Actor
from django.contrib.auth.models import User
import requests


RATE = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
]

class Genre(models.Model):
    """Genre model"""
    title = models.CharField(max_length=20)
    slug = models.SlugField(null=False, unique=True)

    def get_absolute_url(self):
        return reverse('genres', args=[self.slug])

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Returning slug (lower_case name of the field) used in urls"""
        if not self.slug:
            self.title.replace(" ", "")
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Rating(models.Model):
    """Rating model"""
    source = models.CharField(max_length=25)
    rating = models.CharField(max_length=20)

class Movie(models.Model):
    """Movie model"""
    Title = models.CharField(max_length=150, null=True)
    Year = models.CharField(max_length=25, blank=True, null=True)
    Rated = models.CharField(max_length=10, blank=True, null=True)
    Released = models.CharField(max_length=25, blank=True, null=True)
    Runtime = models.CharField(max_length=25, blank=True, null=True)
    Genre = models.ManyToManyField(Genre, blank=True)
    Director = models.CharField(max_length=100, blank=True, null=True)
    Writer = models.CharField(max_length=300, blank=True, null=True)
    Actors = models.ManyToManyField(Actor, blank=True)
    Plot = models.CharField(max_length=900, blank=True, null=True)
    Language = models.CharField(max_length=300, blank=True, null=True)
    Country = models.CharField(max_length=150, blank=True, null=True)
    Awards = models.CharField(max_length=500, blank=True, null=True)
    Poster = models.ImageField(upload_to='movies', blank=True, null=True)
    Poster_url = models.URLField(blank=True, null=True)
    Ratings = models.ManyToManyField(Rating, blank=True)
    Metascore = models.CharField(max_length=5, blank=True, null=True)
    imdbRating = models.CharField(max_length=5, blank=True, null=True)
    imdbVotes = models.CharField(max_length=100, blank=True, null=True)
    imdbID = models.CharField(max_length=100, blank=True, null=True)
    Type = models.CharField(max_length=10, blank=True, null=True)
    DVD = models.CharField(max_length=25, blank=True, null=True)
    BoxOffice = models.CharField(max_length=25, blank=True, null=True)
    Production = models.CharField(max_length=25, blank=True, null=True)
    Website = models.CharField(max_length=150, blank=True, null=True)
    totalSeasons = models.CharField(max_length=3, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Title

    def save(self, *args, **kwargs):
        """Saving the poster in the database (if not already present)"""
        if  str(self.Poster) == '' and str(self.Poster_url) != '':
            response = requests.get(self.Poster_url)
            poster = BytesIO()
            poster.write(response.content)
            poster.flush()
            name = self.Poster_url.split("/")[-1]
            self.Poster.save(name, files.File(poster), save=False)
        return super().save(*args, **kwargs)

class MovieRating(models.Model):
    """Model for movie rating"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    opinion = models.TextField(max_length=300, blank=True)
    rate = models.PositiveIntegerField(choices=RATE)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

class Likes(models.Model):
    """Model for likes"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    rating = models.ForeignKey(MovieRating, on_delete=models.CASCADE, related_name='rating_like')
    like_type = models.PositiveSmallIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)