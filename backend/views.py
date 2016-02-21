import datetime
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from backend.models import *
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components

import numpy as np
from bokeh.charts import Line

def add_point(request, value):
    new_reading = Reading(time=timezone.now(), weight=value)
    new_reading.save()
    return HttpResponse("")

def name(request):
    return HttpResponse("Bananas")

def index(request):
    plot = figure(width=800, height=600)
    plot.title = "Banana weight"
    plot.xaxis.axis_label = "Date"
    plot.yaxis.axis_label = "Weight"

    xvalues = [1, 2, 3, 4, 5]
    yvalues = [6, 7, 2, 4, 5]

    plot.line([1, 2, 3, 4, 6], [6, 7, 2, 4, 5], line_width=2)

    script, div = components(plot, CDN)

    return HttpResponse(Reading.objects.values_list('weight', flat=True))

    #return render(request, "simple_chart.html", {"the_script": script, "the_div": div})
