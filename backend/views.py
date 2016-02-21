import datetime
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from backend.models import *
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
from bokeh.models import Span

import numpy as np
from bokeh.charts import Line

def add_point(request, value):
    new_reading = Reading(time=timezone.now(), weight=value)
    new_reading.save()
    return HttpResponse("")

def name(request):
    return HttpResponse("Bananas")

def index(request):
    plot = figure(width=800, height=600, x_axis_type="datetime")
    plot.title = "Banana weight"
    plot.xaxis.axis_label = "Date"
    plot.yaxis.axis_label = "Weight"

    xvalues = Reading.objects.values_list('time', flat=True)
    yvalues = Reading.objects.values_list('weight', flat=True)

    plot.line(xvalues, yvalues, line_width=2)


    empty_line = Span(location=1, dimension='width', line_color='green', line_width=3, line_dash='dashed')
    full_line = Span(location=7, dimension='width', line_color='green', line_width=3, line_dash='dashed')
    plot.renderers.extend([empty_line, full_line])

    script, div = components(plot, CDN)

    return render(request, "simple_chart.html", {"the_script": script, "the_div": div})

def set_empty(request, value):
    try:
        limit = Limits.objects.get(device=0)
        limit.empty = value
        limit.save()
    except ObjectDoesNotExists:
        limit = Limits(device=0, empty=value)
        limit.save()
    return HttpResponse("")

def set_full(request, value):
    try:
        limit = Limits.objects.get(device=0)
        limit.full = value
        limit.save()
    except ObjectDoesNotExists:
        limit = Limits(device=0, full=value)
        limit.save()
    return HttpResponse("")
