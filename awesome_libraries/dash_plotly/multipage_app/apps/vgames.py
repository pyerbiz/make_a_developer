import pathlib

# import dash_core_components as dcc
# import dash_html_components as html
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
from app import app
from dash.dependencies import Input, Output, State

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
        html.H1("Video Games Sales", style={"textAlign": "center"}),
        html.Div(
            [
                html.Div(
                    dcc.Dropdown(
                        id="genre-dropdown",
                        value="Strategy",
                        clearable=False,
                        options=[
                            {"label": x, "value": x}
                            for x in sorted(dfv.Genre.unique())
                        ],
                    ),
                    className="six columns",
                ),
                html.Div(
                    dcc.Dropdown(
                        id="sales-dropdown",
                        value="EU Sales",
                        clearable=False,
                        persistence=True,
                        persistence_type="memory",
                        options=[{"label": x, "value": x} for x in sales_list],
                    ),
                    className="six columns",
                ),
                html.Div(
                    dcc.Dropdown(
                        id="publisher-dropdown",
                        value=dfv.Publisher.unique()[:10][0],
                        clearable=False,
                        persistence=True,
                        persistence_type="memory",
                        options=[
                            {"label": x, "value": x}
                            for x in dfv.Publisher.unique()[:10]
                        ],
                    ),
                    className="six columns",
                ),
            ],
            className="row",
        ),
        dcc.Graph(id="my-bar", figure={}),
    ]
)


@app.callback(
    Output(component_id="my-bar", component_property="figure"),
    [
        Input(component_id="genre-dropdown", component_property="value"),
        Input(component_id="sales-dropdown", component_property="value"),
        Input(component_id="publisher-dropdown", component_property="value"),
        Input("genre_item", "modified_timestamp"),
    ],
    [State("genre_item", "data")],
)
def display_value(
    genre_chosen, sales_chosen, publisher_item, modified_timestamp, genre_item
):

    """makes figure based on inputs

    Args:
    genre_chosen (_type_): _description_
    sales_chosen (_type_): _description_

    Returns:
        plotly_fig: _description_
    """

    # dfv_fltrd = dfv[dfv["Genre"] == genre_chosen]
    # dfv_fltrd = dfv.nlargest(10, sales_chosen)

    print(f"modified_timestamp:{modified_timestamp}")
    print(genre_item)
    dfv_fltrd = dfv[dfv["Genre"] == genre_item]
    dfv_fltrd = dfv_fltrd[dfv_fltrd["Publisher"] == publisher_item]
    print(dfv_fltrd.shape)
    fig = px.bar(dfv_fltrd, x="Video Game", y=sales_chosen, color="Platform")
    fig = fig.update_yaxes(tickprefix="$", ticksuffix="M")
    return fig
