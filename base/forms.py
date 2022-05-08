from django import forms

from .models import Contact, Expenses, Financial

class FinancialForm(forms.ModelForm):
    class Meta:
        model = Financial
        fields = ('entity', 'project', 'profile', 'amount', 'contact', 'upload_date')
        
        widgets = {
            'upload_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),           
        }
        
    def __init__(self, *args, **kwargs):
        super(FinancialForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['upload_date'].input_formats = ('%Y-%m-%d',)
        
        
class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ('entity', 'project', 'amount', 'reason', 'captured_date')
        
        widgets = {
            'captured_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),           
        }
        
    def __init__(self, *args, **kwargs):
        super(ExpensesForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['captured_date'].input_formats = ('%Y-%m-%d',)
        
        
class MemberForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('id',)