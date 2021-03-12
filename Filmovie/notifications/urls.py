"""Url patterns for notifications app"""
from django.urls import path
from notifications.views import delete_notification_and_redirect_view


urlpatterns = [
    path('<notification_id>/<username>/<imdb_id>', delete_notification_and_redirect_view, name='notifications')
]