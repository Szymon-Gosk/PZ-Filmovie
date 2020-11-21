from django.db import models
from movies.models import Movie
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image
import os


def user_directory_path(instance, filename):
    profile_picture = 'user_{0}/profile.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture)

    if os.path.exists(full_path):
        os.remove(full_path)
    return profile_picture

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=20, null=True, blank=True)
    bio = models.TextField(max_length=200, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    star = models.ManyToManyField(Movie, related_name='star')
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
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)