from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # user = models.OneToOneField(user, on_delete=models.CASCADE)
    names = models.CharField(max_length=50)
    email = models.EmailField()
        
    def __str__(self):
        return self.names
