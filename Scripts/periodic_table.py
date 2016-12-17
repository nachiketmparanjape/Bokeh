from bokeh.sampledata.periodic_table import elements
from bokeh.io import output_file, show
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, ColumnDataSource
from bokeh.plotting import figure

output_file("C:\Users\labuser\Documents\Python_Data_Analysis\Learning_Bokeh\Output\elements.html")

f = figure()

elements = elements.dropna()
colormap = {'gas':'yellow','liquid':'orange','solid':'red'}
elements['color'] = [colormap[x] for x in elements['standard state']]

gas = ColumnDataSource(elements[elements['standard state'] == 'gas'])
liquid = ColumnDataSource(elements[elements['standard state'] == 'liquid'])
solid = ColumnDataSource(elements[elements['standard state'] == 'solid'])

f.circle(x="atomic radius", y="boiling point",
         size=[i/10 for i in gas.data["van der Waals radius"]],
         fill_alpha=0.2,color="color",line_dash=[5,3],legend='Gas',source=gas)

f.circle(x="atomic radius", y="boiling point",
         size=[i/10 for i in liquid.data["van der Waals radius"]],
         fill_alpha=0.2,color="color",line_dash=[5,3],legend='Liquid',source=liquid)

f.circle(x="atomic radius", y="boiling point",
         size=[i/10 for i in solid.data["van der Waals radius"]],
         fill_alpha=0.2,color="color",line_dash=[5,3],legend='Solid',source=solid)

f.xaxis.axis_label="Atomic radius"
f.yaxis.axis_label="Boiling point"

#Tools
f.toolbar_location='above'
f.toolbar.logo = None

#Title
f.title.text = 'Elements'
f.title.text_font_size = "44px"
f.title.align = "center"

#Stylizing the plot area
f.plot_width=1500
f.plot_height=800
f.background_fill_color = "#CD5C5C"
f.background_fill_alpha = 0.1

show(f)