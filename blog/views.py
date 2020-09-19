from django.shortcuts import render, HttpResponse
from .models import Blogpost

def index(request):
    return render(request, 'blog/bloghome.html')

def ai(request):
    aiposts = Blogpost.objects.filter(category='ai')
    count = 0;
    for i in aiposts:
        count += 1;
    return render(request, 'blog/ai.html',{'aiposts':aiposts, 'nPosts': count})

def ethical(request):
    csposts = Blogpost.objects.filter(category='cs')
    count = 0;
    for i in csposts:
        count += 1;
    return render(request, 'blog/ethical.html',{'csposts':csposts, 'nPosts': count})

def blogslug(request,postslug):
    slugpost = Blogpost.objects.filter(slug=postslug)[0]
    if slugpost.category == 'cs':
        link = 'ethical'
        bCrumb = 'EH'
    elif slugpost.category == 'ai':
        link = 'ai'
        bCrumb = 'AI'
    return render(request, 'blog/blogpost.html',{'post': slugpost,'bCrumb': bCrumb, 'link': link})

# def ai(request):
#     category = Blogpost.objects.filter(category='ai')
#     count = 0;
#     for i in category:
#         count += 1;
#     return render(request, 'blog/ai.html',{'category':category, 'nPosts': count})
#
# def ethical(request):
#     category = Blogpost.objects.filter(category='cs')
#     count = 0;
#     for i in category:
#         count += 1;
#     return render(request, 'blog/ethical.html',{'category':category, 'nPosts': count})
#
# def blogpost(request,id):
#     post = Blogpost.objects.filter(post_id=id)[0]
#     # title = post.title;
#     slu = post.slug
#     print(slu)
#     if post.category == 'cs':
#         link = 'ethical'
#         bCrumb = 'EH'
#     elif post.category == 'ai':
#         link = 'ai'
#         bCrumb = 'AI'
#     return render(request, 'blog/blogpost.html',{'post': post, 'bCrumb': bCrumb, 'link': link})

# def index(request):
#     post = Blogpost.objects.all()
#     print(post)
#     return render(request, 'blog/algo.html', {'post': post})

