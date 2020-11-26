#
# Copyright 2020 Szuczki Marnotrawne. All rights reserved.
#
# Owner: Suczki Marnotrawne
#

"""
Filmovie URL Configuration
"""

from django.urls import path
from movies.views import (
    home,
    pagination,
    movie_detail_view,
    genres_view,
    star_movie_view,
    add_to_watchlist_view,
    add_to_watchedlist_view,
    movie_rate_view,
)


urlpatterns = [
    path('', home, name='home'),
    path('search/<query>/page/<page_number>', pagination, name='pagination'),
    path('<imdb_id>', movie_detail_view, name='movie-details'),
    path('<imdb_id>/star', star_movie_view, name='star'),
    path('<imdb_id>/watchlist', add_to_watchlist_view, name='watchlist'),
    path('<imdb_id>/watchedlist', add_to_watchedlist_view, name='watchedlist'),
    path('genre/<slug:genre_slug>/', genres_view, name='genres'),
    path('<imdb_id>/rate', movie_rate_view, name='rate-movie'),
]
