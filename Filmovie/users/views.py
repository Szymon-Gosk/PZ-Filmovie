"""Views definitions for users app"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from users.forms import SignupForm, ChangePasswordForm, EditProfileForm
from movies.models import Movie, MovieRating, Likes
from comments.models import Comment
from comments.forms import CommentForm
from notifications.models import Notification


def signup_view(request):
    """Returns the 'registration' view"""
    if request.method == 'POST':
        sign_up_form = SignupForm(request.POST)
        if sign_up_form.is_valid():
            username = sign_up_form.cleaned_data.get('username')
            first_name = sign_up_form.cleaned_data.get('first_name')
            last_name = sign_up_form.cleaned_data.get('last_name')
            email = sign_up_form.cleaned_data.get('email')
            password = sign_up_form.cleaned_data.get('password')
            User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
            return redirect('login')
    else:
        sign_up_form = SignupForm()

    return render(request, 'auth/register.html', {'form': sign_up_form})

@login_required
def password_change_view(request):
    """Returns the 'change password' view if the user is authenticated"""
    user = request.user
    if request.method == 'POST':
        password_change_form = ChangePasswordForm(request.POST)
        if password_change_form.is_valid():
            user.set_password(password_change_form.cleaned_data.get('new_password'))
            user.save()
            update_session_auth_hash(request, user)
            return redirect('change-password-done')
    else:
        password_change_form = ChangePasswordForm(instance=user)

    return render(request, 'auth/change_password.html', {'form': password_change_form})

def password_change_done_view(request):
    """Returns the 'password change done' view"""
    return render(request, 'auth/change_password_done.html')

@login_required
def edit_profile_view(request):
    """Returning the edit profile view if user is authenticated"""
    profile = Profile.objects.get(user__id=request.user.id)

    if request.method == 'POST':
        edit_profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if edit_profile_form.is_valid():
            profile.picture = edit_profile_form.cleaned_data.get('picture')
            profile.background = edit_profile_form.cleaned_data.get('background')
            profile.first_name = edit_profile_form.cleaned_data.get('first_name')
            profile.last_name = edit_profile_form.cleaned_data.get('last_name')
            profile.bio = edit_profile_form.cleaned_data.get('bio')
            profile.save()
            return redirect('profile', username=request.user.username)
    else:
        edit_profile_form = EditProfileForm(instance=request.user.profile)

    return render(request, 'profiles/edit_profile.html', {'form': edit_profile_form})

@login_required
def user_profile_view(request, username):
    """Returns the 'user profile' view"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    movies_star_count = profile.star.filter(Type='movie').count()
    series_star_count = profile.star.filter(Type='series').count()
    watchlist_count = profile.watchlist.all().count()
    watchedlist_count = profile.watchedlist.all().count()
    opinions_count = MovieRating.objects.filter(user=user).count()

    following = []
    for p in Profile.objects.all():
        if user in p.followers.all():
            following.append(p.user)

    context = {
        'profile': profile,
        'movies_star_count': movies_star_count,
        'series_star_count': series_star_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'following': len(following),
    }

    return HttpResponse(loader.get_template('profiles/profile.html').render(context, request))

@login_required
def user_profile_followers_view(request, username):
    """Returns the 'user profile' view"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    movies_star_count = profile.star.filter(Type='movie').count()
    series_star_count = profile.star.filter(Type='series').count()
    watchlist_count = profile.watchlist.all().count()
    watchedlist_count = profile.watchedlist.all().count()
    opinions_count = MovieRating.objects.filter(user=user).count()
    following = []
    for p in Profile.objects.all():
        if user in p.followers.all():
            following.append(profile.user)

    followers = []
    for u in profile.followers.all():
        followers.append(u)
            
    context = {
        'profile': profile,
        'movies_star_count': movies_star_count,
        'series_star_count': series_star_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'movie_data': followers,
        'following': len(following),
        'list_title': 'Followers',
    }

    return HttpResponse(loader.get_template('profiles/profile.html').render(context, request))

@login_required
def user_profile_following_view(request, username):
    """Returns the 'user profile' view"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    movies_star_count = profile.star.filter(Type='movie').count()
    series_star_count = profile.star.filter(Type='series').count()
    watchlist_count = profile.watchlist.all().count()
    watchedlist_count = profile.watchedlist.all().count()
    opinions_count = MovieRating.objects.filter(user=user).count()
    following = []
    for p in Profile.objects.all():
        if user in p.followers.all():
            following.append(p.user)

    context = {
        'profile': profile,
        'movies_star_count': movies_star_count,
        'series_star_count': series_star_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'following': len(following),
        'movie_data': following,
        'list_title': 'Following',
    }

    return HttpResponse(loader.get_template('profiles/profile.html').render(context, request))

