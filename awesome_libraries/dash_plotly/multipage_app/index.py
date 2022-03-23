# import dash_core_components as dcc
# import dash_html_components as html
from dash import dcc
from dash import html

# Connect to main app.py file
from app import app

# Connect to your app pages
from apps import global_sales, vgames, vgames_demo
from dash.dependencies import Input, Output
from apps import sidebar
import pandas as pd
import pathlib

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("datasets").resolve()

dfv = pd.read_csv(DATA_PATH.joinpath("vgsales.csv"))
genre_list = dfv.Genre.unique()

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        dcc.Store(id="genre_item", storage_type="session"),
        sidebar.get_filter_sidebar(genre_list),
        html.Div(
            [
                dcc.Link("Video Games|", href="/apps/vgames"),
                dcc.Link("Other Products|", href="/apps/global_sales"),
                dcc.Link("Video Games Rank", href="/apps/vgames_demo"),
            ],
            className="row",
        ),
        html.Div(id="page-content", children=[]),
    ]
)


@app.callback(
    [Output("genre_item", "data")],
    [Input("filter-wellname-dropdown", "value")],
)
def register_genre(genre_id):
    return [genre_id]


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    """_summary_

    Args:
        pathname (_type_): _description_

    Returns:
        _type_: _description_
    """
    if pathname == "/apps/vgames":
        return vgames.layout
    if pathname == "/apps/global_sales":
        return global_sales.layout
    if pathname == "/apps/vgames_demo":
        return vgames_demo.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == "__main__":
    app.run_server(debug=True)
