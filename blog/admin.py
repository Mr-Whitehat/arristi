from django.contrib import admin
from .models import Blogpost, PostComment
# Register your models here.
admin.site.register(PostComment)

@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    class Media:
        js = ('TineMCE.js',)
