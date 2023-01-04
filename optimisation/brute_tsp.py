import math
import numpy as np
from itertools import permutations
import matplotlib.pyplot as plt
import time

startTime = time.time()

n = 10

def create_scaled_random(max_pos, n_points, seed):
    np.random.seed(seed)
    for n in np.random.rand(n_points, 2):
        yield tuple(max_pos*component for component in n)

def create_data_model(n_points, max_pos):
    pointGenerator = create_scaled_random(max_pos, n_points, 0)
    data = {}
    data['locations'] = [point for point in pointGenerator]
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data

def compute_distance_matrix(locations, matrix_scaling):
    distances = {}
    for from_index, from_node in enumerate(locations):
        distances[from_index] = {}
        for to_index, to_node in enumerate(locations):
            if from_index == to_index:
                distances[from_index][to_index] = 0
            else:
                distances[from_index][to_index] = int(
                    matrix_scaling*math.hypot((from_node[0] - to_node[0]), #euclidean distance from point from_node to point to_node
                               (from_node[1] - to_node[1])))
    return distances

data = create_data_model(n, 20)
scaled_dist_matrix = compute_distance_matrix(data['locations'], 100)

best = {'route':[], 'len':1000000}
for route in permutations([a for a in range(0, n)]):
    route = list(route)
    route.append(route[0])
    total_dist = 0
    i = 0
    while i < len(route)-1:
        dist = scaled_dist_matrix[route[i]][route[i+1]]
        total_dist += dist
        i += 1
    if total_dist < best['len']:
        best['route'] = route
        best['len'] = total_dist
    #print(total_dist, route)

def convert_to_plot(points):
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    return x, y

endTime = time.time()
print(round(abs(startTime - endTime), 2))

#points = [data['locations'][i] for i in best['route']]
x, y = convert_to_plot([data['locations'][i] for i in best['route']])
plt.plot(x, y, ls='-', marker='o', mfc='w', mec='r')
plt.show()