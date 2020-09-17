from django.shortcuts import render
from .models import Blogpost

def index(request):
    return render(request, 'blog/index.html')

def ai(request):
    category = Blogpost.objects.filter(category='ai')
    count = 0;
    for i in category:
        count += 1;
    return render(request, 'blog/ai.html',{'category':category, 'nPosts': count})

def ethical(request):
    category = Blogpost.objects.filter(category='cs')
    count = 0;
    for i in category:
        count += 1;
    return render(request, 'blog/ethical.html',{'category':category, 'nPosts': count})

def blogpost(request,id):
    post = Blogpost.objects.filter(post_id=id)[0]
    title = post.title;
    print(title)
    if post.category == 'cs':
        link = 'ethical'
        bCrumb = 'EH'
    elif post.category == 'ai':
        link = 'ai'
        bCrumb = 'AI'
    return render(request, 'blog/blogpost.html',{'post': post, 'bCrumb': bCrumb, 'link': link, 'title': title})

# def index(request):
#     post = Blogpost.objects.all()
#     print(post)
#     return render(request, 'blog/algo.html', {'post': post})

