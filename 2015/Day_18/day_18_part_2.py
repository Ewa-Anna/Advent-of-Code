from day_18_part_1 import input_data, parse_input, count_on_neighbors, count_lights_on

def fix_corners(grid):
    grid[0][0] = '#'
    grid[0][-1] = '#'
    grid[-1][0] = '#'
    grid[-1][-1] = '#'

def step(grid):
    new_grid = [['.' for _ in row] for row in grid]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            on_neighbors = count_on_neighbors(grid, x, y)
            if grid[x][y] == '#' and on_neighbors in (2, 3):
                new_grid[x][y] = '#'
            elif grid[x][y] == '.' and on_neighbors == 3:
                new_grid[x][y] = '#'
            else:
                new_grid[x][y] = '.'
    fix_corners(new_grid) 
    return new_grid

def simulate_lights(initial_grid, steps):
    grid = initial_grid
    fix_corners(grid)  
    for _ in range(steps):
        grid = step(grid)
    return grid

initial_grid = parse_input(input_data.strip())
final_grid = simulate_lights(initial_grid, 100)
result = count_lights_on(final_grid)
print(result)