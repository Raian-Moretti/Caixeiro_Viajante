import random
import math
from plot import plot, plot_progress
from cities import Cities

population_size = 200
generations = 1000
mutation_rate = 0.05
crossover_rate = 0.85

def mutation(population):

    # for i in range(len(population)):
    #     if(random.random() < mutation_rate):
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
    # new_population = []
    # for first_parent, second_parent in parents:
    #     if random.random() < crossover_rate:
    #         first_half = []
    #         second_half = []
    #         first_half_2 = []
    #         second_half_2 = []
    #         # rand1 = random.sample(range (0, int(len(first_parent)/2)))
    #         # rand2 = random.sample(range (0, int(len(first_parent)/2)))
    #         rand1 = math.ceil(random.random()*(len(first_parent)))
    #         rand2 = math.ceil(random.random()*(len(first_parent)))
            
    #         begin = min(rand1,rand2)
    #         end = max(rand1,rand2)
            
    #         for i in range(begin, end):
    #             first_half.append(first_parent[i])
                
    #         for i in range(0, begin):
    #             first_half_2.append(first_parent[i])
             
    #         for i in range(end, len(first_parent)):
    #             first_half_2.append(first_parent[i])
            
    #         second_half = [city for city in second_parent if city not in first_half]
    #         second_half_2 = [city for city in second_parent if city not in first_half_2]
    #         child1 = first_half + second_half
    #         # print(child1)
    #         child2 = first_half_2 + second_half_2
    #         # print(child2)

    #         new_population.append(child1)
    #         new_population.append(child2)

    #     else:
    #         new_population.append(first_parent)
    #         new_population.append(second_parent)
    
    new_population = []
    for first_parent, second_parent in parents:
        if random.random() < crossover_rate:
            child = []
            for i in range(int(len(first_parent)/2)):
                child.append(first_parent[i])
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
    
    # parents = []
    # total_fitness = 0
    # for i in range(len(individuals)):
    #     var_fitness = fitness(individuals[i])
    #     total_fitness += var_fitness    
    
    # probabilities = []
    # for i in range(len(individuals)):
    #     var_fitness = fitness(individuals[i])
    #     probabilities.append(var_fitness/total_fitness)
    # # print(len(probabilities))
    
    # # for i in range(len(individuals)):
    # #     print("aqui:", individuals[i], probabilities[i])
    
    # while len(parents) != (int(len(individuals)/2)):
    #     first_parent = random.choices(individuals, probabilities)[0]
    #     second_parent = random.choices(individuals, probabilities)[0]
    #     if(first_parent != second_parent):
    #         if(len(parents) == 0):
    #             # print("entrou no if")
    #             parents.append((first_parent,second_parent))
    #         else:
    #             # print("entrou no else")
    #             for i in range(len(parents)):
    #                 # print(f"Primeiro: \n{first_parent} != {parents[i][0]} e\n {first_parent} != {parents[i][1]}")
    #                 # print(f"Segundo: \n{second_parent} != {parents[i][0]} e\n {second_parent} != {parents[i][1]}")
    #                 if((first_parent != parents[i][0] and first_parent != parents[i][1]) and (second_parent != parents[i][0] and second_parent != parents[i][1])):
    #                     # print(len(parents))
    #                     parents.append((first_parent,second_parent))
    #                     # print("Adicionei")
    #                     # break
           
    # # for i in range(len(parents)):
    #     # print(parents[i][0], id(parents[i][0]) ,parents[i][1], id(parents[i][1]))
    
    probabilities = [] 
    total_fitness = 0
    for i in range(len(individuals)):
        var_fitness = fitness(individuals[i])
        total_fitness += var_fitness
    
    probabilities = []
    for i in range(len(individuals)):
        var_fitness = fitness(individuals[i])
        probabilities.append(var_fitness/total_fitness)

    parents = []
    while len(parents) != (int(len(individuals))):
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
    progress = []
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
                        print("Melhor encontrado", i)
        progress.append(1/best_fitness)
            # print("generation:",i," ",individuals[j])
    # print(progress)
    # best_route = individuals[0]
    # for i in range(1,len(individuals)):
    #     if(fitness(best_route) < fitness(individuals[i])):
    #         best_route = individuals[i]
    
    # print(best_route)
    print(best_generation)
    print(len(progress))
    plot_progress(progress)
    plot(best_route)
    print("Problem solved for Beam.")
    return 1/best_fitness