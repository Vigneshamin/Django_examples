from django.contrib import admin
from django.urls import path, include
from login import views

urlpatterns = [
    path("", views.index, name='index'),
    path("login.html", views.loginuser, name='loginuser'),
    path("login", views.loginuser, name='loginuser'),
    path("loginuser", views.loginuser, name='loginuser'),
    path("logoutuser", views.logoutuser, name='loginuser')

]
