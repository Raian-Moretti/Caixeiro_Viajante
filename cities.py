import math

class Cities:
    cities = {
        "Abu Dhabi": (24.4539, 54.3773),
        "Amsterdam": (52.3667, 4.8945),
        "Athens": (37.9838, 23.7275),
        "Beijing": (39.9042, 116.4074),
        "Berlin": (52.5200, 13.4050),
        "Brasília": (-15.8267, -47.9218),
        "Cairo": (30.0444, 31.2357),
        "Canberra": (-35.2820, 149.1287),
        "Havana": (23.1136, -82.3666),
        "Islamabad": (33.6844, 73.0479),
        "Jakarta": (-6.1751, 106.8650),
        "Kiev": (50.4501, 30.5234),
        "Lisbon": (38.7223, -9.1393),
        "London": (51.5074, -0.1278),
        "Madrid": (40.4168, -3.7038),
        "Mexico City": (19.4326, -99.1332),
        "Moscow": (55.7558, 37.6173),
        "Nairobi": (-1.2921, 36.8219),
        "New Delhi": (28.6139, 77.2090),
        "Oslo": (59.9139, 10.7522),
        "Ottawa": (45.4215, -75.6972),
        "Paris": (48.8566, 2.3522),
        "Rome": (41.9028, 12.4964),
        "Seoul": (37.5665, 126.9780),
        "Stockholm": (59.3293, 18.0686),
        "Tokyo": (35.6762, 139.6503),
        "Vienna": (48.2082, 16.3738),
        "Washington, D.C.": (38.9072, -77.0369),
        "Wellington": (-41.2865, 174.7762),
        "Bangkok": (13.7563, 100.5018),
    }

    # Distância entre dois pontos em uma esfera a partir de lat e lon
    def calculate_distance(city1, city2):

        lat1, lon1 = Cities.cities[city1]
        lat2, lon2 = Cities.cities[city2]
        radius = 6371 # km

        dlat = math.radians(lat2-lat1)
        dlon = math.radians(lon2-lon1)
        a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = radius * c

        return d
