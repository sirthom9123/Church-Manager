from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from .models import Newsletter

class NewsletterForm(forms.ModelForm):
    contents = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    class Meta:
        model = Newsletter
        fields = ('subject', 'contents')
