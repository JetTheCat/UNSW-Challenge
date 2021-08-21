from django.db import models

# Model imports
from django.contrib.auth.models import User

class Polls(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    timestamp_created = models.DateTimeField(verbose_name='Time Created', auto_now_add=True, null=False)
    timestamp_modified = models.DateTimeField(verbose_name='Time Modified', auto_now=True, null=False)
    title = models.CharField(max_length=100, default=None)
    content = models.TextField(verbose_name='Content')
    active = models.BooleanField(default=True)

