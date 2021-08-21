from django.db import models

# Model imports
from django.contrib.auth.models import User
from .Polls import Polls

class PollOptions(models.Model):
    id = models.AutoField(primary_key=True)
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE)
    time_str = models.CharField(max_length=10, default=None)
    vote_count = models.IntegerField(default=0)

