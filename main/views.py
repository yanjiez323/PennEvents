from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from main.models import Event
from django.http import HttpResponse
from .forms import *
import random


def event_view(request):
    if not request.user.is_authenticated:
        return redirect('/splash/')

    if request.method == 'POST':
        event = Event.objects.create(
         author = request.user,
         event_name = request.POST.get('event_name', False),
         name_of_org = request.POST.get('name_of_org', False),
         date = request.POST.get('date', False),
         location = request.POST.get('location', False),
         time = request.POST.get('time', False),
         description = request.POST.get('description', False),
         ticket_info = request.POST.get('ticket_info', False),
         social_media = request.POST.get('social_media', False)
    )
        event.save()
    
    events = Event.objects.all().order_by('date')
    return render(request, 'main.html', {'events': events})

def upload_image_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
        return render(request, 'main.html', {'form' : form})


    
def splash_view(request):
    return render(request, 'splash.html' )

def login_view(request): 
    username, password = request.POST['username'], request.POST['password'] 
    user = authenticate(username=username, password=password) 
 
    if user is not None: 
        login(request, user) 
        return redirect('/') 
    else: 
        return redirect('/splash?error=LoginError')

def signup_view(request): 
    user = User.objects.create_user( 
        username=request.POST['username'], 
        password=request.POST['password'], 
        email=request.POST['email'], 
) 
    login(request, user) 
    return redirect('/')

def logout_view(request): 
    logout(request) 
    return redirect('/splash')

def delete_view(request): 
    event = Event.objects.get(id=request.GET['id']) 
    if event.author == request.user: 
        event.delete() 
    return redirect('/')

# Random Button


def get_random_page(request):
    pick = list(Event.objects.all())
    pick = random.sample(pick, 1)

    return render(request, 'random.html', {'pick': pick})

#Search button

def search_results(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        event_results = Event.objects.filter(name_of_org__contains= searched)
        return render(request, 'search_results.html', 
        {'searched': searched, 
        'event_results': event_results})
    else:
        return render(request, 'search_results.html', {})

# Upload page

def upload(request):
    return render(request, 'upload.html', {})

# Surprise me page

def surprise_me(request):
    return render(request, 'surprise_me.html', {})