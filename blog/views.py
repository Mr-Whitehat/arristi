from django.shortcuts import render
from .models import Blogpost

def index(request):
    return render(request, 'blog/index.html')

def ai(request):
    category = Blogpost.objects.filter(category='ai')
    return render(request, 'blog/ai.html',{'category':category})

def ethical(request):
    category = Blogpost.objects.filter(category='cs')
    return render(request, 'blog/ethical.html',{'category':category})

def blogpost(request,id):
    post = Blogpost.objects.filter(post_id=id)[0]
    return render(request, 'blog/blogpost.html',{'post': post})

# def index(request):
#     post = Blogpost.objects.all()
#     print(post)
#     return render(request, 'blog/index.html', {'post': post})

