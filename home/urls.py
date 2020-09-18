from django.urls import path  #,include
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('privacy', views.privacy, name='contact'),
    path('terms', views.terms, name='contact'),
]




