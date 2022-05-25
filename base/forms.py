from django import forms

from .models import Contact, Financial, Project

class FinancialForm(forms.ModelForm):
    class Meta:
        model = Financial
        fields = ('project', 'category', 'profile', 'amount', 'contact', 'upload_date', 'reason')
        
        widgets = {
            'upload_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),           
        }
        
    def __init__(self, *args, **kwargs):
        super(FinancialForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['upload_date'].input_formats = ('%Y-%m-%d',)
        
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'start_date', 'end_date')
        
        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),           
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),           
        }
        
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['start_date'].input_formats = ('%Y-%m-%d',)
        self.fields['end_date'].input_formats = ('%Y-%m-%d',)
        
class MemberForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('id', 'belong_to')