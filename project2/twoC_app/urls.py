from django.urls import path
from .import views
urlpatterns=[
    path('2c/',views.index,name='home'),
    path('stlist/',views.stlist,name='stlist'),
    path('colist/',views.colist,name='colist'),
]