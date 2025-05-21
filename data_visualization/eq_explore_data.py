import json
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go

path = Path('earthquake_data/30_days_eq_data.geojson')

content = path.read_text()

all_eq_data = json.loads(content)

"""path = Path('earthquake_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)"""

all_eq_dicts = all_eq_data['features']

mags_list, lons, lats = [], [], []
for eq_dict in  all_eq_dicts:
	mag = eq_dict['properties']['mag']
	lon = eq_dict['geometry']['coordinates'][0]
	lat = eq_dict['geometry']['coordinates'][1]
	mags_list.append(mag)
	lons.append(lon)
	lats.append(lat)

title = 'Global Earthquakes Report'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags_list ,title=title,
		color=mags_list, color_continuous_scale='Viridis', labels={'color': 'Magnitude'},
		projection='natural earth')

fig.update_layout(
	geo=dict(
		projection=dict(
			rotation=dict(lon=0, lat=0)
		)
	)
)
frames = []
for angle in range(0, 360, 2):
	frame = go.Frame(layout=dict(
		geo=dict(
			projection=dict(
				rotation=dict(lon=angle)
			)
		)
	))
	frames.append(frame)

fig.frames = frames

fig.update_layout(
    updatemenus=[{
        'type': 'buttons',
        'buttons': [
            {
                'label': 'Play',
                'method': 'animate',
                'args': [None, {
                    'frame': {'duration': 50, 'redraw': True},
                    'fromcurrent': True,
                    'transition': {'duration': 0}
                }]
            },
            {
                'label': 'Pause',
                'method': 'animate',
                'args': [
                    [None],
                    {
                        'frame': {'duration': 0, 'redraw': True},
                        'mode': 'immediate',
                        'transition': {'duration': 0}
                    }
                ]
            }
        ],
        'direction': 'left',
        'pad': {'r': 10, 't': 87},
        'showactive': False,
        'x': 0.1,
        'xanchor': 'right',
        'y': 0,
        'yanchor': 'top'
    }]
)

fig.show()
