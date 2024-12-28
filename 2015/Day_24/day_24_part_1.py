from itertools import combinations
from math import prod

def find_ideal_configuration(file_path):
    with open(file_path, 'r') as f:
        packages = [int(line.strip()) for line in f.readlines()]

    total_weight = sum(packages)
    if total_weight % 3 != 0:
        raise ValueError("Packages cannot be evenly divided into three groups.")
    target_weight = total_weight // 3

    for group_size in range(1, len(packages)):
        valid_groups = [
            group for group in combinations(packages, group_size)
            if sum(group) == target_weight
        ]
        if valid_groups:
            qes = [(prod(group), group) for group in valid_groups]
            qes.sort()
            return qes[0][0]

if __name__ == "__main__":
    result = find_ideal_configuration("input.txt")
    print("Quantum entanglement of the ideal configuration:", result)
