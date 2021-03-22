from users.models import Profile
from users.forms import EditProfileForm

def edit_profile(request):
    """Returning the edit profile form"""
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
            context = {
                'redirect': 'redirect'
            }
            return context
    else:
        edit_profile_form = EditProfileForm(instance=request.user.profile)
        
    context = {
        'form': edit_profile_form
        }

    return context