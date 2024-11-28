from itertools import permutations


puzzle = "input.txt"

with open(puzzle) as f:
    puzzle_input = [line.rstrip() for line in f]


def parse_input(input_lines):
    distances = {}
    for line in input_lines:
        parts = line.split(" = ")
        locations = parts[0].split(" to ")
        distance = int(parts[1])
        loc1, loc2 = locations
        distances[(loc1, loc2)] = distance
        distances[(loc2, loc1)] = distance  
    return distances


def find_shortest_route(input_lines):
    distances = parse_input(input_lines)

    locations = set()
    for loc1, loc2 in distances.keys():
        locations.add(loc1)
        locations.add(loc2)

    shortest_distance = float('inf')

    for route in permutations(locations):
        route_distance = sum(
            distances[(route[i], route[i+1])] for i in range(len(route) - 1)
        )
        shortest_distance = min(shortest_distance, route_distance)

    return shortest_distance

shortest_distance = find_shortest_route(puzzle_input)
print("Shortest Distance:", shortest_distance)
