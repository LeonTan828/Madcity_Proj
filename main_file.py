# this is the main file
# https://99percentinvisible.org/episode/palaces-for-the-people/

import folium
import pandas

# Set Madison as base map
baseMap = folium.Map(location=[43.071906, -89.396824], \
    zoom_start = 12, tiles = "Stamen Toner")


# Add libraries as points
lib_data = pandas.read_csv("Libraries.csv")

xVals = list(lib_data["X"])
yVals = list(lib_data["Y"])
libNames = list(lib_data["LONG_NAME"])

features = folium.FeatureGroup(name= "Social Infrastructures")

for xVal, yVal, name in zip(xVals, yVals, libNames):
    features.add_child(folium.CircleMarker(location = [yVal, xVal], \
        radius = 6, popup = name, fill_color = "red", fill_opacity = 1, \
        color = None))

baseMap.add_child(features)

# Add parks as points

features.add_child(folium.GeoJson(data = open("Parks.geojson.json", \
    "r", encoding = "utf-8-sig").read() ))

baseMap.save("Map1.html")