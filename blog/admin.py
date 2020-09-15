from django.contrib import admin
from .models import Blogpost
# Register your models here.
# admin.site.register(Blogpost)

@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    class Media:
        js = ('TineMCE.js',)
