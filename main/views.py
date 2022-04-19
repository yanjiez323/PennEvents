from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from main.models import Tweet
from datetime import datetime
from main.models import Event

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

    if request.method == 'POST' and request.POST['name_of_org'] and request.POST['date'] and request.POST['description'] and request.POST['ticket_info'] and request.POST['social_media'] and request.POST['tags'] != "":
        event = Event.objects.create(
         event_name = request.POST['event_name'],
         name_of_org = request.POST['name_of_org'],
         date = request.POST['date'],
         location = request.POST['location'],
         time = request.POST['time'],
         description = request.POST['description'],
         ticket_info = request.POST['ticket_info'],
         social_media = request.POST['social_media'],
         tag_choices = request.POST['tag_choices']
    )
        event.save()
    
    events = Event.objects.all().order_by('date')
    return render(request, 'main.html', {'events': events})

    
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