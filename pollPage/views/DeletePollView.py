from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    CreateView,
    UpdateView,
    DeleteView
)

# Model imports
from pollPage.models import Polls, PollOptions, PollUsers

# View to delete a book post
class DeletePollView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Polls
    template_name = 'poll_confirm_delete.html'

    def get_success_url(self):
        return reverse('poll-home')

    
    # Only allow authenticated users 
    def test_func(self):
        if self.request.user.is_authenticated:
            return True 
        else:
            return False
    
