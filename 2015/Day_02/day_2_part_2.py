puzzle = "input.txt"

with open(puzzle) as f:
    puzzle_input = [line.rstrip() for line in f]

total_ribbon = 0

for present in puzzle_input:
    l, w, h = map(int, present.split("x"))

    perimeters = [2 * l + 2 * w, 2 * w + 2 * h, 2 * h + 2 * l]

    wrap_ribbon = min(perimeters)

    bow_ribbon = l * w * h

    total_ribbon_for_present = wrap_ribbon + bow_ribbon
    total_ribbon += total_ribbon_for_present

print("Total feet of ribbon:", total_ribbon)
