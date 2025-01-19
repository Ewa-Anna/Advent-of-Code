def calculate_shortest_path(filename):
    with open(filename, "r") as file:
        directions = file.read().strip().split(", ")

    x, y = 0, 0
    direction = 0

    for step in directions:
        turn, distance = step[0], int(step[1:])

        if turn == "L":
            direction = (direction - 1) % 4
        elif turn == "R":
            direction = (direction + 1) % 4

        if direction == 0:  # North
            y += distance
        elif direction == 1:  # East
            x += distance
        elif direction == 2:  # South
            y -= distance
        elif direction == 3:  # West
            x -= distance

    return abs(x) + abs(y)


shortest_path = calculate_shortest_path("input.txt")
print(f"The shortest path to Easter Bunny HQ is {shortest_path} blocks.")
