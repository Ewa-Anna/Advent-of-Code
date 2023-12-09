import re

puzzle_txt = "advent_of_code_day_2_puzzle.txt"

with open(puzzle_txt) as f:
    puzzle_input = [line.rstrip() for line in f]

pattern1 = r'(1[3-9]|[2-9][0-9]|100) red'
pattern2 = r'(1[4-9]|[2-9][0-9]|100) green'
pattern3 = r'(1[5-9]|[2-9][0-9]|100) blue'
pattern4 = r'\:'


def bag_of_cubes(puzzle_input):
    list_of_bags = []
    for line in puzzle_input:
        result1 = bool(re.search(pattern1, line))  # red
        result2 = bool(re.search(pattern2, line))  # green
        result3 = bool(re.search(pattern3, line))  # blue

        if (result1 == False) and (result2 == False) and (result3 == False):
            list_of_bags.append(line)
    final_result = []
    for item in list_of_bags:
        # Search for index of where is colon
        colon = re.search(pattern4, item).start()
        # Slice the number starting from index 5 until colon 'Game XXX:'
        item = item[5:colon]
        final_result.append(item)
        # Change strings to integers
        final_result2 = [eval(i) for i in final_result]
        final_result2 = sum(final_result2)
    return final_result2


print(bag_of_cubes(puzzle_input))
