data = "input.txt"

with open(data) as f:
    data = [line.rstrip() for line in f]

points = {
    "A X": 0 + 3,
    "A Y": 3 + 1,
    "A Z": 6 + 2,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 0 + 2,
    "C Y": 3 + 3,
    "C Z": 6 + 1,
}

total_score = 0

for round_choice in data:
    if round_choice in points:
        total_score += points[round_choice]

print(total_score)
