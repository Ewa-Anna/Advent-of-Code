import heapq
from collections import defaultdict

def parse_maze(file_path):
    with open(file_path, 'r') as file:
        maze = [list(line.strip()) for line in file]

    start = None
    end = None

    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)

    return maze, start, end

def get_neighbors(position, direction, maze):
    x, y = position
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] 

    moves = []
    forward_x, forward_y = x + directions[direction][0], y + directions[direction][1]

    if 0 <= forward_y < len(maze) and 0 <= forward_x < len(maze[0]) and maze[forward_y][forward_x] != '#':
        moves.append(((forward_x, forward_y), direction, 1))

    left_direction = (direction - 1) % 4
    right_direction = (direction + 1) % 4
    moves.append(((x, y), left_direction, 1000))  
    moves.append(((x, y), right_direction, 1000)) 

    return moves

def dijkstra(maze, start, initial_directions):
    priority_queue = [(0, start, direction) for direction in initial_directions]  
    visited = defaultdict(lambda: float('inf'))  

    while priority_queue:
        cost, position, direction = heapq.heappop(priority_queue)

        if visited[(position, direction)] <= cost:
            continue
        visited[(position, direction)] = cost

        for next_position, next_direction, move_cost in get_neighbors(position, direction, maze):
            next_cost = cost + move_cost
            if next_cost < visited[(next_position, next_direction)]:
                heapq.heappush(priority_queue, (next_cost, next_position, next_direction))

    return visited

def flip_direction(direction):
    return (direction + 2) % 4

def count_best_path_tiles(maze, from_start, from_end, best_cost):
    best_paths = set()

    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == '#':
                continue

            for direction in range(4):
                if (from_start[((x, y), direction)] + \
                    from_end[((x, y), flip_direction(direction))]) == best_cost:
                    best_paths.add((x, y))

    return len(best_paths)

if __name__ == "__main__":
    maze, start, end = parse_maze("input.txt")

    from_start = dijkstra(maze, start, [0]) 
    best_cost = min(from_start[(end, direction)] for direction in range(4))
    from_end = dijkstra(maze, end, range(4))

    count = count_best_path_tiles(maze, from_start, from_end, best_cost)
    print(count)
