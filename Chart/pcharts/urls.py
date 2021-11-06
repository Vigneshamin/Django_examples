from django.contrib import admin
from django.urls import path
from pcharts import views

urlpatterns = [
    path("",views.ClubChartView.as_view(),name='home')
]
