from django.contrib.sitemaps import Sitemap
from blog.models import Blogpost

class BlogpostSitemap(Sitemap):
    changefreq = "always"  # always, hourly, daily, weekly, monthly, yearly
    priority = 0.0

    def items(self):
        # print(Blogpost.objects.filter(category='cs'))
        return Blogpost.objects.all() #filter(category='cs') #all()  #filter(status = 1)
    
    def lastmod(self, obj):
        return obj.timeStamp #timeStamp #updated_on