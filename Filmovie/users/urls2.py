"""Url patterns for user's profile"""
from django.urls import path
from movies.views import user_activities_view
from users.views import (
    search_users_view,
    user_profile_view,
    follow_profile_view,
    user_profile_followers_view,
    user_profile_following_view,
    user_profile_movies_view,
    user_profile_series_view,
    user_profile_watchlist_view,
    user_profile_watchedlist_view,
    user_profile_reviewed_view
)

urlpatterns = [
    path('search', search_users_view, name='search-users'),
    path('activities', user_activities_view, name='user-activities'),
    path('<username>/', user_profile_view, name='profile'),
    path('<username>/follow', follow_profile_view, name='follow'),
    path('<username>/followers', user_profile_followers_view, name='followers'),
    path('<username>/following', user_profile_following_view, name='following'),
    path('<username>/star-movies', user_profile_movies_view, name='user-star-movies'),
    path('<username>/star-series', user_profile_series_view, name='user-star-series'),
    path('<username>/watchlist', user_profile_watchlist_view, name='user-watchlist'),
    path('<username>/watchedlist', user_profile_watchedlist_view, name='user-watchedlist'),
    path('<username>/reviewed', user_profile_reviewed_view, name='user-reviews'),
]
