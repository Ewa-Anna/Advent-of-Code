from functools import lru_cache

def count_ways_to_form_design(available_patterns, design):
    @lru_cache(None)
    def dfs(design):
        if not design:
            return 1

        ways = 0
        for pattern in available_patterns:
            if design.startswith(pattern):
                ways += dfs(design[len(pattern):])
        return ways

    return dfs(design)

def total_ways_to_form_designs(patterns, designs):
    total_ways = 0
    for design in designs:
        total_ways += count_ways_to_form_design(tuple(patterns), design)
    return total_ways

with open("input.txt", "r") as file:
    data = file.read().strip().split("\n\n")

patterns = data[0].split(", ")
designs = data[1].split("\n")

result = total_ways_to_form_designs(patterns, designs)

print(f"Total number of ways to form all designs: {result}")
