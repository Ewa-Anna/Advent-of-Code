puzzle = "input.txt"

with open(puzzle) as f:
    grid = [list(line.strip()) for line in f]

word = "XMAS"

directions = [
    (0, 1),  # Right
    (0, -1),  # Left
    (1, 0),  # Down
    (-1, 0),  # Up
    (1, 1),  # Diagonal down-right
    (-1, -1),  # Diagonal up-left
    (1, -1),  # Diagonal down-left
    (-1, 1)  # Diagonal up-right
]


def count_word_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0
    
    def is_word_found(r, c, dr, dc):
        for i in range(word_len):
            nr, nc = r + dr * i, c + dc * i
            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != word[i]:
                return False
        return True

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if is_word_found(r, c, dr, dc):
                    count += 1

    return count

print(count_word_occurrences(grid, word))  
