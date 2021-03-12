from .models import Notification
from django.contrib.auth.decorators import login_required


def notifications(request):
    if request.user.is_authenticated:
        return {
            'notifications': Notification.objects.filter(receiver=request.user).order_by("-timestamp")[:5]
        }
    return {}