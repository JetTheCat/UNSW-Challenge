from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Model imports
from user.models import Account

class UpdateAccountForm(forms.ModelForm):
    class Meta:
        model = Account 
        fields = ['image', 'role']