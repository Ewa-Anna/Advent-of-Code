def find_bathroom_code(file_path):
    keypad = {
        (0, 2): "1",
        (1, 1): "2", (1, 2): "3", (1, 3): "4",
        (2, 0): "5", (2, 1): "6", (2, 2): "7", (2, 3): "8", (2, 4): "9",
        (3, 1): "A", (3, 2): "B", (3, 3): "C",
        (4, 2): "D"
    }

    moves = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    def get_next_position(pos, move):
        x, y = pos
        dx, dy = moves[move]
        nx, ny = x + dx, y + dy
        if (nx, ny) in keypad:
            return (nx, ny)
        return pos

    with open(file_path, "r") as file:
        instructions = file.readlines()

    code = []
    position = (2, 0)  # Start at "5"

    for line in instructions:
        for move in line.strip():
            position = get_next_position(position, move)
        code.append(keypad[position])

    return "".join(code)

print(find_bathroom_code("input.txt"))
