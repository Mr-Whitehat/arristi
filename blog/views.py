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
    ''' slugpost = Blogpost.objects.filter(slug=postslug) will give a Query set, check by (print(slugpost));
        but we require its first Object, so here we can use 
        "slugpost = Blogpost.objects.filter(slug=postslug)[0]" or 
        "slugpost = Blogpost.objects.filter(slug=postslug).first()" 
    '''
    if slugpost.category == 'cs':
        link = 'ethical'
        bCrumb = 'EH'
    elif slugpost.category == 'ai':
        link = 'ai'
        bCrumb = 'AI'
    return render(request, 'blog/blogpost.html',{'post': slugpost,'bCrumb': bCrumb, 'link': link})

# def blogpost(request,id):
#     post = Blogpost.objects.filter(post_id=id)[0]

