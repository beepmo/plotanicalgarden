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
                    children="UBC Botanical Garden", className="header-title"
                ),
                html.H1(children=' '),
                html.P(
                    children='''Otherworldly terrain.
                    Here are some teasers that don't give away too much.
                    ''',
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div([
            dcc.Tabs([
                dcc.Tab(label='Throwing numbers', children=[

                ]),
                dcc.Tab(label='Spotlight', children=[

                ])
            ])
        ]),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Browse gardens", className="menu-title"),
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
            ],
            className="menu",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[

                        dcc.Dropdown(
                            id="attribute-filter",
                            options=[
                                {"label": attribute, "value": attribute}
                                for attribute in attributes
                            ],
                            value="Species Count",
                            className="dropdown",
                        ),

                        dcc.Graph(
                            id="chloropleth", config={"displayModeBar": True},
                        ),
                    ],
                    className="card",
                ),

            ],
            className="wrapper",
        ),
        html.Div(
            children=[
                html.P(children="🥑", className="header-emoji"),
                html.H1(
                    id="big number", className="header-title"
                ),
                html.H1(children=' '),
                html.P(
                    children='''\n\n\n SPECIES  ||  GENUS \n\n
                    ''',
                    className="header-description",
                ),
            ],
            className="header",
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
    filtered_df = filter_cache(gardens)
    return map_data(attribute, filtered_df)


df_cache = {}


def filter_cache(gardens):
    filtered = df_cache.get(tuple(gardens))
    if filtered is None:
        filtered = filter_df(gardens)
        df_cache.update({tuple(gardens): filtered})
    return filtered


@app.callback(
    [
        Output("big number", "children")
    ],
    [
        Input(component_id="beds-filter", component_property="value"),
    ]
)
def big_number(gardens):
    filtered_df = filter_cache(gardens)
    species_cnt = filtered_df['Species Count'].sum()
    genus_cnt = filtered_df['Genus Count'].sum()
    return [str(species_cnt) + ' |-------| ' + str(genus_cnt)]


if __name__ == "__main__":
    app.run_server(debug=True)
