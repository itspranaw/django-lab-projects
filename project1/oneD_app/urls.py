from django.contrib import admin
from django.urls import path,include
from .views import todaytime
urlpatterns = [
    path('time/',todaytime,name='todaytime'),
]
