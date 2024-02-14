data = "input.txt"

with open(data) as f:
    data = [line.rstrip() for line in f]

solution = 0
for line in data:
    a, b = line.split(",")
    a1, a2 = map(int, a.split("-"))
    b1, b2 = map(int, b.split("-"))
    if (a1 <= b1 <= b2 <= a2) or (b1 <= a1 <= a2 <= b2):
        solution += 1

print("Part 1:", solution)
