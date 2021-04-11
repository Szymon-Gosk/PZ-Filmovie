from django.contrib.auth.models import User
from users.forms import SignupForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.sites.models import Site
from Filmovie import settings

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
            domain = Site.objects.get_current().domain
            button_href = "http://" + domain
            mail = render_to_string("mails/signup_email.html", {"button_href": button_href})
            text_content = strip_tags(mail)
            mail_object = EmailMultiAlternatives(
                "Welcome to Filmovie!",
                text_content,
                settings.EMAIL_HOST_USER,
                [email]
            )
            mail_object.attach_alternative(mail, "text/html")
            mail_object.send()
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