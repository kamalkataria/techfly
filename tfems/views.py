from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from tfems.models import LoginX,Employee
from tfems.forms import EmployeeForm
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'tfems/index.html')
def logintosys(request):
    if(request.method=="POST"):
        uname=request.POST.get('uname')
        password=request.POST.get('upass')
        logx=LoginX.objects.filter(uname=uname,upass=password)
        if(len(logx)==1):
            emp=Employee.objects.all()
            if(len(Employee.objects.all())==0):
                return render(request, 'tfems/techfly.html',{'uname':uname})
            else:
                return render(request, 'tfems/techfly.html',{'uname':uname,'employee':emp})

        elif(0>len(logx)>=1):
            return HttpResponse('Login Problem,Multiple User Accounts')
        else:
            return HttpResponse('Login Failed')
    else:
        return render(request, 'tfems/techfly.html',{'nlin':'Not Logged In'})
def addemp(request):
    print('Inside addemp')
    if(request.method=='POST'):
        print('POST METHOD')
        formx=EmployeeForm(request.POST)
        if(formx.is_valid()):
            formx.save()
            messages.success(request, 'Form saved')
            return HttpResponseRedirect(reverse('addemp'))
        else:
            messages.error(request,'Form Invalid.')

            return HttpResponseRedirect(reverse('addemp'))

    else:

        print('NOT POST METHOD')

        formx=EmployeeForm()
        return render(request,'tfems/addform.html',{'form':formx})


def delEmp(request,empname,uname):
    Employee.objects.filter(emp_name=empname).delete()
    emp = Employee.objects.all()
    return render(request, 'tfems/techfly.html', {'uname': uname, 'employee': emp})

def editEmp(request,empname,uname):
    print('Inside edit Emp')
    exmp=Employee.objects.filter(emp_name=empname)
    if(request.method=='POST'):
        print('Inside post')
        formx = EmployeeForm(request.POST)
        if (formx.is_valid()):
            row=Employee.objects.get(emp_name=empname)
            fxc=EmployeeForm(request.POST,instance=row)
            fxc.save()
            messages.success(request, 'Information Updated')
            emp = Employee.objects.all()
            return render(request, 'tfems/techfly.html', {'uname': uname, 'employee': emp})
        else:
            messages.warning(request, 'Information entered is incorrect')
            emp = Employee.objects.all()
            return render(request, 'tfems/techfly.html', {'uname': uname, 'employee': emp})
    else:
        print('Inside elseedit')
        form = EmployeeForm()

        for p in exmp:
            data={

            'emp_name':p.emp_name,
            'emp_phone':p.emp_phone,
            'emp_email':p.emp_email,
            'emp_designation':p.emp_designation,
            'emp_joining_date':p.emp_joining_date,
            'emp_working_hours':p.emp_working_hours,
            'emp_address':p.emp_address
            }
            form = EmployeeForm(data)

            return render(request, 'tfems/addemp.html', {'formz':form,'empname':empname})





