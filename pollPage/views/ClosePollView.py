from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import (
    ListView, 
    CreateView,
    UpdateView,
    DeleteView
)

# Model imports
from pollPage.models import Polls, PollOptions, PollUsers

@login_required
def closePoll(request, poll_id):
    poll = Polls.objects.get(id=poll_id)

    if request.user.id != poll.user.id:
        messages.error(request, 'Cannot close poll as you are not the owner!')
        return redirect('poll-home')
    
    poll.active = False 
    poll.save()
    messages.success(request, 'Poll "{}" closed.'.format(poll.title))
    return redirect('poll-home')