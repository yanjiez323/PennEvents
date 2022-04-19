from django.contrib import admin
from .models import Tweet
from .models import Event

admin.site.register(Tweet)
admin.site.register(Event)
# Register your models here.
