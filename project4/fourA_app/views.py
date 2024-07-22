from django.shortcuts import render, HttpResponse
from django.db.models import Q
from .models import Student,Course,Project

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        dob = request.POST['dob']
        gender = request.POST['gender']
        course = request.POST['course']
        usn = request.POST['usn']
        sec = request.POST['sec']
        cgpa = request.POST['cgpa']
        if float(cgpa) < 0 or float(cgpa) > 10:
            return HttpResponse("CGPA must be in the range 0-10")
        obj = Student(name=name, email=email, dob=dob, gender=gender, course=course, sec=sec, usn=usn, cgpa=cgpa)
        obj.save()
        return HttpResponse("Form submitted")
    courses=Course.objects.all()
    return render(request,'index.html',{'courses': courses})

def projform(request):
    if request.method == 'POST':
        name = request.POST['name']
        usn = request.POST['usn']
        proj = request.POST['proj']
        lang = request.POST['lang']
        duration = request.POST['duration']
        obj = Project(name=name, usn=usn, proj=proj, lang=lang, duration=duration)
        obj.save()
        return HttpResponse("Form submitted")
    return render(request, 'projform.html')

def stlist(request):
    selected_course = request.GET.get('course', '')
    courses = Student.objects.values_list('course', flat=True).distinct()
    if selected_course:
        obj = Student.objects.filter(course=selected_course)
    else:
        obj = Student.objects.all()
    return render(request, "list.html", {'obj': obj, 'courses': courses, 'selected_course': selected_course})

def colist(request):
    selected_course = request.GET.get('name', '')
    names = Course.objects.values_list('name', flat=True).distinct()
    if selected_course:
        obj = Course.objects.filter(name=selected_course)
    else:
        obj = Course.objects.all()
    return render(request, "colist.html", {'obj': obj, 'names': names, 'selected_course': selected_course})

def view(request):
    names = Project.objects.values_list('name', flat=True).distinct()
    obj = Project.objects.all()
    return render(request, "projlist.html", {'obj': obj, 'names': names})
 


def student_detail(request, name):
    names = Project.objects.values_list('name', flat=True).distinct()
    if name:
        obj = Project.objects.filter(name=name)
    else:
        return HttpResponse('No Student data')
    return render(request, 'student_detail.html', {'obj':obj})
