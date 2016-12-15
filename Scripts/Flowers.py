from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d

#Naming the output html and defining the path
output_file("C:\Users\labuser\Documents\Python_Data_Analysis\Learning_Bokeh\Output\iris.html")

#Defining the object
f=figure()

"""Stylizing the plot area"""
f.plot_width=1500
f.plot_height=800
f.background_fill_color = "#CD5C5C"
f.background_fill_alpha = 0.1
#f.border_fill_color = 'black'
#f.axis.axis_label_text_color = 'white'
#f.axis.major_tick_line_color = 'white' #TODO: Experiment!

"""Title"""
f.title.text = 'Iris Morphology'
#f.title.text_color = 'Red'
#f.title.text_font = "times"
f.title.text_font_size = "44px"
f.title.align = "center"

"""Axis"""
#f.axis.axis_line_color = 'blue'
#f.xaxis.axis_line_color = None
#f.axis.major_tick_line_color = 'blue'
#f.yaxis.major_label_orientation = 'vertical'
#f.xaxis.visible = True
#f.xaxis.minor_tick_in=6
f.xaxis.axis_label = "Petal Length"
f.yaxis.axis_label = "Petal Width"
f.axis.axis_label_text_color = 'Blue'
f.axis.major_label_text_color = 'Red'

"""Axis Geometry"""
f.x_range = Range1d(start=0,end=8,bounds=(0,9))
f.y_range = Range1d(start=0,end=4,bounds=(0,5))
f.xaxis.bounds = (2,5)

#Basic Plot (Scatter)
f.circle(x=flowers["petal_length"], y=flowers["petal_width"])

#Save and show
show(f)