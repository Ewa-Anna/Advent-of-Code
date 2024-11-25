puzzle = "input.txt"

with open(puzzle) as f:
    puzzle_input = [line.rstrip() for line in f]

puzzle_input = list(puzzle_input[0])

transformed_puzzle = ["1" if char == "(" else "-1" for char in puzzle_input]

string_to_int = [int(char) for char in transformed_puzzle]

print("Total floors: ", sum(string_to_int))
