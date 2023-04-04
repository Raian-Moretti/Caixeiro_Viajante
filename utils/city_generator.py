from geopy.geocoders import Nominatim
from random import randint

def city_generator():
    geolocator = Nominatim(user_agent="my_app")
    cities = {}
    for i in range(1000):
        lat, lon = None, None
        while not lat or not lon:
            cidade = geolocator.reverse(f"{randint(-60, 50)}, {randint(-130, -30)}")
            if cidade:
                address = cidade.raw.get("address")
                if address:
                    cidade_name = address.get("city", address.get("town", address.get("village", "")))
                    if cidade_name and cidade_name not in cities:
                        lat, lon = float(cidade.raw.get("lat")), float(cidade.raw.get("lon"))
                        cities[cidade_name] = (lat, lon)
                        print(i)
    print(cities)


city_generator()