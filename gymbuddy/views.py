from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'gymbuddy/index.html')

def about(request):
    return HttpResponse("Use the map to search for gyms and training partners.")

def login(request):
    return render(request, 'gymbuddy/login.html')

def signup(request):
    return render(request, 'gymbuddy/signup.html')

def test(request):
    return render(request, 'gymbuddy/tester.html')
