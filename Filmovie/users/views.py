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
from django.core.paginator import Paginator
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


@login_required
def user_profile_view(request, username):
    """Returning the user profile view"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    mStar_count = profile.star.filter(Type='movie').count()
    sStar_count = profile.star.filter(Type='series').count()
    watchlist_count = profile.watchlist.all().count()
    watchedlist_count = profile.watchedlist.all().count()
    opinions_count = MovieRating.objects.filter(user=user).count()
    
    following = []
    for p in Profile.objects.all():
        if user in p.followers.all():
            following.append(p.user)
            
    follow = len(following)

    context = {
        'profile': profile,
        'mStar_count': mStar_count,
        'sStar_count': sStar_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'following': follow,
    }

    template = loader.get_template('profiles/profile.html')

    return HttpResponse(template.render(context, request))


@login_required
def user_profile_followers_view(request, username):
    """Returning the user profile view"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    mStar_count = profile.star.filter(Type='movie').count()
    sStar_count = profile.star.filter(Type='series').count()
    watchlist_count = profile.watchlist.all().count()
    watchedlist_count = profile.watchedlist.all().count()
    opinions_count = MovieRating.objects.filter(user=user).count()
    following = []
    for p in Profile.objects.all():
        if user in p.followers.all():
            following.append(profile.user)
            
    follow = len(following)


    followers = []
    for u in profile.followers.all():
        followers.append(u)
            

    context = {
        'profile': profile,
        'mStar_count': mStar_count,
        'sStar_count': sStar_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'movie_data': followers,
        'following': follow,
        'list_title': 'Followers',
    }

    template = loader.get_template('profiles/profile.html')

    return HttpResponse(template.render(context, request))


@login_required
def user_profile_following_view(request, username):
    """Returning the user profile view"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    mStar_count = profile.star.filter(Type='movie').count()
    sStar_count = profile.star.filter(Type='series').count()
    watchlist_count = profile.watchlist.all().count()
    watchedlist_count = profile.watchedlist.all().count()
    opinions_count = MovieRating.objects.filter(user=user).count()
    following = []
    for p in Profile.objects.all():
        if user in p.followers.all():
            following.append(p.user)
            
    follow = len(following)


    context = {
        'profile': profile,
        'mStar_count': mStar_count,
        'sStar_count': sStar_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'following': follow,
        'movie_data': following,
        'list_title': 'Following',
    }

    template = loader.get_template('profiles/profile.html')

    return HttpResponse(template.render(context, request))



@login_required
def user_profile_movies_view(request, username):
    """Returning the user profile view"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    mStar_count = profile.star.filter(Type='movie').count()
    sStar_count = profile.star.filter(Type='series').count()
    watchlist_count = profile.watchlist.all().count()
    watchedlist_count = profile.watchedlist.all().count()
    opinions_count = MovieRating.objects.filter(user=user).count()
    following = []
    for p in Profile.objects.all():
        if user in p.followers.all():
            following.append(p.user)
            
    follow = len(following)


    movies = profile.star.filter(Type='movie')

    paginator = Paginator(movies, 9)
    page_number = request.GET.get('page')
    movie_data = paginator.get_page(page_number)

    context = {
        'profile': profile,
        'mStar_count': mStar_count,
        'sStar_count': sStar_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'movie_data': movie_data,
        'list_title': 'Favourite movies',
        'following': follow,
    }

    template = loader.get_template('profiles/profile.html')

    return HttpResponse(template.render(context, request))


@login_required
def user_profile_series_view(request, username):
    """Returning the user profile view"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    mStar_count = profile.star.filter(Type='movie').count()
    sStar_count = profile.star.filter(Type='series').count()
    watchlist_count = profile.watchlist.all().count()
    watchedlist_count = profile.watchedlist.all().count()
    opinions_count = MovieRating.objects.filter(user=user).count()
    following = []
    for p in Profile.objects.all():
        if user in p.followers.all():
            following.append(p.user)
            
    follow = len(following)


    series = profile.star.filter(Type='series')

    paginator = Paginator(series, 9)
    page_number = request.GET.get('page')
    movie_data = paginator.get_page(page_number)

    context = {
        'profile': profile,
        'mStar_count': mStar_count,
        'sStar_count': sStar_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'movie_data': movie_data,
        'list_title': 'Favourite series',
        'following': follow,
    }

    template = loader.get_template('profiles/profile.html')

    return HttpResponse(template.render(context, request))


@login_required
def user_profile_watchlist_view(request, username):
    """Returning the user profile view"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    mStar_count = profile.star.filter(Type='movie').count()
    sStar_count = profile.star.filter(Type='series').count()
    watchlist_count = profile.watchlist.all().count()
    watchedlist_count = profile.watchedlist.all().count()
    opinions_count = MovieRating.objects.filter(user=user).count()
    following = []
    for p in Profile.objects.all():
        if user in p.followers.all():
            following.append(p.user)
            
    follow = len(following)


    watchlist = profile.watchlist.all()

    paginator = Paginator(watchlist, 9)
    page_number = request.GET.get('page')
    movie_data = paginator.get_page(page_number)

    context = {
        'profile': profile,
        'mStar_count': mStar_count,
        'sStar_count': sStar_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'movie_data': movie_data,
        'list_title': 'Watchlist',
        'following': follow,
    }

    template = loader.get_template('profiles/profile.html')

    return HttpResponse(template.render(context, request))

