from itertools import combinations

puzzle = "input.txt"

with open(puzzle, "r") as file:
    raw_containers = file.read().splitlines()

containers = [int(i) for i in raw_containers]

target_volume = 150


def count_combinations(containers, target):
    count = 0
    for r in range(1, len(containers) + 1):
        for combo in combinations(containers, r):
            if sum(combo) == target:
                count += 1
    return count


result = count_combinations(containers, target_volume)
print(result)
