from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bloghome'),
    path("blogpost/", views.blogpost, name="blogpost") #<int:id>
]