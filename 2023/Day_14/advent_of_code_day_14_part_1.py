with open('advent_of_code_day_14_puzzle.txt', 'r') as file:
    lines = file.readlines()
total_lines = len(lines)
list_of_numbers = []

# rotate counterclockwise 90-degree on 2D grid
lines = list(map(''. join, zip(*lines)))
for _ in range(100):
    lines = [s.replace('.O', 'O.') for s in lines]

for _ in lines:
    line_number = next(enumerate(reversed(lines), start=1))
count_of_rocks = sum(line.count("O") for line in lines)
print(count_of_rocks)

