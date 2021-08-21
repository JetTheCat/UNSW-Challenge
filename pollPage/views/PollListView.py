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

class PollListView(ListView):
    model = None 
    
    # How django looks up template for class based views
    # <app> / <model>_<viewtype>.html
    # In this case the django by default would search for
    # post_list.html where <model> = post and <viewtype> = list
    # template_name allows us to override the default search and
    # specify a specific template to use for a class based view
    template_name = 'pollPage/base.html'
    #context_object_name = 'polls'


    '''
    # Override default query function to filter query set based on user age/priviledge
    # Admin users will have privilege to view all types of books regardless of their age
    # We also order our query set, - (minus sign) means newest to oldest
    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.userinfo.isAdmin == 0:
                if self.request.user.userinfo.age >= 18:
                    return Post.objects.filter(isRestricted=1).order_by('-datePosted')
                else:
                    return Post.objects.filter(isRestricted=0).order_by('-datePosted')
            else:
                return Post.objects.all().order_by('-datePosted')
        else:
            return None
   '''

def home(request):
    return render(request, 'base.html')