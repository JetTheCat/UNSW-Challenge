from django.urls import path
from .views import (
    PollListView
)

from pollPage.views.PollListView import home

urlpatterns = [
    path('', home, name='poll-home'),
]