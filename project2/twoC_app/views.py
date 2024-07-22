from django.shortcuts import render,HttpResponse
from .models import Student,Course

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
    courses=Course.objects.values_list('name',flat=True).distinct()
    return render(request, 'index2.html',{'courses':courses})

def stlist(request):
    selected_course = request.GET.get('course', '')
    courses = Student.objects.values_list('course', flat=True).distinct()
    if selected_course:
        obj = Student.objects.filter(course=selected_course)
    else:
        obj = Student.objects.all()
    return render(request, "stlist.html", {'obj': obj, 'courses': courses, 'selected_course': selected_course})

def colist(request):
    obj = Course.objects.all()
    return render(request, "colist.html", {'obj': obj})