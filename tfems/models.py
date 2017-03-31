from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_address=models.CharField(max_length=100)
    emp_phone=models.CharField(max_length=13)
    emp_email=models.CharField(max_length=100)
    emp_designation=models.CharField(max_length=100)
    emp_joining_date=models.DateField()
    emp_working_hours=models.IntegerField()

class LoginX(models.Model):
    uname=models.CharField(max_length=100)
    upass=models.CharField(max_length=100)