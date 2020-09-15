from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bloghome'),
    path('ai', views.ai, name='ai'),
    path('ethical', views.ethical, name='ethical'),
    path("blogpost/<int:id>", views.blogpost, name="blogpost"),
]