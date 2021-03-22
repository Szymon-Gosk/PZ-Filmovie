from django.shortcuts import get_object_or_404
from movies.models import Movie, MovieRating, Likes
from django.contrib.auth.models import User
from notifications.models import Notification

def like(request, username, imdb_id):
    user_like = request.user
    user_rating = get_object_or_404(User, username=username)
    movie = Movie.objects.get(imdbID=imdb_id)
    rating = MovieRating.objects.get(user=user_rating, movie=movie)
    current_likes = rating.likes
    current_dislikes = rating.dislikes

    liked = Likes.objects.filter(user=user_like, rating=rating, like_type=2).count()
    disliked = Likes.objects.filter(user=user_like, rating=rating, like_type=1).count()

    if not liked:
        if disliked:
            Likes.objects.create(user=user_like, rating=rating, like_type=2)
            current_likes = current_likes + 1
            Likes.objects.filter(user=user_like, rating=rating, like_type=1).delete()
            current_dislikes = current_dislikes - 1
        else:
            Likes.objects.create(user=user_like, rating=rating, like_type=2)
            current_likes = current_likes + 1
            
        if not user_like == user_rating:
            text = "{0} has liked your {1} review".format(user_like.username, rating.movie.Title)
            if Notification.objects.filter(executor=user_like, receiver=user_rating, text=text).count() == 1:
                Notification.objects.get(executor=user_like, receiver=user_rating, text=text).delete()
            Notification.objects.create(
                executor=user_like,
                receiver=user_rating,
                text=text,
                url_name='user-rating',
                imdb_id=imdb_id
                )
    else:
        Likes.objects.filter(user=user_like, rating=rating, like_type=2).delete()
        current_likes = current_likes - 1

    rating.likes = current_likes
    rating.dislikes = current_dislikes
    rating.save()
    
def dislike(request, username, imdb_id):
    user_dislike = request.user
    user_rating = get_object_or_404(User, username=username)
    movie = Movie.objects.get(imdbID=imdb_id)
    rating = MovieRating.objects.get(user=user_rating, movie=movie)
    current_likes = rating.likes
    current_dislikes = rating.dislikes

    liked = Likes.objects.filter(user=user_dislike, rating=rating, like_type=2).count()
    disliked = Likes.objects.filter(user=user_dislike, rating=rating, like_type=1).count()

    if not disliked:
        if liked:
            Likes.objects.filter(user=user_dislike, rating=rating, like_type=2).delete()
            current_likes = current_likes - 1
            Likes.objects.create(user=user_dislike, rating=rating, like_type=1)
            current_dislikes = current_dislikes + 1
        else:
            Likes.objects.create(user=user_dislike, rating=rating, like_type=1)
            current_dislikes = current_dislikes + 1
        
        if not user_dislike == user_rating:
            text = "{0} has disliked your {1} review".format(user_dislike.username, rating.movie.Title)
            if Notification.objects.filter(executor=user_dislike, receiver=user_rating, text=text).count() == 1:
                Notification.objects.get(executor=user_dislike, receiver=user_rating, text=text).delete()
            Notification.objects.create(
                executor=user_dislike,
                receiver=user_rating,
                text=text,
                url_name='user-rating',
                imdb_id=imdb_id
                )
            
    else:
        Likes.objects.filter(user=user_dislike, rating=rating, like_type=1).delete()
        current_dislikes = current_dislikes - 1

    rating.likes = current_likes
    rating.dislikes = current_dislikes
    rating.save()