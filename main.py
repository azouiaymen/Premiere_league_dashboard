import dash
from dash import dcc
from dash import html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)
server = app.server # line for heroku for afterwards
app.title = "Premiere League Dashboard 20/21"
# help(dash.html.Div)


df = pd.read_csv("EPL_20_21.csv")

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
        html.Div(children=['Graph_1', dcc.Graph()],
                 style={'width': '45%', "position": "fixed", "left": "2%",
                 'display': 'inline-block', 'text-align': 'center',
                        'top': '10%', 'border': '2px solid red', 'height': '50%'}),
        html.Div(children=['Graph_2', dcc.Graph()],
                 style={'width': '45%', 'position': 'fixed', 'left': '53%',
                 'display': 'inline-block', 'text-align': 'center',
                        'top': '10%', 'border': '3px solid red', 'height': '50%'})
    ]
)

app.layout = html.Div(id='main_div', children=[drop_down_box, Graphs],
                      style={'background-color': '#FFFFFF', 'padding': '0',
                             'width': '100%', 'height': '100%', 'position': 'fixed',
                             'top': '0%', 'left': '0%', 'bottom': '0%', 'height': '100%',
                             'border': '2px solid blue'}
                      )


if __name__ == '__main__':
    app.run_server(debug=False, port=8080)
