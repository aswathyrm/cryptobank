from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def form(request):
    return render(request,"form.html")

def index(request):
    return render(request,"index.html")

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('form')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print("user registered")
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"Passwords do not match")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def onclick(request):
    messages.info(request,"Application accepted")