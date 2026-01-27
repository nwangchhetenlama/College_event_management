from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages



def user_login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)

        if user:

            login(request,user)
            return redirect('/')

        else:
            messages.error(request,"username or password wrong.")

    return render(request,'accounts/login.html')


def user_logout(request):

    logout(request)
    return redirect('login')


def user_register(request):

    if request.method=='POST':

        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']


        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"username already exists")

            else:
                user=User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                messages.success(request,"user register succesfully")
                return redirect('/accounts/login')

        else:
            messages.warning(request,"password donot match")

    return render(request,'accounts/register.html')

        





