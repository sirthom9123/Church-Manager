from django import forms
from django.contrib.auth.models import User
from django.forms import widgets

from .models import *


# Schedule Meeting Form
class MeetingForm(forms.ModelForm):
    class Meta:
        model = ScheduleMeeting
        fields = ('agenda', 'estimated_period', 'description', 'start_time', 'end_time')

        widgets = {
            'start_time': forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),           
        }

    def __init__(self, *args, **kwargs):
        super(MeetingForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)


# Minutes
class MinutesForm(forms.ModelForm):
    class Meta:
        model = Minutes
        fields = ('duration', 'contents', 'recording')

        widgets = {
            'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'How long was the meeting in minutes'}),
            'recording': forms.FileInput(attrs={'class': 'form-control'}),
        }
