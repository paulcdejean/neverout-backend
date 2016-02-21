import datetime
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from backend.models import *
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components

def add_point(request, value):
    new_reading = Reading(time=timezone.now(), weight=value)
    new_reading.save()
    return HttpResponse("")

def name(request):
    return HttpResponse("Bananas")

def index(request):
    plot = figure(width=300, height=300)
    plot.annulus(x=[1, 2, 3], y=[1, 2, 3], color="#7FC97F", inner_radius=0.2, outer_radius=0.5)

    script, div = components(plot, CDN)

    return render(request, "simple_chart.html", {"the_script": script, "the_div": div})
