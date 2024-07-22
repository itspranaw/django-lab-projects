from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def testing(request):
    template=loader.get_template('index.html')
    context={
        'fruits':['Apple','Banana','Cherry','Kiwi','Orange'],
        'students':['Ram','Rahim','Anuj','Yashpal','Radhe']
    }
    return HttpResponse(template.render(context,request))
