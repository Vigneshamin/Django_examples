from django.shortcuts import render, HttpResponse
from home.models import Contact,Contactus
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        "variable":"this is sent"
    }
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')

def programming(request):
    return render(request, 'programming.html')

def python(request):
    return render(request, 'python.html')

def java(request):
    return render(request, 'java.html')

def other(request):
    return render(request, 'other.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        user = request.POST.get('user')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        comment = request.POST.get('comment')
        contact = Contact( name=name,user=user,email=email,mobile=mobile,comment=comment)
        contact.save()
    return render(request, 'contact.html')


def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        user = request.POST.get('user')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        comment = request.POST.get('comment')
        contactus = Contactus( name=name,user=user,email=email,mobile=mobile,comment=comment)
        contactus.save()
        messages.success(request, 'You comments have been saved!')
    return render(request, 'contactus.html')