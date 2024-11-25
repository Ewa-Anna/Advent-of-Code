import re


puzzle = "input.txt"

with open(puzzle) as f:
    puzzle_input = [line.rstrip() for line in f]


def calculate_difference(strings):
    total_code = 0
    total_memory = 0

    for string in strings:
        code = string
        memory = string[1:-1]

        total_code += len(code)

        memory = memory.replace(r"\\", "\\")
        memory = memory.replace(r"\"", '"')
        memory = re.sub(r"\\x[0-9a-fA-F]{2}", ".", memory)

        total_memory += len(memory)

    return total_code - total_memory


difference = calculate_difference(puzzle_input)
print("Difference:", difference)
