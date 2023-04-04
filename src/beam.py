## Menu class for Beam Search Algorithm
import math
import random
from utils.plot import plot, plot_progress
from src.cities import Cities

k = 10
generations = 2000

def generate_neighbours(individuals):
    new_individual = []
    neighbours = []
    
    for i in range(len(individuals)):
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
        new_individual = []
    
    individuals.extend(neighbours)
    return individuals

# Sorteia os indivíduos da população aleatoriamente
def population(population_size, cities):
    individuals = []
    
    while len(individuals) != population_size:
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

def beam_search():
    
    individuals = population(k, Cities.cities)
    best_generation = 0
    progress = []

    for i in range(generations):
        print("GENERATION: ", i)
        individual_with_neighbour = generate_neighbours(individuals)
        best_individuals = selection(individual_with_neighbour)

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

    print(best_generation)
    print(len(progress))
    print("\nProgress Visualization")
    plot_progress(progress)
    print("\nBest Route Visualization")
    plot(best_route)
    print("\nFinished Beam Algorithm")
    return 1/best_fitness
