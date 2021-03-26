"""Views definitions for users app"""
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from comments.models import Comment
from users.view_functions import (
    signup, 
    change_password, 
    edit_profile, 
    profile, 
    followers, 
    profile_movies, 
    opinion, 
    like, 
    follow
)


def signup_view(request):
    """Returns the 'registration' view"""
    context = signup.signup(request)
    if context.get('redirect'):
        return redirect('login')

    return render(request, 'auth/register.html', context)

@login_required
def password_change_view(request):
    """Returns the 'change password' view if the user is authenticated"""
    context = change_password.change_password(request)
    if context.get('redirect'):
        return redirect('change-password-done')

    return render(request, 'auth/change_password.html', context)

def password_change_done_view(request):
    """Returns the 'password change done' view"""
    return render(request, 'auth/change_password_done.html')

@login_required
def edit_profile_view(request):
    """Returning the edit profile view if user is authenticated"""
    context = edit_profile.edit_profile(request)

    if context.get('redirect'):
        return redirect('profile', username=request.user.username)

    return render(request, 'profiles/edit_profile.html', context)

@login_required
def user_profile_view(request, username):
    """Returns the 'user profile' view"""
    context = profile.user_profile(request, username)

    return HttpResponse(loader.get_template('profiles/profile.html').render(context, request))

@login_required
def user_profile_followers_view(request, username):
    """Returns the 'user profile' view"""
    context = followers.get_followers(request, username)
    return HttpResponse(loader.get_template('profiles/profile.html').render(context, request))

@login_required
def user_profile_following_view(request, username):
    """Returns the 'user profile' view"""
    context = followers.get_following(request, username)
    return HttpResponse(loader.get_template('profiles/profile.html').render(context, request))

@login_required
def user_profile_movies_view(request, username):
    """Returns the 'user profile' view"""
    context = profile_movies.get_movies(request, username)
    return HttpResponse(loader.get_template('profiles/profile.html').render(context, request))

@login_required
def user_profile_series_view(request, username):
    """Returns the 'user profile' view"""
    context = profile_movies.get_series(request, username)
    return HttpResponse(loader.get_template('profiles/profile.html').render(context, request))

@login_required
def user_profile_watchlist_view(request, username):
    """Returns the 'user profile' view"""
    context = profile_movies.get_watchlist(request, username)
    return HttpResponse(loader.get_template('profiles/profile.html').render(context, request))

@login_required
def user_profile_watchedlist_view(request, username):
    """Returns the 'user profile' view"""
    context = profile_movies.get_watchedlist(request, username)
    return HttpResponse(loader.get_template('profiles/profile.html').render(context, request))

@login_required
def user_profile_reviewed_view(request, username):
    """Returns the 'user profile' view"""
    context = profile_movies.get_reviews(request, username)
    return HttpResponse(loader.get_template('profiles/profile.html').render(context, request))

@login_required
def opinion_detail_view(request, username, imdb_id):
    context = opinion.get_opinion(request, username, imdb_id)
    if context.get('reverse'):
        return HttpResponseRedirect(reverse('user-rating', args=[username, imdb_id]))
    return HttpResponse(loader.get_template('movies/movie_rating.html').render(context, request))

@login_required
def comment_delete_view(request, username, imdb_id, comment_id):
    Comment.objects.filter(id=comment_id).delete()
    return HttpResponseRedirect(reverse('user-rating', args=[username, imdb_id]))

@login_required
def like_view(request, username, imdb_id):
    like.like(request, username, imdb_id)
    return HttpResponseRedirect(reverse('user-rating', args=[username, imdb_id]))


@login_required
def dislike_view(request, username, imdb_id):
    like.dislike(request, username, imdb_id)
    return HttpResponseRedirect(reverse('user-rating', args=[username, imdb_id]))

@login_required
def user_settings_view(request):
    """Returning the edit profile view if user is authenticated"""
    user_id = request.user.id
    profile = Profile.objects.get(user__id=user_id)
    return render(request, 'profiles/settings.html', {'profile': profile})

@login_required
def follow_profile_view(request, username):
    follow.follow_profile(request, username)
    return HttpResponseRedirect(reverse('profile', args=[username]))

@login_required
def search_users_view(request):
    query = request.GET.get('q')
    if query:
        users = User.objects.filter(username__contains=query)
        return HttpResponse(loader.get_template('users/user_search_result.html').render({'users': users,'query': query}, request))
    return render(request, 'users/search_users.html')
