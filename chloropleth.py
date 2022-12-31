import plotly.express as px

import json

with open('map.geojson') as raw_map:
    marauders = json.load(raw_map)

from parse_data import df


# REQUIRES: attribute is 'Species Count' or 'Genus count'
def map_data(attribute):
    fig = px.choropleth(
        # pandas dataframe
        df,

        # specify column for regions
        locations='Bed',

        # specify column for color intensity
        color=attribute,

        # loaded geojson
        geojson=marauders,

        # featureidkey = 'properties.<location column in csv, which should be same as property key in geojson>'
        featureidkey='properties.bed',
    )

    # if fitbounds is not set, the entire globe is shown
    fig.update_geos(fitbounds="geojson", visible=True)

    return [fig]
    # return type <list> because callback expects list
