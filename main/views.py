from django.shortcuts import *

# Create your views here.
def home(request):
    return render(request,'main/home.html')

def collections(request):
    return render(request,'collections.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def registration(request):
    return render(request,'registration.html')

def login(request):
    return render(request,'login.html')