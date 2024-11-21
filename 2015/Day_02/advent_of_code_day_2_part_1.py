puzzle = "advent_of_code_day_2_puzzle.txt"

with open(puzzle) as f:
    puzzle_input = [line.rstrip() for line in f]

# Surface area = 2lw + 2wh + 2hl

total_paper = 0

for present in puzzle_input:
    l, w, h = map(int, present.split('x'))

    surface_area = 2 * l * w + 2 * w * h + 2 * h * l

    slack = min(l * w, w * h, h * l)

    total_paper_for_present = surface_area + slack
    total_paper += total_paper_for_present

print("Total paper:", total_paper)