from pollPage.models.PollOptions import PollOptions
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.db.models import Max
from django.views.generic import (
    ListView, 
    CreateView,
    UpdateView,
    DeleteView
)

# Model imports
from pollPage.models import Polls
from pollPage.models import PollUsers
from pollPage.models import PollOptions
from django.contrib.auth.models import User

class PollListView(ListView):
    model = Polls  
    template_name = 'pollList.html'
    context_object_name = 'polls'


    # Override default query function to filter query set based on the polls that the 
    # user is invited to participate in
    def get_queryset(self):
        if self.request.user.is_authenticated:
            invited_polls = PollUsers.objects.filter(participant=self.request.user.id).values('poll')
            invited_polls = (x['poll'] for x in invited_polls)
            invited_polls = list(invited_polls)

            polls = Polls.objects.filter(id__in=invited_polls).values()

            for poll in polls:
                # Get owner/creator of the poll
                owner = User.objects.get(id=poll['user_id'])

                # Get current session user's poll data
                poll_user = PollUsers.objects.get(participant=self.request.user.id, poll=poll['id'])

                poll['owner'] = owner.username
                poll['voted'] = poll_user.voted
                poll['voted_choice'] = poll_user.voted_choice
                poll['options'] = PollOptions.objects.filter(poll=poll['id'])

            return polls
        else:
            return None

