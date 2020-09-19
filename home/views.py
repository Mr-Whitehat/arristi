# 17 September 2020
from django.shortcuts import render,HttpResponse
from .models import Contact
from django.contrib import messages
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

def privacy(request):
    return render(request, 'home/privacy.html')

def terms(request):
    return render(request, 'home/terms.html')