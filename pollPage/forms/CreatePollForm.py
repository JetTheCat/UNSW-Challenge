from django import forms
from django.contrib.auth.models import User
from django.forms import widgets

# Model imports
from pollPage.models import Polls

class CreatePollForm(forms.ModelForm):
    TIME_CHOICES =(
        ("9:00 a.m.", "9:00 a.m."),
        ("10:00 a.m.", "10:00 a.m."),
        ("11:00 a.m.", "11:00 a.m."),
        ("12:00 p.m.", "12:00 p.m."),
        ("1:00 p.m.", "1:00 p.m."),
        ("2:00 p.m.", "2:00 p.m."),
        ("3:00 p.m.", "3:00 p.m."),
        ("4:00 p.m.", "4:00 p.m."),
        ("5:00 p.m.", "5:00 p.m."),
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

