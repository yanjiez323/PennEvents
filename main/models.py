from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model): 
    body = models.TextField(max_length=300) 
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    created_at = models.DateTimeField() 
def __str__(self): 
    return self.body 
