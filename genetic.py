import math
import random

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

    population_size = 5
    generations = 10
    mutation_rate = 0.05
    crossover_rate = 0.8

    route = {}

    # def crossover(parents):
    #     for first_parent, second_parent in parents:
    #         if random.random() < Genetic.crossover_rate:
    #             child = 

    def selection(individuals):
        # ranked_individuals = sorted(individuals, key=lambda x: x[0])
        total_fitness = 0
        for i in range(len(individuals)):
            fitness = Genetic.fitness(individuals[i])
            individuals[i].insert(0,fitness)
            total_fitness += fitness
        
        probabilities = []
        for i in range(len(individuals)):
            probabilities.append(individuals[i][0]/total_fitness)
        

        parents = []
        while len(parents) != len(individuals):
            first_parent = random.choices(individuals, probabilities)[0]
            second_parent = random.choices(individuals, probabilities)[0]
            
            if(first_parent != second_parent):
                parents.append((first_parent,second_parent))
                print(" first parent: ",first_parent,"\n","second parent:",second_parent)


        # itr = len(individuals)
        # for i in range(itr):
        #     current_individuals = individuals
        #     first_parent = random.choices(individuals, probabilities)[0]
        #     second_parent = random.choices(individuals, probabilities)[0]
            
        #     if(first_parent == second_parent):
        #         itr+=1
        #         continue

        #     print(i)
            
        #     parents.append((first_parent,second_parent))

        # for first_parent, second_parent in parents:
        #     print(" first parent: ",first_parent,"\n","second parent:",second_parent)
        #     if(first_parent==second_parent):
        #         print("oi")
        # Genetic.crossover(parents)
        return parents        

    # Sorteia os indivíduos da população aleatoriamente
    def population(population_size, cities):
        individuals = []

        for i in range(population_size):
            individual = list(cities.keys())
            random.shuffle(individual)
            individuals.append(individual)
        
        Genetic.selection(individuals)

        return individuals

    def fitness(route):
        # A distância total da rota é o parâmetro responsável por definir o indivíduo com melhor fitness
        total_distance = 0
        for i in range(1, len(route)):
                total_distance+= Genetic.calculate_distance(route[i], route[i-1])
        
        fitness = 1 / total_distance
        return fitness
    
    # Distância entre dois pontos em uma esfera a partir de lat e lon
    def calculate_distance(city1, city2):

        lat1, lon1 = Genetic.cities[city1]
        lat2, lon2 = Genetic.cities[city2]
        radius = 6371 # km

        dlat = math.radians(lat2-lat1)
        dlon = math.radians(lon2-lon1)
        a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = radius * c

        return d
    
    def genetic_algorithm(self):

        Genetic.population(Genetic.population_size, Genetic.cities)

        print("Problem solved for Genetic.")