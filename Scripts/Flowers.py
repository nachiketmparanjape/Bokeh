from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool

#Naming the output html and defining the path
output_file("C:\Users\labuser\Documents\Python_Data_Analysis\Learning_Bokeh\Output\iris.html")

#Defining the object
f=figure()

"""Tools"""
#f.tools=[PanTool(),ResetTool()]
#dir(bokeh.models.tools)
#f.add_tools(HoverTool())
f.toolbar_location='above'
f.toolbar.logo = None

#Create a specific Hover Tool
#Tip - Can't use pandas with Hover, or most of the interactive features. We need to use 
hover= HoverTool(tooltips=[("Species","@species"),("Sepal Width","@sepal_width")])

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
#f.xaxis.bounds = (2,5)

"""Grid"""
#f.grid

"""Glyphs - glyphs make additions to the plot.

What we will do -   1. Change the size of the dots according to the septal_width
                    2. Change the color of the dots according to species
"""
#Color for species (ColorCode)
#colormap = {'setosa':'red','versicolor':'green','virginica':'blue'}
#flowers['color'] = [colormap[x] for x in flowers['species']]


#Basic Plot (Scatter)
# We are plotting every species separately to be able to add legend to each of them
#In that case, we do not have to do the colormap dictionary!

#setosa
f.circle(x=flowers["petal_length"][flowers['species'] == 'setosa'], y=flowers["petal_width"][flowers['species'] == 'setosa'],
         size=flowers['sepal_width']*4,fill_alpha=0.2,color='red',line_dash=(5,3),legend='setosa')

#versicolor
f.circle(x=flowers["petal_length"][flowers['species'] == 'versicolor'], y=flowers["petal_width"][flowers['species'] == 'versicolor'],
         size=flowers['sepal_width']*4,fill_alpha=0.2,color='green',line_dash=(5,3),legend='versicolor')

#versicolor
f.circle(x=flowers["petal_length"][flowers['species'] == 'virginica'], y=flowers["petal_width"][flowers['species'] == 'virginica'],
         size=flowers['sepal_width']*4,fill_alpha=0.2,color='blue',line_dash=(5,3),legend='virginica')

#Style the legend
f.legend.location = 'top_left' #or exact location (555,20)
f.legend.background_fill_alpha = 0.1
f.legend.border_line_color = None
f.legend.label_text_font_size = '20px'
f.legend.name = 'Species'


#Save and show
show(f)