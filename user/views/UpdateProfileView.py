# Model import
from user.models import Account
from django.contrib.auth.models import User as AuthUser

# Form import
from user.forms import UpdateAccountForm, UpdateUserForm

from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def updateProfile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        acc_form = UpdateAccountForm(request.POST, request.FILES, instance=request.user.account)

        if user_form.is_valid() and acc_form.is_valid():
            user_form.save()
            acc_form.save()
            messages.success(request, 'User Profile has been Updated!')
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        acc_form = UpdateAccountForm()

    context = {
        'userform': user_form,
        'accountform': acc_form,
    }
    
    return render(request, 'profile.html', context)