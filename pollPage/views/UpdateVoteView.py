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
def updateVote(request, user_id, option_id, poll_id):
    poll_user = PollUsers.objects.get(participant=user_id, poll=poll_id)
    poll_option = PollOptions.objects.get(id=option_id)

    # Add new vote for the option
    poll_option.vote_count += 1

    # Update user's vote choice for the given poll
    poll_user.voted_choice = poll_option.time_str
    poll_user.voted = True

    poll_option.save()
    poll_user.save()

    messages.success(request, 'Vote Successful!')
    return redirect('poll-home')