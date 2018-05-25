from geopy.geocoders import Nominatim

def get_cordinates(country_str):
    geolocator = Nominatim()
    location = geolocator.geocode(country_str)

    return (location.latitude , location.longitude)

