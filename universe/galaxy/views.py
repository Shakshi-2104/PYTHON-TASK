from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def galaxy(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())

def dynamic(request):
    data = {'clist':['python','java','php']}
    return render(request,'dynamic.html')

def homepage(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')