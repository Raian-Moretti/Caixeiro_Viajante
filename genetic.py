import math
import random
import matplotlib.pyplot as plt

# Menu class for Genetic Algorithm
class Genetic:
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


    }

    population_size = 500
    generations = 200
    mutation_rate = 0.20
    crossover_rate = 0.8

    def mutation(population):
        # print(population)

        # num_mutations = 2
        first_mutation = math.ceil(random.random()*(len(Genetic.cities)-1))
        second_mutation = math.ceil(random.random()*(len(Genetic.cities)-1))
        # print(population)
        # print(first_mutation,second_mutation)
        # print(population)
        # first_mutation, second_mutation = random.sample(len(Genetic.cities),num_mutations)

        population[first_mutation], population[second_mutation] = population[second_mutation], population[first_mutation]

        return population
        

    def crossover(parents):
        new_population = []
        for first_parent, second_parent in parents:

            if random.random() < Genetic.crossover_rate:
                child = []
                for i in range(int((len(first_parent))/2)):
                    child.append(first_parent[i+1])
                for i in range(len(second_parent)):
                    if not(second_parent[i] in child):
                        child.append(second_parent[i])
                new_population.append(child)
            else:

                if(Genetic.fitness(first_parent) > Genetic.fitness(second_parent)):
                    new_population.append(first_parent)
                else:
                    new_population.append(second_parent)
        
        return new_population


    def selection(individuals):
        total_fitness = 0
        for i in range(len(individuals)):
            fitness = Genetic.fitness(individuals[i])
            total_fitness += fitness
        
        probabilities = []
        for i in range(len(individuals)):
            fitness = Genetic.fitness(individuals[i])
            probabilities.append(fitness/total_fitness)

        parents = []
        while len(parents) != len(individuals):
            first_parent = random.choices(individuals, probabilities)[0]
            second_parent = random.choices(individuals, probabilities)[0]
            
            if(first_parent != second_parent):
                parents.append((first_parent,second_parent))

        return parents        

    # Sorteia os indivíduos da população aleatoriamente
    def population(population_size, cities):
        individuals = []

        for i in range(population_size):
            individual = list(cities.keys())
            random.shuffle(individual)
            individuals.append(individual)
        
        return individuals

    def fitness(route):
        # A distância total da rota é o parâmetro responsável por definir o indivíduo com melhor fitness
        total_distance = 0
        for i in range(1, len(route)):
            total_distance+= Genetic.calculate_distance(route[i], route[i-1])
        total_distance+= Genetic.calculate_distance(route[len(route)-1], route[0])

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
    
    def genetic_algorithm():

        individuals = Genetic.population(Genetic.population_size, Genetic.cities)
        best_route = []
        best_fitness = 0
        for i in range(Genetic.generations):
            parents = Genetic.selection(individuals)

            new_population = Genetic.crossover(parents)
            
            for j in range(len(new_population)):
                new_population[j] = Genetic.mutation(new_population[j])

            individuals = new_population

            for j in range(len(individuals)):
                if(j == 0):
                    best_fitness = Genetic.fitness(individuals[j])
                    best_route = individuals[j]

                else:
                    if(best_fitness < Genetic.fitness(individuals[j])):
                        best_fitness = Genetic.fitness(individuals[j])
                        best_route = individuals[j]
                # print("generation:",i," ",individuals[j])
                # print("Fitness: ", Genetic.fitness(individuals[j]))

        # print(best_route)
        plt.figure(figsize=(8, 6))
        x = []
        y = []
        for i in best_route:
            # print(i)
            city = Genetic.cities[i]
            # city = list(Genetic.cities.keys())[i]
            # print(city)
            x.append(city[1])
            y.append(city[0])
            plt.text(city[1], city[0], city, fontsize=8)
        plt.plot(x, y, '-ro')
        plt.plot(x+[x[0]], y+[y[0]], '-ro')

            # Add distance labels between cities
        total_distance = 0
        for i in range(len(best_route)-1):
            # city = Genetic.cities

            city1 = best_route[i]
            city2 = best_route[i+1]
            x1, y1 = x[i], y[i]
            x2, y2 = x[i+1], y[i+1]
            # print(city1, city2)
            distance = Genetic.calculate_distance(city1, city2)
            total_distance += distance
            plt.text((x1+x2)/2, (y1+y2)/2, "{:.2f}".format(distance), fontsize=6)
        city1 = best_route[len(best_route)-1]
        city2 = best_route[0]
        x1, y1 = x[len(best_route)-1], y[len(best_route)-1]
        x2, y2 = x[0], y[0]
        distance = Genetic.calculate_distance(city1,city2)
        total_distance += distance
        plt.text((x1+x2)/2, (y1+y2)/2, "{:.2f}".format(distance), fontsize=6)

        plt.title("Optimal Route for {} Cities\nTotal Distance: {:.2f} km".format(len(Genetic.cities), total_distance))
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.show()
        print("Problem solved for Genetic.")