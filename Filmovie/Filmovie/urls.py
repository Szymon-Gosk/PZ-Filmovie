#
# Copyright 2020 Szuczki Marnotrawne. All rights reserved.
#
# Owner: Suczki Marnotrawne
#

"""
Filmovie URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import user_profile_view, opinion_detail_view, like_view, dislike_view, user_profile_movies_view, user_profile_series_view, user_profile_watchlist_view, user_profile_watchedlist_view, user_profile_reviewed_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movies.urls')),
    path('actors/', include('actors.urls')),
    path('accounts/', include('users.urls')),
    path('user/<username>/', user_profile_view, name='profile'),
    path('user/<username>/star-movies', user_profile_movies_view, name='user-star-movies'),
    path('user/<username>/star-series', user_profile_series_view, name='user-star-series'),
    path('user/<username>/watchlist', user_profile_watchlist_view, name='user-watchlist'),
    path('user/<username>/watchedlist', user_profile_watchedlist_view, name='user-watchedlist'),
    path('user/<username>/reviewed', user_profile_reviewed_view, name='user-reviews'),
    path('<username>/rating/<imdb_id>/', opinion_detail_view, name='user-rating'),
    path('<username>/rating/<imdb_id>/like', like_view, name='user-rating-like'),
    path('<username>/rating/<imdb_id>/dislike', dislike_view, name='user-rating-dislike'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
