from django.contrib.auth import update_session_auth_hash
from users.forms import ChangePasswordForm

def change_password(request):
    """Returns the change password form"""
    user = request.user
    if request.method == 'POST':
        password_change_form = ChangePasswordForm(request.POST)
        if password_change_form.is_valid():
            user.set_password(password_change_form.cleaned_data.get('new_password'))
            user.save()
            update_session_auth_hash(request, user)
            context = {
                'redirect': 'redirect'
            }
            return context
    else:
        password_change_form = ChangePasswordForm(instance=user)

    context = {
        'form': password_change_form
        }
    return context