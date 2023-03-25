import matplotlib.pyplot as plt
import numpy as np
from itertools import permutations

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

def get_distance(city1, city2):
    lat1, lon1 = city1
    lat2, lon2 = city2
    R = 6371 # Earth radius in kilometers

    dLat = np.deg2rad(lat2 - lat1)
    dLon = np.deg2rad(lon2 - lon1)
    lat1 = np.deg2rad(lat1)
    lat2 = np.deg2rad(lat2)

    a = np.sin(dLat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dLon/2)**2
    c = 2*np.arctan2(np.sqrt(a), np.sqrt(1-a))

    distance = R*c
    return distance

def plot_cities(cities, path):
    x = [city[1] for city in cities.values()]
    y = [city[0] for city in cities.values()]

    fig, ax = plt.subplots()
    ax.scatter(x, y, color="red")

    for i in range(len(path)):
        start = path[i]
        end = path[(i+1)%len(path)]
        distance = get_distance(cities[start], cities[end])
        ax.plot([cities[start][1], cities[end][1]], [cities[start][0], cities[end][0]], color="red")
        ax.text(np.mean([cities[start][1], cities[end][1]]), np.mean([cities[start][0], cities[end][0]]), round(distance, 2), fontsize=8)

    total_distance = sum([get_distance(cities[path[i]], cities[path[(i+1)%len(path)]]) for i in range(len(path))])
    ax.set_title(f"Path Distance: {round(total_distance, 2)} km")
    plt.show()

def beam_search(cities, beam_width):
    cities_list = list(cities.keys())
    paths = [[city] for city in cities_list]
    for i in range(len(cities)-1):
        new_paths = []
        for path in paths:
            last_city = path[-1]
            rest_cities = set(cities_list) - set(path)
            for city in rest_cities:
                new_path = path + [city]
                new_paths.append(new_path)
        sorted_paths = sorted(new_paths, key=lambda x: sum([get_distance(cities[x[i]], cities[x[(i+1)%len(x)]]) for i in range(len(x))]))[:beam_width]
        paths = sorted_paths
    best_path = paths[0]
    return best_path

best_path = beam_search(cities, 100)
plot_cities(cities, best_path)
