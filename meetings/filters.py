from django.forms import widgets
import django_filters
from django import forms

from .models import ScheduleMeeting


class GeneralFilter(django_filters.FilterSet):
    agenda = django_filters.CharFilter(lookup_expr='icontains', 
                                        widget=forms.TextInput(
                                        attrs={'class': 'form-control', 'placeholder': 'Search by agenda...'}), 
                                        label='')