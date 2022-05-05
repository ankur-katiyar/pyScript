import json
import pyodide
from js import Bokeh, console, JSON
from bokeh.embed import json_item
from bokeh.plotting import figure
from bokeh.resources import CDN

fruits = ["Apples", "Pears", "Nectarines", "Plums", "Grapes", "Strawberries"]
counts = [5, 3, 4, 2, 4, 6]
p = figure(
    x_range=fruits, height=350, title="Fruit Counts", toolbar_location=None, tools=""
)
p.vbar(x=fruits, top=counts, width=0.9)
p.xgrid.grid_line_color = None
p.y_range.start = 0
p_json = json.dumps(json_item(p, "chart"))
Bokeh.embed.embed_item(JSON.parse(p_json))
