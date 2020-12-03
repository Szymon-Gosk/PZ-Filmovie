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
from users.views import user_profile_view, opinion_detail_view, like_view, dislike_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('movies.urls')),
    path('actors/', include('actors.urls')),
    path('accounts/', include('users.urls')),
    path('user/<username>/', user_profile_view, name='profile'),
    path('<username>/rating/<imdb_id>/', opinion_detail_view, name='user-rating'),
    path('<username>/rating/<imdb_id>/like', like_view, name='user-rating-like'),
    path('<username>/rating/<imdb_id>/dislike', dislike_view, name='user-rating-dislike'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
