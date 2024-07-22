from django.urls import path
from .import views

urlpatterns = [
    path('', views.projform, name='projform'),
    path('projlist/', views.projlist, name='projlist'),
]
