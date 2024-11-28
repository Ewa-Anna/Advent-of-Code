from itertools import permutations
from day_9_part_1 import puzzle_input, parse_input


def find_longest_route(input_lines):
    distances = parse_input(input_lines)

    locations = set()
    for loc1, loc2 in distances.keys():
        locations.add(loc1)
        locations.add(loc2)

    longest_distance = 0

    for route in permutations(locations):
        route_distance = sum(
            distances[(route[i], route[i+1])] for i in range(len(route) - 1)
        )
        longest_distance = max(longest_distance, route_distance)

    return longest_distance

longest_distance = find_longest_route(puzzle_input)
print("Longest Distance:", longest_distance)
