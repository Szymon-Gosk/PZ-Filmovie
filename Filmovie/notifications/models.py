from django.db import models
from django.contrib.auth.models import User
from django.contrib.humanize.templatetags import humanize


class Notification(models.Model):
    executor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_executor')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_receiver')
    text = models.TextField(max_length=300, null=True, blank=True)
    url_name = models.TextField(max_length=50, null=True, blank=True)
    imdb_id = models.TextField(max_length=50, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.receiver.username
    
    def get_date(self):
        return humanize.naturaltime(self.date)
