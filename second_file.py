# this is the second file
# Showing location of weapon violation in Madison

import folium
import pandas

# Set Madison as base map
baseMap = folium.Map(location=[43.071906, -89.396824],
zoom_start = 12, tiles = "OpenStreetMap")


# Add 2018 Weapon Violation location
weap2018 = pandas.read_csv("WeaponVio2018.csv")

xVals = list(weap2018["Longitude"])
yVals = list(weap2018["Latitude"])

weapVio2018 = folium.FeatureGroup(name = "Weapon Violation in 2018")

for xVal, yVal in zip(xVals, yVals):
    weapVio2018.add_child(folium.CircleMarker(location = [yVal, xVal],
    radius = 6, fill_color = "red", fill_opacity = 1,
    color = None))


# Add 2017 Weapon Violation location
weap2017 = pandas.read_csv("WeaponVio2017.csv")

xVals = list(weap2017["Longitude"])
yVals = list(weap2017["Latitude"])

weapVio2017 = folium.FeatureGroup(name = "Weapon Violation in 2017")

for xVal, yVal in zip(xVals, yVals):
    weapVio2017.add_child(folium.CircleMarker(location = [yVal, xVal],
    radius = 6, fill_color = "blue", fill_opacity = 1,
    color = None))


# Adding all map features
baseMap.add_child(weapVio2018)
baseMap.add_child(weapVio2017)

baseMap.add_child(folium.LayerControl())

baseMap.save("Map2.html")