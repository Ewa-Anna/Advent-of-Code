import heapq

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
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # East, South, West, North

    moves = []
    forward_x, forward_y = x + directions[direction][0], y + directions[direction][1]

    if 0 <= forward_y < len(maze) and 0 <= forward_x < len(maze[0]) and maze[forward_y][forward_x] != '#':
        moves.append(((forward_x, forward_y), direction, 1))

    left_direction = (direction - 1) % 4
    right_direction = (direction + 1) % 4
    moves.append(((x, y), left_direction, 1000))  # Rotate left
    moves.append(((x, y), right_direction, 1000))  # Rotate right

    return moves

def dijkstra_min_cost(maze, start, end):
    start_direction = 0  

    priority_queue = [(0, start, start_direction)] 
    visited = set()

    while priority_queue:
        cost, position, direction = heapq.heappop(priority_queue)

        if (position, direction) in visited:
            continue
        visited.add((position, direction))

        if position == end:
            return cost

        for next_position, next_direction, move_cost in get_neighbors(position, direction, maze):
            heapq.heappush(priority_queue, (cost + move_cost, next_position, next_direction))

    return float('inf')

if __name__ == "__main__":
    maze, start, end = parse_maze("input.txt")
    result = dijkstra_min_cost(maze, start, end)
    print(result)
