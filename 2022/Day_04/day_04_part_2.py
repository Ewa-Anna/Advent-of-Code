data = "input.txt"

with open(data) as f:
    data = [line.rstrip() for line in f]

solution = 0
for line in data:
    a, b = line.split(",")
    a1, a2 = map(int, a.split("-"))
    b1, b2 = map(int, b.split("-"))
    if (a2 >= b1 and a1 <= b2) or (b2 >= a1 and b1 <= a2):
        solution += 1

print("Part 2:", solution)
