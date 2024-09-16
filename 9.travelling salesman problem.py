import itertools

def tsp_brute_force(graph, start_node):
    all_cities = list(graph.keys())
    all_cities.remove(start_node)
    permutations = itertools.permutations(all_cities)
    
    min_distance = float('inf')
    optimal_path = None
    
    for perm in permutations:
        current_path = [start_node] + list(perm) + [start_node]
        total_distance = 0
        
        for i in range(len(current_path) - 1):
            current_city = current_path[i]
            next_city = current_path[i + 1]
            total_distance += graph[current_city][next_city]
        
        if total_distance < min_distance:
            min_distance = total_distance
            optimal_path = current_path
    
    return min_distance, optimal_path

graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

start_node = 'A'

min_distance, optimal_path = tsp_brute_force(graph, start_node)
print("Minimum distance:", min_distance)
print("Optimal path:", optimal_path)
