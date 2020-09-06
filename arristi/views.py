# 06 September 2020
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')
    # return HttpResponse("request,'index.html'")

def ai(request):
    return render(request, 'ai.html')

def ethical(request):
    return render(request, 'ethical.html')