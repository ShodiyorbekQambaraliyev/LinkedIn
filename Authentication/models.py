from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/img/')
    location = models.CharField(max_length=50)
    ish = models.CharField(max_length=100, null=True)
    bio = models.TextField()
    profilBanner = models.ImageField(upload_to='static/img/')
    fullname = models.CharField(max_length=50)
    
    
    def __str__(self):
        return f"{self.fullname}"
    
    