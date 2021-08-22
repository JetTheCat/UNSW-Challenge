from django.urls import path
from .views import (
    PollListView,
    CreatePollView,
    ClosePollView,
    DeletePollView,
    UpdateVoteView,
)

urlpatterns = [
    path('', PollListView.as_view(), name='poll-home'),
    path('poll/create/', CreatePollView.createPoll, name='poll-create'),
    path('poll/close/<int:poll_id>', ClosePollView.closePoll, name='poll-close'),
    path('poll/delete/<int:pk>', DeletePollView.as_view(), name='poll-delete'),
    path('poll/update-vote/<int:user_id>/<int:option_id>/<int:poll_id>', UpdateVoteView.updateVote, name="vote-poll"),
]