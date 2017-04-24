import folium
import pandas
df = pandas.read_csv("Volcanoes-USA.txt")
map = folium.Map(location=[45.372,-121.697],zoom_start=4,tiles='openstreetmap')
for lat,lon,name in zip(df['LAT'],df['LON'],df['NAME']):
    #map.add_child(folium.Marker(location=[45.3288,-121.6625],popup='Mt.Hood',icon=folium.Icon(color='green')))
    map.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color='red')))
map.save(outfile='test.html')
