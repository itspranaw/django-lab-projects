from django.shortcuts import render
from datetime import datetime

date=datetime.now()
def todaytime(request):
    return render(request,'index.html',{'date':date})