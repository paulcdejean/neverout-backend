from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from backend.models import *

def add_point(request, value):
    new_reading = Reading(3.14)
    new_reading.save()
    return HttpResponse(Reading.objects.all())
