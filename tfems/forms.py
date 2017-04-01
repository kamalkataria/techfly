from django.forms import forms
class EmployeeForm(forms.Form):
    emp_name=forms.CharField(max_length=100)
    emp_address=forms.CharField(max_length=100)
    emp_phone=forms.CharField(max_length=13)
    emp_email=forms.CharField(max_length=100)
    emp_designation=forms.CharField(max_length=100)
    emp_joining_date=forms.DateField()
    emp_working_hours=forms.IntegerField()
    class Meta:
        

