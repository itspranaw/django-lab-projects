from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('studentdetail/<str:name>/', views.student_detail, name='studentdetail'),
    path('projform/', views.projform, name='home'),
    path('list/', views.stlist, name='list'),
    path('colist/', views.colist, name='colist'),
    path('view/', views.view, name='view'),
]
