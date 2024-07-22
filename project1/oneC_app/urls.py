from django.contrib import admin
from django.urls import path,include
from .views import todaytime

urlpatterns = [
    path('',todaytime,name="todaytime"),
]