from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from movies.models import Movie, MovieRating
from comments.models import Comment
from comments.forms import CommentForm
from notifications.models import Notification

def get_opinion(request, username, imdb_id):
    user_comment = request.user
    user = get_object_or_404(User, username=username)
    movie = Movie.objects.get(imdbID=imdb_id)
    rating = MovieRating.objects.get(user=user, movie=movie)

    comments = Comment.objects.filter(rating=rating).order_by('-timestamp')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.rating = rating
            comment.user = user_comment
            comment.save()
            if not user_comment == user:
                text = "{0} has commented your {1} review".format(user_comment.username, rating.movie.Title)
                Notification.objects.create(
                    executor=user_comment,
                    receiver=user,
                    text=text,
                    url_name='user-rating',
                    imdb_id=imdb_id
                    )
            context = {
                'reverse': 'reverse'
            }
            return context
    else:
        form = CommentForm()

    context = {
        'rating': rating,
        'movie': movie,
        'comments': comments,
        'form': form,
    }

    return context