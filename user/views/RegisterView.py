# Model import
from user.models import Account
from django.contrib.auth.models import User as AuthUser

# Form import
from user.forms import AccountRegistrationForm, UserRegistrationForm

from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        account_form = AccountRegistrationForm(request.POST)

        if user_form.is_valid() and account_form.is_valid():
            # Commit and save user instance in our database
            user_form.save()
            username = user_form.cleaned_data.get('username')

            # Grab role selected for the account
            role = account_form.cleaned_data.get('role')

            # Get user object instance to store as Fkey reference in the Account instance
            user_instance = AuthUser.objects.get(username=username)

            # Create Account object
            acc_obj = Account(user=user_instance, role=role)
            acc_obj.save()

            messages.success(request, 'Your account has been created! You are now able to log in!')
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        account_form = AccountRegistrationForm()
    return render(request, 'register.html', {'userform': user_form, 'accountform': account_form})