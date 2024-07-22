from django.urls import path
from . import views

urlpatterns = [
	path('4b/', views.home, name='home'),
	path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
    path('generate-csv/', views.generate_csv, name='generate_csv'),
]
