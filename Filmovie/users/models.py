"""
Defining the models in users App
"""
import os
from django.db import models
from movies.models import Movie
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image



def user_directory_path(instance, filename):
    """Specifieing the path for profile picture and returning it"""
    profile_picture = 'user_{0}/profile.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture)

    if os.path.exists(full_path):
        os.remove(full_path)
    return profile_picture

class Profile(models.Model):
    """Defining the Profile model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=20, null=True, blank=True)
    bio = models.TextField(max_length=200, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    star = models.ManyToManyField(Movie, related_name='star')
    watchlist = models.ManyToManyField(Movie, related_name='watchlist')
    watchedlist = models.ManyToManyField(Movie, related_name='watchedlist')
    picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 250, 250

        if self.picture:
            pic = Image.open(self.picture.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(self.picture.path)

    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    """Signal for creating a profile picture"""
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    """Signal for saving user profile"""
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
