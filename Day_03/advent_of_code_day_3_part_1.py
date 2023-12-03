
puzzle_txt = "advent_of_code_day_3_puzzle.txt"

with open(puzzle_txt) as f:
    puzzle_input = [line.rstrip() for line in f]

puzzle_input = [a.split() for a in puzzle_input]
puzzle_input = [[char for char in item[0]] for item in puzzle_input]

calc_board_height = len(puzzle_input)  # 140
calc_board_width = len(puzzle_input[0])  # 140

symbols_coordinates = []

for x, row in enumerate(puzzle_input):
    for y, col in enumerate(row):
        if not col.isdigit() and not col == ".":
            symbols_coordinates.append((x, y))

"""
The matrix:
[x][x][x]
[x][o][x]
[x][x][x]
o - the symbol
x - all that its touching

Coordinates from the 'o' point (starting point)
[-1, -1][-1, 0][-1, 1]
[0, -1][0, 0][0, 1]
[1, -1][1, 0][1, 1]
"""

adjacent_coordinates = [
    (x - 1, y - 1),
    (x - 1, y),
    (x - 1, y + 1),

    (x, y - 1),
    # It does not need to point on itself
    (x, y + 1),

    (x + 1, y - 1),
    (x + 1, y),
    (x + 1, y + 1)
]


# print(puzzle_input)
