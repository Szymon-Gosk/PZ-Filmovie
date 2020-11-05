#
# Copyright 2020 Szuczki Marnotrawne. All rights reserved.
#
# Owner: Suczki Marnotrawne
#

"""
Filmovie URL Configuration
"""

from django.urls import path
from movies.views import home, pagination, movieDetail


urlpatterns = [
    path('', home, name='home'),
    path('search/<query>/page/<page_number>', pagination, name='pagination'),
    path('<imdb_id>', movieDetail, name='movie-details'),
]