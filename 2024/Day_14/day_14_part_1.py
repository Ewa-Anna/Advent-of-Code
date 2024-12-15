def parse_input(file_path):
    robot_positions = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            px, py = map(int, parts[0][2:].split(','))
            vx, vy = map(int, parts[1][2:].split(','))
            robot_positions.append((px, py, vx, vy))
    return robot_positions


def calculate_safety_factor(robot_positions, grid_width, grid_height, time_seconds):
    robot_grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]

    for px, py, vx, vy in robot_positions:
        new_x = (px + vx * time_seconds) % grid_width
        new_y = (py + vy * time_seconds) % grid_height

        robot_grid[new_y][new_x] += 1

    midpoint_x = grid_width // 2
    midpoint_y = grid_height // 2

    quad1 = quad2 = quad3 = quad4 = 0

    for y in range(grid_height):
        for x in range(grid_width):
            if x == midpoint_x or y == midpoint_y:
                continue

            if x < midpoint_x and y < midpoint_y:
                quad1 += robot_grid[y][x]
            elif x >= midpoint_x and y < midpoint_y:
                quad2 += robot_grid[y][x]
            elif x < midpoint_x and y >= midpoint_y:
                quad3 += robot_grid[y][x]
            elif x >= midpoint_x and y >= midpoint_y:
                quad4 += robot_grid[y][x]

    safety_factor = quad1 * quad2 * quad3 * quad4
    return safety_factor

input_file = "input.txt"
robot_positions = parse_input(input_file)

grid_width = 101
grid_height = 103
time_seconds = 100

safety_factor = calculate_safety_factor(robot_positions, grid_width, grid_height, time_seconds)
print("Safety factor after 100 seconds:", safety_factor)
