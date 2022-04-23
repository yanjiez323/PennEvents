from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from main.models import Tweet
from datetime import datetime
from main.models import Event
from django.http import HttpResponse
from .forms import *
import random


def main_view(request):
    if not request.user.is_authenticated:
        return redirect('/splash/')

    if request.method == 'POST' and request.POST['body'] != "":
        tweet = Tweet.objects.create(
         body = request.POST['body'],
         author = request.user,
         created_at = datetime.now()
    )
        tweet.save()
    
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'main.html', {'tweets': tweets})

def event_view(request):
    if not request.user.is_authenticated:
        return redirect('/splash/')

    if request.method == 'POST' and request.POST['name_of_org'] and request.POST['date'] and request.POST['description'] and request.POST['ticket_info'] and request.POST['social_media'] and request.POST['tag_choice'] != "":
        event = Event.objects.create(
         event_name = request.POST['event_name'],
         name_of_org = request.POST['name_of_org'],
         date = request.POST['date'],
         location = request.POST['location'],
         time = request.POST['time'],
         description = request.POST['description'],
         ticket_info = request.POST['ticket_info'],
         social_media = request.POST['social_media'],
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
    tweet = Tweet.objects.get(id=request.GET['id']) 
    if tweet.author == request.user: 
        tweet.delete() 
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
        event_results = Event.objects.filter(event_name__contains= searched)
        return render(request, 'search_results.html', 
        {'searched': searched, 
        'event_results': event_results})
    else:
        return render(request, 'search_results.html', {})
