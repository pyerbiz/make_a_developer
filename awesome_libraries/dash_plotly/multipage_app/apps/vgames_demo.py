import pathlib

# import dash_core_components as dcc
# import dash_html_components as html
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
from app import app
from dash.dependencies import Input, Output

# from pb_list import publisher_list
# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

dfv = pd.read_csv(DATA_PATH.joinpath("vgsales.csv"))  # GregorySmith Kaggle

sales_list = [
    "North American Sales",
    "EU Sales",
    "Japan Sales",
    "Other Sales",
    "World Sales",
]


layout = html.Div(
    [
        html.H1("Video Games Rank", style={"textAlign": "center"}),
        html.Div(
            [
                html.Div(
                    dcc.Dropdown(
                        id="genre-dropdown-rank",
                        value="Strategy",
                        clearable=False,
                        options=[
                            {"label": x, "value": x}
                            for x in sorted(dfv.Genre.unique())
                        ],
                    ),
                    className="six columns-rank",
                ),
                html.Div(
                    dcc.Dropdown(
                        id="sales-dropdown-rank",
                        value="EU Sales",
                        clearable=False,
                        persistence=True,
                        persistence_type="memory",
                        options=[{"label": x, "value": x} for x in sales_list],
                    ),
                    className="six columns-rank",
                ),
                html.Div(
                    dcc.Dropdown(
                        id="publisher-dropdown-rank",
                        value=dfv.Publisher.unique()[:10][0],
                        clearable=False,
                        persistence=True,
                        persistence_type="memory",
                        options=[
                            {"label": x, "value": x}
                            for x in dfv.Publisher.unique()[:10]
                        ],
                    ),
                    className="six columns-rank",
                ),
            ],
            className="row-rank",
        ),
        dcc.Graph(id="my-bar-rank", figure={}),
    ]
)


@app.callback(
    Output(component_id="my-bar-rank", component_property="figure"),
    [
        Input(component_id="genre-dropdown-rank", component_property="value"),
        Input(component_id="sales-dropdown-rank", component_property="value"),
        Input(
            component_id="publisher-dropdown-rank", component_property="value"
        ),
        Input("genre_item", "data"),
    ],
)
def display_value(genre_chosen, sales_chosen, publisher_item, genre_item):

    """makes figure based on inputs

    Args:
    genre_chosen (_type_): _description_
    sales_chosen (_type_): _description_

    Returns:
        plotly_fig: _description_
    """

    # dfv_fltrd = dfv[dfv["Genre"] == genre_chosen]
    # dfv_fltrd = dfv.nlargest(10, sales_chosen)
    print(genre_item)
    print(dfv.shape)
    dfv_fltrd = dfv[dfv["Genre"] == genre_item]
    print(dfv.shape)
    dfv_fltrd = dfv_fltrd[dfv_fltrd["Publisher"] == publisher_item]
    print(dfv_fltrd.shape)
    fig = px.bar(dfv_fltrd, x="Platform", y=sales_chosen)
    fig = fig.update_yaxes(tickprefix="$", ticksuffix="M")
    return fig
