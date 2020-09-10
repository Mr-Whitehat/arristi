from django.shortcuts import render
from .models import Blogpost
# Create your views here.
def index(request):
    post = Blogpost.objects.all()
    print(post)
    return render(request, 'blog/index.html', {'post': post})

def blogpost(request,id):
    post = Blogpost.objects.filter(post_id=id)[0]
    print(post)
    return render(request, 'blog/blogpost.html',{'post': post})