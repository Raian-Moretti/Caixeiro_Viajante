import random
import math
import matplotlib.pyplot as plt

# Define the cities
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

# Define the distance between two cities using the Haversine formula
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

# Define the initial population
def create_population(num_cities, size):
    population = []
    for i in range(size):
        individual = list(range(num_cities))
        random.shuffle(individual)
        population.append(individual)
    return population

# Define the fitness function
def calculate_fitness(individual):
    total_distance = 0
    for i in range(len(individual)):
        city1 = cities[list(cities.keys())[individual[i]]]
        if i == len(individual)-1:
            city2 = cities[list(cities.keys())[individual[0]]]
        else:
            city2 = cities[list(cities.keys())[individual[i+1]]]
        total_distance += calculate_distance(city1, city2)
    return 1/total_distance

# Define the selection function
def selection(population):
    fitnesses = [calculate_fitness(individual) for individual in population]
    total_fitness = sum(fitnesses)
    probabilities = [fitness/total_fitness for fitness in fitnesses]
    indices = range(len(population))
    parents = []
    for i in range(len(population)):
        parent1 = population[random.choices(indices, probabilities)[0]]
        parent2 = population[random.choices(indices, probabilities)[0]]
        parents.append((parent1, parent2))
    return parents

# Define the crossover function
def crossover(parents, crossover_probability):
    offspring = []
    for parent1, parent2 in parents:
        if random.random() < crossover_probability:
            point1 = random.randint(0, len(parent1)-1)
            point2 = random.randint(0, len(parent1)-1)
            if point1 > point2:
                point1, point2 = point2, point1
            child = [None]*len(parent1)
            for i in range(point1, point2+1):
                child[i] = parent1[i]
                j = 0
            for i in range(len(parent2)):
                if not parent2[i] in child:
                    while child[j] != None:
                        j += 1
                    child[j] = parent2[i]
            offspring.append(child)
        else:
            offspring.append(parent1)
    return offspring

# Define the mutation function
def mutate(individual, probability):
    for i in range(len(individual)):
        if random.random() < probability:
            j = random.randint(0, len(individual)-1)
            individual[i], individual[j] = individual[j], individual[i]
    return individual

# Define the genetic algorithm function
def genetic_algorithm(num_cities, population_size, num_generations, crossover_probability, mutation_probability):
    # Create the initial population
    population = create_population(num_cities, population_size)
    # Record the best fitness and the best individual in each generation
    best_fitness = None
    best_individual = None
    fitnesses = []
    # Run the genetic algorithm for the specified number of generations
    for generation in range(num_generations):
        # Select the parents
        parents = selection(population)
        # Crossover the parents to create the offspring
        offspring = crossover(parents, crossover_probability)
        # Mutate the offspring
        population = [mutate(individual, mutation_probability) for individual in offspring]
        # Evaluate the fitness of the new population
        fitnesses = [calculate_fitness(individual) for individual in population]
        # Record the best fitness and the best individual in this generation
        max_fitness_index = fitnesses.index(max(fitnesses))
        if best_fitness == None or fitnesses[max_fitness_index] > best_fitness:
            best_fitness = fitnesses[max_fitness_index]
            best_individual = population[max_fitness_index]
        print("Generation ", generation, " - Best Fitness: ", best_fitness)
    # Plot the optimal route
    plt.figure(figsize=(8, 6))
    x = []
    y = []
    for i in best_individual:
        city = list(cities.keys())[i]
        x.append(cities[city][1])
        y.append(cities[city][0])
        plt.text(cities[city][1], cities[city][0], city, fontsize=8)
    plt.plot(x, y, '-ro')
    plt.plot(x+[x[0]], y+[y[0]], '-ro')

    # Add distance labels between cities
    total_distance = 0
    for i in range(len(best_individual)-1):
        city1 = list(cities.keys())[best_individual[i]]
        city2 = list(cities.keys())[best_individual[i+1]]
        x1, y1 = x[i], y[i]
        x2, y2 = x[i+1], y[i+1]
        distance = calculate_distance(cities[city1], cities[city2])
        total_distance += distance
        plt.text((x1+x2)/2, (y1+y2)/2, "{:.2f}".format(distance), fontsize=6)
    plt.title("Optimal Route for {} Cities\nTotal Distance: {:.2f} km".format(num_cities, total_distance))
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()

# Run the genetic algorithm with num_cities cities
num_cities = 30
genetic_algorithm(num_cities, 1000, 300, 0.8, 0.1)