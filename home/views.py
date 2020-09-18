# 17 September 2020
from django.shortcuts import render,HttpResponse
from .models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        category = request.POST['category']
        desc = request.POST['desc']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(category)< 4 or len(desc)<4:
            messages.error(request, "Please fill the form correctly!")
        else:
            contact = Contact(name=name, email=email, phone=phone, category=category, desc=desc)
            contact.save()
            messages.success(request, "Success! Your query has been sent successfully.")
    return render(request, 'home/contact.html')

def privacy(request):
    return render(request, 'home/privacy.html')

def terms(request):
    return render(request, 'home/terms.html')