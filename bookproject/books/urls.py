from django.urls import path
from . import views

urlpatterns= [
    path('',views.index, name='index'),
    path('index/',views.index,name='index'),
    path('login/',views.user_login, name='user_login'),   
    path('homepage/',views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
]

