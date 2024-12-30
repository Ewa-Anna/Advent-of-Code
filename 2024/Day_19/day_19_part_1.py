from functools import lru_cache

def can_form_design(available_patterns, design):
    @lru_cache(None)
    def dfs(design):
        if not design:
            return True

        for pattern in available_patterns:
            if design.startswith(pattern):
                if dfs(design[len(pattern):]):
                    return True
        return False

    return dfs(design)

def count_possible_designs(patterns, designs):
    possible_count = 0
    for design in designs:
        if can_form_design(tuple(patterns), design):
            possible_count += 1
    return possible_count

with open("input.txt", "r") as file:
    data = file.read().strip().split("\n\n")

patterns = data[0].split(", ")
designs = data[1].split("\n")

result = count_possible_designs(patterns, designs)

print(f"Number of possible designs: {result}")
