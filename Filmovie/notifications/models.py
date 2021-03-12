from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    executor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_executor')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_receiver')
    text = models.TextField(max_length=300, null=True, blank=True)
    seen = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.receiver.username
