import plotly.express as px

import json

with open('map.geojson') as raw_map:
    marauders = json.load(raw_map)


# REQUIRES: attribute is 'Species Count' or 'Genus count'
def map_data(attribute,filtered_df):
    fig = px.choropleth(
        # pandas dataframe
        filtered_df,

        # specify column for regions
        locations='Bed',

        # specify column for color intensity
        color=attribute,

        # loaded geojson
        geojson=marauders,

        # featureidkey = 'properties.<location column in csv, which should be same as property key in geojson>'
        featureidkey='properties.bed',

        hover_data=['Species Count', 'Genus Count'],
        hover_name='Bed',
    )

    # if fitbounds is not set, the entire globe is shown
    fig.update_geos(fitbounds="geojson", visible=True)

    # smooth transition when updated
    fig.update_layout(transition_duration=500)

    # pretty hover
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="white",
            font_size=16,
            font_family="Rockwell"
        )
    )

    return [fig]
    # return type <list> because callback expects list
