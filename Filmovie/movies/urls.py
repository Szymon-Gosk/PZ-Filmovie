"""Url patterns for actors app"""
from django.urls import path
from users.views import (
    opinion_detail_view,
    like_view, 
    dislike_view,
    comment_delete_view,
)
from movies.views import (
    home,
    pagination,
    movie_detail_view,
    genres_view,
    star_movie_view,
    add_to_watchlist_view,
    add_to_watchedlist_view,
    movie_rate_view,
    type_view,
)


urlpatterns = [
    path('', home, name='home'),
    path('<movie_type>/', type_view, name='type'),
    path('genre/<slug:genre_slug>/', genres_view, name='genres'),
    path('<imdb_id>', movie_detail_view, name='movie-details'),
    path('<imdb_id>/star', star_movie_view, name='star'),
    path('<imdb_id>/watchlist', add_to_watchlist_view, name='watchlist'),
    path('<imdb_id>/watchedlist', add_to_watchedlist_view, name='watchedlist'),
    path('<imdb_id>/rate', movie_rate_view, name='rate-movie'),
    path('<username>/rating/<imdb_id>/', opinion_detail_view, name='user-rating'),
    path('<username>/rating/<imdb_id>/delete/<comment_id>', comment_delete_view, name='comment-delete'),
    path('<username>/rating/<imdb_id>/like', like_view, name='user-rating-like'),
    path('<username>/rating/<imdb_id>/dislike', dislike_view, name='user-rating-dislike'),
    path('search/<query>/page/<page_number>', pagination, name='pagination'),
]