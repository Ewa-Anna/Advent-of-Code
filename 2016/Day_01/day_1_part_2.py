def calculate_shortest_path(filename):
    with open(filename, "r") as file:
        directions = file.read().strip().split(", ")

    x, y = 0, 0
    direction = 0
    visited = set()
    visited.add((x, y))

    for step in directions:
        turn, distance = step[0], int(step[1:])

        if turn == "L":
            direction = (direction - 1) % 4
        elif turn == "R":
            direction = (direction + 1) % 4

        for _ in range(distance):
            if direction == 0:  # North
                y += 1
            elif direction == 1:  # East
                x += 1
            elif direction == 2:  # South
                y -= 1
            elif direction == 3:  # West
                x -= 1

            if (x, y) in visited:
                return abs(x) + abs(y)
            visited.add((x, y))

    return None


shortest_path = calculate_shortest_path("input.txt")
if shortest_path is not None:
    print(f"The first location visited twice is {shortest_path} blocks away.")
else:
    print("No location was visited twice.")
