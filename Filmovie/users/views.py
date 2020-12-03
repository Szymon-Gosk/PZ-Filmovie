"""
Defining all the views in users App
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from users.forms import SignupForm, ChangePasswordForm, EditProfileForm
from movies.models import Movie, MovieRating, Likes
from comments.models import Comment
from comments.forms import CommentForm


def signup_view(request):
    """Returning the registration view"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
                )
            return redirect('login')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }

    return render(request, 'registration/register.html', context)


@login_required
def password_change_view(request):
    """Returning the change password view if user is authenticated"""
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            return redirect('change-password-done')
    else:
        form = ChangePasswordForm(instance=user)

    context = {
        'form': form,
    }

    return render(request, 'registration/change_password.html', context)


def password_change_done_view(request):
    """Returning the password change done view"""
    return render(request, 'registration/change_password_done.html')



@login_required
def edit_profile_view(request):
    """Returning the edit profile view if user is authenticated"""
    user = request.user.id
    profile = Profile.objects.get(user__id=user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile.picture = form.cleaned_data.get('picture')
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.location = form.cleaned_data.get('location')
            profile.bio = form.cleaned_data.get('bio')
            profile.save()
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user.profile)

    context = {
        'form': form,
    }

    return render(request, 'registration/edit_profile.html', context)


def user_profile_view(request, username):
    """Returning the user profile view"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    context = {
        'profile': profile,
    }

    template = loader.get_template('profiles/profile.html')

    return HttpResponse(template.render(context, request))

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
            return HttpResponseRedirect(reverse('user-rating', args=[username, imdb_id]))
    else:
        form = CommentForm()


    context = {
        'rating': rating,
        'movie': movie,
        'comments': comments,
        'form': form,
    }

    template = loader.get_template('movies/movie_rating.html')

    return HttpResponse(template.render(context, request))


def like_view(request, username, imdb_id):
    user_like = request.user
    user_rating = get_object_or_404(User, username=username)
    movie = Movie.objects.get(imdbID=imdb_id)
    rating = MovieRating.objects.get(user=user_rating, movie=movie)
    current_likes = rating.likes

    liked = Likes.objects.filter(user = user_like, rating=rating, like_type=2).count()

    if not liked:
        Likes.objects.create(user=user_like, rating=rating, like_type=2)
        current_likes = current_likes + 1
    else:
        Likes.objects.filter(user=user_like, rating=rating, like_type=2).delete()
        current_likes = current_likes - 1

    rating.likes = current_likes
    rating.save()

    return HttpResponseRedirect(reverse('user-rating', args=[username, imdb_id]))


def dislike_view(request, username, imdb_id):
    user_dislike = request.user
    user_rating = get_object_or_404(User, username=username)
    movie = Movie.objects.get(imdbID=imdb_id)
    rating = MovieRating.objects.get(user=user_rating, movie=movie)
    current_dislikes = rating.dislikes

    disliked = Likes.objects.filter(user = user_dislike, rating=rating, like_type=1).count()

    if not disliked:
        Likes.objects.create(user=user_dislike, rating=rating, like_type=1)
        current_dislikes = current_dislikes + 1
    else:
        Likes.objects.filter(user=user_dislike, rating=rating, like_type=1).delete()
        current_dislikes = current_dislikes - 1

    rating.dislikes = current_dislikes
    rating.save()

    return HttpResponseRedirect(reverse('user-rating', args=[username, imdb_id]))



