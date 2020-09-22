from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

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

# sno, comment, user, post, parent, timestamp
class PostComment(models.Model):
    sno = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        if self.parent == None:
            com_rep = 'Comment'
        else:
            com_rep = 'Reply'
        return com_rep + ' -> ' + self.comment[0:20] + '... by ' + self.user.username