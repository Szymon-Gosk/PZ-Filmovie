"""Models definitions for movies app"""
from io import BytesIO
from django.db import models
from django.utils.text import slugify
from django.core import files
from django.urls import reverse
from actors.models import Actor
from django.contrib.auth.models import User

import requests


class Genre(models.Model):
    """Model for genre"""
    title = models.CharField(max_length=25)
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
    """Model for rating"""
    source = models.CharField(max_length=50)
    rating = models.CharField(max_length=10)

    def __str__(self):
        """Returning the name of the source instead of whole object"""
        return self.source


class Movie(models.Model):
    """Model for movie"""
    Title = models.CharField(max_length=150)
    Year = models.CharField(max_length=25, blank=True)
    Rated = models.CharField(max_length=10, blank=True)
    Released = models.CharField(max_length=25, blank=True)
    Runtime = models.CharField(max_length=25, blank=True)
    Genre = models.ManyToManyField(Genre, blank=True)
    Director = models.CharField(max_length=100, blank=True)
    Writer = models.CharField(max_length=300, blank=True)
    Actors = models.ManyToManyField(Actor, blank=True)
    Plot = models.CharField(max_length=900, blank=True)
    Language = models.CharField(max_length=300, blank=True)
    Country = models.CharField(max_length=150, blank=True)
    Awards = models.CharField(max_length=500, blank=True)
    Poster = models.ImageField(upload_to='movies', blank=True)
    Poster_url = models.URLField(blank=True)
    Ratings = models.ManyToManyField(Rating, blank=True)
    Metascore = models.CharField(max_length=5, blank=True)
    imdbRating = models.CharField(max_length=5, blank=True)
    imdbVotes = models.CharField(max_length=100, blank=True)
    imdbID = models.CharField(max_length=100, blank=True)
    Type = models.CharField(max_length=10, blank=True)
    DVD = models.CharField(max_length=25, blank=True)
    BoxOffice = models.CharField(max_length=25, blank=True)
    Production = models.CharField(max_length=25, blank=True)
    Website = models.CharField(max_length=150, blank=True)
    totalSeasons = models.CharField(max_length=3, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title

    def save(self, *args, **kwargs):
        """Saving the poster in the database (if not already present)"""
        if self.Poster == '' and self.Poster_url != '':
            resp = requests.get(self.Poster_url)
            poster = BytesIO()
            poster.write(resp.content)
            poster.flush()
            file_name = self.Poster_url.split("/")[-1]
            self.Poster.save(file_name, files.File(poster), save=False)

        return super().save(*args, **kwargs)


"""Rating definitions"""
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


class MovieRating(models.Model):
    """Model for movie rating"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    opinion = models.TextField(max_length=300, blank=True)
    rate = models.PositiveSmallIntegerField(choices=RATE)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Likes(models.Model):
    """Model for likes"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    like_type = models.PositiveSmallIntegerField()
    rating = models.ForeignKey(MovieRating, on_delete=models.CASCADE, related_name='rating_like')
    timestamp = models.DateTimeField(auto_now_add=True)
