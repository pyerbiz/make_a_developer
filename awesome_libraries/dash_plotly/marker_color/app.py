# import relvant libraries

import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd

import plotly.graph_objects as go
from plotly.colors import sequential
from dash.dependencies import Input, Output
import warnings

warnings.filterwarnings("ignore")

# make sample data
data = pd.DataFrame()
data["Region"] = [
    "Western Europe",
    "North America",
    "Australia and New Zealand",
    "Middle East and Northern Africa",
    "Eastern Asia",
    "North America",
    "Southern Asia",
    "Southern Asia",
    "Southern Asia",
    "Latin America and Caribbean",
]

data["Happiness Rank"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data["Dystopia Residual"] = [
    7.587,
    7.561,
    7.527,
    7.522,
    7.427,
    7.406,
    7.378,
    7.364,
    7.286,
    7.284,
]

# make a dictionary that maps column 'Region' to a color from plotly.colors.sequential

MARKER_COLOR = {
    "Western Europe": sequential.speed[8],
    "North America": sequential.Greys[6],
    "Australia and New Zealand": sequential.turbid[9],
    "Middle East and Northern Africa": sequential.solar[11],
    "Latin America and Caribbean": sequential.haline[2],
    "Southeastern Asia": sequential.Brwnyl[6],
    "Central and Eastern Europe": sequential.PuRd[7],
    "Eastern Asia": sequential.Oranges[7],
    "Sub-Saharan Africa": sequential.Oranges[3],
    "Southern Asia": sequential.Greys[3],
}


# make base graph
def generate_graph(df):
    fig1 = go.Figure()

    for region in df["Region"]:
        trace = go.Scatter(
            x=df["Happiness Rank"],
            y=df["Dystopia Residual"],
            mode="markers",
            name=region,
            marker_color=MARKER_COLOR[
                region
            ],  # pass marker color based on region
        )
        fig1.add_trace(trace)

    return fig1


# create a dict data point that can be passed as data to the graph to 'extend' it
def generate_return_value(n_interval):
    return (
        dict(
            x=[[data.loc[n_interval, "Happiness Rank"]]],
            y=[[data.loc[n_interval, "Dystopia Residual"]]],
            marker_color=[[MARKER_COLOR[data.loc[n_interval, "Region"]]]],
        ),
    )


# setup data
df = data.head(5)
fig = generate_graph(df)

# setup dash app with dcc.Interval
app = dash.Dash(__name__, update_title=None)
server = app.server
app.layout = html.Div(
    [
        dcc.Graph(id="graph", figure=fig),
        dcc.Interval(id="interval", interval=5 * 1000, n_intervals=5),
    ]
)


# setup callback which outputs next data point to 'extendData'
@app.callback(
    Output("graph", "extendData"), [Input("interval", "n_intervals")]
)
def update_data(n_intervals):
    if n_intervals:
        index = n_intervals
        value = generate_return_value(index)
        return (value[0],)
    return dash.no_update


# run app
if __name__ == "__main__":
    app.run_server(debug=True)
