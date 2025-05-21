import json
from pathlib import Path
import plotly.express as px

path = Path('earthquake_data/30_days_eq_data.geojson')

content = path.read_text()

all_eq_data = json.loads(content)

all_eq_dicts = all_eq_data['features']

mags_list, lons, lats, eq_titles = [], [], [], []
for eq_dict in  all_eq_dicts:
	mag = eq_dict['properties']['mag']
	lon = eq_dict['geometry']['coordinates'][0]
	lat = eq_dict['geometry']['coordinates'][1]
	eq_title = eq_dict['properties']['title']
	mags_list.append(mag)
	lons.append(lon)
	lats.append(lat)
	eq_titles.append(eq_title)

title = 'Global Earthquakes Report'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags_list ,title=title,
		color=mags_list, color_continuous_scale='Viridis', labels={'color': 'Magnitude'},
		projection='natural earth', hover_name=eq_titles)

#The config name when you put you mouse over a point is called HOVER

fig.show()
