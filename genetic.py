import random
import math
from plot import plot
from cities import Cities

population_size = 50
generations = 200
mutation_rate = 0.05
crossover_rate = 0.8

def mutation(population):

    # for i in range(len(population)):
    #     if(random.random() < Cities.mutation_rate):

    #         first_mutation = math.ceil(random.random()*(len(Cities.cities)-1))
    #         second_mutation = math.ceil(random.random()*(len(Cities.cities)-1))
    #         population[i][first_mutation], population[i][second_mutation] = population[i][second_mutation], population[i][first_mutation]
    # return population

    new_population = []
    for i in range(len(population)):
        if(random.random() < mutation_rate):
            new_individual = []
            rand1 = math.ceil(random.random()*(len(Cities.cities)-1))
            rand2 = math.ceil(random.random()*(len(Cities.cities)-1))
            begin, end = 0, 0
            if(rand1 < rand2):
                begin = rand1
                end = rand2
            else:
                begin = rand2
                end = rand1
            
            new_individual[:begin] = population[i][:begin]
            new_individual[begin:end] = reversed(population[i][begin:end])
            new_individual[end:] = population[i][end:]
            new_population.append(new_individual)
        else:
            new_population.append(population[i])

    return new_population


def crossover(parents):
    new_population = []
    for first_parent, second_parent in parents:

        if random.random() < crossover_rate:
            child = []
            for i in range(int((len(first_parent))/2)):
                child.append(first_parent[i+1])
            for i in range(len(second_parent)):
                if not(second_parent[i] in child):
                    child.append(second_parent[i])
            new_population.append(child)
        else:

            if(fitness(first_parent) > fitness(second_parent)):
                new_population.append(first_parent)
            else:
                new_population.append(second_parent)
    
    return new_population


def selection(individuals):
    total_fitness = 0
    for i in range(len(individuals)):
        var_fitness = fitness(individuals[i])
        total_fitness += var_fitness
    
    probabilities = []
    for i in range(len(individuals)):
        var_fitness = fitness(individuals[i])
        probabilities.append(var_fitness/total_fitness)

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
        total_distance+= Cities.calculate_distance(route[i], route[i-1])
    total_distance+= Cities.calculate_distance(route[len(route)-1], route[0])

    fitness = 1 / total_distance
    return fitness

def genetic_algorithm():

    individuals = population(population_size, Cities.cities)
    best_route = []
    best_fitness = 0
    best_generation = 0
    for i in range(generations):
        print("GENERATION: ", i)

        parents = selection(individuals)

        new_population = crossover(parents)
        
        new_population = mutation(new_population)

        individuals = new_population

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
            # print("generation:",i," ",individuals[j])
            # print("Fitness: ", Cities.fitness(individuals[j]))

    print(best_generation)
    plot(best_route)
    print("Problem solved for Cities.")