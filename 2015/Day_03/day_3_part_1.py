puzzle = "input.txt"

with open(puzzle) as f:
    puzzle_input = [line.rstrip() for line in f]

puzzle_input = list(puzzle_input[0])

santa_position = (0, 0)

visited_houses = set()
visited_houses.add(santa_position)

for direction in puzzle_input:
    if direction == "^":
        santa_position = (santa_position[0], santa_position[1] + 1)
    elif direction == "v":
        santa_position = (santa_position[0], santa_position[1] - 1)
    elif direction == ">":
        santa_position = (santa_position[0] + 1, santa_position[1])
    elif direction == "<":
        santa_position = (santa_position[0] - 1, santa_position[1])

    visited_houses.add(santa_position)

print(len(visited_houses))
