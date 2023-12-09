puzzle_txt = "advent_of_code_day_4_puzzle.txt"

with open(puzzle_txt) as f:
    puzzle_input = [line.rstrip() for line in f]

puzzle_dict = dict(s.split(":") for s in puzzle_input)
puzzle_dict_with_lists = {}

for key, value in puzzle_dict.items():
    parts = value.split("|")
    puzzle_dict_with_lists[key] = [
        list(map(int, part.strip().split())) for part in parts]

for value in puzzle_dict_with_lists.values():
    matches_dict = {}
    for key, value in puzzle_dict_with_lists.items():
        number_of_matches = sum(item in value[1] for item in value[0])

        matches_dict[key] = number_of_matches

print(sum(2 ** (n - 1) for n in matches_dict.values() if n > 0))
