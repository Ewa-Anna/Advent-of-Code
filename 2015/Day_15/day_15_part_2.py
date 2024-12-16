from day_15_part_1 import ingredients


def calculate_score(amounts, ingredients):
    total_properties = {
        "capacity": 0,
        "durability": 0,
        "flavor": 0,
        "texture": 0,
        "calories": 0,
    }
    for ingredient, amount in zip(ingredients.keys(), amounts):
        for prop in total_properties:
            total_properties[prop] += ingredients[ingredient][prop] * amount
    total_properties = {k: max(0, v) for k, v in total_properties.items()}
    total_score = (
        total_properties["capacity"]
        * total_properties["durability"]
        * total_properties["flavor"]
        * total_properties["texture"]
    )
    return total_score, total_properties["calories"]


max_score = 0

for sprinkles in range(101):
    for butterscotch in range(101 - sprinkles):
        for chocolate in range(101 - sprinkles - butterscotch):
            candy = 100 - sprinkles - butterscotch - chocolate
            amounts = [sprinkles, butterscotch, chocolate, candy]
            score, calories = calculate_score(amounts, ingredients)
            if calories == 500:
                max_score = max(max_score, score)

print(max_score)
