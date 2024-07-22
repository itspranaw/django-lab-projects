from django.shortcuts import render, HttpResponse
from django.db.models import Q
from .models import Project

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

def projlist(request):
    names = Project.objects.values_list('name', flat=True).distinct()
    obj = Project.objects.all()
    return render(request, "projlist.html", {'obj': obj, 'names': names})
 
