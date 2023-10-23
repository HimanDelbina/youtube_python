import phonenumbers
from phonenumbers import geocoder
import folium


key = "4c00c11d335d49e2a16263ad14834217"
number = "+989183739816"
pepnumber = phonenumbers.parse(number,None)
location = geocoder.description_for_number(pepnumber,"en")
print(location)

from phonenumbers import carrier
service_info = phonenumbers.parse(number,None)
operator = carrier.name_for_valid_number(service_info,"en")
print(operator)

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)

query = str(location)
result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat,lng)

map_location = folium.Map(location = [lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=location).add_to(map_location)
map_location.save("mylocation.html")
