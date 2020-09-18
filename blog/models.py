from django.db import models

# Create your models here.
class Blogpost(models.Model):
    categorychoices = (
        ('ai', 'Artificial Intelligence'),
        ('cs', 'Ethical Hacking')
    )
    post_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=2, default="ai", choices=categorychoices)
    slug = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    descForCard = models.CharField(max_length=500)
    content = models.TextField()
    author = models.CharField(max_length=50)
    timeStamp = models.DateTimeField(blank=True)
    thumbnail = models.ImageField(upload_to='blog/images')

    def __str__(self):
        return self.category + '-> ' + self.title + ' by ' + self.author