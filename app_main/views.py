from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "home.html")

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

def signup_view(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("email")
            u = User.objects.create_user(username=username,email=email,password=password)
            u.save()
            messages.success(request,"welcome to wallettree, pls login.")
        except Exception as e:
            messages.error(request,e)


        return redirect("main:login")
    return render(request,"signup.html")

def logout_view(request):
    logout(request)
    messages.success(request,"you have been succesfully logged out")
    return redirect("main:login")