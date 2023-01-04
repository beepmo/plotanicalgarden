## Inspiration
`beep` is a ghost of UBC's Botanical Garden and, spending as much time as possible there, wants to join the ranks of garden cartographer.

## What it does
Chloropleth map shows biodiversity.

## How we built it
Maps were made in three hours of tracing satellite imagery on [geojson.io](geojson.io); more will be drawn later. Species data can be obtained from the official [Garden Explorer](https://collections.botanicalgarden.ubc.ca/default.aspx) and I also have accurate bed names provided by the garden.

## Challenges we ran into
It is around 11pm and deployment on render is not working. Builder bot insists that `numpy~=1.23.4` could not be found but deployment on render with `numpy~=1.23.4` has succeeded before.

## Accomplishments that we're proud of
The map drawing. The feeling of getting features done faster and faster.

## What we learned
Surely 'chloropleth' is spelled with the prefix 'chloro'? 🌿
> Choropleth. Etymology. From Ancient Greek χώρα (khṓra, “location”) + πλῆθος (plêthos, “a great number”)

No matter, I will change it if I can. I learned beginner data wrangling `pandas`, gained appreciation for `plotly` and `geojson`, and practiced `dash` web app development.

## What's next for plotanical garden
Chloropleth animations through past and future.
Get hosting to sink into that sweet sweet domain name: [plotanicalgarden.tech](plotanicalgarden.tech).
Calculate areas and densities, plan routes, document secret gates for Marauder's map.

That would require user authentication.
And planting GPS trackers on garden mobile vehicles.