"""Models definitions for actors app"""
from django.db import models
from django.urls import reverse

from django.utils.text import slugify


class Actor(models.Model):
    """Model for actors"""
    name = models.CharField(max_length=80, unique=True)
    image = models.ImageField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    movies = models.ManyToManyField('movies.Movie')

    def get_absolute_url(self):
        return reverse("actors", args=[self.slug])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
