from django.urls import path
from .views import search_student, get_student_courses

urlpatterns = [
    path('search/', search_student, name='search_student'),
    path('get_student_courses/', get_student_courses, name='get_student_courses'),
]
