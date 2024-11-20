import heapq

with open('advent_of_code_day_17_puzzle.txt', 'r') as file:
    lines = file.readlines()

# Directions: right, down, left, up
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def is_valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def find_min_heat_loss(grid):
    n = len(grid)
    m = len(grid[0])
    start = (0, 0, -1, 0)  # (row, col, direction, consecutive_steps)
    pq = [(0, start)]  # (total_heat_loss, (row, col, direction, consecutive_steps))
    visited = set()

    while pq:
        total_heat_loss, (row, col, dir_idx, steps) = heapq.heappop(pq)
        
        if (row, col, dir_idx, steps) in visited:
            continue
        
        visited.add((row, col, dir_idx, steps))

        if row == n - 1 and col == m - 1:
            return total_heat_loss
        
        for i, (dx, dy) in enumerate(directions):
            if i == dir_idx and steps < 3:
                new_row, new_col, new_steps = row + dx, col + dy, steps + 1
            else:
                new_row, new_col, new_steps = row + dx, col + dy, 1

            if is_valid(new_row, new_col, n, m):
                heapq.heappush(pq, (total_heat_loss + grid[new_row][new_col], (new_row, new_col, i, new_steps)))

    return float('inf')
