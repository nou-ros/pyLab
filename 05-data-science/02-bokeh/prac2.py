from bokeh.plotting import figure, output_file, show, ColumnDataSource, save
import pandas

#for color
from bokeh.transform import factor_cmap
from bokeh.palettes import Reds8

from bokeh.models.tools import HoverTool


from bokeh.embed import components

# read in csv
df = pandas.read_csv('anime.csv')

#before source
# car = df['Car']
# hp = df['Horsepower']

# create column datasource from data frame
source = ColumnDataSource(df)

# car list 
anime_list = source.data['Anime'].tolist()

output_file('prac2.html')

# Add plot
p = figure( 
    # before source
    # y_range = car,

    # after using source 
    # y_range = car_list,

    y_range = anime_list,
    plot_width = 800,
    plot_height = 600,
    title = 'Anime with most episodes',
    x_axis_label = 'Episode',
    tools ="pan, box_select, zoom_in, zoom_out, save, reset",
    )

# adding glyph 
p.hbar(
        #before source
        # y = car,
        # right = hp,
            
        # after source
        # y ='Car',
        # right = 'Horsepower',

        y='Anime',
        right = 'Episode',
        left = 0,
        height = 0.3,
        # color = 'blue',
        fill_color = factor_cmap(
            'Anime',
            palette = Reds8,
            factors = anime_list
        ),
        fill_alpha = 0.9,

        source = source,
        legend_field = 'Anime'
    )

# # add legend 
p.legend.orientation = 'vertical'
p.legend.location = 'top_right'
p.legend.label_text_font_size = '10px'

# add tooltips
hover = HoverTool()
hover.tooltips = """
    <div>
        <h3>@Anime</h3>
        <div><strong>Episodes: </strong>@Episode</div>
        <div><strong>Manga Volume: </strong>@Manga</div>
        <div><img src="@Image" alt="" width="200" /></div>
    </div>
"""

p.add_tools(hover)

# Show the result
show(p)

# # save file
# save(p)

#print out div and script for other files
script, div = components(p)