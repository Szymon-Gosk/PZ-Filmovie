"""Models definitions for users app"""
import os
from django.db import models
from movies.models import Movie
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.conf import settings
from PIL import Image


def user_directory_path(instance, filename):
    """Specifieing the path for profile picture and returning it"""
    profile_pictures = 'users/userid_{0}/profile_image/profile_image.jpg'.format(instance.user.id)
    path = os.path.join(settings.MEDIA_ROOT, profile_pictures)

    if os.path.exists(path):
        os.remove(path)
    return profile_pictures

def user_directory_path_background(instance, filename):
    """Specifieing the path for profile picture and returning it"""
    background_pictures = 'users/userid_{0}/background_image/background_image.jpg'.format(instance.user.id)
    path = os.path.join(settings.MEDIA_ROOT, background_pictures)

    if os.path.exists(path):
        os.remove(path)
    return background_pictures


class Profile(models.Model):
    """Model for profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=25, null=True, blank=True)
    last_name = models.CharField(max_length=25, null=True, blank=True)
    bio = models.TextField(max_length=200, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    star = models.ManyToManyField(Movie, related_name='star')
    watchlist = models.ManyToManyField(Movie, related_name='watchlist')
    watchedlist = models.ManyToManyField(Movie, related_name='watchedlist')
    picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    background = models.ImageField(upload_to=user_directory_path_background, blank=True, null=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        PICTURE_SIZE = 400, 400
        BACKGROUND_SIZE = 1600, 1000

        if self.picture:
            pic = Image.open(self.picture.path)
            if pic.mode in ("RGBA", "P"):
                pic = pic.convert("RGB")
            pic.thumbnail(PICTURE_SIZE, Image.LANCZOS)
            pic.save(self.picture.path)
        if self.background:
            background = Image.open(self.background.path)
            if background.mode in ("RGBA", "P"):
                background = background.convert("RGB")
            background.thumbnail(BACKGROUND_SIZE, Image.LANCZOS)
            background.save(self.background.path)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """Creating profile for new user"""
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        """Saving new profile"""
        instance.profile.save()