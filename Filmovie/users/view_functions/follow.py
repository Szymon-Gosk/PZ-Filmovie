from django.contrib.auth.models import User
from notifications.models import Notification

def follow_profile(request, username):
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