@login_required
def user_profile_watchedlist_view(request, username):
    """Returning the user profile view"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    mStar_count = profile.star.filter(Type='movie').count()
    sStar_count = profile.star.filter(Type='series').count()
    watchlist_count = profile.watchlist.all().count()
    watchedlist_count = profile.watchedlist.all().count()
    opinions_count = MovieRating.objects.filter(user=user).count()
    following = []
    for p in Profile.objects.all():
        if user in p.followers.all():
            following.append(p.user)
            
    follow = len(following)


    watchedlist = profile.watchedlist.all()

    paginator = Paginator(watchedlist, 9)
    page_number = request.GET.get('page')
    movie_data = paginator.get_page(page_number)

    context = {
        'profile': profile,
        'mStar_count': mStar_count,
        'sStar_count': sStar_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'movie_data': movie_data,
        'list_title': 'Watchedlist',
        'following': follow,
    }

    template = loader.get_template('profiles/profile.html')

    return HttpResponse(template.render(context, request))

@login_required
def user_profile_reviewed_view(request, username):
    """Returning the user profile view"""
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    mStar_count = profile.star.filter(Type='movie').count()
    sStar_count = profile.star.filter(Type='series').count()
    watchlist_count = profile.watchlist.all().count()
    watchedlist_count = profile.watchedlist.all().count()
    opinions_count = MovieRating.objects.filter(user=user).count()
    following = []
    for p in Profile.objects.all():
        if user in p.followers.all():
            following.append(p.user)
            
    follow = len(following)


    opinions = MovieRating.objects.filter(user=user)

    paginator = Paginator(opinions, 9)
    page_number = request.GET.get('page')
    movie_data = paginator.get_page(page_number)

    context = {
        'profile': profile,
        'mStar_count': mStar_count,
        'sStar_count': sStar_count,
        'watchlist_count': watchlist_count,
        'watchedlist_count': watchedlist_count,
        'opinions_count': opinions_count,
        'movie_data': movie_data,
        'list_title': 'Reviewed',
        'following': follow,
    }

    template = loader.get_template('profiles/profile.html')

    return HttpResponse(template.render(context, request))


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

    liked = Likes.objects.filter(user = user_like, rating=rating, like_type=2).count()
    disliked = Likes.objects.filter(user = user_like, rating=rating, like_type=1).count()

    if not liked:
        if disliked:
            Likes.objects.create(user=user_like, rating=rating, like_type=2)
            current_likes = current_likes + 1
            Likes.objects.filter(user=user_like, rating=rating, like_type=1).delete()
            current_dislikes = current_dislikes - 1
        else:
            Likes.objects.create(user=user_like, rating=rating, like_type=2)
            current_likes = current_likes + 1
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

    liked = Likes.objects.filter(user = user_dislike, rating=rating, like_type=2).count()
    disliked = Likes.objects.filter(user = user_dislike, rating=rating, like_type=1).count()

    if not disliked:
        if liked:
            Likes.objects.filter(user=user_dislike, rating=rating, like_type=2).delete()
            current_likes = current_likes - 1
            Likes.objects.create(user=user_dislike, rating=rating, like_type=1)
            current_dislikes = current_dislikes + 1
        else:
            Likes.objects.create(user=user_dislike, rating=rating, like_type=1)
            current_dislikes = current_dislikes + 1
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
    user = request.user.id
    profile = Profile.objects.get(user__id=user)

    context = {
        'profile': profile,
    }

    return render(request, 'profiles/settings.html', context)


@login_required
def follow_profile_view(request, username):
    me = request.user
    other_user_qs = User.objects.filter(username=username)
    other = other_user_qs.first()
    profile = other.profile
    if me in profile.followers.all():
        profile.followers.remove(me)
    else:
        profile.followers.add(me)
        
    return HttpResponseRedirect(reverse('profile', args=[username]))


@login_required
def search_users_view(request):
    query = request.GET.get('q')

    if query:
        users = User.objects.filter(username__contains=query)

        context = {
            'users': users,
        }

        template = loader.get_template('users/user_search_result.html')

        return HttpResponse(template.render(context, request))
    
    return render(request, 'users/search_users.html')