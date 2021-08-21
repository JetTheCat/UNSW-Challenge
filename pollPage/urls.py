from django.urls import path
from .views import (
    PollListView,
    CreatePollView
)

from pollPage.views.PollListView import home

urlpatterns = [
    path('', home, name='poll-home'),
    path('create-poll/', CreatePollView.createPoll, name='poll-create'),
]