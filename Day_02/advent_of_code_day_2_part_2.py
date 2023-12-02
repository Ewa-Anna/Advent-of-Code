puzzle_txt = "advent_of_code_day_2_puzzle.txt"

with open(puzzle_txt) as f:
    puzzle_input = [line.rstrip() for line in f]

# Change all semicolons to comma
puzzle_input = [s.replace(';', ',') for s in puzzle_input]

result = []

for game in puzzle_input:
    parts = game.split(":")

    key = parts[0].strip()  # Game is a key
    values = parts[1].strip()  # All cubes in game are values

    # Convert all cubes from string to be separate items in a list
    values_list = [x.strip() for x in values.split(',')]

    # Create dictionary to store
    count_dict = {}
    for item in values_list:
        # Split number from the color
        count, color = item.split()
        # Choose max number for each color and save it to count_dict
        count_dict[color] = max(count_dict.get(color, 0), int(count))

    # Convert dictionary to list containing only numbers
    result_list = [count for count in count_dict.values()]

    # Multiply each element of list by each other
    calc = 1
    for num in result_list:
        calc *= num

    # Add each number to the list
    result.append(calc)

# Sum numbers from result list
total_sum = sum(result)
print(total_sum)
