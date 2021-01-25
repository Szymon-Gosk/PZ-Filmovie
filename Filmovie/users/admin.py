"""
Registering Profile model in admin panel
"""
from django.contrib import admin
from users.models import Profile

# Register your models here.
admin.site.register(Profile)
