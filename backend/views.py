import datetime
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from backend.models import *
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
from bokeh.sampledata.stocks import AAPL

def add_point(request, value):
    new_reading = Reading(time=timezone.now(), weight=value)
    new_reading.save()
    return HttpResponse("")

def name(request):
    return HttpResponse("Bananas")

def index(request):
    plot = figure(width=800, height=600)
    plot.title = "Banana weight"
    p1.xaxis.axis_label = "Date"
    plot.yaxis.axis_label = "Weight"
    plot.line(datetime(AAPL['date']), AAPL['adj_close'])

    script, div = components(plot, CDN)

    return render(request, "simple_chart.html", {"the_script": script, "the_div": div})
