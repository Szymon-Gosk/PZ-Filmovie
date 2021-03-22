from django.contrib.auth.models import User
from users.forms import SignupForm

def signup(request):
    """Returns the registration form"""
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
            context = {
                'redirect': 'redirect'
            }
            return context
    else:
        sign_up_form = SignupForm()

    context = {
        'form': sign_up_form
        }
    return context