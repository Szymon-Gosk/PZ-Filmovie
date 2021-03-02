"""
Filmovie URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from movies.views import user_activities_view, redirect_to_home
from users.views import (
    user_profile_view,
    opinion_detail_view,
    like_view, dislike_view,
    user_profile_movies_view,
    user_profile_series_view,
    user_profile_watchlist_view,
    user_profile_watchedlist_view,
    user_profile_reviewed_view,
    follow_profile_view,
    search_users_view,
    user_profile_followers_view,
    user_profile_following_view,
    comment_delete_view,
)

urlpatterns = [
                  path('', redirect_to_home, name='home-page'),
                  path('admin/', admin.site.urls),
                  path('movie/', include('movies.urls')),
                  path('actors/', include('actors.urls')),
                  path('accounts/', include('users.urls')),
                  path('user/search', search_users_view, name='search-users'),
                  path('user/activities', user_activities_view, name='user-activities'),
                  path('user/<username>/', user_profile_view, name='profile'),
                  path('user/<username>/follow', follow_profile_view, name='follow'),
                  path('user/<username>/followers', user_profile_followers_view, name='followers'),
                  path('user/<username>/following', user_profile_following_view, name='following'),
                  path('user/<username>/star-movies', user_profile_movies_view, name='user-star-movies'),
                  path('user/<username>/star-series', user_profile_series_view, name='user-star-series'),
                  path('user/<username>/watchlist', user_profile_watchlist_view, name='user-watchlist'),
                  path('user/<username>/watchedlist', user_profile_watchedlist_view, name='user-watchedlist'),
                  path('user/<username>/reviewed', user_profile_reviewed_view, name='user-reviews'),
                  path('<username>/rating/<imdb_id>/', opinion_detail_view, name='user-rating'),
                  path('<username>/rating/<imdb_id>/delete/<comment_id>', comment_delete_view, name='comment-delete'),
                  path('<username>/rating/<imdb_id>/like', like_view, name='user-rating-like'),
                  path('<username>/rating/<imdb_id>/dislike', dislike_view, name='user-rating-dislike'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
