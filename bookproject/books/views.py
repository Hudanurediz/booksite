from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from books.models import User

def index(request): 
    return render(request, 'index.html')

def logins(request):
    return render(request,'login.html')

def homepage(request):
    return render(request,'homepage.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        print(request)
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Geçersiz kullanıcı adı veya parola.')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username=request.POST["username"]
        email=request.POST["email"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        password=request.POST["password"]
        password2=request.POST["password2"]
        if password == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'kayitol.html', {'message': 'Username kullanılıyor'})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, 'kayitol.html', {'message': 'Email kullanılıyor'})
                else:
                    user=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
                    user.save()
                    return render(request, 'login.html')
        else:
            return render(request, 'kayitol.html', {'message': 'Hatali parola'})

def logoutview(request):
    logout(request)
    return render(request, 'login.html')  # Oturumdan çıkış yaptıktan sonra yönlendirilecek sayfa
