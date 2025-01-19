def is_valid_triangle(sides):
    a, b, c = sorted(sides)
    return a + b > c


def count_valid_triangles(filename):
    valid_count = 0

    with open(filename, "r") as file:
        for line in file:
            sides = list(map(int, line.split()))
            if is_valid_triangle(sides):
                valid_count += 1

    return valid_count


filename = "input.txt"
valid_triangles = count_valid_triangles(filename)
print(f"Number of valid triangles: {valid_triangles}")
