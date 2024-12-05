from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.


def home1(request):
    post=Blog.objects.all()
    return render(request, 'base.html',{'post':post}) 


def home4(request):
    return render(request, 'base.html',{"name":"pranay"}) 


def home(request):
    return render(request,'home.html')