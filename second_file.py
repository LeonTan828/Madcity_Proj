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

# Add 2016 Weapon Violation location
weap2016 = pandas.read_csv("WeaponVio2016.csv")

xVals = list(weap2016["Longitude"])
yVals = list(weap2016["Latitude"])

weapVio2016 = folium.FeatureGroup(name = "Weapon Violation in 2016")

for xVal, yVal in zip(xVals, yVals):
    weapVio2016.add_child(folium.CircleMarker(location = [yVal, xVal],
    radius = 6, fill_color = "green", fill_opacity = 1,
    color = None))

# Add 2015 Weapon Violation location
weap2015 = pandas.read_csv("WeaponVio2015.csv")

xVals = list(weap2015["Longitude"])
yVals = list(weap2015["Latitude"])

weapVio2015 = folium.FeatureGroup(name = "Weapon Violation in 2015")

for xVal, yVal in zip(xVals, yVals):
    weapVio2015.add_child(folium.CircleMarker(location = [yVal, xVal],
    radius = 6, fill_color = "purple", fill_opacity = 1,
    color = None))

# Add 2014 Weapon Violation location
weap2014 = pandas.read_csv("WeaponVio2014.csv")

xVals = list(weap2014["Longitude"])
yVals = list(weap2014["Latitude"])

weapVio2014 = folium.FeatureGroup(name = "Weapon Violation in 2014")

for xVal, yVal in zip(xVals, yVals):
    weapVio2014.add_child(folium.CircleMarker(location = [yVal, xVal],
    radius = 6, fill_color = "yellow", fill_opacity = 1,
    color = None))

# Add 2013 Weapon Violation location
weap2013 = pandas.read_csv("WeaponVio2013.csv")

xVals = list(weap2013["Longitude"])
yVals = list(weap2013["Latitude"])

weapVio2013 = folium.FeatureGroup(name = "Weapon Violation in 2013")

for xVal, yVal in zip(xVals, yVals):
    weapVio2013.add_child(folium.CircleMarker(location = [yVal, xVal],
    radius = 6, fill_color = "black", fill_opacity = 1,
    color = None))

# Add 2012 Weapon Violation location
weap2012 = pandas.read_csv("WeaponVio2012.csv")

xVals = list(weap2012["Longitude"])
yVals = list(weap2012["Latitude"])

weapVio2012 = folium.FeatureGroup(name = "Weapon Violation in 2012")

for xVal, yVal in zip(xVals, yVals):
    weapVio2012.add_child(folium.CircleMarker(location = [yVal, xVal],
    radius = 6, fill_color = "pink", fill_opacity = 1,
    color = None))

# Add 2011 Weapon Violation location
weap2011 = pandas.read_csv("WeaponVio2011.csv")

xVals = list(weap2011["Longitude"])
yVals = list(weap2011["Latitude"])

weapVio2011 = folium.FeatureGroup(name = "Weapon Violation in 2011")

for xVal, yVal in zip(xVals, yVals):
    weapVio2011.add_child(folium.CircleMarker(location = [yVal, xVal],
    radius = 6, fill_color = "gold", fill_opacity = 1,
    color = None))

# Add 2010 Weapon Violation location
weap2010 = pandas.read_csv("WeaponVio2010.csv")

xVals = list(weap2010["Longitude"])
yVals = list(weap2010["Latitude"])

weapVio2010 = folium.FeatureGroup(name = "Weapon Violation in 2010")

for xVal, yVal in zip(xVals, yVals):
    weapVio2010.add_child(folium.CircleMarker(location = [yVal, xVal],
    radius = 6, fill_color = "silver", fill_opacity = 1,
    color = None))

# Add 2009 Weapon Violation location
weap2009 = pandas.read_csv("WeaponVio2009.csv")

xVals = list(weap2009["Longitude"])
yVals = list(weap2009["Latitude"])

weapVio2009 = folium.FeatureGroup(name = "Weapon Violation in 2009")

for xVal, yVal in zip(xVals, yVals):
    weapVio2009.add_child(folium.CircleMarker(location = [yVal, xVal],
    radius = 6, fill_color = "orange", fill_opacity = 1,
    color = None))

# Add 2008 Weapon Violation location
weap2008 = pandas.read_csv("WeaponVio2008.csv")

xVals = list(weap2008["Longitude"])
yVals = list(weap2008["Latitude"])

weapVio2008 = folium.FeatureGroup(name = "Weapon Violation in 2008")

for xVal, yVal in zip(xVals, yVals):
    weapVio2008.add_child(folium.CircleMarker(location = [yVal, xVal],
    radius = 6, fill_color = "white", fill_opacity = 1,
    color = None))


# Adding all map features
baseMap.add_child(weapVio2018)
baseMap.add_child(weapVio2017)
baseMap.add_child(weapVio2016)
baseMap.add_child(weapVio2015)
baseMap.add_child(weapVio2014)
baseMap.add_child(weapVio2013)
baseMap.add_child(weapVio2012)
baseMap.add_child(weapVio2011)
baseMap.add_child(weapVio2010)
baseMap.add_child(weapVio2009)
baseMap.add_child(weapVio2008)

baseMap.add_child(folium.LayerControl())

baseMap.save("Map2.html")