def calc_inner_area(steps):
    vertices = [(0, 0)]
    for instruction in steps:
        direction, distance, color = instruction
        distance = int(distance)
        x, y = vertices[-1]
        if direction == 'R':
            x += distance
        elif direction == 'L':
            x -= distance
        elif direction == 'U':
            y -= distance
        elif direction == 'D':
            y += distance
        vertices.append((x, y))

    # Schoelace formula
    area = 0.5 * abs(sum(x0*y1 - x1*y0 for (x0, y0), (x1, y1)
                     in zip(vertices, vertices[1:])))
    return area


def calc_perimeter(steps):
    x = 0
    for step in steps:
        _, distance, _ = step
        distance = int(distance)
        x += distance
    return x

# Reading file
steps = []
with open('data.txt', 'r') as file:
    lines = [line.rstrip() for line in file]

steps = [s.split(' ') for s in lines]

# Pick's theorem
# A - inner area
inner_area = calc_inner_area(steps)

# b - perimeter
perimeter = calc_perimeter(steps)

# i = A - b * 0.5 + 1
i = inner_area - perimeter * 0.5 + 1

# i + b - actual area
print(i + perimeter)
