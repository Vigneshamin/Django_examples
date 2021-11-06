

from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("programming",views.programming, name='programming'),
    path("python", views.python, name='python'),
    path("java", views.java, name='java'),
    path("other", views.other, name='other'),
    path("contactus", views.contactus, name='contactus')

]
