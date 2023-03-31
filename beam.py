## Menu class for Beam Search Algorithm
import math
import random
from plot import plot, plot_progress
from cities import Cities

k = 5
generations = 500

def generate_neighbours(individuals):
    new_individual = []
    neighbours = []
    for i in range(len(individuals)):
        # print("pai:",individuals[i], Beam.fitness(individuals[i]))
        rand1 = math.ceil(random.random()*(len(Cities.cities)-1))
        rand2 = math.ceil(random.random()*(len(Cities.cities)-1))
        begin, end = 0, 0
        if(rand1 < rand2):
            begin = rand1
            end = rand2
        else:
            begin = rand2
            end = rand1
        
        new_individual[:begin] = individuals[i][:begin]
        new_individual[begin:end] = reversed(individuals[i][begin:end])
        new_individual[end:] = individuals[i][end:]
        neighbours.append(new_individual)
        # print("fiote:",new_individual, Beam.fitness(new_individual))
        new_individual = []
    
    individuals.extend(neighbours)
    return individuals

# Sorteia os indivíduos da população aleatoriamente
def population(population_size, cities):
    individuals = []
    for i in range(population_size):
        individual = list(cities.keys())
        random.shuffle(individual)
        individuals.append(individual)
    
    return individuals

def selection(individuals):
    mid_point = int(len(individuals)/2)

    best_individuals = individuals[:mid_point]
    for i in range(len(best_individuals)):
        for j in range(mid_point,len(individuals)):
            if(fitness(best_individuals[i]) < fitness(individuals[j])):
                swap = best_individuals[i]
                best_individuals[i] = individuals[j]
                individuals[j] = swap
    
    return best_individuals

def fitness(route):
    # A distância total da rota é o parâmetro responsável por definir o indivíduo com melhor fitness
    total_distance = 0
    for i in range(1, len(route)):
        total_distance+= Cities.calculate_distance(route[i], route[i-1])
    total_distance+= Cities.calculate_distance(route[len(route)-1], route[0])

    fitness = 1 / total_distance
    return fitness

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

def beam_search():
    
    individuals = population(k, Cities.cities)
    best_generation = 0
    progress = []
    for i in range(generations):
        print("GENERATION: ", i)
        individual_with_neighbour = generate_neighbours(individuals)
        best_individuals = selection(individual_with_neighbour)
        # for i in range(len(best_individuals)):
        #     print(best_individuals[i], Beam.fitness(best_individuals[i]))

        individuals = best_individuals

        for j in range(len(individuals)):
            if(i == 0):
                best_fitness = fitness(individuals[j])
                best_route = individuals[j]
            
            else:
                if(best_fitness < fitness(individuals[j])):
                    best_fitness = fitness(individuals[j])
                    if(fitness(best_route) < best_fitness):
                        best_generation = i
                        best_route = individuals[j]
        progress.append(1/best_fitness)

            # else:
            #     if(best_fitness < fitness(individuals[j])):
            #         best_generation = i
            #         best_fitness = fitness(individuals[j])
            #         best_route = individuals[j]
            # print("generation:",i," ",individuals[j])
            # print("Fitness: ", Beam.fitness(individuals[j]))

    # print(best_route)
    print(best_generation)
    print(len(progress))
    plot_progress(progress)
    # plot(best_route)
    print("Problem solved for Beam.")
    return 1/best_fitness
