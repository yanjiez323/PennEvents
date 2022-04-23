from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _



class Event(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    event_name = models.TextField(max_length=100, null=True)
    name_of_org = models.TextField(max_length=300, null=True)
    location = models.TextField(max_length=300, null=True)
    date = models.TextField(max_length=300, null=True)
    time = models.TextField(max_length=15, null=True)
    description = models.TextField(max_length=1000, null=True)
    ticket_info = models.TextField(max_length=100, null=True)
    social_media = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=50, null=True)
    upload_image = models.ImageField(upload_to='images/', null=True, blank=True)

    
def __str__(self): 
    return self.body 
