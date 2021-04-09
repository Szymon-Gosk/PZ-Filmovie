"""Admin configuration for comments app"""
from django.contrib import admin
from .models import Comment


admin.site.register(Comment)