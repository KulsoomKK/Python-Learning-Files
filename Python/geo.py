from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="kulsoom")
location = geolocator.geocode("97 Wythe Ave Brooklyn")
print(location.address)

print((location.latitude, location.longitude))

lat = location.latitude
