from django.shortcuts import render
from django.http import HttpResponse

def demo(request):
    return HttpResponse("Second Project")

def home(request):
    return render(request, 'base.html',{"name":"pranay"}) 

