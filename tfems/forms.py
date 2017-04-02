from django import forms
from tfems.models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['emp_name','emp_phone','emp_email','emp_designation','emp_joining_date','emp_working_hours','emp_address']
        widgets=[
            {'emp_name':forms.TextInput(attrs={'class':'form-control'})},
            {'emp_phone': forms.TextInput(attrs={'class': 'form-control'})},
            {'emp_email': forms.TextInput(attrs={'class': 'form-control'})},
            {'emp_designation': forms.TextInput(attrs={'class': 'form-control'})},
            {'emp_joining_date': forms.TextInput(attrs={'class': 'form-control'})},
            {'emp_working_hours': forms.TextInput(attrs={'class': 'form-control'})},
            {'emp_address': forms.TextInput(attrs={'class': 'form-control'})},

        ]


