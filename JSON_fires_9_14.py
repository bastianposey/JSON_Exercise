import json


infile = open('US_fires_9_14.json','r')

eqdata = json.load(infile)


lons = []
lats = []
fires = []
for eq in eqdata:
    if eq["brightness"] > 450:
        lat = eq["latitude"]
        lats.append(lat)

        lon = eq["longitude"]
        lons.append(lon)

        fire= eq["brightness"]
        fires.append(fire)


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': fires,
    'marker': {
        'color': fires,
        'size': 10,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title':'Magnitude'}
    }
}]

my_layout = Layout(title="US fires, sept 14-20")

fig = {'data':data,"layout":my_layout}

offline.plot(fig, filename='USfires_9_14.html')
