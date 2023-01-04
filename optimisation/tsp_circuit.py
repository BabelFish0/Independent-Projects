from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import numpy as np
import math
import matplotlib.pyplot as plt
import time

start = time.time()

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

def distance_callback(from_index, to_index):
    '''convert from index of routing manager (i.e. route point n) to index of positions (i.e. location matrix point x)'''
    return scaled_dist_matrix[manager.IndexToNode(from_index)][manager.IndexToNode(to_index)]

data = create_data_model(5, 20)
scaled_dist_matrix = compute_distance_matrix(data['locations'], 1)

manager = pywrapcp.RoutingIndexManager(len(data['locations']), data['num_vehicles'], data['depot'])
routing = pywrapcp.RoutingModel(manager)

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
#search_parameters.

solution = routing.SolveWithParameters(search_parameters)

def reorder_points(routing, manager, solution, data):
    ordered_route = []
    ordered_points = []
    index = routing.Start(0)
    while not routing.IsEnd(index):
        ordered_route.append(manager.IndexToNode(index))
        index = solution.Value(routing.NextVar(index))
    ordered_route.append(manager.IndexToNode(index))
    for NodeIndex in ordered_route:
        ordered_points.append(data['locations'][NodeIndex])
    return ordered_points

def convert_to_plot(points):
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    return x, y

end = time.time()

if solution:
    route_points = reorder_points(routing, manager, solution, data)
    #print('Route: {}'.format(route_points))
    print(round(end-start, 2))
    x, y = convert_to_plot(route_points)
    plt.plot(x, y, ls='-', marker='o', mfc='w', mec='r')
    plt.show()