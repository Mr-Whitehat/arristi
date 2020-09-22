from django.db import models
from django.utils.timezone import now

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    category = models.CharField(max_length=50)
    desc = models.TextField()
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.name