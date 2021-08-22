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

# Form imports
from pollPage.forms import CreatePollForm

@login_required
def createPoll(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            participants = list(form.cleaned_data.get('participant'))

            time_list = (x for x in form.cleaned_data.get('time_slot'))
            time_list = list(time_list)

            # Check if owner/creator of the poll is in the list of participant model instances, 
            # if not automatically add them in
            isOwner = False
            for user in participants:
                if user.id == request.user.id:
                    isOwner = True 
                    break 
            
            if isOwner is False:
                participants.append(request.user)
                
            
            # Create new Poll
            poll = Polls(user=request.user, title=title, content=content)
            poll.save()
            
            for time in time_list:
                currPollOption = PollOptions(poll=poll, time_str=time)
                currPollOption.save()

            for user in participants:
                currPollUser = PollUsers(poll=poll, participant=user)
                currPollUser.save()

            messages.success(request, 'Poll Creation Successful!')
            return redirect('poll-home')

    else:
        form = CreatePollForm()

    context = {
        'pollform': form,
    }
    
    return render(request, 'createPoll.html', context)