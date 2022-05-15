from django import forms

from .models import Contact, Financial

class FinancialForm(forms.ModelForm):
    class Meta:
        model = Financial
        fields = ('project', 'profile', 'amount', 'contact', 'upload_date', 'reason')
        
        widgets = {
            'upload_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),           
        }
        
    def __init__(self, *args, **kwargs):
        super(FinancialForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['upload_date'].input_formats = ('%Y-%m-%d',)
        
        
        
class MemberForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('id',)