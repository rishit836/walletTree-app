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
        
        # Use authenticate() to check credentials properly
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            print("login was successful")
            messages.success(request, f"Welcome {user.username}, login was successful.")
            return redirect('main:home')  # Redirect after successful login
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')