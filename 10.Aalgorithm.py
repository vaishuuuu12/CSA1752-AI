import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, goal, neighbors, heuristic):
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    while open_set:
        current = heapq.heappop(open_set)[1]
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for neighbor in neighbors(current):
            tentative_g_score = g_score[current] + 1  # Assumes cost from current to neighbor is always 1
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
                
    return None

def neighbors(node):
    x, y = node
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

# Example usage
start = (0, 0)
goal = (5, 5)

path = a_star(start, goal, neighbors, heuristic)
print("Path:", path)

