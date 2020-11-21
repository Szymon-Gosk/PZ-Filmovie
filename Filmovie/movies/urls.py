#
# Copyright 2020 Szuczki Marnotrawne. All rights reserved.
#
# Owner: Suczki Marnotrawne
#

"""
Filmovie URL Configuration
"""

from django.urls import path
from movies.views import home, pagination, movie_detail_view, genres_view, star_movie_view


urlpatterns = [
    path('', home, name='home'),
    path('search/<query>/page/<page_number>', pagination, name='pagination'),
    path('<imdb_id>', movie_detail_view, name='movie-details'),
    path('<imdb_id>/star', star_movie_view, name='star'),
    path('genre/<slug:genre_slug>/', genres_view, name='genres'),
]
