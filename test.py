#!/usr/bin/env python
from bokeh.plotting import figure, output_file, show

plot = figure(width=300, height=300)
plot.annulus(x=[1, 2, 3], y=[1, 2, 3], color="#7FC97F",
             inner_radius=0.2, outer_radius=0.5)


output_file("log_lines.html")
show(plot)
