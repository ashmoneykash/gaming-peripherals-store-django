from django.shortcuts import *
from .models import ContactMessage

# Create your views here.
def home(request):
    return render(request,'main/home.html')

def collections(request):
    return render(request,'collections.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if name and email and subject and message:
            ContactMessage.objects.create(
                user=request.user if request.user.is_authenticated else None,
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            return render(request, "main/contact.html", {
                "success": True
            })

    return render(request, "main/contact.html")

def registration(request):
    return render(request,'registration.html')

def login(request):
    return render(request,'login.html')