from dash import dcc
from dash import html
from copy import deepcopy

STANDARD_DROPDOWN_CONFIG = {
    "searchable": True,
    "className": "dropdown-dark",
    "persistence": True,
}


def get_updated_config(
    std_config,
    extra_config,
) -> dict:
    # return the updated config that concat
    #   inputs from std_config and extra_config
    #   and overwrite values of key in std_config that
    #   also appears in extra_config
    if std_config is not None:
        # assert isinstance(std_config, dict)
        std_config = deepcopy(std_config)
    else:
        std_config = {}
    if extra_config is not None:
        # assert isinstance(extra_config, dict)
        extra_config = deepcopy(extra_config)
    else:
        extra_config = {}

    try:
        std_config.update(extra_config)
    except TypeError:
        print(
            f"Cannot update std_config ({std_config} with "
            f"extra_config ({extra_config})."
        )

    return std_config


def get_filter_sidebar(genre_list):

    return html.Div(
        id="filter-sidebar",
        children=[
            html.Div(
                id="filter-sidebar-dismiss",
                children=[html.I(className="fas fa-arrow-left")],
            ),
            html.Div(
                [
                    html.Label("Genre: "),
                    dcc.Dropdown(
                        **get_updated_config(
                            std_config=STANDARD_DROPDOWN_CONFIG,
                            extra_config={
                                "id": "filter-wellname-dropdown",
                                "options": genre_list,
                                "value": "",
                            },
                        ),
                    ),
                    html.Br(),
                ]
            ),
        ],
        className="bg-dark",
    )
