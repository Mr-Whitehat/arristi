from django.shortcuts import render
from .models import Blogpost
# Create your views here.
def index(request):
    post = Blogpost.objects.all()
    # print(post)
    return render(request, 'blog/index.html', {'post': post})

def blogpost(request):
    # post = Blogpost.objects.filter(post_id=id)
    return render(request, 'blog/blogpost.html')