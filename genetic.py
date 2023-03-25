import math
# Menu class for Genetic Algorithm
class Genetic:
    cities = {
        "Abu Dhabi": (24.4539, 54.3773),
        "Amsterdam": (52.3667, 4.8945),
        "Athens": (37.9838, 23.7275),
        "Beijing": (39.9042, 116.4074),
        "Berlin": (52.5200, 13.4050),
        "Brasília": (-15.8267, -47.9218),
    }

    num_cities = len(cities)
    population_size = 5
    generations = 10
    mutation_rate = 0.05
    crossover_rate = 0.9

    route = {}

    def fitness(route):
        # A distância total da rota é o parâmetro responsável por definir o melhor fitness
        total_distance = 0
        for i in range(1, len(route)):
                total_distance+= Genetic.calculate_distance(route[i], route[i-1])
        
        return 1 / total_distance

    # Distância entre dois pontos em uma esfera a partir de lat e lon
    def calculate_distance(city1, city2):
        lat1, lon1 = city1
        lat2, lon2 = city2
        radius = 6371 # km

        dlat = math.radians(lat2-lat1)
        dlon = math.radians(lon2-lon1)
        a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = radius * c

        return d
    
    def genetic_algorithm(self):

        print("Problem solved for Genetic.")