@login_required
def user_profile_movies_view(request, username):
    """Returns the 'user profile' view"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    movies_star_count = profile.star.filter(Type='movie').count()
    series_star_count = profile.star.filter(Type='series').count()
    watchlist_count = profile.watchlist.all().count()
    watchedlist_count = profile.watchedlist.all().count()
    opinions_count = MovieRating.objects.filter(user=user).count()
    following = []
    for p in Profile.objects.all():
        if user in p.followers.all():
            following.append(p.user)

    movies = profile.star.filter(Type='movie')

    data = Paginator(movies, 9).get_page(request.GET.get('page'))

    context = {
        'profile': profile,
        'movies_star_count': movies_star_count,
        'series_star_count': series_star_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'movie_data': data,
        'list_title': 'Favourite movies',
        'following': len(following),
    }

    return HttpResponse(loader.get_template('profiles/profile.html').render(context, request))

@login_required
def user_profile_series_view(request, username):
    """Returns the 'user profile' view"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    movies_star_count = profile.star.filter(Type='movie').count()
    series_star_count = profile.star.filter(Type='series').count()
    watchlist_count = profile.watchlist.all().count()
    watchedlist_count = profile.watchedlist.all().count()
    opinions_count = MovieRating.objects.filter(user=user).count()
    following = []
    for p in Profile.objects.all():
        if user in p.followers.all():
            following.append(p.user)

    series = profile.star.filter(Type='series')

    data = Paginator(series, 9).get_page(request.GET.get('page'))

    context = {
        'profile': profile,
        'movies_star_count': movies_star_count,
        'series_star_count': series_star_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'movie_data': data,
        'list_title': 'Favourite series',
        'following': len(following),
    }

    return HttpResponse(loader.get_template('profiles/profile.html').render(context, request))

@login_required
def user_profile_watchlist_view(request, username):
    """Returns the 'user profile' view"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    movies_star_count = profile.star.filter(Type='movie').count()
    series_star_count = profile.star.filter(Type='series').count()
    watchlist_count = profile.watchlist.all().count()
    watchedlist_count = profile.watchedlist.all().count()
    opinions_count = MovieRating.objects.filter(user=user).count()
    following = []
    for p in Profile.objects.all():
        if user in p.followers.all():
            following.append(p.user)

    watchlist = profile.watchlist.all()

    data = Paginator(watchlist, 9).get_page(request.GET.get('page'))

    context = {
        'profile': profile,
        'movies_star_count': movies_star_count,
        'series_star_count': series_star_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'movie_data': data,
        'list_title': 'Watchlist',
        'following': len(following),
    }

    return HttpResponse(loader.get_template('profiles/profile.html').render(context, request))

@login_required
def user_profile_watchedlist_view(request, username):
    """Returns the 'user profile' view"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    movies_star_count = profile.star.filter(Type='movie').count()
    series_star_count = profile.star.filter(Type='series').count()
    watchlist_count = profile.watchlist.all().count()
    watchedlist_count = profile.watchedlist.all().count()
    opinions_count = MovieRating.objects.filter(user=user).count()
    following = []
    for p in Profile.objects.all():
        if user in p.followers.all():
            following.append(p.user)

    watchedlist = profile.watchedlist.all()

    data = Paginator(watchedlist, 9).get_page(request.GET.get('page'))

    context = {
        'profile': profile,
        'movies_star_count': movies_star_count,
        'series_star_count': series_star_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'movie_data': data,
        'list_title': 'Watchedlist',
        'following': len(following),
    }

    return HttpResponse(loader.get_template('profiles/profile.html').render(context, request))

