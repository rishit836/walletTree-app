from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "layout.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        u = authenticate(request,username=username,password=password)
        if u is not None:
            login(request,u)
            print("login was succesful")
            messages.success(request,"welcome " + str(u.username)+",login was succesful.")

    return render(request,'login.html')