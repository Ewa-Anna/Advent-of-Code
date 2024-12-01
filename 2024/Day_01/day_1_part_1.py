puzzle = "input.txt"

with open(puzzle) as f:
    raw_input = [line.strip().split() for line in f]

left_column = [int(pair[0]) for pair in raw_input]
right_column = [int(pair[1]) for pair in raw_input]

sorted_left = sorted(left_column)
sorted_right = sorted(right_column)

zipped = zip(sorted_left, sorted_right)

differences = [abs(a - b) for a, b in zipped]
print(sum(differences))