@login_required
def user_profile_reviewed_view(request, username):
    """Returns the 'user profile' view"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    movies_star_count = profile.star.filter(Type='movie').count()
    series_star_count = profile.star.filter(Type='series').count()
    watchlist_count = profile.watchlist.all().count()
    watchedlist_count = profile.watchedlist.all().count()
    opinions_count = MovieRating.objects.filter(user=user).count()
    following = []
    for p in Profile.objects.all():
        if user in p.followers.all():
            following.append(p.user)

    opinions = MovieRating.objects.filter(user=user)

    data = Paginator(opinions, 9).get_page(request.GET.get('page'))

    context = {
        'profile': profile,
        'movies_star_count': movies_star_count,
        'series_star_count': series_star_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'movie_data': data,
        'list_title': 'Reviewed',
        'following': len(following),
    }

    return HttpResponse(loader.get_template('profiles/profile.html').render(context, request))

@login_required
def opinion_detail_view(request, username, imdb_id):
    user_comment = request.user
    user = get_object_or_404(User, username=username)
    movie = Movie.objects.get(imdbID=imdb_id)
    rating = MovieRating.objects.get(user=user, movie=movie)

    comments = Comment.objects.filter(rating=rating).order_by('date')

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
            return HttpResponseRedirect(reverse('user-rating', args=[username, imdb_id]))
    else:
        form = CommentForm()

    context = {
        'rating': rating,
        'movie': movie,
        'comments': comments,
        'form': form,
    }

    return HttpResponse(loader.get_template('movies/movie_rating.html').render(context, request))

@login_required
def comment_delete_view(request, username, imdb_id, comment_id):
    Comment.objects.filter(id=comment_id).delete()

    return HttpResponseRedirect(reverse('user-rating', args=[username, imdb_id]))

@login_required
def like_view(request, username, imdb_id):
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

    return HttpResponseRedirect(reverse('user-rating', args=[username, imdb_id]))


@login_required
def dislike_view(request, username, imdb_id):
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

    return HttpResponseRedirect(reverse('user-rating', args=[username, imdb_id]))

@login_required
def user_settings_view(request):
    """Returning the edit profile view if user is authenticated"""
    user_id = request.user.id
    profile = Profile.objects.get(user__id=user_id)

    return render(request, 'profiles/settings.html', {'profile': profile})

@login_required
def follow_profile_view(request, username):
    me = request.user
    other_user_qs = User.objects.filter(username=username)
    other = other_user_qs.first()
    profile = other.profile
    if me in profile.followers.all():
        text = "{0} has unfollowed you".format(me.username)
        if Notification.objects.filter(executor=me, receiver=other, text=text).count() == 1:
            Notification.objects.get(executor=me, receiver=other, text=text).delete()
        Notification.objects.create(
            executor=me,
            receiver=other,
            text=text,
            url_name='profile'
            )
        profile.followers.remove(me)
    else:
        text = "{0} has followed you".format(me.username)
        if Notification.objects.filter(executor=me, receiver=other, text=text).count() == 1:
            Notification.objects.get(executor=me, receiver=other, text=text).delete()
        Notification.objects.create(
            executor=me,
            receiver=other,
            text=text,
            url_name='profile'
            )
        profile.followers.add(me)

    return HttpResponseRedirect(reverse('profile', args=[username]))

@login_required
def search_users_view(request):
    query = request.GET.get('q')

    if query:
        users = User.objects.filter(username__contains=query)

        return HttpResponse(loader.get_template('users/user_search_result.html').render({'users': users,'query': query}, request))
    
    return render(request, 'users/search_users.html')
