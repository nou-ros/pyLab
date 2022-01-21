#figure - for creting plot, 
#output_file - generate the html file to show
#show - will show the output_file
from bokeh.plotting import figure, output_file, show

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

output_file('prac1.html')

# Add plot
p = figure( 
    title = "Simple Example",
    x_axis_label = 'X Axis',
    y_axis_label = 'Y Axis'
    )

# adding glyph 
p.line(x, y, legend_label="Test", line_width=2)


# Show the result
show(p)