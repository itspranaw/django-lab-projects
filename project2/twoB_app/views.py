from django.shortcuts import render
from django.http import HttpResponse
def layout(request):
    return render(request,'layout.html')
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')