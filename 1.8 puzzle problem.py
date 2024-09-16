import heapq

DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def get_neighbors(x, y):
    neighbors = []
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny):
            neighbors.append((nx, ny))
    return neighbors

def calculate_cost(puzzle, goal):
    cost = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0 and puzzle[i][j] != goal[i][j]:
                cost += 1
    return cost

def print_puzzle(puzzle):
    for row in puzzle:
        print(' '.join(str(x) for x in row))
    print()

def solve_puzzle(initial, goal):
    empty_tile = [(i, j) for i in range(3) for j in range(3) if initial[i][j] == 0][0]
    pq = []
    heapq.heappush(pq, (calculate_cost(initial, goal), 0, initial, empty_tile, None))

    visited = set()
    visited.add(tuple(tuple(row) for row in initial))

    while pq:
        cost, level, puzzle, (x, y), parent = heapq.heappop(pq)

        if puzzle == goal:
            path = []
            while parent:
                path.append(parent[2])
                parent = parent[4]
            path.reverse()
            for p in path:
                print_puzzle(p)
            print_puzzle(puzzle)
            return

        for nx, ny in get_neighbors(x, y):
            new_puzzle = [row[:] for row in puzzle]
            new_puzzle[x][y], new_puzzle[nx][ny] = new_puzzle[nx][ny], new_puzzle[x][y]
            new_puzzle_tuple = tuple(tuple(row) for row in new_puzzle)

            if new_puzzle_tuple not in visited:
                visited.add(new_puzzle_tuple)
                heapq.heappush(pq, (calculate_cost(new_puzzle, goal) + level + 1, level + 1, new_puzzle, (nx, ny), (cost, level, puzzle, (x, y), parent)))

initial = [
    [1, 2, 3],
    [5, 6, 0],
    [7, 8, 4]
]

goal = [
    [1, 2, 3],
    [5, 8, 6],
    [0, 7, 4]
]

solve_puzzle(initial, goal)
