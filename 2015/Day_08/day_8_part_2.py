import re


puzzle = "input.txt"

with open(puzzle) as f:
    puzzle_input = [line.rstrip() for line in f]


def calculate_encoded_difference(strings):
    total_original = 0
    total_encoded = 0

    for string in strings:
        total_original += len(string)

        encoded = string.replace("\\", "\\\\")
        encoded = encoded.replace('"', '\\"')
        encoded = f'"{encoded}"'

        total_encoded += len(encoded)

    return total_encoded - total_original


encoded_difference = calculate_encoded_difference(puzzle_input)
print("Encoded Difference:", encoded_difference)
