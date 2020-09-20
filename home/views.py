# 17 September 2020
from django.shortcuts import render,HttpResponse, redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Blogpost

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

def search(request):
    query = request.GET['query']
    if len(query)>80:
        matchedposts = Blogpost.objects.none()
    else:
        matchedpoststitle = Blogpost.objects.filter(title__icontains=query)
        matchedpostscontent = Blogpost.objects.filter(content__icontains=query)
        matchedpostsauthor = Blogpost.objects.filter(author__icontains=query)
        matchedpoststimeStamp = Blogpost.objects.filter(timeStamp__icontains=query)
        print(matchedpoststimeStamp)
        matchedpostscategory = Blogpost.objects.filter(category__icontains=query)
        matchedpostsDesc = Blogpost.objects.filter(descForCard__icontains=query)
        matchedposts = matchedpoststitle.union(matchedpostscontent).union(matchedpostsauthor).union(matchedpoststimeStamp).union(matchedpostscategory).union(matchedpostsDesc)

    if matchedposts.count() ==0:
        messages.warning(request, "No search found!")
    count = 0
    for i in matchedposts:
        count += 1;
    dic = {'matchedposts':matchedposts, 'nPosts': count, 'query':query}
    return render(request, 'home/search.html', dic)

def signup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']
        # print(username, fname, lname, email, password1, password2)

        # Check the errorneous inputs

        '''Username should be anything:
        #
        # # Username should only contain letters & numbers:
        # if not username.isalnum():
        #     messages.error(request, "Username should only contain letters & numbers!")
        #     return redirect("index")
        '''
        # Username less then 30 characters:
        if len(username)>30:
            messages.error(request, "Username must be under 30 characters!")
            return redirect("index")

        # First name should only contain letters:
        if not fname.isalpha():
            messages.error(request, "First name should only contains letters!")
            return redirect("index")

        # Last name should only contain letters:
        if not lname.isalpha():
            messages.error(request, "Last name should only contains letters!")
            return redirect("index")

        # Password must contains atleast 8 characters:
        if len(password1) < 8:
            messages.error(request, "Password must contains atleast 8 characters!")
            return redirect("index")

        # Passsword should not only contains letters:
        if password1.isalpha():
            messages.error(request, "Password must contains letters (capital & small), numbers & special characters!")
            return redirect("index")

        # Passsword should not only contains numbers:
        if password1.isnumeric():
            messages.error(request, "Password must contains letters (capital & small), numbers & special characters!")
            return redirect("index")

        # Passsword must contains atleast one capital letter:
        oneCapital = False
        for letter in password1:
            if letter.isupper():
                oneCapital = True

        if oneCapital == False:
            messages.error(request, "Password must contains letters (capital & small), numbers & special characters!")
            return redirect("index")

        # Passsword must contains special characters:
        if password1.isalnum():
            messages.error(request, "Password must contains letters (capital & small), numbers & special characters!")
            return redirect("index")

        # Passwords should match:
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect("index")


        # Create the user
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Arristi account has been successfully created!")
        return redirect("index")

    else:
        return HttpResponse("404 error!")

def Login(request):
    if request.method == "POST":
        uname = request.POST['uname']
        passw = request.POST['passw']

        user = authenticate(username=uname, password=passw)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In!")
            return redirect("index")
        else:
            messages.error(request, "Invalid Username/Password. Please try again!")
            return redirect("index")
    else:
        return HttpResponse("404 error")

def Logout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Successfully Logged Out!")
        return redirect("index")
    else:
        return HttpResponse("404 error")

def privacy(request):
    return render(request, 'home/privacy.html')

def terms(request):
    return render(request, 'home/terms.html')