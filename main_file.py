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

allLib = folium.FeatureGroup(name = "Libraries")

for xVal, yVal, name in zip(xVals, yVals, libNames):
    allLib.add_child(folium.CircleMarker(location = [yVal, xVal],
    radius = 6, popup = name, fill_color = "green", fill_opacity = 1,
    color = None))

# Add parks as points

allParks = folium.FeatureGroup(name = "Parks")

allParks.add_child(folium.GeoJson(data = open("Parks.geojson.json",
"r", encoding = "utf-8-sig").read(),
style_function = lambda x: {"fillColor":"purple"} ))

# Add neighborhood

neigh = folium.FeatureGroup(name = "Neighborhood")

neigh.add_child(folium.GeoJson(data = open("Neighborhood_Associations.geojson.json",
"r", encoding = "utf-8-sig").read(),
style_function = lambda x: {"fillColor":"yellow"} ))

# Add Incident Report

incidentReports = pandas.read_csv("IncidentReprt.csv")

xVals = list(incidentReports["Longitude"])
yVals = list(incidentReports["Latitude"])

incidents = folium.FeatureGroup(name = "Incident Reports in 2018")

for xVal, yVal in zip(xVals, yVals):
    incidents.add_child(folium.CircleMarker(location = [yVal, xVal],
    radius = 6, fill_color = "red", fill_opacity = 1,
    color = None))

# Adding highschools
highschool = pandas.read_csv("Madison Highschool.csv")

xVals = list(highschool["Longitude"])
yVals = list(highschool["Latitude"])

madHigh = folium.FeatureGroup(name = "High Schools")

for xVal, yVal in zip(xVals, yVals):
    madHigh.add_child(folium.CircleMarker(location = [yVal, xVal],
    radius = 6, popup = None, fill_color = "blue", fill_opacity = 1,
    color = None))

# Adding all map features
baseMap.add_child(allLib)
baseMap.add_child(allParks)
baseMap.add_child(neigh)
baseMap.add_child(incidents)
baseMap.add_child(madHigh)

baseMap.add_child(folium.LayerControl())

baseMap.save("Map1.html")