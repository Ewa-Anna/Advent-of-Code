from itertools import combinations
from day_21_part_1 import weapons, armor, boss_armor, boss_damage, boss_hp, rings, simulate_fight


max_cost = float("-inf")
for weapon in weapons:
    for arm in armor:
        for ring_combo in combinations(rings, 2):  
            total_cost = weapon["cost"] + arm["cost"] + ring_combo[0]["cost"] + ring_combo[1]["cost"]
            total_damage = weapon["damage"] + arm["damage"] + ring_combo[0]["damage"] + ring_combo[1]["damage"]
            total_armor = weapon["armor"] + arm["armor"] + ring_combo[0]["armor"] + ring_combo[1]["armor"]

            if not simulate_fight(100, total_damage, total_armor, boss_hp, boss_damage, boss_armor):
                max_cost = max(max_cost, total_cost)

print("Maximum cost to lose:", max_cost)