data = "input.txt"

with open(data) as f:
    data = [line.rstrip() for line in f]

points = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

total_score = 0

for round_choice in data:
    if round_choice in points:
        total_score += points[round_choice]

print(total_score)
