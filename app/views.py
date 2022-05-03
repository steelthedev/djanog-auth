from django.shortcuts import render,redirect

from django.contrib.auth import login, authenticate

# Create your views here.

def Login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('dashboard')
    return render(request,'app/login.html')

def Dashboard(request):
    if request.user.is_authenticated:
        return render(request,'app/dashboard.html')
    else:
        return redirect('login')