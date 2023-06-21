from django.shortcuts import render
from django.http import HttpResponse


def index(request): 
    return render(request, 'index.html')

def logins(request):
    return render(request,'login.html')

def homepage(request):
    return render(request,'homepage.html')