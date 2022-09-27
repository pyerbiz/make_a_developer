import pandas as pd
import plotly.express as px
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from plotly.colors import sequential

CATEGORY_COLOR = {
    "APPLES": sequential.speed[8],
    "ORANGES": sequential.speed[5],
    "GRAPES": sequential.Greys[6],
    "KIWI": sequential.turbid[9],
    "PAPAYA": sequential.solar[11],
}

datafile = r"C:\Users\saral\OneDrive\Desktop\training\projects\data\sample.csv"
data = pd.read_csv(datafile, usecols=["DATE", "Yvalue", "Category"])
data0 = data.head(5)


figure = px.scatter(
    data0,
    x="DATE",
    y="Yvalue",
    color="Category",
)


app = dash.Dash(__name__)  # remove "Updating..." from title
app.layout = html.Div(
    [
        dcc.Graph(id="graph", figure=figure),
        dcc.Interval(id="interval", interval=1 * 1000, n_intervals=6),
    ]
)


@app.callback(
    Output("graph", "extendData"), [Input("interval", "n_intervals")]
)
def update_data(n_intervals):
    print(n_intervals)

    x = data["DATE"][n_intervals]
    y = data["Yvalue"][n_intervals]
    category = data["Category"][n_intervals]
    color = CATEGORY_COLOR[category]

    return {
        "x": [[x]],
        "y": [[y]],
        "marker": [[color]],
    }, [0]


if __name__ == "__main__":
    app.run_server(debug=True)
