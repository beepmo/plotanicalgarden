import dash
from dash import dcc
from dash import html
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output

from chloropleth import map_data
from filter_data import filter_df

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.title = "UBC Bot Garden"
logo_image = 'assets/UBC-logo-2018-fullsig-white-rgb72.png'

attributes = ['Species Count',
              'Genus Count',
              ]
gardens = ['All I mapped',
           'Carolinian Forest',
           # 'Contemporary Garden',
           'Winter Garden',
           'Alpine Australasia',
           'Alpine Asia',
           'Alpine South America',
           'Alpine North America',
           'Alpine Cactus and Succulent',
           'Alpine Europe'
           ]
# todo draw more gardens!

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                # html.P(children="🥑", className="header-emoji"),
                html.Img(src=logo_image, className="header-logo",
                         style={'textAlign': 'center'}),
                html.H1(
                    children="Avocado Analytics", className="header-title"
                ),
                html.P(
                    children="Analyze the behavior of avocado prices"
                             " and the number of avocados sold in the US"
                             " between 2015 and 2018\n\n\n\n",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Attribute", className="menu-title"),
                        dcc.Dropdown(
                            id="attribute-filter",
                            options=[
                                {"label": attribute, "value": attribute}
                                for attribute in attributes
                            ],
                            value="Species Count",
                            clearable=True,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children="Garden", className="menu-title"),
                        dcc.Dropdown(
                            id="beds-filter",
                            options=[
                                {"label": garden, "value": garden}
                                for garden in gardens
                            ],
                            value="All I mapped",
                            clearable=True,
                            searchable=True,
                            multi=True,
                            className="dropdown",
                        ),
                    ],
                ),
                # html.Div(
                #     children=[
                #         html.Div(
                #             children="Date Range",
                #             className="menu-title"
                #         ),
                #         dcc.DatePickerRange(
                #             id="date-range",
                #             min_date_allowed=data.Date.min().date(),
                #             max_date_allowed=data.Date.max().date(),
                #             start_date=data.Date.min().date(),
                #             end_date=data.Date.max().date(),
                #         ),
                #     ]
                # ),
            ],
            className="menu",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="chloropleth", config={"displayModeBar": True},
                    ),
                    className="card",
                ),
                # html.Div(
                #     children=dcc.Graph(
                #         id="volume-chart", config={"displayModeBar": False},
                #     ),
                #     className="card",
                # ),
            ],
            className="wrapper",
        ),
    ]
)


@app.callback(
    [
        Output("chloropleth", "figure"),
    ],
    [
        Input(component_id="attribute-filter", component_property="value"),
        Input(component_id="beds-filter", component_property="value"),

    ],
)
def plots(attribute, gardens):
    filtered_df = filter_df(gardens)
    return map_data(attribute,filtered_df)


if __name__ == "__main__":
    app.run_server(debug=True)
