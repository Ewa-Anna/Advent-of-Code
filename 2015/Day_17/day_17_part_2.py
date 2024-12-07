from itertools import combinations
from day_17_part_1 import containers, target_volume


def min_container_combinations(containers, target):
    valid_combinations = []
    
    for r in range(1, len(containers) + 1):
        for combo in combinations(containers, r):
            if sum(combo) == target:
                valid_combinations.append(combo)
    
    min_containers = min(len(combo) for combo in valid_combinations)
    
    min_combinations_count = sum(1 for combo in valid_combinations if len(combo) == min_containers)
    
    return min_containers, min_combinations_count

min_containers, ways_to_fill_min = min_container_combinations(containers, target_volume)
print(min_containers, ways_to_fill_min)