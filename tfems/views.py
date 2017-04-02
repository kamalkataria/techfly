from django.shortcuts import render,HttpResponse
from tfems.models import LoginX,Employee
from tfems.forms import EmployeeForm
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
    formx=EmployeeForm()
    return render(request,'tfems/addform.html',{'form':formx})