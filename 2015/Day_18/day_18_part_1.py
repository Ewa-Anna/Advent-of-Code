puzzle = "input.txt"

with open(puzzle, "r") as file:
    input_data = file.read()


def parse_input(input_data):
    return [list(line.strip()) for line in input_data.splitlines()]


def count_on_neighbors(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            count += grid[nx][ny] == "#"
    return count


def step(grid):
    new_grid = [["." for _ in row] for row in grid]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            on_neighbors = count_on_neighbors(grid, x, y)
            if grid[x][y] == "#" and on_neighbors in (2, 3):
                new_grid[x][y] = "#"
            elif grid[x][y] == "." and on_neighbors == 3:
                new_grid[x][y] = "#"
            else:
                new_grid[x][y] = "."
    return new_grid


def simulate_lights(initial_grid, steps):
    grid = initial_grid
    for _ in range(steps):
        grid = step(grid)
    return grid


def count_lights_on(grid):
    return sum(row.count("#") for row in grid)


initial_grid = parse_input(input_data.strip())
final_grid = simulate_lights(initial_grid, 100)
result = count_lights_on(final_grid)
print(result)
