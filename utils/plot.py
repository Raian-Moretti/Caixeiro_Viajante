import matplotlib.pyplot as plt
from src.cities import Cities

def plot_progress(progress):
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.plot(progress)
    plt.show()

def plot(best_route):
    plt.figure(figsize=(8, 6))
    x = []
    y = []
    for i in best_route:
        # print(i)
        city = Cities.cities[i]
        # city = list(Genetic.cities.keys())[i]
        # print(city)
        x.append(city[1])
        y.append(city[0])
        # plt.text(city[1], city[0], city, fontsize=8)
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
        distance = Cities.calculate_distance(city1, city2)
        total_distance += distance
        plt.text((x1+x2)/2, (y1+y2)/2, "{:.2f}".format(distance), fontsize=6)
    city1 = best_route[len(best_route)-1]
    city2 = best_route[0]
    x1, y1 = x[len(best_route)-1], y[len(best_route)-1]
    x2, y2 = x[0], y[0]
    distance = Cities.calculate_distance(city1,city2)
    total_distance += distance
    plt.text((x1+x2)/2, (y1+y2)/2, "{:.2f}".format(distance), fontsize=6)

    plt.title("Optimal Route for {} Cities\nTotal Distance: {:.2f} km".format(len(Cities.cities), total_distance))
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()