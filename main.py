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


data = pd.read_csv("Data.csv")


def get_team_runs(player):
    global data
    bat_df = data.groupby(['Club'])["batsman_runs"].sum().reset_index().copy()
    bat_df = bat_df[bat_df["batsman"]==player]
    bat_df = bat_df[bat_df["batsman_runs"]>0]

    fig = px.bar(bat_df, x="bowling_team", y="batsman_runs", color="batsman_runs",
             labels={'bowling_team':'Teams', 'batsman_runs':'Runs Scored'}, height=400, width = 500,
                title="Runs Scored by " + player + " against all teams", template='plotly_dark')
    fig.update_layout({'paper_bgcolor': '#282828', 'plot_bgcolor':'#282828'})
    return fig

drop_down_box = html.Div(
    children=["dropdown", dcc.Dropdown()],
    style={'width': '90%',
           "position": "fixed", "left": "5%",
           'display': 'inline-block', 'height': "5%", "top": "1%",
           'z-index': '1', 'border': '2px solid green',
           'text-align': 'center'}
)

main_div_style = {"background-color": "#181818", 
                    "padding":"0", 
                    "width":"100%", 
                    "height":"100", 
                    "position": "fixed",
                    "top": "0%",
                    "left": "0",
                    "bottom": "0",
                }

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
