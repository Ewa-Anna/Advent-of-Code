puzzle = "advent_of_code_day_1_puzzle.txt"

with open(puzzle) as f:
    puzzle_input = [line.rstrip() for line in f]

puzzle_input = list(puzzle_input[0])

transformed_puzzle = ["1" if char == "(" else "-1" for char in puzzle_input]

string_to_int = [int(char) for char in transformed_puzzle]

floor = 0
position = 0

for i, change in enumerate(string_to_int):
    floor += change  
    if floor == -1:  
        position = i + 1  #
        break

print("First basement entry:", position)