from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model): 
    body = models.TextField(max_length=300) 
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    created_at = models.DateTimeField() 

class Event(models.Model):
    event_name = models.TextField(max_length=100, null=True)
    name_of_org = models.TextField(max_length=300, null=True)
    location = models.TextField(max_length=300, null=True)
    date = models.TextField(max_length=300, null=True)
    time = models.TextField(max_length=15, null=True)
    description = models.TextField(max_length=1000, null=True)
    ticket_info = models.TextField(max_length=100, null=True)
    social_media = models.CharField(max_length=100, null=True)
    FREE = 'free'
    ACADEMIC = 'academic'
    ATHLETIC = 'athletic'
    FOOD = 'food'
    CULTURAL = 'cultural'
    TAGS = [
        (FREE, 'free'),
        (ACADEMIC, 'academic'),
        (ATHLETIC, 'athletic'),
        (FOOD, 'food'),
        (CULTURAL, 'cultural'),
    ]
    tag_choices = models.CharField(
        max_length=8,
        choices=TAGS,
        null=True
    )
    # upload_image = models.ImageField(upload_to='images/')


    
def __str__(self): 
    return self.body 
