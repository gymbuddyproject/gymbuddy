from django.shortcuts import render
from django.http import HttpResponse
from gymbuddy.models import Gym

def index(request):
    gym_list = Gym.objects.all()
    context_dict = {"Gyms": gym_list}
    return render(request, 'gymbuddy/index.html', context_dict)

def about(request):
    return render(request, 'gymbuddy/about.html')

def login(request):
    return render(request, 'gymbuddy/login.html')

def signup(request):
    return render(request, 'gymbuddy/signup.html')

def contactus(request):
    return render(request, 'gymbuddy/contactus.html')

def gymprofile(request, gym_slug):
    context_dict = {}
    try:
        gym = Gym.objects.get(slug=gym_slug)
        context_dict["Gym"] = gym
    except Gym.DoesNotExist:
        context_dict["Gym"] = None

    return render(request, 'gymbuddy/gymprofile.html', context=context_dict)

def userprofile(request):
    return render(request, 'gymbuddy/userprofile.html')

def test(request):
    return render(request, 'gymbuddy/tester.html')
