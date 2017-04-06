from django.shortcuts import render,HttpResponse,reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request, 'log/signuppage.html')
def signup(request):
    print('Inside signup')
    if(request.method=='POST'):
        usernamed=request.POST.get('username')
        passwordd=request.POST.get('password')
        email=request.POST.get('email')
        if(User.objects.filter(username=usernamed)).exists():
            messages.error(request,"User Already Exists")
        else:
            try:
                User.objects.create_user(username=usernamed,email=email,password=passwordd)
                messages.success(request,'User Created Successfully')

            except:
                # return HttpResponse('Error in creating')
                messages.warning(request,'Error in creating')
    else:
        messages.success('Please Login')
    return HttpResponseRedirect(reverse(index))
