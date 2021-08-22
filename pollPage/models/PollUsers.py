from django.db import models

# Model imports
from django.contrib.auth.models import User
from .Polls import Polls

class PollUsers(models.Model):
    id = models.AutoField(primary_key=True)
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE, default=None)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    voted = models.BooleanField(default=False)
    voted_choice = models.CharField(max_length=10, default=None, null=True)