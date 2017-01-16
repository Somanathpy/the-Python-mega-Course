import folium 
import pandas as pd

df = pd.read_csv("Volcanoes-USA.txt")

map = folium.Map(location=[45.372,-121.697],zoom_start=4,tiles='Stamen Terrain')

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
	map.simple_marker(location=[lat,lon],popup=name,marker_color='green' if elev in range(0,1000) else 'orange' if elev in range(1000,2000)else 'red')
	map.save('Volcanos_USA1.html')