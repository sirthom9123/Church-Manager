from django import forms

from .models import *

class ShareFileForm(forms.ModelForm):
    class Meta:
        model = Dropbox
        fields = ('title', 'category', 'desc',)


class FileFieldForm(forms.ModelForm):
    class Meta:
        model = ShareFileField
        fields = ('file_field',)
