"""
Registering Profile model in admin panel
"""
from django.contrib import admin
from users.models import Profile

admin.site.register(Profile)
