from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50, default="")
    title = models.CharField(max_length=500, default="")
    descForCard = models.CharField(max_length=500, default="")
    content = models.TextField(default="")
    author = models.CharField(max_length=50, default="")
    pub_date = models.DateField(default="")
    timeStamp = models.DateTimeField(blank=True, default="")
    thumbnail = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return self.category + '-> ' + self.title + ' by ' + self.author