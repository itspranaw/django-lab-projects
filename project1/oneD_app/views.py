from django.shortcuts import render
from datetime import datetime,timedelta

def todaytime(request):
    now=datetime.now()
    ahead=now+timedelta(hours=4)
    before=now-timedelta(hours=4)
    context={
        'ahead':ahead.strftime("%Y-%M-%D %H:%M:%S"),
        'before':before.strftime("%Y-%M-%D %H:%M:%S")
    }
    return render(request,'index2.html',context)