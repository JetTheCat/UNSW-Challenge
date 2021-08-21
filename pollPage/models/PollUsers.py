from django.db import models

# Model imports
from django.contrib.auth.models import User
from .PollOptions import PollOptions

class PollUsers(models.Model):
    id = models.AutoField(primary_key=True)
    pollOption = models.ForeignKey(PollOptions, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    voted = models.BooleanField(default=False)