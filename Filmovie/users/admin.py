"""Admin configuration for users app"""
from django.contrib import admin
from users.models import Profile, FollowerRelation

admin.site.register(Profile)
admin.site.register(FollowerRelation)
