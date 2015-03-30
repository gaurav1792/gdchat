from django.db import models
from django.contrib.auth.models import User
import datetime
import hashlib


class Message(models.Model):
    to_user = models.CharField(max_length=30)
    from_user = models.CharField(max_length=30)
    msg = models.TextField()
    msg_type = models.CharField(max_length=10,default='text')
    msg_date = models.DateTimeField(auto_now_add=True, blank=True)


class Login_status(models.Model):
    user = models.CharField(max_length=30)
    is_online=models.BooleanField(default=0)
    last_seen = models.DateTimeField(auto_now_add=True, blank=True)


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

# Create your models here.
