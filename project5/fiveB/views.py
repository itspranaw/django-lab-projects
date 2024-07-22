# enrolment/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Student

def search_student(request):
    return render(request, 'search.html')

def get_student_courses(request):
    if request.method == 'GET':
        name = request.GET.get('name', None)
        try:
            student = Student.objects.get(name = name)
            courses = student.courses.all()
            courses_list = list(courses.values('name'))
            return JsonResponse({'success': True, 'courses': courses_list})
        except Student.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Student not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})
