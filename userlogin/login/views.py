from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/loginuser")
    return render(request,"index.html")

def loginuser(request):
    if request.method == "POST":
        username= request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request,'loginuser.html')
    return render(request,'loginuser.html')

def logoutuser(request):
    logout(request)
    return redirect("/loginuser")