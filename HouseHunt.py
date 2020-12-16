import folium
import pandas

data=data = pandas.read_excel("ApartmentSummary.xlsx", sheet_name=0, engine='openpyxl', skiprows=[0])

lat=list(data["Latitude"])
lon=list(data["Longitude"])
name=list(data["Apartments"])
year_built=list(data["Year"])
listed_price=list(data["Listed price Current"])
strata_fees=list(data["Strata Fees/month"])
sqft=list(data["Area"])


html = """
Apartment Listed:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Year Build: %s <br />
Listed Price: %s CAD <br />
Strata Fees: %s CAD <br />
Area: %s sq.ft
"""

#"tiles = "Stamen Terrain"

map = folium.Map(location=[49.18186245, -122.834697328997], zoom_start = 11)

fg = folium.FeatureGroup(name="My Map")

for lt, ln, na, yr, lp, sf, ft in zip(lat, lon, name, year_built, listed_price, strata_fees, sqft ):
    print(ft)
    iframe = folium.IFrame(html=html %(na, na, yr, lp, sf, ft), width=200, height=130)
    fg.add_child(folium.Marker(location=(lt,ln), popup=folium.Popup(iframe), icon=folium.Icon(color='red',icon="home")))


map.add_child(fg)

map.save("Apartments.html")
