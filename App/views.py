from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hi():
    return HttpResponse('<h1> This is my Home Page! </h1>')

def myview(request):
    return render(request, "index.html")