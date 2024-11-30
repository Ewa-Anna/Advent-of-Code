from itertools import permutations


puzzle = "input.txt"

with open(puzzle) as f:
    raw_input = [line.strip().split() for line in f]

happiness = {}
for line in raw_input:
    person1 = line[0]
    person2 = line[-1].strip('.')
    change = int(line[3]) if line[2] == "gain" else -int(line[3])
    happiness[(person1, person2)] = change

guests = set(person for person, _ in happiness.keys())

def calculate_total_happiness(arrangement):
    total_happiness = 0
    for i in range(len(arrangement)):
        person1 = arrangement[i]
        person2 = arrangement[(i + 1) % len(arrangement)]  
        total_happiness += happiness.get((person1, person2), 0)
        total_happiness += happiness.get((person2, person1), 0)
    return total_happiness

optimal_happiness = float('-inf')
optimal_arrangement = None

for arrangement in permutations(guests):
    total_happiness = calculate_total_happiness(arrangement)
    if total_happiness > optimal_happiness:
        optimal_happiness = total_happiness
        optimal_arrangement = arrangement

print("Optimal Happiness:", optimal_happiness)
