from day_4_part_1 import grid


def count_xmas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def matches_mas(d1, d2, d3):
        return (d1 + d2 + d3 == "MAS") or (d1 + d2 + d3 == "SAM")

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if matches_mas(grid[r - 1][c - 1], grid[r][c], grid[r + 1][c + 1]) and \
               matches_mas(grid[r - 1][c + 1], grid[r][c], grid[r + 1][c - 1]):
                count += 1

    return count

print(count_xmas_patterns(grid))