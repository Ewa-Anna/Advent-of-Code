puzzle = "input.txt"

with open(puzzle) as f:
    puzzle_input = [line.rstrip() for line in f]


def is_nice(word):
    # 1) at least 3 vowels 
    vowels = "aeiou"
    vowel_count = sum(1 for char in word if char in vowels)

    # 2) at least 1 double letter
    has_double = any(word[i] == word[i + 1] for i in range(len(word) - 1))

    # 3) does not contain ab, cd, pq, or xy
    disallowed = ["ab", "cd", "pq", "xy"]
    has_disallowed = any(sub in word for sub in disallowed)

    return vowel_count >= 3 and has_double and not has_disallowed

nice_count = sum(1 for word in puzzle_input if is_nice(word))

print(f"Nice words: {nice_count}")
