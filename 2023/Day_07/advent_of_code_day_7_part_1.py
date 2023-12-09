from collections import Counter

puzzle_txt = "advent_of_code_day_7_puzzle.txt"

data = []

with open(puzzle_txt) as f:
    puzzle_input = [line.rstrip() for line in f]
    for line in puzzle_input:
        pairs = line.strip().split()
        data.append(pairs)


def custom_sort(s):
    return ''.join(sorted(s, key=lambda x: (ord(x), x), reverse=True))


def score(i):
    counts = Counter(i[0])
    # XXXXX
    if len(counts) == 1:
        return 7
    # XXXXA or XXXAA
    if len(counts) == 2:
        # XXXXA
        if 4 in counts.values():
            return 6
        # XXXAA
        else:
            return 5
    # XXAAY or XXXAY
    if len(counts) == 3:
        # XXXAY
        if 3 in counts.values():
            return 4
        # XXAAY
        else:
            return 3
    # XX123
    if len(counts) == 4:
        return 2
    # 12345
    if len(counts) == 5:
        return 1


replacements = {'A': 'E', 'K': 'D', 'Q': 'C', 'J': 'B', 'T': 'A'}

translated_combinations = [
    [''.join(replacements.get(char, char)
             for char in combination[0]), combination[1]]
    for combination in data
]

sorted_data_with_score = sorted(
    translated_combinations, key=score, reverse=False)

sorted_data = [[custom_sort(item[0]), item[1]]
               for item in sorted_data_with_score]

final_sorted_data = sorted(sorted_data, key=lambda x: x[0], reverse=True)

result = sum(i * int(item[1])
             for i, item in enumerate(sorted_data_with_score[::-1], 1))

print(result)
