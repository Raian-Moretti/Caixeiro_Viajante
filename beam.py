import itertools
import random
import math
import matplotlib.pyplot as plt





def plot_cities_and_path(cities, path):
    fig, ax = plt.subplots()
    x_vals = [coord[0] for coord in cities.values()]
    y_vals = [coord[1] for coord in cities.values()]
    ax.scatter(x_vals, y_vals, color='blue')
    total_distance = 0
    for i in range(len(path)-1):
        city1 = path[i]
        city2 = path[i+1]
        x1, y1 = cities[city1]
        x2, y2 = cities[city2]
        dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        total_distance += dist
        ax.plot([x1, x2], [y1, y2], color='red')
        ax.annotate(str(round(dist, 2)), ((x1+x2)/2, (y1+y2)/2), color='green')
    city1 = path[-1]
    city2 = path[0]
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    total_distance += dist
    ax.plot([x1, x2], [y1, y2], color='red')
    ax.annotate(str(round(dist, 2)), ((x1+x2)/2, (y1+y2)/2), color='green')
    plt.title('Total Distance: {}'.format(round(total_distance, 2)))
    plt.show()

def distance(city1, city2):
    R = 6371  # radius of the Earth in km
    lat1, lon1 = cities[city1]
    lat2, lon2 = cities[city2]
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * \
        math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def all_permutations(cities):
    return list(itertools.permutations(cities))


def generate_random_beam(cities, beam_width):
    return [list(perm) for perm in random.sample(all_permutations(cities), beam_width)]

def evaluate_fitness(paths):
    fitness_scores = []
    for path in paths:
        total_distance = 0
        for i in range(len(path)-1):
            total_distance += distance(path[i], path[i+1])
        total_distance += distance(path[-1], path[0])
        fitness_scores.append(1/total_distance)
    return fitness_scores

def select_best_paths(paths, fitness_scores, num_best):
    path_fitness_pairs = list(zip(paths, fitness_scores))
    sorted_pairs = sorted(path_fitness_pairs, key=lambda x: x[1], reverse=True)
    return [pair[0] for pair in sorted_pairs[:num_best]]

def generate_children(parents, beam_width):
    children = []
    for i in range(beam_width):
        random.shuffle(parents)
        child = list(parents[0])
        for j in range(1, len(parents)):
            for k in range(len(child)):
                if parents[j][k] not in child:
                    child[k] = parents[j][k]
                    break
        children.append(child)
    return children

def local_beam_search(cities, beam_width, iterations):
    beam = generate_random_beam(cities, beam_width)
    for i in range(iterations):
        fitness_scores = evaluate_fitness(beam)
        best_paths = select_best_paths(beam, fitness_scores, beam_width)
        if len(set([tuple(path) for path in best_paths])) == 1:
            # all best paths are the same, terminate early
            return best_paths[0]
        beam = generate_children(best_paths, beam_width)
    fitness_scores = evaluate_fitness(beam)
    best_path = select_best_paths(beam, fitness_scores, 1)[0]
    return best_path

# example usage
cities = {
    'Lisbon': (38.736946, -9.142685),
    'Madrid': (40.416775, -3.703790),
    'Paris': (48.856614, 2.352222),
    'Berlin': (52.520008, 13.404954),
    'Rome': (41.902782, 12.496366),
    'Warsaw': (52.229676, 21.012229),
    'Athens': (37.983810, 23.727539),
    'Ankara': (39.933365, 32.859741),
    'Moscow': (55.755825, 37.617298),
    'London': (51.507351, -0.127758)
}

best_path = local_beam_search(cities, 5, 100)
plot_cities_and_path(cities, best_path)
print("Best path found:", best_path)