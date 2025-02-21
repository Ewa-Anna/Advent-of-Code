def parse_instruction(line):
    if line.startswith("rect"):
        _, size = line.split()
        a, b = map(int, size.split("x"))
        return ("rect", a, b)
    elif line.startswith("rotate row"):
        parts = line.split()
        y = int(parts[2].split("=")[1])
        by = int(parts[-1])
        return ("rotate_row", y, by)
    elif line.startswith("rotate column"):
        parts = line.split()
        x = int(parts[2].split("=")[1])
        by = int(parts[-1])
        return ("rotate_column", x, by)


def apply_instruction(screen, instruction):
    if instruction[0] == "rect":
        a, b = instruction[1], instruction[2]
        for y in range(b):
            for x in range(a):
                screen[y][x] = 1

    elif instruction[0] == "rotate_row":
        y, by = instruction[1], instruction[2]
        screen[y] = screen[y][-by:] + screen[y][:-by]

    elif instruction[0] == "rotate_column":
        x, by = instruction[1], instruction[2]
        col = [screen[y][x] for y in range(6)]
        col = col[-by:] + col[:-by]
        for y in range(6):
            screen[y][x] = col[y]


width, height = 50, 6
screen = [[0] * width for _ in range(height)]

with open("input.txt") as file:
    for line in file:
        instruction = parse_instruction(line.strip())
        apply_instruction(screen, instruction)

lit_pixels = sum(sum(row) for row in screen)
print(f"Number of lit pixels: {lit_pixels}")
