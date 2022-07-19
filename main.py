import dash
from dash import dcc
from dash import html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)
app.title = "Premiere League Dashboard"
# help(dash.html.Div)

drop_down_box = html.Div(
    children=["dropdown", dcc.Dropdown()],
    style={'width': '90%',
           "position": "fixed", "left": "5%",
           'display': 'inline-block', 'height': "5%", "top": "1%",
           'z-index': '1', 'border': '2px solid green',
           'text-align': 'center'}
)

# section for the graphs 
Graphs = html.Div(
    children=[
        html.Div(children=['Graph_1',dcc.Graph()]),
        html.Div(children=['Graph_2',dcc.Graph()])
    ]
)

app.layout = html.Div()


if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
