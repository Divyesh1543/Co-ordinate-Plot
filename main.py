import phonenumbers
import opencage
import folium
from number import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_provider= phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from  opencage.geocoder import OpenCageGeocode

key='d956ce84569044cca98ad9e7bed9745c'

geocoder=OpenCageGeocode(key)
query=str(location)
result=geocoder.geocode(query)

lat=result[0]["geometry"]["lat"]
lng=result[0]["geometry"]["lng"]
print(lat, lng)

myMap=folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save("location.html")
