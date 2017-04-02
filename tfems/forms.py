from django import forms
from tfems.models import Employee
class EmployeeForm(forms.ModelForm):
    # emp_name = forms.CharField(max_length=100,label='',help_text='')
    # emp_phone = forms.CharField(max_length=13,label='',help_text='')
    # emp_email = forms.CharField(max_length=100,label='',help_text='')
    # emp_designation = forms.CharField(max_length=100,label='',help_text='')
    # emp_joining_date = forms.DateField(label='',help_text='')
    # emp_working_hours = forms.IntegerField(label='',help_text='')
    # emp_address = forms.CharField(max_length=100,label='',help_text='')
    class Meta:
        model=Employee
        fields=['emp_name','emp_phone','emp_email','emp_designation','emp_joining_date',\
                'emp_working_hours','emp_address']
        widgets={
            'emp_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Employee Name'}),
            'emp_phone': forms.TextInput(attrs={'class': 'form-control','placeholder':'Phone Number'}),
            'emp_email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}),
            'emp_designation': forms.TextInput(attrs={'class': 'form-control','placeholder':'Designation'}),

            'emp_joining_date': forms.DateInput(attrs={'class':'datepicker form-control'}),
            'emp_working_hours': forms.NumberInput(attrs={'class': 'form-control','placeholder':'Working Hours'}),
            'emp_address': forms.Textarea(attrs={'class': 'form-control','placeholder':'Address','rows':3}),

        }


