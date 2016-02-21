from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def add_point(request, value):
    return HttpResponse("Hello, world. You're at the polls index." + value)
