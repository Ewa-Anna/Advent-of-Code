from itertools import combinations


with open("input.txt") as f:
    lines = f.read().strip().split("\n")
    boss_hp = int(lines[0].split(": ")[1])
    boss_damage = int(lines[1].split(": ")[1])
    boss_armor = int(lines[2].split(": ")[1])


weapons = [
    {"name": "Dagger", "cost": 8, "damage": 4, "armor": 0},
    {"name": "Shortsword", "cost": 10, "damage": 5, "armor": 0},
    {"name": "Warhammer", "cost": 25, "damage": 6, "armor": 0},
    {"name": "Longsword", "cost": 40, "damage": 7, "armor": 0},
    {"name": "Greataxe", "cost": 74, "damage": 8, "armor": 0}
]

armor = [
    {"name": "No Armor", "cost": 0, "damage": 0, "armor": 0},
    {"name": "Leather", "cost": 13, "damage": 0, "armor": 1},
    {"name": "Chainmail", "cost": 31, "damage": 0, "armor": 2},
    {"name": "Splintmail", "cost": 53, "damage": 0, "armor": 3},
    {"name": "Bandedmail", "cost": 75, "damage": 0, "armor": 4},
    {"name": "Platemail", "cost": 102, "damage": 0, "armor": 5}
]

rings = [
    {"name": "No Ring", "cost": 0, "damage": 0, "armor": 0},
    {"name": "Damage +1", "cost": 25, "damage": 1, "armor": 0},
    {"name": "Damage +2", "cost": 50, "damage": 2, "armor": 0},
    {"name": "Damage +3", "cost": 100, "damage": 3, "armor": 0},
    {"name": "Defense +1", "cost": 20, "damage": 0, "armor": 1},
    {"name": "Defense +2", "cost": 40, "damage": 0, "armor": 2},
    {"name": "Defense +3", "cost": 80, "damage": 0, "armor": 3}
]


def simulate_fight(player_hp, player_damage, player_armor, boss_hp, boss_damage, boss_armor):
    player_net_damage = max(1, player_damage - boss_armor)
    boss_net_damage = max(1, boss_damage - player_armor)

    player_turns_to_win = (boss_hp + player_net_damage - 1) // player_net_damage
    boss_turns_to_win = (player_hp + boss_net_damage - 1) // boss_net_damage

    return player_turns_to_win <= boss_turns_to_win

min_cost = float("inf")
for weapon in weapons:
    for arm in armor:
        for ring_combo in combinations(rings, 2):  
            total_cost = weapon["cost"] + arm["cost"] + ring_combo[0]["cost"] + ring_combo[1]["cost"]
            total_damage = weapon["damage"] + arm["damage"] + ring_combo[0]["damage"] + ring_combo[1]["damage"]
            total_armor = weapon["armor"] + arm["armor"] + ring_combo[0]["armor"] + ring_combo[1]["armor"]

            if simulate_fight(100, total_damage, total_armor, boss_hp, boss_damage, boss_armor):
                min_cost = min(min_cost, total_cost)

print("Minimum cost to win:", min_cost)
