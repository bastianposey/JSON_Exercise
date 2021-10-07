import json


infile = open('US_fires_9_1.json','r')

eqdata = json.load(infile)


lons = []
lats =[]
fires = []
for eq in eqdata:
    if eq["brightness"] > 450:
        lat = eq["latitude"]
        lats.append(lat)

        lon = eq["longitude"]
        lons.append(lon)

        fire= eq["brightness"]
        fires.append(fire)




print(lons[:15])
print(lats[:15])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': fires,
    'marker': {
        'size': 10,
        'color': fires,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title':'Magnitude'}
    }
}]

my_layout = Layout(title="US fires, sept 1-13")

fig = {'data':data,"layout":my_layout}


offline.plot(fig, filename='USfires_9_1.html')
