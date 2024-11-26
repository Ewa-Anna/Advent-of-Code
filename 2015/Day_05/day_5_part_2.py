puzzle = "input.txt"

with open(puzzle) as f:
    puzzle_input = [line.rstrip() for line in f]


def is_nice(word):
    # a pair of any two letters that appears at least twice without overlapping
    has_pair = any(word[i : i + 2] in word[i + 2 :] for i in range(len(word) - 1))

    # at least one letter that repeats with exactly one letter in between
    has_repeat_with_gap = any(word[i] == word[i + 2] for i in range(len(word) - 2))

    return has_pair and has_repeat_with_gap


nice_count = sum(1 for word in puzzle_input if is_nice(word))

print(f"Nice words: {nice_count}")
