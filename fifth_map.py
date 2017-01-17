import folium 
import pandas as pd

df = pd.read_csv("Volcanoes-USA.txt")

map = folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=4,tiles='Stamen Terrain')

def color(elev):
	minimum = int( min(df['ELEV']))
	step = int((max(df['ELEV'])-minimum)/3)
	if elev in range(minimum,minimum+step):
		col = 'green'
	elif elev in range(minimum+step,minimum+step*2):
		col = 'orange'
	else:
		col = 'red'
	return col

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
	map.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color=color(elev))))
map.save(outfile='Volcanos_USA3.html')