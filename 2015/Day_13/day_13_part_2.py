from itertools import permutations
from day_13_part_1 import calculate_total_happiness


puzzle = "input.txt"

with open(puzzle) as f:
    raw_input = [line.strip().split() for line in f]

happiness = {}
for line in raw_input:
    person1 = line[0]
    person2 = line[-1].strip(".")
    change = int(line[3]) if line[2] == "gain" else -int(line[3])
    happiness[(person1, person2)] = change


guests = set(person for person, _ in happiness.keys())

new_guest = "Me"
guests.add(new_guest)
for guest in list(guests):
    happiness[(new_guest, guest)] = 0
    happiness[(guest, new_guest)] = 0


optimal_happiness = float("-inf")
optimal_arrangement = None

for arrangement in permutations(guests):
    total_happiness = calculate_total_happiness(arrangement)
    if total_happiness > optimal_happiness:
        optimal_happiness = total_happiness
        optimal_arrangement = arrangement

print("Optimal Happiness", optimal_happiness)
