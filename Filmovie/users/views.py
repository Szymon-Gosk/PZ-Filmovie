from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from users.forms import SignupForm, ChangePasswordForm, EditProfileForm


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            return redirect('login')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }

    return render(request, 'registration/register.html', context)


@login_required
def password_change_view(request):
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
    return render(request, 'registration/change_password_done.html')



@login_required
def edit_profile_view(request):
    user = request.user.id
    profile = Profile.objects.get(user__id=user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile.picture = form.cleaned_data.get('picture')
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.location = form.cleaned_data.get('location')
            profile.bio = form.cleaned_data.get('bio')
            profile.save()
            return redirect('home')
    else:
        form = EditProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'registration/edit_profile.html', context)
