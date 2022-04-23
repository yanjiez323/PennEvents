from django import forms
from .models import *
  
class ImageForm(forms.ModelForm):
  
    class Meta:
        model = Event
        fields = ['name', 'upload_image']