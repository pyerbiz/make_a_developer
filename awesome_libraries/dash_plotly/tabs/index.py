from dash import html, dbc, dcc, Input, Output
import plotly.express as px
import pandas as pd
from app import app


app.layout = html.Div(
    [
        dcc.Store(id="CENTRAL_SUBJECT_WELL_REGISTRY", storage_type="session"),
        html.Div(
            [
                dbc.Row(
                    id="header-id",
                    children=[
                        dcc.Location(id="url", refresh=False),
                    ],
                    className="header zero-margin-dbc-row",
                ),
               # page content
                dbc.Row(
                    id="page-content",
                    className="zero-margin-dbc-row",
                ),
            ],
            style={"height": "100vh"},
        ),
    ],
    id="full-page",
)