puzzle = "input.txt"

with open(puzzle) as f:
    raw_input = [line.strip().split() for line in f]

ingredients = {}

for line in raw_input:
    name = line[0][:-1]  
    capacity = int(line[2].strip(","))
    durability = int(line[4].strip(","))
    flavor = int(line[6].strip(","))
    texture = int(line[8].strip(","))
    calories = int(line[10])

    ingredients[name] = {
        "capacity": capacity,
        "durability": durability,
        "flavor": flavor,
        "texture": texture,
        "calories": calories
    }


def calculate_score(quantities, properties):
    total_capacity = max(0, sum(q * properties[i]["capacity"] for i, q in enumerate(quantities)))
    total_durability = max(0, sum(q * properties[i]["durability"] for i, q in enumerate(quantities)))
    total_flavor = max(0, sum(q * properties[i]["flavor"] for i, q in enumerate(quantities)))
    total_texture = max(0, sum(q * properties[i]["texture"] for i, q in enumerate(quantities)))
    return total_capacity * total_durability * total_flavor * total_texture

ingredient_names = list(ingredients.keys())
ingredient_properties = [ingredients[name] for name in ingredient_names]

total_teaspoons = 100

max_score = 0
for sprinkles in range(0, total_teaspoons + 1):
    for butterscotch in range(0, total_teaspoons - sprinkles + 1):
        for chocolate in range(0, total_teaspoons - sprinkles - butterscotch + 1):
            candy = total_teaspoons - sprinkles - butterscotch - chocolate
            quantities = [sprinkles, butterscotch, chocolate, candy]
            score = calculate_score(quantities, ingredient_properties)
            max_score = max(max_score, score)

print(max_score)
