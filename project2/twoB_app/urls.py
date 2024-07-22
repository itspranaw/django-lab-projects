from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('2b/',layout,name='layout'),
    path('home/',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
]
