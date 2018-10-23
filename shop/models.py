from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=True)
    names = models.CharField(max_length=50)
    email = models.EmailField()
        
    def __str__(self):
        return self.names

    class Meta:
        ordering = ['names']

class Tag (models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name        

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='home/', blank=True)
    name = models.CharField(max_length=25, blank=True)
    caption = models.TextField(max_length=25)
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Blog(models.Model):
    author = models.ForeignKey(User)
    date = models.DateField()
    title = models.CharField(max_length=100)
    post = models.TextField()