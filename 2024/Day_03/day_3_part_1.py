import re


puzzle = "input.txt"

with open(puzzle, 'r') as f:
    lines = f.readlines()

corrupted_memory = "".join(lines)
pattern = r"mul\((\d+),(\d+)\)"

matches = re.findall(pattern, corrupted_memory)

results = [int(x) * int(y) for x, y in matches]
total_sum = sum(results)

print(total_sum)