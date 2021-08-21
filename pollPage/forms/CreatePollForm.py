from django import forms
from django.contrib.auth.models import User
from django.forms import widgets

# Model imports
from pollPage.models import Polls

class CreatePollForm(forms.ModelForm):
    TIME_CHOICES =(
        ("9", "09:00"),
        ("10", "10:00"),
        ("11", "11:00"),
        ("12", "12:00"),
        ("13", "13:00"),
        ("14", "14:00"),
        ("15", "15:00"),
        ("16", "16:00"),
        ("17", "17:00"),
    )
    time_slot = forms.MultipleChoiceField(label="Select Time Slots", choices=TIME_CHOICES, widget=forms.CheckboxSelectMultiple) 
    participant = forms.ModelMultipleChoiceField(label="Invite Participants", queryset=User.objects.all(), 
                                                    to_field_name='username', 
                                                    help_text="Use Ctrl + Left Click to select multiple participants.",
                                                    widget=forms.SelectMultiple(attrs={'size': '10'}) 
                                                )


    class Meta:
        model = Polls 
        fields = ['title', 'content']

