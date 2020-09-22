from django.urls import path
from . import views
urlpatterns = [

    # API display a comment:
    path('postcomment', views.postcomment, name='postcomment'),

    path('', views.index, name='bloghome'),
    path('ai', views.ai, name='ai'),
    path('ethical', views.ethical, name='ethical'),
    path('blogpost/<str:postslug>', views.blogslug, name='slug'),
    # path("blogpost/<int:id>", views.blogpost, name="blogpost"),


]

