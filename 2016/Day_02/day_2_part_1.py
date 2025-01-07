def find_bathroom_code(file_path):
    keypad = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    
    moves = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    def get_next_position(pos, move):
        x, y = pos
        dx, dy = moves[move]
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            return (nx, ny)
        return pos

    with open(file_path, "r") as file:
        instructions = file.readlines()

    code = []
    position = (1, 1)  # Start at "5"

    for line in instructions:
        for move in line.strip():
            position = get_next_position(position, move)
        code.append(keypad[position[0]][position[1]])

    return "".join(code)

print(find_bathroom_code("input.txt"))
