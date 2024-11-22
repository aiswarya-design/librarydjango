from lib2to3.fixes.fix_input import context

from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from users.models import Users
from django.http import HttpResponse



# Create your views here.
def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']

        if(p==cp):
            u=User.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e)
            u.save()
        else:
            return HttpResponse("Password are not same")
        return redirect('users:login')
    return render(request,'adminregister.html')

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('book:home')
        else:
            return HttpResponse("invalid")
    return render(request,'login.html')
# @login_required()
def user_logout(request):
    logout(request)
    return redirect('users:login')
    # return login(request)
# @login_required()
def viewusers(request):
    k=Users.objects.all()
    context={'user':k}

    return render(request,'viewusers.html',